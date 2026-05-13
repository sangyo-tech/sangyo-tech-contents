#!/usr/bin/env python3
"""Notify IndexNow-compatible search engines about contents URLs."""
from __future__ import annotations

import json
import urllib.error
import urllib.request

API_KEY = "d00ed3ee747299f665b04f29cd0fab9c"
HOST = "contents.sangyo-tech.jp"
ENDPOINT = "https://api.indexnow.org/indexnow"

URLS = [
    "https://contents.sangyo-tech.jp/",
    "https://contents.sangyo-tech.jp/sitemap.xml",
    "https://contents.sangyo-tech.jp/robots.txt",
    "https://contents.sangyo-tech.jp/llms.txt",
]


def main() -> None:
    payload = {
        "host": HOST,
        "key": API_KEY,
        "keyLocation": f"https://{HOST}/{API_KEY}.txt",
        "urlList": URLS,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"Status: {resp.status}")
            body = resp.read().decode("utf-8", errors="replace")
            if body:
                print(body)
    except urllib.error.HTTPError as exc:
        print(f"HTTPError: {exc.code} {exc.reason}")
        print(exc.read().decode("utf-8", errors="replace"))


if __name__ == "__main__":
    main()
