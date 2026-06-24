from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import build_pets_site as site


ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "PET_AUDIT_TODO.md"
CONTACT_SCRIPT = Path(r"C:\Users\TabYe\.codex\skills\hatch-pet\scripts\make_contact_sheet.py")
CONTACT_DIR = ROOT / ".tmp" / "audit-contacts"
LEGACY_ASSET_CACHE_DIR = Path(os.environ.get("NINEPETS_LEGACY_ASSET_DIR", r"C:\tmp\9pets-Reverse-1999-CN-Asset"))
CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
STATE_COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6]
ANIMATED_MODES = {"official-live2d-cubism", "official-spine", "official-cute-spine"}


def run(command: list[str]) -> str:
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    output = (completed.stdout or "") + (completed.stderr or "")
    if output.strip():
        print(output.strip(), flush=True)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")
    return output


def package_for_name(name: str, *, cute: bool = False) -> str:
    return site.package_name_for(name, site.DEFAULT_SKIN_NAME, cute=cute)


def contact_slug(package_name: str) -> str:
    suffix = package_name.removeprefix("9Pets-").lower()
    return f"9pets-{suffix}-final-contact.png"


def read_manifest_items() -> dict[str, dict[str, object]]:
    data = json.loads((ROOT / "docs" / "data" / "pets.json").read_text(encoding="utf-8"))
    return {item["packageName"]: item for item in [*data.get("pets", []), *data.get("cuteVariants", [])]}


def copy_from_legacy(repo_path: str) -> list[Path]:
    if not repo_path:
        return []
    normalized = repo_path.replace("\\", "/").strip("/")
    if normalized in {"live2d", "live2d/roles", "roles", "singlebg"}:
        return []
    destination = site.local_asset_path(repo_path)
    if destination.exists():
        return [destination]
    source = LEGACY_ASSET_CACHE_DIR / Path(repo_path)
    if not source.exists():
        return []
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
    return [destination]


def ensure_image_candidates(asset_id: int | str) -> list[Path]:
    copied: list[Path] = []
    for template in site.OFFICIAL_IMAGE_PATHS:
        copied.extend(copy_from_legacy(template.format(asset_id=asset_id)))
    return copied


def ensure_role_candidates(asset_id: int | str) -> list[Path]:
    copied: list[Path] = []
    if not LEGACY_ASSET_CACHE_DIR.exists():
        return copied
    for root in ["live2d/roles", "roles"]:
        legacy_root = LEGACY_ASSET_CACHE_DIR / Path(root)
        if not legacy_root.exists():
            continue
        for source in sorted(legacy_root.glob(f"*{asset_id}*")):
            if source.is_dir():
                copied.extend(copy_from_legacy(source.relative_to(LEGACY_ASSET_CACHE_DIR).as_posix()))
    return copied


def lookup_default_skin(name: str, official_index: dict[str, dict[str, object]]) -> dict[str, object]:
    manual = site.MANUAL_OFFICIAL_ASSETS.get(name)
    if manual and not site.find_official_entry(name, official_index):
        return {
            "id": manual["assetId"],
            "spinePath": manual.get("spinePath", ""),
            "cubismPath": manual.get("cubismPath", ""),
        }

    skins = site.official_skin_entries(name, official_index)
    skin = site.default_skin_entry(skins)
    if not skin:
        return {}
    return {
        "id": skin["id"],
        "spinePath": site.repo_path_from_tree_url(skin.get("spine", "")),
        "cubismPath": site.repo_path_from_tree_url(skin.get("cubism", "")),
    }


def ensure_character_asset_cache(name: str, official_index: dict[str, dict[str, object]]) -> tuple[dict[str, object], list[Path]]:
    copied: list[Path] = []
    default_skin = lookup_default_skin(name, official_index)
    if default_skin.get("id"):
        copied.extend(ensure_role_candidates(default_skin["id"]))
        copied.extend(ensure_image_candidates(default_skin["id"]))
    for key in ["cubismPath", "spinePath"]:
        copied.extend(copy_from_legacy(str(default_skin.get(key, ""))))

    asset = site.resolve_official_asset(name, official_index)
    if asset.get("assetId"):
        copied.extend(ensure_role_candidates(asset["assetId"]))
        copied.extend(ensure_image_candidates(asset["assetId"]))
    for key in ["cubismPath", "spinePath"]:
        copied.extend(copy_from_legacy(str(asset.get(key, ""))))

    cute_override = site.CUTE_SPINE_SOURCE_OVERRIDES.get(package_for_name(name, cute=True), {})
    if cute_override.get("assetId"):
        copied.extend(ensure_role_candidates(cute_override["assetId"]))
        copied.extend(ensure_image_candidates(cute_override["assetId"]))
    copied.extend(copy_from_legacy(cute_override.get("spinePath", "")))

    unique_paths = sorted({path.resolve() for path in copied if path.exists()})
    return asset, unique_paths


def source_audit(name: str) -> dict[str, str]:
    official_index = site.load_official_asset_index()
    asset, cached_paths = ensure_character_asset_cache(name, official_index)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    live2d_dir = site.local_asset_path(cubism_path)
    spine_dir = site.local_asset_path(spine_path)
    motion_dir = live2d_dir / "motions"
    live2d_motions = sorted(path.name for path in motion_dir.glob("*.motion3.json")) if motion_dir.exists() else []
    room_skeletons = sorted(path.name for path in spine_dir.glob("*_room.skel")) if spine_dir.exists() else []
    fight_skeletons = sorted(path.name for path in spine_dir.glob("*_fight.skel")) if spine_dir.exists() else []
    normal_uses_live2d = site.live2d_model_cached(cubism_path) and package_for_name(name) not in site.NORMAL_SPINE_OVERRIDE_PACKAGES
    return {
        "asset_id": str(asset["assetId"]),
        "skin_name": str(asset.get("skinName", "Default")),
        "cubism_path": cubism_path,
        "spine_path": spine_path,
        "live2d_cached": "yes" if site.live2d_model_cached(cubism_path) else "no",
        "live2d_motion_count": str(len(live2d_motions)),
        "room_skeleton": room_skeletons[0] if room_skeletons else "",
        "fight_skeleton": fight_skeletons[0] if fight_skeletons else "",
        "normal_source": cubism_path if normal_uses_live2d else f"static official art ({asset['assetId']})",
        "cute_source": f"{spine_path}/{fight_skeletons[0]}" if fight_skeletons else "",
        "cached_paths": "\n".join(path.relative_to(ROOT).as_posix() for path in cached_paths if path.is_relative_to(ROOT)),
    }


def assert_default_normal_skin(audit: dict[str, str], name: str) -> None:
    if audit["skin_name"].strip().casefold() != "default":
        raise RuntimeError(
            f"{name} resolved to non-default skin {audit['skin_name']!r}. "
            "Build a separate skin package named 9Pets-Character-Skin-Name instead."
        )


def parse_motion_lines(output: str) -> str:
    pairs = []
    pattern = r"^(idle|running-right|running-left|waving|jumping|failed|waiting|running|review) (motion|animation) (.+)$"
    for line in output.splitlines():
        match = re.match(pattern, line)
        if match:
            pairs.append(f"{match.group(1)}={match.group(3)}")
    return ", ".join(pairs)


def package_paths(package_name: str) -> list[Path]:
    return [
        ROOT / "pets" / package_name / "spritesheet.webp",
        ROOT / "docs" / "assets" / "spritesheets" / f"{package_name}.webp",
        ROOT / "docs" / "assets" / "detail-spritesheets" / f"{package_name}.webp",
    ]


def pixel_qa(package_names: list[str]) -> None:
    for package_name in package_names:
        for path in package_paths(package_name):
            if not path.exists():
                continue
            image = Image.open(path).convert("RGBA")
            scale_x = image.width // (COLS * CELL_W)
            scale_y = image.height // (ROWS * CELL_H)
            if scale_x != scale_y or scale_x < 1:
                raise AssertionError(f"{path} has unexpected size {image.size}")
            cell_w = CELL_W * scale_x
            cell_h = CELL_H * scale_x
            if image.size != (COLS * cell_w, ROWS * cell_h):
                raise AssertionError(f"{path} has unexpected size {image.size}")

            pixels = image.load()
            for y in range(image.height):
                for x in range(image.width):
                    r, g, b, a = pixels[x, y]
                    if a == 0 and (r or g or b):
                        raise AssertionError(f"{path} has transparent RGB residue")

            for row_index, count in enumerate(STATE_COUNTS):
                for col in range(COLS):
                    cell = image.crop((col * cell_w, row_index * cell_h, (col + 1) * cell_w, (row_index + 1) * cell_h))
                    bbox = cell.getchannel("A").getbbox()
                    if col < count:
                        if bbox is None:
                            raise AssertionError(f"{path} row {row_index} col {col} is empty")
                        left, top, right, bottom = bbox
                        if left <= 0 or top <= 0 or right >= cell_w or bottom >= cell_h:
                            raise AssertionError(f"{path} row {row_index} col {col} clips at {bbox}")
                    elif bbox is not None:
                        raise AssertionError(f"{path} row {row_index} col {col} should be transparent")
            print(f"{path.relative_to(ROOT)}: pixel QA passed", flush=True)


def visible_color_qa(package_names: list[str]) -> None:
    for package_name in package_names:
        path = ROOT / "pets" / package_name / "spritesheet.webp"
        image = Image.open(path).convert("RGBA")
        total = 0
        near_black = 0
        for index, (r, g, b, a) in enumerate(image.getdata()):
            if index % 4 or a <= 16:
                continue
            total += 1
            if max(r, g, b) <= 12:
                near_black += 1
        if total < 500:
            raise AssertionError(f"{path} has too few visible sampled pixels")
        dark_ratio = near_black / total
        if dark_ratio > 0.85:
            raise AssertionError(f"{path} looks like a black silhouette; near-black sampled pixel ratio is {dark_ratio:.1%}")
        print(f"{path.relative_to(ROOT)}: visible color QA passed ({dark_ratio:.1%} near-black)", flush=True)


def compact_white_blocks(path: Path) -> list[tuple[int, tuple[int, int, int, int], float]]:
    image = Image.open(path).convert("RGBA")
    atlas_scale = max(1, image.width // (COLS * CELL_W))
    min_area = 8 * atlas_scale * atlas_scale
    min_size = 3 * atlas_scale
    max_size = 30 * atlas_scale
    pixels = image.load()
    candidates: set[tuple[int, int]] = set()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a >= 235 and r >= 246 and g >= 246 and b >= 246 and max(r, g, b) - min(r, g, b) <= 5:
                candidates.add((x, y))

    blocks: list[tuple[int, tuple[int, int, int, int], float]] = []
    while candidates:
        start = candidates.pop()
        stack = [start]
        xs: list[int] = []
        ys: list[int] = []
        while stack:
            x, y = stack.pop()
            xs.append(x)
            ys.append(y)
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (nx, ny) in candidates:
                    candidates.remove((nx, ny))
                    stack.append((nx, ny))
        area = len(xs)
        bbox = (min(xs), min(ys), max(xs) + 1, max(ys) + 1)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        fill = area / (width * height)
        squareish = 0.65 <= width / height <= 1.55
        pad = max(4 * atlas_scale, round(max(width, height) * 0.75))
        outer = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(image.width, bbox[2] + pad),
            min(image.height, bbox[3] + pad),
        )
        ring_area = 0
        ring_visible = 0
        for ring_y in range(outer[1], outer[3]):
            for ring_x in range(outer[0], outer[2]):
                if bbox[0] <= ring_x < bbox[2] and bbox[1] <= ring_y < bbox[3]:
                    continue
                ring_area += 1
                if pixels[ring_x, ring_y][3] > 32:
                    ring_visible += 1
        isolated = ring_area > 0 and ring_visible / ring_area < 0.16
        solid_square = fill > 0.98 and max(width, height) <= 12 * atlas_scale
        if (
            min_area <= area <= 500 * atlas_scale * atlas_scale
            and min_size <= width <= max_size
            and min_size <= height <= max_size
            and fill > 0.75
            and squareish
            and (isolated or solid_square)
        ):
            blocks.append((area, bbox, fill))
    return sorted(blocks, reverse=True)


def white_block_artifact_qa(
    package_names: list[str],
    *,
    animation_modes: set[str] | None = None,
) -> None:
    allowed_modes = animation_modes or {"official-live2d-cubism"}
    manifest_items = read_manifest_items()
    for package_name in package_names:
        item = manifest_items.get(package_name, {})
        if item.get("animationMode") not in allowed_modes:
            continue
        for path in package_paths(package_name):
            if not path.exists():
                continue
            blocks = compact_white_blocks(path)
            if blocks:
                raise AssertionError(f"{path} has compact white block artifacts: {blocks[:10]}")
        print(f"{package_name}: white block artifact QA passed", flush=True)


def raw_frame_qa(package_names: list[str]) -> None:
    manifest_items = read_manifest_items()
    for package_name in package_names:
        item = manifest_items.get(package_name, {})
        if item.get("animationMode") not in ANIMATED_MODES:
            print(f"{package_name}: raw frame QA skipped for {item.get('animationMode', 'unknown')}", flush=True)
            continue
        roots = [site.LIVE2D_FRAME_ROOT / package_name, site.SPINE_FRAME_ROOT / package_name]
        existing_roots = [root for root in roots if root.exists()]
        if not existing_roots:
            raise AssertionError(f"No raw frame capture folder found for {package_name}")
        for root in existing_roots:
            for frame_path in sorted(root.glob("*/*.png")):
                image = Image.open(frame_path).convert("RGBA")
                bbox = image.getchannel("A").getbbox()
                if bbox is None:
                    raise AssertionError(f"{frame_path} is empty")
                left, top, right, bottom = bbox
                if left <= 0 or top <= 0 or right >= image.width or bottom >= image.height:
                    raise AssertionError(f"{frame_path} raw capture touches canvas edge at {bbox}")
            print(f"{root.relative_to(ROOT)}: raw frame QA passed", flush=True)


def make_contact(package_name: str) -> Path:
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    output = CONTACT_DIR / contact_slug(package_name)
    run([sys.executable, str(CONTACT_SCRIPT), str(ROOT / "pets" / package_name / "spritesheet.webp"), "--output", str(output)])
    return output


def update_todo(
    name: str,
    normal_package: str,
    cute_package: str,
    *,
    visual_qa_pass: bool,
    committed: bool,
    note: str,
) -> None:
    text = TODO.read_text(encoding="utf-8")
    done = "[x]" if visual_qa_pass and committed else "[ ]"
    visual = "[x]" if visual_qa_pass else "[ ]"
    commit = "[x]" if committed else "[ ]"
    row = (
        f"| {done} | {name} | `{normal_package}` | `{cute_package}` | [x] | [x] | [x] | [x] | "
        f"{visual} | {commit} | {note} |"
    )
    pattern = rf"^\| \[[ x]\] \| {re.escape(name)} \| `[^`]+` \| `[^`]+` \| .*$"
    updated, count = re.subn(pattern, lambda _: row, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Could not update TODO row for {name}")
    TODO.write_text(updated, encoding="utf-8")


def stage_paths(package_names: list[str], audit: dict[str, str]) -> None:
    paths: list[Path] = [
        TODO,
        ROOT / "docs" / "data" / "pets.json",
        ROOT / "docs" / "data" / "pets-data.js",
        site.ASSET_CACHE_DIR / "mappings" / "ArcanistMap.json",
    ]
    for package_name in package_names:
        paths.extend(
            [
                ROOT / "pets" / package_name,
                ROOT / "docs" / "assets" / "source" / f"{package_name}.png",
                ROOT / "docs" / "assets" / "spritesheets" / f"{package_name}.webp",
                ROOT / "docs" / "assets" / "detail-spritesheets" / f"{package_name}.webp",
                ROOT / "docs" / "assets" / "previews" / f"{package_name}.png",
                ROOT / "docs" / "downloads" / f"{package_name}.zip",
            ]
        )
    for cached_path in audit.get("cached_paths", "").splitlines():
        paths.append(ROOT / cached_path)
    existing = [str(path.relative_to(ROOT)) for path in paths if path.exists()]
    if existing:
        run(["git", "add", "--", *existing])


def commit_audit(name: str, package_names: list[str], audit: dict[str, str]) -> None:
    stage_paths(package_names, audit)
    run(["git", "commit", "-m", f"Audit {name} normal and cute pets"])


def rebuild_character(name: str, *, visual_qa_pass: bool, commit: bool, skip_rebuild: bool) -> None:
    if commit and not visual_qa_pass:
        raise RuntimeError("--commit requires --visual-qa-pass so the TODO does not record an unaudited commit.")

    normal_package = package_for_name(name)
    cute_package = package_for_name(name, cute=True)
    package_names = [normal_package, cute_package]
    audit = source_audit(name)
    assert_default_normal_skin(audit, name)
    print(json.dumps({"character": name, "audit": audit}, indent=2), flush=True)

    normal_output = ""
    cute_output = ""
    if not skip_rebuild:
        normal_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--only", name])
        cute_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--cute-only", name])
    normal_contact = make_contact(normal_package)
    cute_contact = make_contact(cute_package)
    run([sys.executable, str(ROOT / "tools" / "verify_build.py")])
    raw_frame_qa(package_names)
    pixel_qa(package_names)
    visible_color_qa(package_names)

    note_bits = [
        f"{datetime.now().date().isoformat()}",
        f"asset {audit['asset_id']}",
        f"normal={audit['normal_source'] or 'static fallback'}",
        f"cute={audit['cute_source'] or 'missing fight spine'}",
        f"cached paths={len(audit.get('cached_paths', '').splitlines())}",
    ]
    normal_motions = parse_motion_lines(normal_output)
    cute_motions = parse_motion_lines(cute_output)
    if normal_motions:
        note_bits.append(f"normal motions: {normal_motions}")
    if cute_motions:
        note_bits.append(f"cute motions: {cute_motions}")
    note_bits.append(f"contacts: {normal_contact.relative_to(ROOT).as_posix()}, {cute_contact.relative_to(ROOT).as_posix()}")

    if commit:
        update_todo(name, normal_package, cute_package, visual_qa_pass=True, committed=True, note="; ".join(note_bits))
        commit_audit(name, package_names, audit)
    else:
        update_todo(name, normal_package, cute_package, visual_qa_pass=visual_qa_pass, committed=False, note="; ".join(note_bits))


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild one 9Pets character, update PET_AUDIT_TODO, and optionally commit.")
    parser.add_argument("character", help="Display name, package name, or pet id.")
    parser.add_argument("--visual-qa-pass", action="store_true", help="Mark the visual QA column complete after reviewing contact sheets/previews.")
    parser.add_argument("--commit", action="store_true", help="Stage the audited character files and create one git commit.")
    parser.add_argument("--skip-rebuild", action="store_true", help="Reuse current package outputs; only regenerate contacts, verify, update TODO, and optionally commit.")
    args = parser.parse_args()
    item = site.find_catalog_item(site.read_catalog(), args.character)
    rebuild_character(item["name"], visual_qa_pass=args.visual_qa_pass, commit=args.commit, skip_rebuild=args.skip_rebuild)


if __name__ == "__main__":
    main()
