from __future__ import annotations

import colorsys
import hashlib
import json
import math
import re
import shutil
import unicodedata
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageChops, ImageDraw, ImageFont


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
OFFICIAL_SITE_ASSETS = {
    "logo.png": "https://re.bluepoch.com/home/img/logo.png",
    "hero-v2.webp": "https://re.bluepoch.com/home/img/v2.webp",
    "first-panel-1.png": "https://re.bluepoch.com/home/img/first/1.png",
    "first-panel-2.png": "https://re.bluepoch.com/home/img/first/2.png",
    "first-panel-3.webp": "https://re.bluepoch.com/home/img/first/3.webp",
    "news-title.png": "https://re.bluepoch.com/home/img/News.png",
    "role-frame.webp": "https://re.bluepoch.com/home/img/role/false.webp",
}


def read_catalog() -> dict[str, Any]:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def slug_suffix(name: str) -> str:
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    text = text.replace("&", "and")
    tokens = re.findall(r"[A-Za-z0-9]+", text)
    return "-".join(tokens) or "Character"


def pet_id_from_package(package_name: str) -> str:
    return package_name.lower()


def digest_int(text: str) -> int:
    return int.from_bytes(hashlib.sha256(text.encode("utf-8")).digest()[:8], "big")


def color_from_hash(seed: int, offset: int = 0) -> tuple[int, int, int]:
    hue = ((seed >> (offset * 9)) % 360) / 360.0
    saturation = 0.42 + ((seed >> (offset * 5)) % 24) / 100.0
    lightness = 0.42 + ((seed >> (offset * 7)) % 20) / 100.0
    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    return (round(r * 255), round(g * 255), round(b * 255))


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/seguisb.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


FONT_BIG = load_font(54, bold=True)
FONT_MEDIUM = load_font(28, bold=True)
FONT_SMALL = load_font(16)


def initials(name: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", name)
    if not tokens:
        return "?"
    if len(tokens) == 1:
        token = tokens[0]
        return token[:3].upper() if len(token) <= 3 else token[:2].upper()
    return "".join(token[0] for token in tokens[:3]).upper()


def draw_centered_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, font: ImageFont.ImageFont, fill: tuple[int, int, int, int]) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - width) / 2
    y = box[1] + (box[3] - box[1] - height) / 2 - 2
    draw.text((x, y), text, font=font, fill=fill)


def draw_hash_mark(draw: ImageDraw.ImageDraw, seed: int, color: tuple[int, int, int, int]) -> None:
    variant = seed % 5
    if variant == 0:
        draw.polygon([(95, 20), (104, 42), (128, 42), (109, 56), (116, 80), (96, 66), (76, 80), (83, 56), (64, 42), (88, 42)], fill=color)
    elif variant == 1:
        draw.rounded_rectangle((66, 20, 126, 44), radius=12, fill=color)
        draw.rectangle((78, 42, 114, 62), fill=color)
    elif variant == 2:
        draw.ellipse((70, 18, 122, 70), outline=color, width=8)
        draw.line((96, 70, 96, 91), fill=color, width=8)
    elif variant == 3:
        draw.polygon([(96, 15), (127, 49), (96, 83), (65, 49)], outline=color, width=8)
    else:
        draw.arc((60, 18, 132, 90), 200, 340, fill=color, width=8)
        draw.line((70, 64, 122, 64), fill=color, width=7)


def make_generated_sprite(name: str) -> Image.Image:
    seed = digest_int(name)
    main = color_from_hash(seed, 0)
    secondary = color_from_hash(seed, 1)
    accent = color_from_hash(seed, 2)
    ink = (28, 25, 24, 255)
    paper = (245, 232, 198, 255)
    gold = (214, 174, 93, 255)

    image = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    body = (42, 54, 150, 176)
    shape = seed % 4
    if shape == 0:
        draw.rounded_rectangle(body, radius=38, fill=(*main, 255), outline=gold, width=5)
    elif shape == 1:
        draw.ellipse(body, fill=(*main, 255), outline=gold, width=5)
    elif shape == 2:
        draw.polygon([(96, 48), (153, 98), (136, 176), (56, 176), (39, 98)], fill=(*main, 255))
        draw.line([(96, 48), (153, 98), (136, 176), (56, 176), (39, 98), (96, 48)], fill=gold, width=5)
    else:
        draw.rounded_rectangle((46, 46, 146, 180), radius=18, fill=(*main, 255), outline=gold, width=5)

    draw.rounded_rectangle((58, 82, 134, 132), radius=18, fill=paper, outline=(255, 255, 255, 170), width=2)
    draw_centered_text(draw, (58, 78, 134, 130), initials(name), FONT_BIG if len(initials(name)) <= 2 else FONT_MEDIUM, ink)
    draw.ellipse((72, 140, 82, 150), fill=ink)
    draw.ellipse((110, 140, 120, 150), fill=ink)
    draw.arc((82, 142, 110, 164), 15, 165, fill=ink, width=3)

    draw.rounded_rectangle((39, 100, 54, 150), radius=8, fill=(*secondary, 255), outline=gold, width=3)
    draw.rounded_rectangle((138, 100, 153, 150), radius=8, fill=(*secondary, 255), outline=gold, width=3)
    draw.ellipse((62, 172, 88, 188), fill=(*secondary, 255), outline=gold, width=3)
    draw.ellipse((104, 172, 130, 188), fill=(*secondary, 255), outline=gold, width=3)

    draw_hash_mark(draw, seed, (*accent, 255))
    return crop_and_fit(image, max_width=168, max_height=196)


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


def crop_and_fit(image: Image.Image, max_width: int = 174, max_height: int = 198) -> Image.Image:
    cropped = crop_alpha(image)
    scale = min(max_width / cropped.width, max_height / cropped.height, 1.0)
    size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    return cropped.resize(size, Image.Resampling.LANCZOS)


def download_image(url: str, output: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/1.0"})
        if response.status_code != 200:
            return False
        image = Image.open(BytesIO(response.content)).convert("RGBA")
        image.save(output)
        return True
    except Exception:
        return False


def download_binary(url: str, output: Path) -> bool:
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0 9PetsBuilder/1.0"})
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


def get_source_sprite(name: str, package_name: str, official_assets: dict[str, str]) -> tuple[Image.Image, str, str | None]:
    asset_id = official_assets.get(name)
    if not asset_id:
        return make_generated_sprite(name), "generated-card", None

    source_path = SOURCE_DIR / f"{package_name}.png"
    role_url = OFFICIAL_ROLE_URL.format(asset_id=asset_id)
    thumb_url = OFFICIAL_THUMB_URL.format(asset_id=asset_id)
    if not source_path.exists():
        if not download_image(role_url, source_path):
            download_image(thumb_url, source_path)
    if source_path.exists():
        try:
            return crop_and_fit(Image.open(source_path).convert("RGBA")), "official-sourced", role_url
        except Exception:
            pass
    return make_generated_sprite(name), "generated-card", None


def transformed(sprite: Image.Image, *, scale: float = 1.0, angle: float = 0.0, flip: bool = False, opacity: float = 1.0) -> Image.Image:
    image = sprite
    if flip:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if scale != 1.0:
        size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)
    if angle:
        image = image.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    if opacity < 1.0:
        alpha = image.getchannel("A").point(lambda p: round(p * opacity))
        image = image.copy()
        image.putalpha(alpha)
    return image


def frame_motion(state: str, frame: int, total: int) -> dict[str, Any]:
    phase = frame / max(total - 1, 1)
    wave = math.sin(phase * math.tau)
    if state == "idle":
        return {"scale": 1.0 + 0.012 * wave, "angle": 1.5 * wave, "x": 0, "y": round(-3 * abs(wave)), "flip": False}
    if state == "running-right":
        return {"scale": 1.0, "angle": [-4, 3, -5, 4, -3, 5, -2, 2][frame], "x": [-12, -8, -4, 0, 4, 8, 12, 8][frame], "y": [2, -2, 1, -3, 2, -2, 1, 0][frame], "flip": False}
    if state == "running-left":
        return {"scale": 1.0, "angle": [4, -3, 5, -4, 3, -5, 2, -2][frame], "x": [12, 8, 4, 0, -4, -8, -12, -8][frame], "y": [2, -2, 1, -3, 2, -2, 1, 0][frame], "flip": True}
    if state == "waving":
        return {"scale": 1.0, "angle": [0, -8, 8, 0][frame], "x": [0, -3, 3, 0][frame], "y": [0, -5, -4, 0][frame], "flip": False}
    if state == "jumping":
        return {"scale": [1.0, 0.98, 1.02, 1.01, 1.0][frame], "angle": [0, -3, 2, 1, 0][frame], "x": 0, "y": [6, -18, -34, -14, 4][frame], "flip": False}
    if state == "failed":
        return {"scale": 1.0, "angle": [0, 7, -5, 10, -8, 5, -3, 0][frame], "x": [0, 2, -3, 4, -4, 2, -1, 0][frame], "y": [8, 10, 12, 10, 14, 12, 10, 8][frame], "flip": False, "opacity": [1, 0.92, 0.88, 0.95, 0.9, 0.94, 0.98, 1][frame]}
    if state == "waiting":
        return {"scale": 1.0 + 0.01 * abs(wave), "angle": [0, -2, -4, 4, 2, 0][frame], "x": [0, -1, -2, 2, 1, 0][frame], "y": [0, -2, -4, -2, 0, 1][frame], "flip": False}
    if state == "running":
        return {"scale": 1.0 + 0.008 * wave, "angle": [0, -2, 2, -1, 1, 0][frame], "x": 0, "y": [-1, -4, -2, -5, -2, -1][frame], "flip": False}
    if state == "review":
        return {"scale": [1.0, 1.015, 1.02, 1.015, 1.0, 0.995][frame], "angle": [0, -2, -3, -2, 0, 1][frame], "x": [0, -2, -3, -2, 0, 1][frame], "y": [0, -1, -2, -1, 0, 1][frame], "flip": False}
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


def make_preview(sprite: Image.Image, output: Path) -> None:
    preview = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
    preview.alpha_composite(make_cell(sprite, "idle", 0, 6))
    output.parent.mkdir(parents=True, exist_ok=True)
    preview.save(output)


def make_pet_json(package_name: str, name: str, source_type: str) -> dict[str, str]:
    return {
        "id": pet_id_from_package(package_name),
        "displayName": f"9Pets - {name}",
        "description": f"A fan-made Reverse: 1999 Codex pet for {name}. Source mode: {source_type}.",
        "spritesheetPath": "spritesheet.webp",
    }


def write_zip(package_name: str, pet_json: dict[str, str], spritesheet_path: Path, zip_path: Path, source_type: str, source_url: str | None) -> int:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    readme = "\n".join(
        [
            f"# {package_name}",
            "",
            "Fan-made Codex pet package for Reverse: 1999.",
            f"Source mode: {source_type}.",
            f"Source URL: {source_url or 'Generated from character catalog metadata.'}",
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
    for path in [PETS_DIR, OFFICIAL_SITE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]:
        if path.exists():
            shutil.rmtree(path)
    for path in [PETS_DIR, SOURCE_DIR, OFFICIAL_SITE_DIR, PREVIEW_DIR, SPRITESHEET_DIR, DOWNLOAD_DIR, DATA_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def build() -> None:
    catalog = read_catalog()
    clean_output_dirs()
    official_site_assets = download_official_site_assets()
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    official_assets = catalog.get("officialAssetIds", {})
    pets: list[dict[str, Any]] = []

    for index, item in enumerate(catalog["characters"], start=1):
        name = item["name"]
        package_name = f"9Pets-{slug_suffix(name)}"
        package_dir = PETS_DIR / package_name
        package_dir.mkdir(parents=True, exist_ok=True)

        sprite, source_type, source_url = get_source_sprite(name, package_name, official_assets)
        atlas = make_atlas(sprite)
        spritesheet_path = package_dir / "spritesheet.webp"
        atlas.save(spritesheet_path, format="WEBP", lossless=True, quality=100, method=0)

        pet_json = make_pet_json(package_name, name, source_type)
        (package_dir / "pet.json").write_text(json.dumps(pet_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        docs_spritesheet = SPRITESHEET_DIR / f"{package_name}.webp"
        shutil.copy2(spritesheet_path, docs_spritesheet)
        preview_path = PREVIEW_DIR / f"{package_name}.png"
        make_preview(sprite, preview_path)

        zip_path = DOWNLOAD_DIR / f"{package_name}.zip"
        package_bytes = write_zip(package_name, pet_json, spritesheet_path, zip_path, source_type, source_url)

        pets.append(
            {
                "id": pet_json["id"],
                "packageName": package_name,
                "displayName": name,
                "download": f"downloads/{package_name}.zip",
                "preview": f"assets/previews/{package_name}.png",
                "spritesheet": f"assets/spritesheets/{package_name}.webp",
                "sourceType": source_type,
                "sourceUrl": source_url or catalog["sources"]["prydwenCatalog"],
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
