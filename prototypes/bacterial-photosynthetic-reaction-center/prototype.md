---
id: bacterial-photosynthetic-reaction-center
name: 紫色细菌光合反应中心（电子互补预组织 → 供体-受体电荷转移识别腔）（Purple Bacterial Photosynthetic Reaction Center (Donor-Acceptor CT Recognition Cavity)）
category: 微生物
organism: Rhodopseudomonas viridis / Blastochloris viridis（紫色细菌光合反应中心，Deisenhofer 1985 晶体结构）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
pollutants:
  - 奥克立林
  - octocrylene
  - OC
adsorption_mechanisms:
  - 富电子 π 供体面与电子亏缺核的供体-受体电荷转移（CT）识别
  - 孔壁电子密度同拓扑三成员梯度（D/N/A）因果归因
  - 疏水预浓缩 + CT 选择性分层
qmax_range: "设计目标 q_m(OC) ≥ 20 mg/g（实验待验证）"
applicability:
  pH_range: [3, 11]
  temp_range: [10, 40]
  salinity: low_to_moderate
evidence_level: medium
coverage: full
source_scheme: S34_A01 (OC, score 85, passed) — 供体-受体 CT 识别腔
---
# 紫色细菌光合反应中心（电子互补预组织 → 供体-受体电荷转移识别腔）

## 1. 生物原型简介

**问题定义**：紫色细菌光合反应中心（RC）是自然界最精密的电子转移装置之一。Deisenhofer 1985 解析了其晶体结构（诺贝尔化学奖 1988），揭示特殊对（special pair）两个细菌叶绿素分子周围精确排列富电子 π 供体面，实现电子互补选择性耦合。

**生物策略**：RC 以精确空间几何预组织富电子 π 供体面（细胞色素 c 亚基、细菌叶绿素、细菌脱镁叶绿素），使光驱电荷分离沿确定方向高效进行。Moser-Dutton 距离标度律（PMID 1311417，被引 2483）确认距离为定义电子转移速率与方向性的充分参数之一。

**仿生转译**（来源方案 S34，score 85）：将 RC 电子互补预组织原理转译为多孔骨架孔壁预组织富电子芳香供体面，对 OC 的 α-氰基-二苯基丙烯酸酯核（π 电子受体）执行水相 CT 识别。诚实标注：RC 功能为光驱电荷分离而非吸附，转译距离大；水相 CT 幅度为未证赌注。

## 2. 吸附机制详解

### 机制1：富电子 π 供体面与电子亏缺核的 CT 识别

**描述**：OC 的 α-氰基-二苯基丙烯酸酯核为 π 电子受体（氰基致双键电子亏缺，kO3 OC 1.58 vs EHMC 5.25×10⁴ M⁻¹s⁻¹，低约 3.3×10⁴ 倍）。S34 方案以 β-酮烯胺 COF 孔壁预组织富电子芳香供体面，通过 CT 相互作用识别电子亏缺核
**关键官能团**：烷氧供体壁（D 端）/ TTF（起始氧化电位 +0.34 V vs Ag/AgCl，强 π 供体）
**来源**：DOI 10.1038/318449a0 (Deisenhofer 1985), PubMed PMID 28535480 (Hopkins 2017 kO3)

### 机制2：孔壁电子密度同拓扑三成员梯度因果归因

**描述**：D（供体壁）/N（中性壁）/A（受体壁）近同拓扑三成员，以 α(OC/EHMC) 在三人上的序关系为核心因果对照区分 CT 贡献与疏水基线。供体强度单调且疏水解耦成立为必要判据
**关键官能团**：D=烷氧供体壁 / N=中性壁 / A=非联苯胺电子贫壁
**来源**：DOI 10.1021/ja308278w (COF 平台), DOI 10.1021/ja308278w (β-酮烯胺水稳 COF)

### 机制3：疏水预浓缩 + CT 选择性分层

**描述**：第一层疏水预浓缩（前置、非选择性来源，OC logKow~6.1–7.5）；第二层腔内 CT（选择性来源，主判据）；第三层刚性有限腔几何窗口（使能，几何协同）
**关键官能团**：疏水孔壁 + 富电子供体面
**来源**：方案 S34 通过版

## 3. 结构特征与结构-功能关系

### 多尺度结构描述

| 尺度 | 特征 | 尺寸范围 | 功能作用 |
|------|------|----------|----------|
| 宏观 | COF/分子笼颗粒填充床 | 1–100 µm | 固定床吸附 |
| 介观 | COF 周期孔道 / 笼窗口 | 2–50 nm | 传质 + 几何窗口 |
| 微观 | 孔壁电子密度梯度 | ~0.3–1 nm 孔壁 | CT 选择性 |
| 纳米 | 供体面-OC 核 CT 相互作用 | ~3–5 Å | 电子互补识别 |

### 结构-功能关系

**功能**：OC 对 EHMC 的 CT 选择性捕获（α(OC/EHMC) ≥ 3），对 logKow 非单调
**结构基础**：孔壁富电子 π 供体面与 OC 电子亏缺核的 CT 相互作用
**物理原理**：电子互补预组织使 CT 自由能增量最大化；同拓扑三成员梯度排除纯疏水归因
**关键参数**：α(OC/EHMC) ≥ 3（D 端）；供体强度单调且疏水解耦成立；OC/HHCB 疏水解耦 α ≥ 2

**仿生制造启示**：
- 主平台：β-酮烯胺水解稳定 COF（D/N/A 三成员）
- 供体强化：TTF-COF（TTF 起始氧化电位 +0.34 V）
- 第三验证格式：离散亚胺分子笼（Cooper 型，孔径解耦电子梯度对照）

## 4. 已报道性能数据

> 来源方案 S34 设计目标（实验待验证）

| 污染物 | 材料形态 | 去除率 | qmax (mg/g) | pH | 温度(°C) | 数据来源 | 文献 |
|--------|----------|--------|-------------|-----|----------|----------|------|
| OC | β-酮烯胺 COF | ≥80%（S2 二级出水） | ≥20（设计目标） | 3–11 | 25 | S34 工程设计值 | 方案通过版 |

## 5. 适用场景

**最适合**：紫外过滤剂选择性研究（OC vs EHMC）；供体-受体 CT 水相识别机制研究
**不适用**：需完全矿化 OC 的场景；高 DOM 芳组分基质（π-π 竞争）
**约束条件**：
- RC 功能为光驱电荷分离而非吸附，转译距离大
- 水相 CT 幅度为未证赌注（Stage −1 DFT-SAPT 计算门前置）
- 论文措辞禁称"CT 选择性水相捕获全球首例"（碘/硝基芳烃主题已占用）
- ng/L 床层性能显式依赖预浓缩协作

## 6. 相关原型

- polydopamine-coating：聚多巴胺涂层（富电子吲哚/儿茶酚面，CT 原理旁证）
- plant-tannin：植物单宁（富电子酚面，CT 原理旁证）

## 参考文献

[1] Deisenhofer J, et al. Nature. 1985;318:449. DOI 10.1038/318449a0
[2] Allen JP, et al. Nature. 1987;326:825. DOI 10.1038/326825a0
[3] Moser CC, et al. Nature. 1992;355:796. PMID 1311417
[4] Hopkins GW, et al. Environ Sci Technol. 2017. PubMed PMID 28535480
[5] Canevet D, et al. Chem Commun. 2009. DOI 10.1039/b820692b (TTF 氧化电位)
[6] S34 方案通过版 (score 85). rounds/fresh_1000/octocrylene/SCHEMES/S34_A01_donor-acceptor-CT-cavity_passed.md
