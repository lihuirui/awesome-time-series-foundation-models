# Awesome Time-Series Foundation Models (时序大模型)

> Curated list of **Time-Series Foundation Models (TSFMs)** and **Multimodal / Temporal VL** papers with **verified arXiv metadata only**.

> 仅收录经 arXiv API 核验的论文条目；严禁编造标题、作者、年份或链接。


### 📖 Living Survey / 活体综述

- **[Comprehensive Living Survey (时序基础模型全面综述)](survey/SURVEY.md)** — 涵盖数学定义、四大技术路线、模型对比表、跨模态前沿、评测基准与开放挑战。
- **[BibTeX References (参考文献库)](survey/references.bib)** — 由 `data/papers.json` 自动生成的完整 BibTeX 数据库。


**Maintainer focus:** 龙明盛/THUML · 金明 groups · Chronos-family · major TSFMs.


**Stats:** 138 verified papers in [`data/papers.json`](data/papers.json) (updated 2026-09-26).


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

- **Post-Training in Time Series Foundation Models: A Unifying Framework** — Shifeng Xie, Ambroise Odonnat, Zehao Xiao et al. (2026) [[arXiv](https://arxiv.org/abs/2607.20002)]
- **Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework** — Delun Kong, Wanyun Ling, Chenxi Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2609.21425)] *(ACM AI Summit 2026)* — _Source-first taxonomy and audit framework separating frozen LLM prior reuse, parametric TSFM pretraining, and RAG._
- **Foundation Models for Time Series Analysis: A Tutorial and Survey** — Yuxuan Liang, Haomin Wen, Yuqi Nie et al. (2024) [[arXiv](https://arxiv.org/abs/2403.14735)] *(ACM SIGKDD 2024)* — _KDD'24 tutorial/survey; methodology-centric FM taxonomy._
- **Large Language Models for Time Series: A Survey** — Xiyuan Zhang, Ranak Roy Chowdhury, Rajesh K. Gupta et al. (2024) [[arXiv](https://arxiv.org/abs/2402.01801)] [[Code](https://github.com/xiyuanzh/awesome-llm-time-series)]
- **Large Models for Time Series and Spatio-Temporal Data: A Survey and Outlook** — Ming Jin, Yaxuan Kong, Yuxuan Liang et al. (2023) [[arXiv](https://arxiv.org/abs/2310.10196)] *(ACM Computing Surveys)* [[Code](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM)] — _Jin/Wen survey; LM4TS & LM4STD taxonomy._
- **Transformers in Time Series: A Survey** — Qingsong Wen, Tian Zhou, Chaoli Zhang et al. (2022) [[arXiv](https://arxiv.org/abs/2202.07125)] *(IJCAI 2023)* [[Code](https://github.com/qingsongedu/time-series-transformers-review)] — _Pre-TSFM Transformer survey; useful background._


## Time-Series Foundation Models / 时序基础模型

- **$t_0$: A Time-Series Foundation Model for Forecasting with Context** — Lucas Meyer, Claudio Sole, Huikan Xiang et al. (2026) [[arXiv](https://arxiv.org/abs/2609.24559)] — _t₀; TSFM for forecasting with context._
- **A Hybrid Attention Model Learning Unified Time-aware Patch Representation for Irregular Multivariate Time Series Forecasting** — Zhihao Lin, Li Lin, Qi Zhang et al. (2026) [[arXiv](https://arxiv.org/abs/2609.22836)] *(arXiv)*
- **A Unified Shape-Aware Foundation Model for Time Series Classification** — Zhen Liu, Yucheng Wang, Boyuan Li et al. (2026) [[arXiv](https://arxiv.org/abs/2601.06429)] *(AAAI 2026)* — _UniShape: unified shape-aware foundation model tailored for time series classification using interpretable shapelets._
- **Align-RAG: Alignment Is All You Need for TSFM In-Context Learning** — Mohammad Asadi, Soheil Hor, Bardiya Akhbari et al. (2026) [[arXiv](https://arxiv.org/abs/2608.05571)] [[Code](https://github.com/masadi-99/align-rag)]
- **CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting** — Yosuke Yamaguchi, Issei Suemitsu, Yuki Kajihara et al. (2026) [[arXiv](https://arxiv.org/abs/2606.10798)] *(EUSIPCO 2026)* [[Code](https://github.com/hitachi-ais/citras-fm)] — _EUSIPCO 2026; 7M-parameter tiny TSFM optimized for real-time CPU inference with covariates._
- **Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series Foundation Model** — Roberto Tacconelli (2026) [[arXiv](https://arxiv.org/abs/2609.06008)] — _Error-bounded lossy compression pairing Google TimesFM-3 (330M) with adaptive arithmetic coding guaranteeing strict error bounds._
- **ChorusTIC: Training-Free Multivariate Time Series Classification via Chorus In-Context Learning** — Juntao Fang, Shifeng Xie, Ruichu Cai et al. (2026) [[arXiv](https://arxiv.org/abs/2608.24033)] — _Training-free multivariate time series classification via chorus in-context learning with foundation model embeddings._
- **Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding** — Paul Quinlan, Jeremy Levasseur, Qingguo Li et al. (2026) [[arXiv](https://arxiv.org/abs/2605.20268)] *(arXiv)* — _324M parameter unified decoder-only transformer trained from scratch on natural language and time series._
- **DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters** — Haoran Zhang, Haixuan Liu, Yong Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2602.06597)] — _THUML multimodal diffusion transformer (DiT) framework for high-dimensional and cross-modal time series forecasting._
- **Distillation of Synthetic Data for Time Series Foundation Models** — Niloy Biswas, Noureddine El Karoui (2026) [[arXiv](https://arxiv.org/abs/2609.09586)] — _Data distillation framework for time series foundation models pre-trained on synthetic trajectories under fixed dataset budgets._
- **Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models** — Haiqiang Chen, Li Chen, Yunlong Chen et al. (2026) [[arXiv](https://arxiv.org/abs/2609.20554)] — _Systematic investigation of look-ahead bias and future data leakage in pretrained financial time-series foundation models._
- **EIDOS: Latent-Space Predictive Learning for Time Series Foundation Models** — Xinxing Zhou, Qingren Yao, Yiji Zhao et al. (2026) [[arXiv](https://arxiv.org/abs/2602.14024)] — _金明 coauthor; latent-space predictive learning for TSFMs._
- **EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series** — Seunghan Lee, Jaehoon Lee, Jun Seo et al. (2026) [[arXiv](https://arxiv.org/abs/2609.04239)]
- **FactoryNet: A Large-Scale Dataset toward Industrial Time-Series Foundation Models** — Karim Othman, Jonas Petersen, Matei Ignuta-Ciuncanu et al. (2026) [[arXiv](https://arxiv.org/abs/2605.09081)] *(ICML 2026)* [[Code](https://github.com/Forgis-Labs/FactoryNet)] — _First universal pretraining corpus for industrial robotics and manufacturing time series across physical embodiments._
- **Falcon-X: A Time Series Foundation Model for Heterogeneous Multivariate Modeling** — Yiding Liu, Yifan Hu, Hongjie Xia et al. (2026) [[arXiv](https://arxiv.org/abs/2605.27286)] *(arXiv)* — _Decouples heterogeneous variates and maps into a unified latent prototype space with Prototype Diff-Attention._
- **FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting** — Amit Sharma, Nitin Auluck, Akramul Azim (2026) [[arXiv](https://arxiv.org/abs/2608.01290)]
- **FlowTSFM: Turning Encoder Depth into Quantile Transport** — Bahaeddine Abdessalem, Shifeng Xie, Zehao Xiao et al. (2026) [[arXiv](https://arxiv.org/abs/2609.13640)] — _FlowTSFM: 38.8M param encoder interpreting depth as recurrent quantile transport with pinball loss and path supervision._
- **Forecast Collapse in Time-Series Foundation Models** — Shu Wan, Miles Ma, Hank Zhu et al. (2026) [[arXiv](https://arxiv.org/abs/2608.14106)] — _Empirical discovery of forecast collapse where TSFM predictions degenerate into flat lines on noisy financial time series._
- **Ground-Truth Neighborhood Regularization for Reinforcement Learning Post-Training of Time Series Foundation Models** — Jianqi Zhang, Xingyu Zhang, Zeen Song et al. (2026) [[arXiv](https://arxiv.org/abs/2608.08010)] — _Reinforcement learning post-training for TSFMs with ground-truth neighborhood regularization to prevent reward collapse._
- **Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models** — Jinmyeong Choi, Jinkwan Jang, Seul Lee et al. (2026) [[arXiv](https://arxiv.org/abs/2609.25980)] — _Training-free post-processing coupling frozen univariate TSFM marginal distributions into joint multivariate forecast paths._
- **Knowledge-Graph-Augmented Chronos-2 for HEC-RAS Surrogate Forecasting** — Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi (2026) [[arXiv](https://arxiv.org/abs/2609.21381)]
- **LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning** — Alexander Chemeris, Ming Jin, Randall Balestriero (2026) [[arXiv](https://arxiv.org/abs/2607.00958)] *(KDD MILETS 2026)* [[Code](https://github.com/langotime/lenepa-milets-2026)] — _No-augmentation next-latent prediction (JEPA-style) representation learning avoiding destructive time series data augmentations._
- **LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling** — Sheng Pan, Ming Jin, Bo Du et al. (2026) [[arXiv](https://arxiv.org/abs/2605.10292)] *(arXiv)*
- **MACROCAST: A Vintage-Consistent Time Series Foundation Model for Real-Time Macroeconomic Forecasting** — Andrea Carriero, Davide Pettenuzzo, Shubhranshu Shekhar (2026) [[arXiv](https://arxiv.org/abs/2606.28670)] *(arXiv)* — _Vintage-consistent macroeconomic TSFM strictly avoiding revision leakage via synthetic pretraining._
- **OATS: Online Data Augmentation for Time Series Foundation Models** — Junwei Deng, Chang Xu, Jiaqi W. Ma et al. (2026) [[arXiv](https://arxiv.org/abs/2601.19040)] [[Code](https://github.com/microsoft/TimeCraft)] — _Online dynamic data augmentation via diffusion for pretraining TSFMs; part of Microsoft TimeCraft._
- **Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density** — Jingru Fei, Kun Yi, Alex Xing Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2605.17340)] *(ICML 2026)* [[Code](https://github.com/TSTS13/Olivia)] — _ICML 2026; Introduces Harmonizer module to align heterogeneous datasets in power spectral density domain._
- **QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization** — Yujie Li, Zezhi Shao, Chengqing Yu et al. (2026) [[arXiv](https://arxiv.org/abs/2609.20156)] *(VLDB 2027)* — _VLDB 2027; resolves multi-domain corpus imbalance and forgetting in TSFMs via pattern quantization and learnability synchronization._
- **SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models** — Xin-Yu Hu, Shuang Liang, Cheng Feng et al. (2026) [[arXiv](https://arxiv.org/abs/2609.28582)] — _Self-Guided Autoregressive (SGA) framework quantifying multi-step forecast uncertainty and mitigating error accumulation in TSFMs._
- **SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals** — Fangke Chen, Sirry Chen, Wei Chen et al. (2026) [[arXiv](https://arxiv.org/abs/2609.16804)] — _Generative foundation model for physiological signals; PSD-guided MoE and neural CDE decoder pretrained on 226B points._
- **Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking** — Taihua Chen, Xiang Ma, Yixin Zhang et al. (2026) [[arXiv](https://arxiv.org/abs/2608.20005)] — _Scale-aware pretraining handling diverse temporal frequencies through multi-patch token alignment and hybrid masking._
- **SwitchPFN: Shared Switching Dynamics for Frozen In-Context Time Series Classification** — Zhenyi Zhu, Jacqueline Pang, Peilin Shen et al. (2026) [[arXiv](https://arxiv.org/abs/2609.29814)]
- **TRACE: A Temporal Conditional Estimation for Multimodal Time Series Foundation Models** — Ziwen Kan, Yishuo Chen, Kecheng Li et al. (2026) [[arXiv](https://arxiv.org/abs/2606.06285)] — _TRACE; multimodal time series foundation models._
- **TW3Cast: A Frozen Router of Lightly Fine-Tuned Foundation Models for Time-Series Forecasting on GIFT-Eval, Selected Entirely on the Training Split** — Nathan Thierry, Andre-Louis Rochet (2026) [[arXiv](https://arxiv.org/abs/2609.28506)]
- **Tabby: An Open Pretraining Recipe for Time Series Foundation Models** — Shifeng Xie, Bahaeddine Abdessalem, Zehao Xiao et al. (2026) [[arXiv](https://arxiv.org/abs/2609.13956)] — _Tabby; open pretraining recipe for TSFMs._
- **Time-Series Foundation Models That Understand Data Revisions** — Taimoor Ahmad (2026) [[arXiv](https://arxiv.org/abs/2609.28576)]
- **Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling** — Yong Liu, Xingjian Su, Shiyu Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2603.04791)] [[Code](https://github.com/thuml/Large-Time-Series-Model)] — _THUML / 龙明盛; Timer-S1 8.3B MoE with Serial-Token Prediction; TimeBench._
- **Toto 2.0: Time Series Forecasting Enters the Scaling Era** — Emaad Khwaja, Chris Lettieri, Gerald Woo et al. (2026) [[arXiv](https://arxiv.org/abs/2605.20119)] [[Code](https://github.com/DataDog/toto)] — _Datadog Toto 2.0; scaling time series foundation models up to 2.5B parameters._
- **WaveMoE: A Wavelet-Enhanced Mixture-of-Experts Foundation Model for Time Series Forecasting** — Shunyu Wu, Jiawei Huang, Weibin Feng et al. (2026) [[arXiv](https://arxiv.org/abs/2604.10544)] *(ICLR 2026 TSALM Workshop)* — _ICLR 2026 TSALM; Wavelet-enhanced MoE foundation model routing sub-frequency temporal components._
- **Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis** — Yisong Fu, Zezhi Shao, Chengqing Yu et al. (2026) [[arXiv](https://arxiv.org/abs/2607.01918)] *(ICML 2026)* — _ICML 2026; Unified tuning-free TSFM with U-shaped hierarchy and Multi-Objective Temporal Masking (MOTM)._
- **Chronos-2: From Univariate to Universal Forecasting** — Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken et al. (2025) [[arXiv](https://arxiv.org/abs/2510.15821)] [[Code](https://github.com/amazon-science/chronos-forecasting)] — _Native multivariate + covariate ICL._
- **CoRA: Covariate-Aware Adaptation of Time Series Foundation Models** — Guo Qin, Zhi Chen, Yong Liu et al. (2025) [[arXiv](https://arxiv.org/abs/2510.12681)]
- **FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting** — Xingjian Wu, Hanyin Cheng, Xiangfei Qiu et al. (2025) [[arXiv](https://arxiv.org/abs/2512.14253)] — _FLAME; flow-enhanced Legendre memory for general forecasting._
- **FlowState: Sampling-Rate-Equivariant Time-Series Forecasting** — Lars Graf, Thomas Ortner, Stanisław Woźniak et al. (2025) [[arXiv](https://arxiv.org/abs/2508.05287)] [[Code](https://huggingface.co/ibm-granite/granite-timeseries-flowstate-r1)] — _IBM FlowState; sampling-rate-equivariant SSM+functional decoder; also in granite-tsfm._
- **From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting** — Shi Bin Hoo, Samuel Müller, David Salinas et al. (2025) [[arXiv](https://arxiv.org/abs/2501.02945)] [[Code](https://github.com/PriorLabs/tabpfn-time-series)] — _TabPFN-TS; tabular foundation model extended to time series._
- **KAIROS: Unified Training for Universal Non-Autoregressive Time Series Forecasting** — Kuiye Ding, Fanda Fan, Zheya Wang et al. (2025) [[arXiv](https://arxiv.org/abs/2510.02084)] — _Disambiguated from Kairos (2509.25826); universal non-autoregressive segment-level multi-peak distribution modeling._
- **Kairos: Toward Adaptive and Parameter-Efficient Time Series Foundation Models** — Kun Feng, Shaocheng Lan, Yuchen Fang et al. (2025) [[arXiv](https://arxiv.org/abs/2509.25826)] [[Code](https://github.com/foundation-model-research/Kairos)] — _Mixture-of-Size tokenization; PreSTS corpus; project page also at foundation-model-research.github.io/Kairos._
- **LightGTS: A Lightweight General Time Series Forecasting Model** — Yihang Wang, Yuying Qiu, Peng Chen et al. (2025) [[arXiv](https://arxiv.org/abs/2506.06005)] *(ICML 2025)* [[Code](https://github.com/decisionintelligence/LightGTS)] — _ICML 2025; periodical tokenization + parallel decoding; ~4M params._
- **Moirai 2.0: When Less Is More for Time Series Forecasting** — Chenghao Liu, Taha Aksu, Juncheng Liu et al. (2025) [[arXiv](https://arxiv.org/abs/2511.11698)] [[Code](https://github.com/SalesforceAIResearch/uni2ts)] — _Moirai 2.0 (Salesforce); decoder-only / quantile + multi-token prediction._
- **Output Scaling: YingLong-Delayed Chain of Thought in a Large Pretrained Time Series Forecasting Model** — Xue Wang, Tian Zhou, Jinyang Gao et al. (2025) [[arXiv](https://arxiv.org/abs/2506.11029)] [[Code](https://huggingface.co/qcw1314/YingLong_300m)] — _YingLong; encoder-only pretrained TSFM with delayed CoT / output scaling._
- **Sundial: A Family of Highly Capable Time Series Foundation Models** — Yong Liu, Guo Qin, Zhiyuan Shi et al. (2025) [[arXiv](https://arxiv.org/abs/2502.00816)] [[Code](https://github.com/thuml/Sundial)] — _THUML; TimeFlow Loss; TimeBench._
- **This Time is Different: An Observability Perspective on Time Series Foundation Models** — Ben Cohen, Emaad Khwaja, Youssef Doubli et al. (2025) [[arXiv](https://arxiv.org/abs/2505.14766)] [[Code](https://github.com/DataDog/toto)] — _Toto (Datadog) + BOOM benchmark._
- **TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning** — Andreas Auer, Patrick Podest, Daniel Klotz et al. (2025) [[arXiv](https://arxiv.org/abs/2505.23719)] — _xLSTM-based; NeurIPS 2025._
- **TimesBERT: A BERT-Style Foundation Model for Time Series Understanding** — Haoran Zhang, Yong Liu, Yunzhong Qiu et al. (2025) [[arXiv](https://arxiv.org/abs/2502.21245)]
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

- **ChatAD: Reasoning-Enhanced Time-Series Anomaly Detection with Multi-Turn Instruction Evolution** — Hui Sun, Chang Xu, Haonan Xie et al. (2026) [[arXiv](https://arxiv.org/abs/2601.13546)]
- **Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools** — Shunya Nagashima (2026) [[arXiv](https://arxiv.org/abs/2609.27385)] — _Forecast Workflow Bench; evaluates LLM-based agentic decision making with budgeted time-series forecasting tools._
- **LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models** — Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen et al. (2026) [[arXiv](https://arxiv.org/abs/2607.24892)] — _Training-free text conditioning using LLMs as forecasting planners to decompose numerical and textual context for frozen TSFMs._
- **MILM: Large Language Models for Multimodal Irregular Time Series with Informative Sampling** — Hsing-Huan Chung, Shijun Li, Yoav Wald et al. (2026) [[arXiv](https://arxiv.org/abs/2605.13711)] *(arXiv)* — _Represents multimodal irregular time series as XML triplets with informative sampling in LLMs._
- **Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning** — Patara Trirat, Jin Myung Kwak, Jay Heo et al. (2026) [[arXiv](https://arxiv.org/abs/2601.19151)] *(EMNLP 2026)* — _EMNLP 2026; TS-Debate inference-time multi-agent protocol coordinating text, vision, and numerical agents._
- **ReasonCast: Agentic Demand Forecasting with Selective Semantic Reasoning** — Ziyue Yang, Chaolin Xu, Yijing Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2608.15291)] — _Agentic demand forecasting framework with selective semantic reasoning triggering LLM reasoning only on volatile non-stationarities._
- **Rethinking Post-Training Recipes for Multimodal Time-Series Forecasting** — Haoxin Liu, Yichen Zhou, Rajat Sen et al. (2026) [[arXiv](https://arxiv.org/abs/2605.29401)] *(arXiv)* — _PostTime: combines SFT and RLVR to teach LLMs to act as context-guided revisors for numerical TSFM priors._
- **STReasoner: Empowering LLMs for Spatio-Temporal Reasoning in Time Series via Spatial-Aware Reinforcement Learning** — Juntong Ni, Shiyu Wang, Qi He et al. (2026) [[arXiv](https://arxiv.org/abs/2601.03248)] *(ACL 2026)* [[Code](https://github.com/LingFengGold/STReasoner)]
- **TimeBraid: Unifying Time Series and Language for Understanding and Forecasting** — Xinyue Wang, Jiacheng Pang, Kun Zhou et al. (2026) [[arXiv](https://arxiv.org/abs/2609.29792)]
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
- **FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences** — Tyler Farnan, Benjamin Eng, Adam Abate et al. (2026) [[arXiv](https://arxiv.org/abs/2609.11993)]
- **GALA: Generation-Aware Cross-Modal Alignment for Text-to-Time-Series Synthesis** — Haochen Zhang, Gengwei Zhang, Laura Yao et al. (2026) [[arXiv](https://arxiv.org/abs/2608.13741)] — _Generation-aware cross-modal alignment framework for high-fidelity text-to-time-series conditional diffusion synthesis._
- **Rethinking Multimodal Time-Series Forecasting Evaluation** — Haoxin Liu, Yichen Zhou, Rajat Sen et al. (2026) [[arXiv](https://arxiv.org/abs/2607.06973)] — _Rethinking multimodal time-series forecasting evaluation._
- **SCENARIODIFF: A Scenario-level Guidance Framework for Multimodal Time Series Forecasting--Extended Version** — Tuan-Binh Tran, Dat Nguyen Cong, Duc-Trong Le et al. (2026) [[arXiv](https://arxiv.org/abs/2608.17164)] *(arXiv)* — _Hierarchical reasoning framework decomposing news/reports into scenarios and anchors to guide multimodal diffusion forecasters._
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
- **Causal Analysis for Time Series Foundation Models** — Mathis Jander, Wouter van Heeswijk, Martijn Mes (2026) [[arXiv](https://arxiv.org/abs/2608.24303)]
- **Do Time Series Foundation Model Benchmarks Hide Regime-Dependent Failures? Evidence from Traffic Speed Forecasting** — Yingshuo Wang, Xian Sun, Lingdong Kong et al. (2026) [[arXiv](https://arxiv.org/abs/2606.18367)] *(arXiv)* — _Introduces regime-stratified evaluation for traffic speed benchmarks, revealing severe failure modes during congestion phase transitions._
- **Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study** — Guan-Hua Wen, Kuan-Yu Chen (2026) [[arXiv](https://arxiv.org/abs/2608.22968)] *(CIF 2026)*
- **Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models** — Panagiotis Michael, Moysis Symeonides, Demetris Trihinas (2026) [[arXiv](https://arxiv.org/abs/2609.25788)] *(ADBIS 2026)* — _ADBIS 2026; benchmark study on zero-shot TSFMs analyzing predictive accuracy and probabilistic calibration trade-offs._
- **HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications** — Inesh Chakrabarti, Zejun Xiong, Pragya Sharma et al. (2026) [[arXiv](https://arxiv.org/abs/2609.12412)]
- **It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks** — Zhongzheng Qiao, Sheng Pan, Anni Wang et al. (2026) [[arXiv](https://arxiv.org/abs/2602.12147)] [[Code](https://huggingface.co/spaces/Real-TSF/TIME-leaderboard)] — _ICML 2026; THUML+Jin coauthors; leakage-aware zero-shot._
- **LiveHouse-TS: An Open-world Living Benchmark for Time Series Foundation Models** — Haomin Wen, Ziyu Zhou, Qingxiang Liu et al. (2026) [[arXiv](https://arxiv.org/abs/2608.17299)] — _LiveHouse-TS; open-world living benchmark for TSFMs._
- **When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters** — Nicholas Tan Jerome, Frank Simon (2026) [[arXiv](https://arxiv.org/abs/2607.04919)] *(arXiv)* — _Break-even economic and accuracy analysis comparing TSFMs (Chronos, Moirai, Lag-Llama) against XGBoost/ARIMA across 30 datasets._
- **Estimating Time Series Foundation Model Transferability via In-Context Learning** — Qingren Yao, Ming Jin, Chengqi Zhang et al. (2025) [[arXiv](https://arxiv.org/abs/2509.23695)] — _Ming Jin group zero-shot in-context transferability estimation framework for downstream TSFM fine-tuning model selection._
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

