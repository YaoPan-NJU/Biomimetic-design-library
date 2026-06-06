# shark-skin

## 元数据

- **原型 ID**: shark-skin
- **知识条目数**: 103
- **性能数据数**: 0
- **机制描述数**: 1
- **工程约束数**: 5

## 仿生元数据

- **organism_scientific**: Nelumbo nucifera
- **biomimetic_dimension**: 结构仿生
- **features**: ['微纳双尺度结构', '低表面能修饰', 'Cassie-Baxter态', '空气层隔离', '自清洁效应', '超疏水界面']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '机械稳定性与耐磨性', 'relevance': 'high', 'explanation': '纳米级结构强度有限，耐磨性不足是超疏水材料走向工业化应用的主要障碍'}, {'constraint': '大面积制备与结构均匀性', 'relevance': 'medium', 'explanation': '模板法和静电纺丝在复杂或大面积基底上保持微纳双尺度结构的均匀性和一致性存在工艺挑战'}]

## 仿生叙事

### problem_definition

自然界中水生或潮湿环境下的动植物需要保持表面干燥、清洁及防污；在水处理领域，油水分离膜和吸附材料需要构建超疏水/超亲油界面，以实现高效油水分离、抗污染和自清洁功能。

### biological_solution

荷叶等生物通过进化出表皮微纳双尺度乳突结构并覆盖蜡质等低表面能物质，实现超疏水与自清洁。关键机制是形成Cassie-Baxter态，利用微纳结构截留空气层隔离液滴与固体表面，水滴滚落时携带走污染物颗粒。成功案例包括荷叶的自清洁效应、鲨鱼皮的表面防污以及壁虎脚的微纳结构调控。

### key_features

必须保留特征：微米与纳米相结合的双尺度粗糙结构、低表面能化学修饰（构建Cassie态空气层）；可灵活调整特征：微纳结构的具体形貌与尺寸（如微柱间距）、低表面能修饰剂种类（如TEOS、各类硅烷偶联剂）、基底与骨架材料（如PVDF、PDMS、SiO2颗粒）。

### design_mapping

生物→材料映射：荷叶表皮微乳突映射为PDMS模板法或静电纺丝构建的微纳阵列/纤维膜，植物表面蜡质映射为硅烷偶联剂脱水缩合引入的疏水基团（如-CnH2n+1等）。软约束建议：优先采用反应条件温和的硅烷脱水缩合或PDMS“胶+粉”法以提升工艺通用性，并利用Si-O键赋予材料优异的UV抗性和热稳定性。

### explainability_anchors

仿生故事线：从荷叶“出淤泥而不染”的宏观自清洁现象出发，深入解析微纳双尺度与空气垫的微观物理机制，最终通过硅基化学与模板/纺丝工艺实现人工超疏水界面的工程化复刻。设计溯源：基于Young方程与Cassie-Baxter润湿模型，将自然界的低表面能与粗糙度协同策略，溯源并转化为硅烷偶联剂改性与微纳结构构建的材料设计准则。

## 吸附机制

- **超疏水表面防污机制 Superhydrophobic surface antifouling mechanism**: 超疏水表面的抗污性能归因于截留的空气泡层，减少了细菌与表面之间的接触
  - 条件: {'mechanism': 'entrapped air-bubble layer reduces contact between bacteria and surface', 'state': 'Cassie-Baxter regime with air trapped underneath', 'bacteria_type': 'gram-positive', 'signal': 'autoinducing peptide (AIP)'}
  - 来源: literature: 10.33263/BRIAC132.185

## 工程约束

- **超疏水表面接触角阈值 Superhydrophobic contact angle threshold**: 接触角>150°表现为超疏水行为；接触角<10°为超亲水 degrees
  - 条件: {'superhydrophobic': '>150°', 'superhydrophilic': '<10°', 'classification': 'based on contact angle with substratum surface'}
  - 来源: literature: 10.33263/BRIAC132.185
- **TiO2纳米颗粒仿鲨鱼皮抗菌 TiO2 nanoparticle photocatalytic shark-skin antibacterial**: 抗菌TiO2纳米颗粒+光催化仿鲨鱼皮图案表面使E. coli附着比相同化学成分的平滑膜减少约70% percent
  - 条件: {'biomimetic_source': 'shark skin pattern', 'nanoparticles': 'titanium dioxide (TiO2) NPs', 'mechanism': 'photocatalytic', 'target': 'Escherichia coli', 'reduction': '~70%', 'comparison': 'compared with smooth films with same chemical composition', 'plants': 'lotus (Nelumbo nucifera), water fern (Salvinia), lady mantle (Alchemilla mollis)', 'animals': 'shark (dermal denticles with microstructured ribbons)'}
  - 来源: literature: 10.33263/BRIAC132.185
- **超疏水表面防污机制 Superhydrophobic surface antifouling mechanism**: 超疏水表面的抗污性能归因于截留的空气泡层，减少了细菌与表面之间的接触 None
  - 条件: {'mechanism': 'entrapped air-bubble layer reduces contact between bacteria and surface', 'state': 'Cassie-Baxter regime with air trapped underneath', 'bacteria_type': 'gram-positive', 'signal': 'autoinducing peptide (AIP)'}
  - 来源: literature: 10.33263/BRIAC132.185
- **超疏水表面防污短暂性 Superhydrophobic surface antifouling short-lived**: 超疏水表面的抗污性能是短暂的（short-lived） None
  - 条件: {'limitation': 'anti-biofouling properties are short-lived'}
  - 来源: literature: 10.33263/BRIAC132.185
- **硅基超疏水材料机械稳定性挑战**: 纳米级结构强度有限，耐磨性不足是工业化主要障碍 None
  - 条件: {'challenge_1': '微纳结构在纳米级别时强度有限', 'challenge_2': '现有研究尝试在强厚多孔结构中制备涂层以增强耐久性，但非普适方案', 'challenge_3': '微米级网格可保护内部纳米结构但无法抵抗切割和穿刺', 'status': '所有超疏水材料均需解决的通用问题'}
  - 来源: literature: 10.3390/polym15030543

## 来源汇总

- literature: 10.1002/admi.202201425
- literature: 10.1016/j.jmst.2020.07.002
- literature: 10.33263/BRIAC132.185
- literature: 10.3390/polym15030543
