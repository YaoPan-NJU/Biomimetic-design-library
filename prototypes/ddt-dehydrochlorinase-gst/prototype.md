---
id: ddt-dehydrochlorinase-gst
name: DDT-脱氯化氢酶（谷胱甘肽 S-转移酶 GST）（DDT-Dehydrochlorinase (Glutathione S-Transferase, GST)）
category: 动物
organism: Anopheles funestus / Musca domestica（冈比亚按蚊近缘种 GSTe2 抗性结构体系与家蝇 DDT-脱氯化氢酶酶学体系）
biomimetic_dimension: 分子仿生
features:
  - 特异性识别
  - 催化降解
adsorption_mechanisms:
  - GSTe2 双分区活性位点（G 位/H 位）与 DDT 脱氯化氢代谢（降解/转化）
  - DDT-脱氯化氢酶的底物桥基序读出（p,p'-取代双苯环与桥连叔碳 β-氢）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 5 papers, 14 verified, 0 unverified
# coverage: partial
# status: active
---
# DDT-脱氯化氢酶（谷胱甘肽 S-转移酶 GST）（DDT-Dehydrochlorinase (Glutathione S-Transferase, GST)）

## 1. 生物原型简介

**问题定义**：DDT 是典型有机氯农药，双翅目昆虫（家蝇、按蚊）在长期选择下进化出代谢抗性：体内 DDT-脱氯化氢酶将 DDT 脱氯化氢转化为 DDE 而降低毒性。该酶学体系是自然界对有机氯分子进行酶促转化的经典案例，同时也是「如何从结构上识别 DDT 型分子」的分子识别问题。本库将其定位为降解/转化仿生原型（天然机制为降解/转化）与桥基序读出动机原型。

**生物策略**：按蚊 epsilon 类谷胱甘肽 S-转移酶 GSTe2 催化 DDT 的脱氯化氢代谢。Riveron 等（Genome Biology 2014）解析了冈比亚按蚊近缘种（An. funestus）GSTe2 敏感（UG）与抗性（BN）等位基因晶体结构（PDB 3ZML，GSH 复合物）：活性位点分两个子位点，G 位结合一分子 GSH（辅因子位，SITE AC1 记结合残基 Ser12/Pro14/Leu36/His41/His53/Thr54/Ile55/Pro56/Glu67/Ser68/His69/Phe108/Arg112，chain A），H 位为邻接 G 位的大而略开放的疏水底物口袋（由 N 端 loop 与 C 端 H4/H8 螺旋构成）。DDT 以对接模型容纳于 H 位，二氯苯环被稳定、桥碳 Cα 指向谷胱甘肽硫醇盐；L119F 突变弯折 H4 螺旋 N 端、扩大 H 位腔，抗性等位基因对 DDT 的催化效率显著更高（kcat/Km 316.3 对 92.0 µM−1·s−1），且作者明确指出 DDT/DDE 共结晶尝试未成功、结合姿态为对接模型。Li 等（2014 ES&T）对 agGSTe2 脱毒机制作 QM/MM 计算：质子转移机制指数平均能垒 15.2 kcal/mol，较 GS-DDT 共轭机制低 27.6 kcal/mol，支持 GSH 作辅因子（碱）而非共轭底物，Arg112/Glu116/Phe120/Ile55 等残基对反应影响显著。冈比亚按蚊 GSTe2（PDB 2IMI，Wang 2008）架构同源且具高 DDT 代谢活性。酶学层面，Lipke & Kearns（JBC 1959）系统测定了家蝇 DDT-脱氯化氢酶的底物与辅因子特异性：p,p'-取代双苯环为结合必要条件（未取代双苯环不反应），桥连叔碳（C-2）质子释放为消除步骤所需，DDT 仅生成 DDE，TDE（DDD）降解约为 DDT 的 4 倍，且仅谷胱甘肽与半胱氨酰甘氨酸能引发反应；Clark & Shamaan（1984）随后证明家蝇 DDT-脱氯化氢酶即谷胱甘肽 S-转移酶。

## 2. 吸附机制详解

### 机制1：GSTe2 双分区活性位点（G 位/H 位）与 DDT 脱氯化氢代谢（降解/转化）

**描述**：双翅目按蚊 epsilon 类谷胱甘肽 S-转移酶 GSTe2 代谢 DDT（1,1,1-三氯-2,2-双(对氯苯基)乙烷），产物为 DDE（1,1-二氯-2,2-双(对氯苯基)乙烯）。活性位点分两个子位点：G 位结合 GSH 辅因子（PDB 3ZML 中一分子 GSH 结合于 G 位），H 位为邻接 G 位的大而略开放的疏水底物口袋；DDT 以对接模型容纳于 H 位，二氯苯环被稳定、桥碳 Cα 指向谷胱甘肽硫醇盐。L119F 突变使 H4 螺旋 N 端弯折、扩大 H 位腔，抗性（119 F）等位基因对 DDT 的催化效率显著高于敏感（L119）等位基因（kcat/Km 316.3 对 92.0 µM−1·s−1）。Li 2014 QM/MM 计算（agGSTe2）支持脱毒经质子转移机制：其指数平均能垒 15.2 kcal/mol，较 GS-DDT 共轭机制低 27.6 kcal/mol，GSH 作辅因子（碱）而非共轭底物。家蝇 DDT-脱氯化氢酶活性经 Clark & Shamaan 1984 证明属于谷胱甘肽 S-转移酶。本条按天然机制如实标记为降解/转化。
**关键官能团**：['G 位谷胱甘肽结合位点（硫醇盐稳定化的极性位点）', 'H 位疏水腔（芳香/卤亲接触面，H4/H8 螺旋腔壁）', '活性位点残基（Arg112、Ile55、Glu116、Phe120 等，Li 2014 QM/MM；Arg112/Ile55 见于 3ZML SITE AC1）']
**来源**：DOI 10.1186/gb-2014-15-2-r27

### 机制2：DDT-脱氯化氢酶的底物桥基序读出（p,p'-取代双苯环与桥连叔碳 β-氢）

**描述**：Lipke & Kearns 1959 系统测定家蝇 DDT-脱氯化氢酶对 DDT 类似物的底物特异性：酶读出双重基序，其一为 p,p'-取代双苯环（未取代双苯环类似物完全不反应），其二为桥连叔碳（C-2）质子（β-消除必需；烯烃产物 DDE 无此氢而为终端产物）。环取代类似物活性序：p-Br 与 p-Cl 相当，p-F、CH3、CH3O、I 取代依次降低；烷取代类似物 TDE（即 DDD，1,1-二氯-2,2-双(对氯苯基)乙烷）降解约为 DDT 的 4 倍，表明读出基于桥基序而非 DDT 独有。该酶经 Clark & Shamaan 1984 证明为谷胱甘肽 S-转移酶，为 DDT 型分子识别提供结构基序读出原型。
**关键官能团**：["p,p'-取代双苯环读出位（疏水口袋壁）", '桥连叔碳 β-氢读出位（消除反应化学把手）']
**来源**：DOI 10.1016/S0021-9258(18)69878-3

## 3. 结构特征与结构-功能关系

必须保留：① 与双(对氯苯基)底物几何互补的 H 位疏水腔（腔形与尺寸决定底物可及性）；② 双基序读出（p,p'-取代双苯环 + 桥连叔碳 β-氢）；③ 双分区活性位点架构概念（底物口袋邻接辅因子位点）。可灵活调整：载体骨架、腔深与腔壁化学（芳香/卤亲修饰程度）、识别基团类型；催化化学与 GSH 辅因子依赖不可移植。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶酶形态: GSTe2 为双翅目昆虫可溶性胞内酶；冈比亚按蚊近缘种 GSTe2 单体约 25.3 kDa（RCSB 3ZML 聚合物实体 1：25.283 kDa），冈比亚按蚊 GSTe2 约 24.9 kDa（RCSB 2IMI：24.88 kDa）；用作吸附须固定化或将识别原理移植于固体载体 None
- GSH 辅因子依赖: 仅谷胱甘肽与半胱氨酰甘氨酸能引发脱氯化氢反应，缺乏 GSH 辅因子时催化活性无从发起；催化功能不可脱离辅因子化学 None
- 缺乏 DDT 复合物晶体结构: DDT/DDE 与 GSTe2 的共结晶尝试未成功，现有 DDT 结合姿态为分子对接模型（以 GSH 位点为中心定义对接腔）；涉及结合姿态的设计论据按模型级证据对待 None
- 催化不可直接转译: β-消除脱氯化氢依赖 G 位硫醇盐化学与完整三级结构的配合，被动吸附材料无法复制；可提取的仅为 H 位腔几何与桥基序读出的识别原理 None

## 6. 相关原型

- cell-membrane-ion-channel
- diatom-frustule
- dmpr-phenol-effector-binding-domain
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding

## 参考文献

[待补充]
