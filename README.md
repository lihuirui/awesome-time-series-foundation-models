# Awesome Time-Series Foundation Models (时序大模型)

> Curated list of **Time-Series Foundation Models (TSFMs)** and **Multimodal / Temporal VL** papers with **verified arXiv metadata only**.

> 仅收录经 arXiv API 核验的论文条目；严禁编造标题、作者、年份或链接。


### 📖 Living Survey / 活体综述

- **[Comprehensive Living Survey (时序基础模型全面综述)](survey/SURVEY.md)** — 涵盖数学定义、四大技术路线、模型对比表、跨模态前沿、评测基准与开放挑战。
- **[BibTeX References (参考文献库)](survey/references.bib)** — 由 `data/papers.json` 自动生成的完整 BibTeX 数据库。


**Maintainer focus:** 龙明盛/THUML · 金明 groups · Chronos-family · major TSFMs.


**Stats:** 93 verified papers in [`data/papers.json`](data/papers.json) (updated 2026-09-24).


## Visual Landscape / 演化图景

![TSFM Timeline](survey/figures/tsfm_timeline.png)


## Table of Contents

- [Living Survey / 活体综述](#-living-survey--活体综述)
- [Visual Landscape / 演化图景](#visual-landscape--演化图景)
- [Surveys / 综述](#surveys)
- [Time-Series Foundation Models / 时序基础模型](#time-series-foundation-models)
- [LLM for Time Series / 大模型赋能时序](#llm-for-time-series)
- [Multimodal Time Series & Temporal VL / 多模态时序](#multimodal-time-series--temporal-vl)
- [Benchmarks & Datasets / 基准与数据集](#benchmarks--datasets)
- [Toolkits / 工具库](#toolkits--工具库)
- [Resources / 资源](#resources--资源)
- [Maintenance](#maintenance)

---


## Surveys / 综述

- **Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework** — Delun Kong, Wanyun Ling, Chenxi Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2609.21425)] *(ACM AI Summit 2026)* — _Source-first taxonomy and audit framework separating frozen LLM prior reuse, parametric TSFM pretraining, and RAG._
- **Foundation Models for Time Series Analysis: A Tutorial and Survey** — Yuxuan Liang, Haomin Wen, Yuqi Nie et al. (2024) [[arXiv](https://arxiv.org/abs/2403.14735)] *(ACM SIGKDD 2024)* — _KDD'24 tutorial/survey; methodology-centric FM taxonomy._
- **Large Language Models for Time Series: A Survey** — Xiyuan Zhang, Ranak Roy Chowdhury, Rajesh K. Gupta et al. (2024) [[arXiv](https://arxiv.org/abs/2402.01801)] [[Code](https://github.com/xiyuanzh/awesome-llm-time-series)]
- **Large Models for Time Series and Spatio-Temporal Data: A Survey and Outlook** — Ming Jin, Yaxuan Kong, Yuxuan Liang et al. (2023) [[arXiv](https://arxiv.org/abs/2310.10196)] *(ACM Computing Surveys)* [[Code](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM)] — _Jin/Wen survey; LM4TS & LM4STD taxonomy._
- **Transformers in Time Series: A Survey** — Qingsong Wen, Tian Zhou, Chaoli Zhang et al. (2022) [[arXiv](https://arxiv.org/abs/2202.07125)] *(IJCAI 2023)* [[Code](https://github.com/qingsongedu/time-series-transformers-review)] — _Pre-TSFM Transformer survey; useful background._


## Time-Series Foundation Models / 时序基础模型

- **$t_0$: A Time-Series Foundation Model for Forecasting with Context** — Lucas Meyer, Claudio Sole, Huikan Xiang et al. (2026) [[arXiv](https://arxiv.org/abs/2609.24559)] — _t₀; TSFM for forecasting with context._
- **DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters** — Haoran Zhang, Haixuan Liu, Yong Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2602.06597)] — _THUML multimodal diffusion transformer (DiT) framework for high-dimensional and cross-modal time series forecasting._
- **EIDOS: Latent-Space Predictive Learning for Time Series Foundation Models** — Xinxing Zhou, Qingren Yao, Yiji Zhao et al. (2026) [[arXiv](https://arxiv.org/abs/2602.14024)] — _金明 coauthor; latent-space predictive learning for TSFMs._
- **FlowTSFM: Turning Encoder Depth into Quantile Transport** — Bahaeddine Abdessalem, Shifeng Xie, Zehao Xiao et al. (2026) [[arXiv](https://arxiv.org/abs/2609.13640)] — _FlowTSFM: 38.8M param encoder interpreting depth as recurrent quantile transport with pinball loss and path supervision._
- **Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models** — Jinmyeong Choi, Jinkwan Jang, Seul Lee et al. (2026) [[arXiv](https://arxiv.org/abs/2609.25980)] — _Training-free post-processing coupling frozen univariate TSFM marginal distributions into joint multivariate forecast paths._
- **OATS: Online Data Augmentation for Time Series Foundation Models** — Junwei Deng, Chang Xu, Jiaqi W. Ma et al. (2026) [[arXiv](https://arxiv.org/abs/2601.19040)] [[Code](https://github.com/microsoft/TimeCraft)] — _Online dynamic data augmentation via diffusion for pretraining TSFMs; part of Microsoft TimeCraft._
- **QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization** — Yujie Li, Zezhi Shao, Chengqing Yu et al. (2026) [[arXiv](https://arxiv.org/abs/2609.20156)] *(VLDB 2027)* — _VLDB 2027; resolves multi-domain corpus imbalance and forgetting in TSFMs via pattern quantization and learnability synchronization._
- **SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals** — Fangke Chen, Sirry Chen, Wei Chen et al. (2026) [[arXiv](https://arxiv.org/abs/2609.16804)] — _Generative foundation model for physiological signals; PSD-guided MoE and neural CDE decoder pretrained on 226B points._
- **TRACE: A Temporal Conditional Estimation for Multimodal Time Series Foundation Models** — Ziwen Kan, Yishuo Chen, Kecheng Li et al. (2026) [[arXiv](https://arxiv.org/abs/2606.06285)] — _TRACE; multimodal time series foundation models._
- **Tabby: An Open Pretraining Recipe for Time Series Foundation Models** — Shifeng Xie, Bahaeddine Abdessalem, Zehao Xiao et al. (2026) [[arXiv](https://arxiv.org/abs/2609.13956)] — _Tabby; open pretraining recipe for TSFMs._
- **Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling** — Yong Liu, Xingjian Su, Shiyu Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2603.04791)] [[Code](https://github.com/thuml/Large-Time-Series-Model)] — _THUML / 龙明盛; Timer-S1 8.3B MoE with Serial-Token Prediction; TimeBench._
- **Toto 2.0: Time Series Forecasting Enters the Scaling Era** — Emaad Khwaja, Chris Lettieri, Gerald Woo et al. (2026) [[arXiv](https://arxiv.org/abs/2605.20119)] [[Code](https://github.com/DataDog/toto)] — _Datadog Toto 2.0; scaling time series foundation models up to 2.5B parameters._
- **Chronos-2: From Univariate to Universal Forecasting** — Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken et al. (2025) [[arXiv](https://arxiv.org/abs/2510.15821)] [[Code](https://github.com/amazon-science/chronos-forecasting)] — _Native multivariate + covariate ICL._
- **CoRA: Covariate-Aware Adaptation of Time Series Foundation Models** — Guo Qin, Zhi Chen, Yong Liu et al. (2025) [[arXiv](https://arxiv.org/abs/2510.12681)]
- **FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting** — Xingjian Wu, Hanyin Cheng, Xiangfei Qiu et al. (2025) [[arXiv](https://arxiv.org/abs/2512.14253)] — _FLAME; flow-enhanced Legendre memory for general forecasting._
- **FlowState: Sampling-Rate-Equivariant Time-Series Forecasting** — Lars Graf, Thomas Ortner, Stanisław Woźniak et al. (2025) [[arXiv](https://arxiv.org/abs/2508.05287)] [[Code](https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1)] — _IBM FlowState; sampling-rate-equivariant SSM+functional decoder; also in granite-tsfm._
- **From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting** — Shi Bin Hoo, Samuel Müller, David Salinas et al. (2025) [[arXiv](https://arxiv.org/abs/2501.02945)] [[Code](https://github.com/PriorLabs/tabpfn-time-series)] — _TabPFN-TS; tabular foundation model extended to time series._
- **Kairos: Toward Adaptive and Parameter-Efficient Time Series Foundation Models** — Kun Feng, Shaocheng Lan, Yuchen Fang et al. (2025) [[arXiv](https://arxiv.org/abs/2509.25826)] [[Code](https://github.com/foundation-model-research/Kairos)] — _Mixture-of-Size tokenization; PreSTS corpus; project page also at foundation-model-research.github.io/Kairos._
- **LightGTS: A Lightweight General Time Series Forecasting Model** — Yihang Wang, Yuying Qiu, Peng Chen et al. (2025) [[arXiv](https://arxiv.org/abs/2506.06005)] *(ICML 2025)* [[Code](https://github.com/decisionintelligence/LightGTS)] — _ICML 2025; periodical tokenization + parallel decoding; ~4M params._
- **Moirai 2.0: When Less Is More for Time Series Forecasting** — Chenghao Liu, Taha Aksu, Juncheng Liu et al. (2025) [[arXiv](https://arxiv.org/abs/2511.11698)] [[Code](https://github.com/SalesforceAIResearch/uni2ts)] — _Moirai 2.0 (Salesforce); decoder-only / quantile + multi-token prediction._
- **Output Scaling: YingLong-Delayed Chain of Thought in a Large Pretrained Time Series Forecasting Model** — Xue Wang, Tian Zhou, Jinyang Gao et al. (2025) [[arXiv](https://arxiv.org/abs/2506.11029)] [[Code](https://huggingface.co/qcw1314/YingLong_300m)] — _YingLong; encoder-only pretrained TSFM with delayed CoT / output scaling._
- **Sundial: A Family of Highly Capable Time Series Foundation Models** — Yong Liu, Guo Qin, Zhiyuan Shi et al. (2025) [[arXiv](https://arxiv.org/abs/2502.00816)] [[Code](https://github.com/thuml/Sundial)] — _THUML; TimeFlow Loss; TimeBench._
- **This Time is Different: An Observability Perspective on Time Series Foundation Models** — Ben Cohen, Emaad Khwaja, Youssef Doubli et al. (2025) [[arXiv](https://arxiv.org/abs/2505.14766)] [[Code](https://github.com/DataDog/toto)] — _Toto (Datadog) + BOOM benchmark._
- **TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning** — Andreas Auer, Patrick Podest, Daniel Klotz et al. (2025) [[arXiv](https://arxiv.org/abs/2505.23719)] — _xLSTM-based; NeurIPS 2025._
- **Chronos: Learning the Language of Time Series** — Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen et al. (2024) [[arXiv](https://arxiv.org/abs/2403.07815)] *(Transactions on Machine Learning Research (TMLR))* [[Code](https://github.com/amazon-science/chronos-forecasting)] — _Chronos-Bolt is a later patch-based variant in the same repo/AWS blog; no standalone arXiv paper found (as of 2026-09-24)._
- **In-Context Fine-Tuning for Time-Series Foundation Models** — Abhimanyu Das, Matthew Faw, Rajat Sen et al. (2024) [[arXiv](https://arxiv.org/abs/2410.24087)] — _TimesFM-family / Google; in-context fine-tuning for TSFMs._
- **In-context Time Series Predictor** — Jiecheng Lu, Yan Sun, Shihao Yang (2024) [[arXiv](https://arxiv.org/abs/2405.14982)] — _ICTSP; in-context time series predictor (ICLR 2025)._
- **MOMENT: A Family of Open Time-series Foundation Models** — Mononito Goswami, Konrad Szafer, Arjun Choudhry et al. (2024) [[arXiv](https://arxiv.org/abs/2402.03885)] *(ICML 2024)* [[Code](https://huggingface.co/AutonLab/MOMENT-1-large)] — _Time Series Pile; ICML 2024._
- **Moirai-MoE: Empowering Time Series Foundation Models with Sparse Mixture of Experts** — Xu Liu, Juncheng Liu, Gerald Woo et al. (2024) [[arXiv](https://arxiv.org/abs/2410.10469)] [[Code](https://github.com/SalesforceAIResearch/uni2ts)]
- **Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts** — Xiaoming Shi, Shiyu Wang, Yuqi Nie et al. (2024) [[arXiv](https://arxiv.org/abs/2409.16040)] *(ICLR 2025)* — _金明 group; ICLR 2025; up to 2.4B params._
- **TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis** — Shiyu Wang, Jiawei Li, Xiaoming Shi et al. (2024) [[arXiv](https://arxiv.org/abs/2410.16032)] *(ICLR 2025)*
- **TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting** — Shiyu Wang, Haixu Wu, Xiaoming Shi et al. (2024) [[arXiv](https://arxiv.org/abs/2405.14616)] *(ICLR 2024)* [[Code](https://github.com/thuml/Time-Series-Library)] — _Included as major multiscale mixer; also in TSlib._
- **TimeXer: Empowering Transformers for Time Series Forecasting with Exogenous Variables** — Yuxuan Wang, Haixu Wu, Jiaxiang Dong et al. (2024) [[arXiv](https://arxiv.org/abs/2402.19072)] *(NeurIPS 2024)* [[Code](https://github.com/thuml/TimeXer)] — _THUML; exogenous-variable Transformer (NeurIPS 2024); not a separate TimesNet/Autoformer/iTransformer entry._
- **Timer-XL: Long-Context Transformers for Unified Time Series Forecasting** — Yong Liu, Guo Qin, Xiangdong Huang et al. (2024) [[arXiv](https://arxiv.org/abs/2410.04803)] *(NeurIPS 2024)* [[Code](https://github.com/thuml/Timer-XL)] — _THUML._
- **Timer: Generative Pre-trained Transformers Are Large Time Series Models** — Yong Liu, Haoran Zhang, Chenyu Li et al. (2024) [[arXiv](https://arxiv.org/abs/2402.02368)] *(ICML 2024)* [[Code](https://github.com/thuml/Large-Time-Series-Model)] — _THUML / 龙明盛 group._
- **Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series** — Vijay Ekambaram, Arindam Jati, Pankaj Dayama et al. (2024) [[arXiv](https://arxiv.org/abs/2401.03955)] *(NeurIPS 2024)* [[Code](https://huggingface.co/ibm-granite/granite-timeseries-ttm-r2)] — _IBM Granite TTM; NeurIPS 2024._
- **Towards a General Time Series Forecasting Model with Unified Representation and Adaptive Transfer** — Yihang Wang, Yuying Qiu, Peng Chen et al. (2024) [[arXiv](https://arxiv.org/abs/2405.17478)] *(ICML 2024)* [[Code](https://github.com/decisionintelligence/ROSE)]
- **UniTS: A Unified Multi-Task Time Series Model** — Shanghua Gao, Teddy Koker, Owen Queen et al. (2024) [[arXiv](https://arxiv.org/abs/2403.00131)] *(NeurIPS 2024)* [[Code](https://github.com/mims-harvard/UniTS)] — _NeurIPS 2024._
- **Unified Training of Universal Time Series Forecasting Transformers** — Gerald Woo, Chenghao Liu, Akshat Kumar et al. (2024) [[arXiv](https://arxiv.org/abs/2402.02592)] *(ICML 2024)* [[Code](https://github.com/SalesforceAIResearch/uni2ts)] — _Moirai / LOTSA; Salesforce._
- **VisionTS: Visual Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters** — Mouxiang Chen, Lefei Shen, Zhuo Li et al. (2024) [[arXiv](https://arxiv.org/abs/2408.17253)] *(NeurIPS 2024)* [[Code](https://github.com/Keytoyze/VisionTS)] — _ImageNet MAE as TSFM; ICML 2025._
- **A decoder-only foundation model for time-series forecasting** — Abhimanyu Das, Weihao Kong, Rajat Sen et al. (2023) [[arXiv](https://arxiv.org/abs/2310.10688)] *(ICML 2024)* [[Code](https://github.com/google-research/timesfm)] — _TimesFM (Google); ICML 2024._
- **ForecastPFN: Synthetically-Trained Zero-Shot Forecasting** — Samuel Dooley, Gurnoor Singh Khurana, Chirag Mohapatra et al. (2023) [[arXiv](https://arxiv.org/abs/2311.01933)] *(NeurIPS 2023)* — _NeurIPS 2023; synthetic PFN prior._
- **Lag-Llama: Towards Foundation Models for Probabilistic Time Series Forecasting** — Kashif Rasul, Arjun Ashok, Andrew Robert Williams et al. (2023) [[arXiv](https://arxiv.org/abs/2310.08278)] *(ICML 2024 Workshop)* [[Code](https://github.com/time-series-foundation-models/lag-llama)]


## LLM for Time Series / 大模型赋能时序

- **Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools** — Shunya Nagashima (2026) [[arXiv](https://arxiv.org/abs/2609.27385)] — _Forecast Workflow Bench; evaluates LLM-based agentic decision making with budgeted time-series forecasting tools._
- **LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models** — Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen et al. (2026) [[arXiv](https://arxiv.org/abs/2607.24892)] — _Training-free text conditioning using LLMs as forecasting planners to decompose numerical and textual context for frozen TSFMs._
- **STReasoner: Empowering LLMs for Spatio-Temporal Reasoning in Time Series via Spatial-Aware Reinforcement Learning** — Juntong Ni, Shiyu Wang, Qi He et al. (2026) [[arXiv](https://arxiv.org/abs/2601.03248)] *(ACL 2026)* [[Code](https://github.com/LingFengGold/STReasoner)]
- **When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting** — Yifan Hu, Xilin Dai, Zhiyuan Qu et al. (2026) [[arXiv](https://arxiv.org/abs/2609.24862)] — _TimEvolve: self-evolving policy framework for agentic TSF converting realized deployment outcomes into persistent orchestration updates._
- **$\textbf{S}^2$IP-LLM: Semantic Space Informed Prompt Learning with LLM for Time Series Forecasting** — Zijie Pan, Yushan Jiang, Sahil Garg et al. (2024) [[arXiv](https://arxiv.org/abs/2403.05798)]
- **AutoTimes: Autoregressive Time Series Forecasters via Large Language Models** — Yong Liu, Guo Qin, Xiangdong Huang et al. (2024) [[arXiv](https://arxiv.org/abs/2402.02370)] *(NeurIPS 2024)* [[Code](https://github.com/thuml/AutoTimes)] — _THUML._
- **CALF: Aligning LLMs for Time Series Forecasting via Cross-modal Fine-Tuning** — Peiyuan Liu, Hang Guo, Tao Dai et al. (2024) [[arXiv](https://arxiv.org/abs/2403.07300)] [[Code](https://github.com/Hank0626/LLaTA)]
- **ChatTS: Aligning Time Series with LLMs via Synthetic Data for Enhanced Understanding and Reasoning** — Zhe Xie, Zeyan Li, Xiao He et al. (2024) [[arXiv](https://arxiv.org/abs/2412.03104)] [[Code](https://github.com/NetManAIOps/ChatTS)] — _ChatTS; align multivariate TS with LLMs via synthetic data._
- **ChatTime: A Unified Multimodal Time Series Foundation Model Bridging Numerical and Textual Data** — Chengsen Wang, Qi Qi, Jingyu Wang et al. (2024) [[arXiv](https://arxiv.org/abs/2412.11376)] *(AAAI 2025)* — _AAAI 2025._
- **LLM-Mixer: Multiscale Mixing in LLMs for Time Series Forecasting** — Md Kowsher, Md. Shohanur Islam Sobuj, Nusrat Jahan Prottasha et al. (2024) [[arXiv](https://arxiv.org/abs/2410.11674)]
- **LSTPrompt: Large Language Models as Zero-Shot Time Series Forecasters by Long-Short-Term Prompting** — Haoxin Liu, Zhiyuan Zhao, Jindong Wang et al. (2024) [[arXiv](https://arxiv.org/abs/2402.16132)]
- **TimeCMA: Towards LLM-Empowered Multivariate Time Series Forecasting via Cross-Modality Alignment** — Chenxi Liu, Qianxiong Xu, Hao Miao et al. (2024) [[arXiv](https://arxiv.org/abs/2406.01638)] — _AAAI 2025 Oral._
- **LLM4TS: Aligning Pre-Trained LLMs as Data-Efficient Time-Series Forecasters** — Ching Chang, Wei-Yao Wang, Wen-Chih Peng et al. (2023) [[arXiv](https://arxiv.org/abs/2308.08469)] *(ACM TIST 2025)* [[Code](https://github.com/blacksnail789521/LLM4TS)]
- **Large Language Models Are Zero-Shot Time Series Forecasters** — Nate Gruver, Marc Finzi, Shikai Qiu et al. (2023) [[arXiv](https://arxiv.org/abs/2310.07820)] *(NeurIPS 2023)* [[Code](https://github.com/ngruver/llmtime)] — _LLMTime; NeurIPS 2023._
- **One Fits All:Power General Time Series Analysis by Pretrained LM** — Tian Zhou, PeiSong Niu, Xue Wang et al. (2023) [[arXiv](https://arxiv.org/abs/2302.11939)] *(NeurIPS 2023)* [[Code](https://github.com/DAMO-DI-ML/One_Fits_All)] — _GPT4TS / FPT; NeurIPS 2023 Spotlight._
- **TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting** — Defu Cao, Furong Jia, Sercan O Arik et al. (2023) [[arXiv](https://arxiv.org/abs/2310.04948)] *(ICLR 2024)* — _ICLR 2024._
- **Time-LLM: Time Series Forecasting by Reprogramming Large Language Models** — Ming Jin, Shiyu Wang, Lintao Ma et al. (2023) [[arXiv](https://arxiv.org/abs/2310.01728)] *(ICLR 2024)* — _金明; ICLR 2024._
- **UniTime: A Language-Empowered Unified Model for Cross-Domain Time Series Forecasting** — Xu Liu, Junfeng Hu, Yuan Li et al. (2023) [[arXiv](https://arxiv.org/abs/2310.09751)] *(WWW 2024)*
- **PromptCast: A New Prompt-based Learning Paradigm for Time Series Forecasting** — Hao Xue, Flora D. Salim (2022) [[arXiv](https://arxiv.org/abs/2210.08964)] *(IEEE TKDE)* [[Code](https://github.com/HaoUNSW/PISA)] — _Early prompt-to-forecast paradigm._


## Multimodal Time Series & Temporal VL / 多模态时序

- **Beyond Numerical Time Series: A Unified Benchmark for Multimodal Forecasting with Heterogeneous Context** — Peng Chen, Zhihao Zhuang, Hongzhou Chen et al. (2026) [[arXiv](https://arxiv.org/abs/2609.15087)] — _Unified multimodal forecasting benchmark with heterogeneous context._
- **Empowering VLMs for Few-Shot Multimodal Time Series Classification via Tailored Agentic Reasoning** — Lin Li, Jiawei Huang, Qihao Quan et al. (2026) [[arXiv](https://arxiv.org/abs/2605.09395)] [[Code](https://github.com/HuangJW0821/MarsTSC)] — _VLM agentic reasoning for few-shot multimodal TS classification._
- **Rethinking Multimodal Time-Series Forecasting Evaluation** — Haoxin Liu, Yichen Zhou, Rajat Sen et al. (2026) [[arXiv](https://arxiv.org/abs/2607.06973)] — _Rethinking multimodal time-series forecasting evaluation._
- **Sonar-TS: Search-Then-Verify Natural Language Querying for Time Series Databases** — Zhao Tan, Yiji Zhao, Shiyu Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2602.17001)] — _金明; ICML 2026; NLQ4TSDB + NLQTSBench._
- **Spectral Text Fusion: A Frequency-Aware Approach to Multimodal Time-Series Forecasting** — Huu Hiep Nguyen, Minh Hoang Nguyen, Dung Nguyen et al. (2026) [[arXiv](https://arxiv.org/abs/2602.01588)] [[Code](https://github.com/hiepnh137/SpecTF)] — _Spectral Text Fusion for multimodal TS forecasting._
- **TAC-Time: Texts as Channels For Multimodal Time Series Forecasting** — Jiayi Liang, Xiaotian Gu, Xinyu Xie et al. (2026) [[arXiv](https://arxiv.org/abs/2609.24156)] — _TAC-Time; texts as channels for multimodal TS forecasting._
- **TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series** — Sheng Pan, Yongli Gu, Yiqing Guo et al. (2026) [[arXiv](https://arxiv.org/abs/2609.26389)] — _金明; TimeInteract — real-time interactive streaming TS intelligence._
- **TimeOmni-VL: Unified Models for Time Series Understanding and Generation** — Tong Guan, Sheng Pan, Johan Barthelemy et al. (2026) [[arXiv](https://arxiv.org/abs/2602.17149)] *(ICML 2026)* — _金明; ICML 2026; Bi-TSI + understanding-guided generation._
- **TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments** — Qingren Yao, Yaxuan Kong, Yuqi Nie et al. (2026) [[arXiv](https://arxiv.org/abs/2608.14270)] — _Live benchmark tracking 60 institutional scenarios with 1,485 scenario-period QA pairs evaluating agents in evolving temporal environments._
- **TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning** — Yaxuan Kong, Qingren Yao, Yuqi Nie et al. (2026) [[arXiv](https://arxiv.org/abs/2606.01498)] — _Multi-turn benchmark for agentic TS reasoning with 240 tasks and 2,680 dialogue turns across 8 domains._
- **TimeVista: Exploring and Exploiting Vision-Language Models as Judges for Time Series Forecasting** — Zhi Chen, Yuxuan Wang, Jialong Wu et al. (2026) [[arXiv](https://arxiv.org/abs/2606.16173)] — _THUML / 龙明盛; Vision-Language Models as evaluators and judges for time series forecasting._
- **Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Natural Language** — Yunkai Zhang, Yawen Zhang, Ming Zheng et al. (2025) [[arXiv](https://arxiv.org/abs/2512.11251)] [[Code](https://huggingface.co/datasets/zhykoties/time-series-language-alignment)] — _Insight Miner; cross-domain TS–language alignment dataset._
- **OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data** — Patrick Langer, Thomas Kaar, Max Rosenblattl et al. (2025) [[arXiv](https://arxiv.org/abs/2510.02410)] [[Code](https://github.com/StanfordBDHG/OpenTSLM)] — _OpenTSLM (not OpenTSLab); medical text+TS reasoning._
- **SciTS: Scientific Time Series Understanding and Generation with LLMs** — Wen Wu, Ziyang Zhang, Liwei Liu et al. (2025) [[arXiv](https://arxiv.org/abs/2510.03255)] — _ICLR 2026; SciTS benchmark + TimeOmni framework._
- **Time-MQA: Time Series Multi-Task Question Answering with Context Enhancement** — Yaxuan Kong, Yiyuan Yang, Yoontae Hwang et al. (2025) [[arXiv](https://arxiv.org/abs/2503.01875)] *(ACL 2025)* — _Time-MQA; multi-task TS question answering with context._
- **Time-VLM: Exploring Multimodal Vision-Language Models for Augmented Time Series Forecasting** — Siru Zhong, Weilin Ruan, Ming Jin et al. (2025) [[arXiv](https://arxiv.org/abs/2502.04395)] [[Code](https://github.com/CityMind-Lab/ICML25-TimeVLM)] — _金明; ICML 2025 Time-VLM — temporal + vision + text via VLMs._
- **TimeOmni-1: Incentivizing Complex Reasoning with Time Series in Large Language Models** — Tong Guan, Zijie Meng, Dianqi Li et al. (2025) [[arXiv](https://arxiv.org/abs/2509.24803)] *(ICLR 2026)* — _金明; ICLR 2026; TSR-Suite._
- **Time-MMD: Multi-Domain Multimodal Dataset for Time Series Analysis** — Haoxin Liu, Shangqing Xu, Zhiyuan Zhao et al. (2024) [[arXiv](https://arxiv.org/abs/2406.08627)] [[Code](https://github.com/AdityaLab/Time-MMD)] — _NeurIPS 2024 D&B; MM-TSFlib._


## Benchmarks & Datasets / 基准与数据集

- **A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out** — Mahdi Naser Moghadasi, Faezeh Ghaderi (2026) [[arXiv](https://arxiv.org/abs/2609.10357)] [[Code](https://github.com/mahdinaser/tsfm-bench)] — _Critical evaluation of pretraining contamination in TSFMs; designs a strict time-delayed holdout postdating model release dates._
- **AION: Next-Generation Tasks and Practical Harness for Time Series** — Tianxiang Zhan, Xiaobao Song, Tong Guan et al. (2026) [[arXiv](https://arxiv.org/abs/2605.25045)] [[Code](https://github.com/ztxtech/aion)] — _金明; AION harness / next-gen TS tasks._
- **Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models** — Panagiotis Michael, Moysis Symeonides, Demetris Trihinas (2026) [[arXiv](https://arxiv.org/abs/2609.25788)] *(ADBIS 2026)* — _ADBIS 2026; benchmark study on zero-shot TSFMs analyzing predictive accuracy and probabilistic calibration trade-offs._
- **It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks** — Zhongzheng Qiao, Sheng Pan, Anni Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2602.12147)] [[Code](https://huggingface.co/spaces/Real-TSF/TIME-leaderboard)] — _ICML 2026; THUML+Jin coauthors; leakage-aware zero-shot._
- **LiveHouse-TS: An Open-world Living Benchmark for Time Series Foundation Models** — Haomin Wen, Ziyu Zhou, Qingxiang Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2608.17299)] — _LiveHouse-TS; open-world living benchmark for TSFMs._
- **Rethinking Evaluation in the Era of Time Series Foundation Models: (Un)known Information Leakage Challenges** — Marcel Meyer, Sascha Kaltenpoth, Kevin Zalipski et al. (2025) [[arXiv](https://arxiv.org/abs/2510.13654)] — _Leakage risks for TSFM eval._
- **GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation** — Taha Aksu, Gerald Woo, Juncheng Liu et al. (2024) [[arXiv](https://arxiv.org/abs/2410.10393)] [[Code](https://github.com/SalesforceAIResearch/gift-eval)]
- **TimeSeriesExam: A time series understanding exam** — Yifu Cai, Arjun Choudhry, Mononito Goswami et al. (2024) [[arXiv](https://arxiv.org/abs/2410.14752)] — _NeurIPS'24 workshop; LLM TS understanding exam._


## Toolkits / 工具库

- **Time-Series-Library (TSlib)** — THUML unified codebase (TimesNet, Autoformer, iTransformer, TimeMixer, etc. as baselines; not listed as separate Awesome entries above). [[GitHub](https://github.com/thuml/Time-Series-Library)]
- **GluonTS** — Probabilistic time series toolkit. [[arXiv](https://arxiv.org/abs/1906.05264)] [[Docs](https://ts.gluon.ai/)]
- **uni2ts / Moirai** — Salesforce TSFM stack. [[GitHub](https://github.com/SalesforceAIResearch/uni2ts)]
- **chronos-forecasting** — Amazon Chronos / Chronos-Bolt / Chronos-2. [[GitHub](https://github.com/amazon-science/chronos-forecasting)]
- **OpenLTM / Large-Time-Series-Model** — THUML Timer family. [[GitHub](https://github.com/thuml/Large-Time-Series-Model)]
- **Toto** — Datadog Toto 2.0 open-weights TSFM library. [[GitHub](https://github.com/DataDog/toto)]


## Resources / 资源

- Chronos-Bolt: **no standalone paper** (verified 2026-09-24). Use Chronos paper + [AWS blog](https://aws.amazon.com/blogs/machine-learning/fast-and-accurate-zero-shot-forecasting-with-chronos-bolt-and-autogluon/) + HF `amazon/chronos-bolt-*`.
- OpenTSLab: string not found as arXiv title; closest verified entry is **OpenTSLM** (`2510.02410`).
- TimeMixer++ (`2410.16032`): **permanent public code URL still unconfirmed** (2026-09-24). Paper appendix names [kwuking/TimeMixer](https://github.com/kwuking/TimeMixer); review anonymous repo [TimeMixerPP](https://anonymous.4open.science/r/TimeMixerPP); not in THUML TSlib. `code_url` kept null.
- Related Awesome lists: [Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM), [awesome-llm-time-series](https://github.com/xiyuanzh/awesome-llm-time-series).


## Maintenance

```bash
make all          # run validate, figures, survey-check, bibtex, readme
make fetch        # refresh titles/authors/years from arXiv HTTPS API
make validate     # schema + count checks
make figures      # regenerate all 5 reproducible figures
make survey-check # verify survey citations, figures and links
make bibtex       # regenerate survey/references.bib
make count        # print paper count
make readme       # regenerate this README from data/papers.json
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/MAINTENANCE.md](docs/MAINTENANCE.md).


## License

CC0-1.0 (see [LICENSE](LICENSE)).

