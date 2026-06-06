# mycelium

## 元数据

- **原型 ID**: mycelium
- **知识条目数**: 40
- **性能数据数**: 6
- **机制描述数**: 0
- **工程约束数**: 3

## 仿生元数据

- **biomimetic_dimension**: 结构仿生
- **features**: ['纤维素纳米纤丝网络', '改性木质素基质', '三维多孔/泡沫形态', '高羧基/含氧官能团表面', '酶/微生物固定化界面', '吸附-降解协同微环境']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '生物炭热解产率低与高能耗', 'relevance': 'high', 'explanation': '热解产率通常<30%，能耗高且释放有毒气体，显著增加全生命周期环境负担'}, {'constraint': '含氧官能团热损失', 'relevance': 'high', 'explanation': '高温热处理大量去除含氧官能团，直接削弱后续酶固定化等生物技术改性能力'}, {'constraint': '水凝胶溶胀与结构稳定性平衡', 'relevance': 'medium', 'explanation': '需在低溶胀率下维持高吸附容量（如近100%金属吸附），以保证材料在实际水流中的机械强度与循环寿命'}]

## 仿生叙事

### problem_definition

自然界中植物细胞壁需高效捕获水分与养分并维持抗降解结构，而传统水处理依赖多级串联工艺（treatment train），存在能耗高、碳足迹大、吸附与降解环节割裂的局限。

### biological_solution

进化出由纤维素纳米纤丝与改性木质素构成的分级多孔网络，兼具高比表面积、丰富含氧官能团及生物相容性；关键机制为物理/化学吸附富集（静电、氢键、π-π堆叠、配体交换）与酶/微生物原位降解的协同；成功案例如RAPIMER系统实现‘吸附-富集-降解-营养供给’一体化，突破传统处理链局限。

### key_features

必须保留：纤维素-木质素分级网络骨架、高密度含氧/羧基官能团、三维多孔/泡沫形态、酶/微生物固定化界面；可灵活调整：具体生物质来源（如咖啡渣、丝瓜络、刺柏）、交联度与溶胀率、表面接枝化学（如PEI、氨基化）、目标污染物靶向修饰。

### design_mapping

生物→材料映射：植物细胞壁纤维素网络→TEMPO氧化纳米纤维素/水凝胶骨架（提供高羧基密度与物理吸附位点）；木质素基质→改性木质素粉末/生物炭（提供π-π堆叠、疏水作用及电子供受体复合物）；真菌营养微环境→多孔泡沫/水凝胶载体（负载漆酶/脲酶等实现原位降解）。软约束建议：优先采用水热碳化或温和改性以保留含氧官能团；调控交联网络平衡溶胀率与结构强度；合成过程需严格兼容生物酶活性中心。

### explainability_anchors

仿生故事线：借鉴植物细胞壁‘结构支撑-养分循环’双重角色，将传统单一吸附材料升级为‘吸附基质+生物修复营养源’的复合系统；设计溯源：基于RAPIMER逆向工程原理，以纤维素纳米纤丝构建吸附骨架，以改性木质素提供疏水/π-π作用及酶固定化微环境，最终实现全生命周期可持续的水处理材料设计范式。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| 重金属去除方法比较 Comparison of heavy metal removal methods | 生物吸附法: 来源丰富/操作简单/成本低/快速高效/无二次污染/但不稳定 | None |  |  | literature: 10.19465/j.cnki.2095-9710.2021.04.005 |
| 刺柏纳米纤维素Cd2+去除 Spinifex nanocellulose Cd2+ removal | 大而快速的去除容量，源于纳米纤维素表面羧酸根与Cd2+离子的相互作用 | None |  | nanocellulose from spinifex | literature: 10.1016/j.tibtech.2022.09.011 |
| 纤维素纳米纤维/PVA染料去除效率 CNF/PVA dye removal | 阳离子和阴离子染料分子平均去除效率>60% | percent |  | cellulose nanofibers blended with PVA | literature: 10.1016/j.tibtech.2022.09.011 |
| TOCNFs对Cu2+吸附容量 TOCNFs Cu2+ adsorption capacity | 75 mg/g（羧酸根含量1.5 mmol/g） | mg/g |  | TEMPO-oxidized cellulose nanofibers (TOCNFs) | literature: 10.1016/j.tibtech.2022.09.011 |
| TOCNFs对亚甲基蓝吸附容量 TOCNFs methylene blue adsorption | TOCNFs: 769 mg/g; CNCs: 118 mg/g | mg/g |  |  | literature: 10.1016/j.tibtech.2022.09.011 |
| 灵芝菌丝-玉米芯-海藻酸去除土壤蒽 Ganoderma-corn cob-alginate anthracene removal | 土壤蒽去除率约96%（pH 5.0，45°C，20天） | percent |  | Ganoderma lucidum mycelium pellets with corncobs in hydrophobically modified Ca-alginate (PCL modified) | literature: 10.1016/j.tibtech.2022.09.011 |

## 工程约束

- **pH对真菌吸附的影响 pH effect on fungal adsorption**: pH 6.0时球孢白僵菌Z1对Cd²⁺去除率56.17%；pH过低→H⁺竞争位点；pH过高→金属氢氧化物沉淀 %
  - 条件: {'optimal_pH': '6.0', 'organism': '球孢白僵菌Z1 (Beauveria bassiana Z1)', 'pollutant': 'Cd²⁺', 'removal_rate': '56.17%', 'mechanism_low_pH': '大量氢离子和游离重金属竞争结合位点，导致吸附效果不佳', 'mechanism_high_pH': 'pH大于金属离子形成微沉淀的临界值，金属离子沉淀形成不溶性氢氧化物或氧化物', 'reference': '[Page 1; Section 2.1]'}
  - 来源: literature: 10.19465/j.cnki.2095-9710.2021.04.005
- **PEI-接枝碱木质素-La纳米氢氧化物的磷酸盐去除 PEI-graft-alkali lignin-La for phosphate**: 表面沉淀和配体交换 None
  - 条件: {'material': 'poly(ethyleneimine)-graft-alkali lignin loaded with nanoscale lanthanum hydroxide (AL-PEI-La)', 'contaminant': 'phosphate', 'mechanism': 'surface precipitation and ligand exchange'}
  - 来源: literature: 10.1016/j.tibtech.2022.09.011
- **酯化纤维素纳米纤维去除药物废物 Esterified cellulose nanofibers for pharmaceutical waste**: 环丙沙星: 45.04 mg/g; 氧氟沙星: 85.30 mg/g mg/g
  - 条件: {'material': 'esterified cellulose nanofibers assembled with functionalized graphene oxide', 'ciprofloxacin_capacity': '45.04 mg/g', 'ofloxacin_capacity': '85.30 mg/g', 'mechanism': 'electrostatic interaction, π-π interactions, and hydrogen bonding'}
  - 来源: literature: 10.1016/j.tibtech.2022.09.011

## 来源汇总

- literature: 10.1016/j.tibtech.2022.09.011
- literature: 10.19465/j.cnki.2095-9710.2021.04.005
