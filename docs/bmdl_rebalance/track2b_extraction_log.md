# Track 2B — 源项目设计抽取扩库日志（第一批）

**日期：** 2026-07-29 ｜ **分支：** `massive` ｜ **来源：** `biomimetic-adsorbent-design`（本地 checkout，Ultimate 分支 + main 分支 git show）

## 方法与红线
- 从源项目设计（`DEEP_RESEARCH_BIOMIMETIC_SCHEME_PORTFOLIO.md` 十套方案 + main 分支 ROX/PFHxS 深研文档）抽取**生物原型/机制**，而非搬运材料方案或性能数值。
- **知识隔离红线**：`performance_data` 一律留空，未从源项目搬运任何吸附容量数值；机制经**联网核验的原始文献**独立接地。
- 新原型只声明 `mechanism_tags` 即经机制层自动可达（Track 2A 能力）；对其关键目标污染物另做 pollutant_prototype_map 直接接线以保证 top-N 浮现。

## 抽取盘点（口径：跨全部分支、只看原型、不论方案成败）
跨 Ultimate + main + Qwen + kimi-k3 分支，逐设计只提取生物原型/机制，好的入库、不完整的补全+对抗，与方案是否"通过"无关。
- **已在库（V1-B 已吸收）**：hL-FABP、HSA、ERRγ、核糖体出口隧道、TTR、氯酚羟化酶 → 无需重复。
- **本批抽取（库中缺口）**：β-环糊精主客体包合(Ultimate S2)、SERT 芳香胺识别(model_only A5)、成熟污水生物膜大环内酯类别富集(main ROX)。
- **不作为独立原型**：PFHxS "PFH-1"（源项目自述为工程离子交换珠、非仿生原型，方向性已由 NTCP/ASBT/OATP 转运体覆盖）；大环内酯@阴离子磷脂界面（与 pulmonary-surfactant 重叠，已并入 biofilm 界面机制）。
- **batch_b 已挖（入库）**：SMX→DHPS、As(III)→ArsR；nitrate→NrtA、phosphate→PstS/PBP-1、BPA→ERRγ 均已在库。
- **Qwen/kimi-k3**：Qwen ROX 用 FcRn（已在库）、PFBS 用 β-CD（已入）；kimi-k3 无独立设计文档。→ **源项目 4 分支设计原型已基本挖尽**。
- **剩余（证据弱/近重复，暂不入）**：ER/GPER 烷基酚受体、BSA（与 HSA 近重复）。

## 本批入库（3 个，来自 3 个不同来源）
### beta-cyclodextrin-host-guest-inclusion（β-环糊精天然环状腔体主客体包合，Ultimate S2）
- **生物身份**：细菌 CGTase 由淀粉环化生成的天然环状低聚糖（Bacillus sp.），非通用合成材料，过生物身份门槛。
- **机制**：① 锥台形天然疏水环腔对疏水/全氟链段主客体包合（from_source，Alsbaiee 2016 Nature 529:190，DOI 10.1038/nature19764，题录/页码接地）；② 环缘羟基 + 阳离子交联点对阴离子头基静电/氢键协同（literature_backed，Wang 2022 ACS Cent Sci，DOI 10.1021/acscentsci.2c00478，题录级）。
- **诚实分层**：Nature 页码接地要素标 from_source（2 条 causal 要素 compliant）；Wang 仅题录级→literature_backed；转译标 lead/inspiration；无搬运容量数值。
- **mechanism_tags**：疏水分配 / 孔道限域分子筛分 / 几何识别 / 氢键 / 静电吸附。
- **接线**：PFOA/PFOS/PFBS/BPA/Nonylphenol/MB（exploratory–lead）；导出含 β-CD 4 行。

### sert-serotonin-transporter-aromatic-amine-recognition（血清素转运体 SERT 芳香胺识别，model_only A5）
- **生物身份**：人 SERT（SLC6A4，动物）。**机制**：① 中央位点(TM1/3/6/8/10)对芳香胺配体识别（**from_source**，Coleman 2016 *Nature* 532:334，DOI 10.1038/nature17629，PDB 5I6X）；② Na⁺/Cl⁻ 耦合交替开放门控（from_source）。
- **诚实分层**：SERT 结构/机制 from_source；对 ODV/文拉法辛的识别为 inspiration（专属结合未核验）；无搬运数值。
- **mechanism_tags**：几何识别/π-π堆积/静电吸附/氢键/疏水分配。接线 Venlafaxine/ODV；经机制层对芳香污染物浮现（导出 0.48）。

### wastewater-biofilm-macrolide-class-enrichment（成熟污水生物膜大环内酯类别富集，main ROX；系统仿生）
- **生物身份**：混合微生物群落（成熟失活污水生物膜/MBBR，微生物）。**机制**：成熟生物膜对克拉霉素/红霉素/罗红霉素的类别级分配富集（**literature_backed**，Torresi 2017 *Water Res* PMID 28686941 + Burzio 2024，题录级）。
- **诚实分层**：类别富集为事实层；界面成因(EPS/磷脂)与浅层结构可制造性为 inspiration/假说；无搬运分配系数。
- **mechanism_tags**：静电吸附/疏水分配/孔道限域分子筛分。接线 Roxithromycin/CLA/ERY；对 Roxithromycin 查询浮现（exploratory）。

### dhps-dihydropteroate-synthase-paba-recognition（二氢蝶酸合酶 DHPS PABA/磺胺识别，model_only/bmdl_assisted batch_b）
- **生物身份**：细菌 DHPS（叶酸合成酶，微生物）。**机制**：pABA 口袋对磺胺骨架的竞争性识别（**literature_backed**，Hevener 2010 J Med Chem DOI 10.1021/jm900861d + Babaoglu 2004 Structure，PDB 3H26；磺胺=pABA 类似物）。
- **mechanism_tags**：几何识别/氢键/π-π堆积/静电吸附。接线 SMX；对 SMX 查询浮现（exploratory）。

### arsr-arsenic-trithiol-disorder-to-order（ArsR 砂感应三硫醇 AsS3 捕获，model_only/bmdl_assisted batch_b）
- **生物身份**：细菌 ArsR/SmtB 家族 As(III) 感应蠕压蛋白（微生物）。**机制**：3 个半胱氨酸对 As(III) 三配位(AsS3)+As(III) 诱导无序到有序（**literature_backed**，Shi 1996 JBC 271:9291 + Prabaharan 2019 + Zhu 2023 JACS DOI 10.1021/jacs.3c11665）。
- **mechanism_tags**：配位蟎合/几何识别。接线 As(III)；已入库可达，但处于 As(III) 饱和 top-10 之下（排序局限，见下）。

## 排序局限（建议后续修复）
多个优质新原型（β-CD 对 PFOA、ArsR 对 As(III)）因旗舰污染物 top-10 饱和、且 query 合并后未按权重排序即截断而不浮现。建议：在 query 合并 candidates 后、取 top-N 前按 weight 降序排序（小改动、高价值），使新原型能按权重浮现。

## 验证
- 库规模 89 → **94** 原型（Track2B 累计 +5：β-CD、SERT、biofilm、DHPS、ArsR）；DHPS 对 SMX、biofilm 对 Roxithromycin、β-CD 对 BPA/PFOS/Nonylphenol、SERT 经机制层均浮现（lane 多为 exploratory）；ArsR 已入库可达但在 As(III) 饱和 top-10 之下。
- validate_consistency 0 error；from_source_integrity 0 non-compliant；causal_chain 全合格；source_authenticity 无硬错误；check_chimera 10（预存，5 个新原型均单物种/单群落未新增）。
- 导出 390 行 / 44 污染物，含 5 个新原型。

## 下一批建议
- ER/GPER 烷基酚受体、main 分支 ROX 生物膜类别富集与 PFHxS 专属结合原型（需先联网核验目标专属结构证据，达不到则标 inspiration/exploratory）。
- 扫描 Qwen / kimi-k3 分支设计，补充机制多样性缺口（如尚缺的机制类别）。
