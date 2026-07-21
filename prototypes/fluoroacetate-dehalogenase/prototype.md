---
id: fluoroacetate-dehalogenase
name: 氟乙酸脱卤酶（Fluoroacetate Dehalogenase）（Fluoroacetate Dehalogenase (FAcD, EC 3.8.1.3)）
category: 微生物
organism: Rhodopseudomonas palustris CGA009（RPA1163 氟乙酸脱卤酶）；同源原型 Burkholderia sp. FA1（FAcD）
biomimetic_dimension: 分子仿生
features:
  - 催化降解
adsorption_mechanisms:
  - Asp-His-Asp 催化三联体对氟乙酸 C-F 键的 SN2 水解脱氟
  - 卤素洞三氢键对离去氟离子的稳定化与氟选择性
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 11 verified, 0 unverified
# coverage: partial
# status: active
---
# 氟乙酸脱卤酶（Fluoroacetate Dehalogenase）（Fluoroacetate Dehalogenase (FAcD, EC 3.8.1.3)）

## 1. 生物原型简介

**问题定义**：C-F 键是有机化学中最强的共价键，生物体系中能断裂该键的酶极少。氟乙酸脱卤酶（FAcD，EC 3.8.1.3）可在温和生理条件下将氟乙酸水解为乙醇酸并释放氟离子，其分子机制是生物脱氟的基础问题，也是设计针对更复杂氟化有机物（含全氟化合物）脱氟体系的原理源头。

**生物策略**：Rhodopseudomonas palustris CGA009 的 RPA1163 为 α/β 水解酶折叠，催化三联体 Asp110（亲核体）、His280（碱）、Asp134（羧酸）埋藏于结构域界面，经约 11 Å 通道与溶剂相通（PMC3101105）。Chan 2011 以 1.15–1.80 Å 系列结构捕获游离酶、酶-氟乙酸 Michaelis 复合物、乙醇酰-酶共价中间体与酶-产物复合物四态：Asp110 对底物 C2 作 SN2 攻击直接排出氟离子，生成乙醇酰-Asp110 酯，再由 His280/Asp134 活化水分子水解酯键释放乙醇酸。卤素洞（His155、Trp156、Tyr219）提供三个氢键稳定离去氟离子，其空腔专为较小氟原子裁剪；His155 咪唑环具受控柔性，His155Asn/Tyr219Phe 突变可扩大空腔并使氯乙酸活性升至氟乙酸的 8 倍。同源酶 Burkholderia sp. FA1 FAcD（PDB 1Y37，1.5 Å）活性位点组成与排布高度保守。该酶执行的是降解/转化（水解脱氟），而非吸附。

## 2. 吸附机制详解

### 机制1：Asp-His-Asp 催化三联体对氟乙酸 C-F 键的 SN2 水解脱氟

**描述**：RPA1163 氟乙酸脱卤酶（α/β 水解酶折叠）以两阶段机制催化氟乙酸（FCH2COO⁻）水解脱氟：Asp110 侧链羧基对底物 C2 作 SN2 亲核攻击，直接排出氟离子，生成乙醇酰-Asp110 酯共价中间体；随后 His280/Asp134 活化水分子水解该酯键，释放产物乙醇酸并再生游离酶。催化三联体（Asp110 亲核体、His280 碱、Asp134 羧酸）埋藏于结构域界面，经长约 11 Å 的通道进入（RPA1163 编号；与 Burkholderia sp. FA1 FAcD 活性位点组成相同、排布保守）
**关键官能团**：['羧基亲核体（Asp110 侧链 COO⁻）', '咪唑碱（His280）与羧酸（Asp134）电荷中继', '卤素洞氢键给体（Arg111、Trp156、His155、Tyr219）']
**来源**：DOI 10.1021/ja200277d

### 机制2：卤素洞三氢键对离去氟离子的稳定化与氟选择性

**描述**：活性位点卤素洞（His155、Trp156、Tyr219 等）提供三个氢键稳定离去氟离子，其空腔容积专为较小的氟原子裁剪，从而建立对氟化底物的选择性；His155 咪唑环具有柔性弹性可让出空间，His155Asn/Tyr219Phe 突变可扩大卤素洞并反转卤素偏好（氯乙酸活性升为氟乙酸的 8 倍）
**关键官能团**：['卤素洞氢键给体（His155、Trp156、Tyr219）', '色氨酸吲哚环（Trp185 动态隔水）']
**来源**：DOI 10.1021/ja200277d

## 3. 结构特征与结构-功能关系

必须保留：① 羧基亲核体（SN2 攻击 C-F）；② 咪唑碱/羧酸电荷中继（活化水、水解酯中间体）；③ 多氢键卤素洞（稳定离去氟离子）；④ 与氟原子半径匹配的空腔几何（卤素选择性）；⑤ 埋藏隔水微环境。可灵活调整：蛋白骨架、口袋残基（可经突变重编程选择性）、载体形式。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 天然底物尺寸与化学特异性: 天然底物为二碳单氟乙酸（FCH2COO⁻，EC 3.8.1.3）；C-F 键是有机化学中最强的共价键，FAcD 是自然界少数能在温和水相条件下水解该键的酶 None
- 可溶蛋白与埋藏活性位点: α/β 水解酶折叠；活性位点埋藏于结构域界面，仅经长约 11 Å 的通道可达；PDB 1Y37 不对称单元含 A/B 链，RCSB 报告条目分子量 68.31 kDa；吸附应用需固定化或全细胞部署 None
- 卤素洞对氟原子的空间适配: 卤素洞专为较小氟原子裁剪，对较大卤代乙酸活性显著下降（尽管其 C-X 键更弱）；His155Asn/Tyr219Phe 突变可扩大卤素洞并反转卤素偏好 None

## 6. 相关原型

- iron-oxidizing-bacteria
- magnetic-bacteria

## 参考文献

[待补充]
