from __future__ import annotations

import unittest
from pathlib import Path
from unittest import mock

from tools import audit_skin_cutes as audit
from tools import build_pets_site as site


class AuditSkinCuteStagingTest(unittest.TestCase):
    def test_deterministic_qa_runs_cute_white_block_scan(self) -> None:
        with (
            mock.patch.object(audit.pet_qa, "raw_frame_qa") as raw_frame,
            mock.patch.object(audit.pet_qa, "pixel_qa") as pixel,
            mock.patch.object(audit.pet_qa, "visible_color_qa") as visible_color,
            mock.patch.object(audit.pet_qa, "white_block_artifact_qa") as white_block,
            mock.patch.object(audit.pet_qa, "make_contact", return_value=Path("contact.png")) as make_contact,
        ):
            contact = audit.deterministic_qa("9Pets-Cute-Test-Skin")

        self.assertEqual(Path("contact.png"), contact)
        raw_frame.assert_called_once_with(["9Pets-Cute-Test-Skin"])
        pixel.assert_called_once_with(["9Pets-Cute-Test-Skin"])
        visible_color.assert_called_once_with(["9Pets-Cute-Test-Skin"])
        white_block.assert_called_once_with(["9Pets-Cute-Test-Skin"], animation_modes={"official-cute-spine"})
        make_contact.assert_called_once_with("9Pets-Cute-Test-Skin")

    def test_detail_page_qa_waits_for_sprite_background_before_checking(self) -> None:
        package_name = "9Pets-Cute-Test-Delayed-Skin"
        row = {
            "cute_package": package_name,
            "skin": "Delayed Skin",
        }

        class FakeLocator:
            def __init__(self, page: "FakePage", selector: str) -> None:
                self.page = page
                self.selector = selector

            def evaluate(self, script: str) -> str:
                if self.selector == ".detail-sprite" and self.page.sprite_waited:
                    return f'url("http://example.test/assets/detail-spritesheets/{package_name}.webp?v=123")'
                return "none"

            def get_attribute(self, name: str) -> str:
                if self.selector == "a[download]":
                    return f"downloads/{package_name}.zip?v=123"
                if self.selector == "#sourceImage":
                    return f"assets/source/{package_name}.png?v=123"
                return ""

        class FakeButton:
            def __init__(self, page: "FakePage") -> None:
                self.page = page

            def click(self) -> None:
                self.page.wave_active = True

            def get_attribute(self, name: str) -> str:
                return "active" if self.page.wave_active else ""

        class FakePage:
            def __init__(self, kind: str) -> None:
                self.kind = kind
                self.sprite_waited = False
                self.wave_active = False

            def set_viewport_size(self, size: dict[str, int]) -> None:
                return

            def goto(self, url: str, wait_until: str) -> None:
                return

            def wait_for_selector(self, selector: str) -> None:
                return

            def evaluate(self, script: str, args: list[str]) -> dict[str, str | bool]:
                return {
                    "hasVariant": True,
                    "animationMode": "official-cute-spine",
                    "skinDisplayName": "-- Delayed Skin",
                    "expectedSkinDisplay": "-- Delayed Skin",
                }

            def wait_for_function(self, script: str, *, arg: str, timeout: int) -> None:
                self.sprite_waited = True

            def locator(self, selector: str) -> FakeLocator:
                return FakeLocator(self, selector)

            def get_by_role(self, role: str, name: str) -> FakeButton:
                return FakeButton(self)

            def close(self) -> None:
                return

        class FakeContext:
            def __init__(self) -> None:
                self.pages = [FakePage("catalog"), FakePage("detail")]

            def new_page(self) -> FakePage:
                return self.pages.pop(0)

        session = audit.PageQaSession()
        session.context = FakeContext()

        session.check("http://example.test", row)

    def test_stage_paths_include_skin_spine_cache(self) -> None:
        row = {
            "cute_package": "9Pets-Cute-37-A-Prime-Number",
            "spine_path": "roles/v1a4_306602_37",
        }

        paths = audit.stage_paths_for_row(row)

        self.assertIn("docs/index.html", paths)
        self.assertIn("docs/pet.html", paths)
        self.assertIn("assets/source-cache/Reverse-1999-CN-Asset/roles/v1a4_306602_37", paths)

    def test_entrypoint_and_package_files_are_allowed_when_staged(self) -> None:
        row = {
            "cute_package": "9Pets-Cute-37-A-Prime-Number",
            "spine_path": "roles/v1a4_306602_37",
        }

        unexpected = audit.unexpected_staged_paths(
            [
                "docs/index.html",
                "docs/pet.html",
                "docs/data/pets.json",
                "docs/data/pets-data.js",
                "docs/assets/spritesheets/9Pets-Cute-37-A-Prime-Number.webp",
                "assets/source-cache/Reverse-1999-CN-Asset/roles/v1a4_306602_37/306602_37_fight.skel",
            ],
            row,
        )

        self.assertEqual([], unexpected)

    def test_non_default_skin_does_not_inherit_default_cute_override(self) -> None:
        info = site.cute_source_info(
            {
                "skinName": "Order of St. Gabriel",
                "isDefaultSkin": False,
                "spinePath": "roles/300702_weixiukai",
                "spineUrl": site.repo_tree_url("roles/300702_weixiukai"),
            },
            "9Pets-Cute-A-Knight-Order-of-St-Gabriel",
            "assets/source/9Pets-Cute-A-Knight-Order-of-St-Gabriel.png",
            "9Pets-Cute-A-Knight",
        )

        self.assertEqual("roles/300702_weixiukai", info["spinePath"])

    def test_default_skin_can_inherit_default_cute_override(self) -> None:
        info = site.cute_source_info(
            {
                "skinName": "Default",
                "isDefaultSkin": True,
                "spinePath": "roles/300701_weixiukai_s",
                "spineUrl": site.repo_tree_url("roles/300701_weixiukai_s"),
            },
            "9Pets-Cute-A-Knight-Default",
            "assets/source/9Pets-Cute-A-Knight-Default.png",
            "9Pets-Cute-A-Knight",
        )

        self.assertEqual("roles/300701_weixiukai", info["spinePath"])

    def test_exact_spine_profile_merges_with_default_skin_skeleton(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-A-Knight-Galloping-Across-the-Times",
            "roles/v1a6_300703_wxk",
            "9Pets-Cute-A-Knight",
        )

        self.assertEqual("300703_wxk_fight.skel", profile["skeleton"])
        self.assertEqual(1600, profile["width"])
        self.assertEqual(800, profile["x"])

    def test_default_spine_profile_prefers_asset_id_matching_files(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Aleph-A-Feast-of-Imagery",
            "roles/v3a1_311303_alf",
            "9Pets-Cute-Aleph",
        )

        self.assertEqual("311303_alf_fight.skel", profile["skeleton"])
        self.assertEqual("311303_alf.atlas", profile["atlas"])

    def test_exact_spine_profile_inherits_character_layout(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-APPLe-Erudite-and-Juicy",
            "roles/302802_apple",
            "9Pets-Cute-APPLe",
        )

        self.assertEqual("302802_apple_fight.skel", profile["skeleton"])
        self.assertEqual(1600, profile["width"])
        self.assertEqual(800, profile["x"])
        self.assertEqual(1900, profile["height"])
        self.assertEqual(1350, profile["y"])

    def test_skin_spine_profile_inherits_character_motion_map(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Click-The-Best-Angle",
            "roles/304902_kachakacha",
            "9Pets-Cute-Click",
        )

        self.assertEqual("giddy", profile["motionMap"]["jumping"])
        self.assertEqual("skill2", profile["motionMap"]["running"])

    def test_cristallo_stained_glass_profile_has_extra_top_headroom(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Cristallo-A-Dream-in-Stained-Glass",
            "roles/v3a1_303103_qbl",
            "9Pets-Cute-Cristallo",
        )

        self.assertEqual(1000, profile["y"])
        self.assertEqual("unique", profile["motionMap"]["review"])

    def test_jessica_voyage_profile_has_horizontal_headroom(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Jessica-Voyage-from-your-Bed",
            "roles/v1a9_305603_jiexika",
            "9Pets-Cute-Jessica",
        )

        self.assertEqual("305603_jiexika_fight.skel", profile["skeleton"])
        self.assertEqual("305603_jiexika.atlas", profile["atlas"])
        self.assertEqual(1600, profile["width"])
        self.assertEqual(800, profile["x"])

    def test_nautika_behind_unknown_profile_has_top_headroom(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Nautika-Behind-the-Unknown",
            "roles/v2a8_312002_ndk",
            "9Pets-Cute-Nautika",
        )

        self.assertEqual("312002_ndk_fight.skel", profile["skeleton"])
        self.assertEqual("312002_ndk.atlas", profile["atlas"])
        self.assertEqual(1800, profile["width"])
        self.assertEqual(1400, profile["height"])
        self.assertEqual(700, profile["x"])
        self.assertEqual(1000, profile["y"])

    def test_nautika_from_darkness_light_profile_has_large_canvas(self) -> None:
        profile = site.spine_render_profile_for(
            "9Pets-Cute-Nautika-From-Darkness-Light",
            "roles/v3a7_312003_ndk",
            "9Pets-Cute-Nautika",
        )

        self.assertEqual("312003_ndk_fight.skel", profile["skeleton"])
        self.assertEqual("312003_ndk.atlas", profile["atlas"])
        self.assertEqual(2400, profile["width"])
        self.assertEqual(2200, profile["height"])
        self.assertEqual(900, profile["x"])
        self.assertEqual(1700, profile["y"])

    def test_cute_base_source_info_can_be_metadata_only(self) -> None:
        official_index = site.load_official_asset_index()
        item = site.find_catalog_item(site.read_catalog(), "APPLe")
        skin = site.find_skin_entry(item, official_index, explicit_skin="302802")

        info = site.base_source_info_for_cute(
            "APPLe",
            "9Pets-APPLe-Erudite-and-Juicy",
            None,
            official_index,
            skin,
        )

        self.assertEqual("302802", info["assetId"])
        self.assertEqual("roles/302802_apple", info["spinePath"])


if __name__ == "__main__":
    unittest.main()
