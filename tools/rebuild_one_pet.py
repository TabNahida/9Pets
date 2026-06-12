from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

import build_pets_site as site


ROOT = Path(__file__).resolve().parents[1]
WORKLOG = ROOT / "PET_REBUILD_WORKLOG.md"
CONTACT_SCRIPT = Path(r"C:\Users\TabYe\.codex\skills\hatch-pet\scripts\make_contact_sheet.py")
TMP_DIR = Path(r"C:\tmp")
LIVE2D_FRAME_ROOT = Path(tempfile.gettempdir()) / "9pets-live2d-frames"
SPINE_FRAME_ROOT = Path(tempfile.gettempdir()) / "9pets-spine-frames"
CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
STATE_COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6]


def run(command: list[str]) -> str:
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    output = (completed.stdout or "") + (completed.stderr or "")
    if output.strip():
        print(output.strip(), flush=True)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")
    return output


def slug_for(name: str) -> str:
    return site.slug_suffix(name)


def contact_slug(package_name: str) -> str:
    suffix = package_name.removeprefix("9Pets-").lower()
    return f"9pets-{suffix}-final-contact.png"


def parse_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in WORKLOG.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ["):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 7 or parts[1] == "Character":
            continue
        rows.append(
            {
                "done": parts[0],
                "name": parts[1],
                "package": parts[2].strip("`"),
                "prior": parts[3],
                "cache": parts[4],
                "asset": parts[5],
                "note": parts[6],
                "line": line,
            }
        )
    return rows


def row_for(name: str) -> dict[str, str]:
    normalized = site.normalized_lookup_name(name)
    for row in parse_rows():
        if site.normalized_lookup_name(row["name"]) == normalized:
            return row
    raise RuntimeError(f"Character not found in worklog table: {name}")


def next_after(name: str) -> dict[str, str] | None:
    rows = parse_rows()
    for index, row in enumerate(rows):
        if site.normalized_lookup_name(row["name"]) == site.normalized_lookup_name(name):
            return rows[index + 1] if index + 1 < len(rows) else None
    return None


def replace_active_slot(text: str, row: dict[str, str] | None) -> str:
    if row:
        values = {
            "Active character": row["name"],
            "Package": f"{row['package']} / 9Pets-Cute-{row['package'].removeprefix('9Pets-')}",
            "Asset id": row["asset"],
            "Source folder audited": "pending",
            "Live2D model used": "pending",
            "Motion files selected": "pending",
            "Last QA artifact": "pending",
            "Blocker": "none",
        }
    else:
        values = {
            "Active character": "none",
            "Package": "none",
            "Asset id": "none",
            "Source folder audited": "none",
            "Live2D model used": "none",
            "Motion files selected": "none",
            "Last QA artifact": "none",
            "Blocker": "none",
        }
    for key, value in values.items():
        text = re.sub(rf"^- {re.escape(key)}: .*$", f"- {key}: {value}", text, flags=re.MULTILINE)
    return text


def set_active(row: dict[str, str] | None) -> None:
    text = WORKLOG.read_text(encoding="utf-8")
    WORKLOG.write_text(replace_active_slot(text, row), encoding="utf-8")


def mark_done(row: dict[str, str], note: str) -> None:
    text = WORKLOG.read_text(encoding="utf-8")
    escaped_package = re.escape(f"`{row['package']}`")
    pattern = (
        rf"^\| \[.\] \| {re.escape(row['name'])} \| {escaped_package} \| "
        rf"{re.escape(row['prior'])} \| {re.escape(row['cache'])} \| {re.escape(row['asset'])} \| .* \|$"
    )
    replacement = (
        f"| [x] | {row['name']} | `{row['package']}` | {row['prior']} | {row['cache']} | "
        f"{row['asset']} | {note} |"
    )
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Could not update table row for {row['name']}")
    WORKLOG.write_text(updated, encoding="utf-8")


def package_paths(package_name: str) -> list[Path]:
    return [
        ROOT / "pets" / package_name / "spritesheet.webp",
        ROOT / "docs" / "assets" / "detail-spritesheets" / f"{package_name}.webp",
    ]


def pixel_qa(package_names: list[str]) -> None:
    for package_name in package_names:
        for path in package_paths(package_name):
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


def raw_frame_qa(package_names: list[str]) -> None:
    for package_name in package_names:
        roots = [LIVE2D_FRAME_ROOT / package_name, SPINE_FRAME_ROOT / package_name]
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
            print(f"{root}: raw frame QA passed", flush=True)


def make_contact(package_name: str) -> Path:
    output = TMP_DIR / contact_slug(package_name)
    run([sys.executable, str(CONTACT_SCRIPT), str(ROOT / "pets" / package_name / "spritesheet.webp"), "--output", str(output)])
    return output


def source_audit(name: str, package_name: str) -> dict[str, str]:
    official_index = site.load_official_asset_index()
    asset = site.resolve_official_asset(name, official_index)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    live2d_dir = site.local_asset_path(cubism_path)
    spine_dir = site.local_asset_path(spine_path)
    live2d_motions: list[str] = []
    if site.live2d_model_cached(cubism_path):
        motion_dir = live2d_dir / "motions"
        live2d_motions = sorted(path.name for path in motion_dir.glob("*.motion3.json")) if motion_dir.exists() else []
    room_skeletons = sorted(path.name for path in spine_dir.glob("*_room.skel")) if spine_dir.exists() else []
    fight_skeletons = sorted(path.name for path in spine_dir.glob("*_fight.skel")) if spine_dir.exists() else []
    return {
        "asset_id": str(asset["assetId"]),
        "cubism_path": cubism_path,
        "spine_path": spine_path,
        "live2d_cached": "yes" if site.live2d_model_cached(cubism_path) else "no",
        "live2d_motion_count": str(len(live2d_motions)),
        "live2d_motion_sample": ", ".join(live2d_motions[:12]),
        "room_skeleton": room_skeletons[0] if room_skeletons else "",
        "fight_skeleton": fight_skeletons[0] if fight_skeletons else "",
        "normal_source": cubism_path if site.live2d_model_cached(cubism_path) else (f"{spine_path}/{room_skeletons[0]}" if room_skeletons else ""),
        "cute_source": f"{spine_path}/{fight_skeletons[0]}" if fight_skeletons else "",
        "normal_mode": "Live2D" if site.live2d_model_cached(cubism_path) else "room Spine",
    }


def parse_motion_lines(output: str) -> str:
    pairs = []
    for line in output.splitlines():
        motion_match = re.match(r"^(idle|running-right|running-left|waving|jumping|failed|waiting|running|review) motion (.+)$", line)
        animation_match = re.match(r"^(idle|running-right|running-left|waving|jumping|failed|waiting|running|review) animation (.+)$", line)
        match = motion_match or animation_match
        if match:
            pairs.append(f"{match.group(1)}={match.group(2)}")
    return ", ".join(pairs)


def append_logs(
    row: dict[str, str],
    audit: dict[str, str],
    normal_output: str,
    cute_output: str,
    normal_contact: Path,
    cute_contact: Path,
) -> None:
    package_name = row["package"]
    cute_package = f"9Pets-Cute-{package_name.removeprefix('9Pets-')}"
    normal_motions = parse_motion_lines(normal_output) or "recorded in renderer output"
    cute_motions = parse_motion_lines(cute_output) or "recorded in renderer output"
    text = WORKLOG.read_text(encoding="utf-8").rstrip()
    normal_source_line = (
        f"local normal Cubism folder `{audit['cubism_path']}` exists with {audit['live2d_motion_count']} motion files"
        if audit["normal_mode"] == "Live2D"
        else f"no cached normal Cubism source was available; selected normal-equivalent room Spine `{audit['normal_source']}`"
    )
    addition = f"""

### 2026-06-12 - {row['name']} Normal / {package_name}
- Source audit: {normal_source_line}; local Spine path is `{audit['spine_path']}`.
- Normal source: `{audit['normal_source']}`.
- Motions selected by the renderer: {normal_motions}.
- Capture settings: scoped one-character rebuild with 4x detail atlas.
- Files changed: rebuilt `pets/{package_name}`, `docs/assets/spritesheets/{package_name}.webp`, `docs/assets/detail-spritesheets/{package_name}.webp`, `docs/assets/previews/{package_name}.png`, `docs/downloads/{package_name}.zip`, and docs data for {row['name']}.
- QA artifacts: `{normal_contact}`.
- Verification: `python tools\\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this normal {audit['normal_mode']} pass.

### 2026-06-12 - {row['name']} Cute / {cute_package}
- Source audit: local official chibi/fight Spine source `{audit['cute_source']}`.
- Spine source: `{audit['fight_skeleton']}`.
- Motions selected by the renderer: {cute_motions}.
- Capture settings: scoped one-character fight Spine rebuild with 4x detail atlas.
- Files changed: built `pets/{cute_package}`, `docs/assets/spritesheets/{cute_package}.webp`, `docs/assets/detail-spritesheets/{cute_package}.webp`, `docs/assets/previews/{cute_package}.png`, `docs/assets/source/{cute_package}.png`, `docs/downloads/{cute_package}.zip`, and docs cute data for {row['name']}.
- QA artifacts: `{cute_contact}`.
- Verification: `python tools\\verify_build.py` passed; targeted image QA found no empty frames, no transparent RGB residue, no nontransparent unused cells, and no edge clipping in either the standard or detail atlas.
- Decision: accepted for this cute pass.
"""
    WORKLOG.write_text(text + addition + "\n", encoding="utf-8")


def rebuild_character(name: str) -> None:
    row = row_for(name)
    set_active(row)
    package_name = row["package"]
    cute_package = f"9Pets-Cute-{package_name.removeprefix('9Pets-')}"
    audit = source_audit(row["name"], package_name)
    print(json.dumps({"character": row["name"], "audit": audit}, indent=2), flush=True)

    normal_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--only", row["name"]])
    cute_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--cute-only", row["name"]])
    normal_contact = make_contact(package_name)
    cute_contact = make_contact(cute_package)
    run([sys.executable, str(ROOT / "tools" / "verify_build.py")])
    raw_frame_qa([package_name, cute_package])
    pixel_qa([package_name, cute_package])

    note = (
        "Rebuilt one-character pass with audited normal animation source, official fight Spine Cute variant, "
        "visible state motion, and 4x detail atlases."
    )
    mark_done(row, note)
    append_logs(row, audit, normal_output, cute_output, normal_contact, cute_contact)
    set_active(next_after(row["name"]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild exactly one 9Pets character and update the durable worklog.")
    parser.add_argument("character", help="Display name, package name, or pet id.")
    args = parser.parse_args()
    item = site.find_catalog_item(site.read_catalog(), args.character)
    rebuild_character(item["name"])


if __name__ == "__main__":
    main()
