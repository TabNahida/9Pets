from __future__ import annotations

import unittest

from tools import verify_build


class VerifyBuildCuteLinkTest(unittest.TestCase):
    def test_missing_normal_package_is_allowed_when_link_is_self_consistent(self) -> None:
        verify_build.check_cute_normal_link(
            {
                "packageName": "9Pets-Cute-A-Knight-Galloping-Across-the-Times",
                "normalPackageName": "9Pets-A-Knight-Galloping-Across-the-Times",
                "normalId": "9pets-a-knight-galloping-across-the-times",
                "isDefaultSkin": False,
            },
            normal_ids=set(),
            normal_packages=set(),
        )

    def test_missing_default_normal_package_is_rejected_unless_hidden(self) -> None:
        with self.assertRaisesRegex(AssertionError, "missing default normal package"):
            verify_build.check_cute_normal_link(
                {
                    "packageName": "9Pets-Cute-Matilda-Default",
                    "normalPackageName": "9Pets-Matilda-Default",
                    "normalId": "9pets-matilda-default",
                    "isDefaultSkin": True,
                },
                normal_ids=set(),
                normal_packages=set(),
            )

    def test_hidden_missing_default_normal_package_is_allowed(self) -> None:
        verify_build.check_cute_normal_link(
            {
                "packageName": "9Pets-Cute-Baby-Blue-Default",
                "normalPackageName": "9Pets-Baby-Blue-Default",
                "normalId": "9pets-baby-blue-default",
                "isDefaultSkin": True,
            },
            normal_ids=set(),
            normal_packages=set(),
        )

    def test_existing_normal_package_must_have_matching_normal_id(self) -> None:
        with self.assertRaisesRegex(AssertionError, "unknown normal pet"):
            verify_build.check_cute_normal_link(
                {
                    "packageName": "9Pets-Cute-Matilda-Default",
                    "normalPackageName": "9Pets-Matilda-Default",
                    "normalId": "9pets-matilda-default",
                },
                normal_ids=set(),
                normal_packages={"9Pets-Matilda-Default"},
            )

    def test_normal_package_name_must_match_cute_package_name(self) -> None:
        with self.assertRaisesRegex(AssertionError, "normal package link"):
            verify_build.check_cute_normal_link(
                {
                    "packageName": "9Pets-Cute-Matilda-Default",
                    "normalPackageName": "9Pets-Sonetto-Default",
                    "normalId": "9pets-sonetto-default",
                },
                normal_ids={"9pets-sonetto-default"},
                normal_packages={"9Pets-Sonetto-Default"},
            )


if __name__ == "__main__":
    unittest.main()
