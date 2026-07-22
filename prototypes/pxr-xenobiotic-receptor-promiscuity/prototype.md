---
id: pxr-xenobiotic-receptor-promiscuity
name: 孕烷 X 受体 PXR 异生物质定向混杂核受体（Pregnane X Receptor PXR Xenobiotic Directed-Promiscuity Nuclear Receptor）
category: 动物
organism: Homo sapiens（人孕烷 X 受体 PXR / NR1I2，异生物质-甾体核受体）
biomimetic_dimension: 分子仿生
features:
  - 广谱识别
  - 疏水性
adsorption_mechanisms:
  - 大体积柔性疏水腔加少量极性锚对结构多样异生物质配体的定向混杂（多取向）识别
  - 定向混杂作为进化的异生物质感知-解毒功能（机制层级声明）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 孕烷 X 受体 PXR 异生物质定向混杂核受体（Pregnane X Receptor PXR Xenobiotic Directed-Promiscuity Nuclear Receptor）

## 1. 生物原型简介

**问题定义**：机体需在接触多种结构各异的亲脂异生物质（药物、外源化学物）时迅速启动解毒。若每种异生物质都需一个专一受体，则监测成本极高。孕烷 X 受体 PXR（人 NR1I2，曾称甾体与异生物质受体 SXR）进化为广谱异生物质传感器：被多种异生物质激活后转录上调 CYP3A 等解毒/外排酶。其分子基础问题是，单一配体结合腔如何识别结构多样的异生物质。

**生物策略**：Watkins 等（2001）测定人 PXR LBD 单独及其与降脂药 SR12813 复合物的晶体结构（PDB 1ILH，2.5/2.75 Å）：配体结合腔为大体积疏水腔、仅含少量极性残基，SR12813 可在腔内取三种不同取向，少量极性残基的位置与性质对建立精确药理激活谱至关重要；论文标题概括为'人核异生物质受体 PXR：定向混杂的结构基础'。Chrencik 等（2005）解析人 PXR LBD 与大环内酯利福平的复合物（PDB 1SKX），揭示复合物中存在结构无序（腔壁柔性）。比较两结构：利福平（PDB 1SKX SITE AC1 15 残基）与 SR12813（PDB 1ILH SITE AC1 21 残基）共享 Val211/Leu240/Met243/Ser247/Phe251/Phe281/Cys284/Gln285/Trp299/Met323/His407/Phe420 等腔壁残基，即同一柔性疏水腔以重叠残基集合容纳结构迥异的配体，这正是定向混杂的结构基础：混杂本身即进化的异生物质感知功能，而非碰巧结合。

## 2. 吸附机制详解

### 机制1：大体积柔性疏水腔加少量极性锚对结构多样异生物质配体的定向混杂（多取向）识别

**描述**：人 PXR 配体结合域（LBD）具大体积疏水腔，腔壁以疏水残基为主、仅含少量极性残基；该腔以定向混杂方式结合结构差异显著的异生物质配体：大环内酯抗生素利福平（PDB 1SKX，配体 RFP，chain A）与膦酸酯类降脂药 SR12813（PDB 1ILH，配体 SRL，chain A）。PDB 1ILH SITE AC1 列 21 个结合位点残基（Leu206、Ser208、Leu209、Val211、Leu240、Met243、Ala244、Met246、Ser247、Phe251、Phe281、Cys284、Gln285、Phe288、Trp299、Met323、Leu324、His407、Arg410、Phe420、HOH1595），PDB 1SKX SITE AC1 列 15 个（Lys210、Val211、Leu240、Met243、Ser247、Phe251、Phe281、Cys284、Gln285、Trp299、Leu308、Met323、His407、Phe420、HOH608），二者共享 Val211/Leu240/Met243/Ser247/Phe251/Phe281/Cys284/Gln285/Trp299/Met323/His407/Phe420 等腔壁残基；Watkins 2001 摘要指出 SR12813 可在腔内取三种不同取向，少量极性残基的位置与性质决定激活谱。残基编号为 PDB 链 A 编号（1SKX construct 残基 130-431），未做与 UniProt O75469 的逐位偏移核对
**关键官能团**：['大体积疏水腔壁残基（Leu/Val/Met/Ala/Phe/Cys/Trp，范德华接触）', '稀疏极性锚残基（Ser208、Ser247、Gln285、His407、Arg410）']
**来源**：DOI 10.1126/science.1060762

### 机制2：定向混杂作为进化的异生物质感知-解毒功能（机制层级声明）

**描述**：PXR 进化为广谱异生物质/甾体传感器：被多种亲脂异生物质激活后经转录上调细胞色素 P450 3A（CYP3A）等解毒/外排通路。Watkins 2001 摘要逐字陈述 hPXR 响应多种异生物质激活 CYP3A 表达、并在药物-药物相互作用中起关键作用，其感知异生物质的能力即由该定向混杂腔提供。故定向混杂本身是进化的功能（感知异生物质并启动解毒），而非碰巧结合；PXR 的天然读出是转录激活（解毒上调），并非配体的物理去除或隔离
**关键官能团**：['异生物质感知腔（大体积疏水腔加稀疏极性锚）', '激活谱决定残基（少量极性残基的位置与性质）']
**来源**：DOI 10.1126/science.1060762

## 3. 结构特征与结构-功能关系

必须保留：① 大体积疏水腔（容纳多样亲脂骨架的范德华接触面）；② 稀疏分布的预组织极性锚（Ser/Gln/His/Arg 型，有限而关键的方向性锚定，决定激活/结合谱）；③ 腔壁构象柔性（多配体/多取向适配）。可灵活调整：载体骨架、腔容积与孔径、极性锚种类与密度、柔性间隔臂。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶核受体结构域形态: PXR LBD construct 残基 130-431（人 NR1I2，PDB 1SKX COMPND），识别依赖三级疏水腔，用作吸附须将腔壁/极性锚基序移植或固定于固体载体 None
- 定向混杂=广谱而非专一: PXR 腔对结构多样的亲脂异生物质呈定向混杂识别（利福平/SR12813 共享腔壁残基且 SR12813 取三种取向），材料转译只得类/混合物水平的广谱识别，不构成对 BPA 的专一锁钥选择性 None
- 双酚为碰巧/混杂配体，机制层级为感知非去除: 双酚类（含 BPA）作为亲脂异生物质属 PXR 的碰巧/混杂配体，本条目未核验任何 PXR-双酚复合物结构或亲和力数据；PXR 天然功能为异生物质感知-解毒（CYP3A 转录上调），非配体物理去除 None
- 构象柔性/无序依赖: 定向混杂部分依赖腔壁构象柔性（PDB 1SKX 标题记复合物中'结构无序'）；材料移植若刚性化腔体，可能降低对多样配体的混杂容量 None

## 6. 相关原型

- cactus-spine
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding
- hsa-fatty-acid-pfas-binding
- lipocalin-hydrophobic-calyx

## 参考文献

[待补充]
