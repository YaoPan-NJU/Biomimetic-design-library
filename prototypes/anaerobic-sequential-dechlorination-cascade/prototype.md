---
id: anaerobic-sequential-dechlorination-cascade
name: 厌氧菌群顺序脱氯级联（DDT/DDE 多位点有序还原脱氯）（Anaerobic Sequential Dechlorination Cascade (Ordered Multi-Site Reductive Dechlorination of DDT/DDE)）
category: 微生物
organism: 厌氧沉积物还原脱氯功能群落
biomimetic_dimension: 分子仿生
features:
  - 催化降解
adsorption_mechanisms:
  - 厌氧菌群对 DDT 及其持久代谢物的有序顺序还原脱氯级联（DDT→DDD/DDE→DDMU）
  - 各位点依托的低电位辅酶/辅基电子转移化学（B12/类咕啉、F430、血红素）——群落次序之下的单位点还原脱氯层
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 3 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 厌氧菌群顺序脱氯级联（DDT/DDE 多位点有序还原脱氯）（Anaerobic Sequential Dechlorination Cascade (Ordered Multi-Site Reductive Dechlorination of DDT/DDE)）

## 1. 生物原型简介

**问题定义**：DDT 是代表性的高氯化、高疏水有机氯农药，进入环境后经还原脱氯生成 DDD、经脱氯化氢生成 DDE；其中 DDE 因缺桥氢、高度稳定而长期被认为在环境中不再进一步降解，成为沉积物中的持久终端代谢物。如何理解并驱动这类高氯化有机氯的持续转化，是有机氯污染修复的基础问题。单个酶或单个辅酶只能催化一步转化（DDT→DDD 或 DDT→DDE），无法独自完成对顽固中间产物的后续转化；自然界是否在更高的组织层级（群落）给出多步有序转化的解决路径，是本原型要提取的原理。

**生物策略**：Quensen 等（Science 1998）在含 DDE 的海洋沉积物微宇宙中证明：在产甲烷与硫酸盐还原两类厌氧条件下，DDE 均被进一步脱氯为 DDMU，推翻了 DDE 在环境中不再降解的旧认识；而 DDD 脱氯化氢为 DDMU 慢约三个数量级，故这些沉积物中 DDMU 的主要前体是 DDE 而非 DDD。这一结果在群落层级确立了 DDT 的顺序脱氯级联：DDT 先经还原脱氯（DDT→DDD）与脱氯化氢（DDT→DDE）生成第一代代谢物，再由群落中相应功能种群将 DDE 通道化进入下一步（DDE→DDMU），各步由不同功能种群衔接电子供体与产物，速率差异决定级联次序。在化学层级，级联中每一步脱氯依托低电位过渡金属辅酶/辅基的电子转移：游离维生素 B12 在温和还原条件下即可使 DDT 脱氯（Berry 与 Stotter 1977），细菌过渡金属辅酶（钴胺素、辅酶 F430、血红素类）催化有机氯的还原脱氯（Gantzer 与 Wackett 1991）。但辅酶化学是单位点、单步的共转化，本身不携带跨步次序；次序是群落级的涌现性质，正是本原型相对辅酶层与单酶层的增量。任务简报所称 Lesage 1991 经核验无对应文献，其描述（B12/F430/血红素介导有机氯共代谢）与 Gantzer 与 Wackett 1991 相符，本条据实引用后者。

## 2. 吸附机制详解

### 机制1：厌氧菌群对 DDT 及其持久代谢物的有序顺序还原脱氯级联（DDT→DDD/DDE→DDMU）

**描述**：厌氧微生物群落在产甲烷与硫酸盐还原条件下对 DDT 进行顺序脱氯：DDT 先经还原脱氯生成 DDD、经脱氯化氢生成 DDE；其后 DDE 被进一步还原脱氯为 DDMU，而 DDD 脱氯化氢为 DDMU 慢约三个数量级，故这些沉积物中 DDMU 的主要前体是 DDE 而非 DDD。该功能由混合厌氧菌群完成（无单一模式种），各步由不同功能种群衔接电子供体与产物，形成有次序的多位点级联。DDE 曾长期被认为在环境中不再进一步降解，Quensen 等 1998 在海洋沉积物微宇宙中证明其可被顺序脱氯，确立了高氯代有机氯在厌氧群落中被逐步有序转化的自然解决路径。
**关键官能团**：['多位点顺序分工的功能种群/位点（各位点专司一步脱氯/转化）', '中间产物通道化衔接（前一种群产物为后一种群底物）']
**来源**：DOI 10.1126/science.280.5364.722

### 机制2：各位点依托的低电位辅酶/辅基电子转移化学（B12/类咕啉、F430、血红素）——群落次序之下的单位点还原脱氯层

**描述**：级联中每一步脱氯在化学上由低电位过渡金属辅酶/辅基介导：游离维生素 B12（钴胺素/类咕啉）在温和还原条件下即可使 DDT 还原脱氯（Berry 与 Stotter 1977）；细菌过渡金属辅酶（包括钴胺素、辅酶 F430 与血红素类）催化有机氯的还原脱氯（Gantzer 与 Wackett 1991）。该层是各位点功能种群执行单步脱氯所依托的电子转移化学，属单位点共转化。本条将其作为边界层引用：辅酶化学层已由库内 reductive-dehalogenase-b12-dechlorination 原型专司，本原型不复述其化学，仅在其上叠加群落级次序。
**关键官能团**：['低电位钴胺素/类咕啉钴中心', '辅酶 F430（镍四吡咯）', '血红素/金属卟啉催化中心']
**来源**：DOI 10.1021/es00016a017

## 3. 结构特征与结构-功能关系

必须保留：① 多个按次序排列、各位点专司一步脱氯/转化的功能单元（多位点分工）；② 中间产物通道化衔接（前一步产物进入下一步，DDE 为主要中间体）；③ 由相对速率设定的级联次序（DDE→DDMU 远快于 DDD→DDMU）；④ 厌氧/还原微环境与功能种群/位点活性。可灵活调整：位点的化学实现（生物或非生物）、载体与分区方式、电子供体形式。不可由本条移植者：具体辅酶化学（属 reductive-dehalogenase-b12-dechlorination）与单酶 β-消除机制（属 ddt-dehydrochlorinase-gst）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 群落/厌氧还原条件依赖: 顺序脱氯级联在产甲烷与硫酸盐还原（厌氧还原）微宇宙中进行，需维持厌氧/还原条件与各功能种群活性；曝气或氧化使级联停滞 None
- 中间产物通道化/多位点衔接依赖: 级联次序依赖不同功能种群间的中间产物通道化衔接（前一种群产物为后一种群底物）；分离单一菌种则丧失级联次序 None
- 无单一可固定化蛋白: 功能单元为混合厌氧菌群（无单一模式种、无单一蛋白结构），工程转译须以架构重建次序而非移植单一分子 None

## 6. 相关原型

- acidimicrobium-reductive-defluorination
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fluoroacetate-dehalogenase
- hrp-laccase-phenol-radical-coupling

## 参考文献

[待补充]
