from __future__ import annotations

import json
import zipfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DOCS_DATA = ROOT / "docs" / "data" / "pets.json"
CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
EXPECTED_SIZE = (CELL_W * COLS, CELL_H * ROWS)
STATE_FRAMES = [6, 8, 8, 4, 5, 8, 6, 6, 6]


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def has_visible_pixels(image: Image.Image) -> bool:
    return image.getchannel("A").getbbox() is not None


def check_spritesheet(path: Path) -> None:
    with Image.open(path) as image:
        rgba = image.convert("RGBA")
        assert_true(rgba.size == EXPECTED_SIZE, f"{path} has size {rgba.size}, expected {EXPECTED_SIZE}")
        for row, used_frames in enumerate(STATE_FRAMES):
            for col in range(COLS):
                cell = rgba.crop((col * CELL_W, row * CELL_H, (col + 1) * CELL_W, (row + 1) * CELL_H))
                if col < used_frames:
                    assert_true(has_visible_pixels(cell), f"{path} row {row} col {col} is empty")
                else:
                    assert_true(not has_visible_pixels(cell), f"{path} row {row} col {col} should be transparent")


def check_zip(path: Path, package_name: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        assert_true(f"{package_name}/pet.json" in names, f"{path} missing pet.json")
        assert_true(f"{package_name}/spritesheet.webp" in names, f"{path} missing spritesheet.webp")


def main() -> None:
    data = json.loads(DOCS_DATA.read_text(encoding="utf-8"))
    pets = data["pets"]
    assert_true(data["total"] == 127, f"manifest total is {data['total']}, expected 127")
    assert_true(len(pets) == 127, f"manifest contains {len(pets)} pets, expected 127")
    official_count = sum(1 for pet in pets if pet["sourceType"] == "official-sourced")
    prydwen_count = sum(1 for pet in pets if pet["sourceType"] == "prydwen-sourced")
    generated_count = sum(1 for pet in pets if pet["sourceType"] == "generated-card")
    assert_true(official_count == 10, f"official count is {official_count}, expected 10")
    assert_true(prydwen_count == 117, f"prydwen count is {prydwen_count}, expected 117")
    assert_true(generated_count == 0, f"generated count is {generated_count}, expected 0")
    assert_true((ROOT / "docs" / "data" / "pets-data.js").exists(), "docs/data/pets-data.js is missing")
    assert_true(len(data.get("officialSiteAssets", {})) >= 17, "official site assets were not downloaded")

    for pet in pets:
        package = pet["packageName"]
        pet_dir = ROOT / "pets" / package
        assert_true((pet_dir / "pet.json").exists(), f"{package} missing pet.json")
        check_spritesheet(pet_dir / "spritesheet.webp")
        check_spritesheet(ROOT / "docs" / pet["spritesheet"])
        assert_true((ROOT / "docs" / pet["preview"]).exists(), f"{package} missing preview")
        check_zip(ROOT / "docs" / pet["download"], package)

    for site_file in ["index.html", "styles.css", "app.js", ".nojekyll"]:
        assert_true((ROOT / "docs" / site_file).exists(), f"docs/{site_file} is missing")

    print("Build verification passed")
    print(f"pets={len(pets)} official={official_count} prydwen={prydwen_count} generated={generated_count}")
    print(f"atlas_size={EXPECTED_SIZE[0]}x{EXPECTED_SIZE[1]}")


if __name__ == "__main__":
    main()
