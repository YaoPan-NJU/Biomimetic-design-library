---
id: acidimicrobium-reductive-defluorination
name: Acidimicrobium sp. A6 还原脱氟微生物原型（Acidimicrobium sp. Strain A6 Reductive Defluorination Prototype）
category: 微生物
organism: Acidimicrobium sp. strain A6（铁还原偶联铵氧化自养菌，Feammox；可还原脱氟）；结构先例还原脱卤酶来自 Nitratireductor pacificus pht-3B（PDB 4RAS）
biomimetic_dimension: 分子仿生
features:
  - 催化降解
adsorption_mechanisms:
  - 厌氧还原条件下 Acidimicrobium sp. A6 对 PFOA/PFOS 的还原脱氟
  - B12（咕啉）依赖型还原脱卤酶作为还原性碳-卤键断裂的结构先例
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 9 verified, 0 unverified
# coverage: partial
# status: active
---
# Acidimicrobium sp. A6 还原脱氟微生物原型（Acidimicrobium sp. Strain A6 Reductive Defluorination Prototype）

## 1. 生物原型简介

**问题定义**：PFOA 与 PFOS 等全氟烷基物质因全氟碳骨架极难被破坏而在环境中高度持久，常规处理难以断裂其 C-F 键。自然界是否存在能攻击全氟烷基 C-F 键的生物过程，是 PFAS 去除的基础问题。Acidimicrobium sp. strain A6 是一种可营 Feammox（铁还原偶联铵氧化）的化能自养菌，被发现可在厌氧还原条件下对 PFOA/PFOS 还原脱氟，属降解/转化类生物原型，而非吸附识别类原型。

**生物策略**：Huang & Jaffe（2019）以 A6 纯培养与富集培养在 0.1 与 100 mg/L 两浓度孵育 PFOA 或 PFOS：观察到氟离子累积、更短链全氟化产物与乙酸生成，以及单位铵氧化所还原 Fe(III) 的下降；以氢为唯一电子供体时同样发生脱氟。百日孵育中 PFOA/PFOS 至多约六成被去除，期间总氟（有机氟加氟离子）守恒，证明发生了还原性 C-F 键断裂而非单纯吸附。A6 在还原铁的同时以铵或氢为电子供体完成脱氟。需明确：执行 C-F 键断裂的具体酶在 A6 中尚未被鉴定/表征。作为还原脱卤化学的结构先例，Nitratireductor pacificus pht-3B 来源的还原脱卤酶（PDB 4RAS，Payne 2015）含咕啉（维生素 B12）辅因子与铁硫簇，其结构提示 B12 依赖型脱卤机制；该酶作用于有机卤化物（较重卤素碳-卤键），并非全氟烷基 C-F 脱氟酶，亦非 A6 自身脱氟酶，仅作为还原脱卤化学原理的结构先例。

## 2. 吸附机制详解

### 机制1：厌氧还原条件下 Acidimicrobium sp. A6 对 PFOA/PFOS 的还原脱氟

**描述**：Acidimicrobium sp. strain A6（一种以铁还原偶联铵氧化的化能自养菌，可营 Feammox）在厌氧还原条件下可将 PFOA 与 PFOS 还原脱氟：孵育体系中观察到氟离子累积、更短链全氟化产物与乙酸的生成，以及单位铵氧化所还原 Fe(III) 的下降；以氢为唯一电子供体时同样发生脱氟。该过程与铁还原偶联，以铵或氢为电子供体。执行 C-F 键断裂的具体酶在 A6 中尚未被鉴定/表征
**关键官能团**：['低氧化还原电位还原中心（与铁还原偶联，具体酶未表征）', '电子供体（铵经 Feammox / 氢）', '末端电子受体（Fe(III)）']
**来源**：DOI 10.1021/acs.est.9b04047

### 机制2：B12（咕啉）依赖型还原脱卤酶作为还原性碳-卤键断裂的结构先例

**描述**：Nitratireductor pacificus pht-3B 来源的还原脱卤酶（PDB 4RAS，Payne 2015 Nature）含咕啉（维生素 B12）辅因子与铁硫簇，其结构提示 B12 依赖型脱卤的机制，为还原性碳-卤键断裂提供了结构生物学先例。该酶属有机卤化物呼吸的还原脱卤酶（作用对象为卤代烃，非全氟烷基 C-F 键脱氟酶），在此仅作为还原脱卤化学原理的结构先例，并非 Acidimicrobium sp. A6 自身的脱氟酶
**关键官能团**：['咕啉（维生素 B12 / Co-咕啉）辅因子', '铁硫簇（电子中继）']
**来源**：DOI 10.1038/nature13901

## 3. 结构特征与结构-功能关系

必须保留：① 厌氧低氧化还原电位微环境；② 电子供体（铵经 Feammox 或氢）与末端电子受体（Fe(III)）的还原偶联；③ 可介导还原性碳-卤键断裂的低电位辅因子化学（咕啉/B12 类，先例层）。可灵活调整：载体/反应器形态、电子供体供给方式、还原性矿物或人工还原剂、辅因子/催化剂固定化方式。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 严格厌氧/还原条件与电子供体依赖: A6 还原脱氟须在厌氧还原条件下进行，以铁还原为末端电子汇、以铵（经 Feammox）或氢为电子供体；脱离该还原偶联则脱氟不成立 None
- 低效率与慢动力学: 天然 A6 体系对 PFOA/PFOS 的脱氟缓慢且不完全：百日尺度孵育仅观察到至多约六成去除，并停留在更短链全氟产物，未完全矿化；不构成高效降解方案 None
- 脱氟酶未表征，转译限原理层: A6 中执行 C-F 键断裂的具体酶尚未鉴定/表征，B12 依赖型还原脱卤酶（PDB 4RAS）仅为有机卤化物还原脱卤的结构先例，非 A6 脱氟酶；仿生还原脱氟材料转译限于原理层，须实验验证 None

## 6. 相关原型

- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fluoroacetate-dehalogenase
- iron-oxidizing-bacteria
- lignin-peroxidase-white-rot

## 参考文献

[待补充]
