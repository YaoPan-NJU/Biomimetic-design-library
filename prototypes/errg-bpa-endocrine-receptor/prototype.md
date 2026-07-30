---
id: errg-bpa-endocrine-receptor
name: 雌激素相关受体 γ ERRγ（双酚 A 识别）（Estrogen-Related Receptor Gamma ERRγ (Bisphenol A Recognition)）
category: 动物
organism: Homo sapiens（人源雌激素相关受体 γ ERRγ, NR3B3）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
  - 疏水性
adsorption_mechanisms:
  - 双酚 A 的双酚羟基氢键锚定与狭长疏水口袋接触
  - 组成型激活孤儿受体的预组织口袋与双酚骨架形状读出
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 雌激素相关受体 γ ERRγ（双酚 A 识别）（Estrogen-Related Receptor Gamma ERRγ (Bisphenol A Recognition)）

## 1. 生物原型简介

**问题定义**：BPA 是典型内分泌干扰物：其与雌激素受体 ER 的结合和激素活性极弱，却在很低剂量即显示效应，真正的高亲和核受体靶点长期不明。ERRγ 是人 48 个核受体之一的孤儿核受体，呈组成型转录激活，高表达于发育期脑等组织，内源配体未知。BPA 如何高亲和结合 ERRγ，是内分泌干扰物-核受体相互作用的分子基础问题。

**生物策略**：Takayanagi 等（2006）发现 BPA 强结合 ERRγ：以 [3H]4-OHT 为示踪剂的竞争结合实验给出剂量依赖曲线（IC50 13.1 nM），4-壬基酚与己烯雌酚弱 5-50 倍；BPA 完全保留 ERRγ 的组成型转录激活活性。Matsushima 等（2007）测定 ERRγ LBD 与 BPA 的 1.60 Å 晶体结构（PDB 2E2R）：BPA（配体 2OH，4,4'-propane-2,2-diyldiphenol，chain A 1401）结合于 LBD 疏水口袋，两个酚羟基一个同时与 Glu275 和 Arg316 氢键、另一个与 Asn346 氢键，周围疏水接触（尤其 Tyr326）完成强结合（结合位点 AC1 含 Leu268/Ala272/Glu275/Met306/Leu309/Arg316/Tyr326/Leu345/Asn346/Ile349/Phe435 共 11 残基）；坐标直测酚氧 O2 距 Glu275 OE2 2.55 Å、距 Arg316 NH2 2.98 Å，酚氧 O1 距 Asn346 OD1 2.77 Å。BPA 结合不改变 apo 口袋内部结构并维持 helix 12 活性构象；K(D) = 5.5 nM 且不与 ER 结合。同一口袋还结合双酚 Z（PDB 2ZKC）与 4-α-枯基酚（PDB 2ZAS，BPA 衍生物；后者报道有诱导契合成分）。残基编号与 UniProt P62508 一一对应，无偏移。

## 2. 吸附机制详解

### 机制1：双酚 A 的双酚羟基氢键锚定与狭长疏水口袋接触

**描述**：人源 ERRγ LBD（PDB 2E2R，分辨率 1.60 Å，Rfree 0.197，chain A）结合 BPA（配体 2OH，即 4,4'-propane-2,2-diyldiphenol，chain A 残基 1401）：BPA 两个酚羟基中一个同时与 Glu275 和 Arg316 氢键，另一个与 Asn346 氢键，周围疏水接触（尤其 Tyr326）完成强结合；结合位点 AC1 含 11 个残基（Leu268、Ala272、Glu275、Met306、Leu309、Arg316、Tyr326、Leu345、Asn346、Ile349、Phe435）。异丙叉桥与两苯环占据狭长疏水口袋。残基编号与 UniProt P62508（ERR3_HUMAN，chain A 222-458）一一对应，无偏移
**关键官能团**：['酚羟基氢键锚（Glu275 羧酸根、Arg316 胍基、Asn346 酰胺）', '疏水口袋壁残基（Tyr326、Leu268、Ala272、Met306、Leu309、Leu345、Ile349、Phe435）']
**来源**：DOI 10.1093/jb/mvm158

### 机制2：组成型激活孤儿受体的预组织口袋与双酚骨架形状读出

**描述**：ERRγ 是孤儿核受体（内源配体未知）与组成型转录激活因子；其 LBD 疏水口袋在 apo 形式即为预组织构象。BPA 结合受体腔而口袋内部结构与 apo 形式相比无任何改变，并维持激活螺旋（helix 12）活性构象从而保留组成型活性（Matsushima 2007 摘要），故 ERRγ 对 BPA 的识别以预组织口袋形状读出为主。亲和力与选择性具定量窗口：BPA 结合 ERRγ 的 IC50 为 13.1 nM（[3H]4-OHT 示踪竞争实验），4-壬基酚与己烯雌酚弱 5-50 倍（Takayanagi 2006 摘要）。对类似物 4-α-枯基酚报道有诱导契合结合成分（Matsushima 2008 BBRC），显示形状读出并非绝对刚性锁钥
**关键官能团**：['预组织疏水口袋（LBD 螺旋围成的固有腔形）', '组成型激活螺旋 helix 12']
**来源**：DOI 10.1093/jb/mvm158

## 3. 结构特征与结构-功能关系

必须保留：① 与 BPA 两酚羟基互补的成对极性锚（Glu275/Arg316 羧酸根-胍基型 + Asn346 酰胺型氢键基序）；② 与双酚骨架（两苯环 + 异丙叉桥）几何互补的疏水口袋；③ 口袋预组织（apo 形式即成型，结合不重塑口袋内部）。可灵活调整：载体骨架、锚定基团化学（羧基/胍基/脲/硫脲）、孔壁疏水修饰程度、腔深与孔径。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶核受体结构域形态: ERRγ LBD construct 残基 216-459（222-458 对应 UniProt P62508，216-221 为表达标签），识别依赖预组织口袋三级结构，用作吸附须将识别基序移植/固定于固体载体 None
- 孤儿受体（内源配体未知）: ERRγ 内源配体未知，BPA 结合属有文献记载的内分泌干扰物-核受体相互作用（内分泌/毒理语境）；作 BPA 识别原型时提供机制层原理，而非可假设的天然生理识别方案 None
- 纳摩尔亲和依赖锚-腔组合: K(D) 5.5 nM（Matsushima 2007 摘要）与 IC50 13.1 nM（Takayanagi 2006 摘要）依赖 Glu275/Arg316/Asn346 氢键锚与疏水口袋的组合；材料移植中锚定几何或口袋形状丧失可能使亲和力与选择性大幅下降（机理推断） None

## 6. 相关原型

- cactus-spine
- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- fabp4-fatty-acid-pfas-binding

## 参考文献

[待补充]
