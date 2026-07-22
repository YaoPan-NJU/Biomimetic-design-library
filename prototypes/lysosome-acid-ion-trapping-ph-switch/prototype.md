---
id: lysosome-acid-ion-trapping-ph-switch
name: 溶酶体酸性离子捕获（pH 质子化态依赖陷获）（Lysosomal Acid Ion Trapping (pH Protonation-State-Dependent Trapping)）
category: 动物
organism: Rattus norvegicus / Mus musculus（溶酶体，细胞器级；经典模型为大鼠肝溶酶体与小鼠腹膜巨噬细胞，无单一蛋白结构）
biomimetic_dimension: 功能仿生
features:
  - pH 响应
  - 动态响应
adsorption_mechanisms:
  - 弱电解质质子化态依赖的跨膜离子陷获（lysosomotropism，酸性陷获）
  - 溶酶体酸性腔室的建立与维持（V-ATPase 质子泵，pH 4.5–5.0）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 4 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 溶酶体酸性离子捕获（pH 质子化态依赖陷获）（Lysosomal Acid Ion Trapping (pH Protonation-State-Dependent Trapping)）

## 1. 生物原型简介

**问题定义**：细胞须在中性胞质中维持酸性溶酶体腔以激活水解酶并处理内吞底物；弱电解质在跨膜 pH 梯度下如何随质子化态发生跨膜分配并被酸性腔室选择性截留，是细胞器级的物理化学问题，也构成自然界 pH 梯度驱动捕获/释放的原型。

**生物策略**：溶酶体膜 V 型 ATPase 以 ATP 代谢能泵质子入腔，反离子流动耗散跨膜电压，建立稳态腔内 pH 4.5–5.0（Mindell 2012）。Ohkuma 与 Poole 1978 以荧光素异硫氰酸酯标记葡聚糖（FD）探针首次在活巨噬细胞中定量测得腔内 pH 4.7–4.8（瞬时可低至 4.5），发现弱碱使腔内 pH 快速升高，并为「弱碱经质子陷获在溶酶体累积」的理论提供证据（摘要原文 support the theory of lysosomal accumulation of weak bases by proton trapping）。Ohkuma 与 Poole 1981 进一步证明：培养基 pH 不影响腔内 pH，弱碱的活性形态为中性未质子化形式，其累积浓度依赖性地升高腔内 pH，结果被诠释为能量依赖的溶酶体酸化与质子以质子化弱碱形式漏出。de Duve 1974 将此类在溶酶体累积的弱碱命名为溶酶体向性剂（lysosomotropic agents）。

## 2. 吸附机制详解

### 机制1：弱电解质质子化态依赖的跨膜离子陷获（lysosomotropism，酸性陷获）

**描述**：溶酶体腔经 V-ATPase 维持 pH 4.5–5.0；弱碱（溶酶体向性胺类，天然陷获底物）以中性未质子化形态透过溶酶体膜，在酸性腔内质子化带电荷后不能自由回渗而累积，即质子陷获（proton trapping）/离子陷获；Ohkuma 1981 证明弱碱的活性形态为中性未质子化形式，其累积使腔内 pH 浓度依赖性升高，可诠释为质子以质子化弱碱形式漏出溶酶体。该机制是自然界 pH 梯度驱动捕获/释放的原型
**关键官能团**：['可电离弱碱基团（胺类，可质子化）', '溶酶体膜双分子层屏障（对带电形态不通透）', 'V-ATPase 质子泵（梯度源）']
**来源**：DOI 10.1073/pnas.75.7.3327

### 机制2：溶酶体酸性腔室的建立与维持（V-ATPase 质子泵，pH 4.5–5.0）

**描述**：溶酶体为内吞途径末端细胞器；膜上 V 型 ATPase 以 ATP 代谢能泵质子入腔，反离子流动耗散跨膜电压（ClC-7 Cl⁻/H⁺ 反向转运体可能参与），建立并维持稳态腔内 pH 4.5–5.0；该酸性腔室激活水解酶并为质子化态依赖的离子陷获（LYST-001）提供梯度驱动力。Ohkuma 1978 以荧光素异硫氰酸酯标记葡聚糖探针在活细胞中直接测得腔内 pH 4.7–4.8
**关键官能团**：['V 型 ATPase 质子泵', '反离子通道/转运体（ClC-7 Cl⁻/H⁺ 反向转运体）', '溶酶体膜双分子层']
**来源**：DOI 10.1146/annurev-physiol-012110-142317

## 3. 结构特征与结构-功能关系

必须保留：① pKa 落于摆动两 pH 之间、两形态在电荷与界面亲和上差异显著的可电离单元（天然为弱碱胺类，捕获在酸性侧）；② 可维持的 pH 差（天然由 V-ATPase 主动维持，体外由外部酸碱摆动维持）；③ 对带电形态的截留屏障（天然为膜双分子层，体外为吸附位点与选择性屏障）。可灵活调整：载体骨架、识别位点类型（阳离子/阴离子交换/氢键 π 协同）、摆动操作方式与区室构型。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 细胞器级现象，无蛋白结构接地: 溶酶体酸性离子捕获是 V-ATPase 泵质子、膜双分子层屏障与弱电解质酸碱分配综合作用的细胞器级理化现象，不可归于单一蛋白结合位点，无 PDB 结构接地，无法以分子识别蛋白方式移植，仅原理层（pH 梯度+质子化态依赖分配）可转译 None
- 捕获方向酸碱反转: 天然离子陷获为弱碱的酸性陷获（低 pH 捕获）；2,6-DCP 为弱酸，转译方向相反，偏碱酚盐阴离子被阳离子/阴离子识别位捕获、偏酸质子化中性酚释放，吸附位点须以阳离子型阴离子识别单元匹配 None
- pH 摆动窗口须跨越目标 pKa: 2,6-DCP 酚羟基 pKa ≈ 6.8（简报常用文献值，本条目未经全文核验，实验前须以电位法或分光法复核）；捕获 pH（偏碱，酚盐阴离子）与再生 pH（偏酸，中性酚）须跨越该 pKa，摆动幅度直接决定吸附-脱附驱动力 pH
- 梯度维持方式: 天然腔内 pH 4.5–5.0 由 V-ATPase 主动泵质子与代谢能维持，且糖酵解与氧化磷酸化同时受抑方可使腔内 pH 升高；体外无主动质子泵，须以外部酸碱加药或双区室操作构建 pH 摆动，并计及试剂消耗与循环成本 None

## 6. 相关原型

- fcrn-ph-dependent-fc-recycling
- hemoglobin-bohr-ph-allostery
- mscl-mechanosensitive-channel
- natural-dna-imotif-gquadruplex-switch
- natural-riboswitch-metabolite-sensing

## 参考文献

[待补充]
