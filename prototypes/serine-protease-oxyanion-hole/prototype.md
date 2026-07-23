---
id: serine-protease-oxyanion-hole
name: 丝氨酸/半胱氨酸蛋白酶氧阴离子穴（预组织双氢键阵列）（Serine/Cysteine Protease Oxyanion Hole (Preorganized Dual Hydrogen-Bond Array)）
category: 动物
organism: Bos taurus（γ-胰凝乳蛋白酶，PDB 1GCT）/ Bacillus amyloliquefaciens（枯草蛋白酶 BPN′，PDB 1SBT）/ Carica papaya（木瓜蛋白酶，PDB 1PAD）；跨物种趋同的氧阴离子穴基序
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
adsorption_mechanisms:
  - 丝氨酸蛋白酶氧阴离子穴：预组织双骨架酰胺 NH 氢键阵列稳定四面体过渡态氧阴离子
  - 半胱氨酸蛋白酶氧阴离子穴：双骨架酰胺氢键阵列稳定过渡态负电荷（趋同原理）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 丝氨酸/半胱氨酸蛋白酶氧阴离子穴（预组织双氢键阵列）（Serine/Cysteine Protease Oxyanion Hole (Preorganized Dual Hydrogen-Bond Array)）

## 1. 生物原型简介

**问题定义**：蛋白酶须在温和条件下高效水解肽键，而肽键本身动力学稳定。如何选择性稳定肽键水解的高能四面体过渡态，是酶催化的核心问题。丝氨酸蛋白酶（胰凝乳蛋白酶、枯草蛋白酶）与半胱氨酸蛋白酶（木瓜蛋白酶）在进化中各自独立形成了氧阴离子穴这一结构方案。

**生物策略**：氧阴离子穴由两个预组织骨架酰胺 NH 供体构成：丝氨酸蛋白酶为 chymotrypsinogen 编号 Gly193 与 Ser195 的主链 NH（DOI 10.3390/molecules31091454 全文逐字记 '...the carbonyl oxygen ... formed hydrogen bonds with the backbone NH groups of Gly193 and Ser195 in the oxyanion hole'），半胱氨酸蛋白酶为 Gly172 与 Cys213 主链 NH（DOI 10.1038/s41467-026-72367-y 记氧阴离子穴 'formed by the backbone amides of Gly172 and Cys213' 且 'essential for stabilizing the negative charge developed during the transition state'）。两个供体以固定间距与取向对四面体过渡态羰基氧形成方向性氢键，选择性稳定带负电的过渡态而非平面基态。γ-胰凝乳蛋白酶酰基-酶加合物（PDB 1GCT，1.6 Å）、枯草蛋白酶 BPN′（PDB 1SBT）与木瓜蛋白酶氯甲基酮底物类似物复合物（PDB 1PAD）提供结构参照；该基序在 chymotrypsin 与 subtilisin 两个不同折叠中趋同保守。

## 2. 吸附机制详解

### 机制1：丝氨酸蛋白酶氧阴离子穴：预组织双骨架酰胺 NH 氢键阵列稳定四面体过渡态氧阴离子

**描述**：丝氨酸蛋白酶（γ-胰凝乳蛋白酶 PDB 1GCT、枯草蛋白酶 BPN′ PDB 1SBT）在进化中形成氧阴离子穴，由两个预组织骨架酰胺 NH 供体（chymotrypsinogen 编号 Gly193 与 Ser195 主链 NH）以固定间距与取向排布，对肽键水解四面体过渡态发展的氧阴离子（底物羰基氧获得的负电荷）形成两个定向氢键，选择性稳定该高能过渡态；该基序在不同折叠的丝氨酸蛋白酶（chymotrypsin 与 subtilisin）中趋同保守
**关键官能团**：['骨架酰胺 NH 氢键供体（Gly193、Ser195 主链 NH，chymotrypsinogen 编号）', '预组织活性位点氧阴离子穴']
**来源**：DOI 10.1074/jbc.M503499200

### 机制2：半胱氨酸蛋白酶氧阴离子穴：双骨架酰胺氢键阵列稳定过渡态负电荷（趋同原理）

**描述**：半胱氨酸蛋白酶（木瓜蛋白酶 PDB 1PAD；天冬酰胺肽连接酶 C13 折叠）以两个预组织骨架酰胺供体（Gly172 与 Cys213 主链 NH）构成氧阴离子穴，稳定过渡态发展的负电荷；与丝氨酸蛋白酶氧阴离子穴为趋同原理，表明预组织双骨架酰胺 NH 氢键阵列是稳定四面体过渡态氧阴离子的通用结构方案
**关键官能团**：['骨架酰胺 NH 氢键供体（Gly172、Cys213 主链 NH）', '预组织氧阴离子穴']
**来源**：DOI 10.1038/s41467-026-72367-y

## 3. 结构特征与结构-功能关系

必须保留：① 两个（或多个）中性氢键供体（骨架酰胺 NH 或其合成等价物脲/硫脲）；② 供体以固定间距与取向预组织，与目标氧阴离子几何/方向互补；③ 埋藏或低介电微环境以降低水竞争。可灵活调整：供体化学（脲/硫脲/酰胺）、载体骨架（活性炭/聚合物/介孔二氧化硅）、孔壁疏水性。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 催化蛋白形态与变性约束: 氧阴离子穴依赖蛋白酶三级结构的预组织（chymotrypsin/subtilisin/papain 均为约 23–27 kDa 球状蛋白）；游离蛋白在水相易变性，氢键几何与活性位点预组织丧失 None
- 供体几何预组织依赖: 识别要求两个氢键供体维持固定间距与取向；柔性或溶剂化使方向性氢键与几何互补丧失 None
- 水相氢键竞争: 水分子与目标氧阴离子竞争供体氢键；天然氧阴离子穴位于埋藏活性位点以降低水竞争，转译至开放孔壁需以低介电/疏水微环境或刚性预组织补偿 None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[待补充]
