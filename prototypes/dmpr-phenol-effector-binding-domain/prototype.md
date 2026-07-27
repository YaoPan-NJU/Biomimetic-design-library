---
id: dmpr-phenol-effector-binding-domain
name: DmpR 苯酚效应物结合域（A 域）（DmpR Phenol Effector-Binding Domain (A domain / sensory domain)）
category: 微生物
organism: Pseudomonas putida KCTC 1452 / Pseudomonas sp. CF600（DmpR 苯酚响应转录调控蛋白，PDB 6IY8 酚结合态）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 特异性识别
pollutants:
  - BPA
  - BPF
  - BPS
  - BPAF
  - 壬基酚
  - 雌二醇
adsorption_mechanisms:
  - 疏水腔与 His100/Trp128 酚羟基定位对芳香效应物的识别
  - 效应物结合诱导感觉域构象变化与下游信号传递
  - 合成转译：固定酚锚（吡啶 N）+ 桥连区空间门谱切换的 COF/HCP 识别单元
qmax_range: "ng/L 级 Kd ≥ 10⁴ L/kg 目标"
applicability:
  pH_range: [6, 9]
  temp_range: [10, 40]
  salinity: low_to_moderate
evidence_level: medium
coverage: full
source_scheme: S14_A01 (BPA, score 86, passed) — DmpR 型固定酚锚加桥连区空间门晶态 COF
---
# DmpR 苯酚效应物结合域（A 域）（DmpR Phenol Effector-Binding Domain）

## 1. 生物原型简介

**问题定义**：苯酚及取代酚是常见芳香族环境污染物，细菌需特异性感应它们以启动降解操纵子。DmpR 源于 Pseudomonas sp. CF600（质粒 pVI150 dmp 系统），是 σ54 依赖苯酚降解操纵子的 AAA+ 转录激活蛋白，其 N 端 A 域特异识别苯酚/取代酚效应物。

**生物策略**：Park 等测定了苯酚结合活性态 DmpR 晶体结构（PDB 6IY8，DmpRΔD 构建体）：A 域以 V4R 支架的（β/α）4 桶围成封闭疏水腔（约 24–36 Å³）容纳苯酚芳环，酚羟基定位于 His100 与 Trp128 之间。PDB SITE AC1 记录结合残基 Pro97/His100/Val108/Met126/Trp128/Ala156/Ser160。His100 保守存在于酚响应蛋白 PoxR/MopR，是酚类特异性的关键决定簇。苯酚结合诱导口袋构象变化，经卷曲螺旋 B-linker 传至 AAA+ ATPase 域。苯酚 Kd 约 12–16 µM。

**仿生转译**（来源方案 S14）：提取三条设计原则——① 锚化学身份保守（酚羟基为不变锚柄）；② 对位侧壁身份界定口袋体积（单氨基酸替换 E135K 切换效应物谱）；③ 谱可经单位点调制（同位点原位调制）。转译为非蛋白晶态 β-酮烯胺 COF：单一不变芳香氮氢键锚（吡啶 N）+ 晶格固定同一几何位点上独立改变桥连区空间门（G0 氢门/G1 甲基门/G2 氟门/G3 极性门），在中性水相四元竞争中对 BPA 给出可测且逆 logKow 梯度的分离因子。

## 2. 吸附机制详解

### 机制1：疏水腔与 His100/Trp128 酚羟基定位对芳香效应物的识别

**描述**：DmpR A 域以 V4R/(β/α)4 桶构成封闭疏水腔容纳苯酚芳环，酚羟基定位于 His100 与 Trp128 之间。Kd 约 12–16 µM
**关键官能团**：疏水腔壁残基（Phe93、Trp128、Tyr155、Tyr170、Tyr159）、酚羟基定位残基（His100、Trp128）
**来源**：DOI 10.1038/s41467-020-16562-5

### 机制2：效应物结合诱导感觉域构象变化与下游信号传递

**描述**：苯酚结合诱导口袋构象变化，经 B-linker 传至 AAA+ 域，激活 σ54 依赖转录
**关键官能团**：苯酚结合口袋、卷曲螺旋 B-linker
**来源**：DOI 10.1038/s41467-020-16562-5

### 机制3：合成转译——固定酚锚 + 桥连区空间门谱切换（S14 方案）

**描述**：S14 方案将 DmpR 识别原理转译为 2,6-二芳基吡啶单体编织的 HCP/COF：中央吡啶 N 为氢键受体锚（结合一个对位酚 OH），两侧芳基 3,5 位取代基构成门壁（G0 氢门/G1 甲基门/G2 氟门/G3 极性门）。锚门空间解耦：吡啶 N 居中锚定，门壁分列两侧。G1 甲基门匹配 BPA 异丙叉偕二甲基，BPAF 双三氟甲基桥过填位阻排除，BPS 砜桥极性错配。选择性由锚门空间解耦+门身份谱切换承担
**关键官能团**：2,6-二芳基吡啶（锚门一体单体）、β-酮烯胺 COF 晶格
**来源**：S14 方案通过版（score 86）

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | COF/HCP 颗粒 | 50–200 µm | 固定床吸附载体 |
| 介观 | 微孔孔道 | 0.6–1.5 nm | 分子可及与传质 |
| 微观 | 2,6-二芳基吡啶识别单元 | ~1.0–1.5 nm | 锚门一体识别 |
| 纳米 | 酚 OH···N 氢键 | ~1.8–2.2 Å | 酚羟基配准锚定 |

### 结构-功能关系

**功能**：单一不变酚锚 + 桥连区空间门对 BPA 类似物的非单调选择性
**结构基础**：吡啶 N 居中锚定酚 OH；门壁取代基体积/极性匹配桥连区
**物理原理**：锚门热力学解耦——亲和力由疏水孔壁承担，选择性由锚门空间解耦承担
**关键参数**：α(BPA/BPAF) > 1（逆 logKow 签名）；S2 硬 go/no-go：α*(BPA/BPAF) ≥ 1.2

**仿生制造启示**：
- 2,6-二溴吡啶 + 芳基硼酸 Suzuki 偶联 → G0–G3 单体
- 单体 + 四苯基甲烷 + FDA + FeCl₃ → Friedel-Crafts 编织成网

## 4. 已报道性能数据

> 来源方案 S14 设计目标（实验待验证）

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| BPA | G1 甲基门 COF | — | ng/L 级 Kd ≥ 10⁴ L/kg 目标 | 7 | 25 | S14 工程设计值 | 方案通过版 |

## 5. 适用场景

**最适合**：中性水相四元双酚类似物（BPA/BPF/BPS/BPAF）选择性分离；需逆 logKow 非单调签名的场景
**不适用**：单酚（苯酚、壬基酚）无桥连区门匹配，仅锚定结合；高 DOM 基质
**约束条件**：
- 酚 OH 与吡啶 N 氢键在水相近乎热中性（0–4 kJ/mol），疏水微孔低介电增强仅为推断
- S2 逆梯度签名（α(BPA/BPAF) > 1）为低先验预测（P(S2) ≈ 20–30%）
- 非晶 HCP 门为统计预组织，位点异质性使 α 为系综平均

## 6. 相关原型

- errg-bpa-endocrine-receptor：ERRγ BPA 内分泌受体
- lipocalin-hydrophobic-calyx：脂质运载蛋白疏水杯
- serine-protease-oxyanion-hole：丝氨酸蛋白酶氧阴离子穴（同为通过方案原型）

## 参考文献

[1] Park MH, et al. Nat Commun. 2020;11:2625. DOI 10.1038/s41467-020-16562-5 (PDB 6IY8)
[2] Pavel L, et al. J Bacteriol. 1994;176:7069-7076. DOI 10.1128/jb.176.22.7069-7076.1994 (E135K)
[3] Chen 2016 (BPA 类似物 pKa/logKow 综述)
[4] S14 方案通过版 (score 86). rounds/fresh_1000/bpa/SCHEMES/S14_A01_DmpR-anchor-gate-COF_passed.md
