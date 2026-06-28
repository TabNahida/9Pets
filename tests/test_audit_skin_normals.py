from __future__ import annotations

import unittest

from tools import audit_skin_normals as audit
from tools import build_pets_site as site


class AuditSkinNormalStagingTest(unittest.TestCase):
    def test_catalog_selector_prefers_exact_match_over_short_prefix(self) -> None:
        catalog = site.read_catalog()
        item = site.find_catalog_item(catalog, "Jessica")

        self.assertEqual("Jessica", item["name"])

    def test_stage_paths_include_entrypoint_hash_files(self) -> None:
        paths = audit.stage_paths_for_package(
            "9Pets-Argus-All-Seeing-Light",
            "live2d/roles/v2a1_309702_aegs",
        )

        self.assertIn("docs/index.html", paths)
        self.assertIn("docs/pet.html", paths)

    def test_entrypoint_hash_files_are_allowed_when_staged(self) -> None:
        unexpected = audit.unexpected_staged_paths(
            [
                "docs/index.html",
                "docs/pet.html",
                "docs/data/pets.json",
                "docs/data/pets-data.js",
            ],
            "9Pets-Argus-All-Seeing-Light",
            "live2d/roles/v2a1_309702_aegs",
        )

        self.assertEqual([], unexpected)


if __name__ == "__main__":
    unittest.main()
