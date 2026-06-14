from __future__ import annotations

import functools
import http.server
import socket
import threading
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DESKTOP_SHOT = ROOT / ".tmp-site-desktop.png"
MOBILE_SHOT = ROOT / ".tmp-site-mobile.png"
FILE_SHOT = ROOT / ".tmp-site-file.png"
HIDDEN_NORMAL_PACKAGES = {
    "9Pets-Baby-Blue",
    "9Pets-Baby-Blue-Default",
    "9Pets-Balloon-Party",
    "9Pets-Balloon-Party-Default",
}
HIDDEN_NORMAL_PREFIXES = (
    "9Pets-Baby-Blue-",
    "9Pets-Balloon-Party-",
)
EXPECTED_VISIBLE_NORMAL_TOTAL = 125


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def start_server() -> tuple[http.server.ThreadingHTTPServer, int]:
    port = free_port()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DOCS))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, port


def requests_smoke(base_url: str) -> None:
    session = requests.Session()
    session.trust_env = False
    for path in ["/", "/styles.css", "/app.js", "/data/pets.json"]:
        response = session.get(f"{base_url}{path}", timeout=10)
        response.raise_for_status()
    data = session.get(f"{base_url}/data/pets.json", timeout=10).json()
    if data["total"] != EXPECTED_VISIBLE_NORMAL_TOTAL:
        raise AssertionError(f"manifest total is {data['total']}, expected {EXPECTED_VISIBLE_NORMAL_TOTAL}")
    normal_packages = {pet["packageName"] for pet in data.get("pets", [])}
    if normal_packages & HIDDEN_NORMAL_PACKAGES:
        raise AssertionError("hidden normal packages are visible in the manifest")
    if any(package.startswith(HIDDEN_NORMAL_PREFIXES) for package in normal_packages):
        raise AssertionError("hidden normal skin packages are visible in the manifest")
    non_default_normals = [pet["packageName"] for pet in data.get("pets", []) if not pet.get("isDefaultSkin", True)]
    if non_default_normals:
        raise AssertionError(f"non-default normal skin packages require cached Live2D audit: {non_default_normals[:5]}")
    if data.get("cuteTotal") != len(data.get("cuteVariants", [])):
        raise AssertionError("cute variant total mismatch")
    cute_by_normal = {variant.get("normalPackageName"): variant for variant in data.get("cuteVariants", [])}
    for package in {"9Pets-Baby-Blue-Default", "9Pets-Balloon-Party-Default"}:
        variant = cute_by_normal.get(package)
        if not variant:
            raise AssertionError(f"{package} is hidden but its cute variant is missing")
        if not variant.get("sourceImage", "").startswith("assets/source/9Pets-Cute-"):
            raise AssertionError(f"{variant['packageName']} should use cute source art")


def playwright_smoke(base_url: str) -> None:
    from playwright.sync_api import sync_playwright

    def assert_detail_sprite_framed(page, title_text: str) -> None:
        boxes = page.evaluate(
            """() => {
                const stage = document.querySelector(".detail-stage").getBoundingClientRect();
                const sprite = document.querySelector(".detail-sprite").getBoundingClientRect();
                const tabs = document.querySelector(".state-tabs").getBoundingClientRect();
                return {stage, sprite, tabs};
            }"""
        )
        stage = boxes["stage"]
        sprite = boxes["sprite"]
        tabs = boxes["tabs"]
        tolerance = 2
        if (
            sprite["left"] < stage["left"] - tolerance
            or sprite["right"] > stage["right"] + tolerance
            or sprite["top"] < stage["top"] - tolerance
            or sprite["bottom"] > stage["bottom"] + tolerance
        ):
            raise AssertionError(f"detail sprite is outside the preview frame for {title_text}")
        if sprite["bottom"] > tabs["top"] + tolerance:
            raise AssertionError(f"detail sprite overlaps state tabs for {title_text}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1100}, device_scale_factor=1)
        page.goto(base_url, wait_until="networkidle")
        page.wait_for_selector(".pet-card")
        page.wait_for_function(
            "expected => document.querySelectorAll('.pet-card').length === expected",
            arg=EXPECTED_VISIBLE_NORMAL_TOTAL,
        )
        count = page.locator(".pet-card").count()
        if count != EXPECTED_VISIBLE_NORMAL_TOTAL:
            raise AssertionError(f"desktop card count is {count}, expected {EXPECTED_VISIBLE_NORMAL_TOTAL}")
        hidden_visible = page.evaluate(
            """hidden => hidden.some((packageName) =>
                [...document.querySelectorAll(".pet-card p")].some((node) => node.textContent.includes(packageName))
            )""",
            list(HIDDEN_NORMAL_PACKAGES),
        )
        if hidden_visible:
            raise AssertionError("hidden normal packages are visible on the desktop catalog")
        page.screenshot(path=str(DESKTOP_SHOT), full_page=True)
        cute_total = page.evaluate("() => window.NINEPETS_DATA.cuteVariants.length")
        if cute_total < 2:
            raise AssertionError(f"cute variant count is {cute_total}, expected at least 2")
        page.get_by_role("button", name="Cute").click()
        page.wait_for_function("document.querySelectorAll('.pet-card').length === window.NINEPETS_DATA.cuteVariants.length")
        cute_count = page.locator(".pet-card").count()
        if cute_count != cute_total:
            raise AssertionError(f"cute card count is {cute_count}, expected {cute_total}")
        page.get_by_role("button", name="Normal").click()
        page.wait_for_function(
            "expected => document.querySelectorAll('.pet-card').length === expected",
            arg=EXPECTED_VISIBLE_NORMAL_TOTAL,
        )

        mobile = browser.new_page(viewport={"width": 390, "height": 920}, is_mobile=True)
        mobile.goto(base_url, wait_until="networkidle")
        mobile.wait_for_selector(".pet-card")
        mobile.wait_for_function(
            "expected => document.querySelectorAll('.pet-card').length === expected",
            arg=EXPECTED_VISIBLE_NORMAL_TOTAL,
        )
        mobile_count = mobile.locator(".pet-card").count()
        if mobile_count != EXPECTED_VISIBLE_NORMAL_TOTAL:
            raise AssertionError(f"mobile card count is {mobile_count}, expected {EXPECTED_VISIBLE_NORMAL_TOTAL}")
        mobile.screenshot(path=str(MOBILE_SHOT), full_page=True)

        for pet_id, title_text, spritesheet in [
            ("9pets-37-default", "37", "detail-spritesheets/9Pets-37-Default.webp"),
            ("9pets-alien-t-default", "aliEn T", "spritesheets/9Pets-aliEn-T-Default.webp"),
            ("9pets-an-an-lee-default", "An-an Lee", "detail-spritesheets/9Pets-An-an-Lee-Default.webp"),
            ("9pets-anjo-nala-default", "Anjo Nala", "detail-spritesheets/9Pets-Anjo-Nala-Default.webp"),
            ("9pets-apple-default", "APPLe", "spritesheets/9Pets-APPLe-Default.webp"),
            ("9pets-argus-default", "Argus", "detail-spritesheets/9Pets-Argus-Default.webp"),
            ("9pets-avgust-default", "Avgust", "detail-spritesheets/9Pets-Avgust-Default.webp"),
        ]:
            detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
            detail.goto(f"{base_url}/pet.html?id={pet_id}", wait_until="networkidle")
            detail.wait_for_selector(".detail-sprite")
            if title_text not in detail.locator("#detailTitle").inner_text():
                raise AssertionError(f"detail page did not load {title_text}")
            sprite_image = detail.locator(".detail-sprite").evaluate("node => getComputedStyle(node).backgroundImage")
            if spritesheet not in sprite_image:
                raise AssertionError(f"detail page did not use {spritesheet}")
            assert_detail_sprite_framed(detail, title_text)
            detail.get_by_role("button", name="Wave").click()
            if "active" not in (detail.get_by_role("button", name="Wave").get_attribute("class") or ""):
                raise AssertionError(f"detail state tabs did not switch to Wave for {title_text}")

        cute_detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        cute_detail.goto(f"{base_url}/pet.html?id=9pets-cute-baby-blue-default", wait_until="networkidle")
        cute_detail.wait_for_selector(".detail-sprite")
        if "Baby Blue" not in cute_detail.locator("#detailTitle").inner_text():
            raise AssertionError("cute detail page did not load Baby Blue")
        if "cute official-sourced package" not in cute_detail.locator("#detailEyebrow").inner_text().lower():
            raise AssertionError("cute detail page did not show the cute package eyebrow")
        cute_sprite = cute_detail.locator(".detail-sprite").evaluate("node => getComputedStyle(node).backgroundImage")
        if "detail-spritesheets/9Pets-Cute-Baby-Blue-Default.webp" not in cute_sprite:
            raise AssertionError("cute detail page did not use the Baby Blue cute detail spritesheet")
        active_variant = cute_detail.locator("#variantSwitch .variant-link.active")
        if active_variant.inner_text() != "Cute":
            raise AssertionError("cute detail page did not mark Cute as active")
        if cute_detail.get_by_role("link", name="Normal").count() != 0:
            raise AssertionError("blocked Baby Blue normal should not be a detail-page link")
        normal_disabled = cute_detail.locator("#variantSwitch .variant-link.disabled")
        if normal_disabled.inner_text() != "Normal":
            raise AssertionError("blocked Baby Blue normal should be shown as a disabled variant")
        source_image = cute_detail.locator("#sourceImage").get_attribute("src")
        if "assets/source/9Pets-Cute-Baby-Blue-Default.png" not in (source_image or ""):
            raise AssertionError("cute detail page did not use Cute source art")
        back_href = cute_detail.locator(".back-link").get_attribute("href")
        if "index.html?variant=cute#catalog" not in (back_href or ""):
            raise AssertionError("cute detail back link does not preserve the Cute catalog")

        file_page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_page.goto((DOCS / "index.html").as_uri(), wait_until="networkidle")
        file_page.wait_for_selector(".pet-card")
        file_page.wait_for_function(
            "expected => document.querySelectorAll('.pet-card').length === expected",
            arg=EXPECTED_VISIBLE_NORMAL_TOTAL,
        )
        file_count = file_page.locator(".pet-card").count()
        if file_count != EXPECTED_VISIBLE_NORMAL_TOTAL:
            raise AssertionError(f"file:// card count is {file_count}, expected {EXPECTED_VISIBLE_NORMAL_TOTAL}")
        file_page.get_by_role("button", name="Cute").click()
        file_page.wait_for_function("document.querySelectorAll('.pet-card').length === window.NINEPETS_DATA.cuteVariants.length")
        file_page.screenshot(path=str(FILE_SHOT), full_page=True)

        file_detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_detail.goto((DOCS / "pet.html").as_uri() + "?id=9pets-37-default", wait_until="networkidle")
        file_detail.wait_for_selector(".detail-sprite")
        file_detail.get_by_role("link", name="Back to catalog").click()
        file_detail.wait_for_url("**/index.html#catalog")
        file_detail.goto((DOCS / "pet.html").as_uri() + "?id=9pets-37-default", wait_until="networkidle")
        file_detail.get_by_label("9Pets home").click()
        file_detail.wait_for_url("**/index.html#catalog")

        file_cute_detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_cute_detail.goto((DOCS / "pet.html").as_uri() + "?id=9pets-cute-baby-blue-default", wait_until="networkidle")
        file_cute_detail.wait_for_selector(".detail-sprite")
        file_cute_detail.get_by_role("link", name="Back to catalog").click()
        file_cute_detail.wait_for_url("**/index.html?variant=cute#catalog")
        file_cute_detail.wait_for_function("document.querySelector('[data-variant-mode=\"cute\"]').classList.contains('active')")
        browser.close()


def main() -> None:
    server, port = start_server()
    base_url = f"http://127.0.0.1:{port}"
    try:
        requests_smoke(base_url)
        try:
            playwright_smoke(base_url)
            print(f"Playwright smoke passed at {base_url}")
            print(f"desktop_screenshot={DESKTOP_SHOT}")
            print(f"mobile_screenshot={MOBILE_SHOT}")
            print(f"file_screenshot={FILE_SHOT}")
        except ImportError as error:
            print(f"HTTP smoke passed at {base_url}")
            print(f"Playwright smoke skipped: {error}")
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
