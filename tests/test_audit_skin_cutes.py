from __future__ import annotations

import unittest

from tools import audit_skin_cutes as audit
from tools import build_pets_site as site


class AuditSkinCuteStagingTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
