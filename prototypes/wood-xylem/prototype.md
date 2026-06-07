---
id: wood-xylem
name: 木材木质部（Wood Xylem）
category: 植物
organism: Limonia acidissima
biomimetic_dimension: 结构仿生
features:
  - 大孔
  - 层次孔
adsorption_mechanisms:
  - 吸附机制——分子态酚+静电排斥
  - 共价交联网络的XPS证据
  - 吸附机制：氨基配位螯合
  - TCTGAs组分与合成工艺
qmax_range: "2.0-571.0 mg/g"
applicability:
  pH_range: [6.0, 6.0]
  temp_range: null
  salinity: low
evidence_level: low
# provenance: 2 papers, 0 verified, 7 unverified
# coverage: normal
# status: active
---
# 木材木质部（Wood Xylem）

## 1. 生物原型简介

**问题定义**：自然界中植物果壳需形成抗降解的致密复合结构以保护内部组织；对应水处理中面临低浓度酚类及卤代酚类污染物的高效、低成本去除难题。

**生物策略**：木苹果壳在进化中形成纤维素/半纤维素/木质素三组分天然结构，经碳化后保留稳定的芳香碳骨架与丰富含氧官能团，提供多机制吸附位点；结合绿色物理球磨细化策略，成功实现120 min内快速吸附平衡，对2,4-DCPh吸附容量达226.55 mg/g。

## 2. 吸附机制详解

### 机制1：吸附机制——分子态酚+静电排斥

**描述**：pH<pKa时分子态酚占优→利于吸附；高pH酚酸根阴离子→与负电荷WAS-BC排斥
**来源**：DOI 10.1038/s41598-021-82277-2

### 机制2：共价交联网络的XPS证据

**描述**：XPS C 1s确认C-N键形成→TMPTAP成功交联TCNF和GO。N 1s吸附后偏移：Pb²⁺@TCTGAs 399.2, Cu²⁺@ 399.2, Zn²⁺@ 399.4, Cd²⁺@ 399.2, Mn²⁺@ 399.1 eV(vs原始398.9 eV)→N孤对电子与金属离子形成配位键
**关键官能团**：NH3+, -NH2, -NH- responsible for divalent metal cation adsorption (HSAB)
**来源**：DOI 10.1016/j.jhazmat.2021.125612

### 机制3：吸附机制：氨基配位螯合

**描述**：XPS确认N 1s偏移(398.9→399.1-399.4 eV)→N孤对电子与金属离子形成配位键。O 1s也偏移→含氧官能团参与吸附。EDX mapping确认Pb/Cu/Zn/Cd均匀分布。机制：NH3+/NH2/NH-基团与重金属离子螯合/配位
**关键官能团**：NH3+, -NH2, -NH- → borderline base → complex borderline acids (Pb²⁺, Cu²⁺, Zn²⁺)
**来源**：DOI 10.1016/j.jhazmat.2021.125612

### 机制4：TCTGAs组分与合成工艺

**描述**：TCNF(TEMPO氧化纤维素纳米纤维)+GO(改良Hummers法)+TMPTAP(三(2-氨基乙基)胺-聚丙二醇→交联剂+金属螯合配体)。Zr/BDC/OA比例不适用→但TCNF/GO/TMPTAP混合→超声分散→定向冷冻→冻干
**来源**：DOI 10.1016/j.jhazmat.2021.125612

## 3. 结构特征与结构-功能关系

必须保留：天然生物质碳化衍生的芳香碳骨架、纳米级多孔形貌、表面-OH/-COOH/C=O官能团；可灵活调整：球磨强度与时间（调控粒径与比表面积）、热解温度（调控孔隙与官能团比例）、表面化学修饰（靶向增强卤素-π或疏水作用）。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
|  | WAS-BC | 苯酚102.71、4-CPh 172.2 | 6.0 | literature: 10.1038/s41598-021 | ❓ |
|  |  | 2,4-DCPh(二氯) > 4-CPh | - | literature: 10.1038/s41598-021 | ❓ |
|  |  | Pb(II) 571, Cu(II) 4 | - | literature: 10.1016/j.jhazmat. | ❓ |

## 5. 适用场景

**约束条件**：
- TGA热稳定性分析: 生物质200-750°C主要热解；生物炭500°C仅~10wt%质量损失→高温稳定 °C
- 再生性能与循环稳定性: 0.05 mol/L EDTA-2Na洗脱，25°C，3h。5次循环后保持良好吸附性能。可制成压缩过滤装置原型 None
- 水下力学稳定性: TCTGAs在水下表现出优异的力学结构稳定性→有利于水处理中的循环回收。普通冷冻法制备的气凝胶无法承受大变形 None

## 6. 相关原型

- bone-structure
- coral-skeleton
- iron-oxidizing-bacteria
- metal-organic-framework
- oyster-shell

## 参考文献

[1] DOI: 10.1016/j.jhazmat.2021.125612
[2] DOI: 10.1038/s41598-021-82277-2
