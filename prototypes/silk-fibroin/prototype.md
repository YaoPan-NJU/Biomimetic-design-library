# silk-fibroin

## 元数据

- **原型 ID**: silk-fibroin
- **知识条目数**: 122
- **性能数据数**: 8
- **机制描述数**: 5
- **工程约束数**: 8

## 仿生元数据

- **organism_scientific**: Bombyx mori
- **biomimetic_dimension**: 分子仿生
- **features**: ['极性基团协同', '表面粗糙度增强', '多层吸附机制', '静电吸引主导', '生物相容性']
- **applicability**: {'pH_range': [6, 10], 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': 'pH敏感性', 'relevance': 'high', 'explanation': '强酸性条件(pH 2)下H+与MB竞争结合位点导致去除率骤降至~10%，工程应用需将废水pH严格控制在6-10区间。'}, {'constraint': '吸附平衡时间长', 'relevance': 'medium', 'explanation': '达到吸附平衡需约22小时，虽初始2小时快速吸附，但连续流工艺需优化水力停留时间或采用多级反应器。'}, {'constraint': 'GO分散均匀性', 'relevance': 'medium', 'explanation': 'GO在SF基体中的均匀分散是提升表面粗糙度与吸附位点的关键，制备时需控制溶液共混与干燥工艺以防团聚。'}]

## 仿生叙事

### problem_definition

天然水体中阳离子染料污染难降解且传统吸附剂容量受限；自然界中蚕丝蛋白通过丰富的极性氨基酸残基与微纳界面实现高效的分子识别与结合。

### biological_solution

家蚕丝素蛋白进化出富含甘氨酸、丙氨酸等极性氨基酸的序列以结合环境分子；通过引入氧化石墨烯的层状褶皱结构与含氧官能团，模拟并强化天然蛋白的多层吸附与静电捕获机制；成功将亚甲基蓝吸附容量提升61.8%至381.67 mg/g。

### key_features

必须保留SF极性基团与GO含氧官能团的静电协同作用及pH 6-10下的负电荷捕获机制；可灵活调整GO掺杂比例、成膜厚度及针对不同目标污染物的表面官能团修饰。

### design_mapping

SF氨基酸残基映射为材料表面高活性吸附位点，GO二维褶皱结构映射为高粗糙度界面以暴露更多结合位点；软约束建议维持中性至弱碱性操作环境以保障COO⁻电离，并优化溶液共混-浇铸工艺确保GO均匀分散。

### explainability_anchors

仿生故事线：借鉴天然蛋白极性结合能力，耦合二维纳米材料构建仿生复合吸附界面；设计溯源：吸附容量跃升源于极性基团协同与表面粗糙度增加，伪二级动力学与Freundlich等温线模型印证化学吸附主导与多层仿生机制，生物相容性数据保障其作为绿色水处理吸附剂的工程潜力。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| 最大吸附容量 qmax | Cu2+: 331.69 mg/g; Cr6+: 201.56 mg/g | mg/g |  | BS/SF/PUF biocomposite | literature: 10.1016/j.eti.2022.102741 |
| 去除率 removal efficiency | Cu2+ 89.8% (pH 5); Cr6+ 80.8% (pH 3) | % |  | BS/SF/PUF biocomposite | literature: 10.1016/j.eti.2022.102741 |
| Cu²⁺最大吸附容量 qmax | 186.7 | mg/g | Cu²⁺ | SF-PEI-2 millimetric aerogel beads | literature: 10.1002/admi.202001892 |
| SF-PEI-2@GO Cu²⁺最大吸附容量 | 171.6 | mg/g | Cu²⁺ | SF-PEI-2@GO core-shell aerogel beads | literature: 10.1002/admi.202001892 |
| 甲基橙(MO)最大吸附容量 | 811.3 | mg/g | methyl orange (MO) | SF-PEI-2 millimetric aerogel beads | literature: 10.1002/admi.202001892 |
| 氯仿吸附容量 | 1138 | g/g% | chloroform | SF-PEI-2@GO aerogel beads | literature: 10.1002/admi.202001892 |
| 最大吸附容量 qmax | SF: 235.84 mg/g; SF/GO: 381.67 mg/g | mg/g | methylene blue (MB) |  | literature: 10.1039/d1va00047k |
| 去除率 removal efficiency | SF: 86.24% (24h); SF/GO: 96.29% (24h) | % | MB |  | literature: 10.1039/d1va00047k |

## 吸附机制

- **吸附机制**: 多重机制协同: 静电作用+离子交换+范德华力+交联+氢键
  - 条件: {'mechanisms': ['electrostatic interactions', 'ion exchange', 'van der Waals forces', 'crosslinking', 'H-bonding'], 'functional_groups': '-OH, -NH, C=O on biocomposite surface', 'reference': '[Page 11; Conclusion]'}
  - 来源: literature: 10.1016/j.eti.2022.102741
- **结晶紫吸附机制**: π-π共轭 + 氢键 + 阴阳离子结合
  - 条件: {'mechanism': ['Π-Π conjugation', 'hydrogen bonding', 'binding of anions and cations'], 'kinetics': 'pseudo-second-order → chemisorption', 'isotherm': 'Freundlich → multilayer adsorption', 'reference': '[Page 1 + Page 11; Fig. 5h]'}
  - 来源: literature: 10.1016/j.ijbiomac.2023.126863
- **MO吸附机制**: 主导：PEI质子化氨基(-NH₃⁺)与阴离子染料MO静电吸引；辅助(GO部分)：MO芳香环与GO的π-π堆叠
  - 条件: {'primary': 'electrostatic interactions between anionic MO and protonated amino groups of PEI', 'secondary': 'π-π interactions between aromatic moieties of MO and GO (trivial contribution due to low GO quantity)', 'comparison': '2× higher than Ouyang CS/GO core-shell (353 mg/g) due to high amino content + hierarchical pores', 'ref': '[Page 9; Section 2.4.2]'}
  - 来源: literature: 10.1002/admi.202001892
- **Cu²⁺吸附机制**: PEI氨基(-NH₂)螯合Cu²⁺→化学吸附；中心发散孔道→快速扩散→活性位点可及；低密度+高孔隙→快速传质
  - 条件: {'mechanism': 'chelation of Cu²⁺ with surface amino groups of PEI', 'structure_advantage': 'center divergent pore channels decrease diffusion path; enable rapid diffusion and cation uptake', 'morphology': 'low density + aligned macropores + high amino groups', 'ref': '[Page 1; abstract; Page 9; Section 2.4.1]'}
  - 来源: literature: 10.1002/admi.202001892
- **吸附机制——静电作用**: pH升高→COO⁻形成→负电荷密度增加→静电吸引阳离子MB→去除率从7.93%升至94-96%
  - 条件: {'mechanism': 'electrostatic attraction', 'low_pH': 'H+ competes with MB for binding sites → low removal', 'high_pH': 'OH- association → increased negative charge density → COO- groups formed → electrostatic attraction with cationic MB', 'reference': '[Page 4; Section 4.4.1]'}
  - 来源: literature: 10.1039/d1va00047k

## 工程约束

- **pH最优条件**: Cu2+最优pH 5(去除率89.8%); Cr6+最优pH 3(去除率80.8%) None
  - 条件: {'pH_range_tested': '3-9', 'Cu2+': 'optimal at pH 5; removal increases from pH 3 to 5, then decreases above pH 5 due to metal-hydroxide precipitation', 'Cr6+': 'optimal at pH 3; in acidic environment, Cr6+ exists as HCrO4- with higher free energy → better removal', 'isoelectric_point': 'between pH 4 and 5', 'constant_conditions': 'dose 0.5 g, time 60 min, temp 30°C, 100 ppm', 'reference': '[Page 5; Section 3.2.1]'}
  - 来源: literature: 10.1016/j.eti.2022.102741
- **循环再生性能**: EDTA脱附→4次连续吸附/脱附循环后仍可高效再用 cycles
  - 条件: {'eluent': 'EDTA solution', 'cycles': 4, 'method': 'adsorption/desorption cycles', 'reference': '[Page 12; Section 4, Fig. 6]'}
  - 来源: literature: 10.1016/j.eti.2022.102741
- **TGA热稳定性**: BS: 总失重仅9%(至800°C); 复合材料: 第一阶段8.6%(150°C失水)→第二阶段35.4%(380°C SF酰胺分解)→第三阶段28.3%(400-800°C PUF碳骨架分解)→73%总失重 %
  - 条件: {'BS_thermogram': 'total 9% weight loss till 800°C', 'composite_stage1': '8.6% at 150°C (water evaporation, more hydrophilic than BS)', 'composite_stage2': '35.4% at 380°C (amide structure of SF degradation)', 'composite_stage3': '28.3% from 400-800°C (carbon backbone of PUF decomposition)', 'composite_total': '73% deteriorated at 800°C, BS residue remaining', 'reference': '[Page 4; Section 3.1.2]'}
  - 来源: literature: 10.1016/j.eti.2022.102741
- **TGA热稳定性**: SF: 92%→73%→37%→2%残余(三阶段)；SF-GLYMO: 97%→35%→15%→15%残余(SiO₂)；SF-PEI-2: 86%→62%→31%→5%残余 %
  - 条件: {'SF': '92% → 73% → 37% → 2% (three steps: peptide bond cleavage, hydrocarbon cleavage, oxidation to CO/CO2)', 'SF_GLYMO': '97% → 35% → 15% → 15% SiO2 residue; more stable (≈280°C); less hydrophilic (3% surface water vs 8% for SF)', 'SF_PEI_2': '86% → 62% → 31% → 5% SiO2; decomposition starts at 180°C due to PEI; 14% surface water (hydrophilic amino groups)', 'surface_water': 'SF 8%, SF-GLYMO 3%, SF-PEI-2 14%', 'ref': '[Page 5-6; Fig.3d; Section 2.2]'}
  - 来源: literature: 10.1002/admi.202001892
- **Cu²⁺再生循环**: EDTA(0.1M)洗脱→蓝变白→可循环；但首次循环后容量有损失(EDTA残留) None
  - 条件: {'regeneration_agent': 'Na-EDTA solution (0.1 M)', 'mechanism': 'EDTA competes with PEI for Cu²⁺ chelation', 'color_change': 'blue → white (successful removal)', 'limitation': 'complete removal of EDTA challenging; initial adsorption capacity compromised in further cycles', 'ref': '[Page 9; Scheme 2; Section 2.4.1]'}
  - 来源: literature: 10.1002/admi.202001892
- **再生丝素膜——酸性染料吸附**: 酸性黄11 Qe=88.50 mg/g(b=1.06); 萘酚橙74.63 mg/g(b=0.30); 直接橙S 76.34 mg/g(b=0.12) mg/g
  - 条件: {'material': 'regenerated silk fibroin film (rSFF)', 'dyes': 'Acid yellow 11, direct orange S, naphthol orange', 'conditions': 'pH 2-9, initial conc 20-70 mg/L', 'isotherm': 'Langmuir (R²=0.98-0.99)', 'reference': '[Page 20; Table 6; reference [15]]'}
  - 来源: literature: 10.1007/s10924-022-02741-6
- **pH对吸附的影响**: pH 2: SF去除率7.93%, SF/GO 10.06%; pH 6-10: SF 94%, SF/GO 96% %
  - 条件: {'pH_range': '2-10', 'optimal_pH': '6-10', 'mechanism': 'low pH: H+ competes with MB for binding sites; high pH: COO- groups formed → electrostatic attraction with cationic MB', 'reference': '[Page 4; Section 4.4.1]'}
  - 来源: literature: 10.1039/d1va00047k
- **TGA热稳定性**: SF/GO热稳定性优于纯SF; 第一阶段(至175°C): SF失重17%, SF/GO 12%(水/溶剂损失); 第二阶段(250-430°C): SF~42%, SF/GO~40%分解 %
  - 条件: {'TGA_condition': 'nitrogen atmosphere, 100 mL/min, 20°C/min to 800°C', 'stage1': 'room temperature to 175°C: SF 17% weight loss, SF/GO 12%', 'stage2': '250-430°C: SF ~42%, SF/GO ~40% decomposed', 'stage3': 'final: SF ~51%, SF/GO ~45%', 'reason': 'GO addition stabilizes the blend', 'reference': '[Page 4; Section 4.3]'}
  - 来源: literature: 10.1039/d1va00047k

## 来源汇总

- literature: 10.1002/admi.202001892
- literature: 10.1007/s10924-022-02741-6
- literature: 10.1016/j.eti.2022.102741
- literature: 10.1016/j.ijbiomac.2023.126863
- literature: 10.1039/d1va00047k
