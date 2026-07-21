---
id: fabp4-fatty-acid-pfas-binding
name: FABP4 脂肪酸/PFAS 结合蛋白（FABP4 Fatty Acid / PFAS Binding Protein）
category: 动物
organism: Homo sapiens（人源 FABP4，脂肪细胞型脂肪酸结合蛋白）
biomimetic_dimension: 分子仿生
features:
  - 疏水性
  - 分子筛分
pollutants:
  - PFOA（全氟辛酸）
  - PFTeDA/PFTrDA/PFDoA（C12-C14 全氟羧酸）
adsorption_mechanisms:
  - 埋藏疏水腔与羧酸根极性锚对全氟辛酸的双位点结合
  - 全氟羧酸结合的链长单调依赖与腔体几何容纳
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: high
# provenance: 1 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# FABP4 脂肪酸/PFAS 结合蛋白（FABP4 Fatty Acid / PFAS Binding Protein）

## 1. 生物原型简介

**问题定义**：PFAS 在环境与人畜体内广泛检出并沿食物链蓄积，其与脂质转运/结合蛋白的相互作用是理解生物蓄积、转运与毒性的分子基础，但分子层面认识不足。FABP4（脂肪细胞型脂肪酸结合蛋白）的天然底物为长链脂肪酸，作为胞内脂质载体参与代谢与内分泌调控；PFAS 与 FABP4 的结合属有文献记载的外源污染物-蛋白相互作用（毒理/内分泌语境），而非 FABP4 的天然功能。

**生物策略**：人源 FABP4 以β桶围成的内部埋藏疏水腔结合两亲性阴离子。Birchfield 等测定了 FABP4 与 PFOA（PDB 9MIW）、PFDA、PFHxDA 的晶体结构并结合 ANS 竞争置换荧光实验：PFOA 在腔内占据两个分离位点（配体 8PF 位于链 A 201/202 位）；主位点羧酸根由 Arg126 与 Tyr128 氢键稳定、并有 Arg106 水介导氢键，Ala75/Thr29/Ala33/Phe16 经烃基侧链提供疏水接触；次位点羧酸根与 Thr29 氢键。PFOA/PFDA 诱导 Phe57 由 apo 闭合转为开放构象以扩大疏水腔。结合呈链长单调依赖（C12-C14 PFCA 的 Kd 低于 1 μM，短链显著更弱但仍强于非氟化类似物），且头基化学起关键作用（羧酸根头基结合紧于磺酸/磺酰胺头基）。

## 2. 吸附机制详解

### 机制1：埋藏疏水腔与羧酸根极性锚对全氟辛酸的双位点结合

**描述**：人源 FABP4 以β桶围成的埋藏疏水腔结合 PFOA；PFOA 在腔内占据主、次两个分离位点：主位点羧酸根由 Arg126 与 Tyr128 氢键（并有 Arg106 水介导氢键）锚定，Ala75、Thr29、Ala33、Phe16 经烃基侧链提供疏水接触；次位点羧酸根与 Thr29 氢键。配体结合诱导 Phe57 由 apo 闭合转为开放构象以扩大疏水腔
**关键官能团**：['阳离子/氢键给体（Arg126、Tyr128、Arg106、Thr29 侧链）', '疏水腔壁残基（Ala75、Thr29、Ala33、Phe16、Phe57）', 'β桶骨架']
**来源**：DOI 10.1021/jacsau.5c00504

### 机制2：全氟羧酸结合的链长单调依赖与腔体几何容纳

**描述**：全氟羧酸（PFCA）与 FABP4 的亲和力随全氟碳链链长单调增加：长链 PFTeDA/PFTrDA/PFDoA（C12-C14）的解离常数低于 1 μM，短链 PFCA 显著更弱但仍可测且强于非氟化类似物；长链在腔内需弯折容纳。结合增强源于更大疏水表面积与范德华接触，与血清白蛋白及肝型 FABP 的既有报道一致
**关键官能团**：['疏水腔（范德华/氟亲接触面）']
**来源**：DOI 10.1021/jacsau.5c00504

## 3. 结构特征与结构-功能关系

必须保留：① β桶围成的埋藏疏水腔（容纳全氟碳链，范德华/氟亲接触）；② 与羧酸根头基互补的预组织极性锚（Arg/Tyr 型阳离子与氢键给体）；③ 与目标链长匹配的腔体几何（长链需弯折容纳，Phe57 开放构象扩容）。可灵活调整：载体骨架、锚定基团化学（胍基/脒基/脲/硫脲）、孔壁疏水/氟亲修饰程度、腔深与孔径。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| PFOA（全氟辛酸） | 重组人源 FABP4（可溶蛋白） | 低微摩尔级（low micromolar | - | literature: 10.1021/jacsau.5c0 | ✅ |
| PFTeDA/PFTrDA/P | 重组人源 FABP4（可溶蛋白） | <1 (PFTeDA/PFTrDA/PF | - | literature: 10.1021/jacsau.5c0 | ✅ |

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: FABP4 为胞内可溶性蛋白（约 15 kDa），识别依赖完整β桶三级结构，用作吸附须固定化/移植于固体载体 None
- Phe57 构象门控: 配体结合需 Phe57 呈开放构象以扩大疏水腔；apo 态 Phe57 为闭合构象，固定化或变性若锁闭腔口将丧失结合 None
- 链长单调亲和（非特异选择性）: PFCA 亲和力随链长单调增加（长链更强），FABP4 对 PFOA 无相对更长链 PFCA 的特异选择性；头基偏好为羧酸根紧于磺酸根 None

## 6. 相关原型

- cactus-spine
- cell-membrane-ion-channel
- diatom-frustule
- lotus-leaf
- moda-oxyanion-geometric-recognition

## 参考文献

[1] DOI: 10.1021/jacsau.5c00504
