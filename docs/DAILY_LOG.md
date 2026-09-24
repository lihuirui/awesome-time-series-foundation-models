# Maintenance Daily Log / 每日维护日志

## 2026-09-24 (第 2 轮运行：评测体系全面深化与重点团队前沿纳入 / Iteration 2)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 2 轮迭代（上一轮 4 篇论文二次复核、近 45 天高影响力文献与重点团队前沿检索、第 7 章评测体系全面深化、图表质检与质量门禁）
- **文献总数**：93 篇经 arXiv HTTPS API 严格核验的论文（原 79 篇 + 本轮新增 14 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (4 篇)
通过 arXiv Atom HTTPS API 全量复核上一轮收录的 4 篇文献，标题、作者与发布时间均完全一致：
1. `2605.20119` (Toto 2.0: Time Series Forecasting Enters the Scaling Era)
2. `2606.16173` (TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting)
3. `2609.25788` (Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models)
4. `2609.27385` (Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools)

### 3. 本轮新增与核验论文 (14 篇)
1. **[arXiv:2510.12681]** *CoRA: Covariate-Aware Adaptation of Time Series Foundation Models* — 清华大学 THUML 龙明盛团队，针对通用单变量基础模型提出 Granger 因果嵌入 (GCE) 与零初始化条件注入机制，实现外生时序、文本、图像多模态协变量适配，MSE 降低 31.1%。
2. **[arXiv:2601.03248]** *STReasoner: Empowering LLMs for Spatio-Temporal Reasoning in Time Series via Spatial-Aware Reinforcement Learning* — 金明团队（录用于 ACL 2026），构建 ST-Bench 基准并设计空间感知强化学习算法 S-GRPO，显式强化大模型在复杂时空图拓扑中的因果归因与上下文推断；官方代码已核验：`https://github.com/LingFengGold/STReasoner`。
3. **[arXiv:2601.19040]** *OATS: Online Data Augmentation for Time Series Foundation Models* — 金明团队与微软（Microsoft TimeCraft），提出基于条件扩散模型的 TSFM 在线动态数据增强框架，根据预训练各阶段梯度贡献动态合成高保真时序数据；官方代码已核验：`https://github.com/microsoft/TimeCraft`。
4. **[arXiv:2602.06597]** *DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters* — 清华大学 THUML 龙明盛团队，首次将计算机视觉中的 Diffusion Transformer (DiT) 架构无缝拓展至多模态与高维时序生成预测。
5. **[arXiv:2606.01498]** *TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning* — 金明团队，构建涵盖 240 项任务、2,680 轮长时序交互对话的多轮智能体推理基准，系统揭示大模型在多步推演、置信度校准与复合运筹决策中的记忆退化瓶颈。
6. **[arXiv:2607.24892]** *LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models* — 提出免微调文本条件化方案，利用大语言模型作为时序预测规划器，通过提示工程将文本事件、突变约束与时序趋势解耦，引导冻结数值 TSFM 执行高质量预测。
7. **[arXiv:2608.14270]** *TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments* — 金明团队，构建追踪 2023.02 至 2026.05 间 60 个真实机构场景（1,485 场景问答对）的动态演化活体基准，严格要求模型具备截止日期意识与证据更新有效性。
8. **[arXiv:2609.10357]** *A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out* — 深刻揭露公开数据集预训练污染与熟悉度记忆危机，构建严格截断于模型发布日期之后的无污染测试集并横向评测 13 类预测模型；开源代码已核验：`https://github.com/mahdinaser/tsfm-bench`。
9. **[arXiv:2609.13640]** *FlowTSFM: Turning Encoder Depth into Quantile Transport* — 提出循环分位数传输架构，以仅 38.8M 参数在 GIFT-Eval 与 TIME 上取得与 119.5M 参数 Chronos-2 相当的精度，中间表征定向对齐指标 CosMean 跃升至 0.919。
10. **[arXiv:2609.16804]** *SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals* — 面向可穿戴生理多通道信号的生成式基础模型，基于 PSD 引导的确定性路由 MoE 与神经控制微分方程 (Neural CDE)，在 2260 亿时序观测点上预训练。
11. **[arXiv:2609.20156]** *QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization* — 录用于 VLDB 2027，提出模式量化与可学习性同步机制，攻克跨域多源通用时序预训练中的语料不平衡与灾难性遗忘。
12. **[arXiv:2609.21425]** *Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework* — 录用于 ACM AI Summit 2026，将零样本时序预测从单纯的“无梯度更新”重定义为严格受管制的“证据访问声称”，系统拆解语言模型先验、参数化时序预训练与检索外部记忆三大来源。
13. **[arXiv:2609.24862]** *When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting* — 提出 TimEvolve 智能体架构，利用现实滚动预测后真实值延迟展开的天然弱监督反馈，在线持续进化专家信任矩阵与干预策略。
14. **[arXiv:2609.25980]** *Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models* — 提出完全免训练的多变量样本路径交织耦合算法，通过最优传输重排将单变量概率 TSFM 的边际分布耦合为高质量多维联合未来分布。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **全面重构与深化第 7 章（基准与评测）**：
  - 新增 13 项主流评测基准综合对比矩阵表（涵盖任务、模态、规模、时序因果隔离机制、评估重点及开源状态）；
  - 深度剖析数据污染、预训练熟悉度记忆以及时间截断隔离审计（7.2 节）；
  - 形式化拆解“证据来源第一”的零样本审计框架四大评估维度（7.3 节）；
  - 系统论述概率分布校准指标 (PICP, MPIW, CRPS)、CosMean 方向对齐与多变量联合样本路径耦合（7.4 节）；
  - 深入阐述长程对话记忆衰减、截止日期意识与自进化策略（7.5 节）；
  - 总结多模态视觉大模型裁判 (VLM-as-a-Judge) 与工具预算调度 Harness（7.6 节）。
- **同步更新第 4、5、6、8、9 章**：全面融入 14 篇新论文在模型对比表、清华 THUML 进展、金明组成果与未来开放挑战中的定位。
- **自动更新参考文献**：Section 10 增至 93 篇核验文献，同步生成 93 条 BibTeX 记录 (`survey/references.bib`)。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：将图例移至画布正上方并采用 4 列水平排布，彻底消除原右上角图例遮挡 2026 年末 QUALS 与 FlowTSFM 节点的问题；
  2. `open_weight_share.png`：增加超薄切片自适应百分比过滤，消除占比仅 1.1% 闭源切片内的文字拥挤重叠；
  3. `taxonomy_tree.png`：全面扩充 4 大分支子节点，纳入分位数传输、因果嵌入、多模态扩散、自进化智能体与污染审计框架；
  4. `model_size_vs_date.png`：新增 FlowTSFM (38.8M) 标度点并精准微调标注偏移量；
  5. `papers_by_category_year.png`：更新至 93 篇文献的历年发表堆叠分布柱状图。

### 6. 工具链与自动化质量门禁
- 增强 `Makefile`：新增 `make check`（集成 `validate` 与 `survey-check`）和 `make search` 目标；
- 更新 `maintenance/AGY_DAILY_PROMPT.md`，同步工具链与质检规范；
- 自动化运行 `make all`，5 大门禁（JSON 结构校验、图表生成、综述 286 处引用/锚点/图片存在性校验、BibTeX 生成、README Awesome 清单生成）全部 100% 通过。

### 7. 提交与推送状态
- **本地提交**：`feat(iteration-2): deepen evaluation framework, integrate 14 papers (93 total), refine figures`
- **推送状态**：推送至远端 `origin/main` 并经 `git status` / `git log` 确认。

### 8. 下一轮运行重点
- 持续跟进因果推断时序基础模型框架 (arXiv: 2608.24303) 与工业监控部署经济性评测 (arXiv: 2608.22968)；
- 探索在综述中增加各 TSFM 在边缘设备与云端 GPU 上的实际显存峰值与推理吞吐 (Latency / Throughput) 对比表格；
- 监测 TimeMixer++ 官方开源合规进展。

---

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
