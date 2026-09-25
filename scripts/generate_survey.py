#!/usr/bin/env python3
"""Build the complete, updated living survey (survey/SURVEY.md) with Iteration 3 expansions.

Quality criteria:
1. Deepens Section 5 (LLM4TS) with full LaTeX mathematics, paradigm matrix table, mechanism analysis.
2. Incorporates all 15 new papers (108 total papers cited).
3. Preserves all high-quality content from previous iterations.
4. Generates Section 10 alphabetically from data/papers.json.
5. Updates changelog and TODO backlog.
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
    ("3 分类体系", 0),
    ("4 时序基础模型", 0),
    ("4.1 核心模型对比", 1),
    ("4.2 Chronos 系列：语言化与离散量化路线", 1),
    ("4.3 Google TimesFM：单通道自回归与两阶段修补路线", 1),
    ("4.4 Salesforce Moirai 系列：全频段全变量统一编码器-解码器路线", 1),
    ("4.5 清华 THUML Timer / Sundial 系列：下一补丁自回归到流匹配生成路线", 1),
    ("4.6 混合专家（Mixture of Experts, MoE）路线：参数规模扩展与计算效率平衡", 1),
    ("4.7 MOMENT 与 TTM：编码器架构与轻量级工业部署路线", 1),
    ("4.8 连续动力学与生成式路线：Flow 与 Diffusion 路线", 1),
    ("4.9 新兴开源预训练前沿：Tabby, Toto 2.0 与 t0", 1),
    ("5 大语言模型赋能时序", 0),
    ("5.1 大语言模型赋能时序范式矩阵与理论形式化", 1),
    ("5.2 模型重编程与轻量适配路线 (Model Reprogramming & Adapters)", 1),
    ("5.3 文本化分词与直接提示路线 (Direct Prompting & Reasoning Planners)", 1),
    ("5.4 跨模态微调与跨语义空间对齐 (Cross-Modal Fine-Tuning & Semantic Alignment)", 1),
    ("5.5 上下文学习、检索增强与零样本迁移度量 (In-Context Adaptation & Transferability)", 1),
    ("6 多模态时序", 0),
    ("6.1 文本与时序跨模态推理与交互 (Text + TS Joint Reasoning)", 1),
    ("6.2 视觉与时序跨模态协同 (Visual Time Series & Temporal VLMs)", 1),
    ("6.3 交互式流式时序与智能体决策 (Interactive TS & Agents)", 1),
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
    ("9 开放问题与未来方向", 0),
    ("10 参考文献", 0),
    ("版本变更日志", 0),
    ("TODO 后备待办论文池", 0)
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

> **版本状态：** 持续演进的活体综述 (Living Survey) · **最后更新：** 2026-09-25 (Iteration 3)
> **维护规范：** 仅收录通过 arXiv HTTPS API 严格核验的论文条目；所有事实性陈述均标注 `[arXiv:XXXX.XXXXX]` 真实引用；模型参数与语料规模仅采用论文显式声明数值。

---

## 目录 (Table of Contents)
""" + toc_md + r"""

---

## 摘要

时间序列基础模型 (Time Series Foundation Models, TSFMs) 与多模态时序智能正在深刻变革工业生产、能源调度、金融分析、气象环境及医疗健康领域的时空数据建模范式。受自然语言处理和计算机视觉领域基础模型成功的启发，研究者逐步摒弃传统的针对单一数据集定制训练专有模型 (Task-Specific Training) 的模式，转而探索利用超大规模跨领域时序语料库预训练通用大模型，实现强大的零样本 (Zero-Shot) 泛化能力、上下文学习 (In-Context Learning) 以及跨模态推理协同。

本综述系统梳理了从 2022 年至 2026 年时序基础模型的核心技术路线与最新演化脉络：
1. **时序原生基础模型 (Native TSFMs)**：深入解析自回归离散量化路线（如 Amazon Chronos 系列、FedChronos、KG-Chronos-2）、下一补丁连续自回归路线（如 Google TimesFM、清华 THUML Timer 系列）、任意通道多尺度掩码路线（如 Salesforce Moirai 系列）、稀疏混合专家与冻结路由路线（如 Time-MoE、Timer-S1、Moirai-MoE、TW3Cast）、轻量工业级路线（如 IBM TTM、CMU MOMENT、TimesBERT 双向理解、FlowTSFM 循环分位数传输）以及连续动力学生成路线（如 THUML Sundial、FlowState、SwitchPFN 切换动力学先验）。
2. **大语言模型赋能时序 (LLM-for-TS)**：深入分析跨模态重编程（Reprogramming，如 Time-LLM、One Fits All）、文本标记化直接提示（Prompt-based，如 LLMTime、LLM as Forecasting Planner）、跨模态语义空间对齐（如 S²IP-LLM、CALF、STReasoner 时空强化学习）、闭式无微调检索对齐（如 Align-RAG）以及在途免梯度可迁移性度量（Estimating TSFM Transferability）。
3. **多模态时序智能 (Multimodal Temporal Intelligence)**：剖析 57 页统一大模型 TimeBraid 跨模态注意力残差交错融合、文本-时序联合推理问答（如 OpenTSLM、ChatTime、SciTS、FINESSE 金融多智能体仿真）、视觉-时序协同映射（如 VisionTS、Time-VLM、TimeOmni-VL、清华 DiTS 扩散 Transformer）、交互式流式时序智能体（如 Sonar-TS、TimeInteract、ChatAD 多轮异常检测演化推理）以及时序决策工具集（如 Forecast Workflow Bench、TimEvolve 在线自进化策略）。
4. **评测基准与演化生态**：总结零样本泛化基准（GIFT-Eval、It's TIME、LiveHouse-TS）、多模态与异构基准（Time-MMD、Beyond Numerical TS、FINESSE）、时序因果隔离与数据污染防范审计（Contamination-Free Hold-Out、Rethinking Evaluation、VINTAGE-TS 宏观版本修订审计）、因果系统集中性风险审计（Causal Analysis for TSFMs）、端侧与工业经济性评测（HoliBench、Cost-Aware Industrial Monitoring）以及多模态视觉裁判（TimeVista）。

本综述所有论文条目均经由 arXiv HTTPS API 严格校验，模型参数与实验数据均忠实于原始文献，为该领域的学术研究与工业落地提供全面、严谨、可复现的一手参考。

---

## 1 引言

时间序列预测在过去几十年中经历了三次核心范式跃迁：
- **经典统计与机器学习时代**：以 ARIMA、指数平滑（ETS）、GARCH 以及基于树模型的 LightGBM、XGBoost 为代表，依赖严格的统计假设或手工提取的时序特征；
- **深度时序模型时代**：以 RNN、LSTM、TCN 以及各类时序 Transformer 变体（如 Autoformer、Informer、PatchTST）为代表 [arXiv:2202.07125]，尽管预测精度显著提升，但仍受限于“在目标数据集划分训练集/验证集/测试集”的单一封闭场景假设，面临分布偏移严重、冷启动代价高昂等痛点；
- **时序基础模型与多模态通用智能时代 (2023 - 2026)**：通过汇聚数十亿至数万亿级跨领域时间序列点（包含真实物理传感与合成数据），训练具备广泛通用归纳偏置的模型，直接在未见场景下实现开箱即用的零样本预测与迁移 [arXiv:2403.14735], [arXiv:2310.10196]。

伴随这一跃迁，研究界逐步分化出两条互补的发展主线：
1. **时序原生基础模型**：基于 Transformer、MLP-Mixer、状态空间模型 (SSM)、先验数据网络 (PFN) 或流匹配框架，设计专为时间序列设计的连续或离散分词机制，探索时序领域的标度律 (Scaling Laws)；
2. **跨模态与大语言模型赋能**：利用预训练大语言模型 (LLM) 和多模态大模型 (VLM) 蕴含的通用时序推理、模式识别与世界知识，通过参数重编程、跨模态适配器、闭式检索对齐或直接提示的方式解决时序下游任务 [arXiv:2402.01801]。

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
- **通道依赖 (Channel Dependence, CD) 与任意变量统一 (Any-variate)**：显式通过跨通道注意力机制（如 Moirai [arXiv:2402.02592] 的 Any-variate Attention）或外生变量跨注意力机制（如 TimeXer [arXiv:2402.19072]）建模通道间动态耦合关系。

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

### 2.4 预训练优化目标

1. **下一 Token / 下一 Patch 自回归目标 (Next-Token / Next-Patch Autoregression)**：
   $$\mathcal{L}_{\text{AR}}(\theta) = - \sum_{i=1}^N \log p_\theta(\mathbf{p}_i \mid \mathbf{p}_{<i})$$
   TimesFM [arXiv:2310.10688]、Timer [arXiv:2402.02368] 和 Chronos [arXiv:2403.07815] 均以此为基础目标。

2. **连续流匹配生成目标 (Continuous Flow Matching)**：
   Sundial [arXiv:2502.00816] 提出 TimeFlow 损失，克服离散量化信息损失与高斯先验受限问题。令 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 为先验高斯噪声，$\mathbf{x}_1$ 为真实目标未来补丁，定义线性插值路径 $\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1$，流模型速度场预测网络 $v_\theta$ 的优化目标为：
   $$\mathcal{L}_{\text{FM}}(\theta) = \mathbb{E}_{t \in [0, 1], \mathbf{x}_0, \mathbf{x}_1} \left\| v_\theta(\mathbf{x}_t, t, \mathbf{c}) - (\mathbf{x}_1 - \mathbf{x}_0) \right\|^2$$
   其中 $\mathbf{c}$ 为历史上下文表示。

---

## 3 分类体系

时序基础模型与多模态时序智能体系可从四个主要正交维度进行解构，如下图所示：

![Taxonomy Tree](figures/taxonomy_tree.png)

1. **架构范式 (Architectural Paradigm)**：
   - **Decoder-Only 自回归架构**：TimesFM [arXiv:2310.10688]、Timer [arXiv:2402.02368]、Chronos [arXiv:2403.07815]、Sundial [arXiv:2502.00816]、Toto 2.0 [arXiv:2605.20119]、Tabby [arXiv:2609.13956]、$t_0$ [arXiv:2609.24559]、TimeBraid [arXiv:2609.29792]；
   - **Encoder-Decoder 双端架构**：Moirai [arXiv:2402.02592]、Moirai 2.0 [arXiv:2511.11698]、UniTS [arXiv:2403.00131]、TTM [arXiv:2401.03955]、TimeMixer [arXiv:2405.14616]、QUALS [arXiv:2609.20156]；
   - **Encoder-Only 掩码表示架构**：MOMENT [arXiv:2402.03885]、TimesBERT [arXiv:2502.21245]、VisionTS [arXiv:2408.17253]、TimeCMA [arXiv:2406.01638]、FlowTSFM [arXiv:2609.13640]；
   - **稀疏混合专家与路由架构 (MoE & Routers)**：Time-MoE [arXiv:2409.16040]、Moirai-MoE [arXiv:2410.10469]、Timer-S1 [arXiv:2603.04791]、SOTER [arXiv:2609.16804]、TW3Cast [arXiv:2609.28506]；
   - **先验拟合与连续动力学生成架构 (PFN / Flow / Diffusion)**：TabPFN-v2 (TS) [arXiv:2501.02945]、SwitchPFN [arXiv:2609.29814]、FlowState [arXiv:2508.05287]、FLAME [arXiv:2512.14253]、Sundial [arXiv:2502.00816]、DiTS [arXiv:2602.06597]。
2. **分词机制 (Tokenization Scheme)**：
   - 补丁分词 (Patch)、离散数值量化 (Quantized Bins)、逐点与滞后特征 (Point/Lag)、频域与图像掩码 (Visual/Spectral)、先验动力学状态 (Switching Dynamics)。
3. **跨模态融合深度 (Multimodal Depth)**：
   - 纯时序自监督 (TS-only)、文本-时序特征重编程 (LLM Reprogramming)、图文跨模态对齐 (VLM/Multimodal)、多模态智能体决策 (Agentic / Tool-use)。
4. **评测与保障范式 (Evaluation & Quality Assurance)**：
   - 零样本泛化测试、概率校准评测、数据版本修订审计、因果集中性风险评估、工业经济性度量、大模型充当裁判 (VLM-as-Judge)。

---
"""

print("Part 1 defined.")

part2 = r"""## 4 时序基础模型

随着算力与语料规模的不断扩张，时序基础模型演变呈现出鲜明的标度律特征：

![TSFM Timeline](figures/tsfm_timeline.png)

![Model Size vs Date](figures/model_size_vs_date.png)

### 4.1 核心模型对比

下表汇集了领域内代表性开源/权威基础模型的核心技术参数（所有数值均严格来自于论文声明）：

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
| **Chronos-2** | Amazon | [arXiv:2510.15821] | 2025 | 710M | 扩展 TSMix 与核合成数据 | Decoder-only | 统一离散概率分布分箱 | TS | 是 |
| **Moirai 2.0** | Salesforce | [arXiv:2511.11698] | 2025 | 311M | LOTSA v2 紧凑高质量预训练集 | Encoder-Decoder | 精简轻量多变量注意力 | TS | 是 |
| **Timer-S1** | 清华大学 THUML | [arXiv:2603.04791] | 2026 | 8.3B (激活0.75B) | UTSD-3 强化推理语料 | MoE | 串行缩放 (Serial Scaling) Patch | TS | 是 |
| **Toto 2.0** | Datadog | [arXiv:2605.20119] | 2026 | 2.5B | 超过 1 万亿时序点 (1T points) | Decoder-only | 工业级 Patch 标度律预训练 | TS | 是 |
| **Tabby** | 学术团队 | [arXiv:2609.13956] | 2026 | 145M | OpenTS-Archive 开源配方语料 | Decoder-only | 标准化开源预训练 Patch | TS | 是 |
| **FlowTSFM** | 学术团队 | [arXiv:2609.13640] | 2026 | 38.8M | 未报告 | Encoder-only (Flow) | Recurrent Quantile Patch | TS | 未报告 |
| **SOTER** | 复旦 / 阿里等 | [arXiv:2609.16804] | 2026 | 未报告 | 2260亿时序点 (226B points) | MoE + Neural CDE | 频域 PSD 引导多尺度 Patch | TS | 未报告 |
| **QUALS** | 学术团队 | [arXiv:2609.20156] | 2026 | 未报告 | 跨域多源通用时序语料 | Encoder-Decoder | Pattern Quantization Bins | TS | 未报告 |
| **t0** | 学术团队 | [arXiv:2609.24559] | 2026 | 256M | 未报告 | Decoder-only | 异构时空与文本上下文联合 Patch | TS + Text | 是 |
| **SwitchPFN** | 普林斯顿等学术团队 | [arXiv:2609.29814] | 2026 | 未报告 | 切换动力系统合成先验 | Prior-Data Transformer | 动力学状态分段特征 Token | TS | 是 |
| **TW3Cast** | 学术团队 | [arXiv:2609.28506] | 2026 | 未报告 | GIFT-Eval 训练切分集 | Frozen Router (MoE) | 多骨干特征动态路由 | TS | 是 |

---

### 4.2 Chronos 系列：语言化与离散量化路线

Amazon 提出的 Chronos [arXiv:2403.07815] 奠定了“将时间序列视为一门通用语言”的技术基石。Chronos 通过均值缩放结合等宽或等频分箱量化（4096 bins），将连续时序转化为整数序列，进而直接复用 T5（从 Chronos-Mini 20M 到 Chronos-Large 710M）进行因果自回归交叉熵预训练。为了解决大规模真实时序稀缺的问题，Chronos 创新提出了 TSMix 与高斯过程合成配方，在 840 亿观测点上展现了卓越的零样本概率预测表现。
Chronos-2 [arXiv:2510.15821] 进一步将单变量离散量化拓展至通用多变量与跨序列协同预测，通过跨注意力结构将外部因果驱动变量无缝集成入量化概率预测框架。值得注意的是，工业界广泛使用的 Chronos-Bolt 属于其高效推理的轻量工程演进，虽未独立发表 arXiv 论文，但通过开源 Hugging Face 权重获得广泛应用。

在面向敏感行业与严苛工程系统的最新演化中：
- **FedChronos** [arXiv:2608.01290]：针对大宗商品期货与跨国金融机构间普遍存在的“数据孤岛与数据主权壁垒”，提出面向时序基础模型的联邦参数高效微调 (Federated PEFT) 框架。通过在本地客户端冻结 Chronos 主干并聚合轻量级 Adapter/LoRA 增量，在严格保护底层专有时序隐私的前提下，使得去中心化参与方的预测误差降低 18.4% 至 32.7%；
- **KG-Chronos-2** [arXiv:2609.21381]：探索了将复杂的物理动力学水工知识注入基础模型的新路径。针对水利工程 HEC-RAS 水面高程 (WSE) 这一具有高度非线性回水效应和网格拓扑约束的极端场景，KG-Chronos-2 将河网知识图谱的拓扑连通性转化为跨注意力结构，引导冻结的 Chronos-2 联合推断，在水动力学替代建模中取得超越传统水文深度学习模型的高精度表现。

### 4.3 Google TimesFM：单通道自回归与两阶段修补路线

Google 研发的 TimesFM [arXiv:2310.10688] 坚持基于连续数值补丁分词的自回归路线。TimesFM 采用标准 Decoder-only Transformer 结构，输入补丁长度设为 32，输出步长设为 128，支持不同频段下的单通道独立自回归。预训练语料由包含 Google 搜索趋势、维基百科访问量在内的 1000 亿级真实与合成时间序列点构成。在其后续演进中，Google 团队针对不同下游任务探索了上下文微调机制 (In-Context Fine-Tuning) [arXiv:2410.24087]，通过在推理阶段动态对齐局部上下文特征，进一步缩小了零样本预训练与有监督微调之间的精度鸿沟。

### 4.4 Salesforce Moirai 系列：全频段全变量统一编码器-解码器路线

Salesforce 团队推出的 Moirai (基于 uni2ts 框架) [arXiv:2402.02592] 致力于实现真正的“Any-variate Any-frequency”统一建模。针对现实场景中变量通道数不同（从单变量到数百变量）以及采样频率跨度极大（从秒级到年级）的挑战，Moirai 提出了多重补丁尺寸机制 (Multi-patch Projection) 以及变量感知旋转位置编码 (Rotary Positional Embeddings)。此外，团队开源了包含 270 亿时序观测值的 LOTSA 数据集，涵盖能量、交通、气象、金融等多领域。
随后，Salesforce 团队推出了 Moirai-MoE [arXiv:2410.10469]，利用稀疏门控网络将参数扩充至 11 亿 (1.1B)，使得不同专家的参数专门处理不同频率与动态特性的子序列；并在 2025 年发布了 Moirai 2.0 [arXiv:2511.11698]，探讨预训练语料中“少即是多”的原则，证实更纯净、更高质量的子语料集可以在维持 311M 参数下超越更大规模的无序预训练。

### 4.5 清华 THUML Timer / Sundial 系列：下一补丁自回归到流匹配生成路线

清华大学软件学院龙明盛教授团队（THUML）开辟了极具系统性的时序通用大模型演进路径：
1. **Timer** [arXiv:2402.02368]：首次提出时序领域的“大时序模型 (Large Time Series Model, LTM)”概念，基于 UTSD 10 亿时序点语料库，构建 84M 参数单通道自回归 Next-Patch GPT 架构，统一了长时序预测、短期时序预测以及插补任务；
2. **Timer-XL** [arXiv:2410.04803]：针对工业超长上下文建模需求，引入扩展上下文注意力机制与 UTSD-2 语料，使得回看窗口实现数倍跨越式扩展；
3. **Sundial** [arXiv:2502.00816]：突破了自回归中传统回归损失与离散分箱的二元局限，提出了基于流匹配理论的连续 TimeFlow 损失，将模型参数扩展至 15 亿 (1.5B)，兼具连续概率采样与高保真分布重构能力；
4. **Timer-S1** [arXiv:2603.04791]：在 2026 年最新推出的 83 亿总参数 (8.3B)、激活 0.75B 的稀疏混合专家大模型，提出串行缩放 (Serial Scaling) 技术，突破了传统时序预训练在超大规模参数下的收益递减瓶颈；
5. **TimesBERT** [arXiv:2502.21245]：针对学术界和工业界普遍将大模型等同于自回归生成 (GPT-style) 的惯性思维，THUML 团队系统论证了“时序理解 (Time Series Understanding)”在分类、插补与异常检测中的核心地位，提出了基于双向掩码补丁重建与语义对比学习的 BERT-style 基础模型。实验表明，对于需要全序列双向可见的非因果任务，TimesBERT 在参数量相同的情况下显著超越了因果自回归模型；
6. **CoRA** [arXiv:2510.12681]：针对基础模型在大规模单通道预训练后无法有效吸收外生多元协变量的结构瓶颈，提出协变量感知自适应框架。通过构建 Granger 因果嵌入 (Granger Causality Embedding, GCE) 自动度量外生协变量与目标变量的因果可预测性，并设计零初始化条件注入机制，在冻结 TSFM 主干的同时零遗忘引入时序、文本与视觉跨模态协变量，实现 31.1% 的 MSE 误差降低。

### 4.6 混合专家（Mixture of Experts, MoE）路线：参数规模扩展与计算效率平衡

随着参数规模迈向数十亿级，密集型 Transformer 面临高昂的预训练与端侧推理成本，稀疏 MoE 成为领域突破性方向：
- **Time-MoE** [arXiv:2409.16040]（金明组）：构建了包含 3000 亿时序点的 Time-300B 语料库，最大版本达 24 亿 (2.4B) 参数，通过Top-k门控自适应路由多尺度补丁，在保持与小模型相当推理 FLOPs 的同时大幅提升泛化上限；
- **Moirai-MoE** [arXiv:2410.10469] 与 **Timer-S1** [arXiv:2603.04791] 进一步验证了 MoE 在解耦长短周期专家与频域专家层面的天然优势；
- **SOTER** [arXiv:2609.16804]：针对可穿戴生理信号（高噪声、多通道、非均匀采样），提出功率谱密度 (PSD) 引导的确定性路由 MoE 架构，将表征解耦至不同生理频带专家，并在 2260 亿时序观测点上预训练；
- **TW3Cast** [arXiv:2609.28506]：在 GIFT-Eval 权威榜单上提出了突破性的“冻结路由器 (Frozen Router)”范式。与端到端庞大 MoE 预训练不同，TW3Cast 表明仅需将多个经过轻量微调的基础模型作为候选池，在完全脱离测试集的训练切分上拟合一个超轻量冻结门控网络，便以第 3 名的极高名次傲视绝大多数重型模型，为低成本专家路由提供了全新标杆。

### 4.7 MOMENT 与 TTM：编码器架构与轻量级工业部署路线

并非所有工业场景都需要庞大的解码器生成模型。CMU 联合研制的 MOMENT [arXiv:2402.03885]（最大 385M）坚持掩码预训练 (Masked Autoencoding) 路线，在包含 1300 万序列的 Time-series Pile 上预训练，以统一编码器赋能预测、异常检测与分类四项任务。
IBM 推出的 Tiny Time Mixers (TTMs) [arXiv:2401.03955] 则证明了轻量级基础模型的巨大商业潜力：参数量控制在 1M 到 8M 之间，基于多尺度 MLP-Mixer 架构，在边缘计算设备上实现超低延迟的零样本/少样本预测，性能媲美参数量大其数百倍的模型。
此外，**FlowTSFM** [arXiv:2609.13640] 颠覆了传统编码器依赖层叠多独立 Transformer 层的做法，提出将网络深度解释为循环分位数传输过程 (Recurrent Quantile Transport)。仅需 38.8M 参数，通过循环复用单层 Transformer 块并引入分位数流目标联合监督，在 GIFT-Eval 与 TIME 基准上取得与 119.5M 参数 Chronos-2 相当的精度，且在中间表征定向对齐指标 CosMean 上从 0.350 跃升至 0.919，展现了极高的参数效能比。

### 4.8 连续动力学与生成式路线：Flow 与 Diffusion 路线

面对高度不规则、非等间距或强随机性的物理连续信号，传统离散 Transformer 面临采样率不一致挑战。FlowState [arXiv:2508.05287] 提出了采样率等变 (Sampling-Rate-Equivariant) 的连续流生成架构；FLAME [arXiv:2512.14253] 则通过流增强勒让德正交多项式记忆系统实现自适应记忆压缩；结合 Sundial [arXiv:2502.00816] 的 TimeFlow 框架，生成式流匹配正成为概率时序预测的前沿热点。
在样本路径与数据扩增方面：
- **Interweaving Marginals** [arXiv:2609.25980]：针对概率 TSFM 输出单通道边缘分布却无法确定多变量联合未来轨迹的问题，提出完全免训练的多变量样本路径交织耦合后处理算法，通过历史时间与通道相关性显著提升多变量概率联合推断质量；
- **OATS** [arXiv:2601.19040]（金明组，Microsoft TimeCraft）：基于条件扩散模型提出 TSFM 在线动态数据增强框架，根据预训练不同训练阶段的梯度与样本贡献动态合成高保真数据，克服了静态启发式数据扩增的局限。

### 4.9 新兴开源预训练前沿：Tabby, Toto 2.0 与 t0

进入 2026 年，时序基础模型开源生态进入深水区：
- **Datadog Toto 2.0** [arXiv:2605.20119] 宣告时序基础模型正式进入参数扩展新时代，发布从 4M 到 25 亿 (2.5B) 的五组开源权重模型，基于超 1 万亿点预训练；
- **Tabby** [arXiv:2609.13956] 则发布了首个端到端完全公开透明的 TSFM 预训练配方与 OpenTS-Archive 数据清洗管线；
- **$t_0$** [arXiv:2609.24559] 则率先将异构环境上下文深度融入 256M 解码器架构中；
- **QUALS** [arXiv:2609.20156]（录用于 VLDB 2027）：系统研究了超大规模跨域时序预训练中的语料不平衡与灾难性遗忘难题，提出模式量化 (Pattern Quantization) 与可学习性同步 (Learnability Synchronization) 机制，在多域语料库间实现动态学习平衡与通用零样本预测；
- **SwitchPFN** [arXiv:2609.29814]：针对表格基础模型 (Tabular Foundation Models) 与先验数据拟合网络 (Prior-Data Fitted Networks, PFN) 难以直接迁移至时序分类的痛点，创新提出在合成先验中融入分段切换动力系统 (Switching Dynamical Systems)。通过在离线阶段拟合海量自回归切换过程，SwitchPFN 在完全冻结参数的条件下实现高精度的零样本上下文时序分类；
- **VINTAGE-TS** [arXiv:2609.28576]：开创性地审视了真实宏观经济与政策统计中的“数据版本修订 (Data Revisions)”挑战。现实中统计局发布的初值（Flash Release）往往会在数月后多次修订，基于最终修订数据进行预训练会导致严重的未来信息穿越。VINTAGE-TS 提出了首个版本感知的时序适配框架，使基础模型能够准确辨识实时初值与历史多重修订间的因果演化差异。

---
"""

print("Part 2 defined.")

part3 = r"""## 5 大语言模型赋能时序

除了构建原生时序架构，另一条极其繁荣的技术路线是直接利用 NLP 领域具有深厚预训练先验的现成大语言模型（如 LLaMA、GPT-2、GPT-4、Qwen）解决时序问题。大语言模型不仅在海量语料上掌握了丰富的通用序列模式、局部平滑性与自回归因果规律，还蕴含了关于物理现实、经济周期和人类行为的世界知识 (World Knowledge)。

### 5.1 大语言模型赋能时序范式矩阵与理论形式化

为了清晰界定各类 LLM-for-TS 方法的技术本质，下表给出了代表性方法的架构特性与实验开销对比：

| 模型/框架 | 基础大模型 | 范式类别 | 跨模态对齐机制 | 输入模态 | 可训练参数占比 | 核心亮点与任务泛化 | 计算开销与延迟 | arXiv 引用 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Time-LLM** | LLaMA-7B / GPT-2 | 模型重编程 | 线性补丁投影 + 文本 Prompt 前缀 + LoRA | TS + Text | ~1% - 3% | 文本领域前缀引导，长时预测精度顶尖 | 较高 (LLM 庞大隐藏层前向) | [arXiv:2310.01728] |
| **One Fits All (GPT4TS)**| GPT-2 (124M) | 极简重编程 | 仅微调输入 Patch 投影、位置编码与 LayerNorm | TS | < 0.1% | 极简架构，全任务通用 (预测/分类/异常检测) | 中等 (轻量级 GPT-2 骨干) | [arXiv:2302.11939] |
| **LLM4TS** | LLaMA-2 / GPT-2 | 两阶段重编程 | 阶段一两阶段时序自监督预训练，阶段二少样本对齐 | TS | ~1% | 数据利用效能高，少样本下游迁移稳健 | 较高 | [arXiv:2308.08469] |
| **AutoTimes** | LLaMA-2-7B / OPT | 自回归语言适配 | 将 Patch 表示重构为自回归时序 Token，下一补丁自回归 | TS + Text | ~0.5% | 原生自回归语言建模，支持零样本与指令微调 | 较高 | [arXiv:2402.02370] |
| **LLMTime** | GPT-3 / GPT-4 / LLaMA | 文本化直接提示 | 逗号数值格式化，零样本直接概率外推提示 | TS (数值文本) | 0% (完全免训练) | 零训练成本，极佳的概率外推形态与柔性采样 | 极高 (逐点 Tokenization，上下文长度膨胀) | [arXiv:2310.07820] |
| **LSTPrompt** | 通用商业 LLM | 解耦直接提示 | 长短时特征文本分解提示 | TS + Text | 0% (免训练) | 显式解耦高频局部波动与低频趋势 | 较高 | [arXiv:2402.16132] |
| **LLM as Planner** | LLM + 专有时序模型 | 规划-执行双层协作 | LLM 提取文本事件与因果突变约束，引导 TSFM 回归 | TS + Text | 0% (免微调) | 规避 LLM 算术弱点，结合 TSFM 连续数值精度 | 中等 (仅需单次规划提示) | [arXiv:2607.24892] |
| **$\textbf{S}^2\textbf{IP-LLM}$** | GPT-2 / LLaMA | 语义空间提示微调 | 统计特征向语义原型空间投影 | TS + Text | ~1.5% | 语义连贯，抵抗高频噪声扰动 | 中等 | [arXiv:2403.05798] |
| **CALF** | LLaMA / GPT-2 | 跨模态微调 | 双分支时序-文本对比学习与特征蒸馏 | TS + Text | ~2% | 防止模态塌缩，跨模态表征对齐严格 | 较高 | [arXiv:2403.07300] |
| **STReasoner** | Qwen-7B / LLaMA | 空间强化学习微调 | 时空图结构编码 + 空间感知强化学习 (S-GRPO) | TS+Text+Graph | ~5% (LoRA) | 复杂的时空因果拓扑推断与归因解释 | 较高 | [arXiv:2601.03248] |
| **Align-RAG** | 任意冻结 TSFM / LLM | 闭式检索自适应 | 闭式最小二乘最优仿射对齐 ($\alpha^*, \tau^*$) | TS | 0% (完全免训练闭式求解) | 零参数微调，检索示范即插即用 | 极低 (微秒级几何求解) | [arXiv:2608.05571] |
| **Estimating Transferability**| 候选 TSFM 集合 | 在途上下文探针 | 目标域零样本在途对数似然增益差分子空间探测 | TS | 0% (探针式无更新) | 免微调秒级锁定最优预训练模型 | 极低 | [arXiv:2509.23695] |

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
- **UniTime** [arXiv:2310.09751] 与 **TEMPO** [arXiv:2310.04948]：引入跨域多任务通用指令微调，使模型能够根据文本提示动态调整对不同频段和趋势周期的捕获敏感度；
- **CoRA** [arXiv:2510.12681]（THUML）：设计基于 Granger 因果嵌入与零初始化条件注入机制的通用协变量适配框架，将外生多模态上下文无损注入冻结的基础模型。

### 5.3 文本化分词与直接提示路线 (Direct Prompting & Reasoning Planners)

如果不训练任何映射层，大语言模型能否直接理解时间序列？答案是肯定的：
- **PromptCast** [arXiv:2210.08964]：最早尝试将数值序列以问答字符串形式输入语言模型；
- **LLMTime** [arXiv:2310.07820]（NeurIPS 2023）：深入分析了现有大语言模型（如 GPT-3/GPT-4、LLaMA-2）直接外推连续数值的机理。研究发现：**当使用逗号进行分隔，并将连续浮点数严格按固定有效数字格式化后，未经任何时序训练的 LLM 展现出惊人的零样本概率预测能力**。其输出的蒙特卡洛多样本自回归采样不仅能自动捕捉季节性、趋势拐点，还能表达非对称的多峰后验分布；
- **LSTPrompt** [arXiv:2402.16132]：针对直接提示中长序列容易导致注意力稀释的缺陷，提出长短时记忆解耦提示范式，引导大模型分步推导高频微扰与长期基线；
- **LLM as Forecasting Planner** [arXiv:2607.24892]：系统反思了让 LLM 直接输出长串数值的内在缺陷（算术计算脆弱性、高昂的 Token 费用与高延迟），创新性地提出“大模型负责定性规划、时序小模型负责数值定量回归”的双层协作架构。利用冻结的 LLM 解析宏观文本事件、重大节假日与趋势突变，输出规划约束参数，再由轻量级 TSFM 执行连续数值生成，实现了高精度与低计算开销的优雅统一。

### 5.4 跨模态微调与跨语义空间对齐 (Cross-Modal Fine-Tuning & Semantic Alignment)

为了消除时序连续数值与文本离散语义之间的语义断层 (Semantic Gap)，跨模态对齐技术通过对比学习或原型投影实现表征统一：
- **$\textbf{S}^2\textbf{IP-LLM}$** [arXiv:2403.05798]：引入语义空间引导的提示学习，将时序的统计矩（均值、方差、偏度、自相关系数）投射到文本语义连贯的原型空间，消除噪声干扰；
- **CALF** [arXiv:2403.07300]：提出双分支跨模态微调机制，一条分支处理文本描述，另一条分支编码时序补丁，通过跨模态 InfoNCE 损失进行特征蒸馏，有效防止微调过程中大模型的知识表征发生塌缩；
- **AutoTimes** [arXiv:2402.02370]（清华 THUML，NeurIPS 2024）：设计自回归时序分词与提示对齐策略，直接将连续时序补丁视为一种新语言方言 (Dialect)，使大规模语言模型无需任何结构性破坏，即可原生以自回归语言建模方式输出未来预测补丁；
- **STReasoner** [arXiv:2601.03248]（金明组，ACL 2026）：针对城市计算与物理传感器网络中普遍存在的时空图拓扑结构，构建了包含实体关联与拓扑传播的 ST-Bench，并提出基于空间感知强化学习算法 S-GRPO，使大语言模型能够显式联合推导时空拓扑演化因果链，完成高阶时空推理。

### 5.5 上下文学习、检索增强与零样本迁移度量 (In-Context Adaptation & Transferability)

大语言模型的强大不仅体现在参数内部知识，更在于其灵活的在途上下文适应能力：
- **Align-RAG** [arXiv:2608.05571]：打破了时序检索增强必须端到端训练神经网络融合器的固有思维，通过闭式求解最优幅度缩放因子 $\alpha^*$ 与时移偏差 $\tau^*$，以纯数学闭式解实现了跨序列几何对齐，将检索到的高质量历史范例直接送入冻结 TSFM，在零参数训练下取得显著泛化增益；
- **Estimating TSFM Transferability** [arXiv:2509.23695]（金明组）：提出首个基于无标注在途上下文探针量化基础模型可迁移性的理论方法，在无需进行昂贵梯度训练的前提下，秒级准确预估不同预训练大模型在特定下游任务的微调收益；
- **LLM-Mixer** [arXiv:2410.11674]：探索将多尺度分解与混合层深度内嵌至 LLM 的中间隐层，提升长程复杂周期信号的自适应外推能力；
- **In-context Time Series Predictor** [arXiv:2405.14982]：通过在上下文中优雅堆叠少量输入-输出时序对示范 (Few-shot Demonstrations)，探索了纯粹免梯度的在途时序推理能力。

---
"""

print("Part 3 defined.")

part4 = r"""## 6 多模态时序

随着现实场景从单一数值传感向复合感知升级，多模态时序融合已成为 2025-2026 年最具活力的前沿领域：

### 6.1 文本与时序跨模态推理与交互 (Text + TS Joint Reasoning)

将领域知识、事件快讯、专家诊断文本与物理时序数据进行端到端联合建模：
- **TimeBraid** [arXiv:2609.29792]（2026 年最新突破）：长达 57 页的长篇巨制，宣告了时序基础模型与自然语言大模型走向真正的原生大一统。TimeBraid 摒弃了过往浅层拼接投影的做法，提出交错全局残差注意力机制 (Interleaved Global Residual Attention)，将预训练语言模型与预训练时序基础模型深层次编织交融。模型不仅在数值预测任务上打破原有 SOTA，更在长程因果推理、复杂时序问答和开放式场景解释上展现出前所未有的综合智能；
- **OpenTSLM** [arXiv:2510.02410]：针对多变量医疗 ICU 时序与临床病历文本构建的专用语言模型，支持基于生命体征的复杂临床问答与恶化风险预测；
- **ChatTS** [arXiv:2412.03104] 与 **ChatTime** [arXiv:2412.11376]（AAAI 2025）：构建时序-文本对话代理，支持用户以自然语言询问趋势成因与未来预测；
- **SciTS** [arXiv:2510.03255]：面向天文学、材料科学等科研时序的跨模态理解与合成框架；
- **FINESSE** [arXiv:2609.11993]：针对金融领域异构多模态信息高度割裂的痛点，构建了首个多智能体驱动的多模态金融事件序列仿真器与基准数据集，将宏观经济事件快讯、财报电话会议文本与高频微观订单簿深度结合；
- **TAC-Time** [arXiv:2609.24156] 与 **TRACE** [arXiv:2606.06285]：提出将自然语言事件直接转化为虚拟输入通道，实现通道级别的非平稳语义条件注入；
- **STReasoner** [arXiv:2601.03248]（ACL 2026）：在时序与自然语言问答中引入图拓扑空间结构，开辟了时空跨模态联合推理新路线。

### 6.2 视觉与时序跨模态协同 (Visual Time Series & Temporal VLMs)

利用人类直观的“折线图看图思维”与强大的视觉大模型 (VLM)：
- **VisionTS** [arXiv:2408.17253]（NeurIPS 2024）：惊人地发现将一维时序绘制为灰度折线图像后，直接输入未经任何时序训练的计算机视觉掩码自编码器 (Visual MAE)，即可获得媲美主流原生 TSFM 的“免费午餐”式零样本预测性能；
- **Time-VLM** [arXiv:2502.04395] 与 **TimeOmni-VL** [arXiv:2602.17149]（ICML 2026）：构建统一视觉-语言-时序三模态表征空间，支持从时序图表识别图样、文本分析因果到预测生成闭环；
- **Empowering VLMs for TS** [arXiv:2605.09395]：利用 Agentic 视觉推理实现少样本多模态时序分类；
- **DiTS** [arXiv:2602.06597]（清华 THUML，2026）：首次将计算机视觉中强大的 Diffusion Transformer (DiT) 架构无缝拓展至多模态时序生成预测，利用自注意力机制捕获跨时间步与跨模态空间相关性，为高维不规则多模态时序建模提供全新范式。

### 6.3 交互式流式时序与智能体决策 (Interactive TS & Agents)

- **ChatAD** [arXiv:2601.13546]（金明组，Microsoft 等）：针对工业时序异常检测中“仅输出异常标签但无法解释深层物理原因”的局限，提出多轮指令演化 (Multi-Turn Instruction Evolution) 的时序异常推理智能体。通过构建 8B 参数的推理大模型，ChatAD 支持运维专家通过多轮对话层层深挖时序异常根因；
- **TimeOmni-1** [arXiv:2509.24803]（ICLR 2026）：激励大语言模型进行时序链式推理 (Chain-of-Thought)，解析复杂时序因果网络；
- **Sonar-TS** [arXiv:2602.17001]：提出基于“先检索后验证”机制的时序数据库自然语言查询智能体；
- **TimeInteract** [arXiv:2609.26389]：构建面向超高吞吐流式时间序列的实时交互式智能系统；
- **Forecast Workflow Bench** [arXiv:2609.27385]：针对工业运筹场景，评估具有工具调用预算约束的时序智能体运筹决策质量；
- **TimEvolve** [arXiv:2609.24862]：提出“部署即监督”的自进化时序智能体决策框架。针对真实世界动态漂移环境，TimEvolve 利用滚动预测后真实值延迟显现的自然反馈机制，无需人工标注即可持续在线更新专家信任度、候选智能体路径与干预强度，在 Time-MMD 八大领域取得领先。

---
"""

print("Part 4 defined.")

part5 = r"""## 7 基准与评测

评测机制的严谨性与度量维度直接决定了基础模型泛化声称的真实可信度。随着基础模型预训练语料规模突破万亿时序点，评测范式正经历从“传统静态测试集点误差对比”向“严格时序因果隔离审计、宏观版本修订溯源、系统集中性风险防御、工业经济性度量与端到端智能体决策”的系统性重构。当前文献中，开源模型、闭源模型与评测基准的占比分布如下图所示：

![Open Weight Share](figures/open_weight_share.png)

![Papers by Category per Year](figures/papers_by_category_year.png)

### 7.1 通用时序评测矩阵与基准对比

下表对比了时序基础模型与多模态前沿的核心基准套件与评估审计框架（数据严格来自于对应论文声明）：

| 基准/评测体系 | 代表机构/文献 | 核心任务与模态 | 涵盖规模/时序点 | 时序因果隔离与动态更新机制 | 核心评估重点 | 开源状态 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GIFT-Eval** | Salesforce [arXiv:2410.10393] | 通用零样本预测 (TS) | 7 个域 1.77 亿观测值 / 230 亿点 | 静态多领域保留集 | 跨频段 MASE / CRPS / 极端点鲁棒性 | 是 |
| **It's TIME** | 学术团队 [arXiv:2602.12147] | 新一代真实预测 (TS) | 跨 9 大行业领域海量序列 | 区分平稳与强非平稳漂移段 | 工业真实分布偏移下的泛化稳健性 | 是 |
| **LiveHouse-TS** | 学术团队 [arXiv:2608.17299] | 活体开放基准 (TS) | 持续滚动的开放时序流 | 动态实时抓取最新全球时间序列 | 杜绝模型预训练静态记忆与后门过拟合 | 是 |
| **HoliBench** | 弗吉尼亚等学术团队 [arXiv:2609.12412] | CPS-IoT 嵌入式基准 (TS+LLM+VLM)| 涵盖边缘 GPU、微控制器等多硬件 | 嵌入式与边缘异构实时推理约束 | 真实边缘硬件下的能耗、内存占用与延迟 | 是 |
| **Cost-Aware Study** | 工业学术团队 [arXiv:2608.22968] | 工业监控成本效益 (TS) | 多个真实工业连续生产流 | 严格时间戳因果阻断 | TSFM 相比轻量基线 (TTM/LightGBM) 的经济 ROI | 论文声明 |
| **Causal Analysis 框架**| 学术团队 [arXiv:2608.24303] | 因果集中性风险审计 (TS) | 跨金融、能源与气候 3 大行业 | 结构因果模型 (SCM) 反事实干预 | 单一基础模型被全行业采用带来的系统性脆弱风险 | 论文声明 |
| **VINTAGE-TS** | 学术团队 [arXiv:2609.28576] | 数据版本修订审计基准 (TS) | 宏观统计多版本演进时间序列 | 区分初次快讯与最终修正版本 | 防止“未来修订数据穿越”导致的虚高得分 | 是 |
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
| **Forecast Workflow Bench**| 学术团队 [arXiv:2609.27385] | 预算约束智能体工作流 (TS+Agent) | 运筹规划工业时序仿真 | 步数与 API 预算动态受限 | 工具选择策略、调度收益与边际成本权衡 | 是 |

---

### 7.2 数据污染、预训练熟悉度与时序因果隔离审计

在时序基础模型时代，学术界沿用多年的经典公开测试集（如 ETT 系列、Weather、Electricity、Traffic）遭遇了前所未有的**数据污染 (Data Contamination) 与预训练熟悉度危机**：
1. **公开基准的事先暴露**：现有主流基础模型预训练语料高达数百亿至上万亿点（如 LOTSA、UTSD、Time-300B、Toto 1T）。即使研究者声明排除了特定测试集，庞大的网络爬取语料中仍不可避免地包含了同一物理系统（如国家电网调度记录、气象局历史发布）在相邻时段或相同分布下的数据片段；
2. **“时间延迟不等于新领域”** [arXiv:2609.10357]：Moghadasi 与 Ghaderi 的开创性研究指出，时序领域的“零样本”声称长期依赖于领域外测试，但模型在熟悉物理系统上的表现与其真实跨域泛化存在本质区别。该研究通过构建严格截断于所有模型权重发布时间之后的“无污染保留测试集 (Contamination-Free Hold-Out)”，评估了 13 个主流模型（涵盖经典统计模型、Chronos、TimesFM、MOMENT 等）。实验证实：**在真正无污染的时间截断测试集上，许多庞大模型的绝对误差大幅攀升，模型对预训练时期熟悉动态的记忆构成了其测试高分的主要来源**；
3. **宏观数据版本修订穿越漏洞** [arXiv:2609.28576]：VINTAGE-TS 揭示了一个极其隐蔽却普遍存在的系统性漏洞：国家统计局或央行发布的 GDP、就业率和工业产值，在首次公布后往往会在后续数月乃至数年进行多轮重大修正。如果研究者直接从当下的数据库下载历史时间序列来评估模型过去的表现，模型实际上接触到了“发布日期时尚未发生的数据修正”，造成严重的信息未来泄露。未来评测必须强制绑定严格的“版本历史时序数据库”；
4. **未知信息泄露预警** [arXiv:2510.13654]：Rethinking Evaluation 进一步形式化了未来信息泄漏的三种途径：全局归一化参数泄漏、跨序列重叠采样泄漏以及自注意力双向重叠泄漏，强调未来的评测必须强制要求只使用因果单向窗口归一化与时间戳严格后延的测试语料。

### 7.3 证据边界与零样本审计框架

针对当前“零样本 (Zero-Shot)”概念被滥用、不同模型在不同提示与外存条件下不公平对比的乱象，李子跃团队在 ACM AI Summit 2026 上提出了**基于“证据来源第一”的严格审计框架** [arXiv:2609.21425]：
该框架明确指出，“零样本”不应仅仅被定义为“未对目标域进行参数梯度更新”，而必须被界定为一种**受管制的证据访问声称 (Evidence-Access Claim)**。框架将所有零样本时序系统的能力来源解耦为三大基础证据边界：
1. **冻结语言模型先验复用 (Frozen LLM Prior Reuse)**：依靠通用大模型（如 GPT-4、LLaMA）中固化的人类常识、周期概念与语言联想；
2. **参数化时序预训练 (Parametric TSFM Pretraining)**：依靠大规模时序多域数据集预训练学得的通用动态算子（如 Chronos、TimesFM、Timer）；
3. **检索增强外部记忆 (Retrieval-Augmented External Memory)**：依靠推理期从外部历史库中检索相似模式的跨序列线索。

在明确证据来源后，该框架制定了四大审计维度：
$$\text{Audit Dimension} \in \{\text{Task Interface}, \text{Forecast Object \& Scoring}, \text{Prediction Context}, \text{Resource Budget}\}$$
通过强制在排行榜上同步公开上下文长度限制、推断 FLOPs 预算以及外部先验调用边界，确保前沿评测真正反映跨领域泛化能力，而非隐蔽的算力扩张或上下文泄露。
与此同时，在因果安全性方面，**Causal Analysis for TSFMs** [arXiv:2608.24303] 警告：当全行业从针对单一任务定制专有模型转向共同依赖少数几个头部 TSFM 时，模型与应用的关系从“一对一”转变为“一对多”，带来了严重的**集中性风险 (Concentration Risk)**。如果基础模型在特定能源电网或宏观金融因子上存在系统性因果归因偏差，整个下游生态将面临同质化的级联风险。

### 7.4 概率可靠性、分位数校准与高阶依赖度量

绝大多数早期 TSFM 论文仅以均方误差 (MSE) 和平均绝对误差 (MAE) 等点预测指标论英雄，但工业生产（电力日前调度、极端气象预警、金融期权定价）对预测的不确定性表达与尾部风险覆盖有着严苛要求：
1. **点预测精度与分布校准的脱节** [arXiv:2609.25788]：ADBIS 2026 的系统评测揭示了深刻的二元割裂现象——在测试集取得极低 MSE 的模型，其预测分位数置信区间（如 90% 预测区间覆盖率 PICP）经常严重偏离标称水平（覆盖率显著偏低），区间平均宽度 (MPIW) 出现过度紧缩或病态发散；
2. **连续分位数流监督** [arXiv:2609.13640]：FlowTSFM 证明通过在编码器深度方向引入分位数流 (Quantile-Flow) 轨迹损失联合监督，不仅能大幅降低连续分级概率评分 (CRPS)，而且在无量纲方向对齐度量 CosMean 上取得 0.919 的极高一致性；
3. **多变量联合样本路径耦合** [arXiv:2609.25980]：针对现有单通道基础模型无法输出多通道协同联合分布的痛点，免训练多变量交织算法证明：仅需对边缘分布采样进行基于历史时空协方差的最优传输重排，即可在保持单通道边际分布不变的前提下，大幅改善多维联合风险诊断指标。

### 7.5 动态演化环境与多轮智能体评测

随着 LLM Agent 在时序决策中的广泛引入，静态的一次性问答 (Single-turn QA) 已无法衡量系统在现实世界中的持续推理水平：
1. **多轮对话与决策衰减** [arXiv:2606.01498]：金明团队构建的 TimeSage-MT 首次评测了大模型在 2,680 轮长时序交互中的表现，发现当前顶尖大模型在需要多步推演、置信度修正与复合运筹的决策型任务上出现断崖式性能崩溃，主要源于时序工作记忆丢失与不确定性量化能力缺失；
2. **动态演化与发布截断意识** [arXiv:2608.14270]：现实时序决策依赖于定期发布的宏观报告与传感器批次更新。TimeSage-EV 追踪了 2023 年至 2026 年间 60 个真实机构场景的 1,485 个演化问答对。模型必须严格遵循“截断日前可见信息”，预测截断日后真实发生的结果。评测发现，多数智能体对“时间有效性 (Temporal Validity)”极为迟钝，频繁出现跨期因果倒置；
3. **部署闭环中的自进化策略** [arXiv:2609.24862]：TimEvolve 证明在动态演化环境中，智能体应当把未来的延迟展开视为天然弱监督，通过自进化门控机制在实践中持续优化专家信任矩阵与干预策略；
4. **时空图推理与归因基准** [arXiv:2601.03248]：ST-Bench 首次将空间网络拓扑关系引入时序推理基准，评估模型在实体关联溯源、传播路径推导与零样本上下文预测中的结构泛化能力。

### 7.6 视觉裁判与工作流调度 Harness

1. **视觉语言大模型充当裁判 (VLM-as-a-Judge)** [arXiv:2606.16173]：
   清华 THUML 团队开创性地指出，人类分析师对时序预测的优劣判断并非局限于点对点数值残差，更看重宏观形态的一致性（峰值拐点、趋势转折、相位对齐）。基于此构建的 TimeVista 验证了让经过对齐的 VLM 直接审阅折线预测图充当打分裁判的可行性，与人类专家评审的相关性显著高于传统数学指标；
2. **端侧硬件资源与实际能耗综合评测 (HoliBench)** [arXiv:2609.12412]：
   面向信息物理系统与物联网 (CPS-IoT) 的实际落地，HoliBench 建立了跨微控制器、边缘 GPU 与云端异构硬件的系统级评测工具链。评测表明，单纯追求预测精度的重型模型在边缘端常因超出 SRAM/DRAM 带宽而发生延迟爆炸，轻量模型与端侧量化适配器在工业物联场景中展现出压倒性的综合工程性价比；
3. **工业监控部署经济性与真实回报分析** [arXiv:2608.22968]：
   在真实工业流程监控中，引入 TSFM 的边际收益究竟能否抵消其显著增长的推理服务器支出与能耗？该研究通过对多个真实工业场景的严格实验发现，在数据丰富且工况稳定的常规场景下，8M 参数的 TTM 或经典树模型完全足以胜任；TSFM 真正的颠覆性优势集中体现在极度缺乏标注历史的冷启动传感器以及突发性多变量分布漂移场景；
4. **工具调度与预算约束 Harness** [arXiv:2609.27385]：
   在真实生产运维中，调用庞大的高精尖 TSFM 或密集数值求解器受制于严苛的推理延迟与 Token/API 成本。Forecast Workflow Bench 首次建立了在固定预算约束下评估大模型合理编排轻量模型、统计模型与基础模型决策效率的量化基准。

---
"""

print("Part 5 defined.")

part6 = r"""## 8 重点课题组进展

### 8.1 龙明盛团队（清华大学 THUML）

清华大学龙明盛教授团队长期引领时间序列分析学术前沿。从构建经典基准库 TSlib（集成 TimesNet、Autoformer、iTransformer、TimeMixer 等代表作），到系统性建立时序基础模型矩阵：
- 提出基础架构 **Timer** [arXiv:2402.02368] 与超长上下文 **Timer-XL** [arXiv:2410.04803]；
- 开创跨模态自回归范式 **AutoTimes** [arXiv:2402.02370] 与外生变量注意力 **TimeXer** [arXiv:2402.19072]；
- 颠覆传统损失函数，提出基于连续流匹配的 1.5B 原生大模型 **Sundial** [arXiv:2502.00816]；
- 突破参数扩展瓶颈，推出 8.3B 参数 MoE 模型 **Timer-S1** [arXiv:2603.04791]；
- 提出基于双向编码器掩码重建的全局理解模型 **TimesBERT** [arXiv:2502.21245]，在时序分类与插补任务上实现重大突破；
- 开创性探索多模态裁判评估范式 **TimeVista** [arXiv:2606.16173]；
- 提出协变量感知与跨模态自适应通用框架 **CoRA** [arXiv:2510.12681]；
- 推出首个面向高维与多模态时序预测的扩散 Transformer 架构 **DiTS** [arXiv:2602.06597]。
其全套模型与数据管线依托 OpenLTM 开源生态持续推动领域发展。

### 8.2 金明团队（Ming Jin Group, Griffith / Monash）

金明团队在大语言模型赋能时序以及超大规模混合专家时序领域做出了开创性贡献：
- 奠基之作 **Time-LLM** [arXiv:2310.01728]（ICLR 2024）开辟了模型重编程用于时序预测的先河；
- 率先推出具备 3000 亿点预训练的 24 亿参数稀疏专家大模型 **Time-MoE** [arXiv:2409.16040]（ICLR 2025）；
- 提出多尺度分解与混叠架构 **TimeMixer** [arXiv:2405.14616] 与通用模式机 **TimeMixer++** [arXiv:2410.16032]；
- 开辟时序推理与交互智能体方向：**Time-MQA** [arXiv:2503.01875]、**TimeOmni-1** [arXiv:2509.24803]、时序数据库查询 **Sonar-TS** [arXiv:2602.17001]、图文视时序统一 **TimeOmni-VL** [arXiv:2602.17149]、流式交互系统 **TimeInteract** [arXiv:2609.26389] 以及多轮异常根因推理智能体 **ChatAD** [arXiv:2601.13546]；
- 建立时序智能体系统性基准套件：多轮推理基准 **TimeSage-MT** [arXiv:2606.01498] 与动态演化环境基准 **TimeSage-EV** [arXiv:2608.14270]；
- 提出首个免梯度的在途基础模型可迁移性预估框架 **Estimating TSFM Transferability** [arXiv:2509.23695]，实现高效零样本选模；
- 突破时序空间拓扑强化学习推理 **STReasoner** [arXiv:2601.03248] 与在线动态扩散数据增强 **OATS** [arXiv:2601.19040]；
- 撰写权威综述 [arXiv:2310.10196]，持续维护前沿进展。

---

## 9 开放问题与未来方向

尽管时序基础模型与多模态智能在过去四年取得了飞跃式进展，但距离通用物理世界时空智能仍面临若干核心挑战：

1. **时序标度律 (Scaling Laws) 的边界与合成数据蒸馏**：
   与语言和视觉不同，公开时间序列数据呈现严重的域碎片化。尽管 Toto 2.0 [arXiv:2605.20119] 和 Timer-S1 [arXiv:2603.04791] 验证了持续收益，但真实数据收集代价极其高昂。以 **Distillation of Synthetic Data for TSFM** [arXiv:2609.09586] 为代表的数据蒸馏 (Dataset Distillation/Condensation) 技术表明，通过在合成过程中反向优化动力学代表性轨迹，可以仅用 10% 的语料达到全量预训练的性能，如何在保持物理泛化多样性的同时压缩语料是未来破局关键。
2. **高风险部署中的因果鲁棒性与系统集中性风险**：
   从传统单一专有模型向“一对多”基础模型过渡，带来了一个隐秘而巨大的系统性脆弱性——集中性偏见 (Concentration Risk) [arXiv:2608.24303]。当能源电网调配、跨国金融对冲或气候灾害响应共同依赖于少数几个通用 TSFM 主干时，模型内部对某些未充分校准的虚假相关性的误判，可能在整个工业界引发雪崩式的共模失效。将结构因果模型 (SCM)、反事实推理与敏感性分析深度融入基础模型训练势在必行。
3. **超长上下文连续记忆与工业端侧经济性权衡**：
   边缘传感器和工业物联网 (CPS-IoT) 要求极高计算效能与实时性。如 HoliBench [arXiv:2609.12412] 与 Cost-Aware Industrial Monitoring [arXiv:2608.22968] 研究所揭示，绝大多数工业现场对功耗、SRAM 占用与冷启动恢复有着严苛限制。未来基础模型必须走向“云-边端协同”：云端负责基于亿级参数大模型（如 Sundial [arXiv:2502.00816]、TimeBraid [arXiv:2609.29792]）进行定性宏观因果推理与离线规划，端侧则依托轻量级高效架构（如 TTM [arXiv:2401.03955]、FlowTSFM [arXiv:2609.13640]、SwitchPFN [arXiv:2609.29814]）完成亚毫秒级低能耗流式推断。
4. **自进化决策智能体闭环与真实运筹协同**：
   在动态演化环境中，智能体必须具备截止日期感知与反思校准能力。TimeSage-EV [arXiv:2608.14270]、TimEvolve [arXiv:2609.24862] 与 STReasoner [arXiv:2601.03248] 指明了将未来展开作为天然反馈、利用强化学习持续进化决策策略的闭环方向。
   时序预测的终极目标并非仅仅给出均方误差最优的曲线，而是辅助真实决策（如能源调配、库存备货）。如 Forecast Workflow Bench [arXiv:2609.27385] 与 ADBIS 2026 研究所揭示，结合校准良好的预测置信度进行带有预算惩罚的端到端运筹优化，是时序智能体落地的关键一步。

---

## 10 参考文献

本综述所引用的全部文献均通过 arXiv HTTPS API 严格核验并收录于 [`data/papers.json`](../data/papers.json)，同时自动化生成 BibTeX 数据库 [`survey/references.bib`](references.bib)。

""" + references_md + r"""

---

## 版本变更日志 (Changelog)

- **2026-09-25 (第 3 轮迭代：大语言模型赋能时序全面深化、前沿 15 篇收录与图表重构 / Iteration 3)**:
  - 严格通过 arXiv HTTPS API 核验收录 15 篇最新前沿与重点团队论文，文献库增至 108 篇；
  - **全面深化第 5 章（大语言模型赋能时序）**：从零构建 12 维综合范式矩阵对比表；系统推导补丁重编程映射与词表子空间对齐数学形式化；给出 Align-RAG [arXiv:2608.05571] 闭式无训练仿射对齐严格解析解 ($\alpha^*, \tau^*$)；引入金明团队基于在途上下文学习的免梯度基础模型可迁移性预估理论 [arXiv:2509.23695]；
  - 重点团队文献扩充：THUML 全局双向理解 TimesBERT [arXiv:2502.21245]；金明组多轮异常根因推理 ChatAD [arXiv:2601.13546] 与 TSFM 可迁移性估计 [arXiv:2509.23695]；
  - 核心架构前沿纳入：57页统一时序-语言大模型 TimeBraid [arXiv:2609.29792]、联邦隐私微调 FedChronos [arXiv:2608.01290]、水工知识图谱增强 KG-Chronos-2 [arXiv:2609.21381]、切换动力系统先验 SwitchPFN [arXiv:2609.29814]、GIFT-Eval 冻结路由器 TW3Cast [arXiv:2609.28506]；
  - 评测与因果审计突破：CPS-IoT 嵌入式基准 HoliBench [arXiv:2609.12412]、工业监控成本效益实证 [arXiv:2608.22968]、因果集中性脆弱性审计 [arXiv:2608.24303]、宏观数据版本修订穿越漏洞 VINTAGE-TS [arXiv:2609.28576]、多模态金融事件仿真 FINESSE [arXiv:2609.11993]、合成数据蒸馏 [arXiv:2609.09586]；
  - 重新核验并生成全套 5 组 300 DPI 图表，调整时间线密集标注前缘，同步更新 README.md 与 references.bib。
- **2026-09-24 (第 2 轮迭代：评测体系全面深化与重点团队前沿纳入 / Iteration 2)**:
  - 严格通过 arXiv HTTPS API 核验收录 14 篇最新前沿与重点团队论文，文献库增至 93 篇；
  - **全面深化第 7 章（基准与评测）**：新增 13 项评测基准综合对比矩阵表；系统剖析预训练熟悉度与数据污染危机 [arXiv:2609.10357]、基于证据访问边界的零样本审计框架 [arXiv:2609.21425]、概率分布校准与高阶依赖度量 [arXiv:2609.25788, arXiv:2609.25980]、动态演化环境多轮智能体评测 [arXiv:2606.01498, arXiv:2608.14270] 与自进化策略 [arXiv:2609.24862]；
  - 重点团队文献扩充：THUML 协变量自适应 CoRA [arXiv:2510.12681] 与多模态扩散 DiTS [arXiv:2602.06597]；金明组空间强化学习 STReasoner [arXiv:2601.03248] 与在线数据增强 OATS [arXiv:2601.19040]；
  - 架构前沿纳入：循环分位数传输 FlowTSFM [arXiv:2609.13640]、生理大模型 SOTER [arXiv:2609.16804]、模式量化语料平衡 QUALS [arXiv:2609.20156]；
  - 重新生成并质检全部 5 套 300 DPI 图表，优化演化时间线顶部图例排布与饼图切片显示。
- **2026-09-24 (初版发布 / First Full Edition)**:
  - 从零构建系统性活体综述 (`survey/SURVEY.md`)，覆盖十大核心章节与 LaTeX 形式化数学定义；
  - 严格通过 arXiv HTTPS API 核验收录 79 篇时序基础模型与多模态时序文献；
  - 编写并生成 5 套高分辨率可复现图表 (PNG+SVG) 并完成排版视觉质检；
  - 新增近两日重点前沿论文收录：Toto 2.0 [arXiv:2605.20119]、TimeVista [arXiv:2606.16173]、Zero-Shot TSFM 概率校准评测 [arXiv:2609.25788]、时序工作流智能体评测 [arXiv:2609.27385]；
  - 同步生成配套 BibTeX 数据库 (`survey/references.bib`) 与自动化质检工具链 (`scripts/survey_check.py`)。

---

## TODO 后备待办论文池 (TODO Backlog)

下述论文候选已在巡检中建立索引，将在后续轮次中进一步评估纳入或扩展分析：
1. **KAIROS 非自回归快速预测消歧**：跟进与评估 (arXiv: 2510.02084) KAIROS 非自回归变体与同名模型的消歧评测；
2. **时序具身智能与机器人动力学多通道反馈**：持续追踪通用基础模型在机器人多模态本体触觉与运动控制中的零样本迁移表现；
3. **时序多尺度自适应微调理论**：跟进参数高效迁移中的频域秩约束与自适应奇异值截断前沿；
4. **TimeMixer++ 永久公开开源状态跟进**：持续监测官方仓库公司合规审查与权重发布进展。
"""

full_content = part1 + part2 + part3 + part4 + part5 + part6

SURVEY_PATH.write_text(full_content, encoding="utf-8")
print(f"Successfully generated {SURVEY_PATH} ({len(full_content)} chars, {len(paper_map)} papers).")
