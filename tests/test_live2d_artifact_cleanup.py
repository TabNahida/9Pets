from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tools.build_pets_site import (
    LIVE2D_RENDER_PROFILES,
    STATE_ROWS,
    make_atlas_from_live2d_frames,
    remove_compact_white_block_artifacts,
)


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

    def test_37_white_block_skins_hide_bad_live2d_drawables(self) -> None:
        expected = {
            "9Pets-37-A-Gift-of-Nourishment": ["bone1"],
            "9Pets-37-A-Prime-Number": ["bone1", "bone2", "bone3", "bone4"],
            "9Pets-37-Happy-Bird-Catcher": ["bone1", "bone2", "bone3", "bone4"],
            "9Pets-37-Down-in-the-Grotto": ["bone1", "bone2", "bone3", "bone4", "bone5", "bone6"],
        }
        for package_name, hidden in expected.items():
            with self.subTest(package_name=package_name):
                self.assertEqual(hidden, LIVE2D_RENDER_PROFILES[package_name]["hiddenDrawables"])

    def test_live2d_atlas_generation_applies_white_block_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            frames_root = Path(temp_dir) / "9Pets-37-A-Prime-Number"
            for state, frame_count in STATE_ROWS:
                state_dir = frames_root / state
                state_dir.mkdir(parents=True)
                for index in range(frame_count):
                    frame = Image.new("RGBA", (240, 240), (0, 0, 0, 0))
                    for y in range(80, 100):
                        for x in range(90, 110):
                            frame.putpixel((x, y), (255, 255, 255, 255))
                    frame.save(state_dir / f"{index:02d}.png")

            atlas = make_atlas_from_live2d_frames(frames_root)

        self.assertIsNone(atlas.getchannel("A").getbbox())


if __name__ == "__main__":
    unittest.main()
