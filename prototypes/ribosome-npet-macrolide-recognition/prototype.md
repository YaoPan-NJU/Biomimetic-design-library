---
id: ribosome-npet-macrolide-recognition
name: 核糖体新生肽出口隧道大环内酯识别（Ribosomal Nascent Polypeptide Exit Tunnel (NPET) Macrolide Recognition）
category: 微生物
organism: Deinococcus radiodurans（50S 核糖体亚基新生肽出口隧道 NPET / 肽基转移酶中心 PTC；大环内酯为链霉菌属 Streptomyces 次级代谢产物）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
adsorption_mechanisms:
  - NPET/PTC 受限几何对 14 元大环内酯（罗红霉素）的形状读出
  - 14 元大环内酯在核糖体肽键形成位点的慢结合竞争动力学
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 8 verified, 0 unverified
# coverage: partial
# status: active
---
# 核糖体新生肽出口隧道大环内酯识别（Ribosomal Nascent Polypeptide Exit Tunnel (NPET) Macrolide Recognition）

## 1. 生物原型简介

**问题定义**：大环内酯抗生素（红霉素、罗红霉素、克拉霉素等 14 元大环内酯）是链霉菌属次级代谢产物，长期与细菌共进化，通过占据核糖体 50S 亚基新生肽出口隧道（NPET）抑制翻译。分子层面的问题是：核糖体 NPET 这一受限隧道如何对 14 元大环内酯骨架实现选择性识别，以及该识别可否抽取为对同类分子（如水中罗红霉素 ROX）的形状读出原理。

**生物策略**：Deinococcus radiodurans 50S 与罗红霉素复合物的晶体结构（PDB 1JZZ，X 射线 3.8 Å，Schlünzen 2001，标题为抗生素与真细菌肽基转移酶中心相互作用的结构基础）显示罗红霉素（RCSB 关键词与配体实体 5）占据 NPET/PTC 受限区域；14 元大环内酯的糖基与内酯部分与隧道衬里（23S rRNA 与核糖体蛋白）形成多点接触。Kalpaxis 2003（DOI 10.1124/mol.63.3.617）以慢结合动力学比较红霉素、罗红霉素、克拉霉素与具有肽键形成活性的细菌核糖体复合物的体外相互作用，表明三种 14 元大环内酯竞争同一受限位点。识别由受限隧道的几何形状读出加多点氢键网络共同实现。具体 rRNA 残基编号本文未做坐标级审计。

## 2. 吸附机制详解

### 机制1：NPET/PTC 受限几何对 14 元大环内酯（罗红霉素）的形状读出

**描述**：大环内酯抗生素与细菌长期共进化，作为次级代谢产物天然占据 50S 核糖体亚基新生肽出口隧道（NPET）近肽基转移酶中心（PTC）的受限区域并抑制翻译。PDB 1JZZ 为 Deinococcus radiodurans 50S 与罗红霉素（roxithromycin，14 元大环内酯）复合物，罗红霉素为沉积配体实体 5；受限隧道以尺寸匹配狭缝加多点氢键网络对 14 元大环内酯骨架作形状读出
**关键官能团**：['受限 NPET 隧道衬里（23S rRNA 核糖核酸碱基与骨架及核糖体蛋白，构成受限氢键/范德华口袋；具体残基编号未审计）', '大环内酯糖基羟基与内酯羰基（多点氢键受体/给体）', '罗红霉素 C9 肟醚']
**来源**：DOI 10.1038/35101544

### 机制2：14 元大环内酯在核糖体肽键形成位点的慢结合竞争动力学

**描述**：红霉素、罗红霉素、克拉霉素（均为 14 元大环内酯）以慢结合动力学竞争同一具有肽键形成活性的细菌核糖体复合物位点（Kalpaxis 2003），表明 NPET/PTC 对 14 元大环内酯存在共享的受限识别位点
**关键官能团**：['大环内酯环骨架（14 元内酯）', '去氧糖/克拉定糖羟基与内酯羰基（氢键位点）']
**来源**：DOI 10.1124/mol.63.3.617

## 3. 结构特征与结构-功能关系

必须保留：① 与 14 元大环内酯骨架几何互补的受限狭缝/隧道（尺寸匹配）；② 隧道衬里极性基团对糖基羟基/内酯羰基/肟醚的多点氢键网络；③ 预组织受限微环境。可灵活调整：载体骨架、腔尺寸与给体排布、疏水微环境。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 核糖体为超大分子机器: 50S 亚基约 MDa 量级、由 23S/5S rRNA 与数十种核糖体蛋白组装；无法直接作吸附材料，须将受限几何识别原理抽取至合成载体 None
- NPET 受限几何依赖完整三级结构: 大环内酯识别依赖 NPET/PTC 的预组织受限隧道；rRNA 折叠破坏或隧道溶剂化使几何与氢键网络丧失 None
- 14 元大环内酯骨架尺寸匹配: NPET 容纳 14 元大环内酯（罗红霉素在 PDB 1JZZ 占据 PTC/NPET，配体实体 5）；环尺寸显著失配的分子识别减弱 None
- 结合属翻译语境: 大环内酯-NPET 结合的生理读出为翻译抑制（肽键形成受阻），非环境水相 ROX 清除；转译为吸附须重构识别内核 None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[待补充]
