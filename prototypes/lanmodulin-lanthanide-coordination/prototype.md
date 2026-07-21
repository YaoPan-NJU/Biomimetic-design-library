---
id: lanmodulin-lanthanide-coordination
name: Lanmodulin 镧系结合蛋白（LanM）（Lanmodulin Lanthanide-Binding Protein (LanM)）
category: 微生物
organism: Methylorubrum extorquens AM1（lanmodulin, LanM；兼引 Hansschlegelia quercus LanM 同源蛋白）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
adsorption_mechanisms:
  - EF-hand 预组织羧酸配位几何对 Ln³⁺ 的选择性识别
  - 第二配位层羧酸位移对 Ln³⁺ 半径的读出与金属敏感二聚化
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 11 verified, 2 unverified
# coverage: partial
# status: active
---
# Lanmodulin 镧系结合蛋白（LanM）（Lanmodulin Lanthanide-Binding Protein (LanM)）

## 1. 生物原型简介

**问题定义**：稀土离子化学性质高度相似、分离困难；甲基营养菌需在钙离子丰富的环境中特异性捕获镧系离子以供给甲醇脱氢酶等酶功能。蛋白如何以预组织配位几何在结构相似的阳离子间建立超高选择性，是分子识别与分离的基础问题。

**生物策略**：Methylorubrum extorquens AM1 周质蛋白 Lanmodulin 以四个 EF-hand 基序的高密度羧酸配位口袋结合 Ln3+/Y3+：Y3+ 复合物溶液 NMR 结构（PDB 6MI5）呈紧凑融合 EF-hand 折叠；摘要直陈其发生金属依赖的构象变化且对 Ln3+ 与 Y3+ 相对 Ca2+ 具 10^8 倍选择性，额外羧酸配体贡献皮摩尔级亲和力（Cook 2019）。Hansschlegelia quercus 同源 LanM 结合 Ln3+ 后二聚化，二聚强度对离子半径敏感（La3+ 诱导二聚体比 Dy3+ 紧逾 100 倍）；皮米级半径差异经羧酸位移重排第二配位层氢键网络而传递至四级结构（Mattocks 2023 Nature；PDB 8FNS Nd3+、8DQ2 La3+，均于 pH 7 结合态测定）。

## 2. 吸附机制详解

### 机制1：EF-hand 预组织羧酸配位几何对 Ln³⁺ 的选择性识别

**描述**：Lanmodulin（Methylorubrum extorquens AM1，117 残基，约 12.5 kDa，周质）含四个 EF-hand 基序，以高密度羧酸配体（Asp/Glu 侧链羧基与骨架羰基氧）预组织配位口袋结合 Ln3+/Y3+；Y3+ 复合物溶液 NMR 结构为 PDB 6MI5；结合耦合金属依赖的折叠构象变化，对 Ln3+ 与 Y3+ 相对 Ca2+ 的选择性达 10^8 倍，亲和力达皮摩尔级
**关键官能团**：['羧酸配体（Asp/Glu 侧链羧基）', '骨架羰基氧', 'EF-hand 环区预组织配位口袋']
**来源**：DOI 10.1021/acs.biochem.8b01019

### 机制2：第二配位层羧酸位移对 Ln³⁺ 半径的读出与金属敏感二聚化

**描述**：Hansschlegelia quercus LanM（Hans-LanM）结合 Ln3+ 后形成二聚体，二聚强度对 Ln3+ 离子半径敏感（La3+ 诱导二聚体比 Dy3+ 诱导二聚体紧逾 100 倍）；X 射线结构（PDB 8FNS Nd3+、PDB 8DQ2 La3+，均于 pH 7 结合态测定）显示皮米级离子半径差异经配位层羧酸位移（carboxylate shift）重排第二配位层氢键网络而传递至四级结构；原型 Methylorubrum extorquens AM1 LanM 的 Nd3+ 结合结构为 PDB 8FNS
**关键官能团**：['羧酸配体（第一配位层与羧酸位移）', '第二配位层氢键网络', '二聚界面残基']
**来源**：DOI 10.1038/s41586-023-05945-5

## 3. 结构特征与结构-功能关系

必须保留：① 与硬三价阳离子几何互补的预组织高密度羧酸配位口袋（EF-hand 式）；② 第二配位层氢键网络对配位几何微调的读出；③ 金属依赖折叠与 pH 依赖可逆性；④ 细微几何差异向超分子/宏观结合强度的放大。可灵活调整：载体骨架、配体种类与密度、pH 摆动区间。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶周质小蛋白形态: LanM 为 Methylorubrum extorquens AM1 周质可溶性蛋白（117 残基，约 12.5 kDa），识别基序需移植/固定于固体载体方可用于吸附 None
- 硬阳离子特异性: 天然 EF-hand 羧酸口袋面向 Ln3+/Y3+ 硬阳离子；用于 PFOA 羧酸根阴离子识别须转换为金属桥联或阳性锚定位点模式（原理层外推） None
- pH 依赖性结合/释放: 金属结合态结构于 pH 7 测定（PDB 8FNS/8DQ2）；低 pH 释放的具体阈值未做全文审计，pH 摆动再生设计为定性外推 None
- 第二配位层与寡聚界面完整性依赖: 半径读出与二聚化放大依赖第二配位层氢键网络与二聚界面的完整；羧酸位移突变或界面扰动将改变选择性谱 None

## 6. 相关原型

- fcrn-ph-dependent-fc-recycling
- hsa-fatty-acid-pfas-binding
- kcsa-potassium-channel-selectivity-filter
- ntcp-bile-acid-pfas-transporter
- psts-phosphate-binding-protein

## 参考文献

[待补充]
