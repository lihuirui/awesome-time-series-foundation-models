#!/usr/bin/env python3
"""Search arXiv API for candidate TSFM and multimodal time series papers."""
from __future__ import annotations

import json
import re
import time
import urllib.parse
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
USER_AGENT = "awesome-time-series-fm/1.0 (research; HTTPS search; local maintainer)"

QUERIES = [
    'au:Long_Mingsheng',
    'au:Jin_Ming AND (ti:"time" OR abs:"time series")',
    'all:"Chronos" AND all:"time series" AND (all:"forecasting" OR all:"foundation")',
    'ti:"time series foundation model" OR abs:"time series foundation model"',
    'all:"foundation model" AND all:"time series" AND (all:"forecasting" OR all:"zero-shot")',
    'all:"pretrained" AND all:"time series" AND all:"zero-shot"',
    'all:"multimodal" AND all:"time series" AND (all:"foundation" OR all:"reasoning" OR all:"agent")',
    'all:"time series" AND all:"reasoning" AND all:"agent"',
    'all:"time series" AND (all:"vision" OR all:"image") AND all:"language" AND all:"forecasting"',
    'all:"time series" AND all:"benchmark" AND all:"foundation"',
    'ti:"TimesFM" OR ti:"Moirai" OR ti:"Lag-Llama" OR ti:"TTM" OR ti:"Toto" OR ti:"TabPFN" OR ti:"Kairos" OR ti:"YingLong" OR ti:"FlowState"',
]


def strip_version(aid: str) -> str:
    return re.sub(r"v\d+$", "", aid.strip())


def run_query(query: str, max_results: int = 30) -> list[dict]:
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
    except Exception as e:
        print(f"Error querying {query}: {e}")
        return []

    root = ET.fromstring(data)
    results = []
    for entry in root.findall("a:entry", NS):
        id_el = entry.find("a:id", NS)
        title_el = entry.find("a:title", NS)
        summary_el = entry.find("a:summary", NS)
        pub_el = entry.find("a:published", NS)
        if id_el is None or title_el is None or not title_el.text:
            continue
        raw_id = id_el.text.rstrip("/").split("/abs/")[-1]
        aid = strip_version(raw_id)
        title = " ".join(title_el.text.split())
        if "incorrect id" in title.lower():
            continue
        summary = " ".join(summary_el.text.split()) if summary_el is not None and summary_el.text else ""
        pub = pub_el.text[:10] if pub_el is not None and pub_el.text else ""
        year = int(pub[:4]) if pub else 2026
        authors = [
            a.find("a:name", NS).text
            for a in entry.findall("a:author", NS)
            if a.find("a:name", NS) is not None
        ]
        results.append({
            "arxiv_id": aid,
            "title": title,
            "published": pub,
            "year": year,
            "authors": authors,
            "summary": summary,
        })
    return results


def main():
    existing = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    existing_ids = {p["arxiv_id"] for p in existing["papers"]}

    candidates: dict[str, dict] = {}
    for q in QUERIES:
        print(f"Searching: {q} ...")
        res = run_query(q, max_results=25)
        new_count = 0
        for r in res:
            aid = r["arxiv_id"]
            if aid not in existing_ids and aid not in candidates:
                candidates[aid] = r
                new_count += 1
        print(f"  Found {len(res)} results, {new_count} new candidates")
        time.sleep(3.5)

    print(f"\nTotal new unique candidates found: {len(candidates)}")
    # Sort candidates by publication date descending
    sorted_cand = sorted(candidates.values(), key=lambda x: x["published"], reverse=True)
    out_file = ROOT / "scripts" / "candidates.json"
    out_file.write_text(json.dumps(sorted_cand, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote candidates to {out_file}")

    for c in sorted_cand[:30]:
        print(f"[{c['arxiv_id']}] ({c['published']}) {c['title']} -- {', '.join(c['authors'][:2])}")


if __name__ == "__main__":
    main()
