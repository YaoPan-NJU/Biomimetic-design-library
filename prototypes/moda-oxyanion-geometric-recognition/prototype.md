---
id: moda-oxyanion-geometric-recognition
name: ModA 氧阴离子几何识别蛋白（ModA Oxyanion Geometric Recognition Protein）
category: 微生物
organism: Escherichia coli / Azotobacter vinelandii（ModA 钼酸根结合蛋白，PDB 1AMF/1WOD）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 特异性识别
pollutants:
  - PFBS
  - PFBA
  - PFAS
adsorption_mechanisms:
  - 预组织氢键阵列对四面体钼酸根的几何识别
  - 四面体硫酸根的纯氢键结合（原理先例）
  - 合成转译：孔口几何双位点（T 位点三足硫脲匹配四面体磺酸根 / P 位点 squaramide 匹配平面羧酸根）头基类型反差捕获
qmax_range: "动态床容量待实验验证"
applicability:
  pH_range: [4, 9]
  temp_range: [10, 40]
  salinity: low_to_moderate
evidence_level: medium
coverage: full
source_scheme: S17_A17 (PFBS, score 85, passed) — 孔口几何双位点头基类型反差捕获
---
# ModA 氧阴离子几何识别蛋白（ModA Oxyanion Geometric Recognition Protein）

## 1. 生物原型简介

**问题定义**：钼是生物必需微量元素，细菌需从含高浓度硫酸根等化学相似氧阴离子的环境中特异性捕获微摩尔乃至更低浓度的钼酸根（MoO₄²⁻）。蛋白如何在无金属配位的前提下选择性识别四面体氧阴离子，是分子识别的基础问题。

**生物策略**：大肠杆菌周质 ModA 蛋白以预组织中性氢键给体阵列识别四面体钼酸根：钼酸根埋藏于 N 与 C 结构域间的低介电裂隙（PDB 1AMF）；MoO₄²⁻ 四氧与 Ser12、Ser39、Tyr170 侧链羟基及 Val152、Ala125 骨架酰胺 NH 形成氢键，无任何金属离子参与。同一位点以保守几何结合钨酸根（PDB 1WOD）。硫酸根结合蛋白（Pflugrath & Quiocho 1985, DOI 10.1038/314257a0）证明四面体硫酸根可仅由氢键结合。

**仿生转译**（来源方案 S17）：提取设计原则"几何互补决定氧阴离子选择性"，外推至四面体磺酸根（PFBS）对平面羧酸根（PFBA）的头基类型区分。S17 方案构建孔口双位点：T 位点（三足三硫脲汇聚匹配四面体磺酸根三氧排布，O-S-O ~109.5°）和 P 位点（squaramide 平面双 NH 匹配平面羧酸根双氧排布，O-C-O ~120°）。反差签名 R = α_T(PFBS/PFBA)/α_P(PFBS/PFBA)，R 显著大于 1 即头基几何做功耗能成立。诚实标注：ModA 区分发生在四面体内部（钼酸根对硫酸根），四面体对平面为原理外推而非功能同源。

## 2. 吸附机制详解

### 机制1：预组织氢键阵列对四面体钼酸根的几何识别

**描述**：ModA 以预组织中性氢键给体阵列识别四面体 MoO₄²⁻（Ser12/Ser39/Tyr170 侧链羟基 + Val152/Ala125 骨架酰胺 NH）；埋藏于 N/C 结构域间低介电裂隙，无金属参与
**关键官能团**：氢键给体（Ser/Thr/Tyr 侧链羟基、骨架酰胺 NH）、埋藏低介电口袋
**来源**：DOI 10.1038/nsb0997-703

### 机制2：四面体硫酸根的纯氢键结合（原理先例）

**描述**：硫酸根结合蛋白以纯氢键结合四面体 SO₄²⁻，无金属参与，证明四面体氧阴离子几何可被预组织中性给体阵列识别
**关键官能团**：氢键给体（骨架酰胺 NH、侧链羟基）
**来源**：DOI 10.1038/314257a0

### 机制3：合成转译——孔口几何双位点头基类型反差捕获（S17 方案）

**描述**：S17 方案在 PAF-1 孔口构建 T/P 双位点：T 位点为三足三硫脲（三给体汇聚匹配四面体磺酸根三氧，O-S-O ~109.5°），P 位点为 squaramide（双给体共面匹配平面羧酸根双氧，O-C-O ~120°）。六重对照：空白载体、等立体 N-甲基阻断体、给体计数匹配几何错位体、非预组织柔性体、阳离子电荷体、介孔对照。判决性签名：T/P 反差比 R 显著大于 3。反直觉点：磺酸根氧氢键受体能力弱于羧酸根，T 位点偏好磺酸根须以三给体几何克服更强碱性（高风险）
**关键官能团**：三足三硫脲（T 位点）、squaramide（P 位点）、PAF-1 芳烃疏水孔壁
**来源**：S17 方案通过版（score 85）

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | PAF-1 颗粒 | 50–200 µm | 固定床吸附载体 |
| 介观 | PAF-1 笼与孔口 | 笼 ~1.2 nm | 孔口放置 T/P 位点 |
| 微观 | 三足三硫脲 / squaramide | ~1.0–1.5 nm | 几何匹配头基 |
| 纳米 | NH···O 氢键 | 目标 1.9–2.3 Å | 方向性氢键锚定 |

### 结构-功能关系

**功能**：四面体磺酸根（PFBS）与平面羧酸根（PFBA）头基类型分流
**结构基础**：T 位点三给体汇聚几何匹配四面体；P 位点平面双给体匹配平面
**物理原理**：几何互补决定氧阴离子选择性（从 ModA 提取的设计原则）
**关键参数**：反差比 R = α_T/α_P ≥ 3；分离因子 ≥ 2（~0.41 kcal/mol）

**仿生制造启示**：
- T 位点：1,3,5-三(氨甲基)苯 + 4-硝基苯基异硫氰酸酯 → 三足三硫脲 → CuAAC 接枝
- P 位点：二甲基 squarate + 氨基芳基炔基把手 + 4-硝基苯胺 → squaramide → 接枝

## 4. 已报道性能数据

> 来源方案 S17 设计目标（实验待验证）

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| PFBS | T 位点 PAF-1 | — | 动态床容量待测 | 6–9 | 25 | S17 工程设计值 | 方案通过版 |
| PFBA | P 位点 PAF-1 | — | 动态床容量待测 | 6–9 | 25 | S17 工程设计值 | 方案通过版 |

## 5. 适用场景

**最适合**：PFAS 混合物中磺酸/羧酸组分分流（分别导入各自最优破坏列车）；头基类型维度的机制研究
**不适用**：需 ng/L 单分子特异亲和的场景；高硫酸根基质（硫酸根耐受为独立未决子问题）
**约束条件**：
- 水相氢键弱：中性硫脲/squaramide 水相 K 常低于 10–50 M⁻¹
- T 位点磺酸偏好先验低（须克服羧酸根更强氢键碱性）
- 硫酸根与磷酸根同为四面体，头基选择不天然解决无机含氧阴离子竞争

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- cell-membrane-ion-channel
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- diatom-frustule
- sbp-sulfate-oxyanion-geometric-recognition：硫酸根结合蛋白
- serine-protease-oxyanion-hole：丝氨酸蛋白酶氧阴离子穴
- nrta-nitrate-binding-protein：硝酸盐结合蛋白

## 参考文献

[1] Hu Y, et al. Nat Struct Biol. 1997;4(9):703-707. DOI 10.1038/nsb0997-703 (PDB 1AMF)
[2] Lawson DM, et al. J Chem Soc Dalton Trans. 1997:3981-3984. DOI 10.1039/a704006g
[3] Pflugrath JP, Quiocho FA. Nature. 1985;314:257-260. DOI 10.1038/314257a0
[4] Emami Khansari H, et al. ACS Omega. 2017;2:9057-9066. DOI 10.1021/acsomega.7b01485
[5] S17 方案通过版 (score 85). rounds/fresh_1000/pfbs/SCHEMES/S17_A17_pore-mouth-dual-site-headgroup_passed.md
