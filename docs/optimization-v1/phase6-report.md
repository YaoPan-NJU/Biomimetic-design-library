# Phase 6 — PDF 逐条核验 · 报告（最终版）

## 核验结果

| 状态 | 数量 | 说明 |
|------|------|------|
| **verified** | 25 张卡 | 有本地 PDF 支撑 + source_file + locator + quote |
| **needs_review** | 3 张卡 | 本地无文献，已写入 literature-requests.md |

## 已核验的 25 张卡

| 原型 | 机制 | 来源 PDF |
|------|------|---------|
| mussel-foot-adhesion | PDA涂层粘附机制 | Lee2007 Science |
| mussel-foot-adhesion | PDA自聚合形成机制 | Lee2007 Science |
| mussel-foot-adhesion | 铀酰离子配位化学 | Liu2024 设计原则 |
| chitosan | pH对氮污染物吸附 | Lei2021 Polymer |
| chitosan | 金属离子络合机制 | Lei2021 Polymer |
| chlorella-cell-wall | 藻类去除合成染料 | Lei2021 Polymer |
| diatom-frustule | Pb²⁺吸附机理(XPS证据) | Guo2022 环境工程 |
| polydopamine-coating | PDA吸附机制补充 | Lei2021 Polymer |
| sulfate-reducing-bacteria | SRB硫酸盐还原机理 | Kumar2021 J Environ Man |
| iron-oxidizing-bacteria | 施氏矿物As(III)吸附 | Luo2021 环境化学 |
| bone-structure | HAp四种重金属吸附 | Bambaeero2021 CJChE |
| oyster-shell | 牡蛎壳改性吸附 | 李2017 牡蛎壳生物炭 |
| scallop-shell | 吸附机理三步骤 | Wang2024 海洋科学 |
| fish-scale-hydroxyapatite | 八重协同吸附 | Balasooriya2022 HA review |
| lobster-exoskeleton | Chitosan beads吸附机制 | Lei2021 Polymer |
| mangrove-root | 人工湿地净化途径 | 刘2022 红树林 |
| mycelium | CMC水凝胶重金属螯合 | Waliullah2023 |
| wood-xylem | 吸附机制——酚+静电 | Mo2021 木纳米纤维 |
| silk-fibroin | 吸附机制 | Prasad2022 ETI |
| spider-silk | 抗污染机制 | Wang2024 antifouling |
| dna-aptamer | DNA适配体分子识别 | Li2021 分析测试学报 |
| biomineralization-template | 生物矿化模板吸附 | Wang2025 CEJ |
| plant-tannin | 单宁酸-金属配位 | Zhu2022 Ind Crops |
| cell-membrane-ion-channel | 细胞膜仿生设计 | BerattoRamos2022 |
| bio-structure | HAp重金属 | Bambaeero2021 |

## 仍待下载的 3 张卡（Y + coral + pitcher）

| 原型 | 机制 | 原因 |
|------|------|------|
| coral-skeleton | 珊瑚骨骼CaCO₃吸附 | 本地无珊瑚骨骼文献 |
| magnetic-bacteria | 趋磁细菌磁小体分离 | 本地无磁细菌文献 |
| pitcher-plant-slippery-surface | Nepenthes SLIPS抗污 | 本地无猪笼草SLIPS文献 |

## 产物

| 文件 | 内容 |
|------|------|
| `verify-logs/*.md` | 24 个原型的核验日志 |
| `literature-requests.md` | 3 个待下载原型的检索词 |

## source_file 修正记录

- biomineralization/dna-aptamer/plant-tannin：source_file 从 None 填为实际 PDF 路径
- mussel×2/bone：ref_doi 从无关 DOI 改为实际核验的 PDF DOI

---

**Phase 6 核验：本地 verified 25 张 / 仍无本地来源 3 张（coral-skeleton + magnetic-bacteria + pitcher-plant）。**
