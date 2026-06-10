from __future__ import annotations

import re
from html.parser import HTMLParser
from urllib.parse import urljoin

import requests


class LinkImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.images: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name: value or "" for name, value in attrs}
        if tag == "a" and attr.get("href"):
            self.links.append(attr["href"])
        if tag == "img":
            src = attr.get("src") or attr.get("data-src") or attr.get("data-original")
            if src:
                self.images.append((src, attr.get("alt", "")))


def fetch(url: str) -> str:
    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; 9PetsBuilder/1.0; +https://github.com/)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    print(f"{url} -> {response.status_code} {len(response.text)} bytes")
    return response.text


def inspect(url: str) -> None:
    html = fetch(url)
    parser = LinkImageParser()
    parser.feed(html)
    print("links")
    for link in parser.links[:60]:
        print(" ", urljoin(url, link))
    print("images")
    for src, alt in parser.images[:60]:
        print(" ", urljoin(url, src), "|", alt)
    print("next-like chunks", sorted(set(re.findall(r"/_next/static/[^\"']+", html)))[:10])
    print("asset urls", sorted(set(re.findall(r"https?://[^\"'() ]+\\.(?:png|webp|jpg|jpeg)", html)))[:20])
    scripts = sorted(set(re.findall(r"<script[^>]+src=[\"']([^\"']+)[\"']", html)))
    if scripts:
        print("scripts")
        for script in scripts:
            print(" ", urljoin(url, script))
    role_assets = sorted(
        set(re.findall(r"(?:https://re\\.bluepoch\\.com/)?home/img/(?:role|character)/[^\"'()<> ]+", html))
    )
    if role_assets:
        print("bluepoch character assets")
        for asset in role_assets:
            print(" ", urljoin("https://re.bluepoch.com/", asset))


if __name__ == "__main__":
    inspect("https://www.prydwen.gg/re1999/characters")
    inspect("https://www.prydwen.gg/re1999/characters/regulus")
    inspect("https://re.bluepoch.com/home/")
