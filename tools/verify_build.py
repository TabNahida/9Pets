from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import build_pets_site as site

DOCS_DATA = ROOT / "docs" / "data" / "pets.json"
CELL_W = 192
CELL_H = 208
COLS = 8
ROWS = 9
EXPECTED_SIZE = (CELL_W * COLS, CELL_H * ROWS)
STATE_FRAMES = [6, 8, 8, 4, 5, 8, 6, 6, 6]
HIDDEN_NORMAL_PACKAGES = {
    "9Pets-Baby-Blue",
    "9Pets-Baby-Blue-Default",
    "9Pets-Balloon-Party",
    "9Pets-Balloon-Party-Default",
}
HIDDEN_NORMAL_PREFIXES = (
    "9Pets-Baby-Blue-",
    "9Pets-Balloon-Party-",
)
MIN_VISIBLE_NORMAL_TOTAL = 125


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


def expected_cute_packages() -> set[str]:
    official_index = site.load_official_asset_index()
    expected: set[str] = set()
    for item in site.read_catalog()["characters"]:
        name = item["name"]
        for skin in site.official_skin_entries(name, official_index):
            skin_name = site.skin_name_from_entry(skin)
            package = site.package_name_for(name, skin_name, cute=True)
            profile_package = site.base_profile_package_name(name, cute=True)
            asset = site.resolve_official_asset(name, official_index, skin)
            override = site.CUTE_SPINE_SOURCE_OVERRIDES.get(package) or site.CUTE_SPINE_SOURCE_OVERRIDES.get(profile_package)
            spine_path = override.get("spinePath", "") if override else asset.get("spinePath", "")
            if site.spine_render_ready(package, spine_path, profile_package):
                expected.add(package)
    return expected


def check_cute_normal_link(variant: dict, normal_ids: set[str], normal_packages: set[str]) -> None:
    package = variant["packageName"]
    normal_package = variant.get("normalPackageName")
    assert_true(isinstance(normal_package, str) and normal_package, f"{package} missing normal package link")
    assert_true(package.startswith("9Pets-Cute-"), f"{package} is not a cute package name")

    expected_normal_package = package.replace("9Pets-Cute-", "9Pets-", 1)
    assert_true(
        normal_package == expected_normal_package,
        f"{package} normal package link is {normal_package}, expected {expected_normal_package}",
    )

    expected_normal_id = site.pet_id_from_package(normal_package)
    assert_true(
        variant.get("normalId") == expected_normal_id,
        f"{package} normalId is {variant.get('normalId')}, expected {expected_normal_id}",
    )

    if normal_package in normal_packages:
        assert_true(variant.get("normalId") in normal_ids, f"{package} points to an unknown normal pet")
    else:
        assert_true(
            normal_package in HIDDEN_NORMAL_PACKAGES or not variant.get("isDefaultSkin", True),
            f"{package} points to missing default normal package {normal_package}",
        )


def main() -> None:
    data = json.loads(DOCS_DATA.read_text(encoding="utf-8"))
    pets = data["pets"]
    assert_true(data["total"] == len(pets), f"manifest total {data['total']} does not match pet count {len(pets)}")
    assert_true(
        len(pets) >= MIN_VISIBLE_NORMAL_TOTAL,
        f"manifest contains {len(pets)} pets, expected at least {MIN_VISIBLE_NORMAL_TOTAL}",
    )
    official_count = sum(1 for pet in pets if pet["sourceType"] == "official-sourced")
    assert_true(
        official_count == len(pets),
        f"official count is {official_count}, expected {len(pets)}",
    )
    cute_variants = data.get("cuteVariants", [])
    assert_true(data.get("cuteTotal", len(cute_variants)) == len(cute_variants), "cute variant total mismatch")
    expected_cute = expected_cute_packages()
    cute_packages = {variant["packageName"] for variant in cute_variants}
    assert_true(
        cute_packages == expected_cute,
        "cute variant package set mismatch: "
        f"missing={sorted(expected_cute - cute_packages)[:10]} "
        f"unexpected={sorted(cute_packages - expected_cute)[:10]}",
    )
    assert_true((ROOT / "docs" / "data" / "pets-data.js").exists(), "docs/data/pets-data.js is missing")
    assert_true(len(data.get("officialSiteAssets", {})) >= 17, "official site assets were not downloaded")
    normal_packages = {pet["packageName"] for pet in pets}
    assert_true(not (normal_packages & HIDDEN_NORMAL_PACKAGES), "hidden normal packages are visible in the manifest")
    assert_true(
        not any(package.startswith(HIDDEN_NORMAL_PREFIXES) for package in normal_packages),
        "hidden normal skin packages are visible in the manifest",
    )
    non_default_art_rig = [
        pet["packageName"]
        for pet in pets
        if not pet.get("isDefaultSkin", True) and pet.get("animationMode") == "official-art-elastic-rig"
    ]
    assert_true(
        not non_default_art_rig,
        f"non-default normal skin packages must not use portrait/elastic-rig output: {non_default_art_rig[:5]}",
    )
    non_default_not_live2d = [
        pet["packageName"]
        for pet in pets
        if not pet.get("isDefaultSkin", True) and pet.get("animationMode") != "official-live2d-cubism"
    ]
    assert_true(
        not non_default_not_live2d,
        f"non-default normal skin packages must use audited Live2D output: {non_default_not_live2d[:5]}",
    )

    for pet in pets:
        package = pet["packageName"]
        asset_versions = pet.get("assetVersions")
        assert_true(isinstance(asset_versions, dict), f"{package} missing asset version fingerprints")
        assert_true(pet.get("assetId"), f"{package} missing official asset id")
        assert_true(pet.get("sourceImage"), f"{package} missing source image metadata")
        assert_true("animationMode" in pet, f"{package} missing animation mode")
        assert_true("animationModeLabel" in pet, f"{package} missing animation mode label")
        assert_true("live2dCacheStatus" in pet, f"{package} missing Live2D cache status")
        assert_true("characterSummary" in pet, f"{package} missing character summary")
        assert_true("spinePath" in pet, f"{package} missing spine path metadata")
        assert_true("cubismPath" in pet, f"{package} missing cubism path metadata")
        assert_true("detailAtlasScale" in pet, f"{package} missing detail atlas scale")
        assert_true("skinName" in pet, f"{package} missing skin name")
        assert_true("isDefaultSkin" in pet, f"{package} missing default-skin flag")
        pet_dir = ROOT / "pets" / package
        assert_true((pet_dir / "pet.json").exists(), f"{package} missing pet.json")
        check_spritesheet(pet_dir / "spritesheet.webp")
        check_spritesheet(ROOT / "docs" / pet["spritesheet"])
        if pet.get("detailSpritesheet"):
            check_detail_spritesheet(ROOT / "docs" / pet["detailSpritesheet"], int(pet.get("detailAtlasScale") or 1))
        for field in ("download", "preview", "spritesheet", "detailSpritesheet", "sourceImage"):
            url = pet.get(field)
            if url:
                assert_true(url in asset_versions, f"{package} missing asset fingerprint for {field}")
        assert_true((ROOT / "docs" / pet["sourceImage"]).exists(), f"{package} missing official source image")
        assert_true((ROOT / "docs" / pet["preview"]).exists(), f"{package} missing preview")
        check_zip(ROOT / "docs" / pet["download"], package)

    normal_ids = {pet["id"] for pet in pets}
    cute_by_normal_package = {variant.get("normalPackageName"): variant for variant in cute_variants}
    for package in {"9Pets-Baby-Blue-Default", "9Pets-Balloon-Party-Default"}:
        variant = cute_by_normal_package.get(package)
        assert_true(variant is not None, f"{package} is hidden but its cute variant is missing")
        assert_true(
            variant.get("sourceImage", "").startswith("assets/source/9Pets-Cute-"),
            f"{variant['packageName']} should use cute source art",
        )

    for variant in cute_variants:
        package = variant["packageName"]
        asset_versions = variant.get("assetVersions")
        assert_true(isinstance(asset_versions, dict), f"{package} missing asset version fingerprints")
        assert_true(variant.get("variantType") == "cute", f"{package} missing cute variant type")
        check_cute_normal_link(variant, normal_ids, normal_packages)
        pet_dir = ROOT / "pets" / package
        assert_true((pet_dir / "pet.json").exists(), f"{package} missing pet.json")
        check_spritesheet(pet_dir / "spritesheet.webp")
        check_spritesheet(ROOT / "docs" / variant["spritesheet"])
        if variant.get("detailSpritesheet"):
            check_detail_spritesheet(ROOT / "docs" / variant["detailSpritesheet"], int(variant.get("detailAtlasScale") or 1))
        for field in ("download", "preview", "spritesheet", "detailSpritesheet", "sourceImage"):
            url = variant.get(field)
            if url:
                assert_true(url in asset_versions, f"{package} missing asset fingerprint for {field}")
        assert_true((ROOT / "docs" / variant["sourceImage"]).exists(), f"{package} missing cute source art")
        assert_true((ROOT / "docs" / variant["preview"]).exists(), f"{package} missing preview")
        check_zip(ROOT / "docs" / variant["download"], package)

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
