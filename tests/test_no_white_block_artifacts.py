from __future__ import annotations

import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REGRESSION_PACKAGES = [
    "9Pets-37-A-Prime-Number",
    "9Pets-37-Happy-Bird-Catcher",
    "9Pets-37-Down-in-the-Grotto",
    "9Pets-37-A-Gift-of-Nourishment",
]


def compact_white_blocks(path: Path) -> list[tuple[int, tuple[int, int, int, int], float]]:
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
        if 8 <= area <= 500 and 3 <= width <= 30 and 3 <= height <= 30 and fill > 0.75 and squareish and isolated:
            blocks.append((area, bbox, fill))
    return sorted(blocks, reverse=True)


class WhiteBlockArtifactTest(unittest.TestCase):
    def test_37_skin_spritesheets_do_not_have_compact_white_block_artifacts(self) -> None:
        for package_name in REGRESSION_PACKAGES:
            with self.subTest(package_name=package_name):
                path = ROOT / "pets" / package_name / "spritesheet.webp"
                blocks = compact_white_blocks(path)
                self.assertEqual([], blocks[:10])


if __name__ == "__main__":
    unittest.main()
