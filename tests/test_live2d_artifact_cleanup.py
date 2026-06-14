from __future__ import annotations

import unittest

from PIL import Image

from tools.build_pets_site import remove_compact_white_block_artifacts


class Live2DArtifactCleanupTest(unittest.TestCase):
    def test_removes_detached_white_block_on_transparent_background(self) -> None:
        image = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        for y in range(40, 60):
            for x in range(50, 70):
                image.putpixel((x, y), (255, 255, 255, 255))

        cleaned = remove_compact_white_block_artifacts(image, "9Pets-37-A-Prime-Number")

        self.assertIsNone(cleaned.getchannel("A").getbbox())

    def test_preserves_embedded_white_highlight_inside_visible_character_pixels(self) -> None:
        image = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        for y in range(30, 90):
            for x in range(30, 90):
                image.putpixel((x, y), (80, 150, 160, 255))
        for y in range(50, 70):
            for x in range(50, 70):
                image.putpixel((x, y), (255, 255, 255, 255))

        cleaned = remove_compact_white_block_artifacts(image, "9Pets-37-A-Prime-Number")

        white_pixels = sum(
            1
            for y in range(50, 70)
            for x in range(50, 70)
            if cleaned.getpixel((x, y))[3] > 0
        )
        self.assertEqual(400, white_pixels)


if __name__ == "__main__":
    unittest.main()
