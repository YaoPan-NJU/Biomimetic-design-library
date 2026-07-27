定位于 Cu 附近
**关键官能团**：活性炭微孔疏水环境邻接 Cu 位点
**来源**：方案 BPA-U01 设计文档

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | 活性炭颗粒填充床 | 0.5–2 mm (GAC) | 固定床吸附 |
| 介观 | 微孔-介孔分级孔道 | 0.5–50 nm | 传质 + 疏水预富集 |
| 微观 | 表面 Cu(II)-N 螯合位点 | ~0.5 nm | 酚羟基配位识别 |
| 纳米 | Cu(II)-酚配位键 | ~1.8–2.2 Å | 电子环境读出 |

### 结构-功能关系

**功能**：对可氧化酚（BPA/BPF）的配位判别，提供 logKow 无法解释的正交维度
**结构基础**：单核 Cu(II)-N 螯合位点 + 邻接疏水微孔
**物理原理**：Cu(II)-酚配位化学（电子环境读出）+ 疏水预富集（驱动力）
**关键参数**：BPA 分配增量（Cu 体 vs 无 Cu/Zn 体）；Cu 密度依赖性；BPA>BPS>非酚芳香

**仿生制造启示**：
- 活性炭预氧化引入羧基/酚羟基
- EDC/NHS 偶联接枝三氮唑/联吡啶/IDA 螯合臂（低密度 0.1–0.3 mmol/g，防桥连双核）
- 稀 Cu(II) 溶液装载，对照体：无 Cu、Zn(II) 替代、螯合臂删除

## 4. 已报道性能数据

> 来源方案 BPA-U01 设计目标（实验待验证）

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| BPA | Cu-活性炭 | — | 设计靶标 | 7 | 25 | BPA-U01 工程设计值 | 方案修订版 |

## 5. 适用场景

**最适合**：市政二级出水中 BPA 对 BPS/非酚芳香的配位判别研究；可氧化酚的选择性捕获
**不适用**：高 EDTA/腐殖酸基质（螯合 Cu 竞争）；需区分 BPA/BPF 的场景（二者均为可氧化酚）
**约束条件**：
- Cu 浸出为合规风险（须 < 出水限值）
- O₂ 存在下可能 turnover 氧化 BPA（须控 O₂ 或切换为氧化预浓缩模式）
- 先例密集（Cu 改性碳吸附酚），增量须以因果对照量化

## 6. 相关原型

- dmpr-phenol-effector-binding-domain：DmpR 酚效应物传感器（酚羟基氢键锚定 vs Cu 配位锚定）
- hrp-laccase-phenol-radical-coupling：HRP/漆酶酚自由基偶联（催化 vs 配位识别）

## 参考文献

[1] Reiss R, et al. Cell Mol Life Sci. 2013;70:4359-4375. DOI 10.1007/s00018-013-1305-3 (PMC3670849)
[2] BPA-U01 方案修订版 (score 79). rounds/ultimate_200/deep_design/BPA_U01_LACCASE_CU.md
---
id: laccase-t1-cu-phenol-coordination
name: 漆酶 T1 单核 Cu(II) 酚羟基配位识别（Laccase T1 Mononuclear Cu(II) Phenol Coordination Recognition）
category: 微生物
organism: Trametes versicolor / 多铜氧化酶（漆酶 T1 单核 Cu 中心对酚羟基的配位与单电子转移识别）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 配位选择性
pollutants:
  - BPA
  - 双酚A
  - 壬基酚
  - 酚类污染物
adsorption_mechanisms:
  - 单核 Cu(II)-N 螯合位点对酚羟基的定向配位识别
  - Cu(II)-酚配位提供 logKow 无法解释的正交电子环境读出维度
  - 疏水底物槽邻接 Cu 位点的协同预富集
applicability:
  pH_range: [5, 9]
  temp_range: [10, 40]
  salinity: low_to_moderate
evidence_level: medium
coverage: full
source_scheme: BPA-U01 (BPA, score 79, revise) — 漆酶 T1 位启发单核 Cu(II) 配位识别活性炭
---
# 漆酶 T1 单核 Cu(II) 酚羟基配位识别

## 1. 生物原型简介

**问题定义**：双酚 A（BPA）与 BPF/BPS 在中性水中疏水性接近（logKow 差 ≤0.3），常规吸附按 logKow 单调排序、无判别维度。漆酶以 T1 单核 Cu(II) 对酚羟基的配位与单电子转移区分可氧化酚，这是自然界处理酚的真实进化方案。

**生物策略**：多铜氧化酶（漆酶）在 T1 单核 Cu 中心氧化底物。T1 Cu(II) 与酚羟基形成配位键并执行单电子转移，将酚氧化为酚氧自由基。底物广谱疏水口袋邻接 T1 位，容纳酚类芳环并预定位于 Cu 附近。该识别机制基于酚的电子环境（可氧化性），而非疏水性或分子量。

**仿生转译**（来源方案 BPA-U01，score 79）：提取"单核 Cu(II)-酚定向配位 + 疏水底物槽"两个硬对应，在活性炭表面固定单核 Cu(II)-N 螯合位点（三氮唑/联吡啶/亚氨基二乙酸），获得一个 logKow 无法解释的正交识别维度。承重赌注：固定 Cu(II)-酚配位在中性二级出水（EDTA/Cl⁻/DOM）下能否保留对 BPA 的判别增量。

## 2. 吸附机制详解

### 机制1：单核 Cu(II)-酚定向配位识别

**描述**：T1 Cu(II) 对酚羟基的配位与单电子转移识别。BPA 为可氧化双酚，BPS 砜桥吸电子使酚更难配位/氧化，由此产生判别
**关键官能团**：单核 Cu(II)-N 螯合位点（三氮唑/联吡啶/IDA）
**来源**：DOI 10.1007/s00018-013-1305-3 (Reiss 2013, PMC3670849)

### 机制2：疏水底物槽协同预富集

**描述**：漆酶 T1 位邻近疏水底物槽容纳酚类芳环、预
