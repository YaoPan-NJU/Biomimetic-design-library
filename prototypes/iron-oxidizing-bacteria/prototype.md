---
id: iron-oxidizing-bacteria
name: 铁氧化细菌（Iron Oxidizing Bacteria）
category: 微生物
organism: Acidithiobacillus ferrooxidans
biomimetic_dimension: 过程仿生
features:
  - 层次孔
  - 活性氧位点
  - 催化降解
  - 生物矿化模板
pollutants:
  - As(III)
  - As(V)
  - Cd(II)
  - Cd²⁺, 10 mg/L
  - Pb(II)
  - Pb²⁺, 100 mg/L
  - Sb(III)
  - Sb(V)
  - Se(VI)
adsorption_mechanisms:
  - 亚铁氧化驱动铁氢氧化物共沉淀
  - 施氏矿物As(III)吸附机制-表面沉淀
  - 去除机理三阶段
  - 吸附机制
  - Cu在施氏矿物表面配位模式
  - 砷在铁(氧氢)氧化物表面配位模式
qmax_range: "42.2-177.2 mg/g"
applicability:
  pH_range: [3.0, 7.5]
  temp_range: null
  salinity: low_to_moderate
evidence_level: low
# provenance: 7 papers, 23 verified, 6 unverified
# coverage: normal
# status: active
---
# 铁氧化细菌（Iron Oxidizing Bacteria）

## 1. 生物原型简介

**问题定义**：水体中锑（Sb）和砷（As）污染严重威胁生态安全和人类健康，传统化学合成方法制备的Fe-Mn氧化物能耗高、步骤复杂。铁氧化细菌（IOB）能在常温常压下将Fe(II)氧化为Fe(III)，并矿化形成高活性的铁氧化物，同时细菌胞外聚合物提供丰富的有机官能团，是一种绿色、可持续的材料合成策略。

**生物策略**：氧化亚铁硫杆菌（Acidithiobacillus ferrooxidans）在代谢过程中将Fe(II)氧化为Fe(III)，形成的生物成因Fe(III)矿物具有比非生物矿物更大的比表面积、更小的粒径和更低的结晶度。细菌胞外有机质含有羧基、磷酸基、氨基和羟基等官能团，可增强与重金属的配位作用。将Fe-Mn双金属氧化物负载于高岭土基底上，实现多组分协同吸附。

## 2. 吸附机制详解

### 机制1：亚铁氧化驱动铁氢氧化物共沉淀

**描述**：脲酶水解尿素: CO(NH₂)₂+H₂O→NH₂COOH+NH₃; NH₂COOH+H₂O→NH₃+H₂CO₃; 最终产生CO₃²⁻+Ca²⁺→CaCO₃↓
**关键官能团**：['-NH-（亚氨基）', '-O-（醚键）', '-COOH（羧基）', '-OH（羟基）']

### 机制2：施氏矿物As(III)吸附机制-表面沉淀

**描述**：双齿双核结合，形成Fe-As、As-O原子距特征
**关键官能团**：['-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.7524/j.issn.0254-6108.2020070302

### 机制3：去除机理三阶段

**描述**：第一阶段：As(III)接触锰氧化物壳层后迅速氧化为As(V)，部分Mn(IV)还原溶解；第二阶段：As(V)受静电吸附再吸附于材料表面，少量与Mn-OH表面络合；第三阶段：As(V)扩散穿过壳层到达施氏矿物内核，通过As-O-Fe络合和配体交换富集
**关键官能团**：['-S-（硫醚键）', '-O-（醚键）', '-OH（羟基）']
**来源**：DOI 10.13671/j.hjkxxb.2021.0204

### 机制4：吸附机制

**描述**：内球络合、表面络合、氢键、氧化（Sb(III)/As(III)被部分氧化为Sb(V)/As(V)）
**关键官能团**：['-S-（硫醚键）', '氢键位点']
**来源**：DOI 10.1016/j.clay.2021.106392

### 机制5：Cu在施氏矿物表面配位模式

**描述**：bidentate inner-sphere complexes with singly coordinated surface sites
**关键官能团**：['硫酸根 SO₄²⁻', '配位/螯合位点', 'Fe-O/OH位点', '表面羟基 -OH (Fe-OH)', '-O-（醚键）']
**来源**：DOI 10.3390/min15080868

### 机制6：砷在铁(氧氢)氧化物表面配位模式

**描述**：binuclear bidentate corner-sharing (2C), mononuclear bidentate edge-sharing (2E), mononuclear monodentate corner-sharing (1V)
**关键官能团**：['-S-（硫醚键）', '-O-（醚键）', '配位/螯合位点', '-SH（巯基）']
**来源**：DOI 10.3390/min15080868

## 3. 结构特征与结构-功能关系

必须保留：IOB的生物氧化能力（Fe(II)→Fe(III)）、胞外有机质官能团（-COOH, -OH, -NH₂, -PO₃H₂）、高岭土多孔基底。可灵活调整：Fe/Mn摩尔比（1:0.1最优）、高岭土负载量、IOB培养条件。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| Cd(II) |  | 98.52%（1:1:1混合，10 mg | - | patent: CN113275374A | ❓ |
| Pb(II) |  | 99.49%（1:1:1混合，100 m | - | patent: CN113275374A | ❓ |
| Cd²⁺, 10 mg/L |  | 0.5:0.5:1→94.54%; 1: | - | patent: CN113275374A | ❓ |
| Pb²⁺, 100 mg/L |  | 0.5:0.5:1→92.66%; 1: | - | patent: CN113275374A | ❓ |
| As(V) | Fe³⁺水解合成的施氏矿物 | 95.3 | 3.0 | literature: 10.7524/j.issn.025 | ❓ |
| As(V) | Fe³⁺水解合成的施氏矿物 | 63.9 | 7.0 | literature: 10.7524/j.issn.025 | ❓ |
| As(III) | Fe³⁺水解合成的施氏矿物 | 31.0 | 3.0 | literature: 10.7524/j.issn.025 | ❓ |
| As(III) | Fe³⁺水解合成的施氏矿物 | 81.6 | 7.0 | literature: 10.7524/j.issn.025 | ❓ |
| As(III) |  | >98% at pH 7-9 | - | literature: 10.7524/j.issn.025 | ❓ |
| As(III) |  | 25.1 | 7.5 | literature: 10.7524/j.issn.025 | ❓ |
| As(III) |  | 93.0 | 7.5 | literature: 10.7524/j.issn.025 | ❓ |
| Sb(III) | BKFM (1:0.1) | 177.19 | 6.0 ± 0.1 | literature: 10.1016/j.clay.202 | ❓ |
| Sb(V) | BKFM (1:0.1) | 56.26 | 6.0 ± 0.1 | literature: 10.1016/j.clay.202 | ❓ |
| As(III) | BKFM (1:0.1) | 62.92 | 6.0 ± 0.1 | literature: 10.1016/j.clay.202 | ❓ |
| As(V) | BKFM (1:0.1) | 42.18 | 6.0 ± 0.1 | literature: 10.1016/j.clay.202 | ❓ |
| Se(VI) | J-2.5 (biogenic jaro | 63 | 3.0 | literature: 10.1016/j.jhazmat. | ❓ |
| Se(VI) | J-2.5 | 15 | - | literature: 10.1016/j.jhazmat. | ❓ |
| Se(VI) | J-3.5 | 16 | - | literature: 10.1016/j.jhazmat. | ❓ |
| Se(VI) | J-90C (non-biogenic  | 9 | - | literature: 10.1016/j.jhazmat. | ❓ |
| Se(VI) | S-2.5 (biogenic schw | 77 | - | literature: 10.1016/j.jhazmat. | ❓ |
| Se(VI) | S-2.5 | 33 | - | literature: 10.1016/j.jhazmat. | ❓ |
|  |  | Fe(1.0):S(0.36):K(0. | - | literature: 10.1016/j.jhazmat. | ❓ |
|  |  | Fe(1.0):S(0.11):Se(0 | - | literature: 10.1016/j.jhazmat. | ❓ |

## 5. 适用场景

**约束条件**：
- pH 3-4时富As(III)AMD中施氏矿物对As(III)吸附量: 300-500 mmol As/mol Fe
- pH 9时施氏矿物对As(III)吸附量: 379 mmol As/mol Fe
- Fe³⁺水解施氏矿物对As(V)最大吸附量(pH 3.0): 182.86 mg/g
- Fe³⁺水解施氏矿物对As(III)最大吸附量(pH 3.0): 45.50 mg/g
- Fe³⁺水解施氏矿物对As(V)最大吸附量(pH 7.0): 143.25 mg/g
- Fe³⁺水解施氏矿物对As(III)最大吸附量(pH 7.0): 217.85 mg/g
- 施氏矿物7次循环后对As(V)去除率(pH 3.0): 95.3 %
- 施氏矿物7次循环后对As(V)去除率(pH 7.0): 63.9 %
- 施氏矿物7次循环后对As(III)去除率(pH 3.0): 31.0 %
- 施氏矿物7次循环后对As(III)去除率(pH 7.0): 81.6 %

## 6. 相关原型

- acidimicrobium-reductive-defluorination
- anaerobic-sequential-dechlorination-cascade
- bone-structure
- coral-skeleton
- ddt-dehydrochlorinase-gst

## 参考文献

[1] DOI: 10.1016/j.clay.2021.106392
[2] DOI: 10.1016/j.jhazmat.2024.136256
[3] DOI: 10.7524/j.issn.0254-6108.2020070302
[4] 专利: CN113275374A
