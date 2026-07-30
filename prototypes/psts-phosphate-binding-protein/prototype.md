---
id: psts-phosphate-binding-protein
name: PstS 磷酸盐结合蛋白（PstS Phosphate-Binding Protein）
category: 微生物
organism: Escherichia coli（PstS 磷酸盐结合蛋白）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 特异性识别
adsorption_mechanisms:
  - 预组织氢键给体阵列对四面体磷酸根的几何识别
  - 四面体磷酸根识别的跨物种保守（原理先例）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 7 verified, 0 unverified
# coverage: partial
# status: active
---
# PstS 磷酸盐结合蛋白（PstS Phosphate-Binding Protein）

## 1. 生物原型简介

**问题定义**：磷（主要以磷酸根形式）是细胞的关键营养，细菌需从含多种化学相似氧阴离子的环境中高特异性捕获磷酸根。蛋白如何在无金属配位前提下选择性识别四面体磷酸根氧阴离子，是分子识别的基础问题。大肠杆菌高亲和磷酸盐主动转运系统（Pst/ABC permease）的初始受体 PstS（PBP）是该问题的经典结构模型。

**生物策略**：大肠杆菌周质 PBP（PstS）以预组织中性氢键给体阵列识别四面体磷酸根：磷酸根埋藏于两结构域间裂隙；磷酸盐结合位点 SITE AC1 由 Ala9、Thr10、Phe11、Gly37、Ser38、Asp56、Arg135、Ser139、Gly140、Asp141 构成（PDB 1PBP，chain A；1PBP 为 T141D 定点突变体，野生型第 141 位为 Thr141）。Thr10/Ser38/Ser139 侧链羟基与骨架酰胺 NH 提供方向性氢键，Asp56 对识别起关键作用（Wang 1994 摘要）。Luecke & Quiocho 1990 以 1.7 Å 野生型结构首次揭示'磷酸盐转运蛋白的高特异性由氢键决定'。同一位点同时识别单碱基（H2PO4⁻）与双碱基（HPO4²⁻）磷酸，而 T141D 突变将结合限制为仅单碱基磷酸，显示给体阵列电荷状态对底物质子化形态的微调。产气荚膜梭菌 PBP-1（PDB 4Q8R）以保守 Ser/Thr 给体阵列（Ser11/Thr12/Ser13/Ser41/Ser59/Ser129）识别磷酸根，表明该几何识别原理在 PBP 家族内保守。

## 2. 吸附机制详解

### 机制1：预组织氢键给体阵列对四面体磷酸根的几何识别

**描述**：大肠杆菌 PstS/PBP 以预组织中性氢键给体阵列（Thr10、Ser38、Ser139 侧链羟基与骨架酰胺 NH，Asp56 起关键定位作用）识别四面体磷酸根 PO4；磷酸根埋藏于两结构域间裂隙，无金属离子直接配位氧阴离子（PDB 1PBP 非水配体仅 PO4）。1PBP 为 T141D 定点突变体，沉积记录第 141 位为工程化 Asp141，野生型该位为 Thr141
**关键官能团**：['氢键给体（Thr/Ser 侧链羟基、骨架酰胺 NH）', '定位天冬氨酸（Asp56）', '埋藏低介电结构域裂隙']
**来源**：DOI 10.1038/347402a0

### 机制2：四面体磷酸根识别的跨物种保守（原理先例）

**描述**：产气荚膜梭菌磷酸盐结合蛋白 PBP-1 以保守 Ser/Thr 氢键给体阵列识别四面体磷酸根（PDB 4Q8R SITE AC1：Ser11、Thr12、Ser13、Ser41、Ser59、Ser129 等），与大肠杆菌 PBP 几何保守，为预组织氢键给体阵列识别四面体氧阴离子在 PstS/PBP 家族内保守提供结构生物学先例
**关键官能团**：['氢键给体（Ser/Thr 侧链羟基、骨架酰胺 NH）']
**来源**：DOI 10.1038/srep06636

## 3. 结构特征与结构-功能关系

必须保留：① 与四面体氧阴离子几何互补的中性氢键给体阵列（Thr/Ser 羟基/骨架 NH）；② 埋藏低介电结构域裂隙（强化静电、排除水竞争）；③ 预组织（结合熵代价预先支付）；④ 给体阵列电荷/质子化状态可调（区分底物质子化形态）。可灵活调整：载体骨架、给体密度与取向、口袋疏水微环境、给体电荷。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: PstS/PBP 为大肠杆菌周质可溶性结合蛋白（约 34.5 kDa），其识别基序需移植/固定于固体载体方可用作吸附 None
- 结构预组织依赖: 结合依赖两结构域间裂隙的预组织三级结构；变性或口袋溶剂化使氢键几何与低介电环境丧失 None
- 四面体氧阴离子几何与给体电荷特异性: 结合位点与四面体磷酸根几何互补，对非四面体或尺寸失配阴离子匹配差；给体阵列电荷状态（如 T141D）切换对磷酸根质子化形态的识别 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding

## 参考文献

[待补充]
