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


def check_detail_spritesheet(path: Path, scale: int) -> None:
    with Image.open(path) as image:
        expected_size = (EXPECTED_SIZE[0] * scale, EXPECTED_SIZE[1] * scale)
        assert_true(image.size == expected_size, f"{path} has size {image.size}, expected {expected_size}")


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
    assert_true(official_count == 127, f"official count is {official_count}, expected 127")
    assert_true((ROOT / "docs" / "data" / "pets-data.js").exists(), "docs/data/pets-data.js is missing")
    assert_true(len(data.get("officialSiteAssets", {})) >= 17, "official site assets were not downloaded")

    for pet in pets:
        package = pet["packageName"]
        assert_true(pet.get("assetId"), f"{package} missing official asset id")
        assert_true(pet.get("sourceImage"), f"{package} missing source image metadata")
        assert_true("animationMode" in pet, f"{package} missing animation mode")
        assert_true("animationModeLabel" in pet, f"{package} missing animation mode label")
        assert_true("live2dCacheStatus" in pet, f"{package} missing Live2D cache status")
        assert_true("characterSummary" in pet, f"{package} missing character summary")
        assert_true("spinePath" in pet, f"{package} missing spine path metadata")
        assert_true("cubismPath" in pet, f"{package} missing cubism path metadata")
        assert_true("detailAtlasScale" in pet, f"{package} missing detail atlas scale")
        pet_dir = ROOT / "pets" / package
        assert_true((pet_dir / "pet.json").exists(), f"{package} missing pet.json")
        check_spritesheet(pet_dir / "spritesheet.webp")
        check_spritesheet(ROOT / "docs" / pet["spritesheet"])
        if pet.get("detailSpritesheet"):
            check_detail_spritesheet(ROOT / "docs" / pet["detailSpritesheet"], int(pet.get("detailAtlasScale") or 1))
        assert_true((ROOT / "docs" / pet["sourceImage"]).exists(), f"{package} missing official source image")
        assert_true((ROOT / "docs" / pet["preview"]).exists(), f"{package} missing preview")
        check_zip(ROOT / "docs" / pet["download"], package)

    for site_file in ["index.html", "pet.html", "styles.css", "app.js", "pet.js", ".nojekyll"]:
        assert_true((ROOT / "docs" / site_file).exists(), f"docs/{site_file} is missing")

    app_js = (ROOT / "docs" / "app.js").read_text(encoding="utf-8")
    assert_true("pet.preview" in app_js, "catalog should use lightweight preview images")
    assert_true("pet.spritesheet" not in app_js, "catalog should not animate full spritesheets")

    print("Build verification passed")
    print(f"pets={len(pets)} official={official_count}")
    print(f"atlas_size={EXPECTED_SIZE[0]}x{EXPECTED_SIZE[1]}")


if __name__ == "__main__":
    main()
