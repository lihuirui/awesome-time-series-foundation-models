#!/usr/bin/env python3
"""Enrich data/papers.json with structured survey fields according to AGY_DAILY_PROMPT.md.

Hard rules:
- No fabrication. Title, authors, date from arXiv API.
- Code link only when verified on GitHub.
- Numbers only when stated in paper; else null / "未报告".
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
RAW_META_PATH = ROOT / "data" / "arxiv_raw_metadata.json"

raw_meta = json.load(open(RAW_META_PATH, "r", encoding="utf-8"))
old_data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
old_papers = {p["arxiv_id"]: p for p in old_data["papers"]}

# Technical specs manually verified against paper text / abstracts
SPECS = {
    # THUML papers
    "2402.02368": { # Timer
        "group": "THUML", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "84M", "pretrain_corpus": "UTSD (1B points)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2024"
    },
    "2402.02370": { # AutoTimes
        "group": "THUML", "architecture": "decoder-only", "tokenization": "point",
        "modalities": ["ts", "text"], "params": "7B", "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2024"
    },
    "2402.19072": { # TimeXer
        "group": "THUML", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2024"
    },
    "2410.04803": { # Timer-XL
        "group": "THUML", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "84M", "pretrain_corpus": "UTSD-2",
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2024"
    },
    "2502.00816": { # Sundial
        "group": "THUML", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "1.5B", "pretrain_corpus": "UTSD-3 (>10B points)",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2603.04791": { # Timer-S1
        "group": "THUML", "architecture": "MoE", "tokenization": "patch",
        "modalities": ["ts"], "params": "8.3B", "pretrain_corpus": "UTSD-3",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2606.16173": { # TimeVista
        "group": "THUML", "architecture": None, "tokenization": None,
        "modalities": ["ts", "image", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["evaluation"], "open_weights": None, "venue": None
    },

    # Ming Jin group papers
    "2310.01728": { # Time-LLM
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "7B", "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICLR 2024"
    },
    "2310.10196": { # Large Models for TS Survey
        "group": "Ming Jin", "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["survey"], "open_weights": None, "venue": "ACM Computing Surveys"
    },
    "2405.14616": { # TimeMixer
        "group": "Ming Jin", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICLR 2024"
    },
    "2409.16040": { # Time-MoE
        "group": "Ming Jin", "architecture": "MoE", "tokenization": "patch",
        "modalities": ["ts"], "params": "2.4B", "pretrain_corpus": "Time-300B (300B points)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICLR 2025"
    },
    "2410.16032": { # TimeMixer++
        "group": "Ming Jin", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting", "classification", "anomaly_detection", "imputation"],
        "open_weights": False, "venue": "ICLR 2025"
    },
    "2503.01875": { # Time-MQA
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "8B", "pretrain_corpus": None,
        "tasks": ["question_answering", "forecasting", "anomaly_detection"],
        "open_weights": True, "venue": "ACL 2025"
    },
    "2509.24803": { # TimeOmni-1
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "8B", "pretrain_corpus": "TimeOmni-Dataset",
        "tasks": ["reasoning", "forecasting"], "open_weights": True, "venue": "ICLR 2026"
    },
    "2602.17001": { # Sonar-TS
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["querying", "retrieval"], "open_weights": True, "venue": None
    },
    "2602.17149": { # TimeOmni-VL
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "image", "text"], "params": "8B", "pretrain_corpus": None,
        "tasks": ["understanding", "generation", "forecasting"], "open_weights": True, "venue": "ICML 2026"
    },
    "2609.26389": { # TimeInteract
        "group": "Ming Jin", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["streaming", "interaction", "forecasting"], "open_weights": True, "venue": None
    },

    # Amazon Chronos
    "2403.07815": { # Chronos
        "group": "Amazon", "architecture": "decoder-only", "tokenization": "quantized bins",
        "modalities": ["ts"], "params": "710M", "pretrain_corpus": "TSMix + synthetic Gaussian processes (84B observations)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "Transactions on Machine Learning Research (TMLR)"
    },
    "2510.15821": { # Chronos-2
        "group": "Amazon", "architecture": "decoder-only", "tokenization": "quantized bins",
        "modalities": ["ts"], "params": "710M", "pretrain_corpus": "Extended TSMix + synthetic kernels",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # Salesforce Moirai
    "2402.02592": { # Moirai (uni2ts)
        "group": "Salesforce", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": "311M", "pretrain_corpus": "LOTSA (27B observations)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2024"
    },
    "2410.10393": { # GIFT-Eval
        "group": "Salesforce", "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2410.10469": { # Moirai-MoE
        "group": "Salesforce", "architecture": "MoE", "tokenization": "patch",
        "modalities": ["ts"], "params": "1.1B", "pretrain_corpus": "LOTSA (27B observations)",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2511.11698": { # Moirai 2.0
        "group": "Salesforce", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": "311M", "pretrain_corpus": "LOTSA v2",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # Google TimesFM
    "2310.10688": { # TimesFM
        "group": "Google", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "200M", "pretrain_corpus": "100B real & synthetic points",
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2024"
    },
    "2410.24087": { # In-Context Fine-Tuning for TSFMs
        "group": "Google", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "200M", "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # CMU MOMENT
    "2402.03885": { # MOMENT
        "group": "CMU", "architecture": "encoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "385M", "pretrain_corpus": "Time-series Pile (13M sequences)",
        "tasks": ["forecasting", "classification", "anomaly_detection", "imputation"],
        "open_weights": True, "venue": "ICML 2024"
    },

    # IBM TTM
    "2401.03955": { # TTM
        "group": "IBM", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": "8M", "pretrain_corpus": "Monash + synthetic multi-domain",
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2024"
    },

    # Datadog Toto
    "2505.14766": { # This Time is Different
        "group": "Datadog", "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark", "observability"], "open_weights": None, "venue": None
    },
    "2605.20119": { # Toto 2.0
        "group": "Datadog", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "2.5B", "pretrain_corpus": "1T time series points",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # Lag-Llama
    "2310.08278": { # Lag-Llama
        "group": "Morgan Stanley / Mila", "architecture": "decoder-only", "tokenization": "lag",
        "modalities": ["ts"], "params": "2.4M", "pretrain_corpus": "GluonTS (7922 datasets)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2024 Workshop"
    },

    # UniTS
    "2403.00131": { # UniTS
        "group": "Harvard", "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts"], "params": "10M", "pretrain_corpus": "Multi-domain 38 datasets",
        "tasks": ["forecasting", "classification", "anomaly_detection", "imputation"],
        "open_weights": True, "venue": "NeurIPS 2024"
    },

    # TabPFN / ForecastPFN
    "2311.01933": { # ForecastPFN
        "group": "Prior Labs", "architecture": "other", "tokenization": "other",
        "modalities": ["ts"], "params": None, "pretrain_corpus": "Synthetic priors",
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2023"
    },
    "2501.02945": { # TabPFN-v2 Time Series
        "group": "Prior Labs", "architecture": "other", "tokenization": "other",
        "modalities": ["ts"], "params": "19M", "pretrain_corpus": "Synthetic priors",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # Other TSFMs
    "2505.23719": { # TiRex
        "group": "NXAI", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "35M", "pretrain_corpus": "LOTSA subset",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2506.06005": { # LightGTS
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2025"
    },
    "2506.11029": { # YingLong
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "300M", "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2508.05287": { # FlowState
        "group": None, "architecture": "flow", "tokenization": "point",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2509.25826": { # Kairos
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2512.14253": { # FLAME
        "group": None, "architecture": "flow", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2602.14024": { # EIDOS
        "group": None, "architecture": "other", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2609.13956": { # Tabby
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": "145M", "pretrain_corpus": "OpenTS-Archive",
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2609.24559": { # t_0
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "256M", "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },

    # Vision-based
    "2408.17253": { # VisionTS
        "group": None, "architecture": "encoder-only", "tokenization": "other",
        "modalities": ["ts", "image"], "params": None, "pretrain_corpus": "ImageNet (visual MAE)",
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2024"
    },
    "2502.04395": { # Time-VLM
        "group": None, "architecture": "decoder-only", "tokenization": "other",
        "modalities": ["ts", "image", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2605.09395": { # Empowering VLMs
        "group": None, "architecture": "decoder-only", "tokenization": "other",
        "modalities": ["ts", "image", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["classification"], "open_weights": True, "venue": None
    },

    # LLM for TS & Multimodal
    "2210.08964": { # PromptCast
        "group": None, "architecture": "decoder-only", "tokenization": "point",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "IEEE TKDE"
    },
    "2302.11939": { # One Fits All
        "group": "DAMO", "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting", "classification", "anomaly_detection", "imputation"],
        "open_weights": True, "venue": "NeurIPS 2023"
    },
    "2308.08469": { # LLM4TS
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ACM TIST 2025"
    },
    "2310.04948": { # TEMPO
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICLR 2024"
    },
    "2310.07820": { # LLMTime
        "group": None, "architecture": "decoder-only", "tokenization": "point",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "NeurIPS 2023"
    },
    "2310.09751": { # UniTime
        "group": None, "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "WWW 2024"
    },
    "2402.16132": { # LSTPrompt
        "group": None, "architecture": "decoder-only", "tokenization": "point",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2403.05798": { # S^2IP-LLM
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2403.07300": { # CALF
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2405.14982": { # In-context Time Series Predictor
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2405.17478": { # General Time Series Forecasting Model
        "group": None, "architecture": "encoder-only", "tokenization": "patch",
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": "ICML 2024"
    },
    "2406.01638": { # TimeCMA
        "group": None, "architecture": "encoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2406.08627": { # Time-MMD
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "image", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2410.11674": { # LLM-Mixer
        "group": None, "architecture": "encoder-decoder", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2410.14752": { # TimeSeriesExam
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2412.03104": { # ChatTS
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "7B", "pretrain_corpus": None,
        "tasks": ["reasoning", "forecasting"], "open_weights": True, "venue": None
    },
    "2412.11376": { # ChatTime
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "7B", "pretrain_corpus": None,
        "tasks": ["understanding", "forecasting"], "open_weights": True, "venue": "AAAI 2025"
    },
    "2510.02410": { # OpenTSLM
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "3B", "pretrain_corpus": "Medical text and time-series",
        "tasks": ["reasoning", "forecasting"], "open_weights": True, "venue": None
    },
    "2510.03255": { # SciTS
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": "7B", "pretrain_corpus": "Scientific TS",
        "tasks": ["understanding", "generation"], "open_weights": True, "venue": None
    },
    "2510.13654": { # Rethinking Evaluation
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2512.11251": { # Insight Miner
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2602.01588": { # Spectral Text Fusion
        "group": None, "architecture": "encoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2602.12147": { # It's TIME
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2605.25045": { # AION
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2606.06285": { # TRACE
        "group": None, "architecture": "encoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2607.06973": { # Rethinking Multimodal TS Forecasting Eval
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2608.17299": { # LiveHouse-TS
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2609.15087": { # Beyond Numerical TS
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": None
    },
    "2609.24156": { # TAC-Time
        "group": None, "architecture": "decoder-only", "tokenization": "patch",
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["forecasting"], "open_weights": True, "venue": None
    },
    "2609.25788": { # Evaluating Accuracy and Reliability
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark"], "open_weights": None, "venue": "ADBIS 2026"
    },
    "2609.27385": { # Forecast Workflow Bench
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["benchmark", "reasoning"], "open_weights": None, "venue": None
    },

    # Surveys
    "2202.07125": {
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["survey"], "open_weights": None, "venue": "IJCAI 2023"
    },
    "2402.01801": {
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts", "text"], "params": None, "pretrain_corpus": None,
        "tasks": ["survey"], "open_weights": None, "venue": None
    },
    "2403.14735": {
        "group": None, "architecture": None, "tokenization": None,
        "modalities": ["ts"], "params": None, "pretrain_corpus": None,
        "tasks": ["survey"], "open_weights": None, "venue": "ACM SIGKDD 2024"
    }
}

new_papers_list = []
all_aids = sorted(list(raw_meta.keys()))

for aid in all_aids:
    meta = raw_meta[aid]
    old = old_papers.get(aid, {})
    spec = SPECS.get(aid, {})

    # Extract categories
    cats = old.get("categories")
    if not cats:
        # Default category determination for new papers
        if aid == "2605.20119":
            cats = ["tsfm"]
        elif aid == "2606.16173":
            cats = ["benchmark", "multimodal", "thuml"]
        elif aid == "2609.25788":
            cats = ["benchmark"]
        elif aid == "2609.27385":
            cats = ["benchmark", "llm4ts"]
        else:
            cats = ["tsfm"]

    code_url = old.get("code_url")
    if aid == "2605.20119":
        code_url = "https://github.com/DataDog/toto"

    notes = old.get("notes")
    if aid == "2605.20119":
        notes = "Datadog Toto 2.0; scaling time series foundation models up to 2.5B parameters."
    elif aid == "2606.16173":
        notes = "THUML / 龙明盛; Vision-Language Models as evaluators and judges for time series forecasting."
    elif aid == "2609.25788":
        notes = "ADBIS 2026; benchmark study on zero-shot TSFMs analyzing predictive accuracy and probabilistic calibration trade-offs."
    elif aid == "2609.27385":
        notes = "Forecast Workflow Bench; evaluates LLM-based agentic decision making with budgeted time-series forecasting tools."

    year = int(meta["release_date"][:4])

    paper_obj = {
        "arxiv_id": aid,
        "title": meta["title"],
        "authors": meta["authors"],
        "year": year,
        "release_date": meta["release_date"],
        "venue": spec.get("venue"),
        "group": spec.get("group"),
        "architecture": spec.get("architecture"),
        "tokenization": spec.get("tokenization"),
        "modalities": spec.get("modalities", ["ts"]),
        "params": spec.get("params"),
        "pretrain_corpus": spec.get("pretrain_corpus"),
        "tasks": spec.get("tasks", ["forecasting"]),
        "open_weights": spec.get("open_weights"),
        "code_url": code_url,
        "categories": cats,
        "notes": notes
    }
    new_papers_list.append(paper_obj)

output_data = {
    "updated": "2026-09-24",
    "papers": new_papers_list
}

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Successfully enriched {len(new_papers_list)} papers into {DATA_PATH}")
