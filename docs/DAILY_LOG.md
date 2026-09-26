# Maintenance Daily Log / 每日维护日志

## 2026-09-26 (第 8 轮运行：开放问题与未来前沿理论深化、15 篇前沿收录与全景矩阵扩充 / Iteration 8)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 8 轮迭代（上一轮 15 篇论文二次复核、近 45-60 天高影响力文献与重点团队前沿检索、第 9 章开放问题与未来方向理论全景深化、全套图表生成与排版质检、全自动化质量门禁）
- **文献总数**：183 篇经 arXiv HTTPS API 严格核验的论文（原 168 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (15 篇)
通过 arXiv Atom HTTPS API 全量复核上一轮收录的 15 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2607.00956` (Aionoscope), `2608.13262` (ORBIT), `2608.14067` (When Denoising Hurts), `2608.20024` (TabPFN-TS District Heating), `2608.23473` (MetaCaster), `2608.26226` (LLM Agents Survey), `2608.30976` (Human-in-the-Loop Agent), `2608.31013` (TSPFN), `2609.01896` (OutageDiT), `2609.02068` (DynG-Diff), `2609.06006` (Memory in Deep TS), `2609.08375` (IPM-FM), `2609.09195` (CompEvo), `2609.20193` (Retrieval Regime), `2609.20535` (FreqCondNorm).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2607.01204]** *TiRex-2: Generalizing TiRex to Multivariate Data and Streaming* — JKU Linz / NX-AI，将 xLSTM 架构扩展至通用多变量流式时序基础模型，构建基于块对角指数门控与矩阵记忆单元的循环状态机，打破二次方注意力开销，实现 $\mathcal{O}(1)$ 流式单步推断时间与 $\mathcal{O}(d^2)$ 恒定内存。
2. **[arXiv:2607.14510]** *VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence* — 工业智能前沿团队，提出视觉-语言-时序三模态统一基础模型，协同对齐设备热像图、运维文本工单与毫秒级机电传感波形。
3. **[arXiv:2602.17634]** *Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting* — 提出倒置 Transformer (Inverted Transformer) 架构下的参数高效零样本计算缩放新范式，大幅削减激活参数量并在跨域预测中保持顶尖泛化能力。
4. **[arXiv:2606.16545]** *Can LLM Coding Agents Reason About Time Series?* — 首次将 LLM 代码智能体置于真实端到端时序分析工程流水线中进行严苛审计，揭示智能体在不规则采样、滑动窗口边界效应与时序因果反转中的推理隐患。
5. **[arXiv:2606.05404]** *Harnessing Generalist Agents for Contextualized Time Series* (TimeClaw) — iDEA-iSAIL Lab (UIUC)，构建面向富上下文复杂时序问答与预测的通用智能体系统，支持动态时序专业工具调用与执行编排；官方代码经由 GitHub API 核验通过 (`https://github.com/iDEA-iSAIL-Lab-UIUC/TimeClaw`)。
6. **[arXiv:2609.11282]** *When Does Text Inform? Benchmarking Information-Theoretic Metrics for Multimodal Time-Series Forecasting* — 从信息论（互信息、条件熵、传递熵）底层系统建立评测基准，严格划定多模态文本产生正向收益的因果信息流动边界。
7. **[arXiv:2609.14142]** *T-SMART: Mechanism-Level Attribution for Tool-Augmented Time-Series Question Answering* — ICTAI 2026，提出面向工具增强时序问答系统的机制级归因框架，精准追溯工具调用链中的参数抽取与工具本身的逻辑失效节点。
8. **[arXiv:2609.13454]** *Hindsight Bias in Clinical Temporal Reasoning: How Future Data Exposure Affects Large Language Model Judgment* — ML4H 2026，揭示重症监护 (ICU) 与临床多模态病历中普遍存在的后瞻偏误 (Hindsight Bias)，严谨实证未来病程微泄漏导致大模型虚假繁荣与因果扭曲。
9. **[arXiv:2608.26829]** *SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting* — 提出变量级语义增强框架，为多变量时序中的每个物理通道建立细粒度语义绑定与独立视觉通道投影，消除跨通道语义混淆。
10. **[arXiv:2608.14054]** *Model-agnostic Retrieval-Augmented Extended Forecasting for time series* (R-AF) — 提出模型无关的时序检索增强长视野预测框架，无需重新训练或微调即可将任意标准短视野 TSFM 的预测范围扩展数倍。
11. **[arXiv:2607.12248]** *When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting* — 深入揭露金融量化中方向准确率 (DA) 受资产长期趋势自然基准率偏置欺骗的漏洞，提出无偏评估基准并审计 LoRA 适配 TimesFM 的真实外推表现。
12. **[arXiv:2609.16415]** *How Good Are Time-Series Foundation Models for Pedestrian Crowd Count Forecasting? A Cross-Dataset Comparative Study* — IEEE ITSC 2026，首次跨多个真实城市与空间尺度系统评估现代 TSFMs 在行人群体密集度时序上的零样本泛化能力与时空拓扑约束应对策略。
13. **[arXiv:2609.11135]** *Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with Large Language Models* — 构建将全天空成像仪 (TSI) 鱼眼云图与微秒级地面辐照度时序双向跨模态融合的 LLM 预测架构，联合流体力学演化与数值外推提升太阳能光伏预测精度。
14. **[arXiv:2604.12659]** *Do VLMs Truly "Read" Candlesticks? A Multi-Scale Benchmark for Visual Stock Price Forecasting* — 对声称能够看懂金融 K 线图的视觉语言大模型展开多尺度扰动与几何结构伪造审计，揭示多数模型仅依赖表面颜色与条形长短等视觉捷径。
15. **[arXiv:2606.03629]** *TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning* — 提出首个面向时序数据专业质量评级的智能体系统，通过链式推理自主探测时序传感器漂移、异常脉冲与逻辑违背，实现专业级数据清洗与评级。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **核心深化：全面重构并深度强化第 9 章（开放问题与未来方向）**：
  - 9.1 建立物理守恒公理与时空神经动力学融合的解析形式化，严格推导质量/动量/能量连续性方程与哈密顿保辛几何约束，剖析自由自注意力统计相关性与经典物理公理的本质冲突，提出可微流形投影、跨频段参数归一化与多模态物理大模型破局路线（FactoryNet [arXiv:2605.09081], FreqCondNorm [arXiv:2609.20535], VLT [arXiv:2607.14510]）；
  - 9.2 从信息论视角推导时序可预测性上界与互信息指数衰减律 $I \propto e^{-\lambda H}$，形式化揭示均方误差下极低信噪比诱发“预测崩溃 (Forecast Collapse)”退化为常数均值的临界相变机理，结合逆向去噪终端步漂移、金融方向率欺骗与文本信息论有效性（Forecast Collapse [arXiv:2608.14106], When Denoising Hurts [arXiv:2608.14067], When Does Text Inform? [arXiv:2609.11282], Base-Rate Honest TimesFM [arXiv:2607.12248]）；
  - 9.3 形式化动态时序结构因果模型 (Dynamic TSCM) 与 Pearl 反事实硬干预算子 $do(\mathbf{a}^*)$，揭示纯被动观测数据预训练诱发的混淆偏差与行业集中性脆弱风险（DoTime [arXiv:2607.27263], Causal Analysis [arXiv:2608.24303], Clinical Hindsight Bias [arXiv:2609.13454]）；
  - 9.4 剖析具身机器人与机电高频遥测的二次方算力与显存崩塌，推导具备 $\mathcal{O}(1)$ 单步时间复杂度与 $\mathcal{O}(d^2)$ 恒定内存的 xLSTM 矩阵状态流式递推架构与参数高效零样本计算缩放（TiRex-2 [arXiv:2607.01204], Reverso [arXiv:2602.17634], HoliBench [arXiv:2609.12412]）；
  - 9.5 建立时序决策智能体离散时间动态闭环反馈控制系统与误差动力学方程，严格推导李雅普诺夫渐近稳定性准则与认知摄动界 $\epsilon_{\text{robust}}$，防范误差级联发散（TimeClaw [arXiv:2606.05404], TSQAgent [arXiv:2606.03629], T-SMART [arXiv:2609.14142], CastFSR [arXiv:2608.03031], CTRL [arXiv:2609.23257], Coding Agent TS Reasoning [arXiv:2606.16545]）；
  - 9.6 首创构建 **9.6 全景开放挑战与未来破局路线矩阵 (Table 9.1)**，跨 6 大核心科学维度全面解构科学瓶颈、数学根源、失效范式、破局路线与关键评测里程碑。
- **全景融合 15 篇文献至各大章节**：
  - 4.1 核心对比矩阵扩充 TiRex-2、Reverso、VLT；4.10 展开多变量流式架构、参数高效缩放与工业三模态大模型；
  - 5.1 对比矩阵扩充 R-AF；5.5 详细展开模型无关检索增强长视野预测；
  - 6.1 对比矩阵扩充 TimeClaw、TSQAgent、T-SMART、VLT、SAGE、Solar-Sky-TS；6.3 展开变量级语义增强与地空双向融合；6.4 展开通用上下文智能体、数据质量诊断与机制级归因；
  - 7.1 对比矩阵扩充至 44 个基准体系；7.2 展开临床后瞻偏误与金融方向基准率审判；7.3 展开文本信息论基准、蜡烛图 VLM 真伪评测、时序代码智能体评测与客流密集度评测；
  - 全量同步参考文献：Section 10 收录全部 183 篇核验文献，同步生成 183 条 BibTeX 记录 (`survey/references.bib`) 与 README.md。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：新增 Reverso, TimeClaw, TiRex-2, VLT 等 2026 前沿里程碑，交错纵轴坐标与水平微调，彻底消除 label 重叠；
  2. `open_weight_share.png`：精准反映 183 篇论文中 48.1% 开源权重模型、51.4% 基准/提示/综述、0.5% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：更新四维设计空间拓扑树状图，更新叶子节点；
  4. `model_size_vs_date.png`：更新模型参数量与发布日期分布；
  5. `papers_by_category_year.png`：更新至 183 篇文献的历年发表堆叠分布柱状图。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（183 篇唯一 ID 校验、5 组图表生成与校验、765 处文献与图片锚点引用校验、BibTeX 生成、README.md 自动化生成）全部 100% 一次性通过。

### 7. 下一轮规划与重点
1. **多模态图表看图预测跨分辨率超轻量化**：探索在边缘视觉芯片上实现微秒级视觉时间序列掩码推断与形态保真；
2. **时序因果结构发现与反事实推演统一架构**：结合 DoTime 与动态 TSCM，攻克 TSFMs 在外生干预下的泛化理论下界；
3. **具身多本体触觉-力觉物理遥测跨模态大模型**：持续追踪通用人形机器人动力学与重工业机电融合的超高频时序动力学表征；
4. **时序多尺度自适应微调理论**：跟进参数高效迁移中的频域秩约束与自适应奇异值截断前沿；
5. **TimeMixer++ 永久公开开源状态跟进**：持续监测官方仓库公司合规审查与权重发布进展。

## 2026-09-26 (第 7 轮运行：分类体系全景重构与五大计算范式数学深化、15 篇前沿收录与图表质检 / Iteration 7)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 7 轮迭代（上一轮 15 篇论文二次复核、近 45-60 天高影响力文献与重点团队前沿检索、第 3 章分类体系全景重构与五大计算范式数学深化、全套图表生成与排版质检、全自动化质量门禁）
- **文献总数**：168 篇经 arXiv HTTPS API 严格核验的论文（原 153 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (15 篇)
通过 arXiv Atom HTTPS API 全量复核上一轮收录的 15 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2510.02729` (Accuracy Law), `2510.03519` (TS-Reasoner), `2512.18610` (EOB), `2602.01937` (T-LLM), `2602.07695` (EventCast), `2602.17706` (PaCoDi), `2606.27711` (The Simulacrum), `2607.06504` (RMISC), `2607.27263` (DoTime), `2608.03031` (CastFSR), `2608.03391` (TimeRLM), `2608.22321` (Text Sensitivity), `2608.23058` (LLM-Agent Survey), `2609.13345` (Probabilistic Survey), `2609.23257` (CTRL).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2607.00956]** *Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations* — 金明团队（KDD MILETS 2026），提出首个面向时序基础模型潜空间可访问性 (Latent-State Accessibility) 的调试与探测框架，官方代码经由 GitHub API 核验通过 (`https://github.com/langotime/aionoscope`)。
2. **[arXiv:2608.13262]** *Into the ORBIT for Time Series: Training Regimes for Foundation Models* — 深入探究混合预训练中不同行业领域（金融、交通、气象、工业）的数据配比失衡对零样本下游迁移能力的深远影响，提出动力学多样性平衡采样准则与 ORBIT 评测基准。
3. **[arXiv:2608.14067]** *When Denoising Hurts: Rethinking the Terminal Step of Diffusion Time Series Forecasters* — 揭示扩散时序生成中的“终端阶段漂移 (Terminal Step Drift)”机理，证明在低信噪比下终端去噪会破坏关键波形，提出自适应提前停止准则。
4. **[arXiv:2608.20024]** *Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks* — 首次对先验数据基础模型 TabPFN-TS 在大型城市区域集中供热网中真实零样本概率热负荷预测进行系统性评估，验证了无微调贝叶斯后验拟合的高工程实用性。
5. **[arXiv:2608.23473]** *MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters* — EMNLP 2026，提出 Meta-Harness 优化智能体框架，利用元学习机制动态搜索并优化轻量级时序模型的提示词与微调参数，在极端少样本工业预测场景下实现高精度收敛。
6. **[arXiv:2608.26226]** *LLM Agents for Time-Series: A Survey* — Salesforce Research Moirai 团队与学术界联合发布（Findings of EMNLP 2026），全面系统地回顾了 LLM 赋能时序智能体的最新进展，确立了统一认知框架与决策评价基准。
7. **[arXiv:2608.30976]** *A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting* — 针对关键重工业预测场景建立人机协同 (Human-in-the-Loop) 双层治理架构，智能体在低置信度或动力学突变时主动请求专家确认，兼顾高自治与工业安全生产。
8. **[arXiv:2608.31013]** *TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification* — STACOM 2026，将先验数据网络扩展至多变量生理信号领域，基于 14 万条合成多元生理动力学轨迹预训练，在零样本重症监护多通道分类上取得优异性能；官方代码经由 GitHub API 核验通过 (`https://github.com/Jeremstym/TSPFN`)。
9. **[arXiv:2609.01896]** *OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation* — 将 Diffusion Transformer (DiT) 架构成功迁移至电力网格突发大面积停电预测与级联故障情景仿真，支持极端天气条件引导的高保真生成。
10. **[arXiv:2609.02068]** *DynG-Diff: A State-Aware Dynamic Guidance Diffusion Framework for Probabilistic Time Series Forecasting* — 提出状态感知动态引导扩散架构 (DynG-Diff)，依据各通道当前隐状态的动力学显著性动态调节反向扩散过程中的条件引导强度；官方代码经由 GitHub API 核验通过 (`https://github.com/TT-20011031/DynG-Diff`)。
11. **[arXiv:2609.06006]** *Memory in Deep Time-Series Models* — 理论与实证严格审查深度时序模型的记忆容量边界，通过受控时滞测试揭示 Transformer 注意力弥散与 Softmax 温度退化导致的指数级记忆衰减。
12. **[arXiv:2609.08375]** *IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring* — 针对工业过程监控中的多传感器干扰，提出融合共识特征选择 (Consensus Feature Selection, CFS) 与 MC-Dropout 不确定性估计的自监督工业基础模型。
13. **[arXiv:2609.09195]** *CompEvo: Competition-Induced Evolution for Multi-Agent in News-Driven Time Series Forecasting* — 针对突发新闻驱动的高波动时序，构建基于博弈论的竞争演化多智能体系统，通过角色博弈推动预测假说的自主迭代淘汰。
14. **[arXiv:2609.20193]** *When Does Retrieval Help Time-Series Forecasting?* — 首次对时序检索增强 (RAG) 机制展开严格实证审计，揭示时序 RAG 产生正向收益的“临界操作区间 (Critical Operating Regime)”，指出上下文充足时强行检索会诱发模式相位饥饿；官方代码经由 GitHub API 核验通过 (`https://github.com/KurbanIntelligenceLab/retrieval-regime`)。
15. **[arXiv:2609.20535]** *FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned Transformer Foundation Model* — 提出面向工业跨领域预测维护的频率条件归一化 Transformer 基础模型，通过条件归一化调制算子统一 1Hz 到 100kHz 振动信号，实现跨物理装备零样本迁移。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **核心深化：全面重构并深化第 3 章（分类体系）**：
  - 3.1 形式化定义四维正交分类理论设计空间 $\mathcal{S} = \langle \mathcal{A}, \mathcal{T}, \mathcal{M}, \mathcal{E} \rangle$；
  - 3.2 深度解构五大核心计算范式（因果自回归解码器、双端编码-解码器、纯双向编码器掩码自编码、稀疏 MoE 与频域路由、连续动力学/扩散生成/先验拟合）的因果掩码、损失目标与设计权衡；
  - 3.3 严格推导连续补丁化、离散分箱量化、频域复数小波、形态基元与跨频段自适应归一化 (FreqCondNorm) 的度量与计算权衡；
  - 3.4 形式化通道拓扑演化路径：从通道独立 (CI) 到通道依赖 (CD)、任意变量统一 (vRoPE Any-variate) 到动态状态引导 (DynG-Diff) 与共识特征拓扑 (IPM-FM)；
  - 3.5 首创 **3.5 时序基础模型多维技术分类对比矩阵**，涵盖 12 种主流技术路线、跨 8 个核心维度的全景横向技术解构。
- **全景融合 15 篇文献至各大章节**：
  - 4.1 核心对比矩阵扩充 TSPFN、OutageDiT、DynG-Diff、IPM-FM、FreqCondNorm；4.8 扩充工业监控与预测维护；4.9 扩充动态引导扩散与终端去噪漂移；4.10 扩充 ORBIT 预训练机制基准；
  - 5.5 扩充时序检索增强有效性临界区间研究 (When Does Retrieval Help?)；
  - 6.1 对比矩阵扩充 Salesforce 智能体综述、MetaCaster、CompEvo、人机协同工业智能体；6.4 详细展开这四大智能体架构与治理范式；
  - 7.1 对比矩阵扩充至 38 个基准框架；7.2 展开深度时序模型记忆容量理论审计；7.3 展开 Aionoscope 隐状态可访问性调试探针；
  - 8.2 金明团队纳入 Aionoscope [arXiv:2607.00956]；8.4 Salesforce 团队纳入时序智能体系统综述 [arXiv:2608.26226]；
  - 9 开放问题深入融合 ORBIT 数据配比平衡、扩散终端步漂移、时序 RAG 临界区间、跨频段预测维护与人机协同安全生产。
- **全量同步参考文献**：Section 10 收录全部 168 篇核验文献，同步生成 168 条 BibTeX 记录 (`survey/references.bib`) 与 README.md。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：微调时间线引线分层，增加 TSPFN, OutageDiT, IPM-FM 等 2026 最新里程碑标注，交错纵轴坐标，完全消解密集重叠；
  2. `open_weight_share.png`：精确反映 168 篇论文中 48.8% 开源权重模型、50.6% 基准/提示/综述、0.6% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：更新四维设计空间拓扑树状图，更新叶子节点；
  4. `model_size_vs_date.png`：全面展示从微型 TTM (8M)、CITRAS-FM (7M) 到百兆级 TimesFM、Chronos，再到十亿级 Moirai-MoE (1.1B)、Sundial (1.5B)、Time-MoE (2.4B)、Toto 2.0 (2.5B) 及旗舰 Timer-S1 (8.3B) 的标度分布曲线；
  5. `papers_by_category_year.png`：更新至 168 篇文献的历年发表堆叠分布柱状图，展示 2026 年突破 100 篇大关的态势。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（168 篇唯一 ID 校验、5 组图表生成与校验、675 处文献与图片锚点引用校验、BibTeX 生成、README.md 自动化生成）全部 100% 一次性通过。

### 7. 下一轮规划与重点
1. **多模态图表看图预测跨分辨率超轻量化**：探索在边缘视觉芯片上实现微秒级视觉时间序列掩码推断与形态保真；
2. **时序因果结构发现与反事实推演统一架构**：结合 DoTime 等因果生成基准，攻克 TSFMs 在外生干预下的泛化理论下界；
3. **具身多本体触觉-力觉物理遥测跨模态大模型**：持续追踪通用人形机器人动力学与重工业机电融合的超高频时序动力学表征；
4. **时序多尺度自适应微调理论**：跟进参数高效迁移中的频域秩约束与自适应奇异值截断前沿；
5. **TimeMixer++ 永久公开开源状态跟进**：持续监测官方仓库公司合规审查与权重发布进展。

## 2026-09-26 (第 6 轮运行：重点课题组全景矩阵深化、底层数学理论四维推导、15 篇前沿收录与图表重构 / Iteration 6)

### 1. 今日运行概览
- **维护人员**：Antigravity Autonomous Agent (`lihuirui`)
- **运行性质**：第 6 轮迭代（上一轮 15 篇论文二次复核、近 45 天高影响力文献与重点团队前沿检索、第 8 章重点课题组全景矩阵全面深化、第 2 章底层数学理论深度推导、图表排版质检与全自动化质量门禁）
- **文献总数**：153 篇经 arXiv HTTPS API 严格核验的论文（原 138 篇 + 本轮新增 15 篇，严格遵守 <=15 篇增量约束）

### 2. 上一轮新增论文复核 (15 篇)
通过 arXiv OAI-PMH / Atom HTTPS API 全量复核上一轮收录的 15 篇文献，标题、作者与发布时间均 100% 完全匹配：
`2601.19151` (TS-Debate), `2604.10544` (WaveMoE), `2605.10292` (LeapTS), `2605.13711` (MILM), `2605.17340` (Olivia), `2605.20268` (Chronicle), `2605.27286` (Falcon-X), `2605.29401` (PostTime), `2606.10798` (CITRAS-FM), `2606.18367` (Regime-Dependent), `2606.28670` (MACROCAST), `2607.01918` (Zeus), `2607.04919` (Break-Even), `2608.17164` (SCENARIODIFF), `2609.22836` (VersaTSA).

### 3. 本轮新增与核验论文 (15 篇)
1. **[arXiv:2510.02729]** *Exploring Accuracy Law for Deep Time Series Forecasters: An Empirical Study* — 清华大学 THUML 龙明盛团队，系统研究回看窗口 $L$ 与预测视野 $H$ 及模式复杂度 $\mathcal{C}_P$ 对误差的解析幂律约束，确立时序精度定律 (Accuracy Law)。
2. **[arXiv:2602.17706]** *Parallel Complex Diffusion for Scalable Time Series Generation* — 金明团队与温青山团队等，PaCoDi: 首创将时序映射至复数谱平面的并行复数扩散生成架构，实现全频段一步单次去噪生成，长序列生成吞吐提升数十倍；官方代码经 GitHub API 核验通过 (`https://github.com/RongyaoCai/PaCoDi`)。
3. **[arXiv:2512.18610]** *The Procrustean Bed of Time Series: The Optimization Bias in Point-wise Loss Functions* — 金明团队与温青山团队等，从数学上揭示传统逐点 MSE/MAE 优化对微观相位抖动信号造成的高频振幅指数衰减效应（普洛克路斯忒斯之床），提出频域谱匹配与梯度对齐的结构去偏目标。
4. **[arXiv:2602.07695]** *EventCast: Hybrid Demand Forecasting in E-Commerce with LLM-Based Event Knowledge* — 金明团队等，针对电商大促与营销事件导致的突发需求尖峰，利用 LLM 构建事件知识图谱并与时序骨干进行混合图注意力预测。
5. **[arXiv:2607.06504]** *RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models* — 开源目前规模领先的真实多变量工业与科研预训练语料库，包含 1420 亿真实观测点 (142B)，涵盖电网、重工制造、气象与交通等 10 余个关键工业垂直领域。
6. **[arXiv:2606.27711]** *The Simulacrum: Decision-Theoretic Pretraining for Near-Optimal Time-Series Forecasting and Inference* — Monash / Sydney 等，提出决策论预训练架构 (The Simulacrum)，直接在随机过程先验分布族上极小化有限样本贝叶斯风险，使模型在零样本下输出契合下游任意非对称业务效用的贝叶斯近最优决策。
7. **[arXiv:2510.03519]** *TS-Reasoner: Aligning Time Series Foundation Models with LLM Reasoning* — 构建时序数值隐式表征与大语言模型思维链 (CoT) 的双向认知投影通道，兼顾高精度数值预测与因果自然语言解释归因。
8. **[arXiv:2602.01937]** *T-LLM: Teaching Large Language Models to Forecast Time Series via Temporal Distillation* — 提出时序知识蒸馏框架，将预训练高精度 TSFM 教师网络的状态转移矩阵与频域特征蒸馏注入大语言模型学生网络。
9. **[arXiv:2609.23257]** *CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning* — 将预测过程重塑为现代状态空间闭环反馈控制系统，由 LLM 作为监督控制器预测残差，结合李雅普诺夫稳定性界限彻底规避大模型幻觉导致的失稳。
10. **[arXiv:2608.23058]** *LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications* — 首次对面向预测与推断任务的 LLM 智能体系统进行系统性全景回顾，提出感知、规划、工具使用与反思进化的四层系统化分类法。
11. **[arXiv:2608.03031]** *CastFSR: A Fast--Slow--Reflect Agentic Reasoning Framework for Context-Aware Time Series Forecasting* — 提出快慢反思双系统智能体框架，轻量快系统负责惯性外推，慢系统进行因果反思，反思模块持续比对展开误差更新提示词约束；官方代码经 GitHub API 核验通过 (`https://github.com/Xiaoyu-Tao/CastFSR`)。
12. **[arXiv:2608.03391]** *TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series* — 提出递归语言模型 (Recursive Language Model)，通过多尺度分层下采样与递归聚焦，以线性复杂度实现对超长工业时序中微弱针尖异常的毫秒级定位。
13. **[arXiv:2608.22321]** *Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting* — 构建多模态文本敏感度控制实验审计体系，揭露诸多声称多模态大幅提升的模型实则对语义不敏感，并未真正利用因果文本内涵。
14. **[arXiv:2609.13345]** *Beyond Point Forecasts: A Survey on Probabilistic Forecasting for Time Series and Spatiotemporal Data* — 现代概率时序预测系统性综述，系统梳理参数分布、分位数回归、连续归一化流、扩散模型与基础模型概率校准技术谱系。
15. **[arXiv:2607.27263]** *DoTime: A Synthetic Benchmark Generator for Interventional and Counterfactual Time Series* — 首个面向动态时序的反事实基准生成器，基于 Pearl do-演算与结构因果模型 (TSCM)，为干预响应与反事实评估建立可控基石。

### 4. 活体综述重点深化 (`survey/SURVEY.md`)
- **核心深化一：全面重构与深化第 8 章（重点课题组与代表机构进展）**：
  - 8.1 清华大学 THUML 龙明盛团队：系统梳理从经典深度时序时代（TSlib 开源库、Autoformer, Informer, TimesNet, iTransformer）到大时序模型 LTM（Timer, Timer-XL, Timer-S1 8.3B MoE）、连续流匹配生成（Sundial 1.5B TimeFlow CFM）、多模态与基础理论（AutoTimes, TimeXer, TimesBERT, TimeVista, Accuracy Law 精度定律）的完整学术版图；
  - 8.2 金明团队 (Ming Jin Group, Griffith / Monash)：全面梳理重编程先驱 Time-LLM、3000亿点 2.4B 大模型 Time-MoE、Neural CDE 动态调度 LeapTS、并行复数扩散 PaCoDi、逐点损失偏误理论 EOB、8B 工业异常诊断大模型 ChatAD、自主科学研究智能体 AION、电商事件需求预测 EventCast 及动态演化基准 TimeSage 系列；
  - 8.3 亚马逊 AWS Chronos 团队：深入剖析 4096 离散分箱量化、多项式蒙特卡洛概率采样、Chronos-2 多变量联合注意力、FedChronos 联邦 PEFT 协议与 AutoGluon 工业自动化集成；
  - 8.4 Salesforce Research Moirai 团队：深入剖析 Any-variate 跨通道扁平化注意力、变量感知旋转位置编码 (vRoPE)、多尺寸补丁池 $\mathcal{P}$、Moirai-MoE 1.1B、LOTSA 270 亿语料库与 GIFT-Eval 权威基准；
  - 8.5 谷歌研究院 TimesFM 团队：深入剖析连续浮点数值与两阶段非对称投影（$P_{\text{in}}=32, P_{\text{out}}=128$）、1000 亿真实合成点预训练与 Cadence 误差有界预测残差工业压缩 ($\epsilon$-bounded)；
  - 8.6 IBM Research 与 CMU 团队：系统对比 IBM TTM (1M-8M) 极简多尺度轻量化 Mixer 微秒级端侧边缘部署与 CMU MOMENT (385M) 纯编码器掩码自编码 (MAE) 统一多任务表征；
  - 8.7 Datadog Toto 团队：深入剖析超过 1 万亿真实生产监控时序点 (1T) 预训练、开源 2.5B 模型族以及时序标度律 (Scaling Laws) 的严格工业实证；
  - 8.8 重点课题组与代表机构综合对比矩阵：构建横跨 8 大顶尖团队、8 维核心指标（学术哲学、模型矩阵、分词与损失、标志性语料、最大规模、理论创新、开源状态）的纵深横向矩阵。
- **核心深化二：全面深化第 2 章底层数学理论与公式形式化推导**：
  - 2.5 预测精度定律与窗口模式复杂度 (Accuracy Law & Pattern Complexity) [arXiv:2510.02729]：推导谱熵与局部曲率加权模式复杂度 $\mathcal{C}_P$，推导精度定律幂律函数 $\mathcal{E}(L, H) = \alpha (H/L)^\beta \exp(\gamma \mathcal{C}_P) + \mathcal{E}_\infty$ 及三阶段区间；
  - 2.6 逐点损失优化偏误与经验优化偏差 (Optimization Bias EOB & Debiasing) [arXiv:2512.18610]：推导在相位随机性扰动下条件期望解导致的高频振幅指数衰减定理（普洛克路斯忒斯之床），推导频域能量谱匹配与梯度对齐的结构去偏目标 $\mathcal{L}_{\text{Debiased}}$；
  - 2.7 决策论预训练与有限样本贝叶斯风险极小化 (The Simulacrum) [arXiv:2606.27711]：形式化后验期望风险与先验随机动力学族上的贝叶斯风险，证明 $\mathcal{O}(1/\sqrt{M})$ 有限样本收敛界与零样本近最优决策；
  - 2.8 反事实时序结构因果模型形式化 (Counterfactual & Interventional TSCMs, DoTime) [arXiv:2607.27263]：形式化动态 TSCM 四元组、Pearl do-演算时序硬干预算子与外生噪声溯源反事实潜在结果推导。
- **全景融合 15 篇文献至第 4、5、6、7、8、9 章**：
  - 4.1 对比矩阵加入 PaCoDi、RMISC、The Simulacrum；4.9 补充并行复数扩散与决策论 Transformer；4.10 扩充 1420 亿点真实语料库 RMISC；
  - 5.1 对比矩阵加入 T-LLM、CTRL、TS-Reasoner；5.2-5.4 详细展开时序知识蒸馏、控制论反馈残差预测与认知推理思维链对齐；
  - 6.1 对比矩阵加入 EventCast、CastFSR、TimeRLM、时序智能体综述；6.2 详细展开电商事件需求预测；6.4 展开快慢反思智能体双系统与递归语言模型精准定位；
  - 7.1 对比矩阵扩充至 33 个基准框架，涵盖 RMISC、DoTime、多模态文本敏感度审计、概率预测综述、Accuracy Law 审计与 EOB 优化偏差审计；7.3 展开文本敏感度与反事实审计；7.4 深入探讨概率分布评测体系；
  - 9 开放问题深入结合精度定律缩放边界、反事实因果推演、决策论贝叶斯最优、硬核工业机电通用大模型与快慢反思闭环智能体。
- **全量同步参考文献**：Section 10 收录全部 153 篇核验文献，同步生成 153 条 BibTeX 记录 (`survey/references.bib`) 与 README.md。

### 5. 可复现学术图表质检与排版优化 (`survey/figures/`)
- 运行 `scripts/figures/generate_figures.py` 重新生成全部 5 套图表 (PNG+SVG)；
- **视觉排版质检**：
  1. `tsfm_timeline.png`：微调时间线引线分层（y 轴交错跨度 0.25 到 0.95），精准标注 2026 最新前沿（Timer-S1, WaveMoE, LeapTS, Olivia, Chronicle, Toto 2.0, Falcon-X, FactoryNet, CITRAS-FM, The Simulacrum, MACROCAST, Zeus, RMISC, LeNEPA, Scale-Aware, EXAONE Fin, Cadence, Tabby, FlowTSFM, SOTER, QUALS, t0, SwitchPFN, TW3Cast, VersaTSA, PaCoDi, CastFSR），完全消解密集重叠；
  2. `open_weight_share.png`：精确反映 153 篇论文中 52.3% 开源权重模型、47.1% 基准/提示/综述、0.7% 闭源权重的健康生态；
  3. `taxonomy_tree.png`：融入决策论预训练、并行复数扩散、快慢反思智能体、反事实干预生成器与控制论残差学习等前沿技术子节点；
  4. `model_size_vs_date.png`：精准展示从轻量级 TTM (8M)、CITRAS-FM (7M) 到百兆级 TimesFM、Chronos，再到十亿级 Moirai-MoE (1.1B)、Sundial (1.5B)、Time-MoE (2.4B)、Toto 2.0 (2.5B) 及旗舰 Timer-S1 (8.3B) 的标度分布曲线；
  5. `papers_by_category_year.png`：更新至 153 篇文献的历年发表堆叠分布柱状图，展示 2026 年爆发式增长态势。

### 6. 工具链与自动化质量门禁
- 自动化运行 `make all`，5 大门禁（153 篇唯一 ID 校验、5 组图表生成与校验、585 处文献与图片锚点引用校验、BibTeX 生成、README.md 自动化生成）全部 100% 一次性通过。

### 7. 下一轮规划与重点
1. **多模态时序图表“看图预测”轻量化追踪**：评估端侧视觉大模型直接从时序波形折线图执行形态外推的能耗与精度界限；
2. **时序因果结构发现与反事实推演统一架构**：结合 DoTime 等因果生成基准，攻克 TSFMs 在外生干预下的泛化理论下界；
3. **具身多通道物理遥测与工业机电大模型落地追踪**：持续追踪通用工业装备与人形机器人运动学融合的时变动力学表征；
4. **TimeMixer++ 永久公开开源状态跟进**：持续监测官方仓库公司合规审查与权重发布进展。

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
