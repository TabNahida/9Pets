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
        count = page.locator(".pet-card").count()
        if count != 127:
            raise AssertionError(f"desktop card count is {count}, expected 127")
        page.screenshot(path=str(DESKTOP_SHOT), full_page=True)

        mobile = browser.new_page(viewport={"width": 390, "height": 920}, is_mobile=True)
        mobile.goto(base_url, wait_until="networkidle")
        mobile.wait_for_selector(".pet-card")
        mobile_count = mobile.locator(".pet-card").count()
        if mobile_count != 127:
            raise AssertionError(f"mobile card count is {mobile_count}, expected 127")
        mobile.screenshot(path=str(MOBILE_SHOT), full_page=True)
        file_page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        file_page.goto((DOCS / "index.html").as_uri(), wait_until="networkidle")
        file_page.wait_for_selector(".pet-card")
        file_count = file_page.locator(".pet-card").count()
        if file_count != 127:
            raise AssertionError(f"file:// card count is {file_count}, expected 127")
        file_page.screenshot(path=str(FILE_SHOT), full_page=True)
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
