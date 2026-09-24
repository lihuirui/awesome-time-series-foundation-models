#!/usr/bin/env python3
"""Regenerate README.md from data/papers.json with survey links and visual assets."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
OUT = ROOT / "README.md"

SECTION_MAP = [
    ("survey", "Surveys / 综述"),
    ("tsfm", "Time-Series Foundation Models / 时序基础模型"),
    ("llm4ts", "LLM for Time Series / 大模型赋能时序"),
    ("multimodal", "Multimodal Time Series & Temporal VL / 多模态时序"),
    ("benchmark", "Benchmarks & Datasets / 基准与数据集"),
]


def authors_short(authors: list[str], n: int = 3) -> str:
    if len(authors) <= n:
        return ", ".join(authors)
    return ", ".join(authors[:n]) + " et al."


def entry_md(p: dict) -> str:
    link = f"https://arxiv.org/abs/{p['arxiv_id']}"
    line = f"- **{p['title']}** — {authors_short(p['authors'])} ({p['year']}) [[arXiv]({link})]"
    if p.get("venue"):
        line += f" *({p['venue']})*"
    if p.get("code_url"):
        line += f" [[Code]({p['code_url']})]"
    notes = p.get("notes")
    if notes and len(notes) < 140:
        line += f" — _{notes}_"
    return line


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    papers = data["papers"]
    assigned: set[str] = set()
    sections = {k: [] for k, _ in SECTION_MAP}
    for key, _ in SECTION_MAP:
        for p in papers:
            if p["arxiv_id"] in assigned:
                continue
            if key in p.get("categories", []):
                sections[key].append(p)
                assigned.add(p["arxiv_id"])
    for p in papers:
        if p["arxiv_id"] not in assigned:
            sections["tsfm"].append(p)

    lines: list[str] = []
    lines.append("# Awesome Time-Series Foundation Models (时序大模型)\n")
    lines.append(
        "> Curated list of **Time-Series Foundation Models (TSFMs)** and "
        "**Multimodal / Temporal VL** papers with **verified arXiv metadata only**.\n"
    )
    lines.append("> 仅收录经 arXiv API 核验的论文条目；严禁编造标题、作者、年份或链接。\n")

    lines.append("\n### 📖 Living Survey / 活体综述\n")
    lines.append(
        "- **[Comprehensive Living Survey (时序基础模型全面综述)](survey/SURVEY.md)** — "
        "涵盖数学定义、四大技术路线、模型对比表、跨模态前沿、评测基准与开放挑战。\n"
        "- **[BibTeX References (参考文献库)](survey/references.bib)** — "
        "由 `data/papers.json` 自动生成的完整 BibTeX 数据库。\n"
    )

    lines.append("\n**Maintainer focus:** 龙明盛/THUML · 金明 groups · Chronos-family · major TSFMs.\n")
    lines.append(
        f"\n**Stats:** {len(papers)} verified papers in "
        f"[`data/papers.json`](data/papers.json) (updated {data.get('updated', 'n/a')}).\n"
    )

    lines.append("\n## Visual Landscape / 演化图景\n")
    lines.append("![TSFM Timeline](survey/figures/tsfm_timeline.png)\n")

    lines.append("\n## Table of Contents\n")
    lines.append("- [Living Survey / 活体综述](#-living-survey--活体综述)")
    lines.append("- [Visual Landscape / 演化图景](#visual-landscape--演化图景)")
    for _, title in SECTION_MAP:
        anchor = title.split(" / ")[0].lower().replace(" ", "-").replace("&", "").replace(",", "")
        lines.append(f"- [{title}](#{anchor})")
    lines.append("- [Toolkits / 工具库](#toolkits--工具库)")
    lines.append("- [Resources / 资源](#resources--资源)")
    lines.append("- [Maintenance](#maintenance)")
    lines.append("\n---\n")

    for key, title in SECTION_MAP:
        lines.append(f"\n## {title}\n")
        for p in sorted(sections[key], key=lambda x: (-x["year"], x["title"])):
            lines.append(entry_md(p))
        lines.append("")

    lines.append("\n## Toolkits / 工具库\n")
    lines.append(
        "- **Time-Series-Library (TSlib)** — THUML unified codebase "
        "(TimesNet, Autoformer, iTransformer, TimeMixer, etc. as baselines; "
        "not listed as separate Awesome entries above). "
        "[[GitHub](https://github.com/thuml/Time-Series-Library)]"
    )
    lines.append(
        "- **GluonTS** — Probabilistic time series toolkit. "
        "[[arXiv](https://arxiv.org/abs/1906.05264)] [[Docs](https://ts.gluon.ai/)]"
    )
    lines.append(
        "- **uni2ts / Moirai** — Salesforce TSFM stack. "
        "[[GitHub](https://github.com/SalesforceAIResearch/uni2ts)]"
    )
    lines.append(
        "- **chronos-forecasting** — Amazon Chronos / Chronos-Bolt / Chronos-2. "
        "[[GitHub](https://github.com/amazon-science/chronos-forecasting)]"
    )
    lines.append(
        "- **OpenLTM / Large-Time-Series-Model** — THUML Timer family. "
        "[[GitHub](https://github.com/thuml/Large-Time-Series-Model)]"
    )
    lines.append(
        "- **Toto** — Datadog Toto 2.0 open-weights TSFM library. "
        "[[GitHub](https://github.com/DataDog/toto)]"
    )
    lines.append("")

    lines.append("\n## Resources / 资源\n")
    lines.append(
        "- Chronos-Bolt: **no standalone paper** (verified 2026-09-24). "
        "Use Chronos paper + "
        "[AWS blog](https://aws.amazon.com/blogs/machine-learning/fast-and-accurate-zero-shot-forecasting-with-chronos-bolt-and-autogluon/) "
        "+ HF `amazon/chronos-bolt-*`."
    )
    lines.append(
        "- OpenTSLab: string not found as arXiv title; closest verified entry is "
        "**OpenTSLM** (`2510.02410`)."
    )
    lines.append(
        "- TimeMixer++ (`2410.16032`): **permanent public code URL still unconfirmed** "
        "(2026-09-24). Paper appendix names [kwuking/TimeMixer](https://github.com/kwuking/TimeMixer); "
        "review anonymous repo [TimeMixerPP](https://anonymous.4open.science/r/TimeMixerPP); "
        "not in THUML TSlib. `code_url` kept null."
    )
    lines.append(
        "- Related Awesome lists: "
        "[Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM), "
        "[awesome-llm-time-series](https://github.com/xiyuanzh/awesome-llm-time-series)."
    )
    lines.append("")

    lines.append("\n## Maintenance\n")
    lines.append("```bash\nmake all          # run validate, figures, survey-check, bibtex, readme\n"
                 "make fetch        # refresh titles/authors/years from arXiv HTTPS API\n"
                 "make validate     # schema + count checks\n"
                 "make figures      # regenerate all 5 reproducible figures\n"
                 "make survey-check # verify survey citations, figures and links\n"
                 "make bibtex       # regenerate survey/references.bib\n"
                 "make count        # print paper count\n"
                 "make readme       # regenerate this README from data/papers.json\n```\n")
    lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/MAINTENANCE.md](docs/MAINTENANCE.md).\n")
    lines.append("\n## License\n")
    lines.append("CC0-1.0 (see [LICENSE](LICENSE)).\n")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(papers)} papers)")


if __name__ == "__main__":
    main()
