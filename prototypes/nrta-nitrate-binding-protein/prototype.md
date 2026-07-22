---
id: nrta-nitrate-binding-protein
name: NrtA 硝酸盐结合蛋白（NrtA Nitrate-Binding Protein）
category: 微生物
organism: Synechocystis sp. PCC 6803（NrtA 硝酸盐结合蛋白，蓝细菌高亲和硝酸盐 ABC 转运系统底物结合组分）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 特异性识别
adsorption_mechanisms:
  - 预组织被围口袋与 Lys269 阳离子锚对平面硝酸根的几何氢键识别
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 1 papers, 5 verified, 0 unverified
# coverage: partial
# status: active
---
# NrtA 硝酸盐结合蛋白（NrtA Nitrate-Binding Protein）

## 1. 生物原型简介

**问题定义**：硝酸盐是蓝细菌光合作用与生长最关键的氮营养源，在许多水体（尤其开阔海洋）严重受限；蓝细菌须从高背景阴离子中选择性捕获硝酸盐。NrtA 作为高亲和硝酸盐 ABC 转运系统的底物结合组分，是这类细菌质膜上含量最高的蛋白之一。蛋白如何在无金属配位前提下从众多阴离子中选择性识别平面三角形硝酸根，是含氧阴离子营养盐选择性捕获的分子基础问题，与水体硝酸盐选择性去除的工程问题同构。

**生物策略**：Koropatkin 等测定了 Synechocystis sp. PCC 6803 NrtA 与硝酸根复合体的晶体结构（PDB 2G29，1.5 Å）。摘要称其为硝酸盐特异性受体（nitrate-specific receptor），并揭示 NrtA 硝酸盐选择性的决定簇。结构显示硝酸根（配体 NO3，chain A 700，HETNAM 记 NITRATE ION）埋藏于 N 与 C 结构域围成的口袋；PDB SITE AC1 记录围成位点的十残基为 Leu71/Trp102/Leu124/Gln155/Thr190/His196/Pro222/Val239/Gly240/Lys269（chain A），其中带正电的 Lys269 构成阳离子锚，与中性氢键给体共同按几何互补识别平面硝酸根。NrtA 显著大于其他氧阴离子结合蛋白，代表一类此前未表征的转运蛋白；序列上同类唯一的另一成员是碳酸氢根结合蛋白 CmpA。需要诚实标注：现有实验结构仅硝酸根结合态，去配体后的构象闭合仅来自去配体分子动力学推断，无实验性 apo 结构支撑。

## 2. 吸附机制详解

### 机制1：预组织被围口袋与 Lys269 阳离子锚对平面硝酸根的几何氢键识别

**描述**：蓝细菌 Synechocystis sp. PCC 6803 的 NrtA 是高亲和硝酸盐 ABC 转运系统的周质底物结合蛋白，天然配体即硝酸根。PDB 2G29（1.5 Å，硝酸根结合态）显示硝酸根（配体 NO3，chain A 700）埋藏于由 N 与 C 结构域围成的口袋中；PDB SITE AC1 记录围成结合位点的十个残基为 Leu71、Trp102、Leu124、Gln155、Thr190、His196、Pro222、Val239、Gly240、Lys269（chain A），其中带正电的 Lys269 构成对平面硝酸根的阳离子锚，与中性氢键给体共同按几何互补识别平面三角形硝酸根
**关键官能团**：['阳离子锚（Lys269 侧链铵基）', '中性氢键给体（Gln155、Thr190、His196 等侧链与骨架）', '被围低介电口袋']
**来源**：DOI 10.1073/pnas.0602517103

## 3. 结构特征与结构-功能关系

必须保留：① 与平面三角形硝酸根几何/静电互补的阳离子锚（Lys269 型铵基/胍基）；② 预组织中性氢键给体阵列（Gln/Thr/His 型，方向性固定三氧取向）；③ 被围低介电口袋（强化静电、排除水竞争）。可灵活调整：载体骨架、阳离子锚与给体的间距取向、口袋疏水微环境。不可直接搬用：蛋白的构象动态（无实验 apo 证据，仅静态识别几何可迁移）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: NrtA 为蓝细菌周质可溶底物结合蛋白（约 46 kDa），其识别口袋依赖完整三级结构，用作吸附须将识别基序移植/固定于固体载体 None
- 仅结合态结构已知: 实验结构仅硝酸根结合态（holo，PDB 2G29）；无实验性 apo 结构，配体诱导的构象闭合/结构域运动未经实验测定，转译限静态识别几何层级 None
- 硝酸盐几何/静电特异性与共存阴离子竞争: 被围口袋与阳离子锚按平面三角形硝酸根互补；对几何/电荷相近的平面氧阴离子（碳酸氢根/碳酸根）及高背景阴离子（氯离子、硫酸根）的分辨须在选择性设计上额外约束 None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- cell-membrane-ion-channel
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation

## 参考文献

[待补充]
