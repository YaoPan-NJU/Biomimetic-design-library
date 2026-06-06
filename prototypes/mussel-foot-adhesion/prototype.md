# mussel-foot-adhesion

## 元数据

- **原型 ID**: mussel-foot-adhesion
- **知识条目数**: 488
- **性能数据数**: 31
- **机制描述数**: 27
- **工程约束数**: 60

## 仿生元数据

- **organism_scientific**: Nelumbo nucifera, Mytilus edulis, Oryza sativa, Stenocara gracilipes, Nepenthes
- **biomimetic_dimension**: 结构仿生
- **features**: ['层级微纳结构', 're-entrant几何', 'Janus不对称润湿', '液体灌注', '智能响应切换', '双超疏液', '预润湿切换']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '机械稳定性与鲁棒性', 'relevance': 'high', 'explanation': '微纳结构在复杂水流和摩擦下易受损，需通过层级结构递推或液体灌注策略来维持Cassie态并增强鲁棒性。'}, {'constraint': '表面能精确控制', 'relevance': 'high', 'explanation': '按需分离（尤其是分离表面能差异极小的不混溶有机液体）高度依赖表面能的精确调控，需严格遵循IWT理论和极性-非极性理论。'}, {'constraint': '通量与截留率的权衡', 'relevance': 'medium', 'explanation': '传统2D膜面临通量瓶颈，需通过设计3D Janus材料（如海绵/气凝胶）利用凝聚分离机制替代尺寸筛分，以突破通量限制。'}]

## 仿生叙事

### problem_definition

自然界中生物需在水、油、气等多相复杂环境中实现自清洁、捕食或水面行走；在水处理领域，这对应于高效分离油水乳液、多层油水混合物及多相不混溶有机液体的严苛需求，传统材料难以兼顾高通量、高选择性与多相适应性。

### biological_solution

生物通过进化出层级微纳结构（如荷叶微乳突）、特殊几何形貌（re-entrant结构）、不对称润湿（荷叶上下表面差异）及液体灌注（猪笼草）等策略，实现超润湿或双超疏液特性。这些机制结合四大润湿性理论（Young/Wenzel/Cassie、IWT、极性-非极性、液体灌注），为设计按需分离材料提供了定量指导。

### key_features

必须保留特征：层级微纳结构（增强润湿性并维持鲁棒性）、表面化学与微观形貌的协同调控。可灵活调整特征：智能响应触发器类型（pH/热/光/电/溶剂/离子/气体）、Janus膜的不对称润湿方向、液体灌注的润滑液选择及3D孔隙结构。

### design_mapping

生物原型到材料的映射：荷叶微乳突→静电纺丝/模板法构建微纳粗糙度；贻贝足丝蛋白→PDA（聚多巴胺）涂层实现通用双亲性修饰；猪笼草→多孔材料注入润滑液实现双超疏液。软约束建议：优先采用PDA等温和仿生涂层结合静电纺丝或定向冻塑构建3D多孔网络，以平衡高通量与高截留率，并利用预润湿或外部刺激实现按需切换。

### explainability_anchors

仿生故事线：从‘荷叶出淤泥而不染’的自清洁现象，演进到‘智能响应按需分离’的多相液体处理系统。设计溯源：基于超疏水理论构建基础微纳结构→利用IWT理论精确设计表面能→引入re-entrant几何突破双超疏液限制→结合极性与液体灌注理论实现多相不混溶液体分离。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| 铀吸附容量 / Uranium adsorption capacity | 403.21 | mg/g | 铀(U) | PDA改性PAO薄膜 | patent |
| 改性时间对铀吸附容量影响 / Effect of modification time on U adsorption | 改性时间4h→403.085mg/g; 8h→403.045mg/g; 12h→403.21mg/g，影响不大 | mg/g |  |  | patent |
| 铀吸附容量计算公式 / Uranium adsorption capacity calculation formula | qt = (C0 - Ce) × V / m | None |  |  | patent |
| 铀吸附容量 Uranium adsorption capacity | >50 | mg/g | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 铀去除率 Uranium removal rate (pH≥5) | >90 | % | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 特定条件下去除率 Removal rate at pH 3.0 | 97.3 | % | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 循环吸附稳定性-重金属去除率保持 | >72 | % |  |  | patent: CN115055171A |
| 实施例1对Cu2+吸附容量 / Example 1 adsorption capacity for Cu2+ | 12.5 | mg/g | Cu2+ | PDA-Fe3O4@CS | patent |
| 实施例1对CrO42-吸附容量 / Example 1 adsorption capacity for CrO42- | 114.88 | mg/g | CrO42- | PDA-Fe3O4@CS | patent |
| PDA:CS质量比对Cu2+吸附容量影响 / Effect of PDA:CS ratio on Cu2+ adsorption | PDA:CS=1:4→12.5mg/g; 1:2→15mg/g; 3:4→17.5mg/g; 5:4→25mg/g; 3:2→47.5mg/g(峰值); 7:4→45mg/g(下降) | mg/g | Cu2+ |  | patent |
| PDA:CS质量比对CrO42-吸附容量影响 / Effect of PDA:CS ratio on CrO42- adsorption | PDA:CS=1:4→114.88mg/g; 1:2→109.77mg/g; 3:4→105.8mg/g; 5:4→98.2mg/g; 3:2→88mg/g; 7:4→91.88mg/g | mg/g | CrO42- |  | patent |
| 铀吸附容量 / Uranium adsorption capacity | 403.21 | mg/g | 铀(U) | PDA改性PAO薄膜 | patent |
| 改性时间对铀吸附容量影响 / Effect of modification time on U adsorption | 改性时间4h→403.085mg/g; 8h→403.045mg/g; 12h→403.21mg/g，影响不大 | mg/g |  |  | patent |
| 铀吸附容量计算公式 / Uranium adsorption capacity calculation formula | qt = (C0 - Ce) × V / m | None |  |  | patent |
| 铀吸附容量 Uranium adsorption capacity | >50 | mg/g | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 铀去除率 Uranium removal rate (pH≥5) | >90 | % | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 特定条件下去除率 Removal rate at pH 3.0 | 97.3 | % | 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | patent |
| 实施例1对Cu2+吸附容量 / Example 1 adsorption capacity for Cu2+ | 12.5 | mg/g | Cu2+ | PDA-Fe3O4@CS | patent |
| 实施例1对CrO42-吸附容量 / Example 1 adsorption capacity for CrO42- | 114.88 | mg/g | CrO42- | PDA-Fe3O4@CS | patent |
| PDA:CS质量比对Cu2+吸附容量影响 / Effect of PDA:CS ratio on Cu2+ adsorption | PDA:CS=1:4→12.5mg/g; 1:2→15mg/g; 3:4→17.5mg/g; 5:4→25mg/g; 3:2→47.5mg/g(峰值); 7:4→45mg/g(下降) | mg/g | Cu2+ |  | patent |

## 吸附机制

- **吸附机制-螯合作用 / Adsorption mechanism - chelation**: 聚多巴胺结构中的含氮基团与重金属离子的鳌合作用
  - 条件: {'functional_groups': '含氮基团（儿茶酚/胺基）', 'interaction_type': '配位螯合', 'target': '重金属离子'}
- **贻贝仿生启发机制 / Mussel-inspired biomimetic mechanism**: 通过聚多巴胺自组装单分子层技术对聚酯纤维织物进行表面修饰，受贻贝足丝蛋白粘附机制启发
  - 条件: {'biomimetic_organism': '贻贝(mussel)', 'biological_mechanism': '贻贝足丝蛋白通过多巴胺类化合物的氧化聚合实现强粘附', 'translation_to_material': '聚多巴胺涂层作为桥梁连接聚酯基体和重金属离子'}
- **仿贻贝聚多巴胺改性机制 / Mussel-inspired PDA modification mechanism**: 多巴胺自聚合形成聚多巴胺对PAO薄膜进行表面改性
  - 条件: {'biomimetic_organism': '贻贝(mussel)', 'mechanism': '多巴胺自聚合(oxidative self-polymerization)', 'substrate': 'PAO薄膜', 'functional_groups': '邻苯二酚(catechol)、亚胺/胺基团', 'interaction_types': ['静电相互作用', '共价反应', '非共价作用力(范德华力、氢键)', '金属配位/螯合']}
- **PDA吸附机制-姜黄素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + 形成羰基键', 'description': 'PDA与姜黄素分子产生物理吸附（π-π*电子跃迁）和化学吸附（羰基键）'}
- **PDA吸附机制-番茄红素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + michael加成反应', 'description': 'PDA与番茄红素分子产生物理吸附（π-π*电子跃迁）和化学吸附（michael加成反应）'}
- **聚多巴胺聚合机理 Polydopamine polymerization mechanism**: 多巴胺在弱碱性环境下通过酚羟基氧化成醌，醌式相互叠加实现聚合；聚多巴胺在Fe3O4外以羟基间氢键或物理堆积形式沉积，不涉及与Fe元素的配位作用
  - 条件: {'biomimetic_source': '贻贝足丝蛋白仿生', 'buffer_system': 'Tris-HCl缓冲体系(pH 8.48-8.52)', 'mechanism': '酚羟基氧化→醌式叠加→氢键/物理堆积沉积'}
- **铀吸附机制 Uranium adsorption mechanism**: 聚多巴胺壳层大量羟基为主要吸附位点，氨基主要参与苯环成环，仅部分氨基参与与铀的作用
  - 条件: {'pollutant': '铀 U(VI)', 'material': '聚多巴胺包覆Fe3O4磁性仿生吸附剂', 'primary_group': '羟基(-OH)', 'secondary_group': '氨基(-NH2)'}
- **贻贝仿生改性机制 / Mussel-inspired biomimetic modification mechanism**: 利用贻贝仿生学，通过多巴胺的氧化自聚作用，形成黏附力极强的聚多巴胺涂覆在磁性壳聚糖基体表面
  - 条件: {'biomimetic_organism': '贻贝(mussel)', 'biological_mechanism': '贻贝足丝特有的黏附特性主要来自于L-多巴(L-DOPA)和赖氨酸残基', 'translation': '多巴胺在含氧的弱碱性水溶液里发生氧化自聚，制备出具有超强黏附性能的聚多巴胺涂层', 'historical_context': '1983年Waite发现贻贝足丝黏附机制；2007年Messersmith等首次制备PDA涂层'}
- **吸附机制-螯合作用 / Adsorption mechanism - chelation**: 聚多巴胺结构中的含氮基团与重金属离子的鳌合作用
  - 条件: {'functional_groups': '含氮基团（儿茶酚/胺基）', 'interaction_type': '配位螯合', 'target': '重金属离子'}
- **贻贝仿生启发机制 / Mussel-inspired biomimetic mechanism**: 通过聚多巴胺自组装单分子层技术对聚酯纤维织物进行表面修饰，受贻贝足丝蛋白粘附机制启发
  - 条件: {'biomimetic_organism': '贻贝(mussel)', 'biological_mechanism': '贻贝足丝蛋白通过多巴胺类化合物的氧化聚合实现强粘附', 'translation_to_material': '聚多巴胺涂层作为桥梁连接聚酯基体和重金属离子'}

## 工程约束

- **多巴胺水溶液pH调节 / Dopamine solution pH adjustment**: pH 7.5-9.5（较佳范围）；pH 8.5（最佳） None
  - 条件: {'optimal': '8.5', 'range': '7.5-9.5'}
- **反应温度 / Reaction temperature**: 20-40°C（较佳范围）；30°C（最佳） °C
  - 条件: {'optimal': '30°C', 'range': '20-40°C', 'observation': '随着反应温度的增加，聚酯纤维织物表面的颜色也越深'}
- **薄膜成型-分相脱膜条件 / Film formation phase inversion conditions**: 刮涂厚度0.8mm，浸入水中3min分相脱膜，40°C干燥24h None
  - 条件: {'coating_thickness': '0.8mm', 'phase_inversion': '常温去离子水中3min', 'drying_temp': '40°C', 'drying_time': '24h', 'appearance': '淡黄色的半透明状材料'}
- **PAO薄膜SEM形貌 / PAO film SEM morphology**: 表面光滑平整，分布着许多形状不规则的小孔 None
  - 条件: {'technique': 'SEM(扫描电镜)', 'figure': '图3', 'surface': '光滑平整', 'pores': '形状不规则的小孔'}
- **PDA改性薄膜SEM形貌 / PDA-modified film SEM morphology**: 表面粗糙，无孔隙的存在，聚多巴胺像'鱼鳞'一样分层沉积在材料表面 None
  - 条件: {'technique': 'SEM(扫描电镜)', 'figure': '图4', 'surface': '粗糙', 'pores': '无孔隙', 'pda_morphology': "像'鱼鳞'一样分层沉积"}
- **非溶剂致相分离法(NIPS)制备PAO薄膜 / Non-solvent induced phase separation for PAO film**: 采用非溶剂致相分离法制备PAO薄膜材料 None
  - 条件: {'method': '非溶剂致相分离法(NIPS)', 'process': 'PAO溶液刮涂成膜→浸入水中分相脱膜→干燥', 'advantage': '薄膜成型简单'}
- **番茄红素光稳定性提升**: 97.98 %
  - 条件: {'material': 'HPDA@LYC（纳米包埋后）', 'control': '番茄红素粉末（未包埋）', 'light_condition': '室内散射光全光照射', 'duration': '12h', 'temperature': '25°C', 'control_retention': '83.75%', 'improvement': '从83.75%提升至97.98%'}
- **PDA的pH敏感性机制**: None None
  - 条件: {'mechanism': '聚多巴胺在肿瘤微酸性环境中可解聚', 'application': '响应肿瘤部位pH值，提高肿瘤胞内有效脂溶性色素浓度'}
- **铀去除率 Uranium removal rate (pH≥5)**: >90 %
  - 条件: {'pollutant': '铀 U(VI)', 'material': '聚多巴胺包覆Fe3O4磁性仿生吸附剂', 'ph': '≥5', 'initial_concentration': '100 mg/L'}
- **特定条件下去除率 Removal rate at pH 3.0**: 97.3 %
  - 条件: {'pollutant': '铀 U(VI)', 'material': '聚多巴胺包覆Fe3O4磁性仿生吸附剂', 'ph': 3.0, 'initial_concentration': '100 mg/L', 'volume': '25 mL', 'adsorbent_dosage': '0.05 g', 'temperature': '25±0.2°C', 'shaking_speed': '240 r/min', 'contact_time': '72 h', 'detection_method': '分光光度法(偶氮砷III指示剂)'}

## 来源汇总

- literature: 10.1002/smll.202204624
- literature: 10.1016/j.apcatb.2023.122852
- literature: 10.1016/j.carbpol.2022.120242
- literature: 10.1016/j.cej.2021.129237
- literature: 10.1021/acsami.0c18794
- literature: 10.1021/acsnano.4c18335
- literature: 10.1021/acsnano.5c01252
- literature: 10.1039/d1cs00658d
- literature: 10.1039/d5su00041f
- literature: 10.3390/nano11113008
- patent
- patent: CN115040496A
- patent: CN115055171A
