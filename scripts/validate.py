#!/usr/bin/env python3
"""Validate data/papers.json structure and uniqueness."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
ARXIV_RE = re.compile(r"^(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})$")

REQUIRED = {"arxiv_id", "title", "authors", "year", "categories"}


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload.get("papers")
    if not isinstance(papers, list) or not papers:
        print("ERROR: papers must be a non-empty list", file=sys.stderr)
        return 1

    seen: set[str] = set()
    errors: list[str] = []
    for i, p in enumerate(papers):
        missing = REQUIRED - set(p)
        if missing:
            errors.append(f"[{i}] missing keys: {sorted(missing)}")
            continue
        aid = p["arxiv_id"]
        if not ARXIV_RE.match(aid):
            errors.append(f"[{i}] bad arxiv_id: {aid!r}")
        if aid in seen:
            errors.append(f"[{i}] duplicate arxiv_id: {aid}")
        seen.add(aid)
        if not isinstance(p["authors"], list) or not p["authors"]:
            errors.append(f"[{i}] authors must be non-empty list ({aid})")
        if not isinstance(p["year"], int) or p["year"] < 1990:
            errors.append(f"[{i}] bad year ({aid}): {p['year']!r}")
        if not isinstance(p["categories"], list) or not p["categories"]:
            errors.append(f"[{i}] categories must be non-empty list ({aid})")
        if "code_url" not in p:
            errors.append(f"[{i}] code_url key required (use null) ({aid})")
        if p.get("title", "").strip() == "":
            errors.append(f"[{i}] empty title ({aid})")

    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(" ", e, file=sys.stderr)
        return 1

    print(f"OK: {len(papers)} papers, {len(seen)} unique arXiv ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())
