# Maintenance Daily Log / 每日维护日志

## 2026-09-24 (第 1 轮运行：全量体系构建 / Initial Full Run)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 1 轮运行（首次从零构建活体综述、图表流水线与质量把控门禁）
- **文献总数**：79 篇经 arXiv HTTPS API 严格核验的论文（原 75 篇 + 本轮新增 4 篇）

### 2. 今日新增与核验论文 (4 篇)
1. **[arXiv:2605.20119]** *Toto 2.0: Time Series Forecasting Enters the Scaling Era* — Datadog 团队最新时序基础模型，参数规模覆盖 4M 至 2.5B，基于超 1 万亿点预训练；已核验官方开源仓库 `https://github.com/DataDog/toto` (HTTP 200 OK)。
2. **[arXiv:2606.16173]** *TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting* — 清华大学 THUML 龙明盛团队最新成果，开创性探索视觉语言模型充当时序预测裁判 (VLM-as-a-Judge) 范式。
3. **[arXiv:2609.25788]** *Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models* — 录用于 ADBIS 2026，系统评测了六大主流零样本 TSFMs 的点预测精度与概率分布校准质量 (Probabilistic Calibration)。
4. **[arXiv:2609.27385]** *Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools* — 针对运筹优化与智能体时序决策，评测大模型在调用预算约束下的工具调度能力。

### 3. 数据集结构化增强 (`data/papers.json` & `data/verification_log.json`)
- 为全部 79 篇论文补全了综述结构化字段：`venue`, `release_date`, `group`, `architecture`, `tokenization`, `modalities`, `params`, `pretrain_corpus`, `tasks`, `open_weights`, `code_url`；
- 所有声明数值（参数量、语料规模、基准集）严格忠实于论文原文与摘要，未报告项严格保持 `null`，严禁编造；
- 在 `data/verification_log.json` 中记录完整检验事件流与时间戳。

### 4. 活体综述构建 (`survey/SURVEY.md` & `survey/references.bib`)
- **撰写完成全量综述**：涵盖 10 大核心章节，共计逾 4.2 万字符、220 处精确文献引用；
- **数学体系完备**：详细定义多变量时序观测、通道独立 (CI) 与通道依赖 (CD)、补丁分词 (Patching)、离散量化 (Binning)、下一补丁自回归损失以及连续流匹配 (TimeFlow Loss)；
- **全技术路线剖析**：系统剖析 Chronos 系列、Google TimesFM、Salesforce Moirai 系列、清华 THUML Timer/Sundial 系列、稀疏 MoE 路线（Time-MoE、Timer-S1）、轻量级工业部署路线（MOMENT、TTM）、连续 Flow/Diffusion 路线及跨模态智能；
- **自动化工具**：同步生成学术标准 BibTeX 文件 `survey/references.bib`。

### 5. 可复现学术图表设计与质检 (`survey/figures/`)
- 编写可复现生成脚本 `scripts/figures/generate_figures.py`，生成 5 套 300 DPI PNG 与矢量 SVG 图表：
  1. `tsfm_timeline.png` / `.svg`：时序基础模型演化全景时间线 (2023 - 2026)；
  2. `papers_by_category_year.png` / `.svg`：各类别历年论文发表分布堆叠柱状图；
  3. `taxonomy_tree.png` / `.svg`：时序基础模型与多模态智能体分类架构树；
  4. `model_size_vs_date.png` / `.svg`：模型声明参数规模与发布时间对数坐标图；
  5. `open_weight_share.png` / `.svg`：开源权重与闭源/评测基准占比环形图；
- **视觉质检**：完成所有 PNG 视觉复检，微调了时间线标签高度偏移，全英文排版消除 CJK 字体缺失警告。

### 6. 工具链与自动化质量门禁
- 增强 `scripts/validate.py`：校验必填字段、数据结构及 arXiv ID 唯一性；
- 编写 `scripts/survey_check.py`：自动校验综述中全部 220 处引用的合法性、嵌入图表文件的存在性、内部锚点跳转有效性及核心章节完整性；
- 编写 `scripts/generate_bibtex.py`：自动生成全量 BibTeX 数据库；
- 编写 `scripts/generate_readme.py`：自动同步主页 Awesome 列表、演化图表与活体综述入口；
- 更新 `Makefile`：添加 `figures`, `survey-check`, `bibtex`, `all` 目标，`make all` 实现全流水线自动化一键质检。

### 7. 提交与推送状态
- **本地提交**：`feat: initial full release with living survey, figures, and 79 verified papers`
- **推送状态**：已配置 GitHub CLI 非交互式凭据辅助器 (`gh auth setup-git`)，成功推送至远端 `origin/main` 并经 `git status` / `git fetch` 确认。

### 8. 下一轮运行重点
- 持续监控清华大学 THUML、金明团队及 Amazon/Salesforce/Google/Datadog 等重点团队的预印本更新；
- 探索在综述中增加工业时序基准（如长期电力负荷、气象同化）的端到端吞吐与显存开销对照分析；
- 跟进 TimeMixer++ 官方开源进展。
