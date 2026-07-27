---
id: rw1-bay-region-dioxygenase
name: Sphingomonas RW1 角位双加氧酶（醚骨架识别几何）（Sphingomonas RW1 Bay-Region Dioxygenase (Ether Skeleton Recognition Geometry)）
category: 微生物
organism: Sphingomonas sp. strain RW1（二苯并-p-二噁英降解菌，角位双加氧酶 dxnA1A2 基因簇）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 骨架判别
pollutants:
  - TCDD
  - 二噁英
  - PCDF
  - PCB
adsorption_mechanisms:
  - 醚氧锚定点（偶极/弱相互作用读杂原子）
  - 角位轮廓窗口（区分联苯骨架/呋喃骨架/二噁英骨架）
  - 虚拟模板 MIP 对醚骨架几何的记忆
applicability:
  pH_range: [5, 9]
  temp_range: [10, 40]
  salinity: low
evidence_level: medium
coverage: full
source_scheme: SL11_A04 (TCDD, score 69, revise) — 二芳醚骨架角位轮廓虚拟模板 MIP
---
# Sphingomonas RW1 角位双加氧酶（醚骨架识别几何）

## 1. 生物原型简介

**问题定义**：二噁英类（TCDD）为平面刚性、极疏水、缺电子抗氧化分子，识别把手极少。自然界中 Sphingomonas sp. RW1 是少数能真实降解二苯并-p-二噁英的细菌之一，其角位双加氧酶专攻醚桥相邻角位。

**生物策略**：RW1 角位双加氧酶识别二苯并-p-二噁英醚桥相邻角位（骨架特异），对二噁英的醚骨架执行角位氧合攻击。Wittich 1992 核验 RW1 代谢二苯并-p-二噁英；Wilkes 1996 表征角位双加氧酶；Mutter 2021 以专用环裂解酶敲除证实该路径为近期进化的专用产物。该原型为 approach-1 机制匹配（真实降解菌的真实降解酶），仿生真实性优于毒性受体几何（AhR）。

**仿生转译**（来源方案 SL11，score 69）：取 RW1 角位双加氧酶的醚骨架识别几何，转译为水相虚拟模板 MIP。模板为几何同源水溶物（取代二苯醚/氧杂蒽衍生物），醚氧锚定点 + 角位轮廓窗口区分 TCDD（二芳醚）与 PCB-126（联苯，无醚氧）及 PCDF（呋喃，角位/氧数不同）。诚实边界：取识别几何、非氧合催化。

## 2. 吸附机制详解

### 机制1：醚氧锚定点

**描述**：MIP 腔内预组织氢键/偶极供体对二芳醚醚氧执行弱锚定。醚氧为弱给体、邻位氯部分屏蔽，水相锚定强度须论证超水合竞争
**关键官能团**：MIP 腔内氢键供体阵列（脲/硫脲/酰胺）
**来源**：DOI 10.1128/aem.58.3.1005-1012.1992 (Wittich 1992)

### 机制2：角位轮廓窗口

**描述**：MIP 腔的角位轮廓窗口按 Å 级几何区分二芳醚（TCDD，角位邻氧）、联苯（PCB，无醚氧）、呋喃（PCDF，角位/氧数不同）
**关键官能团**：MIP 腔壁几何轮廓
**来源**：DOI 10.1128/aem.02464-20 (Mutter 2021)

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | MIP 颗粒填充床 | 50–200 µm | 固定床吸附 |
| 介观 | 介孔孔道 | 2–50 nm | 传质 |
| 微观 | MIP 印迹腔 | ~1 nm | 醚骨架几何识别 |
| 纳米 | 醚氧-供体氢键 | ~1.8–2.5 Å | 锚定 |

### 结构-功能关系

**功能**：TCDD 对 PCB-126 与 PCDF 的骨架判别
**结构基础**：虚拟模板 MIP 记忆醚骨架几何 + 角位轮廓窗口
**物理原理**：醚氧锚定（弱识别维度）+ 角位轮廓（几何判别）
**关键参数**：α(TCDD/PCB-126)、α(TCDD/PCDF)

**仿生制造启示**：
- 水相虚拟模板 MIP（模板 = 取代二苯醚/氧杂蒽衍生物）
- 功能单体：氢键供体（脲/硫脲/酰胺硅烷）
- 交联：TEOS 或有机交联剂

## 4. 已报道性能数据

> 来源方案 SL11 设计目标（实验待验证）

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| TCDD | MIP | — | pg/L 级设计靶标 | 7 | 25 | SL11 工程设计值 | 方案修订版 |

## 5. 适用场景

**最适合**：土壤/沉积物提取液中 TCDD 对 PCB/PCDF 的选择性捕获研究；二噁英骨架判别机制验证
**不适用**：pg/L 级超痕量水相直接捕获（MIP 记忆效应 + Kd 要求极高）；高 DOM 基质
**约束条件**：
- TCDD 溶解相 pg/L 级，MIP 须排除模板共洗脱/记忆效应
- 醚氧水相弱识别（弱给体 + 邻位氯屏蔽），锚定强度须论证超水合
- 角位轮廓窗口 Å 级实现难

## 6. 相关原型

- pxr-xenobiotic-receptor-promiscuity：PXR 大软腔（TCDD 几何备选原型，但为毒性受体）
- gaba-rdl-rigid-hydrophobic-cavity：GABA/Rdl 刚性疏水腔（中性笼状分子识别类比）

## 参考文献

[1] Wittich M, et al. Appl Environ Microbiol. 1992;58(3):1005-1012. DOI 10.1128/aem.58.3.1005-1012.1992
[2] Wilkes H, et al. Arch Microbiol. 1996;166:100-109. DOI 10.1007/s002030050357 (PMC1388763)
[3] Mutter M, et al. Appl Environ Microbiol. 2021;87:e02464-20. DOI 10.1128/aem.02464-20
[4] SL11 方案修订版 (score 69). rounds/fresh_1000/tcdd/SCHEMES/SL11_A04_aryl-ether-angular-profile-virtual-template-MIP_r1-revise.md
