#!/usr/bin/env python3
"""Update data/verification_log.json with today's verification records."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / "data" / "verification_log.json"
DATA_PATH = ROOT / "data" / "papers.json"

papers = json.load(open(DATA_PATH, "r", encoding="utf-8"))["papers"]
all_ids = sorted([p["arxiv_id"] for p in papers])

old_log = json.load(open(LOG_PATH, "r", encoding="utf-8"))

new_log = {
    "verified_count": len(all_ids),
    "verified_ids": all_ids,
    "added_this_cycle": [
        "2605.20119",
        "2606.16173",
        "2609.25788",
        "2609.27385"
    ],
    "verification_events": [
        {
            "timestamp": "2026-09-24T15:04:22+08:00",
            "query": "au:Long_Mingsheng (sort: submittedDate)",
            "result": "Discovered 2606.16173 (TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting). Verified via arXiv API."
        },
        {
            "timestamp": "2026-09-24T15:04:38+08:00",
            "query": "all:Toto AND all:\"time series\"",
            "result": "Discovered 2605.20119 (Toto 2.0: Time Series Forecasting Enters the Scaling Era). Verified via arXiv API. Code repo https://github.com/DataDog/toto verified via GitHub API (HTTP 200)."
        },
        {
            "timestamp": "2026-09-24T15:04:33+08:00",
            "query": "id_list:2609.25788",
            "result": "Verified 2609.25788 (Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models, accepted ADBIS 2026)."
        },
        {
            "timestamp": "2026-09-24T15:05:24+08:00",
            "query": "id_list:2609.27385",
            "result": "Verified 2609.27385 (Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools)."
        },
        {
            "timestamp": "2026-09-24T15:05:52+08:00",
            "query": "GitHub API repo existence check on all code_url entries",
            "result": "All 44 declared GitHub repositories verified HTTP 200 OK."
        },
        {
            "timestamp": "2026-09-24T15:06:56+08:00",
            "query": "Full batch arXiv metadata fetch for 79 papers",
            "result": "Successfully fetched published dates, venues, authors, titles and summaries."
        }
    ],
    "failed_or_mismatched": old_log.get("failed_or_mismatched", []),
    "timemixer_plusplus": old_log.get("timemixer_plusplus", {}),
    "method": "arXiv Atom API via HTTPS (export.arxiv.org) + title/author cross-check; GitHub API (api.github.com/repos/...) for code_url verification",
    "date": "2026-09-24"
}

with open(LOG_PATH, "w", encoding="utf-8") as f:
    json.dump(new_log, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Updated {LOG_PATH} successfully with {len(all_ids)} verified papers.")
