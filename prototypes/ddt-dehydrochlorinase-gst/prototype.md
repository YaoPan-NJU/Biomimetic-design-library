---
id: ddt-dehydrochlorinase-gst
name: DDT 脱氯化氢酶（谷胱甘肽 S-转移酶 GSTe2）（DDT-Dehydrochlorinase (Glutathione S-Transferase GSTe2)）
category: 动物
organism: Anopheles funestus（非洲疟蚊谷胱甘肽 S-转移酶 epsilon 2 GSTe2；双翅目蚊科）
biomimetic_dimension: 分子仿生
features:
  - 催化降解
  - 分子筛分
adsorption_mechanisms:
  - GST 双分区活性位点催化 DDT 脱氯化氢（降解/转化）
  - 底物特异性双基序读出（桥碳 C-H 与三氯甲基）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 6 papers, 9 verified, 0 unverified
# coverage: partial
# status: active
---
# DDT 脱氯化氢酶（谷胱甘肽 S-转移酶 GSTe2）（DDT-Dehydrochlorinase (Glutathione S-Transferase GSTe2)）

## 1. 生物原型简介

**问题定义**：DDT 曾是核心有机氯杀虫剂，双翅目昆虫经代谢抗性（尤其 DDT 脱氯化氢）对其产生耐药。在分子层面，酶如何在结构高度相似的有机氯类似物（DDT/DDD/DDE）中专一读取 DDT 并催化其脱氯化氢，是分子识别与酶催化的基础问题。

**生物策略**：DDT 脱氯化氢酶本质为谷胱甘肽 S-转移酶（Clark & Shamaan 1984 证明家蝇 DDT 脱氯化氢酶即 GST；Lipke & Kearns 1959 最早表征 DDT 脱氯化氢酶）。非洲疟蚊 GSTe2（PDB 3ZML，1.64 Å）采用 GST 超家族双分区活性位点：N 端 G 位结合 GSH（配体 GSH A 1222，结合残基 Ser12/Pro14/Leu36/His41/His53/Thr54/Ile55/Pro56/Glu67/Ser68/His69/Phe108/Arg112，chain A），C 端 H 位构成疏水 DDT 结合腔。催化经质子转移（β-消除）机制：GSH 作为辅因子攫取桥碳质子，不作共轭底物，DDT 脱 HCl 生成 DDE（Li 2014 QM/MM）。底物特异性要求桥碳 C-H 与三氯甲基双基序，DDD（-CHCl2）/DDE（无桥碳 C-H）不被有效读取。Riveron 2014 证明 L119F 突变扩大 DDT 结合腔、增加 DDT 进入与代谢，赋予高水平 DDT 抗性。

## 2. 吸附机制详解

### 机制1：GST 双分区活性位点催化 DDT 脱氯化氢（降解/转化）

**描述**：GSTe2 以谷胱甘肽 S-转移酶超家族典型的双分区活性位点催化 DDT 脱氯化氢：N 端 G 位结合谷胱甘肽 GSH（PDB 3ZML 配体 GSH A 1222，结合位点残基 Ser12、Pro14、Leu36、His41、His53、Thr54、Ile55、Pro56、Glu67、Ser68、His69、Phe108、Arg112，chain A，PDB 编号，SITE AC1），C 端 H 位构成疏水 DDT 结合腔；DDT 经质子转移（β-消除）脱去 HCl 生成 DDE，GSH 作为辅因子（碱）攫取桥碳质子，不作共轭底物
**关键官能团**：['谷胱甘肽 GSH 辅因子（巯基/碱）', '疏水 DDT 结合腔（H 位）', '活性位点残基（Arg112、Glu67、Ser68、His53、Ile55 等）']
**来源**：DOI 10.1186/GB-2014-15-2-R27

### 机制2：底物特异性双基序读出（桥碳 C-H 与三氯甲基）

**描述**：DDT 脱氯化氢酶读出 DDT 的一对相邻结构基序（桥碳 C-H 与三氯甲基 -CCl3），二者齐备方能催化脱氯化氢；其类似物 DDD（二氯甲基 -CHCl2 取代 -CCl3）与 DDE（桥碳 C-H 已随脱氯化氢失去而成 C=C）各缺一个决定基，故不被有效读取。该双基序读出是双翅目 DDT 抗性的底物特异性基础，亦构成桥基序读出的分子识别动机原型
**关键官能团**：['桥碳 C-H（可攫取质子）', '三氯甲基 -CCl3（β-氯离去基团）']
**来源**：DOI 10.1021/es405230j

## 3. 结构特征与结构-功能关系

必须保留：① 双分区活性位点（G 位 GSH 辅因子加 H 位疏水腔）；② 质子转移/β-消除催化机制；③ 桥碳 C-H 与三氯甲基双基序读出。可灵活调整：载体骨架、腔体疏水微环境、是否保留催化（转译仅取识别动机）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶酶与辅因子依赖: GSTe2 为可溶性胞内酶（约 25.3 kDa，PDB 3ZML），催化需 GSH 辅因子；其催化与识别基序须固定化或重构方可用于材料 None
- 降解/转化而非吸附: 天然机制为 β-消除催化转化（DDT→DDE+HCl），非吸附富集；且 DDE 仍属持久性有机污染物，转化不等于无害；仿生转译限原理层 None
- 双基序几何/电子特异性: 识别与催化依赖桥碳 C-H 与三氯甲基双基序的互补；DDD（-CHCl2）/DDE（无桥碳 C-H）与 DDT 仅差一至两个原子，材料层面判别难度高 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding

## 参考文献

[待补充]
