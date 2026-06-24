from __future__ import annotations

import argparse
import functools
import http.server
import json
import re
import socket
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

import build_pets_site as site
import rebuild_one_pet as pet_qa


ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "PET_SKIN_BUILD_TODO.md"


def run(command: list[str], *, timeout: int | None = None) -> str:
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=timeout, check=False)
    output = (completed.stdout or "") + (completed.stderr or "")
    if output.strip():
        print(output.strip(), flush=True)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")
    return output


def todo_line_for_asset(asset_id: str) -> str:
    pattern = re.compile(rf"^\| .+ \| `{re.escape(asset_id)}` \| .+$", re.MULTILINE)
    match = pattern.search(TODO.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"Could not find TODO row for asset {asset_id}")
    return match.group(0)


def todo_cells(asset_id: str) -> list[str]:
    return [cell.strip() for cell in todo_line_for_asset(asset_id).strip().strip("|").split("|")]


def todo_cute_done(asset_id: str) -> bool:
    cells = todo_cells(asset_id)
    return len(cells) >= 8 and cells[7] == "[x]"


def update_todo_row(*, row: dict[str, Any], qa_note: str) -> None:
    text = TODO.read_text(encoding="utf-8")
    line = todo_line_for_asset(row["asset_id"])
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) < 13:
        raise RuntimeError(f"Unexpected TODO row shape for asset {row['asset_id']}")
    cells[7] = "[x]"
    cells[8] = "[x]"
    cells[9] = "[x]"
    cells[10] = "[x]"
    cells[11] = "[x]"
    cells[0] = "[x]" if all(cells[index] == "[x]" for index in range(6, 12)) else "[ ]"
    note = cells[12]
    cute_note = f"Cute built from cached chibi Spine `{row['spine_path']}`; QA passed: {qa_note}"
    if "Cute pending" in note:
        note = note.replace("Cute pending", cute_note)
    elif "Cute built from cached chibi Spine" in note:
        note = re.sub(r"Cute built from cached chibi Spine `[^`]+`; QA passed: .*$", cute_note, note)
    else:
        note = f"{note}; {cute_note}" if note else cute_note
    cells[12] = note
    replacement = "| " + " | ".join(cells) + " |"
    updated = text.replace(line, replacement, 1)
    TODO.write_text(updated, encoding="utf-8")


def refresh_site_data() -> None:
    site_data_path = site.DATA_DIR / "pets.json"
    if not site_data_path.exists():
        raise RuntimeError("Cute skin audit requires existing docs/data/pets.json")
    site_data = json.loads(site_data_path.read_text(encoding="utf-8"))
    pets = site.visible_normal_pets(site_data.get("pets", []))
    catalog = site.read_catalog()
    official_index = site.load_official_asset_index()
    site_data["total"] = len(pets)
    site_data["pets"] = sorted(pets, key=site.package_sort_key)
    cute_variants = site.build_cute_variants(pets, catalog, official_index)
    site_data["cuteTotal"] = len(cute_variants)
    site_data["cuteVariants"] = cute_variants
    site.write_site_data(site_data)


def load_variant(package_name: str) -> dict[str, Any]:
    data = json.loads((ROOT / "docs" / "data" / "pets.json").read_text(encoding="utf-8"))
    for variant in data.get("cuteVariants", []):
        if variant["packageName"] == package_name:
            return variant
    raise RuntimeError(f"{package_name} missing from cuteVariants")


def deterministic_qa(package_name: str) -> Path:
    pet_qa.raw_frame_qa([package_name])
    pet_qa.pixel_qa([package_name])
    pet_qa.visible_color_qa([package_name])
    pet_qa.white_block_artifact_qa([package_name], animation_modes={"official-cute-spine"})
    return pet_qa.make_contact(package_name)


class StaticServer:
    def __enter__(self) -> str:
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = int(sock.getsockname()[1])
        class QuietHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format: str, *args: object) -> None:
                return

        class QuietServer(http.server.ThreadingHTTPServer):
            def handle_error(self, request: object, client_address: object) -> None:
                return

        handler = functools.partial(QuietHandler, directory=str(ROOT / "docs"))
        self.server = QuietServer(("127.0.0.1", port), handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        return f"http://127.0.0.1:{port}"

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.server.shutdown()
        self.server.server_close()


class PageQaSession:
    def __enter__(self) -> "PageQaSession":
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context()
        self.context.route(
            "**/*",
            lambda route: route.abort()
            if route.request.resource_type in {"image", "font", "media"}
            else route.continue_(),
        )
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def check(self, base_url: str, row: dict[str, Any]) -> None:
        package_name = row["cute_package"]
        pet_id = site.pet_id_from_package(package_name)
        page = self.context.new_page()
        page.set_viewport_size({"width": 1440, "height": 1000})
        page.goto(f"{base_url}/index.html?variant=cute#catalog", wait_until="domcontentloaded")
        page.wait_for_selector(".pet-card")
        catalog = page.evaluate(
            """([packageName, skinName]) => {
                const data = window.NINEPETS_DATA;
                const variant = data.cuteVariants.find((item) => item.packageName === packageName);
                return {
                  hasVariant: Boolean(variant),
                  animationMode: variant && variant.animationMode,
                  skinDisplayName: variant && variant.skinDisplayName,
                  expectedSkinDisplay: `-- ${skinName}`,
                };
            }""",
            [package_name, row["skin"]],
        )
        page.close()
        if not catalog["hasVariant"]:
            raise AssertionError(f"{package_name} missing from cute catalog manifest")
        if catalog["animationMode"] != "official-cute-spine":
            raise AssertionError(f"{package_name} catalog mode is {catalog['animationMode']}")
        if catalog["skinDisplayName"] != catalog["expectedSkinDisplay"]:
            raise AssertionError(f"{package_name} skin label is {catalog['skinDisplayName']}")

        detail = self.context.new_page()
        detail.set_viewport_size({"width": 1440, "height": 1000})
        detail.goto(f"{base_url}/pet.html?id={pet_id}", wait_until="domcontentloaded")
        detail.wait_for_selector(".detail-sprite")
        detail.wait_for_function(
            """packageName => {
                const sprite = document.querySelector(".detail-sprite");
                return Boolean(sprite)
                    && getComputedStyle(sprite).backgroundImage.includes(`detail-spritesheets/${packageName}.webp`);
            }""",
            arg=package_name,
            timeout=10_000,
        )
        sprite_image = detail.locator(".detail-sprite").evaluate("node => getComputedStyle(node).backgroundImage")
        if f"detail-spritesheets/{package_name}.webp" not in sprite_image:
            raise AssertionError(f"{package_name} detail page uses wrong sprite: {sprite_image}")
        download_href = detail.locator("a[download]").get_attribute("href") or ""
        if f"downloads/{package_name}.zip" not in download_href:
            raise AssertionError(f"{package_name} download link is wrong: {download_href}")
        source_image = detail.locator("#sourceImage").get_attribute("src") or ""
        if f"assets/source/{package_name}.png" not in source_image:
            raise AssertionError(f"{package_name} detail page uses wrong source image: {source_image}")
        detail.get_by_role("button", name="Wave").click()
        if "active" not in (detail.get_by_role("button", name="Wave").get_attribute("class") or ""):
            raise AssertionError(f"{package_name} Wave tab did not activate")
        detail.close()


def skin_rows() -> list[dict[str, Any]]:
    catalog = site.read_catalog()
    official_index = site.load_official_asset_index()
    rows: list[dict[str, Any]] = []
    for item in catalog["characters"]:
        name = item["name"]
        for skin in site.official_skin_entries(name, official_index):
            skin_name = site.skin_name_from_entry(skin)
            if site.is_default_skin_name(skin_name):
                continue
            asset = site.resolve_official_asset(name, official_index, skin)
            spine_path = asset.get("spinePath", "")
            package_name = site.package_name_for(name, skin_name, cute=True)
            profile_package = site.base_profile_package_name(name, cute=True)
            if not site.spine_render_ready(package_name, spine_path, profile_package):
                continue
            rows.append(
                {
                    "character": name,
                    "skin": skin_name,
                    "asset_id": str(skin.get("id", "")),
                    "normal_package": site.package_name_for(name, skin_name),
                    "cute_package": package_name,
                    "spine_path": spine_path,
                }
            )
    return rows


def stage_paths_for_row(row: dict[str, Any]) -> list[str]:
    package_name = row["cute_package"]
    return [
        "PET_SKIN_BUILD_TODO.md",
        "docs/index.html",
        "docs/pet.html",
        "docs/data/pets.json",
        "docs/data/pets-data.js",
        f"docs/assets/previews/{package_name}.png",
        f"docs/assets/source/{package_name}.png",
        f"docs/assets/spritesheets/{package_name}.webp",
        f"docs/assets/detail-spritesheets/{package_name}.webp",
        f"docs/downloads/{package_name}.zip",
        f"pets/{package_name}",
        f"assets/source-cache/Reverse-1999-CN-Asset/{row['spine_path']}",
    ]


def unexpected_staged_paths(staged: list[str], row: dict[str, Any]) -> list[str]:
    package_name = row["cute_package"]
    spine_prefix = f"assets/source-cache/Reverse-1999-CN-Asset/{row['spine_path']}"
    return [
        path
        for path in staged
        if not (
            path == "PET_SKIN_BUILD_TODO.md"
            or path == "docs/index.html"
            or path == "docs/pet.html"
            or path.startswith("docs/data/pets")
            or package_name in path
            or path.startswith(spine_prefix)
        )
    ]


def stage_and_commit(row: dict[str, Any]) -> None:
    run(["git", "add", "--", *stage_paths_for_row(row)], timeout=180)
    staged = run(["git", "diff", "--cached", "--name-only"], timeout=60).splitlines()
    unexpected = unexpected_staged_paths(staged, row)
    if unexpected:
        raise RuntimeError(f"Unexpected staged paths for {row['cute_package']}: {unexpected[:10]}")
    if not staged:
        print(f"No staged changes for {row['cute_package']}", flush=True)
        return
    run(["git", "commit", "-m", f"Audit {row['character']} {row['skin']} cute skin"], timeout=180)


def audit_row(
    row: dict[str, Any],
    base_url: str,
    page_qa: PageQaSession,
    *,
    reuse_existing: bool = False,
    force: bool = False,
) -> None:
    package_name = row["cute_package"]
    if todo_cute_done(row["asset_id"]) and not force:
        print(f"skipping already-audited Cute {package_name}", flush=True)
        return
    print(f"auditing {package_name} ({row['asset_id']})", flush=True)
    package_exists = (site.PETS_DIR / package_name / "spritesheet.webp").exists()
    build_output = ""
    if not (reuse_existing and package_exists):
        build_output = run(
            [
                sys.executable,
                str(ROOT / "tools" / "build_pets_site.py"),
                "--cute-only",
                row["character"],
                "--skin",
                row["asset_id"],
            ],
            timeout=600,
        )
    else:
        refresh_site_data()
        print(f"reused existing package {package_name}", flush=True)
    variant = load_variant(package_name)
    if variant.get("animationMode") != "official-cute-spine":
        raise AssertionError(f"{package_name} built as {variant.get('animationMode')}")
    contact = deterministic_qa(package_name)
    page_qa.check(base_url, row)
    qa_note = "raw frame bounds, pixel/transparent cells, visible color, white block artifact, contact sheet, catalog/detail/download page"
    motions = pet_qa.parse_motion_lines(build_output)
    if motions:
        qa_note += f"; animations: {motions}"
    qa_note += f"; contact: {contact.relative_to(ROOT).as_posix()}"
    update_todo_row(row=row, qa_note=qa_note)
    stage_and_commit(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit cached non-default Cute Spine skin packages.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--only-id")
    parser.add_argument("--reuse-existing", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    rows = skin_rows()
    if args.only_id:
        rows = [row for row in rows if row["asset_id"] == args.only_id]
    else:
        rows = rows if args.force else [row for row in rows if not todo_cute_done(row["asset_id"])]
    if args.limit > 0:
        rows = rows[: args.limit]
    if not rows:
        print("No buildable pending Cute skins found.")
        return

    with StaticServer() as base_url, PageQaSession() as page_qa:
        for row in rows:
            audit_row(row, base_url, page_qa, reuse_existing=args.reuse_existing, force=args.force)


if __name__ == "__main__":
    main()
