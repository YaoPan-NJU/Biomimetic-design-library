---
id: p450bisd-bisphenol-monooxygenase
name: P450bisd 双酚单加氧酶（P450bisd Bisphenol Monooxygenase）
category: 微生物
organism: Sphingobium (原 Sphingomonas) sp. strain AO1（P450bisd 双酚 A 降解细胞色素 P450 单加氧酶）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
adsorption_mechanisms:
  - P450bisd 单加氧酶对双酚 A 的催化转化（酶学机制）
  - 保守 P450 折叠的底物口袋与活化氧几何（P450cam 同源结构代理）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 11 verified, 0 unverified
# coverage: partial
# status: active
---
# P450bisd 双酚单加氧酶（P450bisd Bisphenol Monooxygenase）

## 1. 生物原型简介

**问题定义**：双酚 A（BPA）是大量使用的工业单体，具内分泌干扰活性，在环境中广泛检出。自然界是否存在能真正降解 BPA 骨架的微生物酶学方案，是生物修复与仿生设计的基础问题。Sphingobium（原 Sphingomonas）sp. strain AO1 能降解 BPA，但其降解酶的化学本质此前不明。

**生物策略**：Sasaki 等（2005）纯化了 strain AO1 的 BPA 降解单加氧酶系统三个组分：细胞色素 P450（P450bisd，约 102.3 kDa 同源二聚体）、铁氧还蛋白（Fd(bisd)，约 19.1 kDa，含 putidaredoxin 型 [2Fe-2S] 簇）与铁氧还蛋白还原酶（Red(bisd)）。P450bisd 在 Fd(bisd)/Red(bisd)/NADH 存在下转化 BPA，Km 约 85 μM、kcat 约 3.9 min⁻¹；NADPH 与菠菜铁氧还蛋白/还原酶仅给弱活性，显示电子传递链严格特异性。HPLC 检出两个降解产物，经质谱推断为 1,2-bis(4-hydroxyphenyl)-2-propanol 与 2,2-bis(4-hydroxyphenyl)-1-propanol（羟基化丙醇类，对应 ipso-羟基化转化路线）。这是首次证明细菌细胞色素 P450 单加氧酶系统参与 BPA 降解。P450bisd 无已解析晶体结构，其底物口袋几何以 CYP101 家族同源 P450cam（PDB 1DZ4，恶臭假单胞菌，高铁细胞色素 P450cam，Schlichting 2000 Science 287:1615）作保守折叠代理接地：细菌 P450 共享埋藏血红素口袋与血红素铁上方的活化氧几何，底物在口袋内相对活化氧的定位决定氧化转化的位点选择性。

## 2. 吸附机制详解

### 机制1：P450bisd 单加氧酶对双酚 A 的催化转化（酶学机制）

**描述**：Sphingobium (原 Sphingomonas) sp. strain AO1 的细胞色素 P450 单加氧酶系统参与双酚 A（BPA）降解：纯化的组分包括细胞色素 P450（P450bisd）、铁氧还蛋白（Fd(bisd)，含 putidaredoxin 型 [2Fe-2S] 簇）与铁氧还蛋白还原酶（Red(bisd)）；P450bisd 在 Fd(bisd)、Red(bisd) 与 NADH 存在下转化 BPA，Km 约 85 μM、kcat 约 3.9 min⁻¹；检出两个羟基化降解产物（1,2-bis(4-hydroxyphenyl)-2-propanol 与 2,2-bis(4-hydroxyphenyl)-1-propanol），属 ipso-羟基化转化路线
**关键官能团**：['血红素活化氧（细胞色素 P450 催化中心）', '铁氧还蛋白 [2Fe-2S] 电子传递簇', '底物口袋（双酚骨架夹持几何）']
**来源**：DOI 10.1128/AEM.71.12.8024-8030.2005

### 机制2：保守 P450 折叠的底物口袋与活化氧几何（P450cam 同源结构代理）

**描述**：P450bisd 本身无已解析晶体结构（RCSB 检索未直接命中）；以 CYP101 家族同源 P450cam（恶臭假单胞菌 Pseudomonas putida 高铁细胞色素 P450cam，PDB 1DZ4，Schlichting 2000 Science 287:1615）作底物口袋几何接地代理。P450cam 为氧化还原酶/单加氧酶，含血红素辅基与三价铁活性中心，代表细菌细胞色素 P450 的保守折叠：埋藏底物口袋位于血红素铁上方，活化氧几何朝向底物，构成底物定位与氧化转化的结构框架
**关键官能团**：['血红素辅基（三价铁活性中心）', '埋藏底物口袋（保守 P450 折叠）']
**来源**：DOI 10.1128/AEM.71.12.8024-8030.2005

## 3. 结构特征与结构-功能关系

必须保留：① 与双酚骨架几何互补的刚性底物口袋（夹持定位双酚，使桥键/ipso 碳对准活化氧）；② 受控的活化氧几何（血红素活化氧朝向底物）；③ 位点特异性氧化转化（ipso-羟基化）的产物路径。可灵活调整：口袋骨架材质、夹持基团化学、活化/氧化位点的实现方式。注意：催化氧化转化本身（活化氧、辅因子链）不可直接转译为吸附材料，仅底物口袋几何可转译。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶多组分酶形态: P450bisd 为可溶细胞色素 P450（约 102.3 kDa 同源二聚体），催化须 Fd(bisd)、Red(bisd) 与 NADH 辅因子链耦联，非单一固体材料可直接复制 None
- 酶催化本征活性（非吸附性能）: BPA 降解 Km 约 85 ± 4.7 μM、kcat 约 3.9 ± 0.04 min⁻¹（酶催化动力学参数，非吸附剂 qmax/Kd） μM / min⁻¹
- 电子传递严格特异性: NADPH、菠菜铁氧还蛋白/还原酶仅给弱单加氧酶活性，P450bisd 电子传递链具严格特异性 None
- 底物口袋几何依赖（同源代理外推）: 位点选择性转化依赖底物在口袋内相对血红素活化氧的定位；P450bisd 口袋无解析结构，几何约束由 P450cam（PDB 1DZ4）同源代理外推（机理推断） None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[待补充]
