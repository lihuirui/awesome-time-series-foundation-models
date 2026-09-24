#!/usr/bin/env python3
"""Refresh paper metadata from the arXiv Atom API over HTTPS.

Reads arxiv_id values from data/papers.json, queries
https://export.arxiv.org/api/query?id_list=..., and updates title/authors/year
in place. Missing or mismatched ids are reported and left unchanged.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
API = "https://export.arxiv.org/api/query"
NS = {
    "a": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
USER_AGENT = "awesome-time-series-fm/1.0 (research; HTTPS fetch; local maintainer)"


def strip_version(arxiv_id: str) -> str:
    # 2403.07815v3 -> 2403.07815 ; also handle old-style if present
    return re.sub(r"v\d+$", "", arxiv_id.strip())


def parse_entry(entry: ET.Element) -> dict | None:
    id_el = entry.find("a:id", NS)
    title_el = entry.find("a:title", NS)
    if id_el is None or title_el is None or not title_el.text:
        return None
    raw = id_el.text.rstrip("/").split("/abs/")[-1]
    base = strip_version(raw)
    title = " ".join(title_el.text.split())
    if "incorrect id" in title.lower():
        return None
    authors = [
        a.find("a:name", NS).text
        for a in entry.findall("a:author", NS)
        if a.find("a:name", NS) is not None
    ]
    published = entry.find("a:published", NS)
    year = int(published.text[:4]) if published is not None and published.text else None
    cats: list[str] = []
    pc = entry.find("arxiv:primary_category", NS)
    if pc is not None and pc.get("term"):
        cats.append(pc.get("term"))
    for c in entry.findall("a:category", NS):
        t = c.get("term")
        if t and t not in cats:
            cats.append(t)
    return {
        "arxiv_id": base,
        "title": title,
        "authors": authors,
        "year": year,
        "categories_arxiv": cats,
    }


def fetch_batch(ids: list[str], retries: int = 4) -> list[dict]:
    q = ",".join(ids)
    url = f"{API}?id_list={q}&max_results={len(ids)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
            root = ET.fromstring(data)
            return [r for e in root.findall("a:entry", NS) if (r := parse_entry(e))]
        except urllib.error.HTTPError as e:
            last_err = e
            wait = 10 * (attempt + 1)
            if e.code == 429:
                wait = 20 * (attempt + 1)
            print(f"  HTTP {e.code}; sleeping {wait}s (attempt {attempt+1}/{retries})", flush=True)
            time.sleep(wait)
        except Exception as e:  # noqa: BLE001
            last_err = e
            wait = 10 * (attempt + 1)
            print(f"  Error {e!r}; sleeping {wait}s", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch batch {ids}: {last_err}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between batches")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    papers = payload["papers"]
    ids = [strip_version(p["arxiv_id"]) for p in papers]
    print(f"Refreshing {len(ids)} papers from {API} ...", flush=True)

    by_id: dict[str, dict] = {}
    missing: list[str] = []
    for i in range(0, len(ids), args.batch_size):
        batch = ids[i : i + args.batch_size]
        print(f"Batch {i // args.batch_size + 1}: {batch}", flush=True)
        results = fetch_batch(batch)
        got = {r["arxiv_id"]: r for r in results}
        for aid in batch:
            if aid in got:
                by_id[aid] = got[aid]
            else:
                # fuzzy: returned id may differ only by version already stripped
                hit = next((v for k, v in got.items() if k.startswith(aid) or aid.startswith(k)), None)
                if hit:
                    by_id[aid] = hit
                else:
                    missing.append(aid)
                    print(f"  MISSING {aid}", flush=True)
        if i + args.batch_size < len(ids):
            time.sleep(args.delay)

    updated = 0
    for p in papers:
        aid = strip_version(p["arxiv_id"])
        meta = by_id.get(aid)
        if not meta:
            continue
        changed = False
        for field in ("title", "authors", "year"):
            if meta.get(field) is not None and p.get(field) != meta[field]:
                p[field] = meta[field]
                changed = True
        p["arxiv_id"] = aid
        if changed:
            updated += 1

    print(f"Updated {updated} paper(s); missing {len(missing)}: {missing}", flush=True)
    if args.dry_run:
        print("Dry run — not writing.", flush=True)
        return 0 if not missing else 1

    payload["papers"] = papers
    DATA_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {DATA_PATH}", flush=True)
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
