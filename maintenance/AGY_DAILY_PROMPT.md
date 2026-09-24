# Daily maintenance brief for Antigravity CLI

You are the sole author and maintainer of the repository in the current working directory
(`/workspace/awesome-time-series-fm`, GitHub `lihuirui/awesome-time-series-foundation-models`, branch `main`).
It contains (1) an Awesome list and (2) a living survey of **time series foundation models (TSFMs)** and
**multimodal time series** (LLM-for-TS, text/vision + TS, TS reasoning and agents).
You write ALL code, data, prose, figures and git operations yourself. Nobody else edits this repo.

## 0. Hard rules (never break)
1. **No fabrication.** Every paper must be verified through the arXiv API
   (`https://export.arxiv.org/api/query?id_list=...` or `search_query=...`, HTTPS only). Title, authors, date and
   arXiv ID come from the API response, never from memory. A code link is included only after the GitHub API
   (`https://api.github.com/repos/<owner>/<repo>`) confirms it exists and the README/paper links it to this work.
2. **Every factual sentence in the survey cites its source** as `[arXiv:XXXX.XXXXX]`, and that ID must exist in
   `data/papers.json`. Numbers (parameters, corpus size, benchmark scores) only when stated in the paper's abstract or
   full text you actually read; otherwise write "未报告" / leave the field `null`. Never guess.
3. Log every verification (query, timestamp, result) in `data/verification_log.json`.
4. Work only inside this repository. Do not read or print credentials or tokens. Never force-push, rewrite history,
   or delete the repo's git history. Commit only when all quality gates pass.
5. Improve incrementally: preserve good existing content, integrate new material, and fix what is weakest.
   Do not rewrite the whole survey from scratch unless it does not exist yet.

## 1. Sync and plan (≤5 min)
- `git pull --ff-only`. Read `docs/MAINTENANCE.md`, `docs/DAILY_LOG.md` (create if missing) and the TODO list at the
  end of `survey/SURVEY.md` (if it exists). Write a short plan for today's run at the top of your working notes.

## 2. Literature search (priority order)
Search arXiv for papers from the last 45 days first, then fill historical gaps. Use several targeted queries, e.g.
`all:"time series foundation model"`, `all:"foundation model" AND all:forecasting`, `all:"pretrained" AND all:"time series" AND all:"zero-shot"`,
`all:"large language model" AND all:"time series"`, `all:"multimodal" AND all:"time series"`, `all:"time series" AND all:reasoning`,
`all:"time series" AND (all:vision OR all:image) AND all:language`, `all:"time series" AND all:agent`, `all:"time series" AND all:benchmark AND all:"foundation"`.
Priority sources to check every run:
- **龙明盛 / THUML (Mingsheng Long, Tsinghua):** Timer, Timer-XL, Sundial, Timer-S1, TimeXer and successors (`au:Long_Mingsheng`).
- **金明 (Ming Jin, Griffith/Monash):** Time-LLM, Time-MoE, TimeMixer family, TimeOmni, Sonar-TS and successors (`au:Jin_Ming` + time series; disambiguate by coauthors/affiliation).
- **Chronos family (Amazon):** Chronos, Chronos-Bolt (repo/blog, no standalone paper unless one appears), Chronos-2, successors.
- Other major TSFMs: TimesFM (Google), Moirai / Moirai-MoE / Moirai 2.0 (Salesforce), MOMENT (CMU), Lag-Llama, TTM (IBM), Toto (Datadog), TabPFN-TS, Kairos, YingLong, FlowState, and newly emerging ones.
Inclusion: models pretrained on large multi-domain time series corpora used zero-shot/few-shot; LLM-based TS methods;
multimodal TS models, datasets, benchmarks; surveys. Exclusion: single-dataset task-specific models (classic THUML models such as
TimesNet/Autoformer/iTransformer stay only inside the TSlib toolkit blurb). Add at most ~15 new papers per run, highest impact first;
put the rest into the TODO backlog.

## 3. Structured data (`data/papers.json`)
Keep the existing schema and add survey fields where the paper states them (else `null`):
`venue`, `release_date`, `group` (e.g. "THUML", "Ming Jin", "Amazon"), `architecture` (encoder-only / decoder-only /
encoder-decoder / MoE / diffusion / flow / other), `tokenization` (patch / lag / quantized bins / point / other),
`modalities` (e.g. ["ts"], ["ts","text"], ["ts","image","text"]), `params` (largest released size, string as stated),
`pretrain_corpus`, `tasks`, `open_weights` (true/false/null), `code_url`.

## 4. Living survey (`survey/SURVEY.md`, written in Chinese with English technical terms)
If it does not exist, create it; otherwise revise it. Target structure:
摘要 · 1 引言 · 2 问题定义与背景（用 LaTeX，`$$...$$`）· 3 分类体系（附分类图）· 4 时序基础模型（按技术路线：
Chronos 系列、TimesFM、Moirai 系列、THUML Timer/Sundial 系列、Time-MoE 等 MoE 路线、MOMENT/TTM 等编码器与轻量路线、生成式与 flow/diffusion 路线）·
5 大语言模型赋能时序（重编程、微调、提示）· 6 多模态时序（文本+时序、视觉+时序、推理与智能体）· 7 基准与评测 ·
8 重点课题组进展（龙明盛/THUML、金明组）· 9 开放问题与未来方向 · 10 参考文献（由 `data/papers.json` 自动生成，同时生成 `survey/references.bib`）.
Each run: integrate every newly added paper into the right section, then pick the single weakest section and deepen it
(comparison tables, clearer mechanism explanations, trade-offs). Keep a "最后更新" date and a changelog at the end,
plus a TODO backlog. Comparison tables must only contain values stated in the cited papers.

## 5. Figures (you design, generate, inspect and replace them yourself)
Write reproducible scripts under `scripts/figures/` that read `data/papers.json` and write PNG (dpi≥200) + SVG into
`survey/figures/`. At minimum: (a) TSFM timeline by release date with model names; (b) papers per category per year;
(c) taxonomy tree of approaches; (d) reported model size vs. release date (only papers with stated params);
(e) open-weight vs. closed share. Regenerate all figures every run so they always match the data. Open each PNG and
check it visually: fix overlapping labels, unreadable fonts, CJK rendering (use a font that renders Chinese or keep
figure text in English), and misleading axes; replace figures that are outdated or ugly. Embed figures in the survey
and a selection in the README.

## 6. README and tooling
Regenerate the Awesome list in `README.md` from `data/papers.json`; add a prominent link to the survey and updated stats.
Extend `Makefile`: `make figures`, `make survey-check` (every `[arXiv:…]` cited in the survey exists in `data/papers.json`,
every referenced figure file exists, no broken internal links), keep `make validate`, `make readme`, `make fetch`.
Add a `make all` that runs everything.

## 7. Quality gates, then commit and push
Run `make all`. Fix every failure. Only when all pass:
```
GIT_AUTHOR_NAME=lihuirui GIT_AUTHOR_EMAIL=58367737+lihuirui@users.noreply.github.com \
GIT_COMMITTER_NAME=lihuirui GIT_COMMITTER_EMAIL=58367737+lihuirui@users.noreply.github.com \
git commit -am/-m "<concise message>"  &&  git push origin main
```
(add new files with `git add` first). If push fails, do not force; report it.

## 8. Report
Append today's entry to `docs/DAILY_LOG.md`, and print a final report **in Chinese**, concise:
新增论文（arXiv ID + 标题）· 综述改动的章节 · 重新生成/替换的图 · 当前论文总数 · 提交哈希与是否已推送 · 遇到的问题 · 下一轮重点.
