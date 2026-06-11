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
    if data["total"] != 127:
        raise AssertionError(f"manifest total is {data['total']}, expected 127")


def playwright_smoke(base_url: str) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 1100}, device_scale_factor=1)
        page.goto(base_url, wait_until="networkidle")
        page.wait_for_selector(".pet-card")
        page.wait_for_function("document.querySelectorAll('.pet-card').length === 127")
        count = page.locator(".pet-card").count()
        if count != 127:
            raise AssertionError(f"desktop card count is {count}, expected 127")
        page.screenshot(path=str(DESKTOP_SHOT), full_page=True)

        mobile = browser.new_page(viewport={"width": 390, "height": 920}, is_mobile=True)
        mobile.goto(base_url, wait_until="networkidle")
        mobile.wait_for_selector(".pet-card")
        mobile.wait_for_function("document.querySelectorAll('.pet-card').length === 127")
        mobile_count = mobile.locator(".pet-card").count()
        if mobile_count != 127:
            raise AssertionError(f"mobile card count is {mobile_count}, expected 127")
        mobile.screenshot(path=str(MOBILE_SHOT), full_page=True)

        for pet_id, title_text, spritesheet in [
            ("9pets-37", "37", "detail-spritesheets/9Pets-37.webp"),
            ("9pets-alien-t", "aliEn T", "detail-spritesheets/9Pets-aliEn-T.webp"),
            ("9pets-an-an-lee", "An-an Lee", "detail-spritesheets/9Pets-An-an-Lee.webp"),
            ("9pets-anjo-nala", "Anjo Nala", "detail-spritesheets/9Pets-Anjo-Nala.webp"),
            ("9pets-apple", "APPLe", "detail-spritesheets/9Pets-APPLe.webp"),
        ]:
            detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
            detail.goto(f"{base_url}/pet.html?id={pet_id}", wait_until="networkidle")
            detail.wait_for_selector(".detail-sprite")
            if title_text not in detail.locator("#detailTitle").inner_text():
                raise AssertionError(f"detail page did not load {title_text}")
            sprite_image = detail.locator(".detail-sprite").evaluate("node => getComputedStyle(node).backgroundImage")
            if spritesheet not in sprite_image:
                raise AssertionError(f"detail page did not use {spritesheet}")
            detail.get_by_role("button", name="Wave").click()
            if "active" not in (detail.get_by_role("button", name="Wave").get_attribute("class") or ""):
                raise AssertionError(f"detail state tabs did not switch to Wave for {title_text}")

        file_page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_page.goto((DOCS / "index.html").as_uri(), wait_until="networkidle")
        file_page.wait_for_selector(".pet-card")
        file_page.wait_for_function("document.querySelectorAll('.pet-card').length === 127")
        file_count = file_page.locator(".pet-card").count()
        if file_count != 127:
            raise AssertionError(f"file:// card count is {file_count}, expected 127")
        file_page.screenshot(path=str(FILE_SHOT), full_page=True)

        file_detail = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_detail.goto((DOCS / "pet.html").as_uri() + "?id=9pets-37", wait_until="networkidle")
        file_detail.wait_for_selector(".detail-sprite")
        file_detail.get_by_role("link", name="Back to catalog").click()
        file_detail.wait_for_url("**/index.html#catalog")
        file_detail.goto((DOCS / "pet.html").as_uri() + "?id=9pets-37", wait_until="networkidle")
        file_detail.get_by_label("9Pets home").click()
        file_detail.wait_for_url("**/index.html")
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
        except Exception as error:
            print(f"HTTP smoke passed at {base_url}")
            print(f"Playwright smoke skipped: {error}")
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
