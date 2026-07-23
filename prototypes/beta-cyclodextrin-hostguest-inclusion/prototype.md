---
id: beta-cyclodextrin-hostguest-inclusion
name: β-环糊精主客体包结识别（beta-Cyclodextrin Host-Guest Inclusion Recognition）
category: 植物
organism: 环糊精：直链淀粉（植物多糖，α-D-吡喃葡萄糖 α-1,4）经细菌 CGTase 酶促环化的天然环状寡糖；β-CD 为 7 葡萄糖单元大环
biomimetic_dimension: 分子仿生
features:
  - 疏水性
  - 分子筛分
adsorption_mechanisms:
  - β-环糊精疏水内腔的主客体包结识别
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: medium
# provenance: 5 papers, 2 verified, 0 unverified
# coverage: partial
# status: active
---
# β-环糊精主客体包结识别（beta-Cyclodextrin Host-Guest Inclusion Recognition）

## 1. 生物原型简介

**问题定义**：水中痕量有机微污染物（内分泌干扰物、药物、农药、紫外过滤剂等）种类多、浓度低（ng/L–µg/L），活性炭动力学慢、再生能耗高，需快速、可温和再生、耐真实基质的水相吸附材料。

**生物策略**：β-环糊精为直链淀粉经细菌 CGTase 环化的天然环状寡糖，7 葡萄糖大环具疏水内腔、亲水外缘，水相中以疏水效应+尺寸互补包结芳香/疏水客体（CD-氯酚 NMR 1:1 包结；β-CD:BPA Ka≈3.6–4.1×10³ M⁻¹）。Alsbaiee & Dichtel 2016 将 β-CD 交联为多孔聚合物，快速去除多种有机微污染物、吸附速率常数为活性炭 15–200 倍、在环境相关浓度优于活性炭且可温和再生。

## 2. 吸附机制详解

### 机制1：β-环糊精疏水内腔的主客体包结识别

**描述**：β-CD 7 葡萄糖锥筒外缘亲水、内腔疏水；水相经疏水效应与范德华/尺寸互补将芳香/疏水客体包结进内腔形成 1:1（或 2:1）复合物，客体自体相水去溶剂进入低极性腔为主要驱动力。
**关键官能团**：['β-环糊精疏水内腔（7 葡萄糖大环）', '外缘羟基（亲水/可交联把手）']
**来源**：DOI 10.1038/nature16185

## 3. 结构特征与结构-功能关系

必须保留：① β-CD 疏水内腔（尺寸-客体匹配的包结位点）；② 外缘羟基作交联/亲水把手；③ 多孔化以获高可及位点与快动力学。可灵活调整：交联剂化学、孔结构、颗粒形态。边界：1:1 容量上限、广谱非特异。

## 4. 已报道性能数据

[待补充]（吸附性能以交联多孔 β-CD 聚合物形态报道：Alsbaiee & Dichtel 2016 去除速率为活性炭 15–200 倍；具体 qmax/Kd 数值留待审计逐条接地，本 JSON 不搬运）

## 5. 适用场景

**约束条件**：
- 1:1 容量上限：单位 β-CD 一个内腔，纯位点容量有硬上限（β-CD:BPA 约 201 mg/g 纯位点），交联/载体摊薄总容量
- 需交联多孔化：游离 β-CD 水溶，须交联为不溶多孔聚合物方可作吸附剂
- 广谱非特异：包结为广谱疏水富集，靶标特异性有限，同尺寸疏水共存物竞争同一内腔

## 6. 相关原型

- lipocalin-hydrophobic-calyx
- hsa-fatty-acid-pfas-binding

## 参考文献

- Alsbaiee, Dichtel 等，Rapid removal of organic micropollutants from water by a porous β-cyclodextrin polymer，Nature 2016, 529:190-194，DOI 10.1038/nature16185
- CD-氯酚包结 NMR，DOI 10.1023/A:1008150908997
- CD 聚合物选择性吸附，DOI 10.1039/d0cc04784h
- β-CD 聚合物吸附剂水基质效应评估（RSSCT），DOI 10.1016/j.watres.2020.115551
- Kawano 2014 ES&T（γ-CD 聚合物容纳大体积客体），DOI 10.1021/es501243v

> 诚实边界：主客体包结机制成熟且有真实吸附材料先例（Dichtel 多孔 β-CD 聚合物，摘要级外部核验）；靶标选择性增强为 inspiration/llm_inferred；1:1 容量上限与广谱非特异为硬边界；分类（天然寡糖 vs 合成聚合物材料）留待审计定 tier 与归类。
