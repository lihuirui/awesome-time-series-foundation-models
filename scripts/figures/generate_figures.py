#!/usr/bin/env python3
"""Generate publication-quality figures for the TSFM Survey and README.

Generates:
(a) survey/figures/tsfm_timeline.png (.svg)
(b) survey/figures/papers_by_category_year.png (.svg)
(c) survey/figures/taxonomy_tree.png (.svg)
(d) survey/figures/model_size_vs_date.png (.svg)
(e) survey/figures/open_weight_share.png (.svg)
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "papers.json"
OUT_DIR = ROOT / "survey" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Set clean aesthetic
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
plt.rcParams["axes.edgecolor"] = "#cccccc"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["grid.color"] = "#eeeeee"
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.linewidth"] = 0.6


def load_data() -> list[dict]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["papers"]


def save_fig(fig: plt.Figure, name: str) -> None:
    for ext in ("png", "svg"):
        p = OUT_DIR / f"{name}.{ext}"
        fig.savefig(p, dpi=300, bbox_inches="tight")
        print(f"Saved {p}")
    plt.close(fig)


# ==========================================
# (a) TSFM Timeline
# ==========================================
def plot_timeline(papers: list[dict]) -> None:
    milestones = [
        ("TimesFM", "2023-10-14", "Google", 1.8),
        ("Lag-Llama", "2023-10-12", "Mila/MS", -1.8),
        ("ForecastPFN", "2023-11-03", "Prior Labs", 3.4),
        ("TTM", "2024-01-09", "IBM", -3.2),
        ("Timer", "2024-02-04", "THUML", 4.9),
        ("MOMENT", "2024-02-06", "CMU", -4.6),
        ("Moirai", "2024-02-05", "Salesforce", 2.2),
        ("Chronos", "2024-03-12", "Amazon", -2.2),
        ("UniTS", "2024-03-01", "Harvard", 3.6),
        ("TimeMixer", "2024-05-22", "Ming Jin", -1.8),
        ("VisionTS", "2024-08-26", "ZJU", 3.5),
        ("Time-MoE", "2024-09-24", "Ming Jin", -3.4),
        ("Timer-XL", "2024-10-07", "THUML", 4.8),
        ("Moirai-MoE", "2024-10-15", "Salesforce", -4.8),
        ("TabPFN-v2", "2025-01-06", "Prior Labs", 3.3),
        ("Sundial", "2025-02-03", "THUML", -2.2),
        ("TimesBERT", "2025-02-28", "THUML", 4.9),
        ("TiRex", "2025-05-27", "NXAI", 3.2),
        ("FlowState", "2025-08-08", "Academia", -1.8, -10),
        ("Kairos", "2025-09-25", "Academia", 4.2),
        ("KAIROS-NAR", "2025-10-03", "Academia", -3.8, 0),
        ("Chronos-2", "2025-10-21", "Amazon", -2.0, 12),
        ("Moirai 2.0", "2025-11-17", "Salesforce", 4.8),
        ("UniShape", "2026-01-10", "Academia", 2.0),
        ("Timer-S1", "2026-03-05", "THUML", -4.6, 0),
        ("WaveMoE", "2026-04-12", "Academia", 2.4, -18),
        ("LeapTS", "2026-05-11", "Ming Jin", -3.8, -15),
        ("Olivia", "2026-05-17", "Academia", -1.8, -8),
        ("Chronicle", "2026-05-18", "Academia", 5.6, -14),
        ("Toto 2.0", "2026-05-19", "Datadog", 4.0, -10),
        ("Falcon-X", "2026-05-26", "Academia", 1.4, -10),
        ("FactoryNet", "2026-06-03", "Academia", -5.0, 0),
        ("CITRAS-FM", "2026-06-09", "Hitachi", -3.2, 12),
        ("MACROCAST", "2026-06-27", "Academia", 5.2, 0),
        ("Zeus", "2026-07-02", "Academia", 3.4, 0),
        ("LeNEPA", "2026-07-01", "Ming Jin", 2.0, 0),
        ("Align-RAG", "2026-08-06", "Harvard", 4.4, 5),
        ("ReasonCast", "2026-08-15", "Academia", -4.4, 0),
        ("Cadence", "2026-09-05", "Academia", -2.0, -22),
        ("EXAONE Fin", "2026-09-07", "LG AI", 5.8, -6),
        ("FlowTSFM", "2026-09-12", "Academia", 2.4, -10),
        ("Tabby", "2026-09-12", "Academia", -3.8, -5),
        ("TW3Cast", "2026-09-16", "Academia", 3.6, 0),
        ("QUALS", "2026-09-17", "Academia", 5.0, 22),
        ("t_0", "2026-09-21", "Academia", -5.4, 0),
        ("TimeBraid", "2026-09-24", "Academia", 1.4, 16),
        ("SwitchPFN", "2026-09-24", "Academia", -2.0, 22)
    ]

    dates = [datetime.datetime.strptime(m[1], "%Y-%m-%d") for m in milestones]

    fig, ax = plt.subplots(figsize=(19, 9.5))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    palette = {
        "THUML": "#1f77b4",
        "Ming Jin": "#ff7f0e",
        "Amazon": "#2ca02c",
        "Salesforce": "#d62728",
        "Google": "#9467bd",
        "CMU": "#8c564b",
        "IBM": "#e377c2",
        "Datadog": "#0288d1",
        "Prior Labs": "#bcbd22",
        "Mila/MS": "#17becf",
        "Harvard": "#393b79",
        "ZJU": "#637939",
        "NXAI": "#843c39",
        "LG AI": "#a55194",
        "Hitachi": "#b35806",
        "Academia": "#5254a3"
    }

    ax.axhline(0, color="#444444", linewidth=1.5, zorder=1)

    for i, m_item in enumerate(milestones):
        name, date_str, grp, level = m_item[:4]
        dx_days = m_item[4] if len(m_item) > 4 else 0
        d = dates[i]
        color = palette.get(grp, "#333333")

        # Stem
        ax.plot([d, d], [0, level], color=color, linewidth=1.0, linestyle=":", zorder=2)
        # Nodes
        ax.scatter(d, level, color=color, s=75, zorder=3, edgecolors="#ffffff", linewidth=1.2)
        ax.scatter(d, 0, color=color, s=25, zorder=3)

        # Label text box
        va = "bottom" if level > 0 else "top"
        y_text = level + (0.2 if level > 0 else -0.2)
        x_text = d + datetime.timedelta(days=dx_days)

        if dx_days != 0:
            ax.annotate(
                f"{name}\n({grp})",
                xy=(d, level),
                xytext=(x_text, y_text),
                ha="center",
                va=va,
                fontsize=8.5,
                fontweight="bold",
                color="#222222",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#f8f9fa", edgecolor=color, alpha=0.92, linewidth=0.8),
                arrowprops=dict(arrowstyle="-", color=color, linestyle="--", linewidth=0.8),
                zorder=4
            )
        else:
            ax.annotate(
                f"{name}\n({grp})",
                xy=(d, level),
                xytext=(x_text, y_text),
                ha="center",
                va=va,
                fontsize=8.5,
                fontweight="bold",
                color="#222222",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#f8f9fa", edgecolor=color, alpha=0.92, linewidth=0.8),
                zorder=4
            )

    # Format x-axis
    ax.set_xlim(datetime.datetime(2023, 8, 1), datetime.datetime(2026, 11, 15))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate(rotation=0, ha="center")

    ax.set_ylim(-7.0, 7.5)
    ax.set_yticks([])
    ax.set_title("Evolution of Time Series Foundation Models (2023 - 2026)", fontsize=16, fontweight="bold", pad=36)

    # Legend placed at top center to avoid occluding any milestones
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label=k, markerfacecolor=v, markersize=8)
        for k, v in [
            ("THUML (Tsinghua)", palette["THUML"]),
            ("Ming Jin group", palette["Ming Jin"]),
            ("Amazon (Chronos)", palette["Amazon"]),
            ("Salesforce (Moirai)", palette["Salesforce"]),
            ("Google (TimesFM)", palette["Google"]),
            ("CMU (MOMENT)", palette["CMU"]),
            ("Datadog (Toto)", palette["Datadog"]),
            ("IBM (TTM)", palette["IBM"])
        ]
    ]
    ax.legend(handles=legend_elements, loc="upper center", bbox_to_anchor=(0.5, 1.06), ncol=4, frameon=True, fontsize=9.5, facecolor="#ffffff", edgecolor="#e0e0e0")

    for spine in ["top", "left", "right", "bottom"]:
        ax.spines[spine].set_visible(False)

    save_fig(fig, "tsfm_timeline")


# ==========================================
# (b) Papers by Category per Year
# ==========================================
def plot_papers_by_category_year(papers: list[dict]) -> None:
    years = [2022, 2023, 2024, 2025, 2026]
    categories = [
        ("tsfm", "Native TSFMs", "#1f77b4"),
        ("llm4ts", "LLM-for-TS", "#ff7f0e"),
        ("multimodal", "Multimodal TS", "#2ca02c"),
        ("benchmark", "Benchmarks & Eval", "#d62728"),
        ("survey", "Surveys", "#9467bd")
    ]

    counts = {c[0]: {y: 0 for y in years} for c in categories}
    for p in papers:
        y = p["year"]
        if y not in counts["tsfm"]:
            continue
        p_cats = p.get("categories", [])
        if "survey" in p_cats:
            counts["survey"][y] += 1
        elif "multimodal" in p_cats:
            counts["multimodal"][y] += 1
        elif "benchmark" in p_cats:
            counts["benchmark"][y] += 1
        elif "llm4ts" in p_cats:
            counts["llm4ts"][y] += 1
        else:
            counts["tsfm"][y] += 1

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    bottom = np.zeros(len(years))
    for cat_key, cat_label, color in categories:
        vals = [counts[cat_key][y] for y in years]
        bars = ax.bar(years, vals, bottom=bottom, label=cat_label, color=color, width=0.55, edgecolor="#ffffff", linewidth=0.8)
        for idx, (b, v) in enumerate(zip(bars, vals)):
            if v >= 2:
                ax.text(b.get_x() + b.get_width() / 2, bottom[idx] + v / 2, str(v),
                        ha="center", va="center", color="#ffffff", fontweight="bold", fontsize=9)
        bottom += np.array(vals)

    for i, y in enumerate(years):
        ax.text(y, bottom[i] + 0.6, f"Total: {int(bottom[i])}", ha="center", va="bottom", fontweight="bold", fontsize=10)

    ax.set_title("Verified Publications per Category per Year (2022 - 2026)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Publication Year", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylabel("Number of Papers", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_xticks(years)
    ax.set_ylim(0, max(bottom) + 5)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend(loc="upper left", frameon=True, fontsize=10, facecolor="#ffffff", edgecolor="#e0e0e0")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    save_fig(fig, "papers_by_category_year")


# ==========================================
# (c) Taxonomy Tree of Approaches
# ==========================================
def plot_taxonomy_tree(papers: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(16.5, 8.5))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Root Box
    ax.text(50, 93, "Time Series Foundation Models & Temporal Intelligence",
            ha="center", va="center", fontsize=13.5, fontweight="bold", color="#ffffff",
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#1a365d", edgecolor="#0f2942", linewidth=1.5))

    # 4 Main Branches
    branches = [
        ("Native TSFMs\n(Pretrained Models)", 13.5, 75, "#2b6cb0"),
        ("LLM-for-TS\n(Cross-Modal & Adapters)", 37.8, 75, "#2c7a7b"),
        ("Multimodal TS\n(Text, Vision & Agents)", 62.2, 75, "#9c4221"),
        ("Evaluation & Harness\n(Zero-Shot & Calibration)", 86.5, 75, "#6b46c1")
    ]

    for label, x, y, col in branches:
        ax.plot([50, x], [88, y + 4], color="#a0aec0", linewidth=1.5, linestyle="-", zorder=1)
        ax.text(x, y, label, ha="center", va="center", fontsize=10, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.5", facecolor=col, edgecolor="#cbd5e0", linewidth=1))

    # Sub-nodes
    subnodes = [
        (13.5, [
            ("Decoder-Only, Dynamic Scheduling & Compression\n• TimesFM, Timer, Sundial, LeapTS, Chronos-2, Cadence", 60),
            ("Non-AR, Attention-Free & Unified\n• KAIROS-NAR, EXAONE Fin, Zeus, Falcon-X, MACROCAST", 45),
            ("Sparse MoE, Wavelet & Spectral\n• Time-MoE, Timer-S1, WaveMoE, Olivia, TW3Cast", 30),
            ("Tiny Edge, Shapelets & Quantiles\n• CITRAS-FM (7M), TTM, UniShape, FlowTSFM, VersaTSA", 15)
        ], "#ebf8ff", "#2b6cb0"),

        (37.8, [
            ("Model Reprogramming & Adaptation\n• Time-LLM, GPT4TS, CoRA, FedChronos, PostTime", 60),
            ("Text Tokenization & Direct Prompting\n• LLMTime, PromptCast, LLM as Planner, MILM", 45),
            ("Semantic Alignment & Spatial/RL\n• S2IP-LLM, CALF, STReasoner, RL Post-Training", 30),
            ("In-Context Adaptation & Chorus\n• Align-RAG, ChorusTIC, LLM-Mixer, In-Context Probe", 15)
        ], "#e6fffa", "#2c7a7b"),

        (62.2, [
            ("Unified TS-Text & Diffusion Synthesis\n• TimeBraid, Chronicle (324M), SCENARIODIFF, GALA", 60),
            ("Agentic Reasoning & Debate\n• TimeAgent, TS-Debate, ReasonCast, ChatAD, TimEvolve", 45),
            ("Visual Time Series & Embodied Sensing\n• VisionTS, Time-VLM, TimeOmni-VL, FactoryNet", 30),
            ("Financial Simulators & Dynamic Harness\n• FINESSE, AION, TAC-Time, TRACE, KG-Chronos-2", 15)
        ], "#feebc8", "#9c4221"),

        (86.5, [
            ("Zero-Shot Forecasting & Leaderboards\n• GIFT-Eval, It's TIME, LiveHouse-TS, VersaTSA", 60),
            ("Contamination, Revision & Break-Even\n• Look-Ahead Bias, Break-Even Analysis, VINTAGE-TS", 45),
            ("Forecast Collapse & Regime Failures\n• Forecast Collapse, Regime-Dependent, SGA Uncertainty", 30),
            ("Hardware Profiling & Industrial Cost\n• HoliBench, Cost-Aware Study, TimeSage-EV", 15)
        ], "#faf5ff", "#6b46c1")
    ]

    for bx, items, bg, border in subnodes:
        ax.plot([bx, bx], [70, items[-1][1]], color="#cbd5e0", linewidth=1.2, linestyle="--", zorder=1)
        for text, y in items:
            ax.plot([bx, bx], [y, y], marker="o", color=border, markersize=4)
            ax.text(bx, y, text, ha="center", va="center", fontsize=7.4, color="#1a202c",
                    bbox=dict(boxstyle="round,pad=0.35", facecolor=bg, edgecolor=border, alpha=0.9, linewidth=0.8),
                    zorder=2)

    ax.set_title("Taxonomy of Time Series Foundation Models and Multimodal Temporal Intelligence",
                 fontsize=14, fontweight="bold", pad=12)

    save_fig(fig, "taxonomy_tree")


# ==========================================
# (d) Reported Model Size vs. Release Date
# ==========================================
def plot_model_size_vs_date(papers: list[dict]) -> None:
    def parse_params(p_str: str | None) -> float | None:
        if not p_str:
            return None
        p_str = p_str.strip().upper()
        if p_str.endswith("B"):
            return float(p_str[:-1]) * 1000.0  # Convert to Millions
        elif p_str.endswith("M"):
            return float(p_str[:-1])
        return None

    pts = []
    for p in papers:
        params_val = parse_params(p.get("params"))
        r_date = p.get("release_date")
        if params_val is not None and r_date:
            try:
                dt = datetime.datetime.strptime(r_date, "%Y-%m-%d")
                pts.append({
                    "name": p["title"].split(":")[0].split("—")[0].strip(),
                    "aid": p["arxiv_id"],
                    "date": dt,
                    "params_M": params_val,
                    "group": p.get("group") or "Other",
                    "arch": p.get("architecture") or "Other"
                })
            except Exception:
                pass

    fig, ax = plt.subplots(figsize=(13, 7.5))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    pts = sorted(pts, key=lambda x: x["date"])

    group_colors = {
        "THUML": "#1f77b4",
        "Ming Jin": "#ff7f0e",
        "Amazon": "#2ca02c",
        "Salesforce": "#d62728",
        "Google": "#9467bd",
        "CMU": "#8c564b",
        "IBM": "#e377c2",
        "Datadog": "#0288d1",
        "Other": "#7f7f7f"
    }

    # Frontier envelope
    x_frontier = []
    y_frontier = []
    curr_max = 0.0
    for pt in pts:
        if pt["params_M"] > curr_max:
            curr_max = pt["params_M"]
            x_frontier.append(pt["date"])
            y_frontier.append(curr_max)

    if len(x_frontier) > 1:
        ax.step(x_frontier, y_frontier, where="post", color="#e53e3e", linestyle="--", linewidth=1.5, alpha=0.7, label="Parameter Scaling Frontier")

    # Coordinated label positioning (label, xytext offset dx, dy)
    custom_offsets = {
        "2310.08278": ("Lag-Llama (2.4M)", 0, 8),
        "2401.03955": ("TTM (8M)", -25, -14),
        "2606.10798": ("CITRAS-FM (7M)", 0, -14),
        "2403.00131": ("UniTS (10M)", 25, 8),
        "2501.02945": ("TabPFN-v2 (19M)", 0, 8),
        "2505.23719": ("TiRex (35M)", 0, 8),
        "2609.13640": ("FlowTSFM (38.8M)", -20, -14),
        "2402.02368": ("Timer (84M)", 0, 8),
        "2609.13956": ("Tabby (145M)", -15, -14),
        "2310.10688": ("TimesFM (200M)", 0, 8),
        "2605.20268": ("Chronicle (324M)", -28, 10),
        "2609.06008": ("Cadence (330M)", 12, 10),
        "2609.24559": ("t_0 (256M)", 28, -12),
        "2403.07815": ("Chronos (710M)", 0, 8),
        "2410.10469": ("Moirai-MoE (1.1B)", 0, -15),
        "2502.00816": ("Sundial (1.5B)", 35, -5),
        "2601.13546": ("ChatAD (8B)", -28, 8),
        "2409.16040": ("Time-MoE (2.4B)", -30, 8),
        "2605.20119": ("Toto 2.0 (2.5B)", 0, -15),
        "2510.02410": ("OpenTSLM (3B)", 0, -14),
        "2509.24803": ("TimeOmni-1 (8B)", -35, -14),
        "2603.04791": ("Timer-S1 (8.3B MoE)", 35, 8)
    }

    for pt in pts:
        col = group_colors.get(pt["group"], group_colors["Other"])
        size = 50 + 12 * np.log10(max(pt["params_M"], 1.0))
        ax.scatter(pt["date"], pt["params_M"], color=col, s=size, edgecolors="#ffffff", linewidth=1.2, zorder=3, alpha=0.9)

        if pt["aid"] in custom_offsets:
            lbl, dx, dy = custom_offsets[pt["aid"]]
            ax.annotate(lbl, (pt["date"], pt["params_M"]),
                        xytext=(dx, dy),
                        textcoords="offset points",
                        ha="center", fontsize=8, fontweight="bold",
                        bbox=dict(boxstyle="round,pad=0.2", facecolor="#ffffff", edgecolor=col, alpha=0.9, linewidth=0.7),
                        zorder=4)

    ax.set_yscale("log")
    ax.set_xlim(datetime.datetime(2023, 8, 1), datetime.datetime(2026, 11, 15))
    ax.set_ylim(1, 25000)
    ax.set_yticks([1, 10, 100, 1000, 10000])
    ax.set_yticklabels(["1M", "10M", "100M", "1B", "10B"])

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate(rotation=0, ha="center")

    ax.set_title("Reported Model Parameter Scale vs. Release Date (2023 - 2026)", fontsize=14, fontweight="bold", pad=15)
    ax.set_ylabel("Parameters (Log Scale)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Release Date", fontsize=11, fontweight="bold")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)

    legend_items = [
        plt.Line2D([0], [0], marker='o', color='w', label=k, markerfacecolor=v, markersize=8)
        for k, v in [
            ("THUML (Tsinghua)", group_colors["THUML"]),
            ("Ming Jin group", group_colors["Ming Jin"]),
            ("Amazon", group_colors["Amazon"]),
            ("Salesforce", group_colors["Salesforce"]),
            ("Google", group_colors["Google"]),
            ("Datadog", group_colors["Datadog"]),
            ("CMU / IBM / Others", group_colors["CMU"])
        ]
    ]
    ax.legend(handles=legend_items, loc="upper left", frameon=True, fontsize=9, facecolor="#ffffff", edgecolor="#e0e0e0")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    save_fig(fig, "model_size_vs_date")


# ==========================================
# (e) Open Weights vs. Closed Share
# ==========================================
def plot_open_weight_share(papers: list[dict]) -> None:
    open_w = sum(1 for p in papers if p.get("open_weights") is True)
    closed_w = sum(1 for p in papers if p.get("open_weights") is False)
    no_weights = sum(1 for p in papers if p.get("open_weights") is None)

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    labels = [
        f"Open-Weights Models\n({open_w} papers, {open_w/len(papers)*100:.1f}%)",
        f"Closed / Unreleased Weights\n({closed_w} papers, {closed_w/len(papers)*100:.1f}%)",
        f"Benchmarks, Surveys & Prompts\n({no_weights} papers, {no_weights/len(papers)*100:.1f}%)"
    ]
    sizes = [open_w, closed_w, no_weights]
    colors = ["#2ca02c", "#d62728", "#1f77b4"]
    explode = (0.05, 0.05, 0.05)

    def clean_autopct(pct):
        return f"{pct:.1f}%" if pct > 3.0 else ""

    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, colors=colors,
        autopct=clean_autopct, startangle=140, pctdistance=0.75,
        textprops=dict(color="#222222", fontsize=9.5),
        wedgeprops=dict(width=0.45, edgecolor="#ffffff", linewidth=2)
    )

    for at in autotexts:
        at.set_color("#ffffff")
        at.set_fontweight("bold")
        at.set_fontsize(10)

    ax.text(0, 0, f"Total Papers\n{len(papers)}", ha="center", va="center", fontsize=13, fontweight="bold", color="#1a202c")

    ax.set_title("Open-Weights Availability across Time Series Literature", fontsize=14, fontweight="bold", pad=15)

    save_fig(fig, "open_weight_share")


def main() -> None:
    papers = load_data()
    print(f"Loaded {len(papers)} papers from {DATA_PATH}")
    plot_timeline(papers)
    plot_papers_by_category_year(papers)
    plot_taxonomy_tree(papers)
    plot_model_size_vs_date(papers)
    plot_open_weight_share(papers)
    print("All 5 figures generated successfully!")


if __name__ == "__main__":
    main()
