#!/usr/bin/env python3
"""Generate survey/references.bib from data/papers.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
OUT_PATH = ROOT / "survey" / "references.bib"


def format_bibtex(p: dict) -> str:
    aid = p["arxiv_id"]
    # Key clean for bibtex: p_2403_07815 or aid
    key = f"paper_{aid.replace('.', '_').replace('-', '_').replace('/', '_')}"
    title = p["title"].replace("{", "\\{").replace("}", "\\}")
    authors = " and ".join(p["authors"])
    year = p["year"]
    venue = p.get("venue")

    lines = [
        f"@article{{{key},",
        f"  title = {{{{{title}}}}},",
        f"  author = {{{authors}}},",
        f"  year = {{{year}}},",
        f"  eprint = {{{aid}}},",
        f"  archivePrefix = {{arXiv}},",
        f"  url = {{https://arxiv.org/abs/{aid}}}"
    ]
    if venue:
        lines.append(f"  note = {{{venue}}},")
    lines.append("}\n")
    return "\n".join(lines)


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    papers = data["papers"]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    entries = [format_bibtex(p) for p in sorted(papers, key=lambda x: x["arxiv_id"])]

    OUT_PATH.write_text("\n".join(entries), encoding="utf-8")
    print(f"Generated {OUT_PATH} with {len(entries)} references.")


if __name__ == "__main__":
    main()
