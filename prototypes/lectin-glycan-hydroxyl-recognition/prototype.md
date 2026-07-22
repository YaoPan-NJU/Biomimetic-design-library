---
id: lectin-glycan-hydroxyl-recognition
name: 凝集素糖链羟基模式识别蛋白（刀豆球蛋白 A）（Lectin Glycan Hydroxyl-Pattern Recognition Protein (Concanavalin A)）
category: 植物
organism: Canavalia ensiformis（刀豆 凝集素 Concanavalin A / ConA）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
adsorption_mechanisms:
  - 多点氢键阵列对糖链表面羟基模式的识别
  - Mn/Ca 金属辅因子对糖识别环的结构预组织
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 凝集素糖链羟基模式识别蛋白（刀豆球蛋白 A）（Lectin Glycan Hydroxyl-Pattern Recognition Protein (Concanavalin A)）

## 1. 生物原型简介

**问题定义**：糖类识别要求蛋白在一组化学结构高度相似的糖之间区分特定单糖。甘露糖与半乳糖仅 C2 羟基轴向/平伏取向不同，凝集素却须忠实识别其靶标单糖，以介导细胞黏附、种子贮藏蛋白分选与免疫识别等过程。如何以单一蛋白结构域经由对糖链表面羟基模式的多点读取区分单糖立体化学，是分子识别的基础问题。

**生物策略**：刀豆（Canavalia ensiformis）凝集素 ConA 为约 26 kDa 单体的同源四聚体，每个单体携带一个单糖结合位点，以读取糖链表面羟基的空间模式识别甘露糖型单糖。Naismith 等解析了 ConA 与甲基 α-D-甘露吡喃糖苷的 2.0 Å 晶体复合物（PDB 5CNA）：甘露糖四个羟基与预组织残基核心形成方向性氢键网络，坐标直测为 Asp208 OD2→O4（2.63 Å）、Asp208 OD1→O6（2.88 Å）、Arg228 骨架 NH→O3（2.88 Å）、Asn14 ND2→O4（2.99 Å）；摘要陈述'每个糖分子以氢键加范德华接触被蛋白结合'，且结合伴随有序水分子排出与 Tyr100 侧链取向重排。该结合依赖两个紧邻金属辅因子（Mn²⁺ 与 Ca²⁺，相距 4.22 Å）：Ca²⁺ 由 Tyr12 骨架羰基、Asn14、Asp19、Asp10 配位，Mn²⁺ 由 Glu8、Asp10、Asp19、His24 配位；桥联残基 Asn14 以 OD1 配位 Ca²⁺（2.47 Å）、同时以 ND2 氢键结合糖 O4（2.99 Å），把金属位点与糖识别位点直接耦合。Loris 1998 综述概括 legume 凝集素以'氢键合于糖的保守残基核心'加决定结合位点形状的可变环实现单糖特异性；Kaushik 2009 分子动力学显示去金属化使离子结合环产生大构象变化并废除糖结合，表明金属预组织识别环。

## 2. 吸附机制详解

### 机制1：多点氢键阵列对糖链表面羟基模式的识别

**描述**：刀豆球蛋白 A（ConA）以预组织的残基核心识别甘露糖型单糖表面的羟基空间模式：PDB 5CNA（2.0 Å，链 A）坐标直测，甲基 α-D-甘露吡喃糖苷（配体 MMA）的四个羟基与结合位点形成方向性氢键网络，Asp208 OD2→O4（2.63 Å）、Asp208 OD1→O6（2.88 Å）、Arg228 骨架酰胺 NH→O3（2.88 Å）、Asn14 ND2→O4（2.99 Å），另有 Leu99、Tyr100 骨架 NH 近 O6；同一结合位点以保守几何读取甘露糖的 O3/O4 顺式二醇与 O6 羟基
**关键官能团**：['氢键供体/受体（Asp208、Arg228、Asn14 侧链，Leu99/Tyr100 骨架酰胺 NH）', '预组织结合位点（保守核心加可变环）']
**来源**：DOI 10.1107/s0907444994005287

### 机制2：Mn/Ca 金属辅因子对糖识别环的结构预组织

**描述**：ConA 糖结合能力依赖两个紧邻金属辅因子（Mn²⁺ 与 Ca²⁺，相距 4.22 Å）；PDB 5CNA（链 A）坐标直测，Ca²⁺ 由 Tyr12 骨架羰基（2.27 Å）、Asn14 OD1（2.47 Å）、Asp19 OD2（2.34 Å）、Asp10 OD1（2.44 Å）配位，Mn²⁺ 由 Glu8 OE2（2.30 Å）、Asp10 OD2（1.97 Å）、Asp19 OD1（2.15 Å）、His24 NE2（2.51 Å）配位。桥联残基 Asn14 以 OD1 配位 Ca²⁺、同时以 ND2 氢键结合糖 O4，将金属位点与糖识别位点直接耦合
**关键官能团**：['金属配位残基（Glu8、Asp10、Asp19、His24 配位 Mn²⁺；Tyr12 骨架羰基、Asn14、Asp19、Asp10 配位 Ca²⁺）', '桥联残基（Asn14：OD1 配位 Ca²⁺，ND2 氢键结合糖）']
**来源**：DOI 10.1529/biophysj.108.134601

## 3. 结构特征与结构-功能关系

必须保留：① 与目标羟基模式几何互补的多点氢键供体/受体阵列（Asp/Arg/Asn 型残基，方向性氢键）；② 金属配位预组织（两个紧邻金属离子固定识别环构象，桥联残基 Asn14 同时配位金属与氢键结合目标）；③ 保守核心加可变环界定的结合位点形状（位点几何特异性）。可灵活调整：载体骨架、氢键供体/受体化学、金属配位骨架或刚性间隔臂、腔体尺寸与疏水微环境。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: ConA 为刀豆种子可溶性四聚体凝集素（RCSB 5CNA 条目分子质量 103.68 kDa，即约 26 kDa 单体组成的同源四聚体），其识别基序需移植/固定于固体载体方可用作吸附 None
- 金属辅因子依赖: 糖结合依赖两个紧邻金属位点（Mn²⁺/Ca²⁺）的完整性；去金属化使离子结合环构象紊乱并丧失糖结合能力 None
- 羟基模式几何特异性: 结合位点形状（保守核心加可变环）与甘露糖 O3/O4/O6 羟基模式几何互补，对羟基取向不同的单糖（如半乳糖）匹配差；ConA 本身提供单糖立体化学特异性，而非对某一非天然靶标的特异选择性 None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[待补充]
