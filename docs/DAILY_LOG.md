# Maintenance Daily Log / 每日维护日志

## 2026-09-26 (第 5 轮运行：时序原生基础模型全面数学深化、15 篇前沿收录与全景矩阵扩充 / Iteration 5)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 5 轮迭代（上一轮 15 篇论文二次复核、近 45 天高影响力文献与重点团队前沿检索、第 4 章时序原生基础模型全面数学深化、图表质检与质量门禁）
- **文献总数**：138 篇经 arXiv HTTPS API 严格核验的论文（原 123 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (15 篇)
通过 arXiv OAI-PMH / Atom HTTPS API 全量复核上一轮收录的 15 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2510.02084` (KAIROS), `2601.06429` (UniShape), `2605.09081` (FactoryNet), `2607.00958` (LeNEPA), `2607.20002` (Post-Training), `2608.08010` (GT-Neighborhood RL), `2608.13741` (GALA), `2608.14106` (Forecast Collapse), `2608.15291` (ReasonCast), `2608.20005` (Scale-Aware), `2608.24033` (ChorusTIC), `2609.04239` (EXAONE Fin), `2609.06008` (Cadence), `2609.20554` (Look-Ahead Bias), `2609.28582` (SGA).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2601.19151]** *Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning* — EMNLP 2026，提出 TS-Debate 推理期多模态协作辩论协议，协调数值、视觉与文本智能体交叉质询，消除局部幻觉。
2. **[arXiv:2604.10544]** *WaveMoE: A Wavelet-Enhanced Mixture-of-Experts Foundation Model for Time Series Forecasting* — ICLR 2026 TSALM，小波增强型混合专家架构，依据离散小波分解的高低频能量分布自适应路由子频段。
3. **[arXiv:2605.10292]** *LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling* — 金明团队，重新审视固定步长预测，提出自适应多视野动态调度分层控制器与连续受控微分方程 (Neural CDE) 状态积分。
4. **[arXiv:2605.13711]** *MILM: Large Language Models for Multimodal Irregular Time Series with Informative Sampling* — 将不规则多变量采样转化为带有时间戳的结构化 XML 三元组并结合信息性采样，使 LLM 原生适应不规则时序。
5. **[arXiv:2605.17340]** *Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density* — ICML 2026，揭示跨域预训练中的频域失真病灶，提出功率谱密度协调模块 Harmonizer 与频域一致性损失；官方代码已核验：`https://github.com/TSTS13/Olivia`。
6. **[arXiv:2605.20268]** *Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding* — 324M 参数的原生跨模态 Decoder-only 大模型，从零在文本-时序混合语料上预训练，实现因果生成与双向理解。
7. **[arXiv:2605.27286]** *Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling* — 针对量纲悬殊的异构多变量，提出原型差分注意力 (Prototype Diff-Attention) 解耦变量并对齐至隐式原型流形。
8. **[arXiv:2605.29401]** *Rethinking Post-Training Recipes for Multimodal Time-Series Forecasting* — PostTime: 结合指令监督微调 (SFT) 与可验证奖励强化学习 (RLVR)，训练大语言模型充当数值 TSFM 先验的上下文修正器。
9. **[arXiv:2606.10798]** *CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting* — 日立团队（EUSIPCO 2026），7M 超轻量时序基础模型，支持协变量引导，针对边缘工控 CPU 极速毫秒级推断深度优化；官方代码已核验：`https://github.com/hitachi-ais/citras-fm`。
10. **[arXiv:2606.18367]** *Do Time Series Foundation Model Benchmarks Hide Regime-Dependent Failures? Evidence from Traffic Speed Forecasting* — 状态依赖型相变失效审计，严谨揭示全集平均宏观误差掩盖突发拥堵相变点误差剧增数十倍的系统性缺陷。
11. **[arXiv:2606.28670]** *MACROCAST: A Vintage-Consistent Time Series Foundation Model for Real-Time Macroeconomic Forecasting* — 首个版本一致性宏观 TSFM，基于 FRED-MD 历史实时版本切片与合成宏观轨迹预训练，彻底阻断修订数据未来泄露。
12. **[arXiv:2607.01918]** *Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis* — ICML 2026，U 形多尺度层次 Transformer 骨干与多目标时序掩码 (MOTM)，实现全任务免微调开箱即用。
13. **[arXiv:2607.04919]** *When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters* — 30 个跨域数据集上系统测算 TSFM 相比精调 GBDT/ARIMA 的算力-精度损益平衡点，明确冷启动与突发扰动下的商业回报边界。
14. **[arXiv:2608.17164]** *SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting* — 提出场景级引导扩散预测框架，将宏观文本分解为场景假说与因果时间锚点注入去噪扩散过程。
15. **[arXiv:2609.22836]** *A Hybrid Attention Model Learning Unified Time-aware Patch Representation for Irregular Multivariate Time Series Forecasting* — 开源 300 亿时序观测值 VersaTSA 预训练语料，提出时间感知补丁与混合因果掩码注意力架构。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **全面重构与深化第 4 章（时序基础模型 Native TSFMs）**：
  - 4.1 核心对比矩阵扩充至 43 款代表性模型，完整覆盖 CITRAS-FM、Zeus、Falcon-X、MACROCAST、WaveMoE、Olivia、VersaTSA、Chronicle、LeapTS 等；
  - 4.2 离散量化语言化路线：严格推导均值绝对缩放、分箱映射算子 $\mathcal{Q}(\cdot)$ 与类别交叉熵损失 $\mathcal{L}_{\text{CE}}$，系统剖析分布拟合柔性与有序度量信息丢失的架构权衡；
  - 4.3 连续补丁自回归路线：严格推导两阶段线性投影（输入补丁 $P_{\text{in}}=32$ 与长视野输出 $P_{\text{out}}=128$）与连续 Huber / Smooth L1 回归损失，剖析计算密度与均值退化；
  - 4.4 全频段全变量统一路线：形式化 Any-variate 序列扁平化计算，严格推导变量感知旋转位置编码 (vRoPE) 2D 旋转矩阵 $\mathbf{R}_{\Theta, m, c}$；
  - 4.5 清华 THUML Timer 与 Sundial 系列：推导 Sundial 连续流匹配 (TimeFlow CFM) 概率插值路径、速度场预测目标 $\mathcal{L}_{\text{CFM}}$ 以及 Euler/Heun 数值 ODE 积分采样；
  - 4.6 混合专家 (MoE) 路线与动态路由：推导稀疏 Top-$k$ 门控机制与辅助负载均衡正则化损失 $\mathcal{L}_{\text{balance}}$；系统推导小波子带解耦路由 (WaveMoE) 与功率谱密度一致性损失 $\mathcal{L}_{\text{PSD}}$ (Olivia)；
  - 4.7 动态调度、神经微分方程与误差有界压缩：推导 LeapTS 自适应多视野调度控制器与连续受控微分方程 (Neural CDE) 状态积分；推导 Cadence 误差有界预测残差死区量化与算术熵编码压缩算法；
  - 4.8-4.10 扩充日立 7M 极速边缘模型 CITRAS-FM、免调优 U 形多任务模型 Zeus、异构多变量原型差分注意力 Falcon-X、版本一致性宏观模型 MACROCAST、300 亿时序不规则大语料 VersaTSA；
- **同步更新第 5、6、7、8、9 章**：
  - 5.1/5.3/5.6 引入 MILM 不规则时序 XML 三元组采样、PostTime 可验证奖励 (RLVR) 强化后训练；
  - 6.1/6.2/6.4 引入 Chronicle 324M 原生语言-时序大模型、SCENARIODIFF 场景级引导扩散、TS-Debate 多模态多智能体辩论协议；
  - 7.1/7.4/7.6 扩充至 27 个主流评测基准框架，涵盖 Break-Even 经济学损益平衡分析、Regime-Dependent 状态依赖型相变失效审计、VersaTSA 30B 不规则时序评测集；
  - 8.2 同步更新金明团队动态多视野调度 LeapTS [arXiv:2605.10292]；
  - 9 开放问题深入剖析状态依赖型相变失效防御、可验证奖励后训练与投资回报损益平衡。
- **全量同步参考文献**：Section 10 收录全部 138 篇核验文献，同步生成 138 条 BibTeX 记录 (`survey/references.bib`) 与 README.md。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：微调 2026 前沿模型（Chronicle, Toto 2.0, Falcon-X, MACROCAST, Zeus, LeNEPA, Align-RAG, EXAONE Fin, FlowTSFM, TimeBraid 等）引线高度与水平偏移，完全消解标签接触；
  2. `open_weight_share.png`：准确反映 138 篇论文中 51.4% 开源权重模型、47.8% 基准/提示/综述、0.7% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：融入动态调度、小波解耦、功率谱对齐、自适应视野等技术分支；
  4. `model_size_vs_date.png`：新增 CITRAS-FM (7M) 与 Chronicle (324M) 标度点并精准排布；
  5. `papers_by_category_year.png`：更新至 138 篇文献的历年发表堆叠分布柱状图。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（138 篇唯一 ID 校验、5 组图表生成与校验、483 处文献与图片锚点引用校验、BibTeX 生成、README.md 自动化生成）全部 100% 一次性通过。

### 7. 提交与推送状态
- **本地提交**：`feat(iteration-5): deepen native TSFMs, integrate 15 papers (138 total), refine figures`
- **推送状态**：推送至远端 `origin/main` 并经 `git status` / `git log` 确认。

### 8. 下一轮运行重点
- 深入探索连续时序流匹配与连续扩散生成的几何最优传输收敛界；
- 研发面向万亿级预训练语料的前瞻偏误自动化因果隔离审计工具箱；
- 持续追踪通用人形机器人与重工业机电融合的超高频时序动力学表征大模型；
- 监测 TimeMixer++ 官方开源合规进展。

---

## 2026-09-26 (第 4 轮运行：多模态时序与智能体深度演进、具身物理时序突破、前沿 15 篇收录与图表重构 / Iteration 4)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 4 轮迭代（上一轮 15 篇论文二次复核、近 45 天高影响力文献与重点团队前沿检索、第 6 章多模态时序与智能体演进全面深化、图表质检与质量门禁）
- **文献总数**：123 篇经 arXiv HTTPS API 严格核验的论文（原 108 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (15 篇)
通过 arXiv OAI-PMH / Atom HTTPS API 全量复核上一轮收录的 15 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2502.21245` (TimesBERT), `2509.23695` (Estimating TSFM Transferability), `2601.13546` (ChatAD), `2608.01290` (FedChronos), `2608.05571` (Align-RAG), `2608.22968` (Cost-Aware Study), `2608.24303` (Causal Analysis), `2609.09586` (Synthetic Data Distillation), `2609.11993` (FINESSE), `2609.12412` (HoliBench), `2609.28506` (TW3Cast), `2609.21381` (KG-Chronos-2), `2609.28576` (VINTAGE-TS), `2609.29792` (TimeBraid), `2609.29814` (SwitchPFN).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2510.02084]** *KAIROS: Unified Training for Universal Non-Autoregressive Time Series Forecasting* — Ding 等提出非自回归统一预训练架构，长序列多步外推提速 10-50 倍且避免自回归误差积累；官方代码已核验：`https://github.com/D-X-Y/KAIROS`。
2. **[arXiv:2601.06429]** *A Unified Shape-Aware Foundation Model for Time Series Classification* — AAAI 2026，提出 UniShape 形态基元基础模型，在 128 个 UCR/UEA 数据集上突破刚性切片限制。
3. **[arXiv:2605.09081]** *FactoryNet: A Large-Scale Dataset toward Industrial Time-Series Foundation Models* — ICML 2026，涵盖 6 大类工业物理具身实体（数控机床、六轴机械臂、重型冲压机、分拣输送线、包装机、注塑机）的 5100 万点多通道遥测基准与基础模型；官方代码已核验：`https://github.com/Forgis-Labs/FactoryNet`。
4. **[arXiv:2607.00958]** *LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning* — 金明团队（KDD MILETS 2026），提出免数据增强下一隐状态预测表征学习新范式，规避经验性扰动对物理因果规律的破坏；官方代码已核验：`https://github.com/langotime/lenepa-milets-2026`。
5. **[arXiv:2607.20002]** *Post-Training in Time Series Foundation Models: A Unifying Framework* — Xie 等首次系统梳理时序后训练 (Post-Training) 体系，涵盖 SFT、DPO、强化学习与 PEFT 参数高效微调。
6. **[arXiv:2608.08010]** *Ground-Truth Neighborhood Regularization for Reinforcement Learning Post-Training of Time Series Foundation Models* — 提出真实轨迹局部几何邻域正则化强化学习目标，根治时序 PPO 连续动作空间下的策略崩塌难题。
7. **[arXiv:2608.13741]** *GALA: Generation-Aware Cross-Modal Alignment for Text-to-Time-Series Synthesis* — 提出生成感知跨模态对齐扩散框架，解决多步去噪流形与文本语义的动态一致性，实现精准受控波形合成。
8. **[arXiv:2608.14106]** *Forecast Collapse in Time-Series Foundation Models* — 系统剖析时序大模型在高噪声与极端突变下的预测崩溃 (Forecast Collapse) 退化机理，提出崩溃指数评估红线。
9. **[arXiv:2608.15291]** *ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning* — 提出波动感知选择性大模型推理门控，仅在不规则突变发生时唤醒重型 LLM 思考，节约超 70% 算力开销。
10. **[arXiv:2608.20005]** *Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking* — 提出多补丁跨尺度对齐与混合掩码机制，破除不同工业领域物理量纲悬殊导致的尺度震荡。
11. **[arXiv:2608.24033]** *ChorusTIC: Training-Free Multivariate Time Series Classification via Chorus In-Context Learning* — 提出基于多通道提示合唱的免训练上下文学习分类，实现无需微调的零样本多变量分类。
12. **[arXiv:2609.04239]** *EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series* — LG AI Research 推出面向高频金融市场的无注意力 (Attention-Free) 时序基础模型，基于循环状态空间线性复杂度建模多资产订单簿。
13. **[arXiv:2609.06008]** *Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series Foundation Model* — 利用 TimesFM-3 (330M) 残差分布构建误差有界 ($\epsilon$-bounded) 压缩算法，实现工业时序 4-10 倍高倍率无损保真压缩。
14. **[arXiv:2609.20554]** *Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models* — 严格实证审判预训练阶段违背单向时序因果（未来信息泄露）诱发的前瞻偏误与真实下游负迁移。
15. **[arXiv:2609.28582]** *SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models* — 提出步阶梯度对齐 (Step-wise Gradient Alignment) 框架，有效抑制长视野自回归发散，大幅改善多步概率区间校准。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **全面重构与深化第 6 章（多模态时序与智能体演进）**：
  - 新增涵盖 14 种前沿代表性系统的综合全景对比矩阵表（6.1 节），横跨 Time-LLM、TimeBraid、VisionTS、DiTS、GALA、ReasonCast、ChatAD、TimEvolve、FactoryNet 等；
  - 形式化推导 57 页统一大模型 TimeBraid 的交错全局残差注意力机制与联合优化损失（6.2.1 节）；
  - 系统推导 GALA 生成感知跨模态对齐扩散合成损失函数（6.2.2 节）；
  - 形式化一维时序到二维画面的连续流形渲染算子 $\Phi_{\text{render}}$ 并梳理视觉时序与扩散 Transformer（6.3 节）；
  - 建立时序决策智能体的部分可观测马尔可夫决策过程 (POMDP) 理论形式化（6.4.1 节）；
  - 剖析 ReasonCast 波动感知选择性推理门控，揭示节约 70% 算力的架构机理（6.4.2 节）；
  - 阐述 ChatAD 8B 多轮排查演化、TimEvolve 部署即监督的在线自进化策略与 AION 自主科研闭环（6.4.3 节）；
  - 首次系统剖析 FactoryNet 涵盖 6 大类物理具身装备（数控机床、工业六轴机械臂、重型冲压机、分拣传送线、包装机、注塑机）的 5100 万点多通道遥测具身时序大模型体系与跨本体迁移（6.5 节）。
- **同步更新第 4、5、7、8、9 章**：
  - 4.1 核心模型对比表扩充至 33 款主流模型，新增 KAIROS、UniShape、LeNEPA、Scale-Aware、EXAONE Finance 1.0 与 Cadence；
  - 4.7-4.9 扩充形态感知基元、免数据增强隐状态预测、无注意力状态空间与非自回归并行架构；
  - 5.1/5.6 引入时序后训练统一框架、真实邻域正则化强化学习后训练数学形式化以及 ChorusTIC 合唱上下文学习；
  - 7.1 评测对比表扩充至 23 个主流基准框架，涵盖 FactoryNet、Look-Ahead Bias 审计、Forecast Collapse 崩溃分析、SGA 步阶梯度对齐、AION 科研评测；
  - 7.2-7.4 深入剖析前瞻偏误预训练负迁移、预测崩溃机理与多步滚动梯度对齐；
  - 8.1-8.2 同步更新清华 THUML（TimeAgent）与金明团队（LeNEPA、AION、ChatAD）；
  - 9 开放问题深入剖析时序强化学习策略崩塌防御、前瞻偏误自动化审计以及工业具身多物理实体大模型。
- **全量同步参考文献**：Section 10 收录全部 123 篇核验文献，同步生成 123 条 BibTeX 记录 (`survey/references.bib`) 与 README.md。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：增加 KAIROS、UniShape、LeNEPA、Scale-Aware、Cadence 等新里程碑模型，优化高低引线布局，彻底消除文字重叠；
  2. `open_weight_share.png`：准确反映 123 篇论文中 61.0% 开源权重、38.2% 基准/提示/综述、0.8% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：扩充具身遥测、形态基元、非自回归、无注意力、选择性推理等前沿分支；
  4. `model_size_vs_date.png`：新增 Cadence (330M) 标度点并精准调优标注排布；
  5. `papers_by_category_year.png`：更新至 123 篇文献的历年发表堆叠分布柱状图。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（JSON 结构校验、图表生成、综述 450 处引用/锚点/图片存在性校验、BibTeX 生成、README Awesome 清单生成）全部 100% 一次性通过。

### 7. 提交与推送状态
- **本地提交**：`feat(iteration-4): deepen multimodal TS & agents, integrate 15 papers (123 total), refine figures`
- **推送状态**：推送至远端 `origin/main` 并经 `git status` / `git log` 确认。

### 8. 下一轮运行重点
- 探究时序后训练强化学习连续策略界限（高频扩散流中的收敛界与李雅普诺夫稳定性）；
- 研发面向万亿级 TSFM 预训练语料的前瞻偏误自动化因果隔离审计工具箱；
- 追踪通用人形机器人与重工业机电融合的超高频时序动力学表征大模型；
- 监测 TimeMixer++ 官方开源合规进展。

---

## 2026-09-25 (第 3 轮运行：大语言模型赋能时序全面深化、前沿 15 篇收录与图表重构 / Iteration 3)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 3 轮迭代（上一轮 14 篇论文二次复核、近 45 天高影响力文献与重点团队前沿检索、第 5 章大语言模型赋能时序全面深化、图表质检与质量门禁）
- **文献总数**：108 篇经 arXiv HTTPS API 严格核验的论文（原 93 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (14 篇)
通过 arXiv Atom HTTPS API (`no_proxy=*`) 全量复核上一轮收录的 14 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2510.12681` (CoRA), `2601.03248` (STReasoner), `2601.19040` (OATS), `2602.06597` (DiTS), `2606.01498` (TimeSage-MT), `2607.24892` (LLM as Planner), `2608.14270` (TimeSage-EV), `2609.10357` (Contamination Hold-Out), `2609.13640` (FlowTSFM), `2609.16804` (SOTER), `2609.20156` (QUALS), `2609.21425` (Tracing Evidence), `2609.24862` (TimEvolve), `2609.25980` (Interweaving Marginals).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2502.21245]** *TimesBERT: A BERT-Style Foundation Model for Time Series Understanding* — 清华大学 THUML 龙明盛团队，系统论证时序理解（分类、插补、异常检测）中全局双向注意力的不可替代性，提出双向补丁掩码重建 BERT 基础模型。
2. **[arXiv:2509.23695]** *Estimating Time Series Foundation Model Transferability via In-Context Learning* — 金明团队，首创基于免梯度在途上下文学习探针量化 TSFM 迁移能力的方法，秒级预估目标域微调收益，斯皮尔曼等级相关达 0.867。
3. **[arXiv:2601.13546]** *ChatAD: Reasoning-Enhanced Time-Series Anomaly Detection with Multi-Turn Instruction Evolution* — 金明团队与微软，构建 8B 参数多轮指令演化时序异常检测推理智能体，支持人机多轮追问根因。
4. **[arXiv:2608.01290]** *FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting* — Chronos 家族联邦参数高效微调 (PEFT) 框架，解决跨机构大宗商品时序数据隐私壁垒，误差下降 18.4%-32.7%。
5. **[arXiv:2608.05571]** *Align-RAG: Alignment Is All You Need for TSFM In-Context Learning* — 斯坦福与哈佛团队，颠覆端到端复杂检索适配器，严格闭式推导最优仿射变换尺度与相移 ($\alpha^*, \tau^*$)，以纯数学闭式解实现零训练时序 RAG 对齐；官方代码已核验：`https://github.com/masadi-99/align-rag`。
6. **[arXiv:2608.22968]** *Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study* — 录用于 CIF 2026，系统度量大规模 TSFM 与轻量基线 (TTM/LightGBM) 在连续工业监控中的边际经济回报与能耗开销。
7. **[arXiv:2608.24303]** *Causal Analysis for Time Series Foundation Models* — 建立结构因果模型 (SCM) 反事实审计框架，警告跨能源、金融与气候领域广泛依赖单一头部 TSFM 所带来的系统性集中脆弱性风险 (Concentration Risk)。
8. **[arXiv:2609.09586]** *Distillation of Synthetic Data for Time Series Foundation Models* — 提出针对时序基础模型预训练的数据集蒸馏/浓缩算法，在已知动力学生成过程下反向提取代表性合成轨迹，以 10% 语料达到全量训练效果。
9. **[arXiv:2609.11993]** *FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences* — 摩根士丹利等团队，构建首个结合多智能体金融推演仿真与真实微观订单簿的多模态金融事件序列基准。
10. **[arXiv:2609.12412]** *HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications* — 建立跨边缘 GPU、微控制器等多硬件的信息物理与物联网 (CPS-IoT) 综合能耗、内存带宽与实时延迟部署基准。
11. **[arXiv:2609.28506]** *TW3Cast: A Frozen Router of Lightly Fine-Tuned Foundation Models for Time-Series Forecasting on GIFT-Eval, Selected Entirely on the Training Split* — 提出突破性的轻量级冻结门控路由器范式，仅在训练切分上拟合动态路由，在 GIFT-Eval 榜单取得第 3 名顶尖成绩。
12. **[arXiv:2609.21381]** *Knowledge-Graph-Augmented Chronos-2 for HEC-RAS Surrogate Forecasting* — 将水动力学河网物理知识图谱注入 Chronos-2 跨注意力机制，在具有强回水效应的极端水文场景中构建高精度替代预测模型。
13. **[arXiv:2609.28576]** *Time-Series Foundation Models That Understand Data Revisions* — 揭露宏观统计数据在发布后多次修正导致的“未来数据穿越”系统性漏洞，提出首个版本感知的 VINTAGE-TS 适配框架。
14. **[arXiv:2609.29792]** *TimeBraid: Unifying Time Series and Language for Understanding and Forecasting* — 57页长篇巨制，提出交错全局残差注意力机制，实现预训练语言模型与预训练时序基础模型的深层编织，统一数值预测与开放推理。
15. **[arXiv:2609.29814]** *SwitchPFN: Shared Switching Dynamics for Frozen In-Context Time Series Classification* — 将先验数据拟合网络 (PFN) 拓展至分段切换动力系统，在离线拟合海量自回归切换过程后，实现完全冻结参数的高精度零样本时序分类。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **全面重构与深化第 5 章（大语言模型赋能时序）**：
  - 新增涵盖 12 大主流方法的跨模态赋能范式对比矩阵表（涵盖基础大模型、范式类别、跨模态对齐机制、输入模态、可训练参数占比、核心亮点、计算开销与延迟）；
  - 形式化推导补丁重编程映射、自然语言前缀提示与词表子空间投影数学表达（5.1.1 节）；
  - 给出 Align-RAG 闭式无训练最优几何仿射对齐的严格数学形式化与解析解推导（5.1.2 节）；
  - 形式化拆解基于在途上下文似然增益差分探针的基础模型可迁移性预估理论（5.1.3 节）；
  - 深化模型重编程与适配器路线、直接提示与双层规划协作、跨模态对比微调与空间强化学习、检索增强与上下文示范自适应（5.2-5.5 节）。
- **同步更新第 4、6、7、8、9 章**：
  - 4.1 核心模型对比表扩充至 27 款主流模型，新增 TimesBERT、SwitchPFN 与 TW3Cast；
  - 4.2 融入 FedChronos 隐私微调与 KG-Chronos-2 水利图谱增强；
  - 6.1-6.3 融入 57页统一大模型 TimeBraid、金融仿真 FINESSE 以及多轮异常根因推理 ChatAD；
  - 7.1 评测对比表扩充至 18 个主流基准框架，涵盖 HoliBench、Cost-Aware Study、Causal Analysis、VINTAGE-TS、FINESSE；
  - 8.1-8.2 同步扩充清华 THUML 与金明团队重点成果；
  - 9 开放问题深入剖析合成数据蒸馏、系统集中脆弱性风险、工业端侧云边协同与自进化智能体。
- **全量同步参考文献**：Section 10 收录全部 108 篇核验文献，同步生成 108 条 BibTeX 记录 (`survey/references.bib`)。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：增加 2026 年底密集发布模型（TimeBraid、QUALS、FlowTSFM、Tabby）的高低交错与引线布局，彻底消除文字重叠；
  2. `open_weight_share.png`：准确反映 108 篇论文中 59.3% 开源权重、39.8% 基准/提示/综述、0.9% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：画布拓宽至 16.5x8.5 英寸，完美容纳切换动力学 PFN、循环分位数传输、因果嵌入、版本审计等全部技术分支；
  4. `model_size_vs_date.png`：精确绘制参数标度前缘（直至 8.3B Timer-S1 与 8B ChatAD/TimeOmni-1）；
  5. `papers_by_category_year.png`：更新至 108 篇文献的历年发表堆叠分布柱状图。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（JSON 结构校验、图表生成、综述 371 处引用/锚点/图片存在性校验、BibTeX 生成、README Awesome 清单生成）全部 100% 通过。

### 7. 提交与推送状态
- **本地提交**：`feat(iteration-3): deepen LLM4TS paradigms, integrate 15 papers (108 total), refine figures`
- **推送状态**：推送至远端 `origin/main` 并经 `git status` / `git log` 确认。

### 8. 下一轮运行重点
- 持续跟进 KAIROS 非自回归快速预测变体 (arXiv: 2510.02084) 的消歧评测；
- 探索时序具身智能与机器人动力学多通道反馈中的基础模型迁移表现；
- 监测 TimeMixer++ 官方开源合规进展。

---

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
