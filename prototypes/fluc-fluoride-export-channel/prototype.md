---
id: fluc-fluoride-export-channel
name: Fluc 双拓扑氟离子输出通道（Fluc Dual-Topology Fluoride Export Channel）
category: 微生物
organism: Escherichia coli（菌株 S88，Fluc/crcB 氟离子通道，又称 Fluc-Ec2；UniProt Q6J5N4）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 特异性识别
adsorption_mechanisms:
  - 双拓扑『双桶』同源二聚体氟离子通道架构
  - 窄孔与苯丙氨酸四极边缘对 F− 相对 Cl− 的尺寸/静电选择性识别
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 11 verified, 0 unverified
# coverage: partial
# status: active
---
# Fluc 双拓扑氟离子输出通道（Fluc Dual-Topology Fluoride Export Channel）

## 1. 生物原型简介

**问题定义**：环境氟化物对微生物具毒性，细菌须将胞内 F− 快速排出以抗氟毒性。F− 半径小、水合强、与 Cl− 等卤离子化学相似，如何在膜上构建一个对 F− 特异、排除 Cl− 的输运原型，是离子选择性的基础问题。Fluc/crcB 家族是自然界已知唯一的 F− 特异性生物输运原型。

**生物策略**：细菌 Fluc/crcB 为小型整合膜同源二聚体，两条亚基以反向膜拓扑装配，各自形成一条独立 F− 孔道，构成『双桶』架构，两条 F− 通路跨膜，中心配位一个最可能为 Na+ 的阳离子（Stockbridge 2015，PDB 5A43：E. coli 菌株 S88 的 Fluc/crcB，硒代甲硫氨酸衍生物、单抗 chaperone 结晶，2.58 Å，配体含 F− 与 Na+）。Fluc 对 F− 相对 Cl− 具强选择性，文献提出源于极窄孔道与利用保守苯丙氨酸环四极边缘的不寻常阴离子配位。McIlwain 2021（PDB 7KKA：Fluc-Ec2 S81A·Br− 复合物，2.5 Å，配体 Br−/F−/Na+）以 Br−（Cl− 同族较大卤离子）探针揭示阴离子识别位点：保守 Ser81 突变为 Ala 后 Br− 得以占据该位点，并据结合位点沿渗透通路分布提出『结合位点交替占据、底物接近时完全组装』的渗透机制。Fluc 的功能是保护微生物免受环境氟毒性（『protect microbes against ... cytoplasmic accumulation of this toxic halide』）。

## 2. 吸附机制详解

### 机制1：双拓扑『双桶』同源二聚体氟离子通道架构

**描述**：细菌 Fluc/crcB 为小型整合膜同源二聚体（每亚基约 13.6–13.9 kDa），两条亚基以相反的膜拓扑（dual topology）装配，各自形成一条独立的 F− 传导孔道，构成『双桶』（double-barrelled）架构，两个 F− 通路跨膜；双拓扑排布在二聚体中心配位一个阳离子（最可能为 Na+）。PDB 5A43（E. coli 菌株 S88 的 Fluc/crcB，硒代甲硫氨酸衍生物、单抗 chaperone 结晶，2.58 Å）含配体 F−（FLUORIDE ION）与 Na+（SODIUM ION），直接呈现该双拓扑双桶装配
**关键官能团**：['跨膜孔道骨架（双拓扑同源二聚体）', '中心配位阳离子（Na+）']
**来源**：DOI 10.1038/nature14981

### 机制2：窄孔与苯丙氨酸四极边缘对 F− 相对 Cl− 的尺寸/静电选择性识别

**描述**：Fluc 对 F− 相对 Cl− 具强选择性，文献提出其源于极窄的孔道与一种不寻常的阴离子配位：利用保守苯丙氨酸环的四极边缘（quadrupolar edges）配位阴离子。阴离子识别位点经 PDB 7KKA（Fluc-Ec2，E. coli，UniProt Q6J5N4，S81A 突变体，2.5 Å）以溴离子（Br−，Cl− 的同族较大卤离子）探针揭示：将保守 Ser81（PDB 链 A 81 位，UniProt Q6J5N4 Ser81）突变为 Ala 后，Br− 得以占据/可视化该识别位点（配体 BR，BROMIDE ION），结构同时含 F− 与 Na+。McIlwain 2021 eLife 据此提出阴离子结合位点沿渗透通路交替占据、且仅在底物接近时完全组装的渗透机制
**关键官能团**：['窄孔选择性滤器', '保守苯丙氨酸环（四极边缘阴离子配位）', 'Ser81 阴离子识别位点（Fluc-Ec2 / UniProt Q6J5N4，PDB 7KKA 链 A 81 位）']
**来源**：DOI 10.1038/nature14981

## 3. 结构特征与结构-功能关系

必须保留：① 极窄孔道（尺寸筛分，排除 Cl−/Br−）；② 保守芳香环（苯丙氨酸）四极边缘的阴离子配位；③ 识别位点残基（如 Ser81）对卤离子尺寸的约束；④ 双拓扑双桶二聚体支架与中心阳离子。可灵活调整：孔道骨架材料、芳香给体排布、识别位点化学、门控读出方式。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 整合膜通道形态（脂双层依赖）: Fluc/crcB 为小型整合膜同源二聚体（每亚基约 13.6–13.9 kDa，PDB 5A43 实体 1 约 13.86 kDa、PDB 7KKA 实体 1 约 13.60 kDa），须在脂双层中方可形成跨膜孔道；不可作为可溶蛋白直接用作吸附剂，转译只提取选择性与门控原理 None
- 底物为游离 F−（对完整有机氟惰性）: Fluc 识别/输运对象为裸 F−（小、高电荷密度）；完整 PFAS 的 C−F 键不释放游离 F−，故 Fluc 机制对完整 PFAS 分子无直接识别作用，仅在脱氟降解产生 F− 后间接相关 None
- 真实水体中的阴离子选择性挑战: 天然 F−/Cl− 选择性针对胞内 F− 排出；转译到真实水体须面对 Cl−、HCO3−、SO4²⁻ 等高浓度共存阴离子对 F− 识别的竞争，选择性窗口须实验重标定 None
- 双拓扑二聚体装配依赖: 通道功能依赖反向拓扑同源二聚体与中心配位 Na+ 的完整装配；破坏二聚界面或拓扑排布将使孔道/选择性丧失 None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- cell-membrane-ion-channel
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation

## 参考文献

[待补充]
