---
id: ecdysis-renewable-interface
name: 蜕皮式可更新界面（Ecdysis Renewable Interface）
category: 动物
organism: Arthropoda：Manduca sexta（烟草天蛾，蜕皮内分泌生理模型）/ Ostrinia furnacalis（亚洲玉米螟，表皮蛋白 OfLCP30-C 结构，PDB 9L0P）
biomimetic_dimension: 结构仿生
features:
  - 自清洁
  - 抗生物污染
adsorption_mechanisms:
  - 蜕皮（ecdysis）：周期性整体蜕除表皮以物理更新界面
  - 几丁质-表皮蛋白复合表皮：离散可重建的结构单元
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 8 verified, 0 unverified
# coverage: partial
# status: active
---
# 蜕皮式可更新界面（Ecdysis Renewable Interface）

## 1. 生物原型简介

**问题定义**：吸附/抗污界面材料在服役中不可避免地在表面积累吸附质（如 PFOA、BPA）、有机污损物与生物膜，界面功能随饱和与污损逐步衰减；常规再生依赖化学洗脱或整体更换。节肢动物则以蜕皮（ecdysis）周期性蜕除并重建体表表皮，天然实现了界面物理更新。须诚实注明：蜕皮的首要功能是生长/发育（替代不能扩张的刚性外骨骼），表面更新是其衍生后果。

**生物策略**：发育中的昆虫通过刻板蜕皮行为反复蜕除表皮（Zitnan 1996 摘要逐字：Developing insects repeatedly shed their cuticle by means of a stereotyped behavior called ecdysis）；蜕除行为由 ETH/EH 内分泌正反馈级联触发（Manduca sexta 上表皮腺/Inka 细胞释放 Mas-ETH，中枢 VM 神经元释放 EH，两组细胞相互激发，条件满足后 EH/ETH 激增触发 preecdysis 与 ecdysis，Ewer & Truman 1997），且行为与蜕皮后期的发育变化（新表皮预成）精确协调。蜕除物为整张旧表皮（exuvia，几丁质-表皮蛋白复合体），旧表面附着物随旧层整体丢弃，暴露其下预成的新表皮。可更换的结构单元为几丁质纳米原纤嵌入表皮蛋白基质的复合体：表皮蛋白（CPR 家族）以保守 R&R 结构域结合几丁质（Rebers & Willis 2001 标题：A conserved domain in arthropod cuticular proteins binds chitin）；2025 年固体核磁结构（PDB 9L0P，Ostrinia furnacalis OfLCP30-C/UniProt Q08738）显示该域以平面结构同一侧芳香族氨基酸黏附片贴附几丁质表面，并在结合时发生去折叠→折叠转变（Hu 2025）。

## 2. 吸附机制详解

### 机制1：蜕皮（ecdysis）：周期性整体蜕除表皮以物理更新界面

**描述**：发育中的昆虫通过名为蜕皮的刻板行为周期性蜕除旧表皮并以新表皮替代（Zitnan 1996 摘要逐字：repeatedly shed their cuticle by means of a stereotyped behavior called ecdysis）。蜕除行为由 ETH/EH 内分泌正反馈级联触发：Manduca sexta 上表皮腺（epitracheal glands/Inka 细胞）释放蜕皮触发激素 Mas-ETH，中枢 VM 神经元释放羽化激素 EH，两组内分泌细胞相互激发，条件满足后血淋巴 EH/ETH 激增，触发 preecdysis 与 ecdysis 运动程序（Ewer & Truman 1997）；行为与蜕皮后期的发育变化（新表皮预成）精确协调。蜕除物为整张旧表皮（exuvia），旧界面上的附着物随旧层整体丢弃，暴露其下预成的新表皮界面
**关键官能团**：['内分泌触发肽（ETH 蜕皮触发激素、EH 羽化激素）', '表皮外层（上表皮/外表皮/内表皮，蜕除单元）', '蜕皮运动程序（preecdysis/ecdysis）']
**来源**：DOI 10.1126/science.271.5245.88

### 机制2：几丁质-表皮蛋白复合表皮：离散可重建的结构单元

**描述**：蜕皮蜕除与重建的结构单元是节肢动物表皮：几丁质（β-1,4-N-乙酰氨基葡聚糖）纳米原纤嵌入表皮蛋白基质的复合材料。表皮蛋白（CPR 家族）以保守 R&R 结构域（Rebers-Riddiford 结构域，RR-1/RR-2 型）结合几丁质（Rebers & Willis 2001 标题：A conserved domain in arthropod cuticular proteins binds chitin）。PDB 9L0P（Hu 2025，固体核磁结构）显示亚洲玉米螟幼虫表皮蛋白 OfLCP30-C 的 R&R 结构域在水溶液中本征无序、结合几丁质时发生去折叠→折叠转变，以平面结构同一侧的芳香族氨基酸黏附片（adhesive patches）贴附几丁质表面。表皮组织在每个蜕皮周期从头重建该复合体，使表层成为离散、可按需合成、可更换的结构单元
**关键官能团**：['几丁质纳米原纤（β-1,4-N-乙酰氨基葡聚糖）', '表皮蛋白 CPR 家族（保守 R&R 结构域，RR-1/RR-2）', '芳香族氨基酸黏附片（几丁质结合界面）']
**来源**：DOI 10.1021/jacs.5c05099

## 3. 结构特征与结构-功能关系

必须保留：① 外层周期性整体蜕除（整层丢弃以移除表面积累）；② 离散可更换复合结构单元（表层为可合成、可移除的离散单元）；③ 新层预成后更换（先在其下预成新界面再蜕除旧层）；④ 阈值信号触发离散事件（内分泌级联正反馈触发）。可灵活调整：人工外层材料与厚度、触发方式（pH/温度/溶解/机械剥离）、更新周期、底层功能层化学。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 离散周期性更新: 蜕皮以离散周期事件发生（repeatedly shed），界面非连续更新，更新事件之间为蜕间期；人工类比须接受批次式更新而非连续再生 None
- 更新窗口功能间断: 蜕除旧层后至新层稳定（骨化）前存在软弱窗口期；人工可剥落外层的更换窗口同样存在功能骤降，须做连续性设计（多层预成、分区更换） None
- 天然功能归属为生长发育: 蜕皮首要功能为替代刚性外骨骼以支持生长；抗污自更新为周期性蜕除的衍生后果，转译时不得假托为自然选择直接优化的抗污策略 None
- 可更换单元的材料组成依赖: 天然可更换单元为几丁质原纤-表皮蛋白复合体（R&R 结构域芳香黏附片结合几丁质）；人工类比须自设等效的骨架层加可移除面层材料体系 None

## 6. 相关原型

- cactus-spine
- lotus-leaf
- pitcher-plant-slippery-surface
- shark-skin
- superhydrophobic-artificial

## 参考文献

[待补充]
