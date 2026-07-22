---
id: hl-fabp-liver-fatty-acid-pfas-binding
name: hL-FABP 肝脂肪酸/PFAS 结合蛋白（hL-FABP (FABP1) Liver Fatty Acid / PFAS Binding Protein）
category: 动物
organism: Homo sapiens（人肝脂肪酸结合蛋白 FABP1 / L-FABP，具异常大结合腔、可同时容纳两个配体）
biomimetic_dimension: 分子仿生
features:
  - 疏水性
  - 分子筛分
adsorption_mechanisms:
  - 羧酸头基定点识别 + 有限低极性链段容纳对长链全氟羧酸的结合
  - portal/gap 区骨架动态（动态对应边界，勿过度主张）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 3 verified, 0 unverified
# coverage: partial
# status: active
---
# hL-FABP 肝脂肪酸/PFAS 结合蛋白（hL-FABP (FABP1) Liver Fatty Acid / PFAS Binding Protein）

## 1. 生物原型简介

**问题定义**：长链全氟羧酸（PFOA/PFNA）在水与生物体内广泛存在，如何在阴离子头基相似、仅链长/骨架不同的干扰下选择性识别长链全氟羧酸，是分子识别的难题。

**生物策略**：人肝脂肪酸结合蛋白（hL-FABP/FABP1）以大疏水腔容纳全氟碳链，并以极性残基（Asn111、Arg122 等）作用于阴离子羧酸头基，实现链长依赖的结合（Sheng 2016，荧光置换/ITC/突变/模拟）；其溶液结构与 portal 骨架动力学见 Cai 2012（PDB 2LKK），多种全氟化合物的结构基础相互作用见 Zhang 2013。

## 2. 吸附机制详解

### 机制1：羧酸头基定点识别 + 有限低极性链段容纳对长链全氟羧酸的结合

**描述**：人肝 FABP 以大疏水腔容纳长链全氟羧酸（PFOA/PFNA）的全氟碳链，并以极性残基（Asn111、Arg122 等）与羧酸头基作用；结合呈链长依赖，短链亲和显著弱于长链。
**关键官能团**：['极性头基锚定残基（Asn/Arg 类）', '疏水大腔（容纳低极性链段）']
**来源**：DOI 10.1007/s00204-014-1391-7

### 机制2：portal/gap 区骨架动态（动态对应边界，勿过度主张）

**描述**：hL-FABP 的 portal/gap 区存在骨架运动（Cai 2012，PDB 2LKK）；但 NMR 研究指出其本征慢（毫秒）动力学不太可能是配体进入所需的关键构象重排（Long & Yang），故不作'目标诱导门控'的动态硬对应主张。
**关键官能团**：['portal/gap 柔性区（动态边界，非承重）']
**来源**：DOI 10.1016/j.bpj.2012.04.039

## 3. 结构特征与结构-功能关系

必须保留：① 对阴离子羧酸头基的定向极性锚定；② 对有限长度低极性链段的疏水容纳（链长选择）。可灵活调整：载体骨架、锚定基团化学与密度。勿保留：蛋白双配体大腔的非选择性、portal 动态（无目标诱导门控证据）。

## 4. 已报道性能数据

[待补充]（hL-FABP 为分子识别蛋白原型，本库无其吸附剂性能数据；蛋白-配体亲和力非吸附剂性能）

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态：约 14 kDa 胞内可溶结合蛋白，识别基序需以非蛋白方式抽象/移植于固体载体
- 双配体大腔：结合腔异常大、可同时容纳两个配体，直接照搬腔体几何不利于单一 PFOA 高选择性
- 体内归因禁区：FABP 敲除不改变 PFOS 体内组织分布（Modaresi 2025），仅用于体外几何/化学识别原则

## 6. 相关原型

- fabp4-fatty-acid-pfas-binding
- hsa-fatty-acid-pfas-binding
- lipocalin-hydrophobic-calyx

## 参考文献

- Sheng 等，Interaction of perfluoroalkyl acids with human liver fatty acid-binding protein，Arch Toxicol 2016，DOI 10.1007/s00204-014-1391-7
- Cai 等，Solution Structure and Backbone Dynamics of Human Liver Fatty Acid Binding Protein，Biophys J 2012，DOI 10.1016/j.bpj.2012.04.039（PDB 2LKK）
- Zhang, Ren, Guo，Structure-Based Investigation on the Interaction of Perfluorinated Compounds with hL-FABP，ES&T 2013，DOI 10.1021/es4026722
- Cheng & Ng（氟代亲和归疏水/体积），Protein Sci 2021，DOI 10.1002/pro.4036
- Modaresi 等（FABP 敲除不改变 PFOS 体内分布），Chem Res Toxicol 2025，DOI 10.1021/acs.chemrestox.5c00199

> 诚实边界：机制接地为摘要级核验，未做本地全文 PDF 审计；非蛋白材料转译为 inspiration/llm_inferred；此为广度优先入库条目，待后续审计补全文与残基级定位后可升 tier。
