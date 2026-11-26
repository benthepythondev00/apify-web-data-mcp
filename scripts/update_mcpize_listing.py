#!/usr/bin/env python3
"""Update the live MCPize listing metadata from socialblade-creator-stats/mcpize-listing.json.

Reads auth from /home/paseo/.secrets/mcpize-dev-session.json (never prints tokens),
PATCHes the server record on be.mcpize.com, and verifies the live public page and
MCPize marketplace search ranks.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LISTING_PATH = REPO_ROOT / "socialblade-creator-stats" / "mcpize-listing.json"
DEFAULT_SESSION_PATH = Path("/home/paseo/.secrets/mcpize-dev-session.json")
SEARCH_TERMS = ["socialblade", "creator stats", "influencer", "x402", "pay per call", "usdc"]


def load_session(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("expires_at", 0) < int(time.time()) + 60 and data.get("refresh_token"):
        req = urllib.request.Request(
            "https://be.mcpize.com/auth/v1/token?grant_type=refresh_token",
            data=json.dumps({"refresh_token": data["refresh_token"]}).encode("utf-8"),
            headers={
                "apikey": data["anon"],
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            refreshed = json.loads(resp.read().decode("utf-8"))
        data["access_token"] = refreshed["access_token"]
        if refreshed.get("refresh_token"):
            data["refresh_token"] = refreshed["refresh_token"]
        if refreshed.get("expires_at"):
            data["expires_at"] = refreshed["expires_at"]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return data


def patch_listing(listing: dict, session: dict) -> dict:
    server_id = listing["server_id"]
    payload = {
        "name": listing["name"],
        "seo_title": listing["seo_title"],
        "seo_description": listing["seo_description"],
        "description": listing["description"],
        "long_description": listing["long_description"],
        "tags": listing["tags"],
    }
    url = f"https://be.mcpize.com/rest/v1/servers?id=eq.{urllib.parse.quote(server_id)}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "apikey": session["anon"],
            "Authorization": f"Bearer {session['access_token']}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
            "User-Agent": "mcpize-listing-sync/1.0",
        },
        method="PATCH",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        rows = json.loads(resp.read().decode("utf-8"))
    if not rows:
        raise RuntimeError(f"PATCH returned empty response for server_id={server_id}")
    return rows[0]


def check_search_ranks(slug: str, terms: list[str] = SEARCH_TERMS) -> dict[str, dict]:
    results = {}
    for term in terms:
        url = "https://mcpize.com/marketplace?q=" + urllib.parse.quote(term)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", "replace")
        slugs: list[str] = []
        for match in re.finditer(r'href="/mcp/([a-z0-9-]+)"', body):
            s = match.group(1)
            if s not in slugs:
                slugs.append(s)
        rank = (slugs.index(slug) + 1) if slug in slugs else None
        results[term] = {"rank": rank, "total": len(slugs)}
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync MCPize listing metadata.")
    parser.add_argument("--listing", type=Path, default=DEFAULT_LISTING_PATH)
    parser.add_argument("--session", type=Path, default=DEFAULT_SESSION_PATH)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check-ranks", action="store_true")
    args = parser.parse_args()

    listing = json.loads(args.listing.read_text(encoding="utf-8"))
    if args.dry_run:
        print(
            json.dumps(
                {
                    "dry_run": True,
                    "server_id": listing["server_id"],
                    "slug": listing["slug"],
                    "name": listing["name"],
                    "seo_title": listing["seo_title"],
                    "description_len": len(listing["description"]),
                    "long_description_len": len(listing["long_description"]),
                    "tags_count": len(listing["tags"]),
                },
                indent=2,
            )
        )
        return 0

    session = load_session(args.session)
    updated = patch_listing(listing, session)
    out: dict = {
        "updated": True,
        "id": updated.get("id"),
        "slug": updated.get("slug"),
        "name": updated.get("name"),
        "seo_title": updated.get("seo_title"),
        "description_len": len(updated.get("description") or ""),
        "long_description_len": len(updated.get("long_description") or ""),
        "tags": updated.get("tags"),
    }
    if args.check_ranks:
        out["ranks"] = check_search_ranks(listing["slug"])
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
