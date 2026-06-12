from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image

import build_pets_site as site


ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "PET_AUDIT_TODO.md"
CONTACT_SCRIPT = Path(r"C:\Users\TabYe\.codex\skills\hatch-pet\scripts\make_contact_sheet.py")
CONTACT_DIR = ROOT / ".tmp" / "audit-contacts"
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
    prefix = "9Pets-Cute-" if cute else "9Pets-"
    return f"{prefix}{site.slug_suffix(name)}"


def contact_slug(package_name: str) -> str:
    suffix = package_name.removeprefix("9Pets-").lower()
    return f"9pets-{suffix}-final-contact.png"


def read_manifest_items() -> dict[str, dict[str, object]]:
    data = json.loads((ROOT / "docs" / "data" / "pets.json").read_text(encoding="utf-8"))
    return {item["packageName"]: item for item in [*data.get("pets", []), *data.get("cuteVariants", [])]}


def source_audit(name: str) -> dict[str, str]:
    official_index = site.load_official_asset_index()
    asset = site.resolve_official_asset(name, official_index)
    cubism_path = asset.get("cubismPath", "")
    spine_path = asset.get("spinePath", "")
    live2d_dir = site.local_asset_path(cubism_path)
    spine_dir = site.local_asset_path(spine_path)
    motion_dir = live2d_dir / "motions"
    live2d_motions = sorted(path.name for path in motion_dir.glob("*.motion3.json")) if motion_dir.exists() else []
    room_skeletons = sorted(path.name for path in spine_dir.glob("*_room.skel")) if spine_dir.exists() else []
    fight_skeletons = sorted(path.name for path in spine_dir.glob("*_fight.skel")) if spine_dir.exists() else []
    return {
        "asset_id": str(asset["assetId"]),
        "skin_name": str(asset.get("skinName", "Default")),
        "cubism_path": cubism_path,
        "spine_path": spine_path,
        "live2d_cached": "yes" if site.live2d_model_cached(cubism_path) else "no",
        "live2d_motion_count": str(len(live2d_motions)),
        "room_skeleton": room_skeletons[0] if room_skeletons else "",
        "fight_skeleton": fight_skeletons[0] if fight_skeletons else "",
        "normal_source": cubism_path if site.live2d_model_cached(cubism_path) else (f"{spine_path}/{room_skeletons[0]}" if room_skeletons else ""),
        "cute_source": f"{spine_path}/{fight_skeletons[0]}" if fight_skeletons else "",
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
    updated, count = re.subn(pattern, row, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise RuntimeError(f"Could not update TODO row for {name}")
    TODO.write_text(updated, encoding="utf-8")


def stage_paths(package_names: list[str]) -> None:
    paths: list[Path] = [TODO, ROOT / "docs" / "data" / "pets.json", ROOT / "docs" / "data" / "pets-data.js"]
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
    existing = [str(path.relative_to(ROOT)) for path in paths if path.exists()]
    if existing:
        run(["git", "add", "--", *existing])


def commit_audit(name: str, package_names: list[str]) -> None:
    stage_paths(package_names)
    run(["git", "commit", "-m", f"Audit {name} normal and cute pets"])


def rebuild_character(name: str, *, visual_qa_pass: bool, commit: bool) -> None:
    if commit and not visual_qa_pass:
        raise RuntimeError("--commit requires --visual-qa-pass so the TODO does not record an unaudited commit.")

    normal_package = package_for_name(name)
    cute_package = package_for_name(name, cute=True)
    package_names = [normal_package, cute_package]
    audit = source_audit(name)
    assert_default_normal_skin(audit, name)
    print(json.dumps({"character": name, "audit": audit}, indent=2), flush=True)

    normal_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--only", name])
    cute_output = run([sys.executable, str(ROOT / "tools" / "build_pets_site.py"), "--cute-only", name])
    normal_contact = make_contact(normal_package)
    cute_contact = make_contact(cute_package)
    run([sys.executable, str(ROOT / "tools" / "verify_build.py")])
    raw_frame_qa(package_names)
    pixel_qa(package_names)

    note_bits = [
        f"{datetime.now().date().isoformat()}",
        f"asset {audit['asset_id']}",
        f"normal={audit['normal_source'] or 'static fallback'}",
        f"cute={audit['cute_source'] or 'missing fight spine'}",
    ]
    normal_motions = parse_motion_lines(normal_output)
    cute_motions = parse_motion_lines(cute_output)
    if normal_motions:
        note_bits.append(f"normal motions: {normal_motions}")
    if cute_motions:
        note_bits.append(f"cute motions: {cute_motions}")
    note_bits.append(f"contacts: {normal_contact.relative_to(ROOT)}, {cute_contact.relative_to(ROOT)}")

    if commit:
        update_todo(name, normal_package, cute_package, visual_qa_pass=True, committed=True, note="; ".join(note_bits))
        commit_audit(name, package_names)
    else:
        update_todo(name, normal_package, cute_package, visual_qa_pass=visual_qa_pass, committed=False, note="; ".join(note_bits))


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild one 9Pets character, update PET_AUDIT_TODO, and optionally commit.")
    parser.add_argument("character", help="Display name, package name, or pet id.")
    parser.add_argument("--visual-qa-pass", action="store_true", help="Mark the visual QA column complete after reviewing contact sheets/previews.")
    parser.add_argument("--commit", action="store_true", help="Stage the audited character files and create one git commit.")
    args = parser.parse_args()
    item = site.find_catalog_item(site.read_catalog(), args.character)
    rebuild_character(item["name"], visual_qa_pass=args.visual_qa_pass, commit=args.commit)


if __name__ == "__main__":
    main()
