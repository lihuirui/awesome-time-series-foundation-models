# Maintenance

## Layout

```
awesome-time-series-fm/
├── README.md              # human-facing Awesome list (generated or curated)
├── LICENSE                # CC0-1.0
├── CONTRIBUTING.md
├── Makefile
├── data/
│   ├── papers.json        # source of truth
│   └── verification_log.json
├── scripts/
│   ├── fetch_arxiv.py     # HTTPS arXiv Atom client
│   ├── validate.py
│   └── generate_readme.py
└── docs/MAINTENANCE.md
```

## Refresh metadata

```bash
make fetch
```

Uses `https://export.arxiv.org/api/query?id_list=...` (HTTPS only). Updates `title`, `authors`, and `year` in place for every id in `data/papers.json`. Skips / warns on missing ids. Respects a small inter-batch delay to avoid HTTP 429.

## CI-friendly checks

```bash
make validate   # JSON schema-ish checks + unique arXiv ids
make count      # paper count
```

Suggested CI steps: checkout → `make validate` → `make count` (optional: `make fetch` with network + cache).

## Curation priorities

1. THUML / 龙明盛 (Timer, Timer-XL, Sundial, AutoTimes, TSlib)
2. 金明 group (Time-LLM, Time-MoE, TimeOmni-*, Sonar-TS, surveys)
3. Chronos family (Chronos, Chronos-2; Chronos-Bolt noted without standalone paper)
4. Major TSFMs (TimesFM, Moirai, MOMENT, Lag-Llama, TTM, TiRex, Toto, UniTS, …)
5. Multimodal temporal / Temporal VL (Time-MMD, TimeOmni-VL, OpenTSLM, SciTS, …)

## Do not push

GitHub push is deferred until the local project is solid. No credentials in this repo.
