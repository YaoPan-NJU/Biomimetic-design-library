---
id: asbt-bile-acid-elevator-transporter
name: ASBT 胆汁酸电梯型磺酸腔转运体（ASBT Bile-Acid Elevator Sulfonate-Cavity Transporter）
category: 微生物
organism: Neisseria meningitidis（ASBT_NM 细菌同源物，PDB 3ZUY，基因 NMB0705，菌株 MC58）/ 顶端钠依赖胆汁酸转运体 ASBT（SLC10A2）家族
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 向量传质
  - 分子筛分
adsorption_mechanisms:
  - 预组织两亲阴离子腔对牛磺胆酸盐磺酸根头基的识别
  - 双钠协同驱动的电梯型交替通道（构象循环原理）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 11 verified, 0 unverified
# coverage: partial
# status: active
---
# ASBT 胆汁酸电梯型磺酸腔转运体（ASBT Bile-Acid Elevator Sulfonate-Cavity Transporter）

## 1. 生物原型简介

**问题定义**：胆固醇经转化为胆汁酸排出，约半数胆固醇由此清除；肠腔释放的胆汁酸须在含高浓度背景离子的肠内容物中被顶端钠依赖胆汁酸转运体（ASBT，SLC10A2）高效、选择性地重吸收以完成肠肝循环。蛋白如何以钠协同机制选择性识别两亲胆汁酸阴离子（疏水甾体骨架 + 极性阴离子头基）并驱动其跨膜易位，是分子识别与转运的基础问题。

**生物策略**：Hu 等解析 Neisseria meningitidis 的 ASBT 细菌同源物 ASBT_NM（PDB 3ZUY，2.2 Å）。结构含两组反向五跨膜螺旋重复；核心域六螺旋携带两个钠离子，其余四螺旋排成平板状板域（摘要逐字）。底物牛磺胆酸盐（taurocholate，牛磺酸共轭胆汁酸，牛磺酸末端为磺酸根头基）被捕获于核心域与板域间大型内向疏水腔（摘要逐字）；PDB SITE 记录该腔结合 TCH（AC3：Gly12/Lys13/Phe15/Phe28/Ile47/Thr112/Ala113/Val116/Leu120/Ser199/Val200/Ile203/Asn295 等），两个 Na⁺ 位点为 AC1（Ser114/Asn115/Ser128/Thr132/Glu260）与 AC2（Gln77/Gly110/Glu260/Val261/Met263/Gln264）。Hu 由底物位置与分子构架提出转运机制雏形；后续 ASBT/SLC10 工作将其归为核心域携底物与 Na⁺ 相对板域移动的电梯型交替通道。Zhao 2015 在人/大鼠肝细胞与转染细胞实测：SLC10 家族胆汁酸转运体（NTCP、ASBT）参与全氟烷基磺酸盐（PFAS）处置，呈钠依赖与链长依赖；人 NTCP 转运 PFBS（Km 39.6 µM），但人 ASBT 仅转运 PFOS、大鼠 ASBT 不转运任一被测 PFAS。

## 2. 吸附机制详解

### 机制1：预组织两亲阴离子腔对牛磺胆酸盐磺酸根头基的识别

**描述**：ASBT_NM（PDB 3ZUY）以核心域与板域间的大型内向疏水腔结合天然底物牛磺胆酸盐（taurocholate，牛磺酸共轭胆汁酸，其牛磺酸末端为磺酸根头基 -SO3⁻）；腔的极性/钠端（两个 Na⁺ 位点 AC1：Ser114/Asn115/Ser128/Thr132/Glu260，AC2：Gln77/Gly110/Glu260/Val261/Met263/Gln264）识别阴离子头基，疏水壁（SITE AC3 记 Gly12/Lys13/Phe15/Phe28/Ile47/Thr112/Ala113/Val116/Leu120/Ser199/Val200/Ile203/Asn295 等）容纳甾体骨架，对两亲阴离子实现头基与骨架的同时识别
**关键官能团**：['钠离子配位残基（Ser/Asn/Thr/Glu/Gln 侧链，Na⁺ 位点 AC1/AC2）', '极性/带电头基识别残基（Lys/Asn/Ser/Thr）', '疏水甾体容纳壁（Phe/Ile/Leu/Val/Ala/Gly 疏水残基）', '预组织两亲阴离子腔（核心域-板域界面）']
**来源**：DOI 10.1038/nature10450

### 机制2：双钠协同驱动的电梯型交替通道（构象循环原理）

**描述**：ASBT_NM 含两组反向五跨膜螺旋重复；核心域（六螺旋，含两个 Na⁺ 位点 AC1/AC2）承载底物，板域（四螺旋平板）作支架；底物牛磺胆酸盐结合于核心域与板域间内向腔。Hu 2011 由底物位置与分子构架提出转运机制雏形，后续 ASBT/SLC10 工作将其归为电梯型——核心域携底物与两个 Na⁺ 相对板域/支架移动，实现内向↔外向交替通道
**关键官能团**：['两组反向五跨膜螺旋重复', '核心域（六螺旋，两 Na⁺ 位点 AC1/AC2）', '板域/支架域（四螺旋平板）', '钠协同位点（Ser/Asn/Thr/Glu/Gln 配位 Na⁺）']
**来源**：DOI 10.1038/nature10450

## 3. 结构特征与结构-功能关系

必须保留：① 预组织两亲阴离子腔——极性/钠端（Na⁺ 位点与极性残基）锚定阴离子头基、疏水壁（Phe/Ile/Leu/Val）容纳疏水骨架；② 链长容纳几何（腔尺寸对底物链长的匹配）；③ 钠协同（两个 Na⁺ 稳定底物结合态）。天然机制类别：钠协同电梯型跨膜转运（动态传质类）。可灵活调整（转译层）：载体骨架、给体/疏水壁化学、腔尺寸与链长几何；完整跨膜转运循环不可移植。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 膜整合形态与去垢剂依赖: ASBT_NM 为整合膜蛋白，PDB 3ZUY 以去垢剂 LDAO（lauryl dimethylamine-N-oxide）胶束结晶，含多个 LDA 配体；单体约 33.9 kDa（PDB 3ZUY polymer_entity formula_weight），组装体 molecular_weight 37.59 kDa。识别腔依赖跨膜三级结构与脂质/去垢剂微环境，须移植/固定于固体载体方可用作吸附 None
- 电梯型构象循环依赖: 完整转运依赖核心域相对板域/支架的电梯型构象位移与钠梯度驱动的交替通道；固定化为静态吸附位点时丧失跨膜转运循环，仅保留识别腔几何与头基/链长读取 None
- 链长选择性约束（转译风险）: SLC10 家族对全氟烷基磺酸盐呈链长依赖：人 NTCP Km PFBS 39.6 < PFHxS 112 < PFOS 130 µM；人 ASBT 仅转运 PFOS、大鼠 ASBT 不转运所测任一 PFAS，PFBS 由 NTCP 而非 ASBT 转运。ASBT 衍生腔可能继承偏向长链的选择性，对短链 PFBS 的亲和力/选择性须实验验证 µM（NTCP Km，旁证）

## 6. 相关原型

- cell-membrane-ion-channel
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- diatom-frustule

## 参考文献

[待补充]
