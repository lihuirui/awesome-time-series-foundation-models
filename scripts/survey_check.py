#!/usr/bin/env python3
"""Check survey/SURVEY.md consistency, citations, figures, and internal links.

Quality Gates:
1. Every citation [arXiv:XXXX.XXXXX] exists in data/papers.json.
2. Every embedded figure file exists on disk.
3. No broken internal markdown anchor links.
4. Key required sections exist.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
SURVEY_PATH = ROOT / "survey" / "SURVEY.md"

CITE_RE = re.compile(r"\[arXiv:([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]{7})\]")
FIG_RE = re.compile(r"!\[(.*?)\]\((.*?)\)")
LINK_RE = re.compile(r"\[(.*?)\]\(#(.*?)\)")
HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)

REQUIRED_SECTIONS = [
    "摘要",
    "1 引言",
    "2 问题定义与背景",
    "3 分类体系",
    "4 时序基础模型",
    "5 大语言模型赋能时序",
    "6 多模态时序",
    "7 基准与评测",
    "8 重点课题组进展",
    "9 开放问题与未来方向",
    "10 参考文献",
    "最后更新",
    "TODO",
]


def slugify(title: str) -> str:
    # GitHub markdown anchor generation
    # Lowercase, remove punctuation except hyphens, replace spaces with hyphens
    s = title.strip().lower()
    s = re.sub(r"[^\w\s\-—\u4e00-\u9fff]", "", s)
    s = re.sub(r"[\s—]+", "-", s)
    return s


def main() -> int:
    if not SURVEY_PATH.exists():
        print(f"ERROR: {SURVEY_PATH} does not exist", file=sys.stderr)
        return 1

    papers_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
    valid_ids = {p["arxiv_id"] for p in papers_data["papers"]}

    content = SURVEY_PATH.read_text(encoding="utf-8")
    errors: list[str] = []

    # 1. Citations check
    citations = CITE_RE.findall(content)
    if not citations:
        errors.append("No [arXiv:XXXX.XXXXX] citations found in SURVEY.md")
    for aid in citations:
        if aid not in valid_ids:
            errors.append(f"Cited arXiv ID not in data/papers.json: {aid}")

    # 2. Figures check
    figures = FIG_RE.findall(content)
    for alt, path_str in figures:
        # Resolve relative to survey/
        fig_path = (SURVEY_PATH.parent / path_str).resolve()
        if not fig_path.exists():
            errors.append(f"Referenced figure file does not exist: {path_str} (resolved: {fig_path})")

    # 3. Anchor links check
    headers = [m[1].strip() for m in HEADER_RE.findall(content)]
    anchors = {slugify(h) for h in headers}

    internal_links = LINK_RE.findall(content)
    for text, target in internal_links:
        # Skip external or non-anchor
        target_slug = target.lower()
        if target_slug not in anchors and not any(target_slug in a or a in target_slug for a in anchors):
            errors.append(f"Broken internal anchor link: [#{target}] for text '{text}'")

    # 4. Required sections check
    for req in REQUIRED_SECTIONS:
        if req not in content:
            errors.append(f"Missing required section keyword: '{req}'")

    if errors:
        print("SURVEY CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"OK: SURVEY.md check passed! ({len(citations)} citations checked, {len(figures)} figures verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
