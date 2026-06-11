from __future__ import annotations

import json
import math
import os
import re
import shutil
import subprocess
import tempfile
import time
import unicodedata
import zipfile
from collections import Counter, deque
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "characters.json"
PETS_DIR = ROOT / "pets"
DOCS_DIR = ROOT / "docs"
SOURCE_DIR = DOCS_DIR / "assets" / "source"
OFFICIAL_SITE_DIR = DOCS_DIR / "assets" / "official"
PREVIEW_DIR = DOCS_DIR / "assets" / "previews"
SPRITESHEET_DIR = DOCS_DIR / "assets" / "spritesheets"
DOWNLOAD_DIR = DOCS_DIR / "downloads"
DATA_DIR = DOCS_DIR / "data"
ASSET_CACHE_DIR = Path(os.environ.get("REVERSE_1999_ASSET_DIR", r"C:\tmp\9pets-Reverse-1999-CN-Asset"))
LIVE2D_RENDER_DEPS = Path(os.environ.get("LIVE2D_RENDER_DEPS", r"C:\tmp\9pets-live2d-test"))
LIVE2D_CUBISM_CORE = Path(os.environ.get("LIVE2D_CUBISM_CORE", str(LIVE2D_RENDER_DEPS / "live2dcubismcore.min.js")))
LIVE2D_RENDER_ENABLED = os.environ.get("NINEPETS_RENDER_LIVE2D", "1") != "0"
LIVE2D_RENDER_SCRIPT = ROOT / "tools" / "render_live2d_frames.mjs"
LIVE2D_FRAME_ROOT = Path(tempfile.gettempdir()) / "9pets-live2d-frames"

CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9

STATE_ROWS = [
    ("idle", 6),
    ("running-right", 8),
    ("running-left", 8),
    ("waving", 4),
    ("jumping", 5),
    ("failed", 8),
    ("waiting", 6),
    ("running", 6),
    ("review", 6),
]

OFFICIAL_ROLE_URL = "https://re.bluepoch.com/home/img/role/{asset_id}m.png"
OFFICIAL_THUMB_URL = "https://re.bluepoch.com/home/img/character/{asset_id}.png"
ASSET_REPO_URL = "https://github.com/myssal/Reverse-1999-CN-Asset"
ASSET_RAW_BASE = "https://raw.githubusercontent.com/myssal/Reverse-1999-CN-Asset/master"
ASSET_TREE_BASE = "https://github.com/myssal/Reverse-1999-CN-Asset/tree/master"
ASSET_MAP_URL = f"{ASSET_RAW_BASE}/mappings/ArcanistMap.json"
OFFICIAL_SOURCE_TYPE = "official-sourced"
OFFICIAL_NAME_ALIASES = {
    "37": "Thirty-seven",
    "6": "Six",
    "J": "Joe",
    "Jessica": "Changeling",
    "Kaalaa Baunaa": "Black Dwarf",
    "Liang Yue": "Liang",
    "Matilda": "Matilda Bouanich",
}
MANUAL_OFFICIAL_ASSETS = {
    "Avgust": {
        "assetId": 307801,
        "spinePath": "roles/v1a8_307801_afuxiwei",
        "cubismPath": "live2d/roles/v1a8_307801_afuxiwei",
    },
    "Vila": {
        "assetId": 308701,
        "spinePath": "roles/v1a8_308701_weila",
        "cubismPath": "live2d/roles/v1a8_308701_weila",
    },
    "Yenisei": {
        "assetId": 308201,
        "spinePath": "roles/v1a6_308201_xiaoyenisai",
        "cubismPath": "live2d/roles/v1a6_308201_xiaoyenisai",
    },
    "Zima": {
        "assetId": 301301,
        "spinePath": "roles/301301_dong",
        "cubismPath": "",
    },
}
OFFICIAL_IMAGE_PATHS = [
    "singlebg/store/skin/{asset_id}.png",
    "singlebg/handbookheroicon/{asset_id}.png",
    "singlebg/headicon_img/{asset_id}.png",
]
OFFICIAL_SITE_ASSETS = {
    "logo.png": "https://re.bluepoch.com/home/img/logo.png",
    "hero-v2.webp": "https://re.bluepoch.com/home/img/v2.webp",
    "hero-v2c.png": "https://re.bluepoch.com/home/img/v2c.png",
    "site-bg.png": "https://re.bluepoch.com/home/img/BG.png",
    "site-bg-2.png": "https://re.bluepoch.com/home/img/BG2.png",
    "main-visual.jpg": "https://re.bluepoch.com/home/img/01.jpg",
    "first-panel-1.png": "https://re.bluepoch.com/home/img/first/1.png",
    "first-panel-2.png": "https://re.bluepoch.com/home/img/first/2.png",
    "first-panel-3.webp": "https://re.bluepoch.com/home/img/first/3.webp",
    "download-panel-3.png": "https://re.bluepoch.com/home/img/first/pc3.png",
    "download-panel-4.png": "https://re.bluepoch.com/home/img/first/pc4.png",
    "news-title.png": "https://re.bluepoch.com/home/img/News.png",
    "see.png": "https://re.bluepoch.com/home/img/see.png",
    "arrow.png": "https://re.bluepoch.com/home/img/jian.png",
    "role-frame.webp": "https://re.bluepoch.com/home/img/role/false.webp",
}


def read_catalog() -> dict[str, Any]:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def slug_suffix(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    text = text.replace("&", "and")
    tokens = re.findall(r"[A-Za-z0-9]+", text)
    return "-".join(tokens) or "Character"


def slug_lower(name: str) -> str:
    return slug_suffix(name).lower()


def normalized_lookup_name(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def pet_id_from_package(package_name: str) -> str:
    return package_name.lower()


def crop_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda p: 255 if p > 8 else 0).getbbox()
    if bbox:
        return rgba.crop(bbox)

    bg = Image.new("RGBA", rgba.size, rgba.getpixel((0, 0)))
    diff = ImageChops.difference(rgba, bg)
    bbox = diff.getbbox()
    return rgba.crop(bbox) if bbox else rgba


def squared_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum((a[index] - b[index]) ** 2 for index in range(3))


def remove_edge_background(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    if alpha.getextrema()[0] < 12:
        return rgba

    width, height = rgba.size
    pixels = rgba.load()
    samples: list[tuple[int, int, int]] = []
    for x in range(0, width, 6):
        samples.append(pixels[x, 0][:3])
        samples.append(pixels[x, height - 1][:3])
    for y in range(0, height, 6):
        samples.append(pixels[0, y][:3])
        samples.append(pixels[width - 1, y][:3])

    def quantized(color: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple((channel // 8) * 8 for channel in color)

    background_colors = [color for color, _ in Counter(quantized(color) for color in samples).most_common(8)]
    threshold = 36 * 36

    def is_background(x: int, y: int) -> bool:
        pixel = pixels[x, y]
        if pixel[3] < 12:
            return True
        rgb = pixel[:3]
        return any(squared_distance(rgb, color) <= threshold for color in background_colors)

    queue: deque[tuple[int, int]] = deque()
    visited = bytearray(width * height)

    def enqueue(x: int, y: int) -> None:
        index = y * width + x
        if not visited[index] and is_background(x, y):
            visited[index] = 1
            queue.append((x, y))

    for x in range(width):
        enqueue(x, 0)
        enqueue(x, height - 1)
    for y in range(height):
        enqueue(0, y)
        enqueue(width - 1, y)

    output = rgba.copy()
    output_pixels = output.load()
    while queue:
        x, y = queue.popleft()
        output_pixels[x, y] = (0, 0, 0, 0)
        if x > 0:
            enqueue(x - 1, y)
        if x < width - 1:
            enqueue(x + 1, y)
        if y > 0:
            enqueue(x, y - 1)
        if y < height - 1:
            enqueue(x, y + 1)

    return output


def crop_and_fit(image: Image.Image, max_width: int = 174, max_height: int = 198) -> Image.Image:
    cropped = crop_alpha(remove_edge_background(image))
    scale = min(max_width / cropped.width, max_height / cropped.height, 1.0)
    size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    return cropped.resize(size, Image.Resampling.LANCZOS)


def download_image(url: str, output: Path, referer: str | None = None) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        headers = {"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"}
        if referer:
            headers["Referer"] = referer
        response = requests.get(url, timeout=20, headers=headers)
        if response.status_code != 200:
            return False
        image = remove_edge_background(Image.open(BytesIO(response.content)).convert("RGBA"))
        for attempt in range(8):
            try:
                image.save(output)
                return True
            except PermissionError:
                if attempt == 7:
                    return False
                time.sleep(0.35)
        return False
    except Exception:
        return False


def download_binary(url: str, output: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, timeout=12, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"})
        if response.status_code != 200:
            return False
        output.write_bytes(response.content)
        return True
    except Exception:
        return False


def download_official_site_assets() -> dict[str, str]:
    assets: dict[str, str] = {}
    for filename, url in OFFICIAL_SITE_ASSETS.items():
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    for asset_id in range(1, 11):
        filename = f"character-{asset_id}.png"
        url = OFFICIAL_THUMB_URL.format(asset_id=asset_id)
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    for asset_id in range(1, 11):
        filename = f"role-{asset_id}.png"
        url = OFFICIAL_ROLE_URL.format(asset_id=asset_id)
        output = OFFICIAL_SITE_DIR / filename
        if download_binary(url, output):
            assets[filename] = url

    return assets


def repo_raw_url(path: str) -> str:
    return f"{ASSET_RAW_BASE}/{path}"


def repo_tree_url(path: str) -> str:
    return f"{ASSET_TREE_BASE}/{path}" if path else ""


def repo_path_from_tree_url(url: str) -> str:
    marker = "/tree/master/"
    if marker not in url:
        return ""
    return url.split(marker, 1)[1]


def local_asset_path(repo_path: str) -> Path:
    return ASSET_CACHE_DIR / repo_path if repo_path else Path()


def live2d_render_ready(cubism_path: str) -> bool:
    model_dir = local_asset_path(cubism_path)
    return (
        LIVE2D_RENDER_ENABLED
        and bool(cubism_path)
        and model_dir.exists()
        and any(model_dir.glob("*.model3.json"))
        and LIVE2D_RENDER_SCRIPT.exists()
        and LIVE2D_RENDER_DEPS.exists()
        and LIVE2D_CUBISM_CORE.exists()
    )


def live2d_model_cached(cubism_path: str) -> bool:
    model_dir = local_asset_path(cubism_path)
    return bool(cubism_path) and model_dir.exists() and any(model_dir.glob("*.model3.json"))


def render_live2d_frames(package_name: str, cubism_path: str) -> Path | None:
    if not live2d_render_ready(cubism_path):
        return None

    output_dir = LIVE2D_FRAME_ROOT / package_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    model_dir = local_asset_path(cubism_path)
    command = [
        "node",
        str(LIVE2D_RENDER_SCRIPT),
        "--model-dir",
        str(model_dir),
        "--output",
        str(output_dir),
        "--deps-dir",
        str(LIVE2D_RENDER_DEPS),
        "--cubism-core",
        str(LIVE2D_CUBISM_CORE),
    ]
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=240, check=False)
    if completed.returncode != 0:
        print(f"Live2D render failed for {package_name}: {completed.stderr.strip() or completed.stdout.strip()}", flush=True)
        return None
    return output_dir


def load_official_asset_index() -> dict[str, dict[str, Any]]:
    response = requests.get(ASSET_MAP_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/2.0"})
    if response.status_code != 200:
        raise RuntimeError(f"Could not download official asset mapping: HTTP {response.status_code}")
    index: dict[str, dict[str, Any]] = {}
    for entry in response.json():
        key = normalized_lookup_name(entry.get("nameEng", ""))
        if key:
            index[key] = entry
    return index


def resolve_official_asset(name: str, official_index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    manual = MANUAL_OFFICIAL_ASSETS.get(name)
    if manual:
        return {
            "assetId": manual["assetId"],
            "spinePath": manual.get("spinePath", ""),
            "cubismPath": manual.get("cubismPath", ""),
            "matchedName": name,
            "birthday": "",
            "skinName": "Default",
        }

    lookup_name = OFFICIAL_NAME_ALIASES.get(name, name)
    entry = official_index.get(normalized_lookup_name(lookup_name))
    if not entry or not entry.get("live2d"):
        raise RuntimeError(f"No official asset mapping found for {name}")
    skins = entry["live2d"]

    def has_cached_model(skin_entry: dict[str, Any]) -> bool:
        cubism_path = repo_path_from_tree_url(skin_entry.get("cubism", ""))
        return live2d_model_cached(cubism_path)

    skin = next((candidate for candidate in skins if has_cached_model(candidate)), skins[0])
    return {
        "assetId": skin["id"],
        "spinePath": repo_path_from_tree_url(skin.get("spine", "")),
        "cubismPath": repo_path_from_tree_url(skin.get("cubism", "")),
        "matchedName": lookup_name,
        "birthday": entry.get("roleBirthday", ""),
        "skinName": skin.get("characterSkinNameEng") or "Default",
    }


def download_official_source_image(asset_id: int, source_path: Path) -> tuple[str, str]:
    for template in OFFICIAL_IMAGE_PATHS:
        repo_path = template.format(asset_id=asset_id)
        url = repo_raw_url(repo_path)
        if download_image(url, source_path):
            return repo_path, url
    raise RuntimeError(f"No official source image found for asset id {asset_id}")


def get_source_sprite(name: str, package_name: str, official_index: dict[str, dict[str, Any]]) -> tuple[Image.Image, dict[str, Any]]:
    asset = resolve_official_asset(name, official_index)
    source_path = SOURCE_DIR / f"{package_name}.png"
    image_repo_path, source_url = download_official_source_image(int(asset["assetId"]), source_path)
    sprite = crop_and_fit(Image.open(source_path).convert("RGBA"), max_width=180, max_height=200)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    source_info = {
        "sourceType": OFFICIAL_SOURCE_TYPE,
        "sourceUrl": source_url,
        "sourceImage": f"assets/source/{package_name}.png",
        "sourceRepoPath": image_repo_path,
        "assetId": str(asset["assetId"]),
        "assetRepoUrl": ASSET_REPO_URL,
        "spinePath": spine_path,
        "cubismPath": cubism_path,
        "spineUrl": repo_tree_url(spine_path),
        "cubismUrl": repo_tree_url(cubism_path),
        "birthday": asset.get("birthday", ""),
        "skinName": asset.get("skinName", "Default"),
        "matchedName": asset.get("matchedName", name),
        "live2dCacheStatus": "cached" if live2d_model_cached(cubism_path) else ("mapped" if cubism_path else "none"),
        "animationMode": "official-art-elastic-rig",
        "animationModeLabel": "Official art atlas; Live2D path mapped",
    }
    return sprite, source_info


def transformed(
    sprite: Image.Image,
    *,
    scale: float = 1.0,
    scale_x: float = 1.0,
    scale_y: float = 1.0,
    angle: float = 0.0,
    flip: bool = False,
    opacity: float = 1.0,
) -> Image.Image:
    image = sprite
    if flip:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    width_scale = scale * scale_x
    height_scale = scale * scale_y
    if width_scale != 1.0 or height_scale != 1.0:
        size = (max(1, round(image.width * width_scale)), max(1, round(image.height * height_scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)
    if angle:
        image = image.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    if opacity < 1.0:
        alpha = image.getchannel("A").point(lambda p: round(p * opacity))
        image = image.copy()
        image.putalpha(alpha)
    return image


def frame_motion(state: str, frame: int, total: int) -> dict[str, Any]:
    phase = frame / max(total, 1)
    wave = math.sin(phase * math.tau)
    if state == "idle":
        return {"scale_x": 1.0 - 0.01 * abs(wave), "scale_y": 1.0 + 0.018 * abs(wave), "angle": 1.8 * wave, "x": 0, "y": round(-4 * abs(wave)), "flip": False}
    if state == "running-right":
        return {"scale_x": [1.04, 1.0, 0.98, 1.03, 1.06, 1.0, 0.97, 1.02][frame], "scale_y": [0.96, 1.02, 1.04, 0.98, 0.95, 1.03, 1.04, 0.99][frame], "angle": [-8, -3, 4, 8, 3, -5, -9, -2][frame], "x": [-17, -11, -4, 5, 13, 17, 8, -6][frame], "y": [4, -4, -2, -6, 2, -5, -1, 3][frame], "flip": False}
    if state == "running-left":
        return {"scale_x": [1.04, 1.0, 0.98, 1.03, 1.06, 1.0, 0.97, 1.02][frame], "scale_y": [0.96, 1.02, 1.04, 0.98, 0.95, 1.03, 1.04, 0.99][frame], "angle": [8, 3, -4, -8, -3, 5, 9, 2][frame], "x": [17, 11, 4, -5, -13, -17, -8, 6][frame], "y": [4, -4, -2, -6, 2, -5, -1, 3][frame], "flip": True}
    if state == "waving":
        return {"scale_x": [1.0, 0.98, 1.02, 1.0][frame], "scale_y": [1.0, 1.03, 0.99, 1.0][frame], "angle": [0, -12, 11, 2][frame], "x": [0, -6, 6, 1][frame], "y": [0, -8, -5, 0][frame], "flip": False}
    if state == "jumping":
        return {"scale_x": [1.08, 0.98, 0.95, 0.99, 1.06][frame], "scale_y": [0.91, 1.05, 1.09, 1.03, 0.94][frame], "angle": [0, -6, 3, 6, -2][frame], "x": [0, -3, 1, 4, 0][frame], "y": [10, -20, -42, -18, 6][frame], "flip": False}
    if state == "failed":
        return {"scale_x": [1.0, 1.03, 1.08, 1.05, 1.1, 1.07, 1.03, 1.0][frame], "scale_y": [1.0, 0.96, 0.89, 0.92, 0.86, 0.9, 0.95, 1.0][frame], "angle": [0, 9, -8, 13, -12, 8, -4, 0][frame], "x": [0, 3, -5, 5, -6, 4, -2, 0][frame], "y": [8, 14, 22, 18, 25, 20, 14, 8][frame], "flip": False, "opacity": [1, 0.95, 0.9, 0.94, 0.88, 0.92, 0.97, 1][frame]}
    if state == "waiting":
        return {"scale_x": [1.0, 0.99, 0.98, 1.02, 1.01, 1.0][frame], "scale_y": [1.0, 1.02, 1.04, 1.01, 0.99, 1.0][frame], "angle": [0, -4, -7, 6, 3, 0][frame], "x": [0, -3, -5, 4, 2, 0][frame], "y": [0, -4, -8, -5, -2, 1][frame], "flip": False}
    if state == "running":
        return {"scale_x": [1.0, 1.02, 0.98, 1.03, 0.99, 1.0][frame], "scale_y": [1.0, 0.98, 1.04, 0.97, 1.03, 1.0][frame], "angle": [0, -5, 4, -4, 5, 0][frame], "x": [0, -4, 3, -3, 4, 0][frame], "y": [-1, -7, -2, -8, -3, -1][frame], "flip": False}
    if state == "review":
        return {"scale_x": [1.0, 1.01, 1.02, 1.01, 0.99, 1.0][frame], "scale_y": [1.0, 1.02, 1.03, 1.02, 1.0, 0.99][frame], "angle": [0, -4, -6, -3, 1, 0][frame], "x": [0, -4, -7, -4, 1, 0][frame], "y": [0, -3, -6, -3, 0, 1][frame], "flip": False}
    return {"scale": 1.0, "angle": 0, "x": 0, "y": 0, "flip": False}


def alpha_composite_clipped(target: Image.Image, source: Image.Image, pos: tuple[int, int]) -> None:
    x, y = pos
    src_x0 = max(0, -x)
    src_y0 = max(0, -y)
    src_x1 = min(source.width, target.width - x)
    src_y1 = min(source.height, target.height - y)
    if src_x1 <= src_x0 or src_y1 <= src_y0:
        return
    crop = source.crop((src_x0, src_y0, src_x1, src_y1))
    target.alpha_composite(crop, (max(x, 0), max(y, 0)))


def make_cell(sprite: Image.Image, state: str, frame: int, total: int) -> Image.Image:
    motion = frame_motion(state, frame, total)
    image = transformed(
        sprite,
        scale=motion.get("scale", 1.0),
        scale_x=motion.get("scale_x", 1.0),
        scale_y=motion.get("scale_y", 1.0),
        angle=motion.get("angle", 0.0),
        flip=motion.get("flip", False),
        opacity=motion.get("opacity", 1.0),
    )
    cell = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    x = round((CELL_W - image.width) / 2 + motion.get("x", 0))
    y = round(CELL_H - image.height - 8 + motion.get("y", 0))
    alpha_composite_clipped(cell, image, (x, y))
    return cell


def make_atlas(sprite: Image.Image) -> Image.Image:
    atlas = Image.new("RGBA", (CELL_W * COLS, CELL_H * ROWS), (0, 0, 0, 0))
    for row, (state, frames) in enumerate(STATE_ROWS):
        for col in range(frames):
            cell = make_cell(sprite, state, col, frames)
            atlas.alpha_composite(cell, (col * CELL_W, row * CELL_H))
    return atlas


def union_bbox(a: tuple[int, int, int, int] | None, b: tuple[int, int, int, int] | None) -> tuple[int, int, int, int] | None:
    if not a:
        return b
    if not b:
        return a
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def make_live2d_cell(frame: Image.Image, bbox: tuple[int, int, int, int], scale: float, flip: bool = False) -> Image.Image:
    image = frame.convert("RGBA").crop(bbox)
    if flip:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    image = image.resize(size, Image.Resampling.LANCZOS)
    cell = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    x = round((CELL_W - image.width) / 2)
    y = round(CELL_H - image.height - 6)
    alpha_composite_clipped(cell, image, (x, y))
    return cell


def make_atlas_from_live2d_frames(frames_root: Path) -> Image.Image:
    loaded: dict[str, list[Image.Image]] = {}
    bbox: tuple[int, int, int, int] | None = None
    for state, frame_count in STATE_ROWS:
        state_dir = frames_root / state
        frames: list[Image.Image] = []
        for index in range(frame_count):
            frame_path = state_dir / f"{index:02d}.png"
            if not frame_path.exists():
                raise RuntimeError(f"Missing Live2D frame {frame_path}")
            frame = Image.open(frame_path).convert("RGBA")
            frames.append(frame)
            bbox = union_bbox(bbox, frame.getchannel("A").getbbox())
        loaded[state] = frames

    if not bbox:
        raise RuntimeError(f"Live2D frames are empty under {frames_root}")
    bbox_width = max(1, bbox[2] - bbox[0])
    bbox_height = max(1, bbox[3] - bbox[1])
    scale = min(178 / bbox_width, 198 / bbox_height, 1.0)
    atlas = Image.new("RGBA", (CELL_W * COLS, CELL_H * ROWS), (0, 0, 0, 0))
    for row, (state, frame_count) in enumerate(STATE_ROWS):
        for col in range(frame_count):
            cell = make_live2d_cell(loaded[state][col], bbox, scale, flip=state == "running-left")
            atlas.alpha_composite(cell, (col * CELL_W, row * CELL_H))
    return atlas


def make_preview_from_atlas(atlas: Image.Image, output: Path) -> None:
    preview = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    preview.alpha_composite(atlas.crop((0, 0, CELL_W, CELL_H)))
    output.parent.mkdir(parents=True, exist_ok=True)
    preview.save(output)


def make_pet_json(package_name: str, name: str, source_info: dict[str, Any]) -> dict[str, str]:
    if source_info.get("animationMode") == "official-live2d-cubism":
        description = f"A fan-made Reverse: 1999 Codex pet for {name}, built from official Live2D Cubism motion frames."
    else:
        description = f"A fan-made Reverse: 1999 Codex pet for {name}, built from official game asset-dump artwork."
    return {
        "id": pet_id_from_package(package_name),
        "displayName": f"9Pets - {name}",
        "description": description,
        "spritesheetPath": "spritesheet.webp",
    }


def write_zip(package_name: str, pet_json: dict[str, str], spritesheet_path: Path, zip_path: Path, source_info: dict[str, Any]) -> int:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    readme = "\n".join(
        [
            f"# {package_name}",
            "",
            "Fan-made Codex pet package for Reverse: 1999.",
            f"Source mode: {source_info['sourceType']}.",
            f"Animation mode: {source_info.get('animationModeLabel', source_info.get('animationMode', 'Unknown'))}.",
            f"Official asset id: {source_info['assetId']}.",
            f"Source image: {source_info['sourceUrl']}.",
            f"Spine assets: {source_info['spineUrl'] or 'No mapped Spine path.'}",
            f"Live2D assets: {source_info['cubismUrl'] or 'No mapped Live2D path.'}",
            "",
            "Install by copying the package folder contents into your Codex pets directory.",
            "",
        ]
    )
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        prefix = package_name
        archive.writestr(f"{prefix}/pet.json", json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n")
        archive.write(spritesheet_path, f"{prefix}/spritesheet.webp")
        archive.writestr(f"{prefix}/README.md", readme)
    return zip_path.stat().st_size


def clean_output_dirs() -> None:
    for path in [PETS_DIR, SOURCE_DIR, OFFICIAL_SITE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]:
        if path.exists():
            for attempt in range(8):
                try:
                    shutil.rmtree(path)
                    break
                except PermissionError:
                    if attempt == 7:
                        print(f"Warning: could not fully clean locked output path {path}; overwriting build outputs in place.", flush=True)
                    else:
                        time.sleep(0.35)
    for path in [PETS_DIR, SOURCE_DIR, OFFICIAL_SITE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def build() -> None:
    catalog = read_catalog()
    clean_output_dirs()
    official_site_assets = download_official_site_assets()
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    official_index = load_official_asset_index()
    pets: list[dict[str, Any]] = []

    for index, item in enumerate(catalog["characters"], start=1):
        name = item["name"]
        package_name = f"9Pets-{slug_suffix(name)}"
        package_dir = PETS_DIR / package_name
        package_dir.mkdir(parents=True, exist_ok=True)

        sprite, source_info = get_source_sprite(name, package_name, official_index)
        live2d_frames = render_live2d_frames(package_name, source_info.get("cubismPath", ""))
        if live2d_frames:
            try:
                atlas = make_atlas_from_live2d_frames(live2d_frames)
                source_info["animationMode"] = "official-live2d-cubism"
                source_info["animationModeLabel"] = "Official Live2D Cubism motion capture"
                source_info["live2dCacheStatus"] = "rendered"
            except Exception as error:
                print(f"Live2D atlas compose failed for {package_name}: {error}", flush=True)
                atlas = make_atlas(sprite)
                source_info["live2dCacheStatus"] = "compose-failed"
        else:
            atlas = make_atlas(sprite)
        spritesheet_path = package_dir / "spritesheet.webp"
        atlas.save(spritesheet_path, format="WEBP", lossless=True, quality=100, method=0)

        pet_json = make_pet_json(package_name, name, source_info)
        (package_dir / "pet.json").write_text(json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        docs_spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
        shutil.copy2(spritesheet_path, docs_spritesheet)
        preview_path = PREVIEW_DIR / f"{package_name}.png"
        make_preview_from_atlas(atlas, preview_path)

        zip_path = DOWNLOAD_DIR / f"{package_name}.zip"
        package_bytes = write_zip(package_name, pet_json, spritesheet_path, zip_path, source_info)

        pets.append(
            {
                "id": pet_json["id"],
                "packageName": package_name,
                "displayName": name,
                "download": f"downloads/{package_name}.zip",
                "preview": f"assets/previews/{package_name}.png",
                "spritesheet": f"assets/spritesheets/{package_name}.webp",
                "sourceType": source_info["sourceType"],
                "sourceUrl": source_info["sourceUrl"],
                "sourceImage": source_info["sourceImage"],
                "sourceRepoPath": source_info["sourceRepoPath"],
                "assetId": source_info["assetId"],
                "assetRepoUrl": source_info["assetRepoUrl"],
                "spinePath": source_info["spinePath"],
                "spineUrl": source_info["spineUrl"],
                "cubismPath": source_info["cubismPath"],
                "cubismUrl": source_info["cubismUrl"],
                "birthday": source_info["birthday"],
                "skinName": source_info["skinName"],
                "matchedName": source_info["matchedName"],
                "live2dCacheStatus": source_info["live2dCacheStatus"],
                "animationMode": source_info["animationMode"],
                "animationModeLabel": source_info["animationModeLabel"],
                "characterSummary": (
                    f"{name} is tracked as an official-sourced Reverse: 1999 character package. "
                    f"This build maps asset id {source_info['assetId']} to the game asset dump"
                    + (" and uses captured Live2D motion frames for the pet atlas." if source_info["animationMode"] == "official-live2d-cubism" else " with mapped Live2D or Spine paths where available.")
                ),
                "packageBytes": package_bytes,
            }
        )
        if index == 1 or index % 10 == 0 or index == len(catalog["characters"]):
            print(f"[{index}/{len(catalog['characters'])}] {package_name}", flush=True)

    site_data = {
        "generatedAt": generated_at,
        "total": len(pets),
        "sources": catalog["sources"],
        "notes": catalog["notes"],
        "officialSiteAssets": official_site_assets,
        "pets": pets,
    }
    (DATA_DIR / "pets.json").write_text(json.dumps(site_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    data_js = "window.NINEPETS_DATA = " + json.dumps(site_data, ensure_ascii=False) + ";\n"
    (DATA_DIR / "pets-data.js").write_text(data_js, encoding="utf-8")
    print(f"Generated {len(pets)} pets into {PETS_DIR}")
    print(f"Generated site data into {DATA_DIR / 'pets.json'}")


if __name__ == "__main__":
    build()
