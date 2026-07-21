---
id: moda-oxyanion-geometric-recognition
name: ModA 氧阴离子几何识别蛋白（ModA Oxyanion Geometric Recognition Protein）
category: 微生物
organism: Escherichia coli / Azotobacter vinelandii（ModA 钼酸根结合蛋白）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
adsorption_mechanisms:
  - 预组织氢键阵列对四面体钼酸根的几何识别
  - 四面体硫酸根的纯氢键结合（原理先例）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 7 verified, 0 unverified
# coverage: partial
# status: active
---
# ModA 氧阴离子几何识别蛋白（ModA Oxyanion Geometric Recognition Protein）

## 1. 生物原型简介

**问题定义**：钼是生物必需微量元素，细菌需从含高浓度硫酸根等化学相似氧阴离子的环境中特异性捕获微摩尔乃至更低浓度的钼酸根（MoO4²⁻）。蛋白如何在无金属配位的前提下选择性识别四面体氧阴离子，是分子识别的基础问题。

**生物策略**：大肠杆菌周质 ModA 蛋白以预组织中性氢键给体阵列识别四面体钼酸根：钼酸根埋藏于 N 与 C 结构域间的低介电裂隙（PDB 1AMF，COMPND 记 'MOLYBDATE ANION IS SEQUESTERED BETWEEN N-AND C-DOMAINS'）；MoO4²⁻ 四氧与 Ser12、Ser39、Tyr170 侧链羟基（H···O 1.85–1.89 Å）及 Val152、Ala125 骨架酰胺 NH（N···O 2.89–3.06 Å）形成氢键（PDB SITE 记录残基 SER 12/SER 39/ALA 125/VAL 152/TYR 170），无任何金属离子或阳离子参与。同一位点以保守几何结合钨酸根（PDB 1WOD），显示对四面体氧阴离子的几何选择性。硫酸根结合蛋白（Pflugrath & Quiocho 1985）证明四面体硫酸根可'仅由氢键结合'，为同类原理的先例。

## 2. 吸附机制详解

### 机制1：预组织氢键阵列对四面体钼酸根的几何识别

**描述**：ModA 以预组织中性氢键给体阵列识别四面体钼酸根 MoO4²⁻（Ser12、Ser39、Tyr170 侧链羟基 + Val152、Ala125 骨架酰胺 NH）；钼酸根埋藏于 N 与 C 结构域间的低介电裂隙，无金属离子或阳离子参与配位
**关键官能团**：['氢键给体（Ser/Thr/Tyr 侧链羟基、骨架酰胺 NH）', '埋藏低介电口袋']
**来源**：DOI 10.1038/nsb0997-703

### 机制2：四面体硫酸根的纯氢键结合（原理先例）

**描述**：鼠伤寒沙门氏菌硫酸根结合蛋白以纯氢键结合四面体硫酸根 SO4²⁻，无金属离子或阳离子参与，提供四面体氧阴离子几何可被预组织中性给体阵列识别的结构生物学先例
**关键官能团**：['氢键给体（骨架酰胺 NH、侧链羟基）']
**来源**：DOI 10.1038/314257a0

## 3. 结构特征与结构-功能关系

必须保留：① 与四面体氧阴离子几何互补的中性氢键给体阵列（羟基/骨架 NH）；② 埋藏低介电口袋（强化静电、排除水竞争）；③ 预组织（结合熵代价预先支付）。可灵活调整：载体骨架、给体密度与取向、口袋疏水微环境。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: ModA 为大肠杆菌周质可溶性结合蛋白（约 25 kDa），其识别基序需移植/固定于固体载体方可用作吸附 None
- 结构预组织依赖: 结合依赖 N 与 C 结构域间三级结构的预组织；变性或口袋溶剂化使氢键几何与低介电环境丧失 None
- 四面体氧阴离子几何特异性: 结合位点与四面体氧阴离子（钼酸根/钨酸根）几何互补，对非四面体或尺寸失配阴离子匹配差 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule

## 参考文献

[待补充]
