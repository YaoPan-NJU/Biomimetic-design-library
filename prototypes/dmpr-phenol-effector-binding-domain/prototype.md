---
id: dmpr-phenol-effector-binding-domain
name: DmpR 苯酚效应物结合域（A 域）（DmpR Phenol Effector-Binding Domain (A domain / sensory domain)）
category: 微生物
organism: Pseudomonas putida KCTC 1452（DmpR 苯酚响应转录调控蛋白，又称 CapR）
biomimetic_dimension: 分子仿生
features:
  - 分子筛分
adsorption_mechanisms:
  - 疏水腔与 His100/Trp128 酚羟基定位对芳香效应物的识别
  - 效应物结合诱导感觉域构象变化与下游信号传递
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 1 papers, 9 verified, 0 unverified
# coverage: partial
# status: active
---
# DmpR 苯酚效应物结合域（A 域）（DmpR Phenol Effector-Binding Domain (A domain / sensory domain)）

## 1. 生物原型简介

**问题定义**：苯酚及取代酚是常见芳香族环境污染物，细菌需特异性感应它们以启动降解操纵子。DmpR（di-methyl phenol regulator，又称 CapR）源于 Pseudomonas putida KCTC 1452，是 σ54 依赖苯酚降解操纵子的单组分 AAA+ 转录激活蛋白（bEBP），其 N 端 A 域（感觉域）特异识别苯酚/取代酚效应物。A 域如何在分子层面识别酚类效应物、并将结合信号转化为转录激活，是芳香烃感应的机制基础问题。

**生物策略**：Park 等测定了苯酚结合活性态 DmpR 的晶体结构（PDB 6IY8，DmpRΔD 构建体）：苯酚结合 A 域形成由两个头对头二聚体以头尾排列组成的四聚体。A 域以 V4R 支架的（β/α）4 桶构成反平行发夹基序围成的封闭疏水腔（约 24–36 Å³）容纳苯酚芳环，腔壁主要为 Phe93、Trp128、Tyr155、Tyr170、Tyr159 等疏水残基；酚羟基定位于 His100 与 Trp128 之间（氢键/定位功能；PDB SITE AC1 记录结合残基 Pro97/His100/Val108/Met126/Trp128/Ala156/Ser160）。His100 保守存在于酚响应调控蛋白 PoxR/MopR，而在甲苯/二甲苯响应 XylR 中被酪氨酸取代，是酚类与甲苯类效应物特异性的关键决定簇。苯酚结合诱导口袋构象变化与感觉域 C 端 α6 螺旋位移，经卷曲螺旋 B-linker 将信号传至下游 AAA+ ATPase 域，激活 σ54 依赖转录。苯酚与 DmpR 的结合亲和力为低微摩尔级（DmpRΔD Kd 约 12 μM，全长约 16 μM）。

## 2. 吸附机制详解

### 机制1：疏水腔与 His100/Trp128 酚羟基定位对芳香效应物的识别

**描述**：DmpR 的 A 域（感觉域）以 vinyl-4-reductase（V4R）支架的（β/α）4 桶构成反平行发夹基序围成的封闭疏水腔（约 24–36 Å³）；苯酚芳环入腔，腔壁主要为 Phe93、Trp128、Tyr155、Tyr170、Tyr159 等疏水残基，酚羟基定位于 His100 与 Trp128 之间（氢键/定位功能）。PDB 6IY8（chain A）SITE AC1 记录的苯酚结合位点残基为 Pro97、His100、Val108、Met126、Trp128、Ala156、Ser160，与正文 His100/Trp128 描述一致。苯酚与 DmpR 的结合亲和力为低微摩尔级（DmpRΔD Kd 约 12 μM，全长约 16 μM）
**关键官能团**：['疏水腔壁残基（Phe93、Trp128、Tyr155、Tyr170、Tyr159）', '酚羟基定位残基（His100、Trp128）', 'V4R/（β/α）4 桶支架']
**来源**：DOI 10.1038/s41467-020-16562-5

### 机制2：效应物结合诱导感觉域构象变化与下游信号传递

**描述**：苯酚结合 A 域诱导配体结合口袋构象变化，继而使感觉域 C 端柔性 α6 螺旋位移，经卷曲螺旋 B-linker 将效应物结合信号传递至下游 AAA+ ATPase 域，促进头对头二聚体进一步组装为活性四聚体并与 σ54-RNAP 相互作用，激活苯酚降解操纵子的 σ54 依赖转录
**关键官能团**：['苯酚结合口袋（同 DMPR-001）', '卷曲螺旋 B-linker（信号传递）']
**来源**：DOI 10.1038/s41467-020-16562-5

## 3. 结构特征与结构-功能关系

必须保留：① 与单苯环尺寸/形状互补的封闭疏水腔（芳环容纳，范德华/疏水）；② 与酚羟基几何互补的保守极性锚（His100/Trp128 型氢键给体/受体）；③ 预组织的发夹/桶状口袋几何。可灵活调整：载体骨架、腔尺寸与疏水微环境、锚定基团化学（咪唑/脲/硫脲/硼酸酯）、是否保留变构输出。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶蛋白/多聚体形态: DmpR 为胞内可溶蛋白（单体约 66 kDa，苯酚结合活性四聚体约 264 kDa）；A 域识别依赖完整 V4R/（β/α）4 桶折叠，用作吸附须固定化/移植于固体载体 None
- 苯酚结合亲和力低微摩尔级: DmpR-苯酚结合解离常数为低微摩尔级（DmpRΔD Kd 约 12 μM，全长约 16 μM）；识别低浓度酚类污染物受亲和力约束，材料化须以多价/局部浓缩增强有效亲和 None
- 口袋几何与邻位取代容忍度: 疏水腔为约 24–36 Å³ 封闭小腔，与单苯环互补；DmpR 已表征效应物为苯酚与烷基取代酚，双邻位卤代酚（如 2,6-DCP）的适配性未知 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding
- lipocalin-hydrophobic-calyx

## 参考文献

[待补充]
