# Track 2B — 源项目设计抽取扩库日志（第一批）

**日期：** 2026-07-29 ｜ **分支：** `massive` ｜ **来源：** `biomimetic-adsorbent-design`（本地 checkout，Ultimate 分支 + main 分支 git show）

## 方法与红线
- 从源项目设计（`DEEP_RESEARCH_BIOMIMETIC_SCHEME_PORTFOLIO.md` 十套方案 + main 分支 ROX/PFHxS 深研文档）抽取**生物原型/机制**，而非搬运材料方案或性能数值。
- **知识隔离红线**：`performance_data` 一律留空，未从源项目搬运任何吸附容量数值；机制经**联网核验的原始文献**独立接地。
- 新原型只声明 `mechanism_tags` 即经机制层自动可达（Track 2A 能力）；对其关键目标污染物另做 pollutant_prototype_map 直接接线以保证 top-N 浮现。

## 抽取盘点（Ultimate portfolio 十套方案 vs 库中 89 原型）
- **已在库（V1-B 已吸收）**：hL-FABP(S1)、HSA(S3/S4)、ERRγ(S5)、核糖体出口隧道(S6)、TTR(S9)、氯酚羟化酶(S10) → 无需重复。
- **库中缺口→本批抽取**：**β-环糊精主客体包合(S2)**。
- **待下批评估**：ER/GPER 烷基酚受体(S7，证据弱)、BSA 疏水口袋(S8，与 HSA 近重复)、main 分支 ROX 生物膜类别富集 / PFHxS "PFH-1" / 大环内酯@阴离子磷脂界面（部分与 pulmonary-surfactant 重叠）。

## 本批入库（1 个）
### beta-cyclodextrin-host-guest-inclusion（β-环糊精天然环状腔体主客体包合）
- **生物身份**：细菌 CGTase 由淀粉环化生成的天然环状低聚糖（Bacillus sp.），非通用合成材料，过生物身份门槛。
- **机制**：① 锥台形天然疏水环腔对疏水/全氟链段主客体包合（from_source，Alsbaiee 2016 Nature 529:190，DOI 10.1038/nature19764，题录/页码接地）；② 环缘羟基 + 阳离子交联点对阴离子头基静电/氢键协同（literature_backed，Wang 2022 ACS Cent Sci，DOI 10.1021/acscentsci.2c00478，题录级）。
- **诚实分层**：Nature 页码接地要素标 from_source（2 条 causal 要素 compliant）；Wang 仅题录级→literature_backed；转译标 lead/inspiration；无搬运容量数值。
- **mechanism_tags**：疏水分配 / 孔道限域分子筛分 / 几何识别 / 氢键 / 静电吸附。
- **接线**：PFOA/PFOS/PFBS/BPA/Nonylphenol/MB（exploratory–lead）；导出含 β-CD 4 行。

## 验证
- 库规模 89 → **90** 原型；β-CD 对 BPA/PFOS/Nonylphenol 查询浮现（lane=exploratory，诚实）。
- validate_consistency 0 error；from_source_integrity 0 non-compliant（1619 compliant）；causal_chain 全合格；source_authenticity 无硬错误；check_chimera 10（预存，β-CD 单物种未新增）；boundary_guardrail 预存 superhydrophobic（β-CD 未触发）。
- 导出 390 行 / 44 污染物。

## 下一批建议
- ER/GPER 烷基酚受体、main 分支 ROX 生物膜类别富集与 PFHxS 专属结合原型（需先联网核验目标专属结构证据，达不到则标 inspiration/exploratory）。
- 扫描 Qwen / kimi-k3 分支设计，补充机制多样性缺口（如尚缺的机制类别）。
