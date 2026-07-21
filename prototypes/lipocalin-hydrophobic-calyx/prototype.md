---
id: lipocalin-hydrophobic-calyx
name: 脂质运载蛋白疏水腔 calyx（含 SCP-2 固醇载体蛋白-2）（Lipocalin Hydrophobic Calyx (incl. SCP-2 Sterol Carrier Protein-2)）
category: 动物
organism: Mus musculus（鼠主尿蛋白 MUP） / Aedes aegypti（埃及伊蚊 SCP-2 固醇载体蛋白-2）
biomimetic_dimension: 分子仿生
features:
  - 疏水性
  - 分子筛分
adsorption_mechanisms:
  - 鼠主尿蛋白 MUP-I 疏水 calyx 对信息素小疏水分子的包结
  - SCP-2 大疏水腔对固醇与脂肪酸的结合与转运
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 脂质运载蛋白疏水腔 calyx（含 SCP-2 固醇载体蛋白-2）（Lipocalin Hydrophobic Calyx (incl. SCP-2 Sterol Carrier Protein-2)）

## 1. 生物原型简介

**问题定义**：啮齿类尿液蛋白长期被认为负责信息素的结合与缓释，但分子层面的结合机制不明。雄性大鼠尿 alpha2u-球蛋白还参与透明液滴肾病（一种由多种工业化学品暴露引发的毒理综合征），提示这类蛋白的结合腔可容纳外源疏水小分子。脂运载蛋白如何以统一的结构基序识别一系列小疏水分子，是分子识别的基础问题。

**生物策略**：Böcskei 等测定了鼠主尿蛋白（2.4 Å，PDB 1MUP）与大鼠 alpha2u-球蛋白（2.8 Å）的晶体结构，结果确证其在信息素转运中的角色并阐明配体结合的结构性基础（摘要原文）。PDB 1MUP 中信息素配体 TZL（2-(sec-butyl)thiazole，chain A 第 167 位）埋入 calyx，SITE LIG 记录衬壁残基 Leu44/Leu58/Phe60/Phe94/Ala107/Leu109/Leu120/Tyr124，以疏水残基为主。Flower 1996 综述摘要指出脂运载蛋白晶体结构高度保守，由单一八链连续氢键反平行β桶围成内部配体结合位点，家族共性为结合一系列小疏水分子，并承担内源与外源化合物的清除转运。

## 2. 吸附机制详解

### 机制1：鼠主尿蛋白 MUP-I 疏水 calyx 对信息素小疏水分子的包结

**描述**：脂运载蛋白（lipocalin）成员共享单一八链连续氢键反平行β桶，桶内围成内部配体结合位点（calyx）。鼠主尿蛋白 MUP-I（PDB 1MUP）在 calyx 内包结信息素配体 2-(仲丁基)噻唑（配体 TZL，chain A 第 167 位），calyx 壁由 SITE 记录残基 Leu44、Leu58、Phe60、Phe94、Ala107、Leu109、Leu120、Tyr124 构成，以脂肪族/芳香族疏水残基为主
**关键官能团**：['疏水 calyx 壁残基（Leu/Phe/Ala/Tyr 范德华接触面）', '八链β桶骨架']
**来源**：DOI 10.1038/360186a0

### 机制2：SCP-2 大疏水腔对固醇与脂肪酸的结合与转运

**描述**：SCP-2（固醇载体蛋白-2）以五链β片层与四个α螺旋层在界面围成大疏水腔。埃及伊蚊 SCP-2（PDB 1PZ4，1.35 Å）以该腔结合 C16 脂肪酸：棕榈酸配体（PLM，chain A 第 200 位）羧基端由连接第一α螺旋与第一β链的短 loop（SITE AC1 记录 Arg24、Gln25、Val26、Ile99、Phe105）协调，酰基链伸入蛋白内部疏水腔；SCP-2 已知亦结合胆固醇
**关键官能团**：['疏水腔（α螺旋层/β片层界面，范德华/疏水接触面）', 'loop 极性残基（Arg24/Gln25，头基协调）']
**来源**：DOI 10.1074/jbc.M306214200

## 3. 结构特征与结构-功能关系

必须保留：① 八链β桶围成的埋藏疏水 calyx（范德华接触面）；② 腔体积与衬壁几何对配体轮廓的尺寸/形状读出；③ 骨架预组织。可灵活调整：载体骨架、腔壁疏水基团化学（芳环/烷基/卤代烃面）、腔口极性与腔深。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白形态: MUP-I 为鼠尿可溶性蛋白（RCSB 1MUP 条目分子量 19.72 kDa），SCP-2 为可溶性脂质载体蛋白（RCSB 1PZ4 条目分子量 13.11 kDa）；用作吸附须固定化/移植于固体载体，或仅提取腔体设计原则 None
- 腔体完整性依赖: 包结依赖β桶（MUP）或α螺旋/β片层界面腔（SCP-2）的完整三级结构；变性或腔体溶剂化使疏水包结几何与低介电环境丧失 None
- 混杂腔、化学特异性弱: lipocalin calyx 与 SCP-2 腔以疏水包结与体积/形状读出结合，化学特异性弱（MUP 结合多种信息素，SCP-2 容纳多种脂质）；对 DDT 的选择性须在腔壁化学与腔几何层面构建 None

## 6. 相关原型

- cactus-spine
- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor

## 参考文献

[待补充]
