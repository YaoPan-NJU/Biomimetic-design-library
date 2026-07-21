---
id: oatp-intestinal-hepatic-uptake
name: OATP 有机阴离子转运多肽（肠肝循环向量摄取）（OATP Organic Anion Transporting Polypeptides (Enterohepatic Vectorial Uptake)）
category: 动物
organism: Homo sapiens（人源 OATP1B1/OATP1B3，SLCO1B1/SLCO1B3 肝窦膜摄取转运体）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 向量传质
adsorption_mechanisms:
  - MFS 折叠两亲阴离子识别与抗衡离子交换向量摄取机制
  - 文献记载的 OATP1B1/1B3 介导全氟烷基酸（含 C8 PFCA/PFOA）转运与肠肝循环贡献
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 9 verified, 0 unverified
# coverage: partial
# status: active
---
# OATP 有机阴离子转运多肽（肠肝循环向量摄取）（OATP Organic Anion Transporting Polypeptides (Enterohepatic Vectorial Uptake)）

## 1. 生物原型简介

**问题定义**：全氟辛酸（PFOA）等全氟烷基酸在人血清中的消除半衰期长达数年并优先分布至肝脏，是长期低剂量暴露的毒代动力学基础。肠肝循环（肝摄取→胆汁排泄→肠道重吸收→经门静脉回肝）被视为维持该长半衰期与肝富集的关键过程，但负责全氟烷基酸肝摄取的窦膜转运体分子身份曾长期不明。OATP1B1/OATP1B3（SLCO1B1/SLCO1B3）是肝细胞窦膜特异表达的摄取转运体，其生理功能为将两亲有机阴离子（胆汁酸、胆红素、多种药物）自血液摄入肝细胞；其底物识别与向量跨膜转运机制，构成本条目在分子识别与传质两个层面的生物原型。

**生物策略**：结构层面，Ciuta 等（2023）解析了人源 OATP1B1 与 OATP1B3 的冷冻电镜结构（PDB 8PHW/8PG0）：二者采主要易化子超家族（MFS）折叠，12 条跨膜螺旋形成伪对称 N-bundle（TM1-6）与 C-bundle（TM7-12），inward-open 构象下两束间为向胞质侧开放的大型中央腔。OATP1B1–雌酮-3-硫酸酯（E1S）复合物中，单个 E1S 分子结合于 C-bundle 约跨膜中部的漏斗形腔：带负电硫酸根头基朝向腔顶，与 Tyr422、Tyr425、Gln541、Asn544 形成氢键，并经 Arg633 与 Tyr422 的阳离子-π 作用间接稳定；甾体骨架伸入以芳香与疏水残基衬里的口袋壁，获得范德华接触。OATP1B3 结构为药物游离态，其保守签名基序结合一个碳酸氢根分子，并含普遍存在于 pH 依赖型 OATP 的组氨酸残基，提示胞内碳酸氢根作为抗衡离子、OATP 以交换模式（电中性或可能生电）经 rocker-switch 交替接入完成向量摄取，且转运活性受酸性胞外 pH 增强。转运层面，Zhao 等（2017）以 CHO 与 HEK293 表达系统证明人源 OATP1B1、OATP1B3 与 OATP2B1 可转运 PFBS、PFHxS、PFOS 与 8-9 碳全氟烷基羧酸（即 PFOA 与 PFNA）；8-9 碳 PFCA 已知优先分布于啮齿类肝脏；OATP 与钠依赖转运体 NTCP、肠道顶膜 ASBT 一道构成这些全氟烷基酸的肠肝循环，贡献于人血清消除半衰期的延长。

## 2. 吸附机制详解

### 机制1：MFS 折叠两亲阴离子识别与抗衡离子交换向量摄取机制

**描述**：人源 OATP1B1/1B3 为肝窦摄取转运体，采 MFS 折叠（12 条跨膜螺旋组成伪对称 N-bundle TM1-6 与 C-bundle TM7-12），两束间为大型中央底物结合腔；OATP1B1–E1S（雌酮-3-硫酸酯）复合物（PDB 8PHW）显示两亲有机阴离子结合于 C-bundle 约跨膜中部的漏斗形腔：硫酸根头基位于腔顶，与 Tyr422、Tyr425、Gln541、Asn544 形成氢键，并经 Arg633 与 Tyr422 的阳离子-π 作用间接稳定，甾体骨架由芳香/疏水口袋壁以范德华接触容纳；OATP1B3（PDB 8PG0）于保守签名基序结合碳酸氢根并含普遍存在于 pH 依赖型 OATP 的组氨酸残基，OATP 以胞内碳酸氢根为抗衡离子按交换模式（电中性或可能生电）经 rocker-switch 交替接入完成向量摄取，活性受酸性胞外 pH 增强
**关键官能团**：['阴离子头基氢键锚（Tyr422/Tyr425/Gln541/Asn544 侧链，Arg633 阳离子-π 辅助）', '疏水/芳香口袋壁（范德华容纳疏水/全氟化尾链）', '保守签名基序碳酸氢根结合位点（组氨酸残基介导 pH 依赖）', 'MFS 折叠跨膜域（N-bundle TM1-6 / C-bundle TM7-12，inward-open 中央腔）']
**来源**：DOI 10.1038/s41467-023-41552-8

### 机制2：文献记载的 OATP1B1/1B3 介导全氟烷基酸（含 C8 PFCA/PFOA）转运与肠肝循环贡献

**描述**：Zhao 等（2017）以 CHO 与 HEK293 表达系统证明人源 OATP1B1、OATP1B3 与 OATP2B1 可转运 PFBS、PFHxS、PFOS 与 8-9 碳全氟烷基羧酸（C8 即 PFOA、C9 即 PFNA）；PFAS 以钠依赖（NTCP）与钠非依赖（OATP）双路进入肝细胞；8-9 碳 PFCA 优先分布于啮齿类肝脏；OATP 与 NTCP、肠道 ASBT 共同构成这些全氟烷基酸的肠肝循环，贡献于人血清消除半衰期的延长
**关键官能团**：['阴离子头基锚 + 疏水腔（PFAS 识别基序，推断与 E1S 结合模式同构）']
**来源**：DOI 10.1093/toxsci/kfw236

## 3. 结构特征与结构-功能关系

必须保留：① 两亲阴离子双要素识别基序——阴离子头基（硫酸根/羧酸根）的氢键给体阵列（Tyr/Gln/Asn 型侧链）方向性锚定并辅以阳离子稳定（Arg633 型阳离子-π）；② 容纳疏水/全氟尾链的疏水/芳香口袋壁（范德华接触）；③ 向量传质架构——转运体极化膜定位 + 抗衡离子（碳酸氢根）交换驱动的交替接入循环，使摄取可逆浓度梯度进行；④ 组氨酸介导的 pH 依赖（酸性胞外 pH 增强活性），提供结合-释放的可逆调控抓手。可灵活调整：载体骨架、锚定基团化学、口袋壁疏水/氟亲程度、腔深与孔径、外加梯度或 pH 切换方式。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 整合膜蛋白形态: OATP1B3 为 12 次跨膜整合膜蛋白（PDB 8PG0 聚合物实体式量 77.48 kDa，含 Fab 片段复合物条目总重 127.78 kDa），胞外域具 N-糖基化位点（N134、N516）；功能依赖脂质双层环境，不可直接作可溶性吸附剂使用 None
- 转运依赖跨膜梯度与交替接入循环: 摄取依赖胞内碳酸氢根抗衡离子交换与 rocker-switch 交替接入构象循环；膜电位/梯度丧失或构象锁定（变性、固定化损伤）使转运失活 None
- 底物谱宽、固有特异性弱: 口袋容纳多样有机阴离子（E1S、胆汁酸、多种药物、PFBS/PFHxS/PFOS 与 8-9 碳 PFCA）；OATP 本身不提供 PFOA 特异选择性，选择性须在材料设计层面构建 None
- pH 依赖活性: OATP 转运活性受酸性胞外 pH 增强（Disse 间隙偏酸），pH 依赖型 OATP 普遍的组氨酸残基参与；该性质既是结合-释放可逆调控的仿生抓手，也是对蛋白形态环境 pH 窗口的约束 None

## 6. 相关原型

- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling
- hsa-fatty-acid-pfas-binding
- kcsa-potassium-channel-selectivity-filter

## 参考文献

[待补充]
