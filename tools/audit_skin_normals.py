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


def todo_normal_done(asset_id: str) -> bool:
    line = todo_line_for_asset(asset_id)
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return len(cells) >= 7 and cells[6] == "[x]"


def update_todo_row(
    *,
    asset_id: str,
    character: str,
    skin_name: str,
    normal_package: str,
    cute_package: str,
    cubism_path: str,
    qa_note: str,
) -> None:
    text = TODO.read_text(encoding="utf-8")
    replacement = (
        f"| [ ] | {character} | {skin_name} | `{asset_id}` | `{normal_package}` | `{cute_package}` | "
        f"[x] | [ ] | [x] | [x] | [x] | [x] | "
        f"Normal built from cached Live2D `{cubism_path}`; QA passed: {qa_note}; Cute pending |"
    )
    pattern = re.compile(rf"^\| .+ \| `{re.escape(asset_id)}` \| .+$", re.MULTILINE)
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Could not update TODO row for asset {asset_id}")
    TODO.write_text(updated, encoding="utf-8")


def load_pet(package_name: str) -> dict[str, Any]:
    data = json.loads((ROOT / "docs" / "data" / "pets.json").read_text(encoding="utf-8"))
    return next(pet for pet in data["pets"] if pet["packageName"] == package_name)


def deterministic_qa(package_name: str) -> Path:
    run([sys.executable, str(ROOT / "tools" / "verify_build.py")], timeout=180)
    pet_qa.raw_frame_qa([package_name])
    pet_qa.pixel_qa([package_name])
    pet_qa.visible_color_qa([package_name])
    return pet_qa.make_contact(package_name)


class StaticServer:
    def __enter__(self) -> str:
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = int(sock.getsockname()[1])
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "docs"))
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        return f"http://127.0.0.1:{port}"

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.server.shutdown()
        self.server.server_close()


def page_qa(base_url: str, package_name: str, pet_id: str, skin_name: str) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        page.goto(f"{base_url}/index.html", wait_until="networkidle")
        page.wait_for_selector(".pet-card")
        catalog = page.evaluate(
            """([packageName, skinName]) => {
                const data = window.NINEPETS_DATA;
                const pet = data.pets.find((item) => item.packageName === packageName);
                const card = [...document.querySelectorAll(".pet-card")]
                  .find((node) => node.textContent.includes(packageName));
                return {
                  hasPet: Boolean(pet),
                  animationMode: pet && pet.animationMode,
                  skinDisplayName: pet && pet.skinDisplayName,
                  cardText: card ? card.textContent.replace(/\\s+/g, " ").trim() : "",
                  expectedSkinDisplay: `-- ${skinName}`,
                };
            }""",
            [package_name, skin_name],
        )
        if not catalog["hasPet"]:
            raise AssertionError(f"{package_name} missing from catalog manifest")
        if catalog["animationMode"] != "official-live2d-cubism":
            raise AssertionError(f"{package_name} catalog mode is {catalog['animationMode']}")
        if catalog["skinDisplayName"] != catalog["expectedSkinDisplay"]:
            raise AssertionError(f"{package_name} skin label is {catalog['skinDisplayName']}")
        if package_name not in catalog["cardText"]:
            raise AssertionError(f"{package_name} card not rendered")

        detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        detail.goto(f"{base_url}/pet.html?id={pet_id}", wait_until="networkidle")
        detail.wait_for_selector(".detail-sprite")
        sprite_image = detail.locator(".detail-sprite").evaluate("node => getComputedStyle(node).backgroundImage")
        if f"detail-spritesheets/{package_name}.webp" not in sprite_image:
            raise AssertionError(f"{package_name} detail page uses wrong sprite: {sprite_image}")
        download_href = detail.locator("a[download]").get_attribute("href") or ""
        if f"downloads/{package_name}.zip" not in download_href:
            raise AssertionError(f"{package_name} download link is wrong: {download_href}")
        detail.get_by_role("button", name="Wave").click()
        if "active" not in (detail.get_by_role("button", name="Wave").get_attribute("class") or ""):
            raise AssertionError(f"{package_name} Wave tab did not activate")
        browser.close()


def stage_and_commit(package_name: str, cubism_path: str, message: str) -> None:
    paths = [
        "PET_SKIN_BUILD_TODO.md",
        "docs/data/pets.json",
        "docs/data/pets-data.js",
        f"docs/assets/previews/{package_name}.png",
        f"docs/assets/source/{package_name}.png",
        f"docs/assets/spritesheets/{package_name}.webp",
        f"docs/assets/detail-spritesheets/{package_name}.webp",
        f"docs/downloads/{package_name}.zip",
        f"pets/{package_name}",
        f"assets/source-cache/Reverse-1999-CN-Asset/{cubism_path}",
    ]
    run(["git", "add", "--", *paths], timeout=180)
    staged = run(["git", "diff", "--cached", "--name-only"], timeout=60).splitlines()
    unexpected = [
        path
        for path in staged
        if not (
            path == "PET_SKIN_BUILD_TODO.md"
            or path.startswith("docs/data/pets")
            or package_name in path
            or path.startswith(f"assets/source-cache/Reverse-1999-CN-Asset/{cubism_path}")
        )
    ]
    if unexpected:
        raise RuntimeError(f"Unexpected staged paths for {package_name}: {unexpected[:10]}")
    run(["git", "commit", "-m", message], timeout=180)


def buildable_skin_rows() -> list[dict[str, Any]]:
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
            cubism_path = asset.get("cubismPath", "")
            if not site.live2d_model_cached(cubism_path):
                continue
            rows.append(
                {
                    "character": name,
                    "skin": skin_name,
                    "asset_id": str(skin.get("id", "")),
                    "normal_package": site.package_name_for(name, skin_name),
                    "cute_package": site.package_name_for(name, skin_name, cute=True),
                    "cubism_path": cubism_path,
                    "pet_id": site.pet_id_from_package(site.package_name_for(name, skin_name)),
                }
            )
    return rows


def audit_row(row: dict[str, Any], base_url: str) -> None:
    if todo_normal_done(row["asset_id"]):
        print(f"skipping already-audited Normal {row['normal_package']}", flush=True)
        return
    print(f"auditing {row['normal_package']} ({row['asset_id']})", flush=True)
    build_output = run(
        [
            sys.executable,
            str(ROOT / "tools" / "build_pets_site.py"),
            "--only",
            row["character"],
            "--skin",
            row["asset_id"],
        ],
        timeout=600,
    )
    pet = load_pet(row["normal_package"])
    if pet.get("animationMode") != "official-live2d-cubism":
        raise AssertionError(f"{row['normal_package']} built as {pet.get('animationMode')}")
    contact = deterministic_qa(row["normal_package"])
    page_qa(base_url, row["normal_package"], row["pet_id"], row["skin"])
    qa_note = (
        "verify_build, raw frame bounds, pixel/transparent cells, visible color, contact sheet, "
        "catalog/detail/download page"
    )
    motions = pet_qa.parse_motion_lines(build_output)
    if motions:
        qa_note += f"; motions: {motions}"
    qa_note += f"; contact: {contact.relative_to(ROOT).as_posix()}"
    update_todo_row(
        asset_id=row["asset_id"],
        character=row["character"],
        skin_name=row["skin"],
        normal_package=row["normal_package"],
        cute_package=row["cute_package"],
        cubism_path=row["cubism_path"],
        qa_note=qa_note,
    )
    stage_and_commit(row["normal_package"], row["cubism_path"], f"Audit {row['character']} {row['skin']} skin")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit cached non-default Normal Live2D skin packages.")
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--only-id")
    args = parser.parse_args()
    rows = buildable_skin_rows()
    if args.only_id:
        rows = [row for row in rows if row["asset_id"] == args.only_id]
    else:
        rows = [row for row in rows if not todo_normal_done(row["asset_id"])]
    if args.limit > 0:
        rows = rows[: args.limit]
    if not rows:
        print("No buildable pending Normal skins found.")
        return
    with StaticServer() as base_url:
        for row in rows:
            audit_row(row, base_url)


if __name__ == "__main__":
    main()
