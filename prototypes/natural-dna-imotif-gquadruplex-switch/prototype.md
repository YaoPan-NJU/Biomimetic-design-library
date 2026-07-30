---
id: natural-dna-imotif-gquadruplex-switch
name: 天然核酸二级结构分子开关（i-motif / G-四链体）（Natural Nucleic-Acid Secondary-Structure Conformational Switch (i-motif / G-quadruplex)）
category: 动物
organism: Homo sapiens（人端粒 C 富集链 i-motif 与 (TTAGGG)n G 富集重复 G-四链体；端粒/启动子区天然存在的核酸二级结构，非 SELEX 体外筛选适配体）
biomimetic_dimension: 分子仿生
features:
  - 动态响应
  - pH 响应
adsorption_mechanisms:
  - i-motif 酸性触发的半质子化 C·C⁺ 折叠（构象开关折叠态）
  - G-四链体 Hoogsteen G-四分体堆叠与 K⁺ 稳定（构象开关折叠态）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 8 verified, 0 unverified
# coverage: partial
# status: active
---
# 天然核酸二级结构分子开关（i-motif / G-四链体）（Natural Nucleic-Acid Secondary-Structure Conformational Switch (i-motif / G-quadruplex)）

## 1. 生物原型简介

**问题定义**：真核端粒与基因启动子区在进化中形成 i-motif 与 G-四链体等天然核酸二级结构，参与端粒保护与基因调控。i-motif 由 C 富集链在酸性条件下经胞嘧啶半质子化折叠，G-四链体由 G 富集重复经 Hoogsteen 氢键四分体堆叠并由 K⁺ 稳定。二者是自然界存在的 pH/离子响应构象开关，属自然进化序列而非 SELEX 体外筛选适配体，满足自然界进化解决方案判据。其可逆构象切换能否转译为吸附-再生的动态维度，是动态响应仿生的问题。

**生物策略**：人端粒 C 富集链 d(CCCTA2CCCTA2CCCTA2CCCT) 分子内折叠为 i-motif，四段胞嘧啶 stretches 形成六重 intercalated C·C⁺ 配对，终止于各段 5' 端胞嘧啶（PDB 1ELN NMR；Phan 2000 摘要逐字 'six intercalated C.C+ pairs'）。人端粒 G 富集重复 (TTAGGG)n 在 K⁺ 中分子内折叠为 G-四链体，三层 G-tetrad（Hoogsteen 氢键鸟嘌呤四联体）经混合平行-反平行 G 链连接，K⁺ 居中稳定（PDB 2HY9 NMR hybrid-1 型；Dai 2007 摘要逐字 'three G-tetrads linked with mixed parallel-antiparallel G-strands' 与 'formed in human telomeric DNA in K(+)'）。i-motif 的酸性折叠与 G-四链体的阳离子折叠均为可逆构象切换，构成 pH/离子门控的天然构象开关。

## 2. 吸附机制详解

### 机制1：i-motif 酸性触发的半质子化 C·C⁺ 折叠（构象开关折叠态）

**描述**：人端粒 C 富集链 d(CCCTA2CCCTA2CCCTA2CCCT) 在酸性条件下经胞嘧啶 N3 半质子化形成 intercalated C·C⁺ 配对，分子内折叠为 i-motif：四段胞嘧啶 stretches 构成六重交替插入的 C·C⁺ 配对（PDB 1ELN NMR 结构）。折叠态（紧凑）与去折叠态（伸展）之间的 pH 可逆切换构成构象开关
**关键官能团**：['半质子化胞嘧啶 N3（intercalated C·C⁺ 配对，i-motif 折叠致动基团）', 'TA2 连接环（折叠拓扑的环跨结构）']
**来源**：DOI 10.1006/jmbi.2000.3613

### 机制2：G-四链体 Hoogsteen G-四分体堆叠与 K⁺ 稳定（构象开关折叠态）

**描述**：人端粒 G 富集重复 (TTAGGG)n 在 K⁺ 溶液中分子内折叠为 G-四链体：三层 G-四分体（G-tetrad）经 Hoogsteen 氢键连接的鸟嘌呤四联体堆叠而成，中心通道由 K⁺ 占据稳定（PDB 2HY9 NMR hybrid-1 型）。K⁺ 依赖的折叠/去折叠构成离子门控构象开关，与 i-motif 的 pH 门控互补
**关键官能团**：['Hoogsteen 氢键鸟嘌呤四联体（G-tetrad，G-四链体堆叠致动基团）', '中心通道 K⁺（稳定 G-tetrad 堆叠）']
**来源**：DOI 10.1093/nar/gkm009

## 3. 结构特征与结构-功能关系

必须保留：① 半质子化 intercalated C·C⁺ 拓扑（i-motif pH 门控折叠的致动基团）；② Hoogsteen 氢键 G-tetrad 堆叠与中心 K⁺（G-四链体离子门控折叠的致动基团）；③ 折叠/去折叠的可逆性（动态响应输出）。可灵活调整：骨架化学（寡核苷酸改固定化于多孔载体/聚合物刷/水凝胶）、序列与折叠窗口的调谐、构象切换门控孔道可及性或位点几何的材料实现方式。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- i-motif 酸性触发依赖: i-motif 折叠依赖胞嘧啶半质子化（六重 intercalated C·C⁺ 配对，PDB 1ELN），折叠态与酸性条件耦合；具体折叠 pH 窗口依序列与缓冲液而定，须实测 None
- G-四链体阳离子依赖: G-四链体折叠依赖 K⁺（或特定单价阳离子）居中稳定三层 G-tetrad 堆叠（PDB 2HY9，K⁺ 溶液 hybrid-1 型）；离子环境改变使折叠态不稳定 None
- pH 窗口错配（i-motif 酸性触发 vs ROX 偏碱 pKa）: i-motif 酸性折叠窗口与 ROX（罗红霉素）叔胺 pKa 8.8-9.0（偏碱）相距较远，二者匹配性须实验测定；在 i-motif 折叠的酸性条件下 ROX 叔胺质子化呈阳离子态，对结合的影响不可先验判定 None
- DNA 固定化与稳定性（转译限原理层）: 构象开关为寡核苷酸，直接用作可循环吸附剂须固定于多孔载体并在流动条件下维持可逆折叠/去折叠；核酸酶降解、不可逆变性与固定化成本是关键工程约束 None

## 6. 相关原型

- fcrn-ph-dependent-fc-recycling
- hemoglobin-bohr-ph-allostery
- lysosome-acid-ion-trapping-ph-switch
- mscl-mechanosensitive-channel
- natural-riboswitch-metabolite-sensing

## 参考文献

[待补充]
