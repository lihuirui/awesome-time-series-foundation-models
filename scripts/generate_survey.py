#!/usr/bin/env python3
"""Build the complete, updated living survey (survey/SURVEY.md) with Iteration 6 expansions.

Quality criteria:
1. Deepens Chapter 8 (Key Research Groups & Labs) into comprehensive individual sections:
   - THUML (Tsinghua University / Long Mingsheng)
   - Ming Jin Group (Griffith / Monash)
   - Amazon Web Services (Chronos Team)
   - Salesforce Research (Moirai Team)
   - Google Research (TimesFM Team)
   - IBM Research & CMU (TTM & MOMENT Teams)
   - Datadog (Toto Team)
   - Multi-dimensional research groups & industry labs comparison matrix.
2. Deepens Section 2 (Mathematical Formalization) with:
   - 2.5 Accuracy Law & Window Pattern Complexity Formalization (arXiv:2510.02729)
   - 2.6 Point-wise Loss Optimization Bias (EOB) & Structural Debiasing (arXiv:2512.18610)
   - 2.7 Decision-Theoretic Pretraining & Finite-Sample Bayes Risk (The Simulacrum, arXiv:2606.27711)
   - 2.8 Counterfactual & Interventional Time Series Structural Causal Models (DoTime, arXiv:2607.27263)
3. Integrates all 15 new papers into Sections 4, 5, 6, 7, 8, 9 (153 total papers cited).
4. Generates Section 10 alphabetically from data/papers.json.
5. Updates Changelog (Iteration 6) and TODO backlog.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
SURVEY_PATH = ROOT / "survey" / "SURVEY.md"

data = json.load(open(DATA_PATH, "r", encoding="utf-8"))
papers = data["papers"]
paper_map = {p["arxiv_id"]: p for p in papers}

def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^\w\s\-—\u4e00-\u9fff]", "", s)
    s = re.sub(r"[\s—]+", "-", s)
    return s

TOC_ITEMS = [
    ("摘要", 0),
    ("1 引言", 0),
    ("2 问题定义与背景", 0),
    ("2.1 符号系统与时序预测形式化", 1),
    ("2.2 通道独立 (CI) 与通道依赖 (CD)", 1),
    ("2.3 分词与连续/离散表示机制", 1),
    ("2.4 预训练优化目标", 1),
    ("2.5 预测精度定律与窗口模式复杂度 (Accuracy Law & Pattern Complexity)", 1),
    ("2.6 逐点损失优化偏误与经验优化偏差 (Optimization Bias EOB & Debiasing)", 1),
    ("2.7 决策论预训练与有限样本贝叶斯风险极小化 (Decision-Theoretic Pretraining)", 1),
    ("2.8 反事实时序结构因果模型形式化 (Counterfactual & Interventional TSCMs)", 1),
    ("3 分类体系", 0),
    ("3.1 四维正交分类空间形式化与设计空间拓扑", 1),
    ("3.2 计算范式与网络拓扑演化 (Five Core Computing Paradigms)", 1),
    ("3.3 分词机制与连续-离散表征权衡 (Tokenization Mechanisms & Trade-Offs)", 1),
    ("3.4 通道拓扑演化：从通道独立到动态任意变量交互 (Channel Topology Evolution)", 1),
    ("3.5 时序基础模型多维技术分类对比矩阵 (Comprehensive Taxonomy Matrix)", 1),
    ("4 时序基础模型", 0),
    ("4.1 核心模型对比矩阵与关键参数", 1),
    ("4.2 离散量化语言化路线：分箱映射与交叉熵形式化", 1),
    ("4.3 连续补丁自回归路线：两阶段投影与 Huber 回归推导", 1),
    ("4.4 全频段全变量统一路线：vRoPE 与 Any-variate 跨通道注意力", 1),
    ("4.5 清华 THUML Timer 与 Sundial 系列：下一补丁自回归到连续流匹配", 1),
    ("4.6 混合专家 (MoE) 路线与动态路由：Top-k 门控、频域解耦与负载均衡", 1),
    ("4.7 动态调度、神经微分方程与误差有界压缩 (LeapTS, Cadence)", 1),
    ("4.8 编码器架构、形态基元与轻量边缘部署 (MOMENT, TTM, CITRAS-FM)", 1),
    ("4.9 连续动力学生成、无数据增强表征与无注意力前沿", 1),
    ("4.10 新兴开源预训练前沿：Tabby, Toto 2.0, Zeus, Falcon-X 与 t0", 1),
    ("5 大语言模型赋能时序", 0),
    ("5.1 大语言模型赋能时序范式矩阵与理论形式化", 1),
    ("5.2 模型重编程与轻量适配路线 (Model Reprogramming & Adapters)", 1),
    ("5.3 文本化分词与直接提示路线 (Direct Prompting & Reasoning Planners)", 1),
    ("5.4 跨模态微调与跨语义空间对齐 (Cross-Modal Fine-Tuning & Semantic Alignment)", 1),
    ("5.5 上下文学习、检索增强与零样本迁移度量 (In-Context Adaptation & Transferability)", 1),
    ("5.6 时序后训练理论与强化学习对齐 (Post-Training & Reinforcement Learning Alignment)", 1),
    ("6 多模态时序与智能体演进", 0),
    ("6.1 多模态时序与智能体系统对比矩阵", 1),
    ("6.2 文本与时序跨模态推理与扩散生成 (Text + TS Joint Reasoning & Diffusion Synthesis)", 1),
    ("6.3 视觉与时序跨模态协同 (Visual Time Series & Temporal VLMs)", 1),
    ("6.4 交互式流式时序与自进化智能体决策 (Interactive TS & Self-Evolving Agents)", 1),
    ("6.5 具身智能与工业物理多通道基础模型 (Embodied & Industrial Multi-Channel TSFMs)", 1),
    ("7 基准与评测", 0),
    ("7.1 通用时序评测矩阵与基准对比", 1),
    ("7.2 数据污染、预训练熟悉度与时序因果隔离审计", 1),
    ("7.3 证据边界与零样本审计框架", 1),
    ("7.4 概率可靠性、分位数校准与高阶依赖度量", 1),
    ("7.5 动态演化环境与多轮智能体评测", 1),
    ("7.6 视觉裁判与工作流调度 Harness", 1),
    ("8 重点课题组进展", 0),
    ("8.1 龙明盛团队（清华大学 THUML）", 1),
    ("8.2 金明团队（Ming Jin Group, Griffith / Monash）", 1),
    ("8.3 亚马逊团队（Amazon Web Services / Chronos Team）", 1),
    ("8.4 Salesforce Research（Moirai Team）", 1),
    ("8.5 谷歌团队（Google Research / TimesFM Team）", 1),
    ("8.6 IBM Research 与卡耐基梅隆大学（IBM TTM & CMU MOMENT）", 1),
    ("8.7 Datadog 团队（Toto Team）", 1),
    ("8.8 重点课题组与代表机构综合对比矩阵", 1),
    ("9 开放问题与未来方向", 0),
    ("9.1 物理定律与动力学守恒约束的时空神经物理融合", 1),
    ("9.2 极低信噪比与高频微观结构下的预测崩溃与信息论极限", 1),
    ("9.3 外生策略干预、结构因果模型与反事实可证伪性", 1),
    ("9.4 具身物理遥测、多本体机电动力学与流式毫秒级响应", 1),
    ("9.5 自主反思闭环智能体与控制论反馈稳定性边界", 1),
    ("9.6 全景开放挑战与未来破局路线矩阵", 1),
    ("10 参考文献", 0),
    ("版本变更日志 (Changelog)", 0),
    ("TODO 后备待办论文池 (TODO Backlog)", 0)
]

toc_lines = []
for title, level in TOC_ITEMS:
    indent = "  " * level
    anchor = slugify(title)
    toc_lines.append(f"{indent}- [{title}](#{anchor})")
toc_md = "\n".join(toc_lines)

# Generate References
ref_entries = []
for aid in sorted(paper_map.keys()):
    p = paper_map[aid]
    authors_str = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
    venue_str = f" ({p['venue']})" if p.get("venue") else ""
    code_str = f" [[Code]({p['code_url']})]" if p.get("code_url") else ""
    ref_entries.append(f"- **[arXiv:{aid}]** {p['title']} — {authors_str} ({p['year']}){venue_str}. [https://arxiv.org/abs/{aid}](https://arxiv.org/abs/{aid}){code_str}")
references_md = "\n".join(ref_entries)

print(f"Generated {len(ref_entries)} references.")

part1 = r"""# 时序基础模型与多模态时序智能演进综述 (A Living Survey on Time Series Foundation Models and Multimodal Temporal Intelligence)

> **版本状态：** 持续演进的活体综述 (Living Survey) · **最后更新：** 2026-09-26 (Iteration 8)
> **维护规范：** 仅收录通过 arXiv HTTPS API 严格核验的论文条目；所有事实性陈述均标注 `[arXiv:XXXX.XXXXX]` 真实引用；模型参数与语料规模仅采用论文显式声明数值。

---

## 目录 (Table of Contents)
""" + toc_md + r"""

---

## 摘要

时间序列基础模型 (Time Series Foundation Models, TSFMs) 与多模态时序智能正在深刻变革工业生产、能源调度、金融分析、气象环境、医疗健康及具身物理系统的时空数据建模范式。受自然语言处理和计算机视觉领域通用大模型成功的启发，研究界正迅速跨越传统的针对单一数据集定制训练专有模型 (Task-Specific Training) 的局限，转向基于万亿级跨领域时序点预训练具备强零样本泛化能力、上下文自适应、跨模态因果推理与自主交互决策能力的通用大模型。

本综述系统梳理了从 2022 年至 2026 年时序基础模型的核心技术路线与最新演化脉络，并在本轮迭代中重点完成核心深化与前沿扩充：
1. **开放问题与未来前沿理论全景深化（第 9 章重大深化重点）**：
   - 建立物理守恒公理与时空神经动力学融合的解析形式化，严格推导质量/动量/能量连续性方程与哈密顿保辛几何约束，剖析自注意力统计相关性与物理刚性约束的本质冲突；
   - 基于信息论互信息指数衰减律 $I \propto e^{-\lambda H}$ 与率失真理论 $R(D)$，形式化推导均方误差下极低信噪比诱发“预测崩溃 (Forecast Collapse)”退化为常数均值的临界相变机理；
   - 建立 Pearl 动态反事实结构因果模型 (Dynamic TSCM) 与外生硬干预算子 $do(\mathbf{a}^*)$，揭示纯被动观测数据预训练诱发的混淆偏差与行业集中性脆弱风险；
   - 剖析工业具身与机电高频遥测的二次方算力瓶颈，建立具备 $\mathcal{O}(1)$ 流式单步推断时间与 $\mathcal{O}(d^2)$ 恒定内存的 xLSTM 矩阵状态递推机制 (TiRex-2)；
   - 构建时序决策智能体离散时间动态闭环反馈控制系统与误差动力学方程，确立李雅普诺夫反馈稳定性判据与认知摄动界 $\epsilon_{\text{robust}}$；
   - 首创涵盖 6 大核心科学维度的**全景开放挑战与未来破局路线矩阵** (Table 9.1)。
2. **分类体系全景重构与五大计算范式数学深化（第 3 章）**：
   - 系统建立时序基础模型四维正交理论设计空间形式化 $\mathcal{S} = \langle \mathcal{A}, \mathcal{T}, \mathcal{M}, \mathcal{E} \rangle$；
   - 深入剖析从因果自回归解码器、双端编码-解码器、纯编码器掩码自编码、稀疏混合专家 (MoE) 到连续动力学/扩散生成/先验拟合的五大计算范式；
   - 推导连续补丁 vs 离散分箱量化 vs 频域小波在拓扑度量与多峰后验拟合上的数学权衡；
   - 系统推导通道拓扑从通道独立 (CI) 到变量感知旋转编码 (vRoPE Any-variate) 再到动态引导拓扑的演化路径；
   - 首次构建涵盖 12 类主流架构、跨 8 个维度的全景分类技术对比矩阵。
2. **重点课题组与代表机构前沿矩阵全面深化（第 8 章）**：建立多维度全景横向评测体系，全面系统剖析清华大学 THUML 龙明盛团队、金明团队（Ming Jin Group）、亚马逊 AWS Chronos 团队、Salesforce Research Moirai 团队、谷歌研究院 TimesFM 团队、IBM Research 与卡耐基梅隆大学 CMU (TTM & MOMENT) 以及 Datadog Toto 团队等七大核心科研力量的技术演进路线，构建全景对比矩阵。
3. **时序建模底层理论与数学形式化深化（第 2 章数学深化）**：
   - 严格推导清华大学龙明盛团队提出的**时序预测精度定律与窗口模式复杂度 (Accuracy Law & Pattern Complexity)** [arXiv:2510.02729]；
   - 严格推导金明团队揭示的**逐点损失优化偏误与经验优化偏差 (Empirical Optimization Bias, EOB)** [arXiv:2512.18610]；
   - 形式化推导 **决策论预训练与有限样本贝叶斯风险极小化 (The Simulacrum)** [arXiv:2606.27711]；
   - 建立动态**反事实时序结构因果模型形式化 (Counterfactual & Interventional TSCMs, DoTime)** [arXiv:2607.27263]。
4. **时序原生基础模型 (Native TSFMs)**：推导离散分箱交叉熵 vs 连续 Huber 回归损失；Any-variate 跨通道注意力与变量感知旋转位置编码 (vRoPE)；Sundial 连续流匹配 (CFM)；稀疏混合专家 (MoE) Top-$k$ 门控、辅助负载均衡与小波子带路由 (WaveMoE)；连续 Neural CDE 动态多视野调度 (LeapTS)；误差有界压缩 (Cadence)；并行复数扩散生成 (PaCoDi [arXiv:2602.17706])；涵盖 1420 亿点真实多变量语料库 RMISC [arXiv:2607.06504]。
5. **大语言模型赋能时序 (LLM-for-TS)**：深入分析模型重编程（Time-LLM、One Fits All）、文本化直接提示与规划协作（LLMTime、CTRL 控制论残差学习 [arXiv:2609.23257]）、时序知识蒸馏（T-LLM [arXiv:2602.01937]）、跨模态认知推理对齐（TS-Reasoner [arXiv:2510.03519]）、闭式检索对齐 (Align-RAG) 以及可验证奖励强化后训练 (PostTime RLVR)。
6. **多模态时序智能与智能体决策 (Multimodal Temporal Intelligence & Agents)**：梳理多模态因果融合与交互智能体系统；剖析电商事件知识图谱混合需求预测 (EventCast [arXiv:2602.07695])、快慢反思智能体框架 (CastFSR [arXiv:2608.03031])、递归语言模型长上下文异常定位 (TimeRLM [arXiv:2608.03391])、时序预测智能体系统综述 [arXiv:2608.23058]、TimeBraid 统一大模型与 FactoryNet 具身工业基石。
7. **评测基准与实证审计**：涵盖 GIFT-Eval、It's TIME、RMISC [arXiv:2607.06504]、反事实干预生成器 DoTime [arXiv:2607.27263]、多模态文本敏感度审计 [arXiv:2608.22321]、概率与时空预测系统综述 [arXiv:2609.13345]、版本修订审计 (VINTAGE-TS, MACROCAST) 与前瞻偏误实证审计。

本综述所有收录论文条目均经由 arXiv HTTPS API 严格核验（共 183 篇），代码链接均经由 GitHub API 官方核验，为学术界与工业界提供真实、严密、前沿的一手参考。

---

## 1 引言

时间序列预测在过去几十年中经历了三次核心范式跃迁：
- **经典统计与机器学习时代**：以 ARIMA、指数平滑（ETS）、GARCH 以及基于树模型的 LightGBM、XGBoost 为代表，依赖严格的统计假设或手工提取的时序特征；
- **深度时序模型时代**：以 RNN、LSTM、TCN 以及各类时序 Transformer 变体（如 Autoformer、Informer、PatchTST）为代表 [arXiv:2202.07125]，尽管预测精度显著提升，但仍受限于“在目标数据集划分训练集/验证集/测试集”的单一封闭场景假设，面临分布偏移严重、冷启动代价高昂等痛点；
- **时序基础模型与多模态通用智能时代 (2023 - 2026)**：通过汇聚数十亿至数万亿级跨领域时间序列点（包含真实物理传感与合成数据），训练具备广泛通用归纳偏置的模型，直接在未见场景下实现开箱即用的零样本预测与迁移 [arXiv:2403.14735], [arXiv:2310.10196]。

伴随这一跃迁，研究界逐步分化出两条互补的发展主线：
1. **时序原生基础模型**：基于 Transformer、MLP-Mixer、状态空间模型 (SSM)、先验数据网络 (PFN)、复数连续扩散 (PaCoDi [arXiv:2602.17706]) 或流匹配框架，设计专为时间序列设计的连续或离散分词机制，探索时序领域的标度律与精度定律 (Accuracy Law [arXiv:2510.02729])；
2. **跨模态与大语言模型赋能**：利用预训练大语言模型 (LLM) 和多模态大模型 (VLM) 蕴含的通用时序推理、模式识别与世界知识，通过参数重编程、跨模态适配器、闭式检索对齐、认知推理对齐 (TS-Reasoner [arXiv:2510.03519])、控制论残差学习 (CTRL [arXiv:2609.23257]) 或快慢反思智能体 (CastFSR [arXiv:2608.03031]) 的方式解决时序下游任务 [arXiv:2402.01801], [arXiv:2608.23058]。

---

## 2 问题定义与背景

### 2.1 符号系统与时序预测形式化

令一个多变量时间序列 (Multivariate Time Series) 历史观测表示为：
$$\mathbf{X}_{1:T} = [\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T]^\top \in \mathbb{R}^{T \times C}$$
其中 $T$ 为历史回看窗口长度 (Lookback Context Window)，$C$ 为变量通道数 (Channels / Variates)。预测任务的目标是在给定历史上下文 $\mathbf{X}_{1:T}$ 以及可选的外生上下文 $\mathbf{Z}$（如文本描述、节假日元数据、时序图像）的条件下，预测未来 $H$ 步的时序轨迹：
$$\hat{\mathbf{X}}_{T+1:T+H} = [\mathbf{x}_{T+1}, \dots, \mathbf{x}_{T+H}]^\top \in \mathbb{R}^{H \times C}$$

对于点预测任务，模型学习条件期望映射：
$$\hat{\mathbf{X}}_{T+1:T+H} = f_\theta(\mathbf{X}_{1:T}, \mathbf{Z})$$
对于概率预测任务，模型直接建模未来轨迹的条件概率分布：
$$p_\theta(\mathbf{X}_{T+1:T+H} \mid \mathbf{X}_{1:T}, \mathbf{Z})$$

### 2.2 通道独立 (CI) 与通道依赖 (CD)

在多变量基础模型设计中，通道建模范式构成核心分歧：
- **通道独立 (Channel Independence, CI)**：将多变量时序分解为 $C$ 个独立的单变量序列分别输入模型，共享网络参数。该范式可彻底避免跨通道维度不一致、变量重命名和虚假相关性问题，被 TimesFM [arXiv:2310.10688]、Timer [arXiv:2402.02368] 和 Chronos [arXiv:2403.07815] 广泛采用。
- **通道依赖 (Channel Dependence, CD) 与任意变量统一 (Any-variate)**：显式通过跨通道注意力机制（如 Moirai [arXiv:2402.02592] 的 Any-variate Attention）、外生变量跨注意力机制（如 TimeXer [arXiv:2402.19072]）或潜空间原型注意力（如 Falcon-X [arXiv:2605.27286]）建模通道间动态耦合关系。

### 2.3 分词与连续/离散表示机制

针对连续数值的有效 Token 转化是基础模型能够借鉴自注意力机制的前提：

1. **补丁分词 (Patch Tokenization)**：
   将长度为 $T$ 的单通道序列以步长 $S$ 和补丁长度 $P$ 切分为 $N = \lfloor (T - P)/S \rfloor + 1$ 个子段：
   $$\mathbf{p}_i = \mathbf{x}_{(i-1)S+1 : (i-1)S+P} \in \mathbb{R}^P$$
   经线性投射层和位置嵌入转化为连续隐藏向量：
   $$\mathbf{e}_i = \mathbf{W}_p \mathbf{p}_i + \mathbf{b}_p + \mathbf{e}_{\text{pos}, i} \in \mathbb{R}^D$$
   该机制不仅将注意力计算复杂度由 $\mathcal{O}(T^2)$ 降低至 $\mathcal{O}((T/P)^2)$，还显著增强了局部时序形状模式的捕获能力。

2. **离散分箱量化 (Quantization Tokenization)**：
   Chronos [arXiv:2403.07815] 提出通过均值绝对值缩放归一化 $\tilde{\mathbf{x}} = \mathbf{x} / (\frac{1}{T}\sum |x_t|)$，随后利用非均匀或均匀分箱将连续数值映射为固定词表大小 $B$（如 $B=4096$）的离散类别 Token：
   $$c_t = \text{clip}\left(\left\lfloor \frac{\tilde{x}_t - z_{\min}}{z_{\max} - z_{\min}} \cdot B \right\rfloor, 0, B-1\right)$$
   此举使语言模型原生交叉熵损失可无缝迁移至时序预测。

3. **滞后特征 (Lag Features)**：
   Lag-Llama [arXiv:2310.08278] 沿用经典时序思路，基于预设的日、周、月等周期性间隔构造滞后特征向量，结合多层感知机映射为连续表示。

4. **形态基元与尺度自适应 (Shapelet & Multi-Patch Tokens)**：
   UniShape [arXiv:2601.06429] 突破固定切片限制，提取跨通道多尺度形态基元 (Shapelets)；Scale-Aware Pretraining [arXiv:2608.20005] 引入多尺度 Patch Token 对齐与混合掩码机制；VersaTSA [arXiv:2609.22836] 引入时间感知补丁 (Time-Aware Patch) 处理不规则非均匀采样。

### 2.4 预训练优化目标

1. **下一 Token / 下一 Patch 自回归目标 (Next-Token / Next-Patch Autoregression)**：
   $$\mathcal{L}_{\text{AR}}(\theta) = - \sum_{i=1}^N \log p_\theta(\mathbf{p}_i \mid \mathbf{p}_{<i})$$
   TimesFM [arXiv:2310.10688]、Timer [arXiv:2402.02368] 和 Chronos [arXiv:2403.07815] 均以此为基础目标。

2. **连续流匹配生成目标 (Continuous Flow Matching)**：
   Sundial [arXiv:2502.00816] 提出 TimeFlow 损失，克服离散量化信息损失与高斯先验受限问题。令 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 为先验高斯噪声，$\mathbf{x}_1$ 为真实目标未来补丁，定义线性插值路径 $\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1$，流模型速度场预测网络 $v_\theta$ 的优化目标为：
   $$\mathcal{L}_{\text{FM}}(\theta) = \mathbb{E}_{t \in [0, 1], \mathbf{x}_0, \mathbf{x}_1} \left\| v_\theta(\mathbf{x}_t, t, \mathbf{c}) - (\mathbf{x}_1 - \mathbf{x}_0) \right\|^2$$
   其中 $\mathbf{c}$ 为历史上下文表示。

3. **免数据增强隐状态自监督目标 (No-Augmentation Next-Latent Prediction)**：
   LeNEPA [arXiv:2607.00958] 摒弃了传统对比学习依赖经验性时间扭曲和抖动等容易破坏因果物理规律的数据增强操作，转而在潜空间直接预测未来隐状态 $\mathbf{z}_{i+1}$：
   $$\mathcal{L}_{\text{Latent}}(\theta) = - \cos\left( g_\theta(\mathbf{z}_{\le i}), \text{sg}(\mathbf{z}_{i+1}) \right)$$
   其中 $\text{sg}(\cdot)$ 为停止梯度算子，从源头上保障了时序物理拓扑的自监督无损建模。

### 2.5 预测精度定律与窗口模式复杂度 (Accuracy Law & Pattern Complexity)

在自然语言处理与计算机视觉中，神经标度律 (Scaling Laws) 主要刻画模型参数量 $N$ 与计算量 $C$ 随损失下降的幂律关系。然而在时间序列预测中，预测性能不仅取决于参数规模，更受制于输入输出窗口结构与时间序列内在的动力学复杂度。

清华大学龙明盛团队在 [arXiv:2510.02729] 中首次建立了**深度时序预测器的精度定律 (Accuracy Law for Deep Time Series Forecasters)**。该理论指出，经验预测误差 $\mathcal{E}$ 与历史回看窗口长度 $L$、预测视野 $H$ 以及内在的窗口模式复杂度 (Window Pattern Complexity) $\mathcal{C}_P$ 之间存在严格的数学函数关系。

#### 2.5.1 窗口模式复杂度形式化定义

给定单变量时序片段 $\mathbf{x}_{1:W} \in \mathbb{R}^W$（$W$ 可为历史窗口 $L$ 或未来视野 $H$），其窗口模式复杂度 $\mathcal{C}_P(\mathbf{x}_{1:W})$ 形式化定义为谱熵 (Spectral Entropy) 与局部曲率变差 (Curvature Variation) 的加权几何测度：
$$\mathcal{C}_P(\mathbf{x}_{1:W}) = \mathcal{H}_{\text{spectral}}(\mathbf{x}_{1:W}) + \lambda_c \cdot \frac{1}{W} \sum_{t=2}^{W-1} \left| \nabla^2 x_t \right|$$
其中 $\nabla^2 x_t = x_{t+1} - 2x_t + x_{t-1}$ 为二阶离散差分算子，反映局部震荡与拐点频率；$\mathcal{H}_{\text{spectral}}$ 为功率谱密度的归一化香农熵：
$$\mathcal{H}_{\text{spectral}}(\mathbf{x}_{1:W}) = - \sum_{k=1}^{\lfloor W/2 \rfloor} p_k \log_2 p_k, \quad p_k = \frac{|\mathcal{F}(\mathbf{x})_k|^2}{\sum_{j} |\mathcal{F}(\mathbf{x})_j|^2}$$
当序列退化为单一正弦波或线性趋势时，$\mathcal{H}_{\text{spectral}} \to 0$ 且曲率极低，$\mathcal{C}_P \to 0$；当序列呈现高斯白噪声或多频混合湍流时，$\mathcal{C}_P$ 达到理论极大值。

#### 2.5.2 精度定律数学形式与三阶段演化区间

基于海量跨领域实证，预测误差 $\mathcal{E}(L, H)$ 服从如下解析幂律曲面：
$$\mathcal{E}(L, H) = \alpha \cdot \left(\frac{H}{L}\right)^\beta \cdot \exp\left( \gamma \cdot \mathcal{C}_P(H) \right) + \mathcal{E}_\infty$$
其中 $\alpha, \beta, \gamma > 0$ 为特定领域的固有常数，$\beta \in [0.35, 0.55]$ 为回看缩放指数，$\mathcal{E}_\infty$ 为不可约简的贝叶斯固有噪声下界。该定律揭示了时序预测的三大临界演化区间：
1. **信息匮乏区间 (Starvation Regime, $L \ll H$)**：由于历史观测无法覆盖系统周期或因果驱动特征，模型产生严重欠拟合，误差随 $L$ 增加呈急剧指数级下降；
2. **法定缩放区间 (Lawful Scaling Regime, $L \in [2H, 5H]$)**：预测误差严格遵循以 $\beta$ 为幂次的衰减律，此时增加上下文长度能以最经济的边际增益压降误差；
3. **稀释饱和区间 (Dilution & Saturation Regime, $L \gg 5H$)**：随着远期非平稳历史数据不断涌入，因果注意力权重发生稀释与弥散，环境漂移引入过多外源方差，预测误差曲线平展并收敛至 $\mathcal{E}_\infty$。

精度定律为时序基础模型的上下文窗口设定、补丁划分比例与分词设计提供了首个可计算的数学准则。

### 2.6 逐点损失优化偏误与经验优化偏差 (Optimization Bias EOB & Debiasing)

为什么当前诸多经过庞大参数预训练的时序大模型，在面对高频震荡和剧烈拐点时，往往倾向于预测出严重平滑滤波化、振幅衰减且存在显著相位滞后的平庸轨迹？

金明团队与温青山团队在 [arXiv:2512.18610] 中深入剖析了这一现象，并提出了关于逐点损失函数内在缺陷的突破性理论：**经验优化偏误 (Empirical Optimization Bias, EOB)**，揭示了将均方误差 (MSE) 和平均绝对误差 (MAE) 等逐点损失直接套用于时间序列所造成的“普洛克路斯忒斯之床 (The Procrustean Bed)”效应。

#### 2.6.1 逐点优化偏误 (EOB) 的数学推导

令真实未来时序向量为 $\mathbf{y} \in \mathbb{R}^H$，预测值向量为 $\hat{\mathbf{y}} = f_\theta(\mathbf{x}) \in \mathbb{R}^H$。标准逐点均方误差损失定义为：
$$\mathcal{L}_{\text{MSE}}(\theta) = \mathbb{E}_{(\mathbf{x}, \mathbf{y}) \sim \mathcal{D}} \left[ \frac{1}{H} \sum_{t=1}^H (y_t - \hat{y}_t)^2 \right]$$
在时间序列现实采样中，不可避免地存在时序相位抖动与未观测外生随机冲击，即真实数据分布满足 $y_t = s(t - \tau) + \epsilon_t$，其中 $\tau \sim \mathcal{N}(0, \sigma_\tau^2)$ 为未观测的微观相位随机偏移。

在逐点 MSE 最小化条件下，神经网络的全局最优解在数学上退化为条件期望投影：
$$f^*(\mathbf{x})_t = \mathbb{E}_{\mathbf{y} \mid \mathbf{x}}[y_t] = \int y_t p(y_t \mid \mathbf{x}) dy_t$$
**定理（频域振幅指数衰减定理）**：
若底层动力学波形为角频率为 $\omega$ 的信号 $s(t) = A \cos(\omega t)$，受微小高斯相位抖动 $\tau \sim \mathcal{N}(0, \sigma_\tau^2)$ 扰动，则条件期望最优预测器所输出的波形满足：
$$f^*(\mathbf{x})_t = \mathbb{E}_\tau [A \cos(\omega(t - \tau))] = A \cos(\omega t) \cdot \exp\left( - \frac{1}{2} \omega^2 \sigma_\tau^2 \right)$$
**推论**：随着信号频率 $\omega$ 的升高，其输出振幅遭受以 $\exp(-\frac{1}{2}\omega^2\sigma_\tau^2)$ 形式的指数级剧烈惩罚。对于高频细节与突发冲击，条件期望解的振幅被强行压缩至趋近于零！这从数学本质上证明了：**逐点回归损失本质上在惩罚一切高频尖峰与真实波动，强迫神经网络为了迎合平均误差而输出平直、滞后的均值轨迹**。

#### 2.6.2 结构性去偏损失 (Structural Debiasing Objective)

为了打破这一“普洛克路斯忒斯之床”，文献 [arXiv:2512.18610] 提出了结构性去偏目标，将时域逐点保真度与频域功率谱密度及切线方向梯度进行解耦联合优化：
$$\mathcal{L}_{\text{Debiased}}(\theta) = \mathcal{L}_{\text{MSE}}(\hat{\mathbf{y}}, \mathbf{y}) + \lambda_{\text{spec}} \cdot \left\| |\mathcal{F}(\hat{\mathbf{y}})| - |\mathcal{F}(\mathbf{y})| \right\|_1 + \lambda_{\text{grad}} \cdot \frac{1}{H-1}\sum_{t=1}^{H-1} \left( \nabla \hat{y}_t - \nabla y_t \right)^2$$
其中第二项强制约束预测轨迹保留真实的频域能量谱幅值，消除指数高频阻尼；第三项约束一阶差分速度场对齐，从源头上消除了相位延迟滞后，使模型在保留高精度点预测的同时，完全复原真实物理波形的尖锐峰值与真实动力学形态。

### 2.7 决策论预训练与有限样本贝叶斯风险极小化 (Decision-Theoretic Pretraining)

现有时序大模型的预训练普遍以通用自回归负对数似然 (NLL) 或重构误差为优化目标，假定预训练阶段只需学习通用的无条件或条件数据分布即可。然而，在现实工业运营、库存控制与高频金融等高价值场景中，下游用户并不直接消费概率密度函数本身，而是根据特定非对称效用/损失函数执行决策行动。

Montero-Manso 与 Scharth 在 [arXiv:2606.27711] 中建立了名为 **The Simulacrum（幻象）** 的决策论预训练 (Decision-Theoretic Pretraining) 理论框架。该理论彻底颠覆了“先拟合通用生成模型、再下游进行概率积分决策”的两阶段传统范式，提出在预训练阶段直接逼近**有限样本贝叶斯行动者 (Bayes Decision Actor)**。

#### 2.7.1 统计决策论与贝叶斯最优行动形式化

令下游任务的行动空间为 $\mathcal{A}$，真实未来时序为 $\mathbf{y} \in \mathcal{Y}$，定义任务特定的效用/损失函数为 $\ell(\mathbf{y}, \mathbf{a}): \mathcal{Y} \times \mathcal{A} \to \mathbb{R}$。在给定历史观测 $\mathbf{x}$ 的条件下，贝叶斯最优行动 $\mathbf{a}^*(\mathbf{x})$ 满足后验期望风险最小化：
$$\mathbf{a}^*(\mathbf{x}) = \arg\min_{\mathbf{a} \in \mathcal{A}} \mathbb{E}_{\mathbf{y} \sim p(\mathbf{y} \mid \mathbf{x})} \left[ \ell(\mathbf{y}, \mathbf{a}) \right]$$
在传统方法中，当损失函数是非对称（如报童库存问题中的缺货惩罚显著高于积压成本）或非凸风险测度（如 CVaR 条件在险价值）时，基于蒙特卡洛采样近似 $\mathbf{a}^*$ 计算昂贵且极易发散。

#### 2.7.2 先验过程分布族上的有限样本贝叶斯风险

The Simulacrum [arXiv:2606.27711] 提出构建覆盖广泛随机过程的先验生成分布元集 $\mathcal{P} = \{P_\alpha \mid \alpha \in \Omega\}$（包含广义高斯过程、切换状态空间动力学与跳跃扩散过程）。基础模型参数化为一个直接将历史上下文映射到决策行动的映射网络 $f_\theta: \mathbf{x} \mapsto \mathbf{a}$。预训练目标定义为全先验空间上的有限样本贝叶斯风险期望：
$$\min_\theta \mathcal{R}_{\text{Bayes}}(\theta) = \mathbb{E}_{P \sim \mathcal{P}} \; \mathbb{E}_{(\mathbf{x}, \mathbf{y}) \sim P} \left[ \ell\left(\mathbf{y}, f_\theta(\mathbf{x})\right) \right]$$
**定理（有限样本近最优泛化界）**：
文献证明，当先验分布族 $\mathcal{P}$ 具备足够的动力学多样性，且基础模型网络具备充足表征容量时，利用随机生成的 $M$ 条先验轨迹进行端到端极小化优化，经验决策器 $f_\theta$ 对真实后验贝叶斯最优解 $\mathbf{a}^*$ 的多余风险 (Excess Risk) 满足收敛界：
$$\mathcal{R}(f_\theta) - \mathcal{R}(\mathbf{a}^*) \le \mathcal{O}\left( \frac{1}{\sqrt{M}} \right) + \text{AppxErr}(\Theta)$$
该机制将计算代价昂贵的贝叶斯后验推断与复杂的非对称决策数值优化过程完全“离线摊销 (Offline Amortized)”在预训练参数中，使模型在推理阶段仅需一次前向传播即可输出严格契合任意复杂下游业务损失的近最优决策。

### 2.8 反事实时序结构因果模型形式化 (Counterfactual & Interventional TSCMs)

传统的时序基础模型本质上是**关联性观察模型 (Observational Forecasters)**，其建模的条件分布为 $P(\mathbf{x}_{T+1:T+H} \mid \mathbf{x}_{1:T})$。这一范式仅能回答 Pearl 因果阶梯第一层（关联：如果现有趋势延续，未来会怎样？），但在真实的运筹决策、临床用药干预与宏观调控中，决策者必须回答第二层（干预：如果我们在时间步 $t_0$ 强制上调价格或切断供电线路，未来轨迹会如何变化？）乃至第三层（反事实：如果过去没有采取该项操作，现在的设备是否仍会发生故障？）。

Thumm 等人在 [arXiv:2607.27263] 中构建了首个面向动态时间序列的系统级反事实基准生成器 **DoTime**，形式化定义了动态时序结构因果模型 (Time-Series Structural Causal Models, TSCMs)。

#### 2.8.1 动态时序结构因果模型形式化定义

一个包含 $C$ 个时变变量的动态 TSCM 定义为一个四元组 $\mathcal{M} = \langle \mathbf{V}, \mathbf{U}, \mathcal{F}, P(\mathbf{U}) \rangle$：
- **内生时变变量集 $\mathbf{V}$**：包含所有系统在时间步 $t \in \{1,\dots,T\}$ 的可观测多变量状态 $\mathbf{x}_t = (x_1^t, x_2^t, \dots, x_C^t)^\top$；
- **外生背景噪声集 $\mathbf{U}$**：包含相互独立的连续随机驱动过程 $\mathbf{u}_t = (u_1^t, \dots, u_C^t)^\top \sim P(\mathbf{U})$；
- **结构方程因果机制集 $\mathcal{F}$**：由满足时间不可逆性（因果箭头只能由过去指向未来或同一时刻无环图）的结构方程构成：
  $$x_i^t = f_i\left( \mathbf{pa}_i^t, u_i^t \right), \quad i \in \{1,\dots,C\}$$
  其中因果父节点集 $\mathbf{pa}_i^t \subseteq \{x_j^{t-\tau} \mid \tau > 0, 1 \le j \le C\} \cup \{x_k^t \mid k \in \text{Anc}(i)\}$ 严格排除了未来信息的反馈环。

#### 2.8.2 Pearl do-演算干预与反事实潜在结果推断

1. **时序干预算子 (Intervention Operator)**：
   在时间步 $t_0$ 对特定变量子集实施硬干预 $do(x_k^{t_0:t_0+k} = \mathbf{x}^*)$，其数学本质是切断 $x_k$ 与其原始因果父节点 $\mathbf{pa}_k$ 之间的结构方程，代之以常数强制赋值：
   $$f_k^t(\mathbf{pa}_k^t, u_k^t) \leftarrow x_k^{*, t}, \quad \forall t \in [t_0, t_0+k]$$
   干预后产生新的后干预动态分布 $P_{\mathcal{M}; do(x_k = \mathbf{x}^*)}(\mathbf{x}_{t_0+1:T})$；
2. **反事实轨迹估计 (Counterfactual Potential Trajectory)**：
   给定观测到的具体历史事实轨迹 $\mathbf{X}_{1:T} = \mathbf{x}_{\text{fact}}$，评估反事实假设“如果过去在 $t_0$ 步将变量 $x_k$ 替换为 $x_k^*$，系统后续的发展轨迹 $\mathbf{Y}_{t_0+1:T}^{(\mathbf{x}^*)}$ 为何？”满足 Pearl 反事实三步推导：
   - **外生噪声溯源 (Abduction)**：基于历史观测事实 $\mathbf{x}_{\text{fact}}$ 反解推断特定的外生噪声实现值 $\mathbf{u} = \mathcal{F}^{-1}(\mathbf{x}_{\text{fact}})$；
   - **机制修正 (Action)**：在因果图上应用 $do(x_k = x_k^*)$ 算子修改结构方程形成修改后的模型 $\mathcal{M}_{do}$；
   - **前向推演 (Prediction)**：将溯源得到的外生噪声 $\mathbf{u}$ 重新输入到修正后的因果机制中，确定性前向积分求解潜在结果轨迹：
     $$\mathbf{Y}_{t_0+1:T}^{(\mathbf{x}^*)} = \mathcal{F}_{\mathcal{M}_{do}}(\mathbf{u})$$

DoTime [arXiv:2607.27263] 通过数学严格受控的合成动力系统（如具有非线性耦合的摆动方程、捕食者-猎物 Lotka-Volterra 微分方程网格），建立了首个能够精确比对反事实真实轨迹的通用评测基准，实证暴露出纯粹基于自回归似然的 TSFMs 在面对外生干预时产生灾难性因果虚假相关外推的严峻缺陷。

---

## 3 分类体系

时序基础模型与多模态时序智能体系正经历从单一离散切片向高维跨模态时空连续表征的深刻裂变。为了厘清层出不穷的新模型、新架构与新任务界限，本章建立四维正交分类理论空间，剖析五大核心计算范式，形式化推导分词与通道拓扑权衡，并给出全景横向技术矩阵。

### 3.1 四维正交分类空间形式化与设计空间拓扑

时序基础模型的设计空间可严格形式化为一个四维正交理论空间 $\mathcal{S} = \langle \mathcal{A}, \mathcal{T}, \mathcal{M}, \mathcal{E} \rangle$：

$$\mathcal{S} = \mathcal{A} \times \mathcal{T} \times \mathcal{M} \times \mathcal{E}$$

![Taxonomy Tree](figures/taxonomy_tree.png)

1. **计算架构范式空间 ($\mathcal{A}$ - Architecture Paradigm)**：
   决定模型内部的信息流动与因果约束机制，涵盖五大经典与前沿拓扑：
   - 因果解码器 (Causal Decoder-Only)
   - 双端编码-解码器 (Encoder-Decoder)
   - 纯双向编码器掩码自编码 (Encoder-Only Masked Autoencoding)
   - 稀疏混合专家与频域路由 (Sparse MoE & Spectral Routing)
   - 连续动力学、扩散流与先验拟合 (Continuous Dynamics, Diffusion, Flow & PFN)
2. **数值分词与表征空间 ($\mathcal{T}$ - Tokenization & Representation Scheme)**：
   决定连续时间物理波形如何被离散化或投影至潜空间张量，包含连续补丁 (Continuous Patching)、离散分箱量化 (Discrete Quantized Bins)、逐点与滞后特征 (Point/Lag)、频域复数小波分解 (Complex Spectral / Wavelet)、形态感知基元 (Shapelet Primitives)、自适应动态跨度 (Adaptive Horizon Jump) 以及频率条件归一化补丁 (Frequency-Conditioned Patch [arXiv:2609.20535])。
3. **跨模态与交互协同空间 ($\mathcal{M}$ - Multimodal & Agentic Interaction Depth)**：
   刻画模型处理多源异构信息与动态交互的自主性阶梯，由纯时序无外源传感 (TS-only)、跨模态参数重编程 (Reprogramming)、隐式因果推理对齐 (Cognitive Reasoning Alignment)、图文联合扩散生成 (Cross-Modal Diffusion Synthesis)、交互式自进化智能体闭环 (Interactive Self-Evolving Agents) 递进至具身工业多通道物理遥测 (Embodied Telemetry)。
4. **评测审计与安全保障空间 ($\mathcal{E}$ - Evaluation & Quality Assurance)**：
   构建全生命周期可信泛化基石，涵盖零样本泛化测试、精度定律与神经标度律验证 [arXiv:2510.02729]、逐点优化偏误 (EOB) 频域结构去偏审计 [arXiv:2512.18610]、反事实干预与 Pearl do-演算审计 [arXiv:2607.27263]、版本修订一致性审计 (MACROCAST [arXiv:2606.28670], VINTAGE-TS [arXiv:2609.28576])、文本敏感度与虚假相关性消融 [arXiv:2608.22321]、预测崩溃相变预警 [arXiv:2608.14106] 以及真实工业 ROI 损益平衡分析 [arXiv:2607.04919]。

### 3.2 计算范式与网络拓扑演化 (Five Core Computing Paradigms)

从 2022 年到 2026 年，时序基础模型的底层骨干网络经历了显著的结构分化与拓扑重组，形成了五大各具优势的计算范式：

#### 3.2.1 因果解码器范式 (Decoder-Only Autoregressive Paradigm)
- **核心机制**：通过下三角因果注意力掩码 (Causal Mask) 确保序列推断的时序单向不可逆性：
  $$\mathbf{M}_{i, j} = \begin{cases} 0 & \text{if } j \le i \\ -\infty & \text{otherwise} \end{cases}$$
  模型在自回归滚动的过程中保持 KV-Cache，具备极高的高吞吐生成效率与理论一致性。
- **代表模型**：Google TimesFM [arXiv:2310.10688]、清华 Timer [arXiv:2402.02368]、Amazon Chronos [arXiv:2403.07815]、Datadog Toto 2.0 [arXiv:2605.20119]、Tabby [arXiv:2609.13956]、Cadence [arXiv:2609.06008]、$t_0$ [arXiv:2609.24559]。
- **设计权衡**：单向自回归对时间物理箭头的因果建模最为自然，但在处理双向上下文插补、长程掩码重构或非因果关联挖掘时存在天然的信息吸收盲区。

#### 3.2.2 双端编码-解码器范式 (Encoder-Decoder Paradigm)
- **核心机制**：编码器利用全双向自注意力 (Full Bidirectional Attention) 深度消化历史上下文 $\mathbf{X}_{1:T}$，解码器通过交叉注意力 (Cross-Attention) 逐步外推未来视野：
  $$\mathbf{H}_{\text{enc}} = \text{Encoder}(\mathbf{X}_{1:T}), \quad \hat{\mathbf{Y}} = \text{Decoder}(\mathbf{Q}_{\text{target}}, \mathbf{H}_{\text{enc}})$$
- **代表模型**：Salesforce Moirai [arXiv:2402.02592]、Moirai 2.0 [arXiv:2511.11698]、Harvard UniTS [arXiv:2403.00131]、IBM TTM [arXiv:2401.03955]、TimeMixer [arXiv:2405.14616]、QUALS [arXiv:2609.20156]。
- **设计权衡**：双向编码使历史特征抽取更为充分，但在自回归长步生成时需要维护编码-解码两套状态，计算开销与显存复杂度显著高于纯解码器。

#### 3.2.3 纯编码器掩码自编码范式 (Encoder-Only Masked Autoencoding)
- **核心机制**：放弃生成式自回归，采用掩码自编码 (MAE) 目标，在非对称掩码比例（如 50% - 75%）下重构随机丢弃的时序补丁：
  $$\mathcal{L}_{\text{MAE}}(\theta) = \frac{1}{|\mathcal{M}|} \sum_{i \in \mathcal{M}} \|\mathbf{p}_i - f_\theta(\mathbf{p}_{\setminus \mathcal{M}})\|_2^2$$
- **代表模型**：CMU MOMENT [arXiv:2402.03885]、清华 TimesBERT [arXiv:2502.21245]、UniShape [arXiv:2601.06429]、Zeus [arXiv:2607.01918]、工业过程监控模型 IPM-FM [arXiv:2609.08375]。
- **设计权衡**：纯编码器学得的特征具有极高的判别力与语义凝聚度，能以单一骨干同时赋能分类、异常检测、插补与预测；但长视野点预测需外挂回归头，概率外推能力相对受限。

#### 3.2.4 稀疏混合专家与频域路由范式 (Sparse MoE & Spectral Routing)
- **核心机制**：引入条件计算，将 FFN 模块解耦为 $E$ 个并行子专家网络，门控路由器依据输入时序的功率谱密度 (PSD) 或动态残差自适应激活 Top-$k$ 专家：
  $$\mathbf{y} = \sum_{e \in \text{TopK}(\mathbf{s}, k)} g_e(\mathbf{h}) F_e(\mathbf{h})$$
- **代表模型**：Time-MoE (2.4B) [arXiv:2409.16040]、Moirai-MoE (1.1B) [arXiv:2410.10469]、Timer-S1 (8.3B) [arXiv:2603.04791]、WaveMoE [arXiv:2604.10544]、SOTER [arXiv:2609.16804]、TW3Cast [arXiv:2609.28506]。
- **设计权衡**：在保持推理 FLOPs 几乎恒定的前提下将模型参数容量扩张 5-10 倍，能够针对高频脉冲与低频趋势实现分工专业化；但专家路由极易发生表征塌缩与负载失衡，对辅助损失设计敏感。

#### 3.2.5 连续动力学、扩散生成与先验拟合范式 (Continuous Dynamics, Diffusion, Flow & PFN)
- **核心机制**：跳出经典离散注意力框架，利用常微分/随机微分方程 (ODE/SDE)、连续流匹配 (CFM)、逆向扩散去噪或先验数据 Transformer (PFN) 拟合生成轨迹：
  - 连续流匹配 (Sundial [arXiv:2502.00816])：$\frac{d\mathbf{x}_t}{dt} = v_\theta(\mathbf{x}_t, t, \mathbf{c})$；
  - 复数频域并行扩散 (PaCoDi [arXiv:2602.17706])：在复数谱平面 $\mathbb{C}^{F \times K}$ 单步逆扩散；
  - 状态感知动态引导扩散 (DynG-Diff [arXiv:2609.02068])：引入隐状态时变引导；
  - 生成式停机预测与情景仿真 (OutageDiT [arXiv:2609.01896])：基于 Diffusion Transformer 架构进行工业突发断电仿真；
  - 扩散终端步去噪反思 (When Denoising Hurts [arXiv:2608.14067])：揭示逆扩散终端步累积漂移并给出提前停止准则；
  - 先验数据拟合 (TabPFN-v2 [arXiv:2501.02945], TabPFN-TS [arXiv:2608.20024], TSPFN [arXiv:2608.31013], SwitchPFN [arXiv:2609.29814])：在海量合成动力学先验上离线拟合有限样本贝叶斯预测分布。
- **设计权衡**：能够完美生成高阶矩一致的复杂多峰物理轨迹，杜绝均方误差导致的平滑滤波；但部分扩散模型存在采样延迟瓶颈，流匹配与先验拟合对先验分布的多样性有着严苛要求。

### 3.3 分词机制与连续-离散表征权衡 (Tokenization Mechanisms & Trade-Offs)

如何将物理连续的时间序列投影为深度神经网络易于消化的 Token 序列，决定了模型的度量拓扑与损失空间：

#### 3.3.1 连续数值补丁化 (Continuous Patching)
将长度为 $P$ 的连续时序切片经线性映射变换为高维隐藏向量：
$$\mathbf{e}_i = \mathbf{W}_p \mathbf{p}_i + \mathbf{b}_p \in \mathbb{R}^D, \quad \mathbf{p}_i \in \mathbb{R}^P$$
- **优势**：严格保留物理信号的欧氏度量性质与浮点精度，计算复杂度降低 $P$ 倍，计算吞吐极高；
- **局限**：在标准 MSE 损失优化下，受经验优化偏差 (EOB [arXiv:2512.18610]) 约束，易输出平滑均值，削弱局部突变。

#### 3.3.2 离散分箱量化 (Discrete Quantized Bins)
利用均值绝对值缩放将数值映射至固定词表大小 $B$（如 $B=4096$）的离散整数集合：
$$c_t = \text{clip}\left(\left\lfloor \frac{\tilde{x}_t - z_{\min}}{\Delta z} \right\rfloor, 0, B-1\right)$$
- **优势**：使自回归交叉熵损失能够无缝迁移，天然支持非对称、多峰概率分布的柔性拟合，对极端异常脉冲具有天然的鲁棒截断；
- **局限**：**损失了数值度量有序性 (Loss of Metric Ordinality)**——在分类损失视角下，$|c - c'|=1$ 与 $|c - c'|=1000$ 遭受无差别的对数似然惩罚；且词表扩大带来 Softmax 计算与显存开销。

#### 3.3.3 频域复数小波分解 (Complex Spectral & Wavelet Decomposition)
将时序投射至正交频域或小波子空间：
$$\mathbf{X}(f) = \sum_{t} x_t e^{-j 2\pi f t}, \quad \text{DWT}(\mathbf{x}) = \{\mathbf{A}_J, \mathbf{D}_1, \dots, \mathbf{D}_J\}$$
- **优势**：从源头上解耦物理信号中的直流平滑趋势与高频突变噪声，彻底规避时域注意力在多周期长序列上的频域混叠；
- **代表**：PaCoDi [arXiv:2602.17706]、WaveMoE [arXiv:2604.10544]、SOTER [arXiv:2609.16804]。

#### 3.3.4 形态感知基元与自适应调度 (Shapelets & Adaptive Tokens)
UniShape [arXiv:2601.06429] 提取跨变量的局部形态基元 (Shapelet)；LeapTS [arXiv:2605.10292] 设计时间跨度动态跳步 $(\tau_k, \Delta \tau_k)$；VersaTSA [arXiv:2609.22836] 引入时间感知非均匀补丁 (Time-Aware Patch)；FreqCondNorm [arXiv:2609.20535] 提出跨频段自适应归一化，支持 1Hz 到 100kHz 工业振动信号的零样本跨域迁移。

### 3.4 通道拓扑演化：从通道独立到动态任意变量交互 (Channel Topology Evolution)

多变量时序系统中变量通道 $C$ 的拓扑耦合是基础模型架构演进的核心战场：

```mermaid
flowchart LR
    A["通道独立 (CI)<br/>单变量循环 / 零跨通道干扰"] --> B["通道依赖 (CD)<br/>刚性固定通道联合注意力"]
    B --> C["任意变量统一 (Any-variate)<br/>序列展平 + vRoPE 旋转编码"]
    C --> D["动态引导与共识拓扑<br/>状态感知引导 / 共识特征选择"]
```

1. **通道独立范式 (Channel Independence, CI)**：
   将多变量张量 $\mathbf{X} \in \mathbb{R}^{T \times C}$ 分解为 $C$ 个独立的单变量序列，共享同一套模型参数进行前向推断：
   $$\hat{\mathbf{X}}_{:, c} = f_\theta(\mathbf{X}_{:, c}), \quad \forall c \in \{1,\dots,C\}$$
   **理论优势**：对变量通道的排列顺序、增减数量天然等变；彻底杜绝了训练集通道命名与测试集不匹配的虚假相关性过拟合；
   **物理缺陷**：完全无视多传感器之间的物理守恒定律与因果联动，在紧密耦合物理系统（如电网潮流、化工管网）中表现次优。
2. **固定通道依赖范式 (Fixed Channel Dependence, CD)**：
   在注意力层中同时计算时间维度与通道维度的联合交互，复杂度为 $\mathcal{O}(T^2 C^2)$。致命弱点是输入通道数 $C$ 被模型参数硬编码绑定，无法零样本迁移至不同通道数的工业场景。
3. **任意变量统一范式 (Any-variate Representation)**：
   Moirai [arXiv:2402.02592] 首创序列展平与变量感知旋转位置编码 (vRoPE)。将 $N$ 个补丁与 $C$ 个通道展平为 $N \cdot C$ 长度序列，正交旋转矩阵解耦相对时间滞后 $\Delta m$ 与通道偏移 $\Delta c$，单套权重无缝支持从 1 到任意 $C$ 个通道的即插即用。
4. **动态状态引导与共识特征拓扑 (Dynamic Guidance & Consensus Topology)**：
   进入 2026 年，通道建模突破静态展平：
   - **DynG-Diff** [arXiv:2609.02068]：提出状态感知动态引导扩散架构，依据各通道当前隐状态的动力学显著性动态调节跨通道交互权重；
   - **IPM-FM** [arXiv:2609.08375]：构建基于共识特征选择 (Consensus Feature Selection) 的工业多变量表征网络，自适应过滤与目标变量无关的噪声传感器；
   - **Falcon-X** [arXiv:2605.27286]：基于潜空间连续隐式原型解耦异构变量，杜绝物理量纲不一致引发的跨通道失真。

### 3.5 时序基础模型多维技术分类对比矩阵 (Comprehensive Taxonomy Matrix)

下表对领域内 12 种主流技术路线在核心维度上的设计权衡进行了系统解构：

| 技术路线 / 代表模型 | 架构范式 | 通道拓扑 | 分词表征机制 | 核心损失范式 | 推理采样复杂度 | 核心优势场景 | 主要局限与理论盲区 | 代表文献 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **连续自回归** (TimesFM) | Decoder-Only | 通道独立 (CI) | 连续补丁 (P=32, H=128) | Smooth L1 / Huber | 单次前向 $\mathcal{O}(1)$ | 工业高吞吐多步点预测 | 复杂多峰分布退化为均值 | [arXiv:2310.10688] |
| **离散自回归** (Chronos) | Decoder-Only | CI / 交叉注意力 | 4096 离散分箱量化 | 类别交叉熵 $\mathcal{L}_{\text{CE}}$ | 自回归多采样 $\mathcal{O}(S \cdot H)$ | 非对称分位数与尾部风险 | 丢失度量有序性，Softmax昂贵 | [arXiv:2403.07815] |
| **全变量统一** (Moirai) | Encoder-Decoder | Any-variate (vRoPE) | 多尺寸补丁投影池 | 稳健高斯/学生-t NLL | 双端交叉注意力 $\mathcal{O}(L_{\text{total}}^2)$ | 异构通道与跨频段通用预测 | 序列展平带来二次方显存压力 | [arXiv:2402.02592] |
| **双向掩码自编码** (MOMENT) | Encoder-Only | 通道独立 (CI) | 连续补丁掩码重构 | 掩码重建 MSE 损失 | 单次前向 $\mathcal{O}(1)$ | 分类、异常检测与缺失插补 | 生成式长程外推需外接回归头 | [arXiv:2402.03885] |
| **连续流匹配** (Sundial) | Decoder-Only | 通道独立 (CI) | TimeFlow 连续补丁流 | 连续流速度场匹配 $\mathcal{L}_{\text{CFM}}$ | ODE 数值积分 ($K \approx 10-20$) | 高阶动力学一致性物理轨迹 | 数值积分步长依赖超参数配置 | [arXiv:2502.00816] |
| **稀疏混合专家** (Time-MoE) | MoE 架构 | 多分辨率动态路由 | 多尺度连续补丁 | 回归损失 + 负载均衡 $\mathcal{L}_{\text{balance}}$ | Top-$k$ 稀疏门控 $\mathcal{O}(k)$ | 超大参数容量与高效推断 | 门控路由存在表征塌缩风险 | [arXiv:2409.16040] |
| **复数并行扩散** (PaCoDi) | Complex Diffusion | 频域联合拓扑 | 复数谱平面并行补丁 | 频域正交扩散去噪损失 | 单步并行去噪 $\mathcal{O}(1)$ | 超长程高保真时序轨迹生成 | 频域映射对非平稳脉冲敏感 | [arXiv:2602.17706] |
| **自适应动力学调度** (LeapTS) | 控制器 + Neural CDE | 连续流形耦合 | 动态多视野跨度补丁 | 连续受控微分方程积分 | 自适应跳步推断 | 变采样率与多尺度连续系统 | 控制器与 CDE 联合训练难度高 | [arXiv:2605.10292] |
| **先验数据拟合** (TabPFN-TS) | Prior-Data Transformer | 通道独立 / 表格拟合 | 动力学先验特征 Token | 贝叶斯后验拟合交叉熵 | 单次前向贝叶斯更新 $\mathcal{O}(1)$ | 小样本与区域热负荷零样本预测 | 严重依赖合成先验分布多样性 | [arXiv:2608.20024] |
| **动态引导扩散** (DynG-Diff) | Diffusion + Guidance | 状态感知动态引导 | 连续高斯扩散补丁 | 状态条件逆扩散评分匹配 | 引导逆扩散采样 | 强耦合多变量概率预测 | 采样迭代步长计算开销大 | [arXiv:2609.02068] |
| **自监督工业监控** (IPM-FM) | Informer 骨干 | 共识特征选择 (CFS) | 连续工业传感时变补丁 | 自监督重建 + MC-Dropout | 编码器前向 + 不确定性估计 | 复杂工业装备实时监控与异常 | 依赖工业历史测点覆盖率 | [arXiv:2609.08375] |
| **具身物理遥测** (FactoryNet) | Encoder-Decoder | 6类具身物理通道 | 具身多通道物理补丁 | 多任务动力学守恒损失 | 编码-解码前向 | 机床/机械臂/冲压跨本体迁移 | 跨物理装备量纲标定复杂 | [arXiv:2605.09081] |

---
"""

part2 = r"""## 4 时序基础模型

随着算力与语料规模的不断扩张，时序基础模型演变呈现出鲜明的标度律特征与技术路线多元化态势：

![TSFM Timeline](figures/tsfm_timeline.png)

![Model Size vs Date](figures/model_size_vs_date.png)

### 4.1 核心模型对比矩阵与关键参数

下表系统汇集了领域内代表性开源/权威基础模型的核心技术参数与实验设计（所有数值与属性均严格来自于论文声明）：

| 模型名称 | 代表机构/团队 | arXiv 引用 | 发布年份 | 最大参数量 | 预训练语料规模 | 核心架构 | 分词机制 | 模态支持 | 权重开源 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TimesFM** | Google | [arXiv:2310.10688] | 2023 | 200M | 1000亿时序点 (100B real & synthetic) | Decoder-only | Patch (输入32/输出128) | TS | 是 |
| **Lag-Llama** | Morgan Stanley / Mila | [arXiv:2310.08278] | 2023 | 2.4M | 7,922 真实数据集 (GluonTS) | Decoder-only | Lag features | TS | 是 |
| **TTM** | IBM Research | [arXiv:2401.03955] | 2024 | 8M | Monash + 合成数据 (Multi-domain) | Encoder-Decoder | Patch (Mixer 架构) | TS | 是 |
| **Timer** | 清华大学 THUML | [arXiv:2402.02368] | 2024 | 84M | UTSD 语料库 (10亿时序点) | Decoder-only | Patch (单一自回归) | TS | 是 |
| **MOMENT** | 卡耐基梅隆大学 CMU | [arXiv:2402.03885] | 2024 | 385M | Time-series Pile (1300万序列) | Encoder-only | Patch (掩码重建) | TS | 是 |
| **Moirai** | Salesforce | [arXiv:2402.02592] | 2024 | 311M | LOTSA (270亿观测值) | Encoder-Decoder | Any-variate 多尺寸 Patch | TS | 是 |
| **Chronos** | Amazon | [arXiv:2403.07815] | 2024 | 710M | TSMix + 高斯过程合成 (840亿观测) | Decoder-only | Quantized bins (4096 bins) | TS | 是 |
| **UniTS** | Harvard | [arXiv:2403.00131] | 2024 | 10M | 跨领域 38 个公开数据集 | Encoder-Decoder | 统一任务 Prompt + Patch | TS | 是 |
| **Time-MoE** | 金明团队 / 东南大学等 | [arXiv:2409.16040] | 2024 | 2.4B | Time-300B (3000亿时序点) | MoE | 多分辨率 Patch | TS | 是 |
| **Timer-XL** | 清华大学 THUML | [arXiv:2410.04803] | 2024 | 84M | UTSD-2 增强超长上下文语料 | Decoder-only | Patch (长上下文窗口) | TS | 是 |
| **Moirai-MoE** | Salesforce | [arXiv:2410.10469] | 2024 | 1.1B | LOTSA (270亿观测值) | MoE | 跨通道与频段专家稀疏激活 | TS | 是 |
| **TabPFN-v2 (TS)** | Prior Labs | [arXiv:2501.02945] | 2025 | 19M | 合成先验过程 (Synthetic Priors) | Prior-Data Transformer | 贝叶斯后验拟合 Token | TS | 是 |
| **Sundial** | 清华大学 THUML | [arXiv:2502.00816] | 2025 | 1.5B | UTSD-3 (超100亿时序点) | Decoder-only | TimeFlow 流匹配连续 Patch | TS | 是 |
| **TimesBERT** | 清华大学 THUML | [arXiv:2502.21245] | 2025 | 未报告 | UTSD 多域大规模时序语料 | Encoder-only (BERT) | Patch (掩码重建与语义分类) | TS | 是 |
| **TiRex** | NXAI | [arXiv:2505.23719] | 2025 | 35M | LOTSA 子集 | Decoder-only | 增强长短周期 In-Context Patch | TS | 是 |
| **YingLong** | 阿里 / 浙大等 | [arXiv:2506.11029] | 2025 | 300M | 未报告 | Decoder-only | 延迟思维链输出缩放 | TS | 是 |
| **KAIROS** | 学术团队 | [arXiv:2510.02084] | 2025 | 20M | 跨领域海量通用基准数据集 | Encoder-Decoder | 非自回归统一多步预测 Patch | TS | 是 |
| **Chronos-2** | Amazon | [arXiv:2510.15821] | 2025 | 710M | 扩展 TSMix 与核合成数据 | Decoder-only | 统一离散概率分布分箱 | TS | 是 |
| **Moirai 2.0** | Salesforce | [arXiv:2511.11698] | 2025 | 311M | LOTSA v2 紧凑高质量预训练集 | Encoder-Decoder | 精简轻量多变量注意力 | TS | 是 |
| **UniShape** | 学术团队 (AAAI 2026) | [arXiv:2601.06429] | 2026 | 35M | UCR/UEA 128 个全域分类集合 | Encoder-only | 统一形态基元 (Shapelet) Token | TS | 是 |
| **PaCoDi** | 金明团队 / 阿里等 | [arXiv:2602.17706] | 2026 | 未报告 | 通用多领域标准基准集 | Complex Diffusion | 并行复数频域补丁 | TS | 是 |
| **Timer-S1** | 清华大学 THUML | [arXiv:2603.04791] | 2026 | 8.3B (激活0.75B) | UTSD-3 强化推理语料 | MoE | 串行缩放 (Serial Scaling) Patch | TS | 是 |
| **WaveMoE** | 学术团队 (ICLR 2026 TSALM) | [arXiv:2604.10544] | 2026 | 未报告 | 通用多领域基准集 | Wavelet-Enhanced MoE | 小波多分辨率频段 Patch | TS | 论文声明 |
| **LeapTS** | 金明团队 (Ming Jin Group) | [arXiv:2605.10292] | 2026 | 未报告 | 跨域长短期多变量基准 | 控制器 + Neural CDE | 自适应动态调度步 Patch | TS | 论文声明 |
| **Olivia** | 学术团队 (ICML 2026) | [arXiv:2605.17340] | 2026 | 未报告 | 跨域多频段公开语料库 | Encoder-Decoder (PSD对齐)| 功率谱密度协调频域 Patch | TS | 是 |
| **Chronicle** | 学术团队 | [arXiv:2605.20268] | 2026 | 324M | 大规模文本-时序混合语料 | Decoder-only | Patch + BPE 混合分词 | TS + Text | 是 |
| **Toto 2.0** | Datadog | [arXiv:2605.20119] | 2026 | 2.5B | 超过 1 万亿时序点 (1T points) | Decoder-only | 工业级 Patch 标度律预训练 | TS | 是 |
| **Falcon-X** | 学术团队 | [arXiv:2605.27286] | 2026 | 未报告 | 异构多变量通用公开数据集 | 原型差分注意力架构 | 潜空间原型解耦 Patch | TS | 论文声明 |
| **FactoryNet** | 学术团队 (ICML 2026) | [arXiv:2605.09081] | 2026 | 未报告 | 5100万点机床/机械臂/冲压遥测 | Encoder-Decoder | 6类具身物理装备遥测 Patch | TS | 是 |
| **CITRAS-FM** | 日立研究团队 (EUSIPCO 2026) | [arXiv:2606.10798] | 2026 | 7M | 跨域边缘工业传感数据集 | Decoder-only (CPU优化) | 协变量门控嵌入 Patch | TS | 是 |
| **The Simulacrum** | Monash / Sydney 等 | [arXiv:2606.27711] | 2026 | 未报告 | 随机过程动力学先验库 | 决策论 Transformer | 贝叶斯最优决策 Token | TS | 论文声明 |
| **MACROCAST** | 学术团队 | [arXiv:2606.28670] | 2026 | 未报告 | FRED-MD 与合成宏观轨迹 | Decoder-only | 版本一致性无泄漏 Patch | TS | 论文声明 |
| **RMISC** | 学术团队 | [arXiv:2607.06504] | 2026 | 未报告 | 1420亿真实多变量时序点 (142B) | Pretraining Corpus / Benchmark | 跨域真实多变量连续 Patch | TS | 是 |
| **Zeus** | 学术团队 (ICML 2026) | [arXiv:2607.01918] | 2026 | 未报告 | U-shaped 多尺度多任务语料 | U-Net Transformer | 点/补丁多目标掩码 Token | TS | 论文声明 |
| **LeNEPA** | 金明团队 (KDD MILETS) | [arXiv:2607.00958] | 2026 | 未报告 | UCR/UEA 标准评测基准 | 自监督编码器 | 无数据增强下一隐状态预测 | TS | 是 |
| **Scale-Aware** | 学术团队 | [arXiv:2608.20005] | 2026 | 未报告 | 多域跨尺度时序语料库 | Transformer | 多 Patch 跨尺度对齐与混合掩码 | TS | 论文声明 |
| **EXAONE Fin** | LG AI Research | [arXiv:2609.04239] | 2026 | 未报告 | 跨国高频订单簿与宏观多变量时序 | Attention-free SSM/Linear | 线性复杂度数值补丁 | TS | 论文声明 |
| **Cadence** | 学术团队 | [arXiv:2609.06008] | 2026 | 330M (TimesFM-3) | 真实工业制造与需求海量数据 | Decoder-only | 误差有界时序残差压缩 Token | TS | 是 |
| **Tabby** | 学术团队 | [arXiv:2609.13956] | 2026 | 145M | OpenTS-Archive 开源配方语料 | Decoder-only | 标准化开源预训练 Patch | TS | 是 |
| **FlowTSFM** | 学术团队 | [arXiv:2609.13640] | 2026 | 38.8M | 未报告 | Encoder-only (Flow) | Recurrent Quantile Patch | TS | 未报告 |
| **SOTER** | 复旦 / 阿里等 | [arXiv:2609.16804] | 2026 | 未报告 | 2260亿时序点 (226B points) | MoE + Neural CDE | 频域 PSD 引导多尺度 Patch | TS | 未报告 |
| **QUALS** | 学术团队 (VLDB 2027) | [arXiv:2609.20156] | 2026 | 未报告 | 跨域多源通用时序语料 | Encoder-Decoder | Pattern Quantization Bins | TS | 未报告 |
| **t0** | 学术团队 | [arXiv:2609.24559] | 2026 | 256M | 未报告 | Decoder-only | 异构时空与文本上下文联合 Patch | TS + Text | 是 |
| **SwitchPFN** | 普林斯顿等学术团队 | [arXiv:2609.29814] | 2026 | 未报告 | 切换动力系统合成先验 | Prior-Data Transformer | 动力学状态分段特征 Token | TS | 是 |
| **TW3Cast** | 学术团队 | [arXiv:2609.28506] | 2026 | 未报告 | GIFT-Eval 训练切分集 | Frozen Router (MoE) | 多骨干特征动态路由 | TS | 是 |
| **VersaTSA** | 学术团队 | [arXiv:2609.22836] | 2026 | 未报告 | VersaTSA (300亿时序观测值) | Decoder-only (混合掩码)| 时间感知非均匀补丁 (Time-Patch)| TS | 论文声明 |
| **TSPFN** | 学术团队 (STACOM 2026) | [arXiv:2608.31013] | 2026 | 未报告 | 14万合成多通道生理数据 (140K) | Prior-Data Transformer | 动力学生理表征 Token | TS | 是 |
| **OutageDiT** | 学术团队 | [arXiv:2609.01896] | 2026 | 未报告 | 区域电网海量停电与天气序列 | Diffusion Transformer (DiT) | 时空条件引导 Patch | TS + Weather | 论文声明 |
| **DynG-Diff** | 学术团队 | [arXiv:2609.02068] | 2026 | 未报告 | 通用多变量时序基准 | State-Aware Diffusion | 状态感知动态引导补丁 | TS | 是 |
| **IPM-FM** | 学术团队 | [arXiv:2609.08375] | 2026 | 未报告 | 大规模工业过程连续传感流 | 自监督 Informer + MC-Dropout | 共识特征选择 Patch | TS | 论文声明 |
| **FreqCondNorm** | 学术团队 | [arXiv:2609.20535] | 2026 | 未报告 | 跨工业预测维护多频段数据集 | Frequency-Conditioned Transformer| 跨频段自适应归一化 Patch | TS | 论文声明 |
| **TiRex-2** | NX-AI / JKU Linz | [arXiv:2607.01204] | 2026 | 35M | LOTSA + 真实多变量流式语料 | Decoder-only (xLSTM) | 流式多变量递推状态 Patch | TS | 是 |
| **Reverso** | 学术团队 | [arXiv:2602.17634] | 2026 | 未报告 | 通用多领域基准集 | Inverted Transformer | 零样本参数高效算力缩放 Patch | TS | 论文声明 |
| **VLT** | 工业智能学术团队 | [arXiv:2607.14510] | 2026 | 未报告 | 工业机电三模态大规模传感语料 | Trimodal VLT Transformer | 视觉-语言-时序三模态统一 Patch | TS + Text + Vision | 论文声明 |

---

### 4.2 离散量化语言化路线：分箱映射与交叉熵形式化

将连续时间序列完全“语言化” (Tokenize into Discrete Symbols) 是 Amazon Chronos 家族开创的代表性路线。该路线的核心理论假设是：**自回归语言模型的交叉熵优化不仅适用于离散自然语言，也天然适合拟合任意复杂的多峰、非高斯连续概率分布，免除了预先假设正态或学生-t 分布的先验偏见**。

#### 4.2.1 均值绝对缩放与分箱映射数学形式化

给定输入单变量时间序列上下文 $\mathbf{x}_{1:T} = [x_1, \dots, x_T]^\top \in \mathbb{R}^T$，Chronos [arXiv:2403.07815] 首先计算局部均值绝对尺度 (Mean Absolute Scale)：
$$\mu_{\mathbf{x}} = \frac{1}{T} \sum_{t=1}^T |x_t| + \epsilon_{\text{scale}}$$
其中 $\epsilon_{\text{scale}} = 10^{-5}$ 用于防止除零异常。将输入序列除以标度因子得到无量纲归一化序列：
$$\tilde{x}_t = \frac{x_t}{\mu_{\mathbf{x}}}, \quad t=1,\dots,T$$

随后，设定词表大小为 $B$（在 Chronos 官方实现中 $B=4096$），定义分箱边界网格 $\{z_0, z_1, \dots, z_B\}$。网格可以是均匀分箱也可以是基于正态分布累积分布函数的非均匀分位数网格。量化映射算子 $\mathcal{Q}: \mathbb{R} \to \{0, 1, \dots, B-1\}$ 定义为：
$$c_t = \mathcal{Q}(\tilde{x}_t) = \text{clip}\left( \left\lfloor \frac{\tilde{x}_t - z_{\min}}{z_{\max} - z_{\min}} \cdot B \right\rfloor, 0, B-1 \right)$$
每个连续数值被严格离散化为一个词表索引 $c_t \in \{0, \dots, B-1\}$。对于缺失值或特殊控制位，Chronos 保留专门的 `<PAD>` 与 `<EOS>` 标记。

#### 4.2.2 因果交叉熵损失与概率采样推断

在自回归解码器中，模型预测未来分箱索引的条件类别分布：
$$p_\theta(c_{t} = k \mid c_{<t}) = \frac{\exp(z_{t, k})}{\sum_{j=0}^{B-1} \exp(z_{t, j})}$$
模型整体优化目标为纯粹的标准类别交叉熵损失 (Categorical Cross-Entropy)：
$$\mathcal{L}_{\text{CE}}(\theta) = - \frac{1}{H} \sum_{t=T+1}^{T+H} \sum_{k=0}^{B-1} \mathbb{I}(c_t = k) \log p_\theta(c_t = k \mid c_{<t})$$

在推理阶段，预测未来的连续值轨迹不再依赖单一数值点回归，而是通过多样本蒙特卡洛采样 (Monte Carlo Sampling)：从多项分布中独立采样 $S$ 条离散路径 $\{c_{T+1:T+H}^{(s)}\}_{s=1}^S$，随后应用反量化算子 $\mathcal{Q}^{-1}(c) = z_c + \frac{z_{c+1} - z_c}{2}$ 并乘以原始尺度恢复真实量纲：
$$\hat{x}_t^{(s)} = \mathcal{Q}^{-1}(c_t^{(s)}) \cdot \mu_{\mathbf{x}}$$
这使得 Chronos 天然具备输出任意分位数预测（如 $p_{10}, p_{50}, p_{90}$）与非对称风险区间的强大能力。

#### 4.2.3 架构演进、行业适配与内在权衡

- **Chronos-2** [arXiv:2510.15821]：将离散量化拓展至通用多变量预测，通过交叉注意力将多条序列的量化分箱进行联合因果建模；
- **FedChronos** [arXiv:2608.01290]：在保护数据主权的前提下，构建联邦参数高效微调 (Federated PEFT) 框架，使去中心化机构共享离散自回归表征；
- **KG-Chronos-2** [arXiv:2609.21381]：将水动力学知识图谱拓扑约束注入 Chronos-2，在极端水文场景下展现出极高的物理保真度。

**技术权衡分析**：
离散量化的核心优势在于**极强的分布拟合柔性与语言模型现成生态的无缝复用**，对离群脉冲和多峰后验具有天然的鲁棒性。然而其核心缺陷在于**损失了连续数值的度量有序性 (Metric Ordinality)**：在标准交叉熵看来，分箱 100 与分箱 101 的预测惩罚，与分箱 100 与分箱 4000 的预测惩罚在分类损失下是完全等同的；此外，随着分箱精度需求提升，词表大小 $B$ 膨胀会导致最后一层 Softmax 计算开销与显存占用显著攀升。

---

### 4.3 连续补丁自回归路线：两阶段投影与 Huber 回归推导

与 Amazon 的离散化路线针锋相对，Google 提出的 TimesFM [arXiv:2310.10688] 坚持基于连续浮点数值的补丁自回归路线。该路线认为时间序列的物理本质是连续波形，分箱离散化破坏了高频细节与微小振幅变化。

#### 4.3.1 连续补丁切分与两阶段线性投影形式化

TimesFM 将输入序列 $\mathbf{x} \in \mathbb{R}^T$ 以步长 $S=P_{\text{in}}$ 进行非重叠切分，得到连续数值补丁 $\mathbf{p}_i = \mathbf{x}_{(i-1)P_{\text{in}}+1 : i P_{\text{in}}} \in \mathbb{R}^{P_{\text{in}}}$。输入补丁长度通常设为 $P_{\text{in}} = 32$。
输入两阶段结构的第一阶段是输入连续投影：
$$\mathbf{h}_i^{(0)} = \mathbf{W}_{\text{in}} \mathbf{p}_i + \mathbf{b}_{\text{in}} + \mathbf{e}_{\text{pos}, i} \in \mathbb{R}^D$$
其中 $\mathbf{W}_{\text{in}} \in \mathbb{R}^{D \times P_{\text{in}}}$ 为输入线性映射矩阵。经过 $L$ 层标准 Transformer 解码器前向传播后，获得最后一层隐藏状态 $\mathbf{h}_i^{(L)} \in \mathbb{R}^D$。

关键的第二阶段是**长视野输出线性投射 (Long-Horizon Output Projection)**：不同于传统模型单步预测单步滑动的做法，TimesFM 采用非对称设计，直接通过输出头矩阵 $\mathbf{W}_{\text{out}} \in \mathbb{R}^{P_{\text{out}} \times D}$ 一次性输出未来长达 $P_{\text{out}} = 128$ 步的预测切片：
$$\hat{\mathbf{y}}_{i} = \mathbf{W}_{\text{out}} \mathbf{h}_i^{(L)} + \mathbf{b}_{\text{out}} \in \mathbb{R}^{P_{\text{out}}}$$
在预测阶段，如果目标预测视野 $H \le P_{\text{out}}$，模型仅需单次前向传播 (One-Shot Forward) 即可截取前 $H$ 步完成预测；若 $H > P_{\text{out}}$，则将生成的 $P_{\text{out}}$ 切片按 $P_{\text{in}}$ 重新切片追加至输入序列，以自回归方式滚动前向推断。

#### 4.3.2 连续 Huber 稳健回归损失与似然推导

为了在连续空间兼顾高斯假设下的平滑收敛与对工业脉冲极端离群点的抗扰动能力，TimesFM 与后续连续自回归模型（如 Timer [arXiv:2402.02368], Timer-XL [arXiv:2410.04803]）普遍采用平滑 L1 / Huber 损失：
$$\mathcal{L}_{\text{Huber}}(\hat{\mathbf{y}}, \mathbf{y}) = \frac{1}{P_{\text{out}}} \sum_{j=1}^{P_{\text{out}}} \ell_\delta(\hat{y}_j - y_j)$$
其中逐点残差误差函数 $\ell_\delta(e)$ 定义为：
$$\ell_\delta(e) = \begin{cases} \frac{1}{2} e^2 & \text{if } |e| \le \delta \\ \delta |e| - \frac{1}{2}\delta^2 & \text{otherwise} \end{cases}$$
阈值 $\delta$ 调节了均方误差 (MSE, 强调高斯平滑) 与绝对误差 (MAE, 抵御长尾离群) 之间的平滑过渡。
在概率预测模式下，模型输出头进一步扩展为同时预测条件均值 $\hat{\mu}_j$ 与方差 $\hat{\sigma}_j^2$，基于学生-t 分布或异方差高斯负对数似然 (NLL) 实施连续端到端反向传播：
$$\mathcal{L}_{\text{NLL}}(\theta) = \sum_{j=1}^{P_{\text{out}}} \left[ \frac{(y_j - \hat{\mu}_j)^2}{2 \hat{\sigma}_j^2} + \frac{1}{2} \log \hat{\sigma}_j^2 \right]$$

**技术权衡分析**：
连续补丁自回归路线的最大优势在于**计算密度极高且天然保留精确的数值量纲**，长视野两阶段输出架构使推理延迟相比离散逐点生成降低了数十倍。然而，其潜在局限在于连续回归损失在面对高度复杂的多峰未来情景时，易退化至条件均值，导致外推轨迹趋向于平滑滤波。

---

### 4.4 全频段全变量统一路线：vRoPE 与 Any-variate 跨通道注意力

在现实工业与宏观经济场景中，多变量时间序列往往面临两个最棘手的结构性挑战：(1) **通道维度剧烈动态变化**（从单通道传感器到数百通道电力网格）；(2) **采样周期千差万别**（从高频毫秒到宏观年度）。Salesforce 团队推出的 Moirai [arXiv:2402.02592] 与 Moirai 2.0 [arXiv:2511.11698] 提出了奠基性的 Any-variate 统一建模理论。

#### 4.4.1 Any-variate 序列扁平化与注意力计算

给定多变量时序张量 $\mathbf{X} \in \mathbb{R}^{T \times C}$，传统方法要么强制通道独立 (CI)，要么要求固定的通道数 $C$。Moirai 提出彻底将多变量时序在 Token 序列维度上执行结构化展平：
将每一个通道 $c \in \{1,\dots,C\}$ 独立切分为 $N$ 个补丁，随后将所有通道的补丁展平拼接为一个总长度为 $L_{\text{total}} = N \cdot C$ 的一维 Token 序列：
$$\mathbf{Z} = [\mathbf{p}_{1, 1}, \mathbf{p}_{2, 1}, \dots, \mathbf{p}_{N, 1}, \mathbf{p}_{1, 2}, \dots, \mathbf{p}_{N, C}] \in \mathbb{R}^{(N \cdot C) \times P}$$
每个 Token 由一个二元元组 $(m, c)$ 唯一标识，其中 $m \in \{1,\dots,N\}$ 为时间切片索引，$c \in \{1,\dots,C\}$ 为变量通道索引。

#### 4.4.2 变量感知旋转位置编码 (vRoPE) 严格推导

在将多变量序列完全展平后，普通的 1D 绝对位置编码或标准 RoPE 无法区分“不同时间同一通道”与“同一时间不同通道”。Moirai 提出了变量感知旋转位置编码 (Variable-aware Rotary Position Embedding, vRoPE)。

将特征维度 $D$ 正交解耦为时间子空间 $D_{\text{time}} = D/2$ 与通道子空间 $D_{\text{var}} = D/2$。整体 2D 旋转变换矩阵设计为对角块矩阵：
$$\mathbf{R}_{\Theta, m, c} = \begin{pmatrix} \mathbf{R}_{\text{time}}(m) & \mathbf{0} \\ \mathbf{0} & \mathbf{R}_{\text{var}}(c) \end{pmatrix} \in \mathbb{R}^{D \times D}$$
其中时间旋转子矩阵 $\mathbf{R}_{\text{time}}(m)$ 由 $D/4$ 个独立二维旋转矩阵构成，频率基底设为 $\theta_k = 10000^{-2(k-1)/D_{\text{time}}}$：
$$\mathbf{R}_{\text{time}}(m) = \text{diag}\left( \begin{pmatrix} \cos m\theta_1 & -\sin m\theta_1 \\ \sin m\theta_1 & \cos m\theta_1 \end{pmatrix}, \dots, \begin{pmatrix} \cos m\theta_{D/4} & -\sin m\theta_{D/4} \\ \sin m\theta_{D/4} & \cos m\theta_{D/4} \end{pmatrix} \right)$$
同理，变量通道旋转子矩阵 $\mathbf{R}_{\text{var}}(c)$ 由正交频率 $\phi_k = 10000^{-2(k-1)/D_{\text{var}}}$ 驱动：
$$\mathbf{R}_{\text{var}}(c) = \text{diag}\left( \begin{pmatrix} \cos c\phi_1 & -\sin c\phi_1 \\ \sin c\phi_1 & \cos c\phi_1 \end{pmatrix}, \dots, \begin{pmatrix} \cos c\phi_{D/4} & -\sin c\phi_{D/4} \\ \sin c\phi_{D/4} & \cos c\phi_{D/4} \end{pmatrix} \right)$$

对于查询向量 $\mathbf{q}_{(m_i, c_i)}$ 与键向量 $\mathbf{k}_{(m_j, c_j)}$，二者的内积注意力评分满足：
$$\langle \mathbf{R}_{\Theta, m_i, c_i} \mathbf{q}, \mathbf{R}_{\Theta, m_j, c_j} \mathbf{k} \rangle = \mathbf{q}_{\text{time}}^\top \mathbf{R}_{\text{time}}(m_i - m_j) \mathbf{k}_{\text{time}} + \mathbf{q}_{\text{var}}^\top \mathbf{R}_{\text{var}}(c_i - c_j) \mathbf{k}_{\text{var}}$$
**数学性质证明**：内积仅取决于相对时间滞后 $\Delta m = m_i - m_j$ 与通道相对偏移 $\Delta c = c_i - c_j$。特别地，当 $c_i = c_j$ 时，通道项获得恒等的零相位最大增益；当 $c_i \ne c_j$ 时，通道项表达跨变量协方差交互，从而以同一套注意力机制无缝支持从 1 个通道到任意 $C$ 个通道的输入，无需改变任何模型权重。

#### 4.4.3 多尺度补丁投影机制

为了适应高频（分钟、小时）与低频（天、周、月）的巨大周期跨度，Moirai 设计了多补丁投射算子池 $\mathcal{P} = \{8, 16, 32, 64, 128\}$。在预训练和推理时，模型根据输入序列的实际采样率，自适应激活对应尺寸的补丁线性层，避免了人工重采样导致的高频失真或信息损失。

---

### 4.5 清华 THUML Timer 与 Sundial 系列：下一补丁自回归到连续流匹配

清华大学软件学院龙明盛教授团队（THUML）开创了从大时序模型 (Large Time Series Model, LTM) 到连续流匹配 (Continuous Flow Matching) 的系统化演进道路。

#### 4.5.1 Timer 与 Timer-XL：长上下文单序列自回归

Timer [arXiv:2402.02368] 建立了首个大规模统一时序预训练架构。采用单序列单补丁自回归形式，基于大规模高质量 UTSD 语料，证明了统一解码器能够同时胜任预测、插补与异常检测。随后推出的 Timer-XL [arXiv:2410.04803] 针对工业时序超长历史回看的需要，结合 UTSD-2 语料，利用扩展上下文因果注意力机制，使模型对超长上下文周期依赖的吸收能力实现数倍跨越。

#### 4.5.2 Sundial：TimeFlow 连续流匹配生成大模型严格形式化

在 2025 年发布的 15 亿参数 (1.5B) 大模型 **Sundial** [arXiv:2502.00816] 中，THUML 团队开创性地指出：传统的均方误差回归容易导致平滑滤波，而离散分箱又破坏了高精度浮点连续性。Sundial 提出了基于条件连续流匹配 (Conditional Flow Matching, CFM) 的 **TimeFlow** 生成理论。

令目标未来时序补丁为 $\mathbf{x}_1 \in \mathbb{R}^P$，历史观测上下文为 $\mathbf{c} \in \mathbb{R}^{L_{\text{ctx}} \times D}$。定义先验噪声分布为标准高斯分布 $\mathbf{x}_0 \sim p_0(\mathbf{x}_0) = \mathcal{N}(\mathbf{0}, \mathbf{I})$。
构造连接先验与真实未来数据的时间依赖连续概率路径 (Probability Path)：
$$\mathbf{x}_t = (1 - t) \mathbf{x}_0 + t \mathbf{x}_1, \quad t \in [0, 1]$$
对应的真实时变速度场为常数目标：
$$\frac{d\mathbf{x}_t}{dt} = \mathbf{x}_1 - \mathbf{x}_0$$

Sundial 训练一个由 Transformer 骨干参数化的神经速度场预测网络 $v_\theta(\mathbf{x}_t, t, \mathbf{c})$，其连续流匹配优化目标定义为：
$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t \sim \mathcal{U}[0, 1], \mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}), \mathbf{x}_1 \sim q(\mathbf{x}_1 \mid \mathbf{c})} \left\| v_\theta\left((1-t)\mathbf{x}_0 + t\mathbf{x}_1, t, \mathbf{c}\right) - (\mathbf{x}_1 - \mathbf{x}_0) \right\|_2^2$$

在生成推断阶段，预测未来轨迹等价于求解常微分方程 (ODE) 的初值问题 (IVP)：
$$\frac{d\mathbf{x}_t}{dt} = v_\theta(\mathbf{x}_t, t, \mathbf{c}), \quad \mathbf{x}(0) = \mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$
采用欧拉法 (Euler Method) 或二阶休恩法 (Heun's Method) 进行高效离散化数值积分（仅需 $K \in [10, 20]$ 个采样步长）：
$$\mathbf{x}_{t_{k+1}} = \mathbf{x}_{t_k} + \Delta t \cdot v_\theta(\mathbf{x}_{t_k}, t_k, \mathbf{c})$$
实验证实，TimeFlow 克服了扩散模型上百步去噪的极端延迟，不仅实现了秒级亚微秒的概率轨迹生成，且生成波形在功率谱密度与相位高阶矩上均完美逼近真实物理动力学过程。

---

### 4.6 混合专家 (MoE) 路线与动态路由：Top-k 门控、频域解耦与负载均衡

当密集基础模型的参数量突破 10 亿大关时，全激活 Transformer 会产生沉重的训练算力与推理延迟负担。稀疏混合专家 (Mixture of Experts, MoE) 架构成为了平衡模型表达容量与计算效率的破局利刃。

#### 4.6.1 动态 Top-k 门控与负载均衡正则化损失

在一个包含 $E$ 个专家网络 $\{F_1, F_2, \dots, F_E\}$ 的 MoE 模块中，对于输入隐藏表示 $\mathbf{h} \in \mathbb{R}^D$，门控路由器计算所有专家的原始匹配分数：
$$\mathbf{s} = \mathbf{h} \mathbf{W}_g + \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}\left(\mathbf{0}, \sigma_{\text{gate}}^2 \mathbf{I}\right)$$
其中 $\mathbf{W}_g \in \mathbb{R}^{D \times E}$ 为可训练门控参数，$\boldsymbol{\epsilon}$ 为探索噪声。门控网络选择得分最高的前 $k$ 个专家 ($k \ll E$，通常 $k=1$ 或 $k=2$)：
$$\mathcal{T} = \text{TopK}(\mathbf{s}, k)$$
归一化门控权重为：
$$g_e(\mathbf{h}) = \begin{cases} \frac{\exp(s_e)}{\sum_{j \in \mathcal{T}} \exp(s_j)} & \text{if } e \in \mathcal{T} \\ 0 & \text{otherwise} \end{cases}$$
该层的最终输出为激活专家的加权组合：
$$\mathbf{y} = \sum_{e \in \mathcal{T}} g_e(\mathbf{h}) F_e(\mathbf{h})$$

为了防止所有时序 Token 均聚集于少数主导专家而导致其余专家退化饿死（即表征崩塌），必须引入辅助负载均衡损失 (Auxiliary Load-Balancing Loss)：
$$\mathcal{L}_{\text{balance}} = \alpha \cdot E \sum_{e=1}^E f_e \cdot P_e$$
其中 $f_e = \frac{1}{N} \sum_{i=1}^N \mathbb{I}(e \in \mathcal{T}_i)$ 为批次内 Token 实际分配给专家 $e$ 的比例频率，$P_e = \frac{1}{N} \sum_{i=1}^N \frac{\exp(s_{i, e})}{\sum_{j=1}^E \exp(s_{i, j})}$ 为批次内专家 $e$ 的平均门控概率。当且仅当所有专家的处理负荷与分配概率达到完全均匀分布时，$\mathcal{L}_{\text{balance}}$ 取得理论极小值。

#### 4.6.2 小波子带解耦与频域协调前沿

时序信号的物理特性天然具备频域分层特征，这与 MoE 的专家专业化具有高度的内在契合性：
- **Time-MoE** [arXiv:2409.16040]（金明组）：构建了包含 3000 亿时序点的 Time-300B 语料库，最大版本达 24 亿 (2.4B) 参数，通过 Top-k 门控自适应路由多尺度补丁，在保持小模型推理 FLOPs 的同时大幅推高泛化边界；
- **Timer-S1** [arXiv:2603.04791]（THUML）：推出 83 亿总参数 (8.3B)、激活仅 0.75B 的大模型，提出串行缩放 (Serial Scaling) 技术，突破了超大规模时序预训练的收益递减瓶颈；
- **WaveMoE** [arXiv:2604.10544]（ICLR 2026 TSALM）：提出小波增强型混合专家架构。WaveMoE 利用离散小波变换 (DWT) 将原始时序严格分解为低频逼近趋势分量 $\mathbf{A}_J$ 与多级高频细节分量 $\{\mathbf{D}_1, \dots, \mathbf{D}_J\}$：
  $$\mathbf{x} = \mathbf{A}_J + \sum_{j=1}^J \mathbf{D}_j$$
  门控路由器依据小波能量分布将平滑趋势分量定向分发给“长程低频趋势专家”，将尖锐微扰分量分发给“局部高频瞬变专家”，从根本上解决了高低频时序特征相互干扰的频域混叠难题；
- **Olivia** [arXiv:2605.17340]（Fei 等，ICML 2026）：揭示了跨领域预训练中“频域失真 (Spectral Distortion)”的核心病灶。不同领域数据集的采样率与物理背景不同，直接混合会导致模型过度偏向特定高频能量分布。Olivia 创新引入功率谱密度协调器 (Harmonizer)，通过频域一致性损失进行对齐约束：
  $$\mathcal{L}_{\text{PSD}} = \left\| \mathcal{F}_{\text{PSD}}(\hat{\mathbf{x}}) - \mathcal{F}_{\text{PSD}}(\mathbf{x}) \right\|_2^2$$
  使模型在零样本迁移至全新频段的物理信号时仍能维持正确的能量分布特性；
- **SOTER** [arXiv:2609.16804]：在 2260 亿生理时序点上预训练，利用功率谱密度 (PSD) 引导确定性频带专家路由；
- **TW3Cast** [arXiv:2609.28506]：在 GIFT-Eval 权威基准上提出突破性的“冻结路由器 (Frozen Router)”范式，无需端到端重训大模型，仅在训练切分上拟合轻量门控即可取得第 3 名顶尖成绩。

---

### 4.7 动态调度、神经微分方程与误差有界压缩 (LeapTS, Cadence)

时间序列建模的物理边界正在向连续动力学自适应调度与海量工业数据流无损压缩方向纵深迈进。

#### 4.7.1 LeapTS：动态多视野调度与连续神经微分方程 (Neural CDE)

主流预测模型普遍采用固定步长滚动预测（例如固定输出未来 96 步或 128 步）。金明团队在最新研究 **LeapTS** [arXiv:2605.10292] 中重新审视了这一范式，创新性地提出将时间序列预测重构为**自适应多视野动态调度过程 (Adaptive Multi-Horizon Scheduling)**。

现实物理系统的动态演化具有强非均匀性：在平稳常态下，系统状态缓慢演化，可以大幅“跳步”预测；在剧烈震荡期，必须采用微小步长细致刻画。LeapTS 构建了双层分层架构：
1. **高层调度控制器 (Hierarchical Scheduler)**：根据当前隐状态的不确定性与演化梯度，动态决策下一步的外推时间跨度 $\Delta \tau_k \in \{\delta_1, \delta_2, \dots, \delta_M\}$；
2. **底层连续动力学生成器 (Continuous Neural CDE)**：为了处理任意非等间距的连续跳跃，底层状态演化被形式化为受控连续微分方程 (Neural Controlled Differential Equation, Neural CDE)：
   $$\mathbf{z}(\tau_{k+1}) = \mathbf{z}(\tau_k) + \int_{\tau_k}^{\tau_{k+1}} f_\theta(\mathbf{z}(s)) dX(s)$$
   其中 $X(s)$ 为驱动时序观测的连续插值路径。该机制允许模型以连续积分的方式推导任意连续时间点上的系统物理状态，完全摆脱了离散固定时间网格的束缚，在多采样率与多尺度预测任务中展现出超越传统刚性自回归模型的卓越泛化性能。

#### 4.7.2 Cadence：基础模型残差驱动的误差有界工业时序压缩

在工业物联网 (IIoT) 与大规模传感器网络中，海量时序数据的云端回传面临巨大的带宽与存储开销。**Cadence** [arXiv:2609.06008] 开创性地将预训练基础模型引入工业数据压缩领域，提出了首个基于大模型预测残差的**误差有界有损压缩机制 ($\epsilon$-bounded Lossy Compression)**。

给定工业时序真值 $x_t$，利用冻结的预训练基础模型（如 Google TimesFM-3 330M）生成条件期望预测值 $\hat{x}_t = \mathbb{E}[x_t \mid x_{<t}]$。真值与模型预测之间的残差为：
$$r_t = x_t - \hat{x}_t$$
由于基础模型已充分吸收了周期、趋势与平滑连续性，残差 $r_t$ 呈现出均值为零、方差极紧致的高斯白噪声特性。

Cadence 引入用户预设的最大允许绝对物理误差限 $\epsilon$（即必须严格保证解压后的信号 $\tilde{x}_t$ 满足 $|x_t - \tilde{x}_t| \le \epsilon$）。对残差实施均匀死区量化：
$$q_t = \text{round}\left( \frac{r_t}{2\epsilon} \right) \cdot 2\epsilon$$
重建信号为 $\tilde{x}_t = \hat{x}_t + q_t$。数学上恒有：
$$|x_t - \tilde{x}_t| = |r_t - q_t| = \left| r_t - \text{round}\left( \frac{r_t}{2\epsilon} \right) \cdot 2\epsilon \right| \le \epsilon$$
随后，利用基础模型输出的条件方差作为上下文概率表，对离散量化阶数 $k_t = \text{round}(r_t / 2\epsilon)$ 实施自适应算术熵编码 (Arithmetic Coding)。实验表明，Cadence **将工业传感器流的传输体积压缩至原始大小的 10% 至 25%**，同时数学上 100% 严密保证了解压信号的物理误差界限，为工业边缘网关数据回传提供了里程碑式的解决方案。

---

### 4.8 编码器架构、形态基元与轻量边缘部署 (MOMENT, TTM, CITRAS-FM)

并非所有应用场景都需要动辄数亿参数的生成式解码器。在许多工业边缘设备与嵌入式芯片中，计算资源受限且更侧重于双向表征理解与亚毫秒级预测。

- **MOMENT** [arXiv:2402.03885]（CMU 联合研制，最大 385M）：坚持纯编码器掩码自编码 (Masked Autoencoding, MAE) 路线。在涵盖 1300 万序列的 Time-series Pile 上预训练，以统一双向特征提取器同时赋能预测、异常检测、分类与插补四项核心任务；
- **TTM** [arXiv:2401.03955]（IBM Research）：提出 Tiny Time Mixers。参数量仅在 1M 至 8M 之间，基于精简的多尺度 MLP-Mixer 架构，在边缘设备上实现微秒级的低延迟推理，证实了轻量基础模型在工业端侧的巨大商业潜能；
- **CITRAS-FM** [arXiv:2606.10798]（Hitachi 研究团队，EUSIPCO 2026）：提出面向边缘 CPU 极速推断的微型时序基础模型（参数量仅 **7M**）。CITRAS-FM 专为集成外生协变量 (Covariate-Informed) 设计，通过精简的自回归因果注意力和门控协变量融合机制，在通用工业预测场景中实现了与百兆级模型相当的零样本表现，且完全能够在低功耗边缘工控机上实现实时无卡 (CPU-only) 毫秒级推断；官方代码已开源核验；
- **UniShape** [arXiv:2601.06429]（AAAI 2026）：颠覆了固定长度补丁的生硬切分，提出基于形态感知基元 (Shapelet Primitives) 的统一分类大模型，在 128 个 UCR/UEA 跨域分类基准上建立全新标杆；
- **FlowTSFM** [arXiv:2609.13640]：将单层 Transformer 结构深度展开解释为循环分位数传输过程 (Recurrent Quantile Transport)，以仅 38.8M 参数比肩 119.5M 的重型模型；
- **VersaTSA** [arXiv:2609.22836]：针对非均匀不规则采样的多变量序列，开源构建了包含 **300 亿时序观测值 (30B observations)** 的超大规模跨领域预训练语料库，并提出混合注意力与时间感知补丁 (Time-Aware Patch) 架构，彻底消除了传统插值对不规则序列时变特性的失真；
- **IPM-FM** [arXiv:2609.08375]：针对复杂工业过程监控 (Industrial Process Monitoring) 中传感器冗余干扰与工况多变的难题，提出融合共识特征选择 (Consensus Feature Selection, CFS) 与 MC-Dropout 不确定性估计的工业基础模型，以自监督方式学习物理测点间的鲁棒拓扑；
- **FreqCondNorm** [arXiv:2609.20535]：提出面向跨领域预测维护 (Predictive Maintenance) 的频率条件归一化 Transformer 基础模型。针对工业旋转机械从低频 (1Hz) 到超声高频 (100kHz) 巨大的振动采样跨度，通过将采样频率显式参数化为条件归一化调制算子，实现了不同工业工况和物理装备间的零样本迁移；
- **TSPFN** [arXiv:2608.31013]（STACOM 2026）：将时间序列拟合先验数据网络扩展至生理时序领域，构建了面向生理信号分类的时序表格基础模型，基于 14 万条合成多元生理动力学轨迹预训练，在零样本重症监护多通道分类上取得优异性能，官方代码经由 GitHub API 严格核验。

---

### 4.9 连续动力学生成、无数据增强表征与无注意力前沿

针对复杂物理系统的动力学连续性与无序高频交互，2025-2026 年涌现出多种前沿探索：
- **PaCoDi** [arXiv:2602.17706]（金明团队 / 阿里等）：针对传统扩散模型在时序生成中必须经历百步自回归串行去噪、采样延迟巨大且容易累积时域漂移的瓶颈，首创**并行复数扩散生成架构 (Parallel Complex Diffusion, PaCoDi)**。PaCoDi 将实数域时间序列映射至复数谱平面 $\mathbf{Z} \in \mathbb{C}^{F \times K}$，实现幅值能量与相位角度的正交解耦；通过设计频域双射前向扩散方程，在所有频段与多步长视野上实现全并行单次生成去噪，在长程高保真时序轨迹生成中将生成吞吐提升了数十倍，官方开源代码经由 GitHub API 严格核验；
- **The Simulacrum** [arXiv:2606.27711]（Monash / Sydney 等）：建立基于统计决策论与随机过程先验的预训练新体系。不同于传统仅以概率密度 NLL 为目标的模型，The Simulacrum 直接在多样化合成随机动力学先验族上极小化有限样本贝叶斯行动风险，使模型在零样本下天然输出契合下游非对称效用的贝叶斯近最优决策；
- **FlowState** [arXiv:2508.05287]：提出采样率等变 (Sampling-Rate-Equivariant) 的连续流生成架构；
- **FLAME** [arXiv:2512.14253]：通过流增强勒让德正交多项式记忆系统实现自适应长程记忆；
- **LeNEPA** [arXiv:2607.00958]（金明组，KDD MILETS 2026）：深入反思传统时序自监督学习依赖经验性时间扭曲和抖动等数据增强操作对物理因果规律的破坏，提出“免数据增强下一隐状态预测 (No-Augmentation Next-Latent Prediction)”范式，直接在潜空间中建模连续动力学转移；
- **SwitchPFN** [arXiv:2609.29814]：将分段切换动力系统 (Switching Dynamical Systems) 先验融入先验拟合 Transformer，在完全冻结参数的条件下实现高精度零样本时序分类；
- **EXAONE Finance 1.0** [arXiv:2609.04239]（LG AI Research）：针对高频金融市场的长序列订单簿交互，提出首个面向金融市场的无注意力 (Attention-Free) 时序大模型，采用线性复杂度的循环状态空间 (SSM) 机制，彻底规避了自注意力二次方算力惩罚；
- **DynG-Diff** [arXiv:2609.02068]：针对扩散模型在非平稳多变量时序预测中条件引导能力不足的缺陷，提出状态感知动态引导扩散框架 (State-Aware Dynamic Guidance Diffusion)。通过引入隐状态自适应门控动态调节反向扩散过程中的引导强度，显著压降了条件生成轨迹的方差漂移，官方开源代码已由 GitHub API 官方核验；
- **OutageDiT** [arXiv:2609.01896]：将 Diffusion Transformer 架构成功应用于极端天气下的电力网格停电预测与故障场景仿真，能够受控生成符合复杂物理网格约束的极端停电级联演变轨迹；
- **扩散逆向终端步去噪反思 (When Denoising Hurts)** [arXiv:2608.14067]：深入揭示了扩散模型在时序生成推断中的“终端阶段漂移 (Terminal Step Drift)”现象——传统扩散模型坚持执行到最后一步 $t=0$，然而在低信噪比时序中，终端逆去噪往往因过度拟合高斯白噪声而抹杀关键周期波形。研究给出了最优提前停止准则，在减少推断步数的同时有效提升了生成保真度；
- **TabPFN-TS 区域集中供热系统系统性评测** [arXiv:2608.20024]：首次对基于先验数据拟合的大模型 TabPFN-TS 在大型区域供热网络 (District Heating Networks) 真实零样本概率热负荷预测进行了全面系统评估，证实了无需微调的贝叶斯后验拟合在公用事业负荷预测中的极高工程实用性。

---

### 4.10 新兴开源预训练前沿：Tabby, Toto 2.0, Zeus, Falcon-X 与 t0

进入 2026 年，时序基础模型开源生态进入深水区，架构探索呈现多点突破：
- **RMISC** [arXiv:2607.06504]（Sun 等）：开源发布了目前公开文献中规模领先的真实多变量工业与科研预训练语料库，包含 **1420 亿真实观测点 (142B points)**。涵盖电网配网高频遥测、重工制造流水线、多源气象站网与分布式交通传感器等 10 余个关键工业垂直领域，彻底打破了此前开源 TSFM 高度依赖合成模拟数据或小规模 ETT 基准的尴尬局面；
- **Zeus** [arXiv:2607.01918]（Fu 等，ICML 2026）：针对传统大模型在不同下游任务（预测、插补、分类、异常检测）上必须分别微调的弊端，提出面向时序分析的**免调优通用基础模型 (Towards Tuning-Free Foundation Model)**。Zeus 构建了 U 形多尺度层次 Transformer 骨干，并首创多目标时序掩码预训练范式 (Multi-Objective Temporal Masking, MOTM)，在无需任何目标域参数微调的前提下，单一模型在多任务综合评测中全面超越诸多经过精细监督微调的专有模型；
- **Falcon-X** [arXiv:2605.27286]（Liu 等）：针对复杂现实系统中传感器物理属性与量纲高度不一致的“异构多变量 (Heterogeneous Multivariate)”建模难题，提出原型差分注意力架构 (Prototype Diff-Attention)。Falcon-X 将异构物理变量显式解耦并投影至统一的连续隐式原型空间，在保持通道互补信息的同时彻底消除了虚假跨通道相关性；
- **MACROCAST** [arXiv:2606.28670]（Carriero 等）：专门针对宏观经济学中“历史数据版本多轮修订”的隐蔽穿越漏洞，基于 FRED-MD 与合成宏观动态轨迹构建了**首个版本一致性宏观时序基础模型 (Vintage-Consistent TSFM)**，在完全杜绝未来信息污染的前提下，在实时 GDP 临近预报与通胀外推中刷新基准；
- **Datadog Toto 2.0** [arXiv:2605.20119]：发布五组开源权重模型（最大达 25 亿参数 2.5B），基于超 1 万亿点预训练语料；
- **Tabby** [arXiv:2609.13956]：发布了首个端到端完全公开透明的 TSFM 预训练配方与 OpenTS-Archive 数据清洗管线；
- **$t_0$** [arXiv:2609.24559]：将异构环境与文本上下文联合融入 256M 解码器架构中；
- **QUALS** [arXiv:2609.20156]（VLDB 2027）：提出模式量化 (Pattern Quantization) 与可学习性同步机制，攻克跨域预训练中的样本不均衡与灾难性遗忘；
- **ORBIT 预训练机制与数据分布基准** [arXiv:2608.13262]：深入探究了时序基础模型的预训练机制 (Training Regimes)，构建了 ORBIT 体系。研究揭示了混合预训练中不同行业领域（金融、交通、气象、工业）的数据配比失衡对零样本下游迁移能力的深远影响，提出了动力学多样性平衡采样准则；
- **TiRex-2 扩展多变量流式基础模型** [arXiv:2607.01204]（NX-AI / JKU Linz）：在单变量 TiRex 基础上，将扩展长短期记忆网络 (xLSTM) 成功推广至通用多变量流式时序基础模型。TiRex-2 构建了基于块对角指数门控与矩阵记忆单元的循环状态机，打破了标准自注意力机制在在线流式推断中计算开销随历史长度呈二次方激增的根本枷锁，以 $\mathcal{O}(1)$ 的单步推断时间复杂度与 $\mathcal{O}(d^2)$ 的恒定内存占用，在毫秒级多变量连续遥测流中实现了零样本高精度滚动预测；
- **Reverso 参数高效零样本计算缩放** [arXiv:2602.17634]：针对时序基础模型在零样本预测中计算资源与参数量扩张过快的问题，提出参数高效的时序基础模型计算缩放新范式 (Reverso)。通过倒置 Transformer (Inverted Transformer) 架构的结构精简与跨通道通道解耦，Reverso 证实通过合理的计算量重新分配与局部秩约束，仅需极小规模的可学习参数量即可在零样本跨域预测中匹敌甚至超越数十倍规模的标准庞大模型；
- **VLT 工业智能三模态基础模型** [arXiv:2607.14510]：针对工业 4.0 场景中物理装备状态由多维时序传感器、红外/光学视觉巡检图以及专家运维工单文本共同定义的复杂现实，提出首个面向工业智能的视觉-语言-时序三模态统一基础模型 (VLT)。VLT 设计了连续流形投影算子，将高频振动/温度遥测时序、机电表面裂纹热成像与非结构化故障日志映射至统一多模态隐式潜空间，在复杂工业装备故障预警与多任务联合推演中展现出强大的跨模态协同表征能力。

---
"""

part3 = r"""## 5 大语言模型赋能时序

除了构建原生时序架构，另一条极其繁荣的技术路线是直接利用 NLP 领域具有深厚预训练先验的现成大语言模型（如 LLaMA、GPT-2、GPT-4、Qwen）解决时序问题。大语言模型不仅在海量语料上掌握了丰富的通用序列模式、局部平滑性与自回归因果规律，还蕴含了关于物理现实、经济周期和人类行为的世界知识 (World Knowledge)。

### 5.1 大语言模型赋能时序范式矩阵与理论形式化

为了清晰界定各类 LLM-for-TS 方法的技术本质，下表给出了代表性方法的架构特性与实验开销对比：

| 模型/框架 | 基础大模型 | 范式类别 | 跨模态对齐机制 | 输入模态 | 可训练参数占比 | 核心亮点与任务泛化 | 计算开销与延迟 | arXiv 引用 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Time-LLM** | LLaMA-7B / GPT-2 | 模型重编程 | 线性补丁投影 + 文本 Prompt 前缀 + LoRA | TS + Text | ~1% - 3% | 文本领域前缀引导，长时预测精度顶尖 | 较高 (LLM 庞大隐藏层前向) | [arXiv:2310.01728] |
| **One Fits All (GPT4TS)**| GPT-2 (124M) | 极简重编程 | 仅微调输入 Patch 投影、位置编码与 LayerNorm | TS | < 0.1% | 极简架构，全任务通用 (预测/分类/异常检测) | 中等 (轻量级 GPT-2 骨干) | [arXiv:2302.11939] |
| **LLM4TS** | LLaMA-2 / GPT-2 | 两阶段重编程 | 阶段一两阶段时序自监督预训练，阶段二少样本对齐 | TS | ~1% | 数据利用效能高，少样本下游迁移稳健 | 较高 | [arXiv:2308.08469] |
| **T-LLM** | LLaMA / Mistral | 时序动力学蒸馏 | 从 TSFM 教师向 LLM 学生迁移连续时序动力学 | TS + Text | ~1.5% | 赋予通用语言大模型对时序物理动力学的敏锐理解 | 中等 | [arXiv:2602.01937] |
| **AutoTimes** | LLaMA-2-7B / OPT | 自回归语言适配 | 将 Patch 表示重构为自回归时序 Token，下一补丁自回归 | TS + Text | ~0.5% | 原生自回归语言建模，支持零样本与指令微调 | 较高 | [arXiv:2402.02370] |
| **LLMTime** | GPT-3 / GPT-4 / LLaMA | 文本化直接提示 | 逗号数值格式化，零样本直接概率外推提示 | TS (数值文本) | 0% (完全免训练) | 零训练成本，极佳的概率外推形态与柔性采样 | 极高 (逐点 Tokenization，上下文长度膨胀) | [arXiv:2310.07820] |
| **LSTPrompt** | 通用商业 LLM | 解耦直接提示 | 长短时特征文本分解提示 | TS + Text | 0% (免训练) | 显式解耦高频局部波动与低频趋势 | 较高 | [arXiv:2402.16132] |
| **CTRL** | LLM + 控制理论 | 控制论引导残差学习 | LLM 引导状态空间反馈与残差误差补偿 | TS + Text | < 1% | 控制理论稳定性保证与突变恢复 | 低 | [arXiv:2609.23257] |
| **MILM** | LLaMA / Mistral | 文本化与信息采样 | 结构化 XML 三元组 `<time, var, val>` + 信息性下采样 | 不规则时序 + 文本 | 0% - 1% | 突破等间隔采样假设，处理临床不规则多变量时序 | 中等 | [arXiv:2605.13711] |
| **LLM as Planner** | LLM + 专有时序模型 | 规划-执行双层协作 | LLM 提取文本事件与因果突变约束，引导 TSFM 回归 | TS + Text | 0% (免微调) | 规避 LLM 算术弱点，结合 TSFM 连续数值精度 | 中等 (仅需单次规划提示) | [arXiv:2607.24892] |
| **$\textbf{S}^2\textbf{IP-LLM}$** | GPT-2 / LLaMA | 语义空间提示微调 | 统计特征向语义原型空间投影 | TS + Text | ~1.5% | 语义连贯，抵抗高频噪声扰动 | 中等 | [arXiv:2403.05798] |
| **CALF** | LLaMA / GPT-2 | 跨模态微调 | 双分支时序-文本对比学习与特征蒸馏 | TS + Text | ~2% | 防止模态塌缩，跨模态表征对齐严格 | 较高 | [arXiv:2403.07300] |
| **TS-Reasoner** | LLaMA / Qwen | 认知推理对齐 | 连续时序特征与 LLM 链式思考 (CoT) 潜空间对齐 | TS + Text | ~2% | 融合因果推理与高精度数值预测 | 中等 | [arXiv:2510.03519] |
| **STReasoner** | Qwen-7B / LLaMA | 空间强化学习微调 | 时空图结构编码 + 空间感知强化学习 (S-GRPO) | TS+Text+Graph | ~5% (LoRA) | 复杂的时空因果拓扑推断与归因解释 | 较高 | [arXiv:2601.03248] |
| **Align-RAG** | 任意冻结 TSFM / LLM | 闭式检索自适应 | 闭式最小二乘最优仿射对齐 ($\alpha^*, \tau^*$) | TS | 0% (完全免训练闭式求解) | 零参数微调，检索示范即插即用 | 极低 (微秒级几何求解) | [arXiv:2608.05571] |
| **ChorusTIC** | 冻结大语言模型 | 提示合唱上下文学习 | 构造多通道上下文范例合唱提示 (Chorus Prompts) | TS (离散/数值) | 0% (完全免训练) | 免训练多变量零样本时序分类 | 中等 | [arXiv:2608.24033] |
| **Estimating Transferability**| 候选 TSFM 集合 | 在途上下文探针 | 目标域零样本在途对数似然增益差分子空间探测 | TS | 0% (探针式无更新) | 免微调秒级锁定最优预训练模型 | 极低 | [arXiv:2509.23695] |
| **PostTime** | Qwen / LLaMA | 后训练强化对齐 | 指令监督微调 (SFT) + 可验证奖励强化学习 (RLVR) | TS + Text | ~2% (LoRA) | 将大模型训练为数值 TSFM 的上下文修正器 | 较高 | [arXiv:2605.29401] |
| **R-AF** | 任意冻结 TSFM / 预测骨干 | 模型无关检索增强 | 无缝时序模式检索与长视野扩展外推 | TS | 0% (完全模型无关免重训) | 零重训将标准短视野模型扩展至长预测视野 | 极低 | [arXiv:2608.14054] |

#### 5.1.1 补丁重编程与子空间对齐形式化

模型重编程 (Model Reprogramming) 的数学本质是在不改变语言模型预训练注意力权重矩阵的前提下，学习一个跨流形仿射变换，将时序几何结构无缝映射到语言模型的隐藏流形上。
给定单变量时序 $\mathbf{x} \in \mathbb{R}^T$，经过步长为 $S$、长度为 $P$ 的补丁切分得到补丁序列 $\mathbf{p}_1, \dots, \mathbf{p}_N \in \mathbb{R}^P$。补丁投影器将其映射为语言模型的隐藏状态序列：
$$\mathbf{h}_i = \mathbf{W}_p \mathbf{p}_i + \mathbf{b}_p \in \mathbb{R}^{D_{\text{LLM}}}, \quad i=1,\dots,N$$
其中 $\mathbf{W}_p \in \mathbb{R}^{D_{\text{LLM}} \times P}$ 为可训练补丁线性投影矩阵。为了让语言模型理解当前时序的物理背景，系统构建自然语言领域前缀提示 $\mathbf{T}_{\text{prompt}}$（例如 `"This is a dataset about hourly electricity consumption..."`），并通过语言模型固有的词嵌入表 $\mathbf{E}_{\text{word}} \in \mathbb{R}^{V \times D_{\text{LLM}}}$ 编码为前缀嵌入：
$$\mathbf{E}_{\text{prompt}} = \text{Embed}(\mathbf{T}_{\text{prompt}}) \in \mathbb{R}^{L_{\text{prompt}} \times D_{\text{LLM}}}$$
将文本前缀与时序补丁隐藏状态在序列维度拼接，构造输入批次：
$$\mathbf{H}_{0} = [\mathbf{E}_{\text{prompt}}; \mathbf{h}_1; \mathbf{h}_2; \dots; \mathbf{h}_N] \in \mathbb{R}^{(L_{\text{prompt}} + N) \times D_{\text{LLM}}}$$
输入完全冻结的多层 Transformer 解码器：
$$\mathbf{H}_{\ell} = \text{TransformerBlock}_\ell(\mathbf{H}_{\ell-1}), \quad \ell=1,\dots,L$$
最后，取时序对应位置的输出状态，通过任务展平投射头 $\mathbf{W}_{\text{out}} \in \mathbb{R}^{H \times (N \cdot D_{\text{LLM}})}$ 还原为未来预测轨迹：
$$\hat{\mathbf{x}}_{T+1:T+H} = \mathbf{W}_{\text{out}} \text{vec}(\mathbf{H}_{L, [L_{\text{prompt}}+1:]}) \in \mathbb{R}^H$$

#### 5.1.2 闭式无训练检索对齐形式化 (Closed-Form In-Context Alignment: Align-RAG)

针对传统检索增强生成 (RAG) 往往需要训练笨重跨注意力适配器的问题，Align-RAG [arXiv:2608.05571] 提出了革命性的闭式几何对齐理论。
假设当前查询时序为 $\mathbf{q} \in \mathbb{R}^L$，其经验均值为 $\bar{q} = \frac{1}{L} \sum_{t=1}^L q_t$；从离线时序数据库中基于形状距离（如 DTW 或余弦相似度）检索出的最相似历史示范时序为 $\mathbf{r} \in \mathbb{R}^L$，其经验均值为 $\bar{r} = \frac{1}{L} \sum_{t=1}^L r_t$。
Align-RAG 证明，由于不同序列在物理尺度与直流偏置 (DC bias) 上的差异，直接拼接 $\mathbf{r}$ 会扰乱语言模型的上下文注意力。最优仿射对齐问题表述为寻找最优尺度缩放 $\alpha$ 与偏置位移 $\tau$：
$$\min_{\alpha, \tau} \left\| \mathbf{q} - (\alpha \mathbf{r} + \tau \mathbf{1}) \right\|_2^2$$
通过对 $\alpha$ 和 $\tau$ 分别求偏导并令其为 0，可求得唯一严格闭式最优解 (Closed-Form Analytical Solution)：
$$\alpha^* = \frac{\langle \mathbf{q} - \bar{q}\mathbf{1}, \mathbf{r} - \bar{r}\mathbf{1} \rangle}{\|\mathbf{r} - \bar{r}\mathbf{1}\|_2^2}, \quad \tau^* = \bar{q} - \alpha^* \bar{r}$$
将检索样本严格几何映射为 $\tilde{\mathbf{r}} = \alpha^* \mathbf{r} + \tau^* \mathbf{1}$，便可在**零参数训练、零梯度更新、微秒级开销**下完成时序流形重合，直接作为上下文示范送入任意冻结的 TSFM 或 LLM，释放极其强悍的上下文增强预测能力。

#### 5.1.3 免梯度在途可迁移性估计理论 (Transferability Estimation via ICL)

随着开源时序大模型激增，针对某一特定下游工业领域，如何从数十个候选模型 $\mathcal{M} = \{M_1, \dots, M_K\}$ 中快速挑选最适合迁移的模型？
金明团队在 [arXiv:2509.23695] 中提出首个基于上下文学习 (ICL) 的在途可迁移性估计理论。该理论指出，一个预训练模型在目标域上的微调潜力，与其在未见目标域上的在途上下文信息吸收率 (In-Context Information Assimilation Rate) 成单调正相关。
给定目标域中少量的未标注示范样本对 $\mathcal{D}_{\text{demo}} = \{(\mathbf{x}_{\text{ctx}}^{(m)}, \mathbf{x}_{\text{tgt}}^{(m)})\}_{m=1}^M$，定义模型 $M$ 在上下文条件下的对数似然增益差分探针：
$$\mathcal{S}_{\text{trans}}(M, \mathcal{D}_{\text{demo}}) = \frac{1}{M} \sum_{m=1}^M \left[ \log p_M(\mathbf{x}_{\text{tgt}}^{(m)} \mid \mathbf{x}_{\text{ctx}}^{(m)}, \mathcal{D}_{\text{demo} \setminus \{m\}}) - \log p_M(\mathbf{x}_{\text{tgt}}^{(m)} \mid \mathbf{x}_{\text{ctx}}^{(m)}) \right]$$
该指标完全无需对目标数据进行昂贵反向传播微调，仅需一次前向推断即可输出候选模型在目标域的适应性排序，在真实工业基准上与完全微调后的最终预测精度取得了高达 0.867 的斯皮尔曼秩相关系数 (Spearman Rank Correlation)。

---

### 5.2 模型重编程与轻量适配路线 (Model Reprogramming & Adapters)

模型重编程路线的核心优势在于能够以极小的数据量激活百亿参数大语言模型的泛化潜能：
- **Time-LLM** [arXiv:2310.01728]（金明组，ICLR 2024）：开创了时序领域的大模型重编程范式。通过设计时序补丁线性映射与词表子空间软对齐机制，结合自然语言任务前缀，使冻结的 LLaMA/GPT-2 展现出超越专属深度学习模型的少样本和零样本预测表现；
- **One Fits All (GPT4TS)** [arXiv:2302.11939]（阿里达摩院，NeurIPS 2023 Spotlight）：提出了令人瞩目的极简性实验——彻底冻结 GPT-2 的多头自注意力层与 MLP 层，仅微调补丁线性投影层与 LayerNorm（可训练参数占比不到 0.1%），却在时间序列预测、分类、异常检测、缺失插补全套任务中同时取得顶尖表现。这强有力地证实了预训练 Transformer 的注意力矩阵蕴含着对通用序列连续拓扑的通用偏置；
- **LLM4TS** [arXiv:2308.08469]：进一步提出两阶段渐进式对齐，首先在混合时序语料库上对投影层进行自监督预训练以匹配时序统计矩，随后在目标领域进行轻量微调，显著缓解了小样本场景下的过拟合；
- **T-LLM** [arXiv:2602.01937]（Guo & Wang 等）：针对现有 LLM 直接处理时序时欠缺物理动力学先验的问题，提出基于**时序知识蒸馏 (Temporal Distillation)** 的教学框架。T-LLM 利用在海量时序语料上预训练的高精度专属 TSFM 作为“教师网络”，将连续隐空间的状态转移矩阵与频域特征蒸馏注入大语言模型（学生网络），使通用大模型在保留丰富世界知识的同时，原生习得高阶时序连续性与波动敏感度；
- **UniTime** [arXiv:2310.09751] 与 **TEMPO** [arXiv:2310.04948]：引入跨域多任务通用指令微调，使模型能够根据文本提示动态调整对不同频段和趋势周期的捕获敏感度；
- **CoRA** [arXiv:2510.12681]（THUML）：设计基于 Granger 因果嵌入与零初始化条件注入机制的通用协变量适配框架，将外生多模态上下文无损注入冻结的基础模型。

### 5.3 文本化分词与直接提示路线 (Direct Prompting & Reasoning Planners)

如果不训练任何映射层，大语言模型能否直接理解时间序列？答案是肯定的：
- **PromptCast** [arXiv:2210.08964]：最早尝试将数值序列以问答字符串形式输入语言模型；
- **LLMTime** [arXiv:2310.07820]（NeurIPS 2023）：深入分析了现有大语言模型（如 GPT-3/GPT-4、LLaMA-2）直接外推连续数值的机理。研究发现：**当使用逗号进行分隔，并将连续浮点数严格按固定有效数字格式化后，未经任何时序训练的 LLM 展现出惊人的零样本概率预测能力**。其输出的蒙特卡洛多样本自回归采样不仅能自动捕捉季节性、趋势拐点，还能表达非对称的多峰后验分布；
- **CTRL** [arXiv:2609.23257]（Kim & Ji 等）：针对传统直接提示中大模型容易产生算术幻觉导致预测发散的痛点，创新性地将**现代控制理论 (Modern Control Theory)** 与 LLM 深度结合。CTRL 将预测过程建模为状态空间闭环反馈控制系统，由基础线性状态模型提供稳定的名义基线预测，由大语言模型充当监督控制器动态预测环境扰动残差，并通过引入严格的李雅普诺夫稳定性界限，数学上杜绝了大模型幻觉造成的轨迹失稳；
- **MILM** [arXiv:2605.13711]（Chung 等）：针对临床电子病历等高度不规则采样、多变量严重异步缺失的极端时序，提出将时序转化为结构化 XML 三元组序列 `<time, variable, value>`。结合信息性重要度采样算法过滤冗余测量，使大语言模型能够原生处理不规则多模态连续物理事件；
- **LSTPrompt** [arXiv:2402.16132]：针对直接提示中长序列容易导致注意力稀释的缺陷，提出长短时记忆解耦提示范式，引导大模型分步推导高频微扰与长期基线；
- **LLM as Forecasting Planner** [arXiv:2607.24892]：系统反思了让 LLM 直接输出长串数值的内在缺陷（算术计算脆弱性、高昂的 Token 费用与高延迟），创新性地提出“大模型负责定性规划、时序小模型负责数值定量回归”的双层协作架构。利用冻结的 LLM 解析宏观文本事件、重大节假日与趋势突变，输出规划约束参数，再由轻量级 TSFM 执行连续数值生成，实现了高精度与低计算开销的优雅统一。

### 5.4 跨模态微调与跨语义空间对齐 (Cross-Modal Fine-Tuning & Semantic Alignment)

为了消除时序连续数值与文本离散语义之间的语义断层 (Semantic Gap)，跨模态对齐技术通过对比学习或原型投影实现表征统一：
- **$\textbf{S}^2\textbf{IP-LLM}$** [arXiv:2403.05798]：引入语义空间引导的提示学习，将时序的统计矩（均值、方差、偏度、自相关系数）投射到文本语义连贯的原型空间，消除噪声干扰；
- **CALF** [arXiv:2403.07300]：提出双分支跨模态微调机制，一条分支处理文本描述，另一条分支编码时序补丁，通过跨模态 InfoNCE 损失进行特征蒸馏，有效防止微调过程中大模型的知识表征发生塌缩；
- **TS-Reasoner** [arXiv:2510.03519]（Yu & Zhao 等）：提出将时序基础模型与大语言模型认知推理深度对齐的新架构。TS-Reasoner 构建了数值表征与推理表征的双向投射通道，使基础模型生成的隐式动态模式能够被映射为 LLM 思维链 (CoT) 中的逻辑因果词元，不仅显著提升了复杂分布突变下的外推精度，更首次实现了对预测结果的自动化自然语言归因与置信度解释；
- **AutoTimes** [arXiv:2402.02370]（清华 THUML，NeurIPS 2024）：设计自回归时序分词与提示对齐策略，直接将连续时序补丁视为一种新语言方言 (Dialect)，使大规模语言模型无需任何结构性破坏，即可原生以自回归语言建模方式输出未来预测补丁；
- **STReasoner** [arXiv:2601.03248]（金明组，ACL 2026）：针对城市计算与物理传感器网络中普遍存在的时空图拓扑结构，构建了包含实体关联与拓扑传播的 ST-Bench，并提出基于空间感知强化学习算法 S-GRPO，使大语言模型能够显式联合推导时空拓扑演化因果链，完成高阶时空推理。

### 5.5 上下文学习、检索增强与零样本迁移度量 (In-Context Adaptation & Transferability)

大语言模型的强大不仅体现在参数内部知识，更在于其灵活的在途上下文适应能力：
- **Align-RAG** [arXiv:2608.05571]：打破了时序检索增强必须端到端训练神经网络融合器的固有思维，通过闭式求解最优幅度缩放因子 $\alpha^*$ 与时移偏差 $\tau^*$，以纯数学闭式解实现了跨序列几何对齐，将检索到的高质量历史范例直接送入冻结 TSFM，在零参数训练下取得显著泛化增益；
- **ChorusTIC** [arXiv:2608.24033]：提出基于“合唱上下文学习 (Chorus In-Context Learning)”的免训练多变量时序分类范式。该方法将多变量序列转化为结构化多通道提示合唱，通过大模型内生序列注意力机制进行多视角投票，实现了无需微调的高鲁棒性分类；
- **Estimating TSFM Transferability** [arXiv:2509.23695]（金明组）：提出首个基于无标注在途上下文探针量化基础模型可迁移性的理论方法，在无需进行昂贵梯度训练的前提下，秒级准确预估不同预训练大模型在特定下游任务的微调收益；
- **LLM-Mixer** [arXiv:2410.11674]：探索将多尺度分解与混合层深度内嵌至 LLM 的中间隐层，提升长程复杂周期信号的自适应外推能力；
- **In-context Time Series Predictor** [arXiv:2405.14982]：通过在上下文中优雅堆叠少量输入-输出时序对示范 (Few-shot Demonstrations)，探索了纯粹免梯度的在途时序推理能力；
- **时序检索增强有效性临界区间研究 (When Does Retrieval Help?)** [arXiv:2609.20193]（Kurban 等）：针对学术界盲目引入检索增强 (RAG) 的倾向，该研究首次对时序检索增强机制进行了严密实证审计。研究指出了时序 RAG 产生正收益的**临界操作区间 (Critical Operating Regime)**：检索增益由目标序列的平稳性与检索库覆盖率决定；当历史上下文长度充足时，模型自身注意力已能有效捕捉周期，强行检索相似片段反而因“模式相位饥饿 (Phase Starvation)”诱发负向干扰；研究提出了自适应检索触发准则，代码经由 GitHub API 严格核验；
- **模型无关检索增强长视野预测 (R-AF)** [arXiv:2608.14054]：针对现有预训练基础模型预测视野 $H$ 往往在架构上被静态固定（如固定输出 96 或 128 步）的应用瓶颈，提出模型无关检索增强长视野预测框架 (Model-agnostic Retrieval-Augmented Extended Forecasting, R-AF)。R-AF 无需对底层预训练模型进行重新微调，通过以模型的初步短程预测轨迹为查询锚点，在离线历史库中快速检索拓扑对齐的长程动态延伸片段并进行最优仿射拼接，以纯外源增强机制成功将任意标准短视野 TSFM 的有效预测范围扩展数倍。

### 5.6 时序后训练理论与强化学习对齐 (Post-Training & Reinforcement Learning Alignment)

随着基础模型进入垂直落地阶段，预训练模型的泛化能力必须通过精细的后训练 (Post-Training) 进行引导与对齐：
- **时序基础模型后训练统一框架** [arXiv:2607.20002]（Xie et al.）：首次系统建立了涵盖指令监督微调 (SFT)、直接偏好优化 (DPO)、强化学习 (RLHF/RLAIF) 以及参数高效微调 (PEFT) 的时序后训练理论体系。综述指出，与自然语言离散 Token 奖励不同，连续时序的强化学习受制于轨迹平滑度、极值惩罚与时空物理规律一致性；
- **PostTime 强化后训练配方** [arXiv:2605.29401]（Liu 等）：针对多模态时序微调容易破坏预训练数值先验的问题，提出结合 SFT 与可验证奖励强化学习 (Reinforcement Learning with Verifiable Rewards, RLVR) 的两阶段后训练范式。将大语言模型训练为数值时序基础模型输出先验的文本上下文修正器，在多模态基准上显著超越端到端微调；
- **真实邻域正则化强化学习后训练** [arXiv:2608.08010]：针对时序强化学习在连续动作空间下容易发生“策略崩塌 (Policy Collapse)”与灾难性发散的痛点，创新提出基于真实轨迹局部几何邻域正则化 (Ground-Truth Neighborhood Regularization) 的策略优化目标：
  $$\mathcal{L}_{\text{RL-Reg}}(\theta) = \mathcal{L}_{\text{PPO}}(\theta) + \lambda \mathbb{E}_{\mathbf{x} \sim \mathcal{D}, \mathbf{y} \sim \pi_\theta} \left[ \min_{\mathbf{y}^* \in \mathcal{B}_\epsilon(\mathbf{y}_{\text{gt}})} \|\mathbf{y} - \mathbf{y}^*\|_2^2 \right]$$
  其中 $\mathcal{B}_\epsilon(\mathbf{y}_{\text{gt}})$ 定义了围绕真实时序轨迹的 $\epsilon$-光滑邻域流形。这一正则项有效约束了策略梯度的探索边界，在能源网格调度与工业交通拥堵控制中，彻底消除了传统 PPO 策略退化到平凡常数输出的顽疾，实现了高奖励与物理合理性的稳健兼顾。

---
"""

part4 = r"""## 6 多模态时序与智能体演进

随着现实场景从单一数值传感向复合感知升级，多模态时序融合与智能体自主决策在 2025-2026 年成为最具突破性与战略价值的演化前沿。现实物理系统（如复杂电网、重化工业装备、金融交易网络与具身机器人）绝非单纯孤立的数字波形，而是时刻与专家运维日志、环境突发事件、遥测图表及宏观多智能体博弈深度交织。

### 6.1 多模态时序与智能体系统对比矩阵

为了全面刻画多模态时序与智能体系统的设计哲学与能力边界，下表对比了 21 种前沿代表性系统的技术参数、模态构成与演化机制：

| 系统/模型 | 代表机构/文献 | 发布年份 | 模态构成 (Modality) | 跨模态核心机制 (Mechanism) | 智能体决策/自进化机制 | 典型适用场景 | 权重/代码开源 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Time-LLM** | 金明团队 [arXiv:2310.01728] | 2023 | TS + Text | 补丁线性投射 + 文本 Prompt 前缀引导 | 静态提示引导 | 通用长短程时序预测 | 开源 (权重与代码) |
| **One Fits All** | 阿里达摩院 [arXiv:2302.11939] | 2023 | TS | 冻结 GPT-2 + 微调输入投影与 LN | 无智能体调用 | 跨任务极简轻量基准 | 开源 |
| **OpenTSLM** | 学术团队 [arXiv:2510.02410] | 2025 | TS + Text | 医疗生命体征 Patch + 临床病历交叉注意力 | 临床推断问答 | ICU 重症监护与病情恶化预警 | 开源 |
| **ChatTime** | 浙大团队 [arXiv:2412.11376] | 2024 | TS + Text | 时序离散分词 + 语言模型联合微调 | 对话式预测意图解析 | 交互式对话时序探索 | 开源 |
| **EventCast** | 金明团队 / 阿里 [arXiv:2602.07695] | 2026 | TS + Text (电商事件) | 混合需求预测 + LLM 事件知识图谱提取 | 事件驱动混合推断 | 电商大促与突发需求尖峰预测 | 论文声明 |
| **TimeBraid** | 学术团队 [arXiv:2609.29792] | 2026 | TS + Text | 57页深度编织交错全局残差注意力 | 统一因果问答与时序生成推演 | 通用多模态因果分析与生成 | 开源 |
| **Chronicle** | 学术团队 [arXiv:2605.20268] | 2026 | TS + Text | 324M 原生语言-时序统一 Decoder-only 架构 | 统一联合因果生成 | 通用跨模态时序-语言理解与预测 | 开源 |
| **SCENARIODIFF**| 学术团队 [arXiv:2608.17164] | 2026 | TS + Text | 多模态扩散 Transformer + 场景-锚点分层引导 | 分层情景引导推演 | 突发新闻与宏观事件驱动的时序预测 | 开源 |
| **VisionTS** | 学术团队 [arXiv:2408.17253] | 2024 | TS + Vision | 1D 折线图渲染 + Visual MAE 掩码重建 | 视觉隐式模式识别 | 免预训练零样本直观外推 | 开源 |
| **Time-VLM** | 学术团队 [arXiv:2502.04395] | 2025 | TS + Text + Vision | 三模态对比流形对齐空间 | 视觉图表与文本协同推断 | 工业图表多模态分析 | 论文声明 |
| **TimeOmni-VL** | 金明团队 [arXiv:2602.17149] | 2026 | TS + Text + Vision | 全模态统一嵌入流形 + 动态跨模态门控 | 复杂跨模态链式推理 (CoT) | 复合工业时空环境全息感知 | 开源 |
| **DiTS** | 清华 THUML [arXiv:2602.06597] | 2026 | TS + Multimodal | Diffusion Transformer 多模态空间自注意力 | 条件引导逆扩散采样 | 高维不规则多模态时序生成 | 开源 |
| **GALA** | 学术团队 [arXiv:2608.13741] | 2026 | TS + Text | 生成感知跨模态对齐 + 条件扩散生成 | 文本条件驱动的时序受控合成 | 文本引导时序生成与数据增强 | 开源 |
| **CastFSR** | 陶晓宇等 [arXiv:2608.03031] | 2026 | TS + Text | 快慢思考双系统 (Fast-Slow-Reflect) 智能体 | 在线自我反思与残差校准 | 复杂多变上下文时序自适应外推 | 开源 |
| **TimeRLM** | 学术团队 [arXiv:2608.03391] | 2026 | TS + Text | 递归语言模型 (Recursive Language Model) | 递归下采样与多尺度聚焦定位 | 超长上下文时序精准异常定位 | 论文声明 |
| **ReasonCast** | 学术团队 [arXiv:2608.15291] | 2026 | TS + Text | 波动感知选择性大模型推理门控 | 动态评估何时触发重型 LLM 思考 | 供应链不稳定突发需求预测 | 开源 |
| **TS-Debate** | KAIST 团队 [arXiv:2601.19151] | 2026 | TS + Text + Vision | 数值/视觉/文本多智能体协作抗辩协议 | 推理期多角色多轮抗辩协作 | 复杂多模态零样本时序推理 | 论文声明 |
| **ChatAD** | 金明团队 [arXiv:2601.13546] | 2026 | TS + Text | 8B 推理大模型 + 多轮指令演化微调 | 多轮排查深挖故障根因链条 | 复杂工业装备故障多轮诊断 | 开源 |
| **TimEvolve** | 学术团队 [arXiv:2609.24862] | 2026 | TS + Agent | 部署即监督 + 延迟真实反馈在线反思 | 在线更新专家信任度与干预策略 | 开放动态环境持续时序决策 | 开源 |
| **LLM-Agent Survey**| 徐晓刚等 [arXiv:2608.23058] | 2026 | 综述全景 | 感知、规划、工具使用与反思系统化分类 | 系统化梳理训练与评测前沿 | 全场景时序智能体系统 | 综述 |
| **FactoryNet** | 学术团队 [arXiv:2605.09081] | 2026 | 6类物理机电时序 | 5100万点机床/机械臂/冲压多通道遥测 | 跨具身实体零样本物理迁移 | 具身工业设备控制与预测维护 | 开源 |
| **LLM Agents Survey**| Salesforce / 徐晓刚等 [arXiv:2608.26226] | 2026 | 综述全景 | 智能体感知、规划、工具调用与反思分类谱系 | 智能体自主工作流与评价基准 | 全场景时序任务 | 综述 |
| **MetaCaster** | 学术团队 (EMNLP 2026) [arXiv:2608.23473] | 2026 | TS + Text | Meta-Harness 优化智能体框架 | 自适应超参数与提示词元演化 | 少样本轻量级时序预测 | 论文声明 |
| **CompEvo** | 学术团队 [arXiv:2609.09195] | 2026 | TS + Text (新闻) | 竞争诱导多智能体演化 (Competition-Induced Evolution) | 多智能体博弈竞争与策略自适应演化 | 新闻驱动高波动时序预测 | 开源 |
| **Human-in-the-Loop Agent** | 工业学术团队 [arXiv:2608.30976] | 2026 | TS + Text | 人机协同闭环交互智能体 | 专家知识反馈与置信度自适应介入 | 工业关键制造与设备预测 | 论文声明 |
| **TimeClaw** | iDEA-iSAIL Lab [arXiv:2606.05404] | 2026 | TS + Text | 通用智能体工具编排与执行引擎 | 动态工具调用与上下文推理 | 上下文丰富的现实复杂时序问答与预测 | 开源 (GitHub 官方核验) |
| **TSQAgent** | 学术团队 [arXiv:2606.03629] | 2026 | TS + Text | 专属时序数据质量智能体推理链 | 多维度质量缺陷分层排查与评分 | 工业与科研时序数据清洗与质量评级 | 论文声明 |
| **T-SMART** | 学术团队 (ICTAI 2026) [arXiv:2609.14142] | 2026 | TS + Text | 机制级归因工具增强 QA 架构 | 工具链机制级追溯与因果归因 | 工具增强时序问答与反思归因 | 论文声明 |
| **VLT** | 工业智能学术团队 [arXiv:2607.14510] | 2026 | TS + Text + Vision | 视觉-语言-时序三模态统一特征对齐 | 工业场景跨模态协同推断 | 复杂工业装备智能运维与多模态决策 | 论文声明 |
| **SAGE** | 学术团队 [arXiv:2608.26829] | 2026 | TS + Text + Vision | 变量级语义增强 (Variate-Wise Augmentation) | 细粒度变量语义引导多模态融合 | 视觉-语言引导的多变量时序预测 | 论文声明 |
| **Solar-Sky-TS** | 学术团队 [arXiv:2609.11135] | 2026 | TS + Text + Vision | 双向天空图像与光伏数值时序多模态融合 | LLM 跨模态上下文协同生成与预测 | 光伏电站太阳能辐射与发电量预测 | 论文声明 |

---

### 6.2 文本与时序跨模态推理与扩散生成 (Text + TS Joint Reasoning & Diffusion Synthesis)

在许多高价值领域，纯数值时序不足以揭示突发的外部扰动。将领域文本、突发新闻、专家运维记录与物理数值进行端到端协同建模，是破除“时序冷启动与黑天鹅预测失误”的核心利刃：

#### 6.2.1 57 页深度大一统模型：TimeBraid 架构与损失形式化

长达 57 页的长篇巨制 **TimeBraid** [arXiv:2609.29792] 宣告了时间序列与自然语言真正走向底层大一统。不同于以往通过浅层投影层或外挂 LoRA 的粗暴拼接，TimeBraid 提出了**交错全局残差注意力机制 (Interleaved Global Residual Attention)**，在模型的每一个主干层内同时编织时序连续动力学和语言因果逻辑。

令输入多变量时序为 $\mathbf{X}_{\text{ts}} \in \mathbb{R}^{T \times C}$，相关联的多轮文本序列为 $\mathbf{X}_{\text{text}}$。在经过各自初级 Patch 嵌入层与词词嵌入层后，得到第 0 层状态 $\mathbf{H}_{\text{ts}}^{(0)} \in \mathbb{R}^{N \times D}$ 和 $\mathbf{H}_{\text{text}}^{(0)} \in \mathbb{R}^{M \times D}$。在第 $\ell$ 层编织层中：
$$\mathbf{H}_{\text{ts}}^{(\ell)} = \text{TS-Block}^{(\ell)}\left(\mathbf{H}_{\text{ts}}^{(\ell-1)}\right) + \alpha_\ell \cdot \text{CrossAttn}_{\text{ts}\to\text{text}}\left(\mathbf{H}_{\text{ts}}^{(\ell-1)}, \mathbf{H}_{\text{text}}^{(\ell-1)}\right)$$
$$\mathbf{H}_{\text{text}}^{(\ell)} = \text{LM-Block}^{(\ell)}\left(\mathbf{H}_{\text{text}}^{(\ell-1)}\right) + \beta_\ell \cdot \text{CrossAttn}_{\text{text}\to\text{ts}}\left(\mathbf{H}_{\text{text}}^{(\ell-1)}, \mathbf{H}_{\text{ts}}^{(\ell)}\right)$$
其中 $\alpha_\ell, \beta_\ell \in [0, 1]$ 为可学习的层级自适应流形门控因子。
整个框架采用统一多任务联合优化损失：
$$\mathcal{L}_{\text{TimeBraid}} = \mathcal{L}_{\text{AR}}(\theta_{\text{text}}) + \lambda_{\text{ts}} \mathcal{L}_{\text{MSE}}(\theta_{\text{ts}}) + \lambda_{\text{align}} \mathcal{L}_{\text{Contrastive}}(\mathbf{H}_{\text{ts}}^{(L)}, \mathbf{H}_{\text{text}}^{(L)})$$

- **Chronicle** [arXiv:2605.20268]（Quinlan 等）：提出了包含 **324M 参数** 的统一跨模态时序基础模型。Chronicle 完全从零开始在自然语言与时间序列的大规模混合语料库上训练 Decoder-only Transformer，避免了继承已有 LLM 的算术偏误，在跨模态图文问答与时序生成推演中展现出强大的原生因果协同理解能力；
- **SCENARIODIFF** [arXiv:2608.17164]（Tran 等）：提出场景级引导扩散预测框架 (Scenario-level Guidance Diffusion)。该方法将长篇宏观报告与突发新闻自动解构为宏观场景假设与局部时间锚点 (Anchors)，通过多模态扩散去噪过程实现高保真受控合成，极大抑制了极端外生事件冲击下的预测震荡；
- **EventCast** [arXiv:2602.07695]（金明团队 / 阿里等）：针对电子商务平台中大促营销、直播秒杀与宏观政策事件所导致的极端需求尖峰难题，提出结合大语言模型事件知识图谱的混合需求预测体系 (EventCast)。EventCast 首先利用 LLM 从海量非结构化运营文本中抽取事件类型、优惠力度与时效窗口，随后构建事件-商品混合图注意力网络，与数值时序骨干进行协同前向推断，大幅压降了电商平台的突发缺货率与库存积压成本。

#### 6.2.2 生成感知跨模态对齐扩散合成 (GALA)

在受控时序合成与仿真领域，**GALA** [arXiv:2608.13741]（Generation-Aware Cross-Modal Alignment）揭示了一个深刻的理论现象：传统的 CLIP 式对比学习仅对齐了时序和文本的静态投影嵌入，当将其作为条件引导连续扩散模型去噪时，由于扩散过程涉及多步时变速度场，静态嵌入无法在不同噪声时间步 $t \in [0, 1]$ 上维持动态因果一致性。
为了解决这一难题，GALA 提出了生成感知对齐机制：
$$\mathcal{L}_{\text{GALA}}(\theta) = \mathbb{E}_{t, \mathbf{x}_0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(\mathbf{x}_t, t, \mathbf{c}_{\text{text}}) \|^2 \right] + \gamma \mathcal{L}_{\text{Trajectory-Align}}(f_\theta(\mathbf{x}_t, t), \mathbf{e}_{\text{text}})$$
通过在扩散逆向轨迹的所有中间步上强力约束生成流形与文本语义的几何夹角，GALA 能够精准受控生成符合极复杂文本叙述的极端故障波形（如“轴承在第 200 秒突现 3 次周期性剥落高频冲击，随后平稳收敛”），为工业机电数据合成提供了强大基座。

#### 6.2.3 虚拟时序语义通道与行业复合系统

在非侵入式语义注入方面：
- **TAC-Time** [arXiv:2609.24156] 与 **TRACE** [arXiv:2606.06285]：提出“文本即虚拟通道 (Text-as-Channel)”理念，将非结构化自然语言事件直接转化为一维连续虚拟传感器通道，使任何标准原生 TSFM 无需任何架构修改即可感知宏观事件；
- **FINESSE** [arXiv:2609.11993]：摩根士丹利团队构建的首个多模态金融事件序列大模型与仿真基准，融合宏观财经快讯、财报电话会音频文本与微观毫秒级订单簿；
- **SciTS** [arXiv:2510.03255]：面向射电天文脉冲星搜寻、材料晶体衍射等复杂科研时序的多模态理解大模型。

---

### 6.3 视觉与时序跨模态协同 (Visual Time Series & Temporal VLMs)

人类时序分析专家在研判心电图、股票 K 线或地震波形时，往往依赖高度直观的“折线图看图思维”。近年来，将计算机视觉与视觉语言模型 (VLMs) 引入时序领域展现出极具潜力的跨模态协同效应。

#### 6.3.1 一维时序到二维画面的连续流形渲染算子 $\Phi_{\text{render}}$

为了将连续一维数值 $\mathbf{x}_{1:T} \in \mathbb{R}^T$ 转换为计算机视觉模型可直接处理的图像张量 $\mathbf{I} \in \mathbb{R}^{H \times W \times 3}$，学术界形式化了连续折线渲染算子 $\Phi_{\text{render}}$：
令归一化坐标点集为 $\mathcal{P} = \left\{ \left( \frac{t-1}{T-1} \cdot (W-1), \frac{x_t - x_{\min}}{x_{\max} - x_{\min}} \cdot (H-1) \right) \right\}_{t=1}^T$。图像在像素坐标 $(u, v)$ 处的强度值由点到分段折线段的高斯距离场决定：
$$\mathbf{I}(u, v) = \exp \left( - \frac{\min_{t} \text{dist}\left( (u, v), \text{Segment}(\mathcal{P}_t, \mathcal{P}_{t+1}) \right)^2}{2 \sigma_{\text{stroke}}^2} \right)$$
其中 $\sigma_{\text{stroke}}$ 控制线条抗锯齿笔触粗细。

#### 6.3.2 代表性视觉时序模型演进

- **VisionTS** [arXiv:2408.17253]（NeurIPS 2024）：实验表明，将一维时序通过 $\Phi_{\text{render}}$ 渲染为灰度折线图后，直接输入在纯自然图像上预训练、**未经任何时序微调**的掩码自编码器 (Visual MAE)，利用其填补未来遮挡图像区域并求逆映射 $\Phi_{\text{render}}^{-1}$，其零样本预测误差竟然击败了大量精心设计的专有时序模型，引发了关于“时序模式识别本质是否即局部几何视觉模式”的学术大讨论；
- **Time-VLM** [arXiv:2502.04395] 与 **TimeOmni-VL** [arXiv:2602.17149]（ICML 2026）：构建了时序-文本-视觉三模态大模型，支持直接输入折线图进行图表异常圈注、因果解释与未来外推；
- **DiTS** [arXiv:2602.06597]（清华 THUML，2026）：首次将计算机视觉中顶级的 Diffusion Transformer (DiT) 架构迁移至多模态高维时序生成，利用 2D 空间自注意力机制全面捕捉时空多变量之间的复杂隐式拓扑；
- **Empowering VLMs for TS** [arXiv:2605.09395] 与 **TimeVista** [arXiv:2606.16173]：验证了经过视觉对齐的 VLM 可以作为公正的“多模态视觉裁判 (VLM-as-a-Judge)”，以超越传统 MSE 的高层次形态保真度标准评估时序预测；
- **SAGE 变量级语义增强多模态预测** [arXiv:2608.26829]：针对视觉-语言多模态时序模型在多变量场景下往往将所有传感器通道混杂渲染、导致通道间语义相互干扰的缺陷，提出变量级语义增强框架 (Variate-Wise Semantic Augmentation, SAGE)。SAGE 为每个独立时间序列变量建立细粒度语义绑定与视觉独立通道投影，从根本上消除了跨变量虚假关联，显著提升了高维工业传感器系统的视觉-语言联合预测精度；
- **Solar-Sky-TS 地空双向多模态协同预测** [arXiv:2609.11135]：针对太阳能光伏发电极易受局部云层流动与突变遮挡影响的难题，构建了首个将全天空成像仪 (Total Sky Imager) 动态鱼眼云图与地面微秒级辐照度时间序列进行双向跨模态融合的大语言模型预测架构。通过在大语言模型内部建立地空双向流形注意力，使模型能够同时从宏观云层流体力学演化和微观辐射数值中联合外推未来光伏发电功率。

---

### 6.4 交互式流式时序与自进化智能体决策 (Interactive TS & Self-Evolving Agents)

传统的时序模型多属于“静态被动式推断”——给定上下文窗口，吐出预测值后推断立即终止。然而工业智能与运筹决策要求系统具备主动提问、工具调用、长期记忆反思与在线自进化的智能体能力。

#### 6.4.1 时序决策智能体的 POMDP 理论形式化

交互式时序智能体在现实物理环境中的决策过程可严格形式化为部分可观测马尔可夫决策过程 (Partially Observable Markov Decision Process, POMDP)：
$$\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \Omega, \mathcal{O}, \gamma \rangle$$
- **物理真实状态 $s_t \in \mathcal{S}$**：包含真实连续物理系统内部不可直接完全测量的动态变量（如轴承微观磨损程度、地下储油层压力、宏观暗流流动性）；
- **观测空间 $o_t \in \Omega$**：包含当前滑动窗口时序 $\mathbf{X}_{t-L:t}$、离散系统告警事件、文本运维日志 $\mathbf{Z}_t$；
- **动作空间 $a_t \in \mathcal{A}$**：智能体的动作集高度复合，包含：(1) 调用 TSFM 执行滚动预测；(2) 检索离线图谱或执行因果排查；(3) 向人类工程师发出高危告警与处置建议；(4) 触发物理阀门控制或电力备用机组启动；
- **奖励函数 $r_t = \mathcal{R}(s_t, a_t)$**：平衡预测误差惩罚、工具调用 FLOPs/API 经济开销、误报惩罚与灾难性物理停机防范收益。

#### 6.4.2 智能体抗辩协议与快慢反思推理机制

- **CastFSR 快慢反思智能体框架** [arXiv:2608.03031]（陶晓宇、程明月等）：提出受认知心理学双系统理论启发的快慢反思智能体框架 (CastFSR)。系统划分出“快思考 (Fast System)”与“慢思考 (Slow System)”：快系统调用轻量级时序模型执行低延迟滚动外推；当系统监测到高不确定性或环境突发相变时，唤醒慢思考智能体调用大语言模型进行因果推理与外部知识检索；核心的“反思模块 (Reflect Module)”持续比对推断轨迹与后续展开的真实值，执行事后残差归因并动态重构后续提示词约束，在复杂多变环境下展现出卓越的自适应能力；官方开源代码已由 GitHub API 严格核验；
- **TimeRLM 递归语言模型** [arXiv:2608.03391]（Zumarraga 等）：针对工业多变量百万步长历史序列中极难定位的针尖式微弱异常，提出递归语言模型 (Recursive Language Model, TimeRLM)。通过分层递归下采样与多尺度注意力聚焦机制，TimeRLM 突破了传统大模型上下文长度限制，以线性复杂度实现对长程时序高精度异常区间的毫秒级精准定位；
- **时序预测大模型智能体系统综述** [arXiv:2608.23058]（徐晓刚、唐家奇等）：首次对面向预测与推断任务的 LLM 智能体系统进行了系统性回顾与分类。综述将时序智能体系统解构为“环境感知、任务规划、工具调用执行与反思进化”四层架构，系统梳理了监督对齐、强化学习自适应策略与实际工业落地的关键评价基线；
- **Salesforce 时序大模型智能体系统综述 (Findings of EMNLP 2026)** [arXiv:2608.26226]（Salesforce Moirai 团队与学术界联合发布）：全面系统地回顾了 LLM 赋能时序智能体的最新进展。综述确立了时序智能体的统一认知框架，系统解构了多轮推理、外部工具链编排、动态反思与环境闭环反馈机制；
- **MetaCaster 元演化智能体 (EMNLP 2026)** [arXiv:2608.23473]：提出 Meta-Harness-Optimized 智能体框架，利用元学习机制动态搜索并优化轻量级时序模型的提示词与微调参数，在极端少样本工业预测场景下实现了极高的精度与收敛速度；
- **CompEvo 竞争诱导演化多智能体系统** [arXiv:2609.09195]：针对突发新闻驱动下的高波动时序（如大宗商品与金融衍生品），构建了基于博弈论的竞争演化机制。不同智能体分别扮演多头、空头与风险精算师，通过市场竞争博弈推动预测假设的自主迭代与优胜劣汰；
- **TS-Debate 多智能体协作辩论** [arXiv:2601.19151]（Trirat 等，EMNLP 2026）：提出在推理期引入数值专家、视觉图表专家与文本因果专家进行多轮结构化协作辩论协议 (TS-Debate)。单一模态智能体容易受到局部噪声误导，而通过跨模态智能体之间的交叉质疑、证据质询与置信度校准，系统在无需参数微调的前提下极大提升了复杂现实时序案例的零样本推理准确度；
- **ReasonCast 波动感知选择性推理** [arXiv:2608.15291]：设计了轻量级的波动与突变检测门控 $g_t \in \{0, 1\}$，平稳期仅由轻量 TSFM 执行惯性外推，突变时唤醒重型 LLM 智能体介入因果推导，**节约超 70% 的计算算力开销**。

#### 6.4.3 工业根因演化排查与闭环自进化架构

- **ChatAD** [arXiv:2601.13546]（金明团队）：构建了具备 80 亿参数 (8B) 的时序异常推理智能体。通过多轮指令演化 (Multi-Turn Instruction Evolution) 技术，在数十个关联传感器通道间多轮深挖设备跳闸的物理诱因；
- **TimEvolve** [arXiv:2609.24862]：提出“部署即监督 (Deployment-is-Supervision)”的自进化智能体，利用系统随时间推进自然显现的真实观测在线计算累积遗憾 (Temporal Regret)，动态更新不同预测专家与 LLM 之间的信任权重；
- **人机协同自主工业预测智能体 (Human-in-the-Loop Agent)** [arXiv:2608.30976]：在重工业与能源调度中，纯自主智能体可能引发失控风险。该系统建立了人机协同 (Human-in-the-Loop) 双层治理架构，智能体在低置信度或相变突变期主动向领域专家呈现因果图并请求关键决策确认，实现了高自治度与工业安全生产的完美平衡；
- **AION** [arXiv:2605.25045]（金明团队）：开创了“自主科研智能体 (Autonomous AI Scientist for Time Series)”先河，支持端到端自主提出时空动力学假设、自动编写模型代码、调度 GPU 集群进行实验回测与自我纠错；
- **TimeClaw 通用上下文时序智能体系统** [arXiv:2606.05404]（iDEA-iSAIL Lab）：针对现实业务中时序数据往往嵌套在长篇财经研报、气象灾害预警和突发宏观快讯中的复杂场景，构建了通用时序智能体系统 TimeClaw。TimeClaw 赋予基础大模型调用专业时序分析工具包（包含趋势平滑、周期分解、因果检验与 TSFM 推理接口）的自主规划执行能力，能够端到端解析自然语言上下文并自适应生成多步预测推理链条，官方开源代码经由 GitHub API 严格核验；
- **TSQAgent 时序数据质量专业诊断智能体** [arXiv:2606.03629]：针对“垃圾进，垃圾出 (Garbage in, Garbage out)”的时序基础模型数据顽疾，提出了首个专门面向时序数据质量评级的智能体系统 TSQAgent。TSQAgent 模拟资深数据工程师的排查逻辑，通过多阶段链式推理自主探测时序序列中的传感器漂移、异常脉冲、结构性缺失与动力学逻辑违背，输出细粒度质量评分报告并自动实施针对性修复；
- **T-SMART 机制级归因工具增强 QA 系统** [arXiv:2609.14142]（ICTAI 2026）：在工具增强的大模型时序问答任务中，针对智能体工具链调用失败时难以追溯是“参数提取错误”还是“工具本身失效”的问题，提出了机制级归因框架 T-SMART。T-SMART 通过建立工具调用的细粒度动力学因果图，实现对复杂时序问答推理链条的透明可解释性审计与自动化容错纠偏。

---

### 6.5 具身智能与工业物理多通道基础模型 (Embodied & Industrial Multi-Channel TSFMs)

2026 年时序基础模型最重大的物理边界突破，是将模型从传统的消费互联网指标（点击率、服务器负载、股价）直接下沉到工业物理实体与具身机器人动力学控制中。

#### 6.5.1 FactoryNet：工业具身物理遥测大模型基石

ICML 2026 收录的突破性工作 **FactoryNet** [arXiv:2605.09081] 标志着时序基础模型正式迈入“硬核物理具身时代”。研究团队构建了涵盖 **5100 万点高频真实物理传感器时序** 的超大规模工业具身基准与基础模型体系。

FactoryNet 首次系统性覆盖了现代制造业最核心的 **6 大类物理机电具身实体 (Physical Embodiments)**：
1. **数控高速铣削机床 (CNC Milling Machines)**：采集三轴切削力传感器、主轴高频振动谱、切削液压力与刀具微米级热形变序列；
2. **工业六自由度机械臂 (6-DOF Robotic Arms)**：采集各关节电机高频伺服力矩、角加速度、末端执行器 6D 位姿轨迹与减速机反向间隙波形；
3. **重型液压冲压机 (Hydraulic Stamping Presses)**：采集主油缸兆帕级压力脉动瞬变曲线、滑块下止点微冲位移及液压油温漂移；
4. **高速自动化分拣输送线 (Conveyor Sorting Systems)**：采集光电对射脉冲、伺服电机相电流突变及包裹质心偏置波形；
5. **智能卷材包装机 (High-Speed Packaging Machinery)**：采集薄膜张力动态控制闭环、热封温度连续曲线与伺服切刀相位同步信号；
6. **热塑性注塑机 (Thermoplastic Injection Molding)**：采集螺杆各温区 PID 功率响应、射胶峰值保压曲线及模温耦合波动序列。

#### 6.5.2 具身多通道时序的核心物理挑战与模型突破

与传统互联网时序相比，具身物理时序具有严密的物理守恒定律与强机械非线性交叉耦合：
- **物理守恒与动力学刚性约束**：例如机械臂运动满足拉格朗日动力学方程 $\mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau}$，常规基础模型生成的平滑预测常常违背角动量守恒或瞬时产生虚假的超限加速度；
- **跨本体零样本物理迁移**：FactoryNet 证明，通过在机床、机械臂与冲压设备的大规模跨设备多通道预训练，模型学习到了机电系统中通用的“摩擦力热衰减、轴承疲劳谐波、伺服刚度谐振”等深层物理动力学不变量。在面对完全未见过的某种新型激光切割机时，FactoryNet 展现出开箱即用的零样本健康状态评估 (RUL) 与突发颤振 (Chatter) 抑制预警能力，为通用具身智能与工业 4.0 提供了强大的物理时序智能基座。

---
"""

part5 = r"""## 7 基准与评测

评测机制的严谨性与度量维度直接决定了基础模型泛化声称的真实可信度。随着基础模型预训练语料规模突破万亿时序点，评测范式正经历从“传统静态测试集点误差对比”向“严格时序因果隔离审计、宏观版本修订溯源、前瞻偏误排查、预测崩溃防御、状态依赖失效审计、系统集中性风险防御、工业经济性损益平衡与端到端智能体决策”的系统性重构。当前文献中，开源模型、闭源模型与评测基准的占比分布如下图所示：

![Open Weight Share](figures/open_weight_share.png)

![Papers by Category per Year](figures/papers_by_category_year.png)

### 7.1 通用时序评测矩阵与基准对比

下表对比了时序基础模型与多模态前沿的核心基准套件与评估审计框架（数据严格来自于对应论文声明）：

| 基准/评测体系 | 代表机构/文献 | 核心任务与模态 | 涵盖规模/时序点 | 时序因果隔离与动态更新机制 | 核心评估重点 | 开源状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GIFT-Eval** | Salesforce [arXiv:2410.10393] | 通用零样本预测 (TS) | 7 个域 1.77 亿观测值 / 230 亿点 | 静态多领域保留集 | 跨频段 MASE / CRPS / 极端点鲁棒性 | 是 |
| **It's TIME** | 学术团队 [arXiv:2602.12147] | 新一代真实预测 (TS) | 跨 9 大行业领域海量序列 | 区分平稳与强非平稳漂移段 | 工业真实分布偏移下的泛化稳健性 | 是 |
| **RMISC** | 学术团队 [arXiv:2607.06504] | 真实多变量时序基准 (MTS) | 1420 亿真实工业时序点 (142B) | 跨 10+ 垂直领域海量真实传感器流 | 大规模真实多变量预训练与跨域零样本泛化 | 是 |
| **DoTime** | 学术团队 [arXiv:2607.27263] | 反事实与干预评测基准 (Causal TS) | 动力学 TSCM 合成系统 | 严格的 do-calculus 因果干预隔离 | 评估模型在外部干预与反事实推演下的真实决策能力 | 是 |
| **LiveHouse-TS** | 学术团队 [arXiv:2608.17299] | 活体开放基准 (TS) | 持续滚动的开放时序流 | 动态实时抓取最新全球时间序列 | 杜绝模型预训练静态记忆与后门过拟合 | 是 |
| **VersaTSA** | 学术团队 [arXiv:2609.22836] | 不规则多变量预测 (MTS) | 300 亿跨领域观测值 (30B points) | 多采样率非等间距跨域测试集 | 评估多变量在通道异步缺失与时间戳不规则下的鲁棒性 | 论文声明 |
| **FactoryNet** | 学术团队 [arXiv:2605.09081] | 工业具身物理基准 (6类机电实体) | 5100 万高频物理时序点 | 跨机床/机械臂/冲压设备因果隔离 | 机械动力学守恒与工业装备跨本体零样本迁移 | 是 |
| **Break-Even 分析** | Jerome & Simon [arXiv:2607.04919] | 投资回报率损益平衡审计 (TS) | 30 个跨领域基准数据集 | 算力/能耗/显存 vs 预测精度损益平衡点 | 明确 TSFM 相比传统 GBDT/ARIMA 的盈利与性能分界线 | 论文声明 |
| **Text Sensitivity 审计**| Sridhar 等 [arXiv:2608.22321] | 多模态文本敏感度审计 (TS+Text) | 多个多模态时序公开基准 | 语义扰动 vs 结构置换对比消融 | 审计大模型究竟利用了真实语义还是仅仅捕捉了统计结构 | 论文声明 |
| **Regime-Dependent 评测**| Wang 等 [arXiv:2606.18367] | 状态依赖型失效分析 (TS) | 真实交通路网超大规模速度流 | 依据拥堵相变分段审计动态失效 | 揭示总指标掩盖下的突发拥堵相变预测盲区 | 论文声明 |
| **HoliBench** | 弗吉尼亚等学术团队 [arXiv:2609.12412] | CPS-IoT 嵌入式基准 (TS+LLM+VLM)| 涵盖边缘 GPU、微控制器等多硬件 | 嵌入式与边缘异构实时推理约束 | 真实边缘硬件下的能耗、内存占用与延迟 | 是 |
| **Cost-Aware Study** | 工业学术团队 [arXiv:2608.22968] | 工业监控成本效益 (TS) | 多个真实工业连续生产流 | 严格时间戳因果阻断 | TSFM 相比轻量基线 (TTM/LightGBM) 的经济 ROI | 论文声明 |
| **Look-Ahead Bias 审计**| 学术团队 [arXiv:2609.20554] | 前瞻偏误实证审计 (TS) | 跨金融、宏观经济多域序列 | 对比严格因果切分与未来信息微泄漏 | 实证证实未来数据预训练导致虚假繁荣与负迁移 | 论文声明 |
| **Forecast Collapse** | 学术团队 [arXiv:2608.14106] | 预测崩溃机理分析 (TS) | 高噪声金融与物理高频序列 | 考察噪声信噪比临界退化相变 | 剖析庞大基础模型退化为平凡平直均值的临界失效条件 | 论文声明 |
| **Causal Analysis 框架**| 学术团队 [arXiv:2608.24303] | 因果集中性风险审计 (TS) | 跨金融、能源与气候 3 大行业 | 结构因果模型 (SCM) 反事实干预 | 单一基础模型被全行业采用带来的系统性脆弱风险 | 论文声明 |
| **Accuracy Law 审计** | 龙明盛团队 [arXiv:2510.02729] | 预测精度定律实证审计 (TS) | 跨领域标准基准集 | 历史回看长度 $L$ vs 预测视野 $H$ 扩展 | 刻画时序预测误差随上下文和复杂度的幂律缩放规律 | 是 |
| **EOB 损失偏误审计** | 金明团队 / 阿里等 [arXiv:2512.18610] | 逐点损失优化偏差审计 (TS) | 广泛时序基准集 | 逐点 MSE/MAE 优化下高频衰减与相位滞后 | 揭示传统损失导致平滑滤波与峰值塌缩的根本机理 | 是 |
| **SGA 评测框架** | 学术团队 [arXiv:2609.28582] | 多步预测不确定性校准 (TS) | 通用多领域基准集 | 步阶梯度对齐度量 | 多步滚动外推累积发散抑制与不确定性置信校准 | 论文声明 |
| **概率预测系统综述** | Besher 等 [arXiv:2609.13345] | 概率与时空预测系统综述 | 全面涵盖分位数/流/扩散/TSFM | 概率校准度量与高阶依赖覆盖 | 概率预测全景分类法与未来基准方向 | 综述 |
| **VINTAGE-TS** | 学术团队 [arXiv:2609.28576] | 数据版本修订审计基准 (TS) | 宏观统计多版本演进时间序列 | 区分初次快讯与最终修正版本 | 防止“未来修订数据穿越”导致的虚高得分 | 是 |
| **MACROCAST 审计** | 学术团队 [arXiv:2606.28670] | 版本一致性实时宏观基准 (TS) | FRED-MD 历史实时快照系列 | 模拟历次政策发布当时的实时可见集 | 评估模型在无修订未来信息污染下的真正实时外推能力 | 论文声明 |
| **FINESSE** | 摩根士丹利等团队 [arXiv:2609.11993] | 多模态金融事件仿真 (TS+Text) | 真实行情+多智能体仿真复杂事件序列 | 事件驱动异步连续流 | 多智能体金融推演与极端事件抗压预测 | 是 |
| **ADBIS 2026 评测** | Trihinas 组 [arXiv:2609.25788] | 零样本概率校准 (TS) | 6 大主流开源 TSFM 横向评测 | 严格因果时序切分 | 点预测误差 vs 区间覆盖率 PICP / 分位数可靠性 | 论文声明 |
| **Contamination Hold-Out** | 学术团队 [arXiv:2609.10357] | 数据污染严格审计 (TS) | 涵盖 13 类预测模型的隔离测试 | 严格截断在模型发布日期之后的最新时序 | 破除预训练数据熟悉度 (Familiarity) 造成的虚高分数 | 是 |
| **Tracing Evidence 框架** | 李子跃组 [arXiv:2609.21425] | 零样本审计体系 (TS+Text) | 概念与审计基准体系 | 区分语言先验、时序预训练与外存检索 | 将零样本归结为可验证的“证据访问边界” | 论文声明 |
| **Time-MMD** | 学术团队 [arXiv:2406.08627] | 多模态时序理解与预测 (TS+Text) | 9 大领域数万图文时序对 | 领域与多源异构跨模态隔离 | 文本因果线索注入对预测精度的增益 | 是 |
| **Beyond Numerical TS** | 学术团队 [arXiv:2609.15087] | 异构上下文预测 (TS+Text+Event) | 多源异构环境工业时序 | 异构事件与外部传感器对齐 | 非数值驱动变量与突变响应 | 是 |
| **ST-Bench (STReasoner)** | 金明组 [arXiv:2601.03248] | 时空跨模态因果推理 (TS+Text+Graph) | 网络 SDE 多智能体合成与真实路网 | 拓扑图变化与时间步演化解耦 | 归因推理、实体识别、关联推理与上下文预测 | 是 |
| **TimeSage-MT** | 金明组 [arXiv:2606.01498] | 多轮智能体时序推理 (TS+Text) | 240 复杂任务 / 2,680 轮对话 | 8 大领域多轮演化上下文追踪 | 状态识别、长程会话记忆与决策分析 | 是 |
| **TimeSage-EV** | 金明组 [arXiv:2608.14270] | 动态演化环境活体评测 (TS+Text) | 60 机构场景 / 1,485 场景问答对 | 2023.02 至 2026.05 真实定期发布截断 | 截止日期意识、证据更新有效性与前瞻推断 | 是 |
| **TimeVista** | 清华 THUML [arXiv:2606.16173] | 多模态裁判评估 (TS+Vision) | 多领域海量折线图像对比对 | 视觉对齐与图表渲染流水线 | 视觉语言模型裁判 (VLM-as-a-Judge) | 是 |
| **AION 科研评测** | 金明组 [arXiv:2605.25045] | 自主科学研究调度评估 (TS+Agent)| 端到端时序发现任务集 | 自动化探索环境闭环 | 科学猜想提出、自动代码实现与假设验证能力 | 是 |
| **Forecast Workflow Bench**| 学术团队 [arXiv:2609.27385] | 预算约束智能体工作流 (TS+Agent) | 运筹规划工业时序仿真 | 步数与 API 预算动态受限 | 工具选择策略、调度收益与边际成本权衡 | 是 |
| **Aionoscope 潜状态审计** | 金明组 [arXiv:2607.00956] | 表征可访问性与隐状态调试 (TS) | 多个主流 TSFM 潜空间 | 隐空间探测探针与流形投影 | 审计时序表征内部状态是否可被下游线性可访问 | 是 |
| **Memory in Deep TS** | 学术团队 [arXiv:2609.06006] | 记忆容量与长程依赖理论评测 (TS)| 理论动力学合成序列基准 | 受控记忆衰减与时滞测试 | 严格度量不同架构对历史长期信息的保持与遗忘边界 | 论文声明 |
| **ORBIT 基准** | 学术团队 [arXiv:2608.13262] | 预训练机制与分布评测 (TS) | 跨域多源合成与真实语料 | 考察领域配比对跨域零样本迁移影响 | 预训练语料多样性与类别平衡理论准则 | 是 |
| **Retrieval Regime 审计**| Kurban 组 [arXiv:2609.20193] | 检索增强临界工作区间审计 (TS) | 多个主流开箱基准集 | 目标域平稳性与历史窗口阶跃测试 | 划定时序 RAG 产生正向收益的物理临界边界 | 是 |
| **TabPFN-TS 供热评测** | 工业学术团队 [arXiv:2608.20024] | 区域集中供热零样本概率评测 (TS)| 城市供热网真实热负荷序列 | 严格时序先后回测 | 评估先验数据模型在真实大型公共公用事业中的泛化表现 | 论文声明 |
| **When Does Text Inform?** | 学术团队 [arXiv:2609.11282] | 信息论多模态时序评测 (TS+Text) | 多领域图文时序基准 | 严格基于互信息与传递熵隔离 | 评估文本模态在时序预测中的真实增益边界与信息冗余 | 论文声明 |
| **Base-Rate Honest TimesFM** | 学术团队 [arXiv:2607.12248] | 金融方向预测无偏基准 (TS) | 跨市场真实股票权益高频序列 | 考虑资产基准率偏差的严格时间戳隔离 | 审计 LoRA 适配 TimesFM 的真实方向预测能力，杜绝基准率作弊 | 论文声明 |
| **Clinical Hindsight Bias** | 学术团队 (ML4H 2026) [arXiv:2609.13454] | 临床后瞻时序偏误基准 (TS+Text) | MIMIC-IV 等真实重症监护多模态病历 | 严格对比不同阶段未来病程信息的泄漏 | 评估大语言模型临床时序推理中的后瞻偏误与因果扭曲 | 论文声明 |
| **Crowd Count Benchmark** | 学术团队 (ITSC 2026) [arXiv:2609.16415] | 行人群体客流预测基准 (MTS) | 跨城市多个真实公共交通与商圈客流集 | 跨空间尺度与时间分辨率严格留出 | 评估时序基础模型在空间-时间异构客流密集度下的零样本泛化能力 | 论文声明 |
| **Candlestick VLMs** | 学术团队 [arXiv:2604.12659] | 多尺度 K 线图表视觉评测 (TS+Vision) | 多尺度金融市场真实高频与日线蜡烛图 | 多尺度扰动与几何结构伪造测试 | 审视视觉语言大模型是否真正“读懂”金融 K 线还是受表面启发式误导 | 论文声明 |
| **Coding Agent TS Reasoning** | 学术团队 [arXiv:2606.16545] | 代码智能体时序编程推理基准 (TS+Code) | 复杂时序清洗、建模与评估全流程任务 | 端到端代码执行沙箱与环境动态反馈 | 评估大模型代码智能体在真实时序全生命周期流程中的严谨推理能力 | 论文声明 |

---

### 7.2 数据污染、预训练熟悉度与时序因果隔离审计

在时序基础模型时代，学术界沿用多年的经典公开测试集（如 ETT 系列、Weather、Electricity、Traffic）遭遇了前所未有的**数据污染 (Data Contamination) 与预训练熟悉度危机**：
1. **公开基准的事先暴露与记忆作弊**：现有主流基础模型预训练语料高达数百亿至上万亿点（如 LOTSA、UTSD、Time-300B、Toto 1T、RMISC 142B、VersaTSA 30B）。即使研究者声明排除了特定测试集，庞大的网络爬取语料中仍不可避免地包含了同一物理系统在相邻时段或相同分布下的数据片段；
2. **“时间延迟不等于新领域”** [arXiv:2609.10357]：Moghadasi 与 Ghaderi 的开创性研究指出，时序领域的“零样本”声称长期依赖于领域外测试，但模型在熟悉物理系统上的表现与其真实跨域泛化存在本质区别。在真正无污染的时间截断测试集上，许多庞大模型的绝对误差大幅攀升；
3. **前瞻偏误的实证审判 (Look-Ahead Bias in Pretraining)** [arXiv:2609.20554]：系统探究了“用未来数据预训练是否真正有益”的重大命题。研究严谨证实：在预训练中违背严格时序先后因果关系（例如混合未来月份甚至未来年份数据进行掩码预训练）不仅会导致测试时产生严重虚高欺骗性性能，更在真实下游迁移时诱发显著的**负迁移 (Negative Transfer)**——模型学会了依赖未来信息的捷径特征，丧失了在纯历史自回归推断时的敏锐因果捕捉力；
4. **宏观数据版本修订穿越漏洞** [arXiv:2609.28576] 与 **MACROCAST** [arXiv:2606.28670]：揭示了一个极其隐蔽却普遍存在的系统性漏洞：国家统计局或央行发布的 GDP、就业率和工业产值，在首次公布后往往会在后续数月乃至数年进行多轮重大修正。如果研究者直接从当下的数据库下载历史时间序列来评估模型过去的表现，模型实际上接触到了“发布日期时尚未发生的数据修正”，造成严重的信息未来泄露。MACROCAST 证明唯有基于实时历史切片 (Vintage Data) 进行预训练才能构建真正可信的实时宏观预测模型；
5. **未知信息泄露预警** [arXiv:2510.13654]：Rethinking Evaluation 进一步形式化了未来信息泄漏的三种途径：全局归一化参数泄漏、跨序列重叠采样泄漏以及自注意力双向重叠泄漏，强调未来的评测必须强制要求只使用因果单向窗口归一化与时间戳严格后延的测试语料；
6. **深度时序模型记忆容量理论审计 (Memory in Deep Time-Series Models)** [arXiv:2609.06006]：该研究针对当前大模型关于“能够吸收无限长历史上下文”的宣称进行了理论与实证审查。通过设计具有精确因果时滞的受控动力学测试序列，评测揭示了当前 Transformer 架构在超过特定窗口阈值后，因注意力弥散与 Softmax 温度退化导致的**指数级记忆衰减**现象，为合理设定预训练上下文长度提供了理论下界；
7. **检索增强时序预测有效区间审计** [arXiv:2609.20193]：严谨证实了当时序信噪比较低或回看窗口已经覆盖主周期时，外源检索会导致模型发生注意力偏离与虚假频率锁定；
8. **临床时序后瞻偏误实证审计 (Hindsight Bias in Clinical Temporal Reasoning)** [arXiv:2609.13454]（ML4H 2026）：揭示了在医疗健康与重症监护 (ICU) 时序评测中极易被忽视的后瞻偏误 (Hindsight Bias)。研究证实，当在提示词或微调语料中无意间混入未来就诊事件、出院记录或后续确诊编码时，大语言模型在当前时间点的诊断与死亡率预测指标呈现虚假的卓越表现；一旦彻底剔除未来暴露，模型性能剧烈下滑，凸显了临床时序基准必须建立绝对因果单向时间屏障的极端重要性；
9. **金融方向准确率基准率欺骗审判 (When Directional Accuracy Lies)** [arXiv:2607.12248]：针对金融量化界广泛采用方向准确率 (Directional Accuracy, DA) 评估 LoRA 适配 TimesFM 的风潮，该研究一针见血地指出：在非对称资产市场中，由于长期上涨或下跌的自然“基准率偏置 (Base-Rate Bias)”，模型只需持续预测多数类方向即可轻松取得 60% 以上的虚假高 DA；研究提出了校正基准率偏置的无偏评估基准，揭示了基础模型在金融权益预测中的真实表现。

### 7.3 证据边界与零样本审计框架

针对当前“零样本 (Zero-Shot)”概念被滥用、不同模型在不同提示与外存条件下不公平对比的乱象，李子跃团队在 ACM AI Summit 2026 上提出了**基于“证据来源第一”的严格审计框架** [arXiv:2609.21425]：
该框架明确指出，“零样本”不应仅仅被定义为“未对目标域进行参数梯度更新”，而必须被界定为一种**受管制的证据访问声称 (Evidence-Access Claim)**。框架将所有零样本时序系统的能力来源解耦为三大基础证据边界：
1. **冻结语言模型先验复用 (Frozen LLM Prior Reuse)**：依靠通用大模型（如 GPT-4、LLaMA）中固化的人类常识、周期概念与语言联想；
2. **参数化时序预训练 (Parametric TSFM Pretraining)**：依靠大规模时序多域数据集预训练学得的通用动态算子（如 Chronos、TimesFM、Timer）；
3. **检索增强外部记忆 (Retrieval-Augmented External Memory)**：依靠推理期从外部历史库中检索相似模式的跨序列线索。

在明确证据来源后，该框架制定了四大审计维度：
$$\text{Audit Dimension} \in \{\text{Task Interface}, \text{Forecast Object \& Scoring}, \text{Prediction Context}, \text{Resource Budget}\}$$
通过强制在排行榜上同步公开上下文长度限制、推断 FLOPs 预算以及外部先验调用边界，确保前沿评测真正反映跨领域泛化能力，而非隐蔽的算力扩张或上下文泄露。

与此同时，多模态与因果安全性审计正在向纵深拓展：
- **Aionoscope 表征可访问性与潜状态可解释性审计** [arXiv:2607.00956]（金明团队，KDD MILETS 2026）：针对当前基础模型内部表征如同“黑盒”的问题，提出针对时序隐状态可访问性的调试探针工具 **Aionoscope**。Aionoscope 能够量化评估不同网络层输出的表征对下游物理属性（如瞬时频率、非线性阻尼比、突发相位跳变）的线性解耦程度，从表征几何学角度揭示了模型产生预测误差的内部动力学根源，官方开源代码经由 GitHub API 严格核验；
- **多模态时序文本敏感度实证审计** [arXiv:2608.22321]（Sridhar & Gupta 等）：揭露了当前多模态时序研究中一个普遍存在的严峻隐患——许多声称通过结合非结构化文本大幅提升预测精度的复合大模型，在经过严格控制的**语义破坏消融实验 (Semantic Perturbation Audit)** 下暴露出虚假繁荣。当把具有真实因果内涵的领域描述替换为随机乱码或颠倒语法时，模型的指标几乎没有发生统计显著下降。这表明诸多模型仅仅学到了对文本 Token 长度或结构性标点位置的虚假相关性捷径，并未真正建立时序动态与自然语言因果语义的深层对齐；
- **反事实干预与结构因果基准审计** [arXiv:2607.27263]（DoTime）：证明在传统关联性测试集上表现优异的基础模型，在面对外生政策干预与反事实推演时均出现严重失效，呼吁将 Pearl do-演算干预响应作为未来评估 TSFM 物理真实性的核心准则；
- **因果集中性风险审计** [arXiv:2608.24303]：警告当全行业从针对单一任务定制专有模型转向共同依赖少数几个头部 TSFM 时，模型与应用的关系从“一对一”转变为“一对多”，带来了严重的**集中性风险 (Concentration Risk)**；
- **信息论视角下的文本真实有效性基准 (When Does Text Inform?)** [arXiv:2609.11282]：针对多模态时序预测中“无脑拼接文本”的行业现状，从信息论（互信息、条件熵、传递熵）的数学底层系统评测了文本信息的边际增益。研究表明，仅当文本所携带的互信息显著高于时序自身自回归信息熵，且两者的传递熵在时序因果上有序单向流动时，引入多模态文本才能产生统计显著的正向增益，否则只会引入额外的高频表征噪声；
- **多尺度 K 线图表视觉真实性基准 (Do VLMs Truly Read Candlesticks?)** [arXiv:2604.12659]：对当前声称能够通过“看股票 K 线图”进行高收益外推的视觉语言模型 (VLMs) 进行了严格的多尺度消融与反事实伪造审计。评测发现，绝大多数通用 VLM 仅仅依赖颜色对比和粗粒度长条形状等低级视觉启发式捷径，当对 K 线时间轴进行尺度缩放或反转时，模型的预测逻辑立刻崩溃，证明其并未真正理解金融微观市场结构；
- **时序代码智能体严谨推理能力评测 (Can LLM Coding Agents Reason About Time Series?)** [arXiv:2606.16545]：首次将大语言模型代码智能体 (Coding Agents) 置于真实复杂的端到端时序分析流水线中进行严苛审计。基准评测了智能体自主处理不规则采样、异构缺失插补、平稳性检验与模型超参数调优的综合表现，揭示了代码智能体在处理时序因果反转和滑动窗口边界效应时频发的逻辑隐患；
- **空间-时间异构客流密集度评测基准 (Crowd Count Forecasting Benchmark)** [arXiv:2609.16415]（IEEE ITSC 2026）：针对城市公共交通与大型枢纽的突发拥挤风险，首次跨多个真实城市与多样化空间尺度系统评估了现代 TSFMs 在行人群体密集度时序上的零样本泛化能力，明确了基础模型在应对强空间拓扑约束与节假日脉冲突变时的能力上限与失效应对策略。

### 7.4 概率可靠性、分位数校准与高阶依赖度量

绝大多数早期 TSFM 论文仅以均方误差 (MSE) 和平均绝对误差 (MAE) 等点预测指标论英雄，但工业生产对预测的不确定性表达与尾部风险覆盖有着严苛要求：
1. **概率预测与时空数据系统性综述** [arXiv:2609.13345]（Besher 等）：全面梳理了从经典参数分布拟合、非参数分位数回归、连续归一化流、条件分数扩散生成到现代 TSFM 概率预测的系统分类谱系。综述指出，仅衡量点误差不仅掩盖了尾部极端事件风险，更严重诱导了模型朝向平滑平均值的退化，系统归纳了连续概率排位分数 (CRPS)、能量分数 (Energy Score) 与多元覆盖率 PICP 的标准评测管线；
2. **逐点损失优化偏差 EOB 审计** [arXiv:2512.18610]：通过严格的数学推导证实，凡是采用均方误差作为单一损失训练的预测器，其理论最优解均不可避免地导致高频振幅指数衰减与显著相位滞后，呼吁未来的评测必须强制引入频域谱匹配与梯度方向一致性审计；
3. **状态依赖型相变失效审计** [arXiv:2606.18367]（Wang 等）：通过对高密度交通速度流的研究严谨证实，**传统的全集平均误差指标极易掩盖模型在关键状态突变期（如突发交通拥堵、电网跳闸）的严重失效**。模型在平稳状态下表现平稳，但在相变临界点的误差剧增数十倍，呼吁必须对动力学相变区间进行分层独立审计；
4. **预测崩溃 (Forecast Collapse) 理论与机理剖析** [arXiv:2608.14106]：深入揭示了时序大模型在高噪声、低信噪比金融或物理传感器场景中的致命软肋——预测崩溃。当模型面对未知突变或强噪声时，庞大的 Transformer 经常为了最小化均方损失，迅速退化为输出一条毫无波动的水平直线（即仅仅预测历史均值）；
5. **点预测精度与分布校准的脱节** [arXiv:2609.25788]：ADBIS 2026 的系统评测揭示了深刻的二元割裂现象——在测试集取得极低 MSE 的模型，其预测分位数置信区间（如 90% 预测区间覆盖率 PICP）经常严重偏离标称水平；
6. **步阶梯度对齐不确定性量化 (SGA)** [arXiv:2609.28582]：针对自回归基础模型在多步滚动预测中误差逐级发散、置信区间快速失效的问题，提出步阶梯度对齐 (Step-wise Gradient Alignment, SGA) 框架，有效抑制长视野自回归发散，大幅改善了模型在多步滚动外推下的概率校准准确率；
7. **多变量联合样本路径耦合** [arXiv:2609.25980]：针对现有单通道基础模型无法输出多通道协同联合分布的痛点，免训练多变量交织算法证明：仅需对边缘分布采样进行基于历史时空协方差的最优传输重排，即可大幅改善多维联合风险诊断指标。

### 7.5 动态演化环境与多轮智能体评测

随着 LLM Agent 在时序决策中的广泛引入，静态的一次性问答 (Single-turn QA) 已无法衡量系统在现实世界中的持续推理水平：
1. **多轮对话与决策衰减** [arXiv:2606.01498]：金明团队构建的 TimeSage-MT 首次评测了大模型在 2,680 轮长时序交互中的表现，发现当前顶尖大模型在需要多步推演、置信度修正与复合运筹的决策型任务上出现断崖式性能崩溃，主要源于时序工作记忆丢失与不确定性量化能力缺失；
2. **动态演化与发布截断意识** [arXiv:2608.14270]：现实时序决策依赖于定期发布的宏观报告与传感器批次更新。TimeSage-EV 追踪了 2023 年至 2026 年间 60 个真实机构场景的 1,485 个演化问答对。模型必须严格遵循“截断日前可见信息”，预测截断日后真实发生的结果。评测发现，多数智能体对“时间有效性 (Temporal Validity)”极为迟钝；
3. **部署闭环中的自进化策略** [arXiv:2609.24862]：TimEvolve 证明在动态演化环境中，智能体应当把未来的延迟展开视为天然弱监督，通过自进化门控机制在实践中持续优化专家信任矩阵与干预策略；
4. **时空图推理与归因基准** [arXiv:2601.03248]：ST-Bench 首次将空间网络拓扑关系引入时序推理基准，评估模型在实体关联溯源、传播路径推导与零样本上下文预测中的结构泛化能力。

### 7.6 视觉裁判与工作流调度 Harness

1. **时序大模型投资回报率损益平衡分析 (Break-Even Analysis)** [arXiv:2607.04919]：
   针对学术界与工业界对“时序大模型是否真正值得昂贵算力开销”的质疑，Jerome 与 Simon 在 30 个跨领域公开基准上系统测算了 Chronos、Moirai、Lag-Llama 与经典树模型 (LightGBM/XGBoost) 及统计基线 (ARIMA) 的算力-精度平衡曲面。实证指出：**在历史观测充足且周期平稳的场景下，精调树模型的投资回报率 (ROI) 显著高于庞大基础模型；TSFM 产生决定性商业价值的平衡点集中于历史少于 50 点的冷启动传感器、非平稳跨域扰动以及异构多频段突发场景**；
2. **视觉语言大模型充当裁判 (VLM-as-a-Judge)** [arXiv:2606.16173]：
   清华 THUML 团队开创性地指出，人类分析师对时序预测的优劣判断并非局限于点对点数值残差，更看重宏观形态的一致性（峰值拐点、趋势转折、相位对齐）。基于此构建的 TimeVista 验证了让经过对齐的 VLM 直接审阅折线预测图充当打分裁判的可行性，与人类专家评审的相关性显著高于传统数学指标；
3. **端侧硬件资源与实际能耗综合评测 (HoliBench)** [arXiv:2609.12412]：
   面向信息物理系统与物联网 (CPS-IoT) 的实际落地，HoliBench 建立了跨微控制器、边缘 GPU 与云端异构硬件的系统级评测工具链。评测表明，单纯追求预测精度的重型模型在边缘端常因超出 SRAM/DRAM 带宽而发生延迟爆炸，轻量模型（如 7M 的 CITRAS-FM [arXiv:2606.10798] 或 8M 的 TTM）在工业物联场景中展现出压倒性的综合工程性价比；
4. **工业监控部署经济性与真实回报分析** [arXiv:2608.22968]：
   在真实工业流程监控中，引入 TSFM 的边际收益究竟能否抵消其显著增长的推理服务器支出与能耗？该研究通过对多个真实工业场景的严格实验发现，在数据丰富且工况稳定的常规场景下，轻量模型与经典基线完全足以胜任；
5. **自主科学探索与闭环科研评测 (AION)** [arXiv:2605.25045]：
   金明团队建立的 AION 系统展示了智能体作为“全自主科学研究者”的调度评测流程。从阅读时序论文、提炼时空动力学假设、自适应编写模型代码，到调度 GPU 集群进行实验回测与自我纠错，代表了时序自动化研究的最高前沿形态；
6. **工具调度与预算约束 Harness** [arXiv:2609.27385]：
   在真实生产运维中，调用庞大的高精尖 TSFM 或密集数值求解器受制于严苛的推理延迟与 Token/API 成本。Forecast Workflow Bench 首次建立了在固定预算约束下评估大模型合理编排轻量模型、统计模型与基础模型决策效率的量化基准。

---
"""

part6 = r"""## 8 重点课题组进展

时序基础模型与多模态时序智能的高速演进，离不开全球顶尖高校、科研机构与工业实验室的系统化攻坚。不同科研力量在分词假设、模型架构、优化损失以及系统定位上形成了各具特色、相互激荡的技术流派。本章深入剖析七大核心团队的研究脉络，并给出跨维度的全景对比矩阵。

### 8.1 龙明盛团队（清华大学 THUML）

清华大学软件学院龙明盛教授领衔的大数据系统软件国家工程研究中心团队（THUML）是全球时序深度学习与大模型领域公认的学术先驱与领军力量。团队的研究脉络呈现出从“经典深度时序架构设计”到“大时序模型 (Large Time Series Models, LTMs)”再到“连续流匹配生成与动力学标度律探索”的严密演进路径：

1. **经典深度时序基石与 TSlib 生态**：
   在专有深度时序模型时代，THUML 团队连续提出了引领国际学术潮流的里程碑工作，包括兼顾全局趋势与局部周期的 Autoformer、突破注意力二次方瓶颈的 Informer、多周期 2D 卷积变换网络 TimesNet 以及倒置自注意力机制 iTransformer [arXiv:2202.07125]。团队构建并长期维护的开源库 **TSlib (Time-Series-Library)** 成为全球深度时序研究使用最广泛的标准基准测试平台。
2. **大时序模型 (LTM) 统一自回归体系**：
   进入大模型时代，THUML 率先破局，建立了从架构到语料的完整开源技术栈：
   - **Timer** [arXiv:2402.02368]：建立了首个大规模统一自回归时序基础模型。采用统一单序列单补丁下一补丁预测范式，证明了单一预训练模型能够在保持零样本特性的同时无缝胜任长短时预测、局部插补与无监督异常检测；
   - **Timer-XL** [arXiv:2410.04803]：针对工业制造与长程气象中超长历史回看的需求，设计因果扩展上下文注意力机制，使模型对数千步超长周期依赖的吸收能力实现数倍跨越；
   - **Timer-S1** [arXiv:2603.04791]：突破时序大模型参数扩展的边际递减瓶颈，推出高达 **83 亿总参数 (8.3B)**、每次推理动态稀疏激活仅 0.75B 的大模型，首创串行缩放 (Serial Scaling) 技术，在海量跨域基准上确立了超大规模预训练的泛化优势。
3. **动力学生成与连续流匹配革命**：
   - **Sundial** [arXiv:2502.00816]：THUML 团队深刻反思均方误差导致平滑均值退化与离散量化破坏浮点连续性的顽疾，推出 15 亿参数 (1.5B) 的连续流匹配大模型，首创 **TimeFlow** 生成理论。利用条件连续流匹配 (CFM) 与常微分方程 (ODE) 亚微秒级快速积分采样，生成高度保真的物理连续波形；
   - **DiTS** [arXiv:2602.06597]：首次将计算机视觉顶级 Diffusion Transformer (DiT) 架构迁移至高维多模态时序生成，以空间自注意力捕获高维时空非线性关联。
4. **跨模态、表征学习与基础理论探索**：
   - **AutoTimes** [arXiv:2402.02370]：开创时序方言自回归范式，使通用语言大模型无需结构改动即可自回归输出未来时序；
   - **TimeXer** [arXiv:2402.19072]：提出面向外生协变量的跨通道注意力解耦架构；
   - **TimesBERT** [arXiv:2502.21245]：基于 BERT 双向掩码重建与语义分类，构建通用时序编码器；
   - **TimeVista** [arXiv:2606.16173]：首创视觉语言模型裁判 (VLM-as-a-Judge) 评测范式；
   - **时序精度定律 (Accuracy Law)** [arXiv:2510.02729]：建立首个数学解析函数，刻画时序预测误差随历史回看长度 $L$、预测视野 $H$ 及模式复杂度 $\mathcal{C}_P$ 的幂律缩放规律；
   - **CoRA** [arXiv:2510.12681] 与 **TimeAgent**（IEEE TKDE 2026）：构建协变量自适应框架与闭环科学探索智能体。
5. **数据与开源生态**：
   依托 OpenLTM 开源社区，持续公开超大规模预训练数据集 UTSD、UTSD-2 与 UTSD-3（超 100 亿时序观测点），推动了整个学术界的标准化演进。

---

### 8.2 金明团队（Ming Jin Group, Griffith / Monash）

澳大利亚格里菲斯大学与莫纳什大学的金明团队（Ming Jin Group）联合温青山（Qingsong Wen）等学术团队，在大语言模型赋能时序 (LLM-for-TS)、超大规模混合专家时序大模型、连续动力学系统与交互式决策智能体方向构建了全球领先的研究矩阵：

1. **大模型时序重编程与跨模态对齐先驱**：
   - **Time-LLM** [arXiv:2310.01728]（ICLR 2024）：奠基之作，首次在国际上确立了“大语言模型重编程用于时间序列分析”的理论与实验范式，证明了利用补丁线性投影层与词表子空间软对齐，冻结的百亿级 LLM 能够直接涌现出惊人的零样本与少样本预测能力；
   - **STReasoner** [arXiv:2601.03248]（ACL 2026）：构建时空拓扑强化学习算法 S-GRPO，使大模型能够推导实体关联拓扑并自主生成因果链条；
   - **在途可迁移性度量理论** [arXiv:2509.23695]：提出免梯度的上下文探针理论，仅需一次前向推断即可精准预测候选模型在未见目标工业领域的微调收益。
2. **超大规模混合专家与连续动力学大模型**：
   - **Time-MoE** [arXiv:2409.16040]（ICLR 2025）：率先构建包含 3000 亿时序点的超大规模开源预训练语料 Time-300B，训练了业界首个达 **24 亿参数 (2.4B)** 的稀疏混合专家基础模型，通过多尺度动态路由推高泛化边界；
   - **TimeMixer** [arXiv:2405.14616] 与 **TimeMixer++** [arXiv:2410.16032]：提出多尺度全混叠模式架构与通用模式机；
   - **LeapTS** [arXiv:2605.10292]：创新性打破固定步长滚动预测的僵化设定，提出自适应多视野动态调度控制器与连续受控微分方程 (Neural CDE)，实现任意连续时间尺度的跨步外推；
   - **LeNEPA** [arXiv:2607.00958]（KDD MILETS 2026）：反思传统时序对比学习数据增强对物理因果规律的扭曲，提出免数据增强下一隐状态预测的自监督表征学习新路线。
3. **动力学生成与损失函数理论突破**：
   - **PaCoDi** [arXiv:2602.17706]：首创**并行复数扩散生成架构 (Parallel Complex Diffusion)**，将时序投影至复数谱平面，解耦相位与能量，在全频段上实现一步并行扩散去噪，将长序列生成吞吐提升数十倍，官方代码全面开源；
   - **逐点损失偏误理论 (The Procrustean Bed / EOB)** [arXiv:2512.18610]：从数学上证明了传统逐点 MSE/MAE 损失对相位随机性时序具有高频振幅指数衰减效应，提出频域能量谱匹配与梯度对齐的结构去偏方案；
   - **OATS** [arXiv:2601.19040]：提出面向非平稳时序的在线自适应扩散数据增强。
4. **决策智能体、多模态全息交互与全自主科学研究**：
   - **ChatAD** [arXiv:2601.13546]：构建具备 80 亿参数 (8B) 的工业异常多轮根因排查推理智能体；
   - **Time-MQA** [arXiv:2503.01875]、**TimeOmni-1** [arXiv:2509.24803] 与 **TimeOmni-VL** [arXiv:2602.17149]（ICML 2026）：建立时序-语言-视觉三模态全息融合推理体系；
   - **Sonar-TS** [arXiv:2602.17001] 与 **TimeInteract** [arXiv:2609.26389]：实现流式高频传感器时序的实时交互与多智能体意图解析；
   - **EventCast** [arXiv:2602.07695]：构建电商平台大促事件知识图谱与混合需求预测大模型；
    - **AION** [arXiv:2605.25045]：开创面向时间序列的全自主科学研究 AI 智能体体系；
    - **Aionoscope** [arXiv:2607.00956]（KDD MILETS 2026）：提出针对时序表示潜状态可访问性 (Latent-State Accessibility) 的调试与探测框架，官方代码全面开源；
    - **权威动态演化基准**：建立首个长时交互多轮基准 TimeSage-MT [arXiv:2606.01498] 与严格时间戳截断评测基准 TimeSage-EV [arXiv:2608.14270]；
    - **持续维护领域权威综述**：[arXiv:2310.10196]。

---

### 8.3 亚马逊团队（Amazon Web Services / Chronos Team）

亚马逊 AWS 团队以开创“时间序列极致语言化”路线而闻名，其核心主张是打破时序连续数值的特殊性偏见，将其彻底抽象为自然语言分词与因果自回归生成：

1. **离散分箱量化与概率采样突破**：
   - **Chronos** [arXiv:2403.07815]：首创均值绝对缩放归一化与 4096 离散分箱量化映射，完全复用语言模型原生类别交叉熵损失。Chronos 证明，无需预设正态或学生-t 分布先验，基于词表的自回归 Softmax 采样天然能够生成任意多峰、长尾且高度校准的未来概率分布。预训练融合海量合成高斯过程与 TSMix 数据（840 亿观测值），实现了极强的零样本泛化能力；
   - **Chronos-2** [arXiv:2510.15821]：将离散量化拓展至通用多变量预测，通过跨变量交叉注意力建模多条量化序列的高阶协方差。
2. **垂直扩展与工业落地**：
   - **FedChronos** [arXiv:2608.01290]：构建联邦参数高效微调框架，在保护商业机密的前提下实现去中心化大模型协同；
   - **KG-Chronos-2** [arXiv:2609.21381]：将水动力学知识图谱约束注入 Chronos-2，在极端水文与防洪调度中展现出物理保真度；
   - **AutoGluon-TimeSeries**：将 Chronos 系列深度集成到 AWS 工业级自动化机器学习流水线中，成为当前全球云计算企业中应用最广泛的时序大模型服务之一。

---

### 8.4 Salesforce Research（Moirai Team）

Salesforce 团队主打“全变量全频段大一统架构 (Any-variate, Any-frequency)”与大规模高质量开源生态建设：

1. **Any-variate 与几何旋转嵌入理论**：
   - **Moirai** [arXiv:2402.02592]：彻底打破固定通道数输入限制，提出 Any-variate 序列结构化展平注意力机制，并推导了变量感知旋转位置编码 (vRoPE)，使单模型权重无需改动即可接收 1 到任意 $C$ 个通道的输入；同时引入多尺寸补丁投影池 $\mathcal{P} = \{8, 16, 32, 64, 128\}$，原生适应从分钟级到月度级的极端采样频率差异；
   - **Moirai-MoE** [arXiv:2410.10469]：推出 11 亿参数 (1.1B) 稀疏混合专家版本，动态解耦跨通道与跨频段专家；
   - **Moirai 2.0** [arXiv:2511.11698]：发布精简高效的紧凑预训练版本，大幅降低了多变量注意力计算与显存开销。
2. **基石数据集与权威评测标杆**：
   - **LOTSA 语料库**：开源构建了涵盖 9 个主要工业与科学领域、270 亿时序观测值的庞大预训练基准；
   - **GIFT-Eval** [arXiv:2410.10393]：构建了涵盖 7 个领域、1.77 亿观测值 / 230 亿点的权威零样本预测评测基准，全面考察跨频段 MASE、CRPS 与尾部鲁棒性，成为全球学术界公认的主流竞技场。
3. **时序智能体系统前沿**：
   - **时序大模型智能体系统综述 (Findings of EMNLP 2026)** [arXiv:2608.26226]：Salesforce Moirai 团队与学术界联合发布，全面系统地回顾了 LLM 赋能时序智能体的最新进展，确立了时序智能体的统一认知框架。

---

### 8.5 谷歌团队（Google Research / TimesFM Team）

谷歌研究院坚守连续浮点数值与补丁自回归路线，强调工业级低延迟与严谨的度量保真性：

1. **长视野非对称连续补丁自回归**：
   - **TimesFM** [arXiv:2310.10688]：坚决反对分箱离散化带来的度量信息丢失，坚持连续浮点补丁建模。创新性设计两阶段非对称投影：输入补丁 $P_{\text{in}}=32$，长视野输出一次性前向投射 $P_{\text{out}}=128$ 步，使推理延迟相比传统单步滚动生成降低了数十倍；基于 Google Cloud TPU 算力集群在包含 1000 亿真实与合成时序点上预训练，在零样本多步点预测与概率外推中树立了精度标杆；
   - **TimesFM-3 (330M)**：进一步拓展模型参数容量与注意力视野，强化了对复杂工业传感器的抗噪能力。
2. **预测残差误差有界工业压缩**：
   - **Cadence** [arXiv:2609.06008]：开创性地利用 TimesFM 输出的条件期望与条件方差，对高频工业传感器流实施误差有界预测残差压缩 ($\epsilon$-bounded Lossy Compression)，在数学上 100% 保证解压物理误差严格有界的同时将数据吞吐压缩至原始体积的 10% 至 25%，为工业边缘网关数据上云提供了革命性方案。

---

### 8.6 IBM Research 与卡耐基梅隆大学（IBM TTM & CMU MOMENT）

IBM 研究院与卡耐基梅隆大学 (CMU) 分别从“极致轻量边缘 Mixer”与“掩码自编码双向表征”两个独特视角丰富了基础模型生态：

1. **IBM Research：Tiny Time Mixers (TTM)** [arXiv:2401.03955]：
   IBM 反思大模型盲目追求百亿参数的算力与延迟代价，提出基于精简多尺度 MLP-Mixer 架构的微型时序基础模型（参数量仅 **1M 至 8M**）。TTM 突破性证明，经过精细多尺度频域设计的紧凑轻量模型，在工业边缘网关和嵌入式芯片上不仅能够实现微秒级实时推断，其零样本与少样本预测精度甚至能与参数量高出两个数量级的 Transformer 基础模型相抗衡，确立了工业端侧极低能耗部署的标杆。
2. **CMU：MOMENT 纯编码器掩码双向表征** [arXiv:2402.03885]：
   卡耐基梅隆大学团队坚持 Encoder-Only 掩码自编码 (MAE) 路线。构建了涵盖 1300 万序列的 Time-series Pile 语料库，训练了最高 385M 参数的统一双向特征提取器。MOMENT 颠覆了生成式解码器单一聚焦预测的局限，以同一套预训练骨干同时高效支持时序预测、分类、异常检测与缺失插补四大任务，成为通用表征学习的代表作。

---

### 8.7 Datadog 团队（Toto Team）

作为全球可观测性与云监控领域的工业巨头，Datadog 团队从超大规模工业真实遥测数据出发，验证了时序大模型的原生标度律：

1. **万亿点全真实云原生遥测大模型**：
   - **Toto 1.0 与 Toto 2.0** [arXiv:2605.20119]：Datadog 依托其全球云基础设施产生的实时监控流，在超过 **1 万亿真实物理时序点 (1T points)** 上预训练开源时序大模型，并全面开源了从 1 亿到 **25 亿参数 (2.5B)** 的五组完整权重模型。
2. **时序标度律 (Scaling Laws) 的严格工业实证**：
   Toto 团队的研究提供了迄今为止工业界最完备的时序标度律实证：明确证明随着预训练数据量突破万亿级、模型参数突破 20 亿大关，时间序列的零样本外推误差与自然语言大模型一样严格服从幂律单调递减曲线，有力驱散了学术界关于“时间序列由于物理域碎片化无法形成统一标度律”的疑虑。

---

### 8.8 重点课题组与代表机构综合对比矩阵

下表对上述七大核心团队及其代表作进行了全面维度的横向解构对比：

| 课题组 / 代表机构 | 核心学术哲学与技术主张 | 代表性模型与系统矩阵 | 分词机制与损失范式 | 标志性预训练语料 / 基准 | 最大公开模型规模 | 核心理论创新贡献 | 生态开源状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **清华大学 THUML** (龙明盛团队) | 架构统一、连续流匹配生成与预测精度定律 | Timer, Timer-XL, Timer-S1, Sundial, TimesBERT, DiTS, TimeXer, AutoTimes | 连续 Patch; Huber 损失, TimeFlow 连续流匹配 $\mathcal{L}_{\text{CFM}}$, MoE 负载均衡 | UTSD, UTSD-2, UTSD-3 (超100亿点) | **8.3B** (Timer-S1, 激活0.75B) | 连续流匹配 (TimeFlow), 串行缩放 (Serial Scaling), 精度定律 (Accuracy Law) | 代码、模型权重与语料库全开源 (OpenLTM) |
| **金明团队** (Ming Jin Group) | 跨模态重编程、超大规模 MoE、连续动力学与交互决策智能体 | Time-LLM, Time-MoE, LeapTS, PaCoDi, ChatAD, TimeOmni-VL, AION, EventCast, LeNEPA | 多尺度 Patch, 复数频域补丁; 结构去偏损失, Neural CDE 连续动力学 | Time-300B (3000亿点), TimeSage-MT/EV | **2.4B** (Time-MoE) | 模型重编程理论, 并行复数扩散 (PaCoDi), 逐点损失偏误 (EOB), 免梯迁移度量 | 代码、模型权重与基准评测集全开源 |
| **亚马逊 AWS** (Chronos Team) | 极致语言化、离散概率分箱与工业级自动化流水线 | Chronos, Chronos-2, FedChronos, KG-Chronos-2 | 4096 离散分箱 (Quantized Bins); 类别交叉熵 $\mathcal{L}_{\text{CE}}$ | TSMix + 高斯过程合成 (840亿观测) | **710M** (Chronos-Large) | 离散分箱非对称后验采样, 联邦 PEFT 协议, 知识图谱物理约束 | 代码与权重全开源 (整合入 AutoGluon) |
| **Salesforce Research** (Moirai Team) | 全变量全频段 (Any-variate) 统一建模与开源权威评测基石 | Moirai, Moirai-MoE, Moirai 2.0 | Any-variate 扁平化 Patch, 多尺寸投射池; 稳健回归 | LOTSA (270亿观测值), GIFT-Eval 权威基准 | **1.1B** (Moirai-MoE) | 变量感知旋转位置编码 (vRoPE), 跨通道跨频段专家稀疏激活 | 代码、权重与 GIFT-Eval 评测集全开源 |
| **谷歌研究院** (Google Research) | 坚守连续浮点数值、长视野两阶段输出与边缘预测残差压缩 | TimesFM, TimesFM-3, Cadence | 连续浮点数值 Patch (输入32/输出128); Smooth L1 / Huber 损失 | 1000亿真实与合成时序点 (100B points) | **330M** (TimesFM-3) | 两阶段非对称长视野投射, 预测残差误差有界工业压缩 ($\epsilon$-bounded) | 代码与核心权重开源 (支持 Hugging Face / TPU) |
| **IBM Research** (TTM Team) | 极简多尺度轻量化 Mixer、微秒级端侧边缘部署与超高能效比 | TTM (Tiny Time Mixers), TTM-v2 | 跨分辨率多尺度分解 Patch; 稳健多任务回归 | Monash + 多域合成工业数据 | **8M** (TTM-Large) | 极简多尺度轻量特征混合架构, 端侧微秒级实时推断 | 官方开源 (Hugging Face) |
| **卡耐基梅隆大学 CMU** (MOMENT Team) | 纯双向编码器掩码自编码 (MAE) 统一多任务通用时序表征 | MOMENT (Small / Base / Large) | 连续非重叠 Patch; 掩码重建自编码损失 (Masked Autoencoding) | Time-series Pile (1300万条序列) | **385M** (MOMENT-Large) | 非自回归双向统一特征提取, 预测/分类/检测/插补四位一体通用表征 | 官方开源 (GitHub / Hugging Face) |
| **Datadog 团队** (Toto Team) | 真实工业云原生万亿级遥测数据驱动与时序标度律实证 | Toto 1.0, Toto 2.0 | 工业标准多通道 Patch; 连续稳健自回归回归 | 超过 **1 万亿真实生产时序点 (1T points)** | **2.5B** (Toto 2.0-Large) | 万亿级时序点真实标度律单调下降验证, 开源工业级基础设施基模型 | 五套参数量权重与开源评估流水线完全开放 |

---

## 9 开放问题与未来方向

尽管时序基础模型与多模态智能在过去四年取得了飞跃式突破，从单一任务定制小模型成功跃升至万亿参数与万亿数据点的通用底座，但其在工业物理实体、高频微观市场、因果策略控制与自主决策智能体等严苛场景的纵深落地中，仍面临深层次的理论瓶颈与工程挑战。本章系统解构时序基础模型迈向下一代“物理世界时空通用智能 (General Physical Spatiotemporal Intelligence)”必须攻克的五大核心科学难题，并给出覆盖六大维度的全景未来破局路线矩阵。

### 9.1 物理定律与动力学守恒约束的时空神经物理融合

#### 9.1.1 统计自注意力机制与物理守恒公理的根本冲突
当前绝大多数主流 TSFMs（如 PatchTST、TimesFM、Moirai、Timer）均建立在以 Softmax 自注意力为核心的序列建模架构之上：
$$\mathbf{A} = \text{Softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right) \mathbf{V}$$
自注意力机制的核心归纳偏置是**数据驱动的成对统计相关性**。然而，现实物理世界中的时间序列（如电网潮流、航空发动机遥测、六自由度机械臂轨迹、化学反应流）受到不可动摇的经典物理公理与动力学守恒定律严格制约。纯数据驱动的神经黑盒在自回归展开或多步预测时，不可避免地产生违背物理现实的虚假震荡与发散：
1. **质量、动量与能量守恒的连续性方程违背**：
   在流体动力学与连续介质力学中，状态变量向量 $\mathbf{X}(\mathbf{x}, t)$ 必须满足守恒通量方程：
   $$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \mathbf{S}(\mathbf{x}, t)$$
   其中 $\rho$ 为守恒物理量密度，$\mathbf{J}$ 为通量密度，$\mathbf{S}$ 为源项。传统 TSFM 产生的多步预测 $\hat{\mathbf{X}}_{T+1:T+H}$ 往往出现守恒量在封闭孤立系统中无故自增或自耗散（例如预测封闭热力学系统的总焓值持续递增）；
2. **拉格朗日与哈密顿动力学方程的辛几何流形违背**：
   对于具身机器人与机电系统，广义坐标 $\mathbf{q} \in \mathbb{R}^n$ 与广义动量 $\mathbf{p} \in \mathbb{R}^n$ 演化服从哈密顿力学方程：
   $$\frac{d\mathbf{q}}{dt} = \frac{\partial \mathcal{H}}{\partial \mathbf{p}}, \quad \frac{d\mathbf{p}}{dt} = -\frac{\partial \mathcal{H}}{\partial \mathbf{q}} + \boldsymbol{\tau}_{\text{control}}$$
   相空间流必须保辛结构（保体积性，Liouville 定理）。常规 Transformer 自回归展开映射往往呈现非保辛耗散或爆炸，导致推演轨迹迅速偏离真实受力平衡流形。

#### 9.1.2 神经物理融合破局路线：几何先验与可微算子约束
为了使时序基础模型在严苛工业物理环境中具备可信性，未来必须建立**时空神经物理融合基础模型 (Physics-Informed Temporal Foundation Models)**：
- **可微动力学流形投影头 (Differentiable Manifold Projection)**：在基础模型解码器后级引入满足守恒定律的可微隐式层：
  $$\hat{\mathbf{y}}_t = \arg\min_{\mathbf{y}} \|\mathbf{y} - \mathbf{f}_\theta(\mathbf{x}_{1:t})\|_2^2 \quad \text{s.t.} \quad \mathcal{G}(\mathbf{y}, \dot{\mathbf{y}}) = \mathbf{0}$$
- **跨频段物理参数自适应归一化**：如 FreqCondNorm [arXiv:2609.20535] 所示，将采样物理机理（如电机极对数、固有机械振动频率）显式编码为先验条件，实现 1Hz 至 100kHz 的超宽频物理动力学解耦；
- **工业三模态物理大模型**：如 VLT [arXiv:2607.14510] 与 FactoryNet [arXiv:2605.09081]，通过跨六类核心物理机电本体（CNC 机床、机械臂、冲压机等）的跨实体表征，让基础模型内生沉淀通用机电不变量（如轴承谐振与热耗散规律）。

---

### 9.2 极低信噪比与高频微观结构下的预测崩溃与信息论极限

#### 9.2.1 时序可预测性的信息论上界与互信息指数衰减
在金融高频订单簿、微观湍流与极端地震监测等领域，时序数据呈现极低信噪比 (Signal-to-Noise Ratio, $\text{SNR} \ll 1$) 与高度有效市场假说特性。学术界长期存在盲目迷信“加大模型参数量即可无限逼近准确预测”的误区。从信息论角度，任意预测器关于未来视野 $H$ 的互信息存在不可突破的物理上界：
$$I(\mathbf{X}_{1:T}; \mathbf{X}_{T+1:T+H}) \le I(\mathbf{X}_{1:T}; \mathbf{S}_T) \le \min\left(H(\mathbf{S}_T), \mathcal{C}_{\text{channel}}\right)$$
其中 $\mathbf{S}_T$ 为物理系统底层潜动力学马尔可夫状态，$\mathcal{C}_{\text{channel}}$ 为传感器观测信道容量。在强混沌系统或高有效性博弈环境中，由李雅普诺夫指数 (Lyapunov Exponent $\lambda_{\max} > 0$) 决定，互信息随预测视野呈指数衰减：
$$I(\mathbf{X}_{1:T}; \mathbf{X}_{T+1:T+H}) \approx I_0 \cdot \exp\left(-\lambda_{\max} H\right)$$
当预测视野 $H > H_{\text{horizon}} = \frac{1}{\lambda_{\max}} \ln\left(\frac{I_0}{\epsilon}\right)$ 时，历史观测与未来轨迹在统计上趋于条件独立，任何模型的预测方差必然退化为不可预测的固有系统方差。

#### 9.2.2 均方误差下的“预测崩溃 (Forecast Collapse)”相变理论
在极低信噪比场景下，当前基础模型普遍遭遇**预测崩溃 (Forecast Collapse)** [arXiv:2608.14106]：
令真实时序生成过程为 $X_t = S_t + \sigma \epsilon_t$，其中 $S_t$ 为真实信号，$\epsilon_t \sim \mathcal{N}(0, 1)$ 为高斯白噪声。信噪比定义为 $\text{SNR} = \frac{\mathbb{E}[S_t^2]}{\sigma^2}$。
当模型在经验均方误差 (MSE) 损失下训练时：
$$\min_\theta \mathbb{E}\left[ \| \hat{X}_{T+1:T+H}(\theta) - X_{T+1:T+H} \|_2^2 \right]$$
根据贝叶斯最优估计理论，最优预测器收敛于条件期望：
$$\hat{X}_{T+1:T+H}^* = \mathbb{E}[X_{T+1:T+H} \mid X_{1:T}]$$
当 $\text{SNR} \to 0$ 时，后验条件期望直接坍缩为全局先验无条件均值：
$$\lim_{\text{SNR} \to 0} \hat{X}_{T+1:T+H}^* = \mathbb{E}[X] \quad (\text{水平平直均值直线})$$
这种相变意味着：**参数量高达数十亿的巨型 Transformer 在面对高噪声时，最优收敛行为反而是“彻底抹杀所有高频微观结构与周期动态，输出一条平庸的均值常数直线”**。
结合扩散模型在逆向去噪终端步的漂移反思 (When Denoising Hurts [arXiv:2608.14067])、金融方向准确率基准率欺骗审判 [arXiv:2607.12248] 以及多模态文本信息论有效性审计 (When Does Text Inform? [arXiv:2609.11282])，未来的核心破局方向在于**从单点均方优化转向率失真理论 (Rate-Distortion Theory) 约束下的生成流形重构与能量基概率扩散**，在数学上严格划定信号可恢复的临界相变阈值 $\text{SNR}_{\text{crit}}$。

---

### 9.3 外生策略干预、结构因果模型与反事实可证伪性

#### 9.3.1 观测性关联与干预性因果的本质断层
现有时序基础模型预训练语料库（如 LOTSA、UTSD、Time-300B、RMISC）绝大多数由**纯被动观测数据 (Observational Data)** 构成。在 Pearl 的三级因果阶梯 (Pearl's Causal Hierarchy) 中，现有时序基础模型仅处于第一级（L1：关联 $P(y|x)$）。
然而在宏观经济调控（央行加息）、医疗临床重症干预（注射血管加压素）、供应链运筹（商品提价促销）等高价值运筹场景中，决策者真正需要回答的是第二级（L2：干预 $P(y \mid do(x))$）与第三级（L3：反事实 $P(y_{x'} \mid x, y)$）问题：
$$\text{若我们在时刻 } T \text{ 强制实施策略 } \mathbf{a}^*, \text{ 未来的物理轨迹将如何演变？}$$

#### 9.3.2 动态反事实结构因果模型 (Dynamic TSCM) 形式化
给定动态时间序列结构因果模型：
$$\mathbf{X}_t = \mathbf{f}_t\left( \mathbf{PA}_t, \mathbf{A}_{t-\tau}, \mathbf{U}_t \right), \quad t=1, 2, \dots$$
其中 $\mathbf{PA}_t$ 为内生父节点历史状态，$\mathbf{A}_{t-\tau}$ 为滞后外生干预动作，$\mathbf{U}_t$ 为不可观测的外生物理噪声。
当被动观测时，模型学习到的是联合伪相关：
$$P(\mathbf{X}_{T+1:T+H} \mid \mathbf{A}_T = \mathbf{a}, \mathbf{X}_{1:T})$$
若存在未测混淆变量 $\mathbf{Z}_t \to \mathbf{A}_t$ 且 $\mathbf{Z}_t \to \mathbf{X}_{t+1}$（例如资深医生根据未记录在结构化数据中的患者脸色苍白提前给药），则被动观测概率与真实因果干预概率产生严重偏离：
$$P(\mathbf{X}_{T+1:T+H} \mid do(\mathbf{A}_T = \mathbf{a}^*), \mathbf{X}_{1:T}) \neq P(\mathbf{X}_{T+1:T+H} \mid \mathbf{A}_T = \mathbf{a}^*, \mathbf{X}_{1:T})$$
如 DoTime [arXiv:2607.27263] 与临床后瞻偏误审计 [arXiv:2609.13454] 所严谨证明：**在标准评测集上得分优异的基础模型，在面对外部策略干预时，预测误差激增数倍，甚至产生与物理事实完全相反的因果倒错**。
此外，全行业共同依赖少数通用 TSFM 所带来的系统集中性脆弱风险 (Concentration Risk [arXiv:2608.24303]) 亦警示：未来必须将因果发现算法、工具变量 (Instrumental Variables)、动态反事实推演引擎与时序大模型深度咬合，建立具备反事实可证伪性的因果基础模型。

---

### 9.4 具身物理遥测、多本体机电动力学与流式毫秒级响应

#### 9.4.1 高频多本体机电系统的维度灾难与流式计算瓶颈
在人形机器人、数控机床与航空航天装备等物理具身实体中，时间序列呈现出与传统统计时序截然不同的极端特性：
1. **超高采样频率 (High-Frequency Sampling)**：力矩传感器、振动加速度计与伺服编码器的采样频率通常高达 $1\text{kHz} - 100\text{kHz}$。仅运行 10 秒钟即可产生 $10^6$ 个时间步长；
2. **标准自注意力的算力与显存崩塌**：传统 Transformer 的二次方注意力计算复杂度 $\mathcal{O}(L^2)$ 与显存开销，在超高频具身场景下导致秒级以上的推断延迟，彻底无法满足工业毫秒级闭环控制 ($< 10\text{ms}$) 的硬实时性要求；
3. **多本体机电动力学的异构尺度与量纲混乱**：不同本体（如 6 自由度机械臂 vs 龙门铣床）在自由度、刚度、传动间隙与传感器量程上差异悬殊。

#### 9.4.2 线性循环状态空间与流式计算破局：TiRex-2 与 Reverso
解决具身流式时序计算瓶颈的核心技术前沿在于**结合循环状态空间 (SSM) 与扩展长短期记忆 (xLSTM) 的线性递推架构**：
- **恒定内存流式递推状态机 (TiRex-2 [arXiv:2607.01204])**：
  将多变量时序映射为矩阵值隐状态 $\mathbf{C}_t \in \mathbb{R}^{d \times d}$ 与法向量 $\mathbf{n}_t \in \mathbb{R}^d$，其状态递推更新式满足：
  $$\mathbf{C}_t = f_t \mathbf{C}_{t-1} + i_t \mathbf{v}_t \mathbf{k}_t^\top, \quad \mathbf{n}_t = f_t \mathbf{n}_{t-1} + i_t \mathbf{k}_t$$
  $$\mathbf{h}_t = o_t \odot \frac{\mathbf{C}_t \mathbf{q}_t}{\max\left(1, |\mathbf{n}_t^\top \mathbf{q}_t|\right)}$$
  在推断期间，每输入一个新的高频传感器数据点，状态递推仅需 $\mathcal{O}(1)$ 的时间复杂度与 $\mathcal{O}(d^2)$ 的恒定内存占用，单步延迟稳定在亚毫秒级 ($< 1\text{ms}$)，从根本上攻克了具身机器人的长程流式推断障碍；
- **参数高效的零样本计算缩放 (Reverso [arXiv:2602.17634])**：
  通过倒置 Transformer 的通道解耦与结构精简，证实了在保持高保真零样本迁移的前提下大幅削减激活参数的可行性，配合端侧微控制器优化基准 (HoliBench [arXiv:2609.12412])，使通用物理模型能够在边缘芯片上低功耗稳定驻留。

---

### 9.5 自主反思闭环智能体与控制论反馈稳定性边界

#### 9.5.1 闭环控制系统中的智能体误差级联与反馈共振
随着从单纯的开环被动时序预测走向具备工具调用、反思重构与动作干预的自主智能体系统（如 TimeClaw [arXiv:2606.05404]、TSQAgent [arXiv:2606.03629]、T-SMART [arXiv:2609.14142]、CastFSR [arXiv:2608.03031]、CTRL [arXiv:2609.23257]），系统本质上构成了一个**由离散大模型认知反馈控制的离散时间动态闭环反馈控制系统 (Closed-Loop Feedback Dynamical System)**。

设物理被控对象的状态方程为：
$$\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k + \mathbf{B}\mathbf{u}_k + \mathbf{w}_k$$
其中 $\mathbf{x}_k$ 为物理状态，$\mathbf{u}_k$ 为控制输入，$\mathbf{w}_k$ 为外界随机过程扰动。
智能体依据历史上下文与预测模型给出控制策略：
$$\mathbf{u}_k = -\mathbf{K}\hat{\mathbf{x}}_k + \mathbf{v}_{\text{agent}}(\mathcal{H}_k)$$
其中 $\mathbf{v}_{\text{agent}}$ 为由 LLM 提示规划、工具检索与反思推理生成的附加调整量。
系统状态跟踪误差 $\mathbf{e}_k = \mathbf{x}_k - \hat{\mathbf{x}}_k$ 的闭环误差动力学方程表述为：
$$\mathbf{e}_{k+1} = (\mathbf{A} - \mathbf{B}\mathbf{K})\mathbf{e}_k + \mathbf{B} \boldsymbol{\delta}_{\text{agent}}(k) + \mathbf{w}_k$$
其中 $\boldsymbol{\delta}_{\text{agent}}(k)$ 表示智能体在多轮思考中产生的幻觉偏误、工具调用延迟与离散跳变扰动。

#### 9.5.2 李雅普诺夫稳定性准则与有界摄动裕度
根据经典控制理论，闭环反馈系统保持渐近稳定或输入-状态稳定 (Input-to-State Stability, ISS) 的充要条件是：
1. **闭环状态转移矩阵谱半径严格小于 1**：
   $$\rho(\mathbf{A} - \mathbf{B}\mathbf{K}) < 1$$
2. **智能体认知决策扰动严格有界**：
   $$\sup_{k} \|\boldsymbol{\delta}_{\text{agent}}(k)\|_\infty \le \epsilon_{\text{robust}} = \frac{1 - \rho(\mathbf{A} - \mathbf{B}\mathbf{K})}{\|\mathbf{B}\|_2 \cdot M_{\text{Lyapunov}}}$$
如果智能体在反思推理过程中产生剧烈幻觉或过激反应（例如突发错误归因导致连续发出激进的反向控制指令），当认知扰动 $\|\boldsymbol{\delta}_{\text{agent}}\| > \epsilon_{\text{robust}}$ 时，**闭环系统将发生反馈共振与误差指数发散，诱发灾难性物理停机**。
如代码智能体时序推理审计 [arXiv:2606.16545] 与人机协同工业智能体 [arXiv:2608.30976] 所警示，未来的核心破局方向在于**将经典鲁棒控制理论、李雅普诺夫能量衰减函数与智能体快慢反思架构严格绑定**，构建具备可证明安全裕度 (Provable Safety Margins) 的确定性闭环时序智能体。

---

### 9.6 全景开放挑战与未来破局路线矩阵

为了系统指引下一阶段时序基础模型与多模态时序智能的理论攻关与工业落地，下表系统性总结了当前学术界与工业界最紧迫的六大开放技术挑战、底层数学根源、典型失效范式、前沿破局路线与关键评测里程碑：

| 开放前沿维度 (Horizon Dimension) | 核心科学瓶颈 (Core Bottleneck) | 理论与数学根源 (Theoretical Root) | 代表性失效范式 (Failure Mode) | 前沿破局路线 (Frontier Breakthrough Path) | 代表文献与成果 (Key References) | 工业与前沿评测里程碑 (Validation Milestones) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. 物理定律与动力学刚性守恒** | 统计自注意力无法保证物理量守恒与相空间辛几何结构 | 自由 Softmax 权重缺乏连续性方程通量约束 $\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = \mathbf{S}$ 与哈密顿变分约束 | 能量自发不守恒、虚假超限加速度、跨本体物理量纲错乱 | 可微连续介质流形投影层、跨频段参数归一化、辛几何神经积分器 | FactoryNet [arXiv:2605.09081], FreqCondNorm [arXiv:2609.20535], VLT [arXiv:2607.14510] | 机床/机械臂/冲压 6 类物理本体动力学保真度评测 |
| **2. 极低信噪比与信息论极限** | 混沌与微观市场信噪比极低，模型在低信噪比下发生预测崩溃 | 互信息随视野指数衰减 $I \propto e^{-\lambda H}$；经验 MSE 驱动后验均值退化 | 预测崩溃为水平均值直线、逆向扩散终端步白噪声过拟合、文本模态注入冗余噪声 | 率失真理论边界 $R(D)$ 建模、频域能量基生成流匹配、逆去噪自适应截断准则 | Forecast Collapse [arXiv:2608.14106], When Denoising Hurts [arXiv:2608.14067], When Does Text Inform? [arXiv:2609.11282] | 基准率无偏评估基准、文本边际互信息消融审计 |
| **3. 外生策略干预与反事实推演** | 被动观测性预训练与主动决策干预之间存在本质断层 | 混淆变量导致观测联合概率偏离因果干预算子 $P(y \mid do(a)) \neq P(y \mid a)$ | 混淆关联当因果、反事实推演严重失真、行业集中性脆弱风险 (Concentration Risk) | 动态 TSCM 因果图学习、时间序列结构因果模型与反事实潜在结果推演三步法 | DoTime [arXiv:2607.27263], Causal Analysis [arXiv:2608.24303], Clinical Hindsight [arXiv:2609.13454] | 严格硬干预外生测试、临床后瞻偏误双盲审计 |
| **4. 高频具身遥测与毫秒流式响应** | 机器人与机电高频传感导致注意力二次方复杂度 $\mathcal{O}(L^2)$ 崩溃 | 序列长度 $L > 10^5$ 引发显存溢出与推断延迟剧增，无法满足闭环硬实时 | 毫秒级控制延迟超限、上下文窗口硬截断、边缘端内存爆炸 | 矩阵状态循环扩展 LSTM (xLSTM)、倒置 Transformer 参数高效计算缩放、无注意力 SSM | TiRex-2 [arXiv:2607.01204], Reverso [arXiv:2602.17634], EXAONE Fin [arXiv:2609.04239], HoliBench [arXiv:2609.12412] | 亚毫秒级流式推断延迟测试、端侧边缘硬件能效审计 |
| **5. 控制论反馈稳定性与智能体闭环** | 智能体多轮反思干预引发闭环误差级联与反馈发散 | 闭环误差动态系统谱半径 $\rho(\mathbf{A}-\mathbf{B}\mathbf{K}) \ge 1$ 或智能体认知摄动超限 | 误差累积爆炸、过激震荡失控、工具调用链幻觉扩散 | 李雅普诺夫反馈稳定性约束、可验证奖励后训练 (RLVR)、机制级工具因果归因 | CastFSR [arXiv:2608.03031], CTRL [arXiv:2609.23257], TimeClaw [arXiv:2606.05404], TSQAgent [arXiv:2606.03629], T-SMART [arXiv:2609.14142] | 动态闭环环境持续演化评测、代码智能体长程沙箱测试 |
| **6. 宏观数据版本修订与因果前瞻隔离** | 历史版本修订穿越与预训练未来数据泄漏引发虚假繁荣 | 全局双向归一化与未来数据掩码预训练破坏单向物理时间箭头 | 生产环境性能断崖式滑坡、负迁移 (Negative Transfer)、前瞻偏误作弊 | 实时快照历史切片 (Vintage Data) 预训练、单向因果窗口归一化、证据访问边界审计 | MACROCAST [arXiv:2606.28670], VINTAGE-TS [arXiv:2609.28576], Look-Ahead Bias [arXiv:2609.20554], Tracing Evidence [arXiv:2609.21425] | 真实实时截断回测、前瞻污染严格对照消融 |


## 10 参考文献

本综述所引用的全部文献均通过 arXiv HTTPS API 严格核验并收录于 [`data/papers.json`](../data/papers.json)，同时自动化生成 BibTeX 数据库 [`survey/references.bib`](references.bib)。

""" + references_md + r"""

---

## 版本变更日志 (Changelog)

- **2026-09-26 (第 8 轮迭代：开放问题与未来前沿理论深化、15 篇前沿收录与全景矩阵扩充 / Iteration 8)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，总文献库扩展至 **183 篇**；代码链接全部经由 GitHub API 官方核验（如 TimeClaw [arXiv:2606.05404] 等，未开源则严格置 null）；
  - **核心深化：全面重构并深度强化第 9 章（开放问题与未来方向）**：
    - 9.1 建立物理定律与动力学刚性守恒约束的时空神经物理融合形式化，严格推导质量/动量/能量连续性方程与哈密顿保辛几何约束，剖析自由自注意力机制与经典力学公理的本质冲突，提出可微流形投影与多模态物理表征破局路线（FactoryNet [arXiv:2605.09081], FreqCondNorm [arXiv:2609.20535], VLT [arXiv:2607.14510]）；
    - 9.2 从信息论视角严格推导时序可预测性上界与互信息指数衰减律 $I \propto e^{-\lambda H}$，形式化揭示均方误差下“预测崩溃 (Forecast Collapse)”退化为平庸直线的临界信噪比相变机理，结合逆向扩散终端步漂移与多模态文本信息论基准（Forecast Collapse [arXiv:2608.14106], When Denoising Hurts [arXiv:2608.14067], When Does Text Inform? [arXiv:2609.11282], Base-Rate Honest TimesFM [arXiv:2607.12248]）；
    - 9.3 形式化动态时序结构因果模型 (Dynamic TSCM) 与 Pearl 反事实硬干预算子 $do(\mathbf{a}^*)$，揭示观测预训练数据的根本混淆偏差与行业集中性脆弱风险（DoTime [arXiv:2607.27263], Causal Analysis [arXiv:2608.24303], Clinical Hindsight Bias [arXiv:2609.13454]）；
    - 9.4 剖析具身机器人与机电高频遥测的二次方算力与显存崩塌，推导具备 $\mathcal{O}(1)$ 单步时间复杂度与 $\mathcal{O}(d^2)$ 恒定内存的 xLSTM 矩阵状态流式递推架构与参数高效零样本计算缩放（TiRex-2 [arXiv:2607.01204], Reverso [arXiv:2602.17634], HoliBench [arXiv:2609.12412]）；
    - 9.5 建立时序决策智能体离散时间动态闭环反馈控制系统与误差动力学方程，严格推导李雅普诺夫渐近稳定性准则与认知摄动界 $\epsilon_{\text{robust}}$，防范误差级联发散（TimeClaw [arXiv:2606.05404], TSQAgent [arXiv:2606.03629], T-SMART [arXiv:2609.14142], CastFSR [arXiv:2608.03031], CTRL [arXiv:2609.23257], Coding Agent TS Reasoning [arXiv:2606.16545]）；
    - 9.6 首创构建 **9.6 全景开放挑战与未来破局路线矩阵 (Table 9.1)**，跨 6 大核心科学维度全面解构科学瓶颈、数学根源、失效范式、破局路线与关键评测里程碑。
  - **全景融合 15 篇新增文献至各大章节**：
    - 第 4 章：TiRex-2 多变量流式架构 [arXiv:2607.01204]、Reverso 参数高效零样本缩放 [arXiv:2602.17634]、VLT 工业三模态大模型 [arXiv:2607.14510]；
    - 第 5 章：R-AF 模型无关检索增强长视野预测 [arXiv:2608.14054]；
    - 第 6 章：TimeClaw 上下文智能体 [arXiv:2606.05404]、TSQAgent 数据质量诊断智能体 [arXiv:2606.03629]、T-SMART 机制级归因系统 [arXiv:2609.14142]、SAGE 变量级语义增强 [arXiv:2608.26829]、Solar-Sky-TS 地空双向融合 [arXiv:2609.11135]、VLT 工业智能大模型 [arXiv:2607.14510]；
    - 第 7 章：When Does Text Inform? 信息论评测 [arXiv:2609.11282]、Base-Rate Honest TimesFM 金融无偏基准 [arXiv:2607.12248]、Clinical Hindsight Bias 临床后瞻偏误基准 [arXiv:2609.13454]、Crowd Count Benchmark 客流密集度基准 [arXiv:2609.16415]、Candlestick VLMs 蜡烛图视觉真伪评测 [arXiv:2604.12659]、Coding Agent TS Reasoning 代码智能体时序推理评测 [arXiv:2606.16545]；
  - **全套图表与质量门禁**：
    - 重新核验并生成全套 5 组 300 DPI 图表 (PNG & SVG)，包括时序大模型里程碑时间线、多模型参数规模演进、四维分类树状图、开源/闭源份额与年度领域分布，全面消解密集标注重叠；
    - 通过全部质量门禁：`validate.py` (183 papers)、`survey_check.py` (全章节、全图表与所有 183 个 arXiv 引用 100% 存在且吻合)、自动生成 `README.md` 与 `references.bib`。
- **2026-09-26 (第 7 轮迭代：分类体系全景重构与五大计算范式数学深化、15 篇前沿收录与图表质检 / Iteration 7)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，总文献库扩展至 **168 篇**；代码链接全部经由 GitHub API 官方核验（如 Aionoscope [arXiv:2607.00956]、DynG-Diff [arXiv:2609.02068]、Retrieval Regime [arXiv:2609.20193]、TSPFN [arXiv:2608.31013] 等）；
  - **核心深化：全面重构并深化第 3 章（分类体系）**：
    - 3.1 形式化定义四维正交分类理论设计空间 $\mathcal{S} = \langle \mathcal{A}, \mathcal{T}, \mathcal{M}, \mathcal{E} \rangle$；
    - 3.2 深度解构五大核心计算范式（因果自回归解码器、双端编码-解码器、纯双向编码器掩码自编码、稀疏 MoE 与频域路由、连续动力学/扩散生成/先验拟合）的因果掩码、损失目标与设计权衡；
    - 3.3 严格推导连续补丁化、离散分箱量化、频域复数小波、形态基元与跨频段自适应归一化 (FreqCondNorm) 的度量与计算权衡；
    - 3.4 形式化通道拓扑演化路径：从通道独立 (CI) 到通道依赖 (CD)、任意变量统一 (vRoPE Any-variate) 到动态状态引导 (DynG-Diff) 与共识特征拓扑 (IPM-FM)；
    - 3.5 首创 **3.5 时序基础模型多维技术分类对比矩阵**，涵盖 12 种主流技术路线、跨 8 个核心维度的全景横向技术解构。
  - **全景融合 15 篇新增文献至各大章节**：
    - 第 3/4 章：DynG-Diff 动态引导扩散 [arXiv:2609.02068]、OutageDiT 停电仿真大模型 [arXiv:2609.01896]、When Denoising Hurts 终端步去噪反思 [arXiv:2608.14067]、TabPFN-TS 区域供热评测 [arXiv:2608.20024]、TSPFN 生理分类基础模型 [arXiv:2608.31013]、IPM-FM 工业监控基础模型 [arXiv:2609.08375]、FreqCondNorm 跨频段预测维护 [arXiv:2609.20535]、ORBIT 预训练机制基准 [arXiv:2608.13262]；
    - 第 5 章：时序检索增强有效性临界区间研究 [arXiv:2609.20193]；
    - 第 6 章：Salesforce 时序智能体全景综述 [arXiv:2608.26226]、MetaCaster 元演化智能体 [arXiv:2608.23473]、CompEvo 竞争诱导演化系统 [arXiv:2609.09195]、人机协同工业智能体 [arXiv:2608.30976]；
    - 第 7 章：Aionoscope 隐状态可访问性审计 [arXiv:2607.00956]、深度时序模型记忆容量理论审计 [arXiv:2609.06006]；
    - 第 8 章：金明团队纳入 Aionoscope [arXiv:2607.00956]、Salesforce 团队纳入智能体全景综述 [arXiv:2608.26226]；
  - **全套图表与质量门禁**：
    - 重新核验并生成全套 5 组 300 DPI 图表 (PNG & SVG)，包括时序大模型里程碑时间线、多模型参数规模演进、四维分类树状图、开源/闭源份额与年度领域分布；
    - 通过全部质量门禁：`validate.py` (168 papers)、`survey_check.py` (全章节、全图表与所有 168 个 arXiv 引用 100% 存在且吻合)、自动生成 `README.md` 与 `references.bib`。
- **2026-09-26 (第 6 轮迭代：重点课题组全景矩阵深化、底层数学理论四维推导、15 篇前沿收录与图表重构 / Iteration 6)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，总文献库扩展至 **153 篇**；代码链接全部经由 GitHub API 官方核验（如 PaCoDi [arXiv:2602.17706]、CastFSR [arXiv:2608.03031] 等）；
  - **核心深化一：全面重构并深化第 8 章（重点课题组与代表机构进展）**：
    - 独立专节系统梳理 **清华大学 THUML 龙明盛团队** (8.1) 全栈脉络（Timer, Timer-XL, Timer-S1, Sundial, TimesBERT, DiTS, Accuracy Law, TimeAgent）；
    - 独立专节深度剖析 **金明团队 (Ming Jin Group)** (8.2) 全景矩阵（Time-LLM, Time-MoE, LeapTS, PaCoDi, ChatAD, TimeOmni-VL, AION, EventCast, EOB, LeNEPA）；
    - 独立专节系统剖析 **亚马逊 AWS Chronos 团队** (8.3)（Chronos, Chronos-2, FedChronos, KG-Chronos-2, AutoGluon）；
    - 独立专节系统剖析 **Salesforce Research Moirai 团队** (8.4)（Moirai, Moirai-MoE, Moirai 2.0, LOTSA, GIFT-Eval）；
    - 独立专节系统剖析 **谷歌研究院 TimesFM 团队** (8.5)（TimesFM, TimesFM-3, Cadence）；
    - 独立专节系统剖析 **IBM Research 与 CMU 团队** (8.6)（TTM 极简轻量多尺度 Mixer 与 MOMENT 纯编码器掩码双向表征）；
    - 独立专节系统剖析 **Datadog Toto 团队** (8.7)（万亿点全真实云原生遥测大模型 Toto 2.0 与标度律实证）；
    - 首创 **8.8 重点课题组与代表机构综合对比矩阵**，从学术哲学、技术主张、分词机制、损失函数、预训练语料规模、最大公开模型参数量、核心理论创新到开源生态开展 8 维度全景横向解构。
  - **核心深化二：全面深化第 2 章底层数学理论与公式形式化推导**：
    - 2.5 预测精度定律与窗口模式复杂度 (Accuracy Law & Pattern Complexity) [arXiv:2510.02729]：推导模式复杂度 $\mathcal{C}_P$（谱熵与局部曲率加权）、精度定律解析幂律函数 $\mathcal{E}(L, H)$ 与三阶段演化区间（信息匮乏、法定缩放、稀释饱和）；
    - 2.6 逐点损失优化偏误与经验优化偏差 (Optimization Bias EOB & Debiasing) [arXiv:2512.18610]：推导在相位随机性扰动下逐点 MSE 导致高频指数衰减 $\exp(-\frac{1}{2}\omega^2\sigma_\tau^2)$ 的数学机理（普洛克路斯忒斯之床），形式化频域谱匹配与梯度对齐的结构去偏目标 $\mathcal{L}_{\text{Debiased}}$；
    - 2.7 决策论预训练与有限样本贝叶斯风险极小化 (The Simulacrum) [arXiv:2606.27711]：形式化统计决策论行动空间、后验期望风险与先验随机过程分布族上的有限样本贝叶斯风险，证明 $\mathcal{O}(1/\sqrt{M})$ 收敛界与零样本近最优决策；
    - 2.8 反事实时序结构因果模型形式化 (Counterfactual & Interventional TSCMs, DoTime) [arXiv:2607.27263]：建立四元组动态 TSCM、Pearl do-演算时序硬干预算子与外生噪声溯源反事实潜在结果推导三步法。
  - **全景融合 15 篇新增文献至各大章节**：
    - 第 4 章：并行复数扩散 PaCoDi [arXiv:2602.17706]、1420 亿点真实多变量语料库 RMISC [arXiv:2607.06504]、决策论模型 The Simulacrum [arXiv:2606.27711]；
    - 第 5 章：时序动力学蒸馏 T-LLM [arXiv:2602.01937]、控制论引导残差预测 CTRL [arXiv:2609.23257]、认知推理对齐 TS-Reasoner [arXiv:2510.03519]；
    - 第 6 章：电商事件知识图谱预测 EventCast [arXiv:2602.07695]、快慢反思双系统 CastFSR [arXiv:2608.03031]、递归语言模型精准异常定位 TimeRLM [arXiv:2608.03391]、时序预测大模型智能体系统全景综述 [arXiv:2608.23058]；
    - 第 7 章：多模态文本敏感度实证审计 [arXiv:2608.22321]、现代概率预测系统综述 [arXiv:2609.13345]、DoTime 反事实干预评测基准 [arXiv:2607.27263]；
  - **全套图表与质量门禁**：
    - 重新运行生成全套 5 组 300 DPI 高清图表 (PNG & SVG)，包括时序大模型里程碑演化时间线、多模型参数规模演变、分类体系树、开源/闭源份额与年度领域分布；
    - 通过全部质量门禁：`validate.py` (153 papers)、`survey_check.py` (全章节、全图表与所有 arXiv 引用 100% 存在且吻合)、自动生成 `README.md` 与 `references.bib`。
- **2026-09-26 (第 5 轮迭代：时序原生基础模型全面数学深化、15 篇前沿收录与全景矩阵扩充 / Iteration 5)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，文献库增至 138 篇；
  - 全面深化第 4 章（时序原生基础模型 Native TSFMs）：推导离散分箱交叉熵 vs 连续 Huber 回归损失；推导 Any-variate 跨通道注意力与变量感知旋转位置编码 (vRoPE)；推导 Sundial 连续流匹配 (TimeFlow CFM)；推导稀疏 MoE Top-$k$ 门控、辅助负载均衡与小波子带路由 (WaveMoE) 与 Olivia 功率谱密度协调；推导 LeapTS 连续 Neural CDE 动态调度与 Cadence 误差有界预测残差压缩；
  - 扩充 CITRAS-FM (7M)、Zeus、Falcon-X、MACROCAST、VersaTSA (30B)、MILM、PostTime、Chronicle、SCENARIODIFF、TS-Debate 等；
  - 重新核验并生成全套 5 组 300 DPI 图表，消解时间线密集标注前缘微小重叠，同步更新 README.md 与 references.bib。
- **2026-09-26 (第 4 轮迭代：多模态时序与智能体深度演进、具身物理时序突破、前沿 15 篇收录与图表重构 / Iteration 4)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，文献库增至 123 篇；
  - 全面深化第 6 章（多模态时序与智能体演进）：构建 14 种主流系统全景对比矩阵；推导 57 页统一大模型 TimeBraid 交错残差注意力与联合优化；剖析 GALA 扩散合成；建立 POMDP 形式化，深入剖析 ReasonCast、ChatAD、TimEvolve、AION；首次深度剖析 FactoryNet 具身工业基石；
  - 重新核验并生成全套 5 组 300 DPI 图表，同步更新 README.md 与 references.bib。
- **2026-09-25 (第 3 轮迭代：大语言模型赋能时序全面深化、前沿 15 篇收录与图表重构 / Iteration 3)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，文献库增至 108 篇；
  - 全面深化第 5 章（大语言模型赋能时序）：构建 12 维综合范式矩阵对比表；推导补丁重编程；给出 Align-RAG 闭式无训练仿射对齐解析解；引入免梯度可迁移性预估理论；
  - 重新核验并生成全套 5 组 300 DPI 图表，同步更新 README.md 与 references.bib。
- **2026-09-24 (第 2 轮迭代：评测体系全面深化与重点团队前沿纳入 / Iteration 2)**:
  - 严格通过 arXiv HTTPS API 核验收录 14 篇最新前沿与重点团队论文，文献库增至 93 篇；
  - 全面深化第 7 章（基准与评测）：新增评测基准综合对比矩阵表；剖析预训练熟悉度危机、证据访问边界零样本审计、概率校准与动态演化环境评测；
  - 重新生成并质检全部 5 套 300 DPI 图表。
- **2026-09-24 (初版发布 / First Full Edition)**:
  - 从零构建系统性活体综述 (`survey/SURVEY.md`)，覆盖十大核心章节与 LaTeX 形式化数学定义；
  - 严格通过 arXiv HTTPS API 核验收录 79 篇时序基础模型与多模态时序文献；
  - 编写并生成 5 套高分辨率可复现图表 (PNG+SVG) 并完成排版视觉质检。

---

## TODO 后备待办论文池 (TODO Backlog)

下述论文候选与前沿技术方向已在日常巡检中建立索引，将在后续轮次中进一步评估纳入或扩展分析：
1. **多模态图表看图预测跨分辨率超轻量化**：探索在边缘视觉芯片上实现微秒级视觉时间序列掩码推断与形态保真；
2. **时序因果结构发现与反事实推演统一架构**：结合 DoTime 等因果生成基准，攻克 TSFMs 在外生干预下的泛化理论下界；
3. **具身多本体触觉-力觉物理遥测跨模态大模型**：持续追踪通用人形机器人动力学与重工业机电融合的超高频时序动力学表征；
4. **时序多尺度自适应微调理论**：跟进参数高效迁移中的频域秩约束与自适应奇异值截断前沿；
5. **TimeMixer++ 永久公开开源状态跟进**：持续监测官方仓库公司合规审查与权重发布进展。
"""

full_content = part1 + part2 + part3 + part4 + part5 + part6

SURVEY_PATH.write_text(full_content, encoding="utf-8")
print(f"Successfully generated {SURVEY_PATH} ({len(full_content)} chars, {len(paper_map)} papers).")
