---
id: reductive-dehalogenase-b12-dechlorination
name: B12/类咕啉依赖还原脱卤酶有机氯还原脱氯（B12/Corrinoid-Dependent Reductive Dehalogenase Organochlorine Reductive Dechlorination）
category: 微生物
organism: Nitratireductor pacificus pht-3B（还原脱卤酶 RdhA，PDB 4RAS；有机卤呼吸厌氧菌的钴胺素依赖还原脱卤酶）
biomimetic_dimension: 分子仿生
features:
  - 催化降解
adsorption_mechanisms:
  - 钴胺素（B12）辅酶经钴-卤素相互作用介导的有机氯还原脱卤
  - 辅酶化学介导的 DDT 还原脱氯（维生素 B12 与还原型黄素/血红素，DDT→DDD）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 4 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# B12/类咕啉依赖还原脱卤酶有机氯还原脱氯（B12/Corrinoid-Dependent Reductive Dehalogenase Organochlorine Reductive Dechlorination）

## 1. 生物原型简介

**问题定义**：有机卤化合物构成大量环境污染物，自然界经有机卤呼吸菌的生物脱卤参与全球卤素循环。还原脱卤酶是这一过程的催化核心，天然底物包括多氯联苯与二噁英等卤代芳烃。该酶如何在温和条件下断裂惰性的有机 C-卤键，是有机卤（生物）化学与生物修复的基础问题。DDT 作为高氯化、高疏水的代表性有机氯农药，其桥键 C-Cl 能否被还原断裂、以及对不同桥键结构（DDT 与 DDE）是否具反应性分辨，是有机氯降解的关键机理问题。

**生物策略**：有机卤呼吸厌氧菌进化出钴胺素（B12/类咕啉）依赖的还原脱卤酶亚家族。Payne 等（2015）报道了一株可溶、耐氧的还原脱卤酶（Nitratireductor pacificus pht-3B，PDB 4RAS，含 COBALAMIN/B12、[4Fe-4S]/SF4 与氯离子/CL 配体），结合结构、EPR 与模拟提出：钴胺素钴中心与底物卤素的直接相互作用是催化的基础，还原脱卤酶经卤素-钴键形成实现有机卤底物的还原，区别于其他钴胺素亚家族的碳-钴键化学。在辅酶化学层，游离维生素 B12 在温和还原条件下即可使 DDT 脱氯（Berry 与 Stotter 1977）；大鼠血液由还原型黄素（经 NADPH/NADH 还原）经血红蛋白血红素催化对 DDT 进行非酶还原脱氯生成 DDD（Sugihara 1998）。Kallman 与 Andrews（1963）以 C14 标记实验证明 DDT 经酵母还原脱氯为 DDD，且由 DDE 生成 DDD 未被观察到，确立了还原脱氯对桥键结构的反应性分辨（DDT 反应、DDE 不反应）。

## 2. 吸附机制详解

### 机制1：钴胺素（B12）辅酶经钴-卤素相互作用介导的有机氯还原脱卤

**描述**：还原脱卤酶是有机卤呼吸菌中负责生物脱卤的钴胺素（B12）依赖酶亚家族。其活性位点的咕啉钴中心与底物卤素发生直接相互作用，经卤素-钴键形成实现对有机卤底物的还原，区别于其他钴胺素亚家族的碳-钴键化学。PDB 4RAS（Payne 2015，Nitratireductor pacificus pht-3B 的可溶耐氧还原脱卤酶）含 COBALAMIN（B12）与 IRON/SULFUR CLUSTER（SF4，[4Fe-4S]）辅因子及 CHLORIDE ION（CL，脱卤产物卤离子）
**关键官能团**：['低电位钴胺素/类咕啉钴中心（Co(I)/Co(II) 氧化还原对）', '[4Fe-4S] 铁硫簇（电子传递）', '咕啉环共轭体系与轴向配位']
**来源**：DOI 10.1038/nature13901

### 机制2：辅酶化学介导的 DDT 还原脱氯（维生素 B12 与还原型黄素/血红素，DDT→DDD）

**描述**：游离钴胺素（维生素 B12）在温和还原条件下即可使 DDT 脱氯（Berry 与 Stotter 1977）；大鼠血液在还原型吡啶核苷酸与黄素存在下，由还原型黄素（FAD/FMN/核黄素，经 NADPH/NADH 还原）经血红蛋白血红素催化，对 DDT 进行非酶还原脱氯生成 DDD（Sugihara 1998）。这表明 DDT 的还原脱氯本质上是低电位辅酶/辅基的电子转移化学，而非整酶专属，构成辅酶化学层先例
**关键官能团**：['低电位钴胺素/类咕啉钴中心（Co(I)）', '还原型黄素（FAD/FMN/核黄素）', '血红素/金属卟啉催化中心']
**来源**：DOI 10.1016/0045-6535(77)90151-5

## 3. 结构特征与结构-功能关系

必须保留：① 低电位钴胺素/类咕啉钴中心（Co(I)/Co(II) 氧化还原对，电子转移中心）；② 钴/金属中心与底物卤素的直接相互作用（卤素-钴/金属-卤素键形成）；③ 低电位电子供体与还原态再生（[4Fe-4S] 簇/铁氧还蛋白、NADPH/NADH 或外源还原剂）；④ 还原/低氧微环境。可灵活调整：中心化学（类咕啉、金属卟啉、还原态矿物）、电子供体形式（化学牺牲还原剂、阴极电生电子、光生电子）、载体骨架与隔氧结构。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 膜结合/氧敏感约束: 多数天然还原脱卤酶膜结合且氧敏感（Payne 2015）；4RAS 为可溶、耐氧的例外，但催化仍需还原态钴中心与低电位电子供体（[4Fe-4S] 簇/铁氧还蛋白）。固定化或合成转译须维持还原微环境 None
- 低电位电子供体依赖: 还原脱氯需低电位电子供体（还原型铁氧还蛋白、NADPH/NADH、还原态矿物或光/电生电子）再生 Co(I)/还原型辅酶；无持续电子供给则反应停止 None
- 底物桥键反应性分辨: DDT 还原脱氯生成 DDD，但 DDE 不被同途径转化（Kallman 1963：DDD from DDE not observed），即反应对桥键结构敏感；对 DDE 等缺桥氢或高氯化/位阻底物，该还原脱氯途径不适用或效率低 None

## 6. 相关原型

- acidimicrobium-reductive-defluorination
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fluoroacetate-dehalogenase
- iron-oxidizing-bacteria

## 参考文献

[待补充]
