from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REGRESSION_PACKAGES = [
    "9Pets-37-A-Prime-Number",
    "9Pets-37-Happy-Bird-Catcher",
    "9Pets-37-Down-in-the-Grotto",
    "9Pets-37-A-Gift-of-Nourishment",
    "9Pets-6-A-Hymn-to-Seclusion",
    "9Pets-Anjo-Nala-Carefree-Days",
    "9Pets-Anjo-Nala-Forbidden-Fruit",
    "9Pets-Charon-Default",
    "9Pets-Ezra-Theodore-Default",
    "9Pets-Fatutu-Default",
    "9Pets-Kiperina-Default",
    "9Pets-Liang-Yue-Default",
    "9Pets-Noire-Default",
    "9Pets-Paper-Heron-Default",
]


def compact_white_blocks(
    path: Path,
    *,
    min_area: int = 8,
    max_area: int = 500,
    min_edge: int = 3,
    max_edge: int = 30,
    require_isolated: bool = True,
) -> list[tuple[int, tuple[int, int, int, int], float]]:
    image = Image.open(path).convert("RGBA")
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
        pad = max(4, round(max(width, height) * 0.75))
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
        solid_square = fill > 0.98 and max(width, height) <= max_edge // 2
        if (
            min_area <= area <= max_area
            and min_edge <= width <= max_edge
            and min_edge <= height <= max_edge
            and fill > 0.75
            and squareish
            and (isolated or solid_square or not require_isolated)
        ):
            blocks.append((area, bbox, fill))
    return sorted(blocks, reverse=True)


class WhiteBlockArtifactTest(unittest.TestCase):
    def test_37_skin_spritesheets_do_not_have_compact_white_block_artifacts(self) -> None:
        for package_name in REGRESSION_PACKAGES:
            with self.subTest(package_name=package_name):
                path = ROOT / "pets" / package_name / "spritesheet.webp"
                blocks = compact_white_blocks(path)
                self.assertEqual([], blocks[:10])

    def test_37_skin_detail_spritesheets_do_not_have_scaled_white_block_artifacts(self) -> None:
        for package_name in REGRESSION_PACKAGES:
            with self.subTest(package_name=package_name):
                path = ROOT / "docs" / "assets" / "detail-spritesheets" / f"{package_name}.webp"
                blocks = compact_white_blocks(
                    path,
                    min_area=300,
                    max_area=8000,
                    min_edge=16,
                    max_edge=140,
                    require_isolated=False,
                )
                self.assertEqual([], blocks[:10])

    def test_37_skin_site_asset_versions_match_current_files(self) -> None:
        data = json.loads((ROOT / "docs" / "data" / "pets.json").read_text(encoding="utf-8"))
        entries = {entry["packageName"]: entry for entry in data["pets"] + data.get("cuteVariants", [])}

        for package_name in REGRESSION_PACKAGES:
            with self.subTest(package_name=package_name):
                entry = entries[package_name]
                versions = entry.get("assetVersions", {})
                for field in ("download", "preview", "spritesheet", "detailSpritesheet", "sourceImage"):
                    url = entry.get(field)
                    if not url or "://" in url or url.startswith("#"):
                        continue
                    path = ROOT / "docs" / str(url).split("#", 1)[0].split("?", 1)[0]
                    expected = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
                    self.assertEqual(expected, versions.get(url), f"{package_name} {url}")


if __name__ == "__main__":
    unittest.main()
