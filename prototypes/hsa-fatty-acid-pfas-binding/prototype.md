---
id: hsa-fatty-acid-pfas-binding
name: 人血清白蛋白脂肪酸结合位点（FA1-FA7）（Human Serum Albumin Fatty Acid Binding Sites (FA1-FA7)）
category: 动物
organism: Homo sapiens（人血清白蛋白 HSA，血浆脂肪酸转运蛋白）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 疏水性
adsorption_mechanisms:
  - 长链脂肪酸的羧酸头基阳离子/氢键锚定与烃链疏水容纳
  - 脂肪酸结合位点 FA1-FA7 的多位点不对称分布与跨位点保守头基锚
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 人血清白蛋白脂肪酸结合位点（FA1-FA7）（Human Serum Albumin Fatty Acid Binding Sites (FA1-FA7)）

## 1. 生物原型简介

**问题定义**：长链脂肪酸不溶于血浆水相，须由载体蛋白可逆结合并转运。人血清白蛋白（HSA，约 66-69 kDa）是血浆丰度最高的蛋白，承担脂肪酸从摄取组织向代谢组织的转运，是脂肪酸体液分布的主要决定蛋白。分子层面的问题是：单个白蛋白分子如何在水相中同时可逆结合多个两亲性脂肪酸分子。

**生物策略**：HSA 以分布于三个结构域（I、II、III，各含 A/B 亚域）的 7 个主要脂肪酸位点（FA1-FA7）结合脂肪酸，位点分布不对称（Curry 1998，DOI 10.1038/1869，PDB 1BKE）。各位点以 Arg/Lys/Tyr 型阳离子与氢键给体锚定脂肪酸羧酸头基：如 FA2 位点（亚域 IIIA，Sudlow 位点 II）的 Arg410 与 Tyr411、FA1 位点的 Lys199 与 Arg218（PDB 1E7G SITE 记录）；侧壁 Leu/Phe 等疏水残基容纳烃链。Bhattacharya 2000（DOI 10.1006/jmbi.2000.4158）测定 HSA 与癸酸至硬脂酸系列复合物（PDB 1E7E-1E7I，C10-C18），显示中长链脂肪酸以共同模式结合、头基锚定保守。PDB 1BKE 中 5 个肉豆蔻酸分子同时占据不同位点，1E7G 中达 8 个，体现多位点高容量转运。PFAS 维度：全氟辛烷磺酸（PFOS）以脂肪酸类似物形式占据 HSA 的 FA2 位点（Luo 2012，DOI 10.1021/tx300112p，PDB 4E99：配体 P8S 即全氟辛烷磺酸位于 A601/A602，SITE AC1 含 Arg410/Tyr411，与肉豆蔻酸位点 AC4 共享 Leu387/Arg410/Tyr411/Phe488/Ser489），即 PFAS 结合是脂肪酸模拟的碰巧占据，并非独立进化的 PFAS 识别位点。

## 2. 吸附机制详解

### 机制1：长链脂肪酸的羧酸头基阳离子/氢键锚定与烃链疏水容纳

**描述**：人血清白蛋白以分布于三个结构域的脂肪酸结合位点（FA1-FA7）结合长链脂肪酸；各位点以 Arg/Lys/Tyr 型阳离子与氢键残基锚定羧酸头基（如 FA2 位点 Arg410 与 Tyr411、FA1 位点 Lys199 与 Arg218，PDB 链 A 编号），侧壁 Leu/Phe 等疏水残基容纳长烃链；PDB 1E7G 为 HSA 与肉豆蔻酸（十四烷酸）复合物，链 A 含 8 个 MYR 配体分子
**关键官能团**：['阳离子/氢键给体（Arg410、Tyr411、Lys199、Arg218、Arg117、Tyr138、Lys73 等位点头基锚）', '疏水侧壁残基（Leu387、Leu460、Phe488、Tyr150、Arg257 邻壁等）', '三域 α 螺旋束骨架']
**来源**：DOI 10.1006/jmbi.2000.4158

### 机制2：脂肪酸结合位点 FA1-FA7 的多位点不对称分布与跨位点保守头基锚

**描述**：HSA 含 7 个主要脂肪酸结合位点（FA1-FA7），不对称分布于 I、II、III 三个结构域（PDB 1BKE 中 5 个肉豆蔻酸分子同时占据不同位点）；跨位点头基锚化学保守为 Arg/Lys/Tyr 型极性残基（如 PDB 1E7G 位点 AC1 的 Arg117/Tyr138/Tyr161、位点 AC4 的 Arg410/Tyr411、位点 AC7 的 Lys199/Arg218）
**关键官能团**：['阳离子/氢键给体（多位点 Arg117、Tyr138、Tyr161、Lys73、Lys199、Arg218、Lys190 等）', '多位点疏水腔（FA1-FA7）']
**来源**：DOI 10.1038/1869

## 3. 结构特征与结构-功能关系

必须保留：① Arg/Lys/Tyr 型阳离子与氢键给体对羧酸头基的方向性锚定；② 容纳长烃链的疏水侧壁（Leu/Phe/Met 型）；③ 多位点、可逆、水相容的结合架构。须警惕：该化学对一切羧酸型两亲阴离子广谱，不区分脂肪酸与 PFAS；HSA 本身为 66-69 kDa 可溶蛋白且天然承担药物结合（Sudlow 位点 I/II），直接仿生只得广谱结合位点。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶大蛋白形态: HSA 为血浆可溶性单链蛋白（RCSB 1BKE 记 molecular_weight 68.28 kDa），识别依赖完整三域三级结构，用作吸附须固定化或仅提取设计原则 None
- 头基锚广谱性（非 PFAS 特异）: Arg/Lys/Tyr 头基锚对所有羧酸型两亲阴离子广谱结合（脂肪酸及经 Sudlow 位点的多种药物）；对该位点的仿生不提供 PFOA 相对脂肪酸/腐殖酸的选择性 None
- PFAS 同位点碰巧占据（警示）: PFOS 占据 HSA FA2 位点（PDB 4E99 SITE AC1 含 ARG A 410、TYR A 411），与肉豆蔻酸位点（PDB 1E7G SITE AC4）共享 Leu387/Arg410/Tyr411/Phe488/Ser489 五个接触残基，属脂肪酸类似物的同位点碰巧占据而非独立进化的 PFAS 识别 None

## 6. 相关原型

- cactus-spine
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding
- lipocalin-hydrophobic-calyx
- lotus-leaf

## 参考文献

[待补充]
