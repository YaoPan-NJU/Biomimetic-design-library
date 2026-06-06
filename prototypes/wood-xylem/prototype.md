# wood-xylem

## 元数据

- **原型 ID**: wood-xylem
- **知识条目数**: 42
- **性能数据数**: 3
- **机制描述数**: 2
- **工程约束数**: 4

## 仿生元数据

- **biomimetic_dimension**: 结构仿生
- **features**: ['定向对齐微通道', '蜂窝状宏观孔道', '三尺度力学层级', '共价交联网络', '超高孔隙率(>99%)', '氨基选择性识别位点', '各向异性力学性能']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': 'moderate'}
- **engineering_constraints**: [{'constraint': '定向冷冻工艺梯度控制', 'relevance': 'high', 'explanation': '冰晶生长方向直接决定微通道对齐度与蜂窝形貌，需精确控制液氮浸入速率与温度梯度以复刻仿生结构。'}, {'constraint': '交联剂与GO配比阈值', 'relevance': 'high', 'explanation': 'GO浓度超过0.5 wt%易引发结节区聚集破坏孔隙连通性，TMPTAP交联密度需平衡力学强度与吸附位点暴露。'}, {'constraint': '水下结构抗剪切稳定性', 'relevance': 'medium', 'explanation': '气凝胶在水相过滤中需承受流体冲击与反复压缩，依赖三尺度协同机制维持>90%形貌恢复率以防粉化流失。'}, {'constraint': '温和再生条件适配', 'relevance': 'medium', 'explanation': '采用0.05 mol/L EDTA-2Na在25°C下洗脱，需优化解吸时间与浓度以兼顾金属回收率与共价网络化学稳定性。'}]

## 仿生叙事

### problem_definition

自然界挑战：植物木质部需在极低密度下实现水分/养分的高效纵向传输，同时抵抗重力与风载带来的机械应力。水处理对应：传统多孔吸附剂面临传质阻力大、吸附动力学慢、机械强度低易粉化、以及复杂水体中目标重金属选择性差的工程瓶颈。

### biological_solution

进化策略：木材演化出“宏观蜂窝骨架+介观纤维管胞+分子级细胞壁”的三尺度层级结构，结合纵向对齐导管实现低阻力流体通道。关键机制：薄壁细胞提供柔韧性与弹性屈曲吸能，细胞壁内纤维素微纤丝与基质共价交联赋予结构完整性与抗疲劳性。成功案例：受此启发的TCTGAs气凝胶成功复现对齐微通道与蜂窝网络，实现Pb(II)超快吸附(2min达87%)、571 mg/g超高容量及优异的水下循环压缩稳定性。

### key_features

必须保留特征：定向对齐的直管微通道(保障超快离子扩散)、三尺度力学层级(宏观蜂窝/介观纤维/分子交联协同抗变形)、氨基配位识别位点(基于HSAB理论的选择性络合)。可灵活调整特征：GO与交联剂(TMPTAP)的相对比例(调控孔隙率与交联密度)、气凝胶宏观几何形态(可塑造成圆柱/星形等适配不同反应器模块)、表面官能团类型(可替换为其他边界碱基团以靶向不同重金属离子)。

### design_mapping

生物→材料映射：木材纵向导管/纤维管胞 → 定向冷冻法构筑的对齐微通道与蜂窝状宏观孔道；细胞壁纤维素-木质素共价网络 → TCNF/GO/TMPTAP共价交联网络(形成C-N键)；水分高效传输与结构支撑 → 超快离子扩散路径与三尺度力学抗压缩机制。软约束建议：优先采用定向冷冻工艺控制冰晶生长方向以复刻各向异性通道；交联剂添加量需控制在0.5 wt% GO最优阈值附近以避免相分离；材料设计需兼顾孔隙率(>99%)与骨架强度的平衡，确保水下可压缩过滤器件的长期服役。

### explainability_anchors

仿生故事线：从“木材如何以极低密度实现高效输水与抗风载”出发，提炼出“对齐通道降阻+三尺度交联强韧”的核心法则，将其平移至重金属吸附场景，解决传统吸附剂“传质慢、易破碎、选择性弱”的痛点。设计溯源：所有性能指标(571 mg/g吸附量、2min超快动力学、20次循环90%形貌保持)均可直接追溯至定向冷冻形成的仿生孔道结构、共价交联网络的力学支撑以及HSAB理论指导的氨基选择性配位机制，形成“结构-传质-力学-化学”四位一体的可解释设计闭环。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| Langmuir最大吸附容量——三种酚类 | 苯酚102.71、4-CPh 172.24、2,4-DCPh 226.55 mg/g | mg/g |  | WAS-BC | literature: 10.1038/s41598-021-82277-2 |
| 氯取代基对吸附容量的影响——构效关系 | 2,4-DCPh(二氯) > 4-CPh(一氯) > 苯酚(无氯)；226.55 > 172.24 > 102.71 mg/g | mg/g |  |  | literature: 10.1038/s41598-021-82277-2 |
| TCTGAs对五种重金属的Langmuir最大吸附容量 qmax | Pb(II) 571, Cu(II) 462, Zn(II) 361, Cd(II) 263, Mn(II) 208 | mg/g |  |  | literature: 10.1016/j.jhazmat.2021.125612 |

## 吸附机制

- **吸附机制——分子态酚+静电排斥**: pH<pKa时分子态酚占优→利于吸附；高pH酚酸根阴离子→与负电荷WAS-BC排斥
  - 条件: {'pH_low': 'molecular phenols dominant → higher sorption', 'pH_high': 'phenolate/dichlorophenate anions → electrostatic repulsion with negatively charged WAS-BC', 'pKa_phenol': '9.95', 'pKa_4_CPh': '9.14', 'pKa_2_4_DCPh': '7.9', 'dominant_mechanism': 'molecular state phenols + hydrophobic + π-π interactions', 'ref': '[Page 6; Fig 8]'}
  - 来源: literature: 10.1038/s41598-021-82277-2
- **吸附机制：氨基配位螯合**: XPS确认N 1s偏移(398.9→399.1-399.4 eV)→N孤对电子与金属离子形成配位键。O 1s也偏移→含氧官能团参与吸附。EDX mapping确认Pb/Cu/Zn/Cd均匀分布。机制：NH3+/NH2/NH-基团与重金属离子螯合/配位
  - 条件: {'XPS_N1s': 'shift from 398.9 eV to 399.1-399.4 eV upon metal loading', 'XPS_O1s': 'also shifted → oxygen groups participate', 'EDX': 'Pb, Cu, Zn, Cd uniformly distributed on TCTGAs', 'functional_groups': 'NH3+, -NH2, -NH- → borderline base → complex borderline acids (Pb²⁺, Cu²⁺, Zn²⁺)', 'meanism': 'chelating/complexation between donor N atom and metal ions', 'ref': '[Fig. 4; Section 3.3.2]'}
  - 来源: literature: 10.1016/j.jhazmat.2021.125612

## 工程约束

- **pH影响——最佳pH 6.0**: pH 2-6吸附容量递增；pH 6最佳(苯酚84.87、4-CPh 90.22、2,4-DCPh 93.14 mg/g)；pH>6下降 mg/g
  - 条件: {'optimal_pH': '6.0', 'phenol_at_pH6': '84.87 mg/g (C0=100 mg/L)', '4_CPh_at_pH6': '90.22 mg/g', '2_4_DCPh_at_pH6': '93.14 mg_g', 'pKa_values': 'phenol 9.95, 4-CPh 9.14, 2,4-DCPh 7.9', 'mechanism': 'pH<pKa: molecular phenols dominant → favorable adsorption; pH>pKa: phenolate anions → electrostatic repulsion with negatively charged WAS-BC', 'ref': '[Page 5-6; Fig 8; 3.1节]'}
  - 来源: literature: 10.1038/s41598-021-82277-2
- **TGA热稳定性分析**: 生物质200-750°C主要热解；生物炭500°C仅~10wt%质量损失→高温稳定 °C
  - 条件: {'biomass_pyrolysis': '200-750°C main decomposition', 'biomass_moisture': '50-100°C evaporation', 'biochar_500C': '~10 wt% mass loss (moisture/adsorbed gases)', 'biochar_high_T': 'continuous decomposition due to extensive carbonization → graphitic carbon formation', 'stability': 'stable at wide range of temperatures; stable at experimental conditions', 'ref': '[Page 5; 7; Fig 6]'}
  - 来源: literature: 10.1038/s41598-021-82277-2
- **再生性能与循环稳定性**: 0.05 mol/L EDTA-2Na洗脱，25°C，3h。5次循环后保持良好吸附性能。可制成压缩过滤装置原型 None
  - 条件: {'regeneration': '0.05 mol/L EDTA-2Na, 25°C, 3h', 'cycles': 'at least 5 cycles', 'post_treatment': 'distilled water wash → room temperature overnight drying', 'device_prototype': 'compression filter device (shown in photos)', 'ref': '[Fig. 5a; Section 2.4.5; Section 3.3]'}
  - 来源: literature: 10.1016/j.jhazmat.2021.125612
- **水下力学稳定性**: TCTGAs在水下表现出优异的力学结构稳定性→有利于水处理中的循环回收。普通冷冻法制备的气凝胶无法承受大变形 None
  - 条件: {'underwater_stability': 'excellent underwater mechanical structural stability (Fig. S10, Movie S1)', 'regular_freezing': 'TCTGAs fabricated in common freezing failed to bear large deformation', 'anisotropic': 'aligned microchannels → anisotropic mechanical performance; parallel to channel → easy crushing', 'ref': '[Section 3.2; Fig. S8-S10]'}
  - 来源: literature: 10.1016/j.jhazmat.2021.125612

## 来源汇总

- literature: 10.1016/j.jhazmat.2021.125612
- literature: 10.1038/s41598-021-82277-2
