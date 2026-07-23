---
id: oat4-organic-anion-transporter
name: OAT4 有机阴离子转运体（OAT4 Organic Anion Transporter (SLC22A11)）
category: 动物
organism: Homo sapiens（OAT4/SLC22A11 有机阴离子转运体；结构接地含 Rattus norvegicus OAT1/SLC22A6）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 分子筛分
adsorption_mechanisms:
  - 阴离子头基与芳香-阳离子底物口袋的两点位识别（硫酸结合型有机阴离子）
  - 顶端有机阴离子/二羧酸交换（二羧酸外排梯度驱动的向量重吸收）
  - 疏水骨架容纳与有限容积口袋的尺寸窗口（链长选择性结构基础）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 16 verified, 5 unverified
# coverage: partial
# status: active
---
# OAT4 有机阴离子转运体（OAT4 Organic Anion Transporter (SLC22A11)）

## 1. 生物原型简介

**问题定义**：全氟烷基物质（PFOA/PFBS 等）在水环境中以持久性有机阴离子形态存在（羧酸根/磺酸根头基加全氟烷基链），选择性捕获需同时解决阴离子头基识别与全氟链链长（C4/C8）区分。人肾近端小管顶端膜 OAT4 恰以高亲和力识别结构多样的有机阴离子，且文献报道其对全氟烷基酸的转运呈结构（链长）相关差异，是有机阴离子头基加链长窗口的分子识别原型。

**生物策略**：OAT4（SLC22A11，550 氨基酸残基、12 跨膜域）以钠离子非依赖方式高亲和力转运硫酸结合型有机阴离子 E1S（Km 1.01 µM）与 DHEAS（Km 0.63 µM），并转运赭曲霉毒素 A（Cha 2000）。人 OAT4·DHEAS 复合物冷冻电镜结构 PDB 9U5A（2025-06-18 释放）坐标直测示 DHEAS 口袋含芳香残基 Phe211/Phe238/Tyr360/Tyr361 与阳离子 Arg389、极性 Gln242（chain A），与 SLC22 保守芳香笼加阳离子锚同源（大鼠 OAT1 PDB 8SDY：Tyr230/Phe438/Tyr353/Phe443 芳香笼 + Lys382/Arg466，Dou 2023 NSMB，PMC11406556；PAH 芳基被 Tyr230/Phe438 钳夹、羧基转向阳离子残基）。OAT4 以顶端有机阴离子/二羧酸交换体运作，戊二酸与 E1S/PAH 双向反式刺激，重吸收由外向二羧酸梯度驱动（Ekaratanawong 2004）。底物口袋容积有限（rOAT1 直测约 15 Å × 7 Å × 13 Å），容忍化学异质骨架（多特异性），构成链长窗口的结构基础。

## 2. 吸附机制详解

### 机制1：阴离子头基与芳香-阳离子底物口袋的两点位识别（硫酸结合型有机阴离子）

**描述**：人 OAT4（SLC22A11，550 氨基酸残基、12 跨膜域）表达于肾近端小管顶端膜与胎盘，以高亲和力、钠离子非依赖方式转运硫酸结合型有机阴离子：雌酮硫酸酯 E1S（Km 1.01 µM）与硫酸脱氢表雄酮 DHEAS（Km 0.63 µM），并转运赭曲霉毒素 A（Cha 2000）。人 OAT4·DHEAS 冷冻电镜结构 PDB 9U5A（2025-06-18 释放）坐标直测：配体 ZWY（DHEAS，17-氧代雄甾-5-烯-3β-基硫酸氢酯）4.0 Å 内含芳香残基 Phe211、Phe238、Tyr360、Tyr361、Met231 与阳离子 Arg389、极性 Gln242（chain A，PDB 编号）；该芳香笼加阳离子锚为 SLC22 家族保守底物结合基序（大鼠 OAT1 PDB 8SDY 同源直测：Tyr230/Phe438/Tyr353/Phe443 芳香笼 + Lys382/Arg466 阳离子残基，Dou 2023）
**关键官能团**：['阳离子残基（Arg389 邻接位，chain A PDB 编号）', '极性残基（Gln242 邻接位）', '芳香笼（Phe211/Phe238/Tyr360/Tyr361 邻接位）']
**来源**：DOI 10.1074/jbc.275.6.4507

### 机制2：顶端有机阴离子/二羧酸交换（二羧酸外排梯度驱动的向量重吸收）

**描述**：OAT4 是顶端有机阴离子/二羧酸交换体：戊二酸（glutarate, GA）抑制 E1S 摄取（IC50 1.25 mM）；预载 GA 反式刺激 E1S 摄取，胞外 E1S 反式刺激 GA 外排；E1S 与 PAH 的摄取与外排均可被 GA 或 PAH 反式刺激（Ekaratanawong 2004）。免疫组化示 OAT4 位于肾近端小管顶端膜（与基底侧 hOAT1/hOAT3 同一管群），主要作为顶端重吸收通路
**关键官能团**：['有机阴离子/二羧酸交换位点', '顶端膜定位基序']
**来源**：DOI 10.1254/jphs.94.297

### 机制3：疏水骨架容纳与有限容积口袋的尺寸窗口（链长选择性结构基础）

**描述**：OAT 底物口袋为 NTD 与 CTD 之间的大腔：大鼠 OAT1·PAH/丙磺舒复合物直测口袋约 15 Å 宽 × 7 Å 深 × 13 Å 高（Dou 2023）；PAH 芳基被 Tyr230 与 Phe438 钳夹、Tyr353 以 edge-to-face 方式参与，底物可在笼内调整取向（柔性结合），且 PAH 与丙磺舒结合于 NTD/CTD 腔末端同一位点。OAT4 与化学异质的阴离子化合物相互作用（NSAIDs、利尿剂、磺溴酞钠、青霉素 G、胆汁酸盐、甾体硫酸酯、赭曲霉毒素 A），呈多特异性；9U5A 中 DHEAS 甾体骨架被 Phe211/Phe238/Tyr360/Tyr361/Met231 包围（坐标直测 ≤4.0 Å）
**关键官能团**：['芳香-疏水笼（π-夹/edge-to-face）', '有限容积底物口袋']
**来源**：DOI 10.1038/s41594-023-01123-3

## 3. 结构特征与结构-功能关系

必须保留：① 阴离子头基的阳离子/极性锚（Arg389/Gln242 邻接位）；② 疏水骨架的芳香-疏水笼（Phe211/Phe238/Tyr360/Tyr361 邻接位）；③ 有限容积口袋的尺寸窗口；④ 摄取与再生共用位点的交换逻辑。可灵活调整：载体骨架与孔结构、锚定位点密度与电荷、孔道宽度与疏水性、再生驱动力形式（以竞争阴离子或 pH 切换替代代谢性二羧酸梯度）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 整合膜蛋白形态: OAT4 为 550 氨基酸残基、12 跨膜域的整合膜蛋白；识别口袋依赖膜内三级结构，直接用于吸附需膜囊泡/脂质体固定化或识别基序移植 None
- 交换驱动力依赖: 天然重吸收由胞内外向二羧酸梯度（戊二酸/α-酮戊二酸）驱动；静态吸附体系无代谢梯度，需以竞争阴离子洗脱或 pH 头基电荷切换替代 None
- 固有选择性有限（多特异性）: OAT4 固有地与化学异质的阴离子化合物相互作用（NSAIDs、利尿剂、磺溴酞钠、青霉素 G、胆汁酸盐、甾体硫酸酯、赭曲霉毒素 A），对单一目标分子选择性低，吸附设计须叠加额外选择性要素 None
- 结构文献尚未同行评审: 人 OAT4 冷冻电镜结构 PDB 9U5A（DHEAS 复合物）与 9M9Y（apo）于 2025-06-18 释放，引文标注 To be published；残基级功能归属（如 Arg389、Gln242 个体贡献）待同行评审文献支持 None
- 口袋容积位阻上限: 大鼠 OAT1 底物口袋直测约 15 Å 宽 × 7 Å 深 × 13 Å 高；同源 OAT4 口袋对全氟烷基链（C8 PFOA 全伸展约 1 nm 量级）的链长窗口定量阈值属定性外推 Å

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- cell-membrane-ion-channel
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation

## 参考文献

[待补充]
