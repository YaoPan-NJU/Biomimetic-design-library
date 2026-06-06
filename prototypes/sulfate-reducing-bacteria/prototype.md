# sulfate-reducing-bacteria

## 元数据

- **原型 ID**: sulfate-reducing-bacteria
- **知识条目数**: 109
- **性能数据数**: 0
- **机制描述数**: 1
- **工程约束数**: 5

## 仿生元数据

- **organism_scientific**: Desulfovibrio, Desulfobulbus, Desulfotomaculum, Desulfobacterium, Desulfosarcina
- **biomimetic_dimension**: 过程仿生
- **features**: ['硫酸盐还原酶促代谢', '三阶段生物膜形成', 'Fe⁰协同供电子', 'pH/Ksp调控沉淀', 'EPS包裹抗毒性', '硫/金属资源化']
- **applicability**: {'pH_range': [4.0, 7.5], 'temp_range': [23, 35], 'salinity': None}
- **engineering_constraints**: [{'constraint': 'pH环境敏感性', 'relevance': 'high', 'explanation': 'SRB最适pH为6.0-7.5，超出范围还原速率下降；Fe⁰协同可拓宽至pH 4.0-7.0'}, {'constraint': '重金属毒性阈值', 'relevance': 'high', 'explanation': 'Cd、Cu、Zn、Cr、Pb、Ni等超过特定浓度(如Cu 4-20 mg/L)会显著抑制SRB生长与代谢'}, {'constraint': '碳硫比(COD/S)控制', 'relevance': 'high', 'explanation': 'COD/SO₄²⁻=1.0时硫酸盐还原最佳，≤0.67时有机物完全去除，需精确调控电子供体投加量'}, {'constraint': '温度依赖性', 'relevance': 'medium', 'explanation': '温和温度23-35°C(最佳35°C)下代谢活性最高，低温会显著降低反应动力学'}]

## 仿生叙事

### problem_definition

自然界中SRB在厌氧及重金属胁迫环境下需解决硫酸盐代谢与重金属解毒的生存挑战；对应水处理中含硫酸盐废水与潜在有毒元素(PTEs)的高效协同去除及资源回收难题。

### biological_solution

SRB进化出三步酶促还原系统将SO₄²⁻转化为H₂S，利用H₂S与金属离子生成难溶硫化物沉淀实现解毒；同时通过EPS包裹的三阶段生物膜(附着-增殖-成熟)构建抗毒性微环境；成功案例包括酸性矿井排水处理中SO₄²⁻去除>80%及Cd去除90%，以及Fe⁰-SRB协同系统实现Cu²⁺≈100%去除。

### key_features

必须保留：硫酸盐还原产H₂S的核心代谢路径、生物膜EPS保护结构、基于pH/Ksp的选择性沉淀机制；可灵活调整：电子供体类型(乳酸/甘油/零价铁/糖蜜等)、反应器构型(CSTR/UASB/生物膜反应器)、水力停留时间与COD/S操作参数。

### design_mapping

生物代谢酶系统→仿生催化活性位点/复合电子供体材料；生物膜三阶段结构→仿生多孔/分级吸附载体；pH调控沉淀→仿生智能响应型分级沉淀模块。软约束建议：维持微厌氧环境以稳定还原态硫；控制进水COD/S比在0.67-1.0区间；设计Fe⁰缓冲层以应对高浓度重金属毒性及酸性冲击。

### explainability_anchors

仿生故事线：从SRB在极端环境下的‘产硫沉淀解毒+生物膜庇护’生存策略出发，构建人工水处理系统的代谢-沉淀-回收闭环；设计溯源：基于SRB硫酸盐还原总反应与金属硫化物沉淀热力学(Ksp控制)，结合Fe⁰协同提供H₂与碱度的工程实践，映射出‘供电子-还原-选择性沉淀-硫回收’的材料与工艺设计逻辑。

## 吸附机制

- **SRB硫酸盐还原三步酶促机理**: SO₄²⁻ →(sat, ATP) APS →(APS还原酶, 2e⁻) SO₃²⁻ →(CBS, 6e⁻) H₂S；消耗大量H⁺→提升水体pH
  - 条件: {'step_1': "sulfate adenylyltransferase (sat) activates SO₄²⁻ → APS (adenosine-5'-phosphosulfate)", 'step_2': 'APS reductase catalyzes APS → sulfite (SO₃²⁻) with 2e⁻', 'step_3': 'dissimilatory sulfite reductase (CBS) reduces SO₃²⁻ → H₂S with 6e⁻', 'byproducts': 'PPi (pyrophosphate) released; 2H⁺ consumed at step 1, 8H⁺ consumed at step 3', 'alkalinity': 'massive H⁺ consumption → pH increase → favorable for metal precipitation', 'ref': '[Page 2; Fig.2; Section 2.1]'}
  - 来源: literature: 10.16581/j.cnki.issn1671-3206.20230927.002

## 工程约束

- **pH对SRB的影响**: 最适生长pH 5-9；pH<5或>9时生长和硫酸盐还原几乎完全抑制；酸性条件下H₂S和乙酸抑制微生物活性 None
  - 条件: {'optimal_pH': '5–9 for growth of most SRB', 'inhibition': 'almost inhibited when pH < 5 or > 9', 'acidic_conditions': 'strong acidity inhibitory; H₂S and acetic acid produced by SRB severely inhibit activity of sulfur-producing bacteria and fermenting bacteria', 'alkaline_conditions': 'free ammonia inhibits sulfate reduction', 'acid_resistance_SRB': 'Desulfitobacterium sp. CEB3: TOC stimulation at pH ≤ 3.5; eosinophilic SRB at pH 3 → Cu/Zn 99% removal', 'buffering': 'calcite tailings increase pH from 2.5 to 8.4; alkalic metabolic compounds by SRB recycled for pH balancing', 'ref': '[Page 10-11; Section 4.4]'}
  - 来源: literature: 10.1016/j.jwpe.2023.103537
- **SRB生长pH范围**: 5-9(最适)；AMD通常pH<4→不利于SRB生长 None
  - 条件: {'optimal_range': 'pH 5-9', 'amd_condition': 'AMD pH typically <4 → unfavorable for SRB growth', 'mechanisms': ['acidic: H⁺ enters cell → more energy used for H⁺ efflux → insufficient for SO₄²⁻ reduction', 'acidic: H₂S (dominant at low pH) easily crosses cell membrane → binds intracellular Fe-compounds → inhibits electron transfer', 'acidic: high H₂S → protein denaturation + DNA damage', 'acidic: heavy metals in free ionic form → much higher toxicity than complexed metals'], 'ref': '[Page 2; Section 2.2.1]'}
  - 来源: literature: 10.16581/j.cnki.issn1671-3206.20230927.002
- **低pH条件下SRB活性**: SRB可在pH≤3.0条件下生长并实现>99%的Zn和Fe去除 None
  - 条件: {'pH': '≤3.0', 'reactor': 'fluidized bed reactor', 'reference': 'Kaksonen et al. (2003)', 'finding': 'proved SRB can grow and heavy metal removal can also be possible at acidic pH', 'ref': '[Page 3; 2.1节]'}
  - 来源: literature: 10.1016/j.jenvman.2020.111555
- **低pH条件下SRB活性**: SRB可在pH≤3.0条件下生长并实现>99%的Zn和Fe去除 None
  - 条件: {'pH': '≤3.0', 'reactor': 'fluidized bed reactor', 'reference': 'Kaksonen et al. (2003)', 'finding': 'proved SRB can grow and heavy metal removal can also be possible at acidic pH', 'ref': '[Page 3; 2.1节]'}
  - 来源: literature: 10.1016/j.jenvman.2020.111555
- **SRB硫循环耦合其他元素循环**: 硫循环与碳/氮/磷循环耦合；硫氧化可与反硝化耦合(硫自养反硝化)→减少N₂O排放；硫化物可作为反硝化的电子供体→同时去除重金属；微生物硫代谢的环境意义：DMS产生→云形成→气候调节 None
  - 条件: {'coupling': 'sulfur cycle interconnected with carbon, nitrogen, and phosphorus cycles', 'sulfur_oxidation_denitrification': 'coupled with nitrate reduction by sulfur-utilizing autotrophic denitrifiers; reduces N2O emission', 'sulfide_as_electron_donor': 'for nitrogen removal through autotrophic denitrification; catalyst for heavy metal precipitation', 'DMS_production': 'dimethylsulfide produced by microorganisms; rapidly transformed into sulfur compounds; act as nuclei for cloud formation; theorized to offset global climate change', 'ref': '[Page 12; Section 6.2; Page 3; Section 2.1]'}
  - 来源: literature: 10.1016/j.psep.2024.01.103

## 来源汇总

- literature
- literature: 10.1016/j.jclepro.2022.134109
- literature: 10.1016/j.jenvman.2020.111555
- literature: 10.1016/j.jhazmat.2022.130377
- literature: 10.1016/j.jwpe.2023.103537
- literature: 10.1016/j.psep.2024.01.103
- literature: 10.11654/jaes.2020-1156
- literature: 10.16085/j.issn.1000-6613.2021-2532
- literature: 10.16581/j.cnki.issn1671-3206.20211105.008
- literature: 10.16581/j.cnki.issn1671-3206.20230927.002
- literature: 10.3969/j.issn.1671-4172.2022.06.002
