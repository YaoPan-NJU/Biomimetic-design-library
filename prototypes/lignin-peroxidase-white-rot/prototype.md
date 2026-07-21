---
id: lignin-peroxidase-white-rot
name: 木质素过氧化物酶（白腐真菌）（Lignin Peroxidase (White-Rot Fungi, EC 1.11.1.14)）
category: 微生物
organism: Phanerochaete chrysosporium（木质素过氧化物酶 LiP，同工酶 H2/H8；白腐真菌，PDB 1B85 SOURCE 记 ORGANISM_COMMON: WHITE-ROT FUNGUS）
biomimetic_dimension: 分子仿生
features:
  - 催化降解
  - 活性氧位点
adsorption_mechanisms:
  - 藜芦醇氧化还原介体对非酚型芳香底物的一电子自由基氧化
  - 表面色氨酸 171 自由基 relay 位点（W171 氧化还原活性位点）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 9 papers, 12 verified, 0 unverified
# coverage: partial
# status: active
---
# 木质素过氧化物酶（白腐真菌）（Lignin Peroxidase (White-Rot Fungi, EC 1.11.1.14)）

## 1. 生物原型简介

**问题定义**：木质素是植物细胞壁中由非酚型芳香单元交联的顽固聚合物，其生物降解是碳循环的关键环节，也是难降解芳香污染物（有机氯农药、PAH 等）转化研究的原理参照。白腐真菌 Phanerochaete chrysosporium 分泌的木质素过氧化物酶（LiP）可在胞外以 H2O2 驱动氧化降解木质素，其分子机制（高氧化电位血红素化学、介体 relay、表面自由基位点）是降解仿生设计的原理源头。

**生物策略**：LiP 为单体血红素糖蛋白（PDB 1LLP，同工酶 H2，1.70 Å，P. chrysosporium BKM-F1267；RCSB 分子量 37.95 kDa，KEYWDS: HEME PROTEIN, GLYCO PROTEIN, OXIDOREDUCTASE），含一枚铁原卟啉 IX，血红素 Fe 与 His176 NE2 轴向配位（PDB 1LLP/1LGA/1B85 LINK 记录，2.15–2.19 Å，同工酶间保守；Poulos 等 1993 年以 PDB 1LGA 完成 2 Å 精修）。催化按一电子转移途径进行：H2O2 激活血红素生成高价中间体（化合物 I），从底物夺取一个电子生成底物自由基（Hammel 1986 PNAS 标题：'Substrate free radicals are intermediates in ligninase catalysis'）；内源小分子介体藜芦醇被氧化为阳离子自由基，relay 氧化难以进入埋藏血红素口袋的非酚型单甲氧基化芳香底物（Valli 1990 标题直陈藜芦醇在木质素生物降解中的必需角色）。第二条 relay 途径在蛋白表面：PDB 1LLP 在表面 Trp171 的 Cβ 解析出羟基，揭示氧化还原循环中形成的新型自由基位点（Choinowski 1999 JMB 标题），W171F 突变消除该氧化还原活性色氨酸并改变反应机制（Blodig 2001 JMB 标题）。该酶执行的是降解/转化（非特异自由基氧化），而非吸附。

## 2. 吸附机制详解

### 机制1：藜芦醇氧化还原介体对非酚型芳香底物的一电子自由基氧化

**描述**：LiP（白腐真菌 P. chrysosporium 分泌的胞外血红素糖蛋白过氧化物酶，PDB KEYWDS: HEME PROTEIN, GLYCO PROTEIN, OXIDOREDUCTASE）以 H2O2 为共底物激活血红素铁，生成高价血红素中间体（化合物 I，机理层命名），经一电子转移氧化内源小分子介体藜芦醇（veratryl alcohol, 3,4-二甲氧基苄醇）；介体自由基再经扩散或表面 relay 将一电子氧化传递给难以进入埋藏血红素口袋的非酚型（单甲氧基化）芳香底物与木质素聚合物，完成非特异自由基氧化降解
**关键官能团**：['血红素铁氧化还原中心（铁原卟啉 IX，His176 轴向配位）', '小分子氧化还原介体（藜芦醇/3,4-二甲氧基苄醇）', '一电子转移自由基化学']
**来源**：DOI 10.1021/bi00489a005

### 机制2：表面色氨酸 171 自由基 relay 位点（W171 氧化还原活性位点）

**描述**：PDB 1LLP（同工酶 H2，1.70 Å）在表面色氨酸 171 的 Cβ 上解析出羟基，提示该色氨酸在氧化还原循环中形成自由基（Choinowski 1999 JMB 标题：a novel radical site formed during the redox cycle）；W171F 突变消除该氧化还原活性色氨酸并改变反应机制（Blodig 2001 JMB 标题）。Trp171 受高价血红素中间体氧化后在蛋白表面 relay 电子，使难以进入埋藏活性口袋的大分子底物经表面途径完成一电子氧化
**关键官能团**：['表面色氨酸吲哚（Trp171 自由基 relay 位点）', '血红素铁氧化还原中心（经 Trp171 与表面 relay 耦合）']
**来源**：DOI 10.1006/jmbi.1998.2507

## 3. 结构特征与结构-功能关系

必须保留：① 高氧化电位血红素氧化还原中心（铁原卟啉 IX + His 轴向配位）；② H2O2 驱动的一电子转移自由基化学；③ 小分子氧化还原介体 relay（藜芦醇类）；④ 表面氧化还原活性芳香残基 relay 位点（Trp171）；⑤ 酸性工作环境。可灵活调整：蛋白骨架（可经突变增强稳定性，如 Son 2021 引入二硫键/盐桥）、介体种类、载体与部署形式（固定化酶/全细胞/仿生催化材料）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 胞外血红素糖蛋白形态: LiP 为白腐真菌 P. chrysosporium 分泌的胞外单体血红素糖蛋白（RCSB 1LLP 分子量 37.95 kDa；KEYWDS: HEME PROTEIN, GLYCO PROTEIN, OXIDOREDUCTASE；含 HEM 铁原卟啉 IX 与 NAG/MAN 糖基）；材料化需固定化或全细胞（白腐真菌）部署 kDa
- 酸性工作窗口: LiP H8 在酸性条件下行使功能，天然白腐木质素降解发生于酸性胞外环境；中性水相应用需酶工程改造或仿生催化体系替代 None
- H2O2 共底物与氧化自失活: 氧化还原循环需 H2O2 共底物启动；过量 H2O2 引起酶氧化加工与失活（PDB 1B80 沉积标题记录 'oxidatively processed' 重组 LiP H8 形态），氧化剂需计量/流加供给 None
- 介体供给依赖: 非酚型大分子底物的高效氧化依赖藜芦醇等小分子介体 relay；实际体系中需维持介体再生或持续供给，介体的浸出与消耗是工程化约束 None

## 6. 相关原型

- ddt-dehydrochlorinase-gst
- fluoroacetate-dehalogenase
- iron-oxidizing-bacteria
- magnetic-bacteria

## 参考文献

[待补充]
