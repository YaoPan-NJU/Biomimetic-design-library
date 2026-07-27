---
id: alkb-alkane-hydroxylase-chain-length
name: AbAlkB 烷烃羟化酶底物通道深度窗口（Alcanivorax borkumensis AbAlkB Alkane Hydroxylase Substrate Channel Depth Window）
category: 微生物
organism: Alcanivorax borkumensis（AbAlkB 烷烃羟化酶，底物通道有限深度设定链长上限）
biomimetic_dimension: 结构仿生
features:
  - 分子筛分
  - 链长选择
pollutants:
  - 壬基酚
  - NPEO
  - LAS
  - 表面活性剂
adsorption_mechanisms:
  - 刚性狭缝深度窗口按链长上限排斥超长线性尾
  - 底物通道有限深度的几何转译（碳分子筛狭缝超微孔）
applicability:
  pH_range: [5, 9]
  temp_range: [10, 40]
  salinity: low_to_moderate
evidence_level: low
coverage: full
source_scheme: S35_A04 (NP, score 57, terminated) — 链长窗口狭缝碳（AbAlkB 底物通道深度启发）
---
# AbAlkB 烷烃羟化酶底物通道深度窗口

## 1. 生物原型简介

**问题定义**：Alcanivorax borkumensis 是海洋石油降解的优势菌种，其 AbAlkB 烷烃羟化酶以底物通道有限深度设定链长上限——十六烷 C16 不被氧化，偏好位阻小的 C–H，单个大体积残基控制底物特异性。

**生物策略**：AbAlkB 的底物通道为有限深度的疏水管，通道深度设定可氧化链长上限。Naing 2013 经 PMC 全文核验确认：C16 因通道深度不足而无法到达催化中心，不被氧化。该机制为"几何深度窗口"——非化学选择性，而是物理通道长度限制。

**仿生转译**（来源方案 S35，score 57，terminated）：将 AbAlkB 底物通道有限深度的几何原理转译为刚性狭缝碳分子筛（CMS）超微孔。6FDA 热解 CMS 的狭缝深度可调，按尺寸/形状分离异构体。诚实标注：Seo 2021 的 CMS 为等链长 C6 异构体动力学膜分离、线性优先方向，与本案"宽度反转纳支链"方向相反；方案因承重轴平庸化与原创性天花板被终止。

## 2. 吸附机制详解

### 机制1：刚性狭缝深度窗口

**描述**：CMS 狭缝超微孔的有限深度设定链长上限，排斥超长线性尾（NPEO ≥ NP4EO、LAS），保留短链支链异构体
**关键官能团**：刚性碳狭缝壁（范德华表面）
**来源**：DOI 10.1016/j.jinorgbio.2012.12.012 (Naing 2013, PMC 全文核验)

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | CMS 膜/颗粒 | — | 分离 |
| 介观 | 狭缝超微孔 | 0.5–1.0 nm | 链长深度窗口 |
| 微观 | 碳狭缝壁 | 原子级 | 范德华筛分 |

### 结构-功能关系

**功能**：按链长上限排斥超长线性尾
**结构基础**：CMS 狭缝深度有限（~C9 等效深度）
**物理原理**：几何深度窗口（超长链无法进入）
**关键参数**：狭缝深度梯度序列的分离因子曲线

**仿生制造启示**：
- 6FDA 前驱体热解制备 CMS
- 热解温度调控狭缝宽度/深度

## 4. 已报道性能数据

> 方案因原创性天花板终止，无实验数据

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| — | — | — | — | — | — | 方案终止，无实验 | — |

## 5. 适用场景

**最适合**：作为概念验证原型——理解"底物通道深度窗口"原理在分离科学中的通用性
**不适用**：实际 NP 异构体分离（承重轴被裁决为平庸化，疏水/电荷单调即可分 NPEO/LAS）
**约束条件**：
- 方案被终止（score 57），承重轴原创性与已通过 A01 重叠
- CMS 方向与 AbAlkB 天然方向（纳线性排支链）相反
- 狭缝深度 Å 级独立调控物理不可实现

## 6. 相关原型

- ipso-hydroxylation-pathway：ipso 羟基化途径（同为 NP 降解相关微生物原型，但机制不同）
- kcsa-potassium-channel-selectivity-filter：KcsA 钾通道选择性过滤器（通道几何选择类比）

## 参考文献

[1] Naing HT, et al. J Inorg Biochem. 2013;121:46-52. DOI 10.1016/j.jinorgbio.2012.12.012 (PMC 全文核验)
[2] Seo Y, et al. Adv Sci. 2021;8:2004999. DOI 10.1002/advs.202004999
[3] S35 方案终止版 (score 57). rounds/fresh_1000/np/SCHEMES/S35_A04_chain-length-window-slit_terminated.md
