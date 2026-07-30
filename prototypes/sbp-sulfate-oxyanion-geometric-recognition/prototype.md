---
id: sbp-sulfate-oxyanion-geometric-recognition
name: 硫酸根结合蛋白 SBP 氧阴离子几何识别蛋白（Sulfate-Binding Protein (SBP) Oxyanion Geometric Recognition Protein）
category: 微生物
organism: Salmonella typhimurium（硫酸根结合蛋白 SBP）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
adsorption_mechanisms:
  - 预组织中性氢键给体阵列对四面体硫酸根的几何识别（纯氢键、无阳离子）
  - 硫酸根完全埋藏与局部偶极对无补偿电荷的稳定化
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 硫酸根结合蛋白 SBP 氧阴离子几何识别蛋白（Sulfate-Binding Protein (SBP) Oxyanion Geometric Recognition Protein）

## 1. 生物原型简介

**问题定义**：细菌需从水环境中捕获硫酸根（SO4²⁻）以供同化利用。带二价负电荷的氧阴离子在脱水埋藏后如何被蛋白识别与稳定，即在没有溶剂化壳层、没有阳离子或盐桥的前提下如何稳定带电基团，是分子识别与蛋白静电学的基础问题。

**生物策略**：鼠伤寒沙门氏菌周质 SBP 以两个相似球状结构域间的深裂隙完全包埋四面体硫酸根（PDB 1SBP，1.7 Å 精修；Nature 1985 摘要记硫酸根 buried and completely inaccessible to the solvent）。硫酸根主要由七个氢键固定：五个由主链肽 NH 给出，一个由丝氨酸羟基给出，一个由 Trp192 吲哚 NH 给出；二价阴离子范德华距离内无带正电残基、无阳离子、无水分子（J Mol Biol 1988 摘要）。结合氢键经肽单元与多个共振氢键体系耦合。He 与 Quiocho 1993 以 1.7 Å 结构与定点突变证明：无补偿埋藏电荷的稳定化是高度局域化过程，依赖肽单元与螺旋首圈的局部偶极集合；将带正电 His 与两个 Arg 替换为 Asn 后硫酸根结合活性不受影响，螺旋宏偶极贡献可忽略。这为纯氢键、无阳离子、局域偶极稳定的四面体氧阴离子识别提供了完整结构生物学证据。

## 2. 吸附机制详解

### 机制1：预组织中性氢键给体阵列对四面体硫酸根的几何识别（纯氢键、无阳离子）

**描述**：鼠伤寒沙门氏菌硫酸根结合蛋白（SBP）在两个相似球状结构域间的深裂隙中完全包埋四面体硫酸根 SO4²⁻；硫酸根主要由七个氢键固定，其中五个由主链肽 NH 给出，一个由丝氨酸羟基给出，一个由 Trp192 吲哚 NH 给出（PDB 1SBP，SITE AC1 位点残基 Tyr10、Asp11、Pro12、Gly44、Ser45、Ser130、Gly131、Gly132、Gly172、Ala173、Trp192，chain A）；硫酸根二价阴离子范德华距离内无带正电残基、无阳离子、无水分子
**关键官能团**：['氢键给体（主链酰胺 NH 为主，Ser 侧链羟基、Trp192 吲哚 NH）', '完全埋藏低介电裂隙']
**来源**：DOI 10.1016/0022-2836(88)90341-5

### 机制2：硫酸根完全埋藏与局部偶极对无补偿电荷的稳定化

**描述**：硫酸根带电氧原子埋藏且与溶剂完全隔绝，其稳定化无盐桥参与，由蛋白特定位基的氢键完成；这些氢键又经肽单元与多个共振氢键体系耦合。1.7 Å 结构与定点突变表明：无补偿的埋藏二价电荷的稳定化是高度局域化过程，依赖肽单元与螺旋首圈局部偶极的集合；带正电 His 与两个 Arg 突变为 Asn 后硫酸根结合活性不受影响，螺旋宏偶极贡献可忽略
**关键官能团**：['局部偶极（肽单元、螺旋首圈偶极）', '共振氢键网络']
**来源**：DOI 10.1002/pro.5560021010

## 3. 结构特征与结构-功能关系

必须保留：① 以主链酰胺型中性氢键给体为主、与四面体氧阴离子几何互补的预组织阵列（1SBP 中七氢键，五个为主链 NH）；② 完全埋藏的低介电裂隙（排除溶剂竞争、强化静电）；③ 局域偶极与共振氢键网络（电荷稳定化不依赖荷电基团）。可灵活调整：载体骨架、给体密度与取向、裂隙疏水微环境。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶周质蛋白形态: SBP 为鼠伤寒沙门氏菌周质可溶性结合蛋白（约 34.6 kDa，椭球约 35 Å × 35 Å × 65 Å），识别裂隙需移植或固定于固体载体方可用作吸附 None
- 两域裂隙预组织依赖: 结合依赖两球状结构域间深裂隙的完整三级结构与域闭合；裂隙溶剂化或结构解折叠使氢键几何与低介电环境丧失 None
- 二价四面体几何与电荷特异性: 位点与二价四面体硫酸根几何互补且无阳离子补偿；对单价磺酸根（SO3⁻）的亲和力与选择性受电荷、尺寸与水合差异影响，须实验核验 None
- 水相氢键竞争: 天然位点完全埋藏且硫酸根范德华距离内无水分子；水相吸附须以低介电孔壁排除体相水竞争 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding

## 参考文献

[待补充]
