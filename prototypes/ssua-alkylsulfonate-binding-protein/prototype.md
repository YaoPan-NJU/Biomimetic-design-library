---
id: ssua-alkylsulfonate-binding-protein
name: SsuA 烷基磺酸盐结合蛋白（SsuA Alkanesulfonate-Binding Protein）
category: 微生物
organism: Xanthomonas citri subsp. citri 306
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 分子筛分
adsorption_mechanisms:
  - 磺酸头基多齿氢键定位与宽疏水口袋协同识别
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 1 papers, 4 verified, 0 unverified
# coverage: full
# status: active
---
# SsuA 烷基磺酸盐结合蛋白（SsuA Alkanesulfonate-Binding Protein）

## 1. 生物原型简介

Xanthomonas citri 的 SsuA 是烷基磺酸盐 ABC 摄取系统的周质底物结合蛋白。配体结合结构显示，两个结构域在界面形成可闭合裂隙：磺酸头基由多个主链酰胺 NH、Gln 侧链和 Ser 羟基定向定位，有机尾部则进入含疏水残基和保守水分子的宽口袋。该体系证明了“头基多点几何锚定 + 尾部受限容纳”的天然识别组合，但没有证明 SsuA 可直接结合 PFBS，也没有吸附容量、真实水体选择性或再生数据。因此本库保留天然机制为事实，把 PFBS 材料映射严格放在 exploratory 层。

## 2. 吸附机制详解

### 机制1：磺酸头基多齿氢键定位与宽疏水口袋协同识别

**描述**：X. citri SsuA 的两个结构域在界面形成可闭合裂隙。配体磺酸氧与 Gly68、Gly86、Ser141 的主链 NH、Gln36 侧链 NH 和 Ser141 羟基形成多点极性相互作用；水分子与疏水残基参与稳定不同大小和形状的烷基部分。该结构解释了 SsuA 对多种烷基磺酸盐的识别，同时不等同于对无机硫酸根或全氟磺酸盐的已验证结合。
**关键官能团**：['主链酰胺 NH', 'Gln 侧链酰胺', 'Ser 羟基', '口袋疏水残基']
**来源**：DOI 10.1371/journal.pone.0080083

## 3. 结构特征与结构-功能关系

| 结构层级 | 已接地特征 | 功能含义 |
|---|---|---|
| 蛋白整体 | 两结构域在界面形成结合裂隙，配体位于口袋内 | 通过域运动实现受限包埋，而非暴露表面吸附 |
| 头基位点 | Gly68、Gly86、Ser141 主链 NH，Gln36 侧链 NH 与 Ser141 羟基 | 对磺酸氧提供多点、方向性的极性定位 |
| 尾部区域 | 宽口袋、至少十二个疏水残基和保守水 | 容纳不同大小和形状的烷基磺酸盐，但不证明全氟尾兼容 |

材料转译必须同时保留头基位点的预组织几何、口袋的低极性限域和尾部占位；只增加脲/胺密度不能视为复现 SsuA。

## 4. 已报道性能数据

本条没有材料去除性能记录。`performance_data` 为空；蛋白结合与细菌摄取不能换算为吸附容量、去除率、选择性或循环稳定性。

## 5. 适用场景

**约束条件**：
- 可溶周质蛋白形态：SsuA 本身不是可直接投加的耐用吸附介质；若采用蛋白路线需定向固定并验证活性保持、泄漏和寿命。
- 多齿几何与微环境必须共同复现：仅增加脲或胺密度不能等价于 SsuA；给体取向、口袋低极性和尾部容积均需受控。

**探索性材料映射**：受限口袋中的预组织脲/酰胺给体阵列可用于检验 PFBS 磺酸头基定位，但必须以头基阻断、随机给体、烷基磺酸盐和真实水体竞争对照拆分作用。全氟尾相容性未验证。

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- bug-family-carboxylate-pincer
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation

## 参考文献

[1] Tófoli de Araújo F, et al. *PLoS ONE*. 2013;8:e80083. DOI: 10.1371/journal.pone.0080083. PDB: 3E4R, 3KSJ, 3KSX.
