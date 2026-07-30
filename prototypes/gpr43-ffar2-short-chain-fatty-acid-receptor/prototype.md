---
id: gpr43-ffar2-short-chain-fatty-acid-receptor
name: GPR43/FFAR2 短链脂肪酸受体（GPR43/FFAR2 Short-Chain Fatty Acid Receptor）
category: 动物
organism: Homo sapiens（人源 GPR43/FFAR2，游离脂肪酸受体 2，A 类 G 蛋白偶联受体）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 分子筛分
adsorption_mechanisms:
  - 短链脂肪酸羧酸根头基的成对精氨酸离子对锚定
  - 疏水腔对短链尾链的容纳与链长选择性
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# GPR43/FFAR2 短链脂肪酸受体（GPR43/FFAR2 Short-Chain Fatty Acid Receptor）

## 1. 生物原型简介

**问题定义**：短链脂肪酸（乙酸/丙酸/丁酸）是肠道菌群发酵产物，经游离脂肪酸受体 FFAR2（GPR43）调控代谢与免疫功能。FFAR2 如何从化学相似的有机阴离子中选择性识别短链脂肪酸的羧酸根头基并分辨其链长，是分子识别的结构基础问题。FFAR2 属 A 类 G 蛋白偶联受体，与识别长链脂肪酸的 FFA1/FFA4 同家族但配体链长偏好不同。

**生物策略**：Zhang 等以冷冻电镜解析丁酸结合的活性态 FFAR2-miniGq 复合物（PDB 8T3S，分辨率 3.07 Å）：丁酸的羧酸根头基由正构口袋中一对相邻精氨酸 Arg180(5.39) 与 Arg255(7.35) 配位（离子对/氢键），His242(6.55) 与 Arg255 作用以组织羧酸根结合口袋，Tyr165(ECL2) 与羧酸根形成氢键，Gln148(ECL2) 稳定 Arg180；该精氨酸对在 FFA1-FFA3 间高度保守。丁酸的短烷基尾链由疏水亚腔 Cys141/Val144/Val179/Leu183 容纳，Tyr90(3.29) 与短链直接形成疏水作用。突变 Arg180/Arg255/His242 消除对短链脂肪酸的响应（正构拮抗剂结合仅略微受影响），证明该阳离子锚对短链羧酸根头基的特异性。Kugawa 等（PDB 8Y6Y）通过 FFAR2 与 FFA1 的结构比较及突变研究揭示 FFAR2 的链长选择性，并显示拮抗剂 GLPG0974 结合于正构口袋旁侧。同一研究的 FFAR2-乙酸（PDB 8J24，分辨率 2.6 Å）与 FFAR2/3-戊酸（PDB 8J20）结构进一步印证短链羧酸根识别的保守性（Cell Res 2024 沉积引文，仅经 RCSB 沉积记录核验）。

## 2. 吸附机制详解

### 机制1：短链脂肪酸羧酸根头基的成对精氨酸离子对锚定

**描述**：人源 FFAR2 以正构口袋中一对相邻精氨酸 Arg180(5.39) 与 Arg255(7.35) 配位短链脂肪酸（丁酸）的羧酸根头基（离子对/氢键）；His242(6.55) 与 Arg255 作用以组织羧酸根结合口袋，Tyr165(ECL2) 与羧酸根形成氢键，Gln148(ECL2) 稳定 Arg180。该精氨酸对在 FFA1-FFA3 间高度保守。突变为丙氨酸/赖氨酸消除对短链脂肪酸的响应
**关键官能团**：['阳离子/氢键给体（Arg180、Arg255 胍基；His242、Tyr165、Gln148 侧链）', '正构结合口袋']
**来源**：DOI 10.1126/sciadv.adj2384

### 机制2：疏水腔对短链尾链的容纳与链长选择性

**描述**：FFAR2 正构口袋含一疏水亚腔（Cys141(4.57)、Val144(4.60)、Val179(5.38)、Leu183(5.42)）容纳丁酸的短烷基尾链，Tyr90(3.29) 与短链直接形成疏水相互作用；FFAR2 选择性识别短链脂肪酸（C2-C4），长链脂肪酸由 FFA1/FFA4 识别，链长选择性由结构比较与突变研究揭示
**关键官能团**：['疏水腔壁残基（Cys141、Val144、Val179、Leu183、Tyr90）']
**来源**：DOI 10.1038/s41467-025-57983-4

## 3. 结构特征与结构-功能关系

必须保留：① 与短链羧酸根头基几何互补的成对阳离子锚（精氨酸胍基型，模拟 Arg180/Arg255）；② 辅助极性残基（His/Tyr/Gln 型）组织并稳定锚定；③ 与短链（C2-C4）尾链几何匹配的疏水腔。可灵活调整：载体骨架、阳离子/氢键给体化学（胍基/脒基/脲/硫脲）、疏水腔壁修饰（烃/氟碳链）与腔深/孔径。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 膜蛋白/复合物形态: FFAR2 为 A 类 G 蛋白偶联受体（膜整合蛋白），已解析结构为 FFAR2-G 蛋白复合物（8T3S 复合物约 126 kDa，8J24 约 157 kDa，冷冻电镜），其识别基序依赖跨膜束与膜环境，用作吸附须固定化/移植于固体载体 None
- 头基化学偏好（羧酸根）: FFAR2 识别的是短链脂肪酸的羧酸根头基（由精氨酸对锚定）；PFBS 为磺酸根头基，与羧酸根在电荷分布、几何与 pKa 上不同，转译为磺酸根识别较软，最直接的头基同源物为短链全氟羧酸（如全氟丁酸 PFBA，C4 羧酸根） None
- 链长选择性窗口: FFAR2 疏水腔适配短链烷基（C2-C4）；全氟 C4 尾链较烃类丁基更刚硬、更大、更疏水，能否适配同一疏水腔未知 None

## 6. 相关原型

- cell-membrane-ion-channel
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- diatom-frustule
- dmpr-phenol-effector-binding-domain

## 参考文献

[待补充]
