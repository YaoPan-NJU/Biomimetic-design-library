# polydopamine-coating

## 元数据

- **原型 ID**: polydopamine-coating
- **知识条目数**: 125
- **性能数据数**: 9
- **机制描述数**: 6
- **工程约束数**: 15

## 仿生元数据

- **organism_scientific**: Mytilus edulis（贻贝，聚多巴胺仿生来源）
- **biomimetic_dimension**: 分子仿生
- **features**: ['邻苯二酚基团', '氨基功能基团', '多巴胺氧化自聚合', 'pH敏感性', 'π-π*电子跃迁', '中空介孔结构', '表面强粘附性']
- **applicability**: {'pH_range': [4.5, 7.4], 'temp_range': [25, 50], 'salinity': 'low'}
- **engineering_constraints**: [{'constraint': '生物相容性', 'relevance': 'high', 'explanation': '空白载体在0.98~1000μg/mL浓度范围内对人正常肝细胞LO2存活率>80%，安全性良好'}, {'constraint': 'pH响应性', 'relevance': 'high', 'explanation': '聚多巴胺在肿瘤微酸性环境中可解聚，实现pH响应性药物释放'}, {'constraint': '冻干条件', 'relevance': 'medium', 'explanation': '冷冻干燥温度-40~-70°C，时间12-24h'}, {'constraint': 'HF蚀刻安全性', 'relevance': 'medium', 'explanation': '使用3-5%氢氟酸水溶液蚀刻二氧化硅硬模板，需注意安全防护'}]

## 仿生叙事

### problem_definition

脂溶性色素（姜黄素、番茄红素）具有抗肿瘤、抗氧化等广泛药理作用，但难溶于水、口服不易吸收、存在肝脏首过效应、体内代谢清除快、生物利用率低、稳定性差、见光易分解，需要合适的药物递送系统解决这些问题。

### biological_solution

聚多巴胺（PDA）是天然生物色素黑色素的主要成分，通过多巴胺的氧化自聚合反应得到，具有良好的稳定性、生物可降解性、生物相容性和光热转换特性。PDA表面具有大量邻苯二酚和氨基功能基团，具有很强的粘附性（仿贻贝足丝蛋白机制），可包覆在多种材料表面。壳聚糖是由氨基葡萄糖组成的天然阳离子聚合物，具有良好的生物相容性、低毒性和可生物降解性，且具有肠粘膜粘附特性。

### key_features

必须保留：中空介孔聚多巴胺纳米粒（HPDA）作为核心载体（高比表面积、纳米孔道、中空结构、pH敏感性、邻苯二酚/氨基官能团）、聚乙二醇改性壳聚糖作为外层包覆（肠粘膜粘附、减少巨噬细胞摄取、被动靶向）。可灵活调整：HPDA与脂溶性色素质量比（5-8:1）、壳聚糖与PEG质量比（1:0.2-0.3）、冻干条件。

### design_mapping

生物结构→材料设计：贻贝足丝蛋白→多巴胺自聚合→聚多巴胺（PDA）载体；天然生物色素黑色素→PDA化学组成；甲壳类动物外壳→壳聚糖→PEG改性壳聚糖外层包覆。中空介孔结构→硬模板法（SiO2模板+HF蚀刻）。软约束建议：保留邻苯二酚和氨基官能团是物理+化学吸附的关键，中空介孔结构是高负载效率的核心，壳聚糖包覆是肠粘膜粘附和延释的保障。

### explainability_anchors

仿生故事线：模仿贻贝足丝蛋白的邻苯二酚粘附化学，用多巴胺自聚合制备聚多巴胺中空介孔纳米粒作为药物载体；利用天然壳聚糖的肠粘膜粘附特性作为外层包衣，实现脂溶性色素的高效负载、pH响应释放和靶向缓释。设计溯源：贻贝→多巴胺→PDA→中空介孔结构（SiO2硬模板+HF蚀刻）→物理+化学吸附脂溶性色素→PEG-CS包覆→肿瘤pH响应释放。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| 最大吸附容量 qmax — BC/PDA/La(OH)3复合材料 | 159.8 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 吸附容量对比 — BC/PDA/La(OH)3 vs BC/La(OH)3 vs BC/PDA vs BC | 159.8 vs 91.2 vs 12.6 vs 0 | mg/g | 无机磷 |  | patent |
| 循环稳定性 — 5次循环后吸附容量保持 | 110 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 实际水体吸附容量 | 143.4 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 循环吸附稳定性-重金属去除率保持 | >72 | % |  |  | patent: CN115055171A |
| 最大吸附容量 qmax — BC/PDA/La(OH)3复合材料 | 159.8 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 吸附容量对比 — BC/PDA/La(OH)3 vs BC/La(OH)3 vs BC/PDA vs BC | 159.8 vs 91.2 vs 12.6 vs 0 | mg/g | 无机磷 |  | patent |
| 循环稳定性 — 5次循环后吸附容量保持 | 110 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 实际水体吸附容量 | 143.4 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |

## 吸附机制

- **吸附机制 — 配位螯合**: La与磷酸根配位生成磷酸镧化合物
  - 条件: {'mechanism_type': '化学吸附/配位作用', 'active_component': 'La(OH)3纳米颗粒'}
- **PDA吸附机制-姜黄素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + 形成羰基键', 'description': 'PDA与姜黄素分子产生物理吸附（π-π*电子跃迁）和化学吸附（羰基键）'}
- **PDA吸附机制-番茄红素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + michael加成反应', 'description': 'PDA与番茄红素分子产生物理吸附（π-π*电子跃迁）和化学吸附（michael加成反应）'}
- **吸附机制 — 配位螯合**: La与磷酸根配位生成磷酸镧化合物
  - 条件: {'mechanism_type': '化学吸附/配位作用', 'active_component': 'La(OH)3纳米颗粒'}
- **水滴'生长-跳跃'排液机制 Water droplet 'growing-jumping' discharge mechanism**: 两阶段机制：'生长'阶段(水滴在微腔中核化生长→Laplace压力梯度∇P~2σ/d_eq(1/R₁-1/R₂)驱动水滴变形自导向)→'跳跃'阶段(合并后表面能释放触发自发跳跃运动，低粘附力确保跳跃)
  - 条件: {'stage_1_growing': '水滴在微腔中核化生长→随机和reentrant几何结构导致变形→Laplace压力梯度∇P驱动自导向', 'stage_2_jumping': '合并后表面能释放→自发面外跳跃运动→低粘附力确保跳跃', 'laplace_pressure': '∇P ~ 2σ/d_eq(1/R₁ - 1/R₂)', 'purpose': '避免粘性Wenzel态破坏超疏水性，确保稳定乳液分离'}
  - 来源: literature: 10.1016/j.seppur.2023.123547
- **油滴捕获的'捕获-聚并-脱离'机制 Oil capture 'capture-coalescence-detachment' mechanism**: 三阶段机制：'捕获'(超疏水Al₂O₃突起作为油吸收器捕获微小油滴，不平衡力Fd=γ_oil(cosθ₁-cosθ₂)驱动)→'聚并'(被捕获油滴作为油储库，小油滴聚并成大油滴)→'脱离'(水下超疏油PDA/PET表面+Al₂O₃突起表面张力排斥大油滴)
  - 条件: {'stage_1_capture': '超疏水Al₂O₃突起捕获微小油滴，Fd = γ_oil(cosθ₁-cosθ₂)驱动(θ₁<1°, θ₂>150°)', 'stage_2_coalescence': "被捕获油滴作为'油储库'，小油滴聚并成大油滴", 'stage_3_detachment': '水下超疏油PDA/PET表面+Al₂O₃突起表面张力排斥大油滴脱离', 'hydration_layer': '亲水PDA/PET区域的水化层排斥被捕获油滴'}
  - 来源: literature: 10.1016/j.seppur.2023.123547

## 工程约束

- **循环稳定性 — 5次循环后吸附容量保持**: 110 mg/g
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'pollutant': '无机磷', 'cycles': 5, 'desorption_condition': '0.1 mol/L NaOH甲醇溶液超声解吸'}
- **镧泄漏量 — 5次循环**: 5 mg/L
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'cycles': 5, 'measurement_type': '最大值上限'}
- **pH适用范围**: 150 mg/g
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'pollutant': '无机磷', 'ph_range': '5.0-9.0', 'tested_ph_values': [5.0, 6.0, 7.0, 8.0, 9.0]}
- **番茄红素光稳定性提升**: 97.98 %
  - 条件: {'material': 'HPDA@LYC（纳米包埋后）', 'control': '番茄红素粉末（未包埋）', 'light_condition': '室内散射光全光照射', 'duration': '12h', 'temperature': '25°C', 'control_retention': '83.75%', 'improvement': '从83.75%提升至97.98%'}
- **PDA的pH敏感性机制**: None None
  - 条件: {'mechanism': '聚多巴胺在肿瘤微酸性环境中可解聚', 'application': '响应肿瘤部位pH值，提高肿瘤胞内有效脂溶性色素浓度'}
- **步骤2-Tris缓冲液pH**: 8-10 None
  - 条件: {'优选': '8.5-9', '实施例1': 'pH 8.0'}
- **循环吸附稳定性-重金属去除率保持**: >72 %
  - 条件: {'循环次数': '5-10次解吸试验后', '最优选(镍离子)': '去除率保持在78%以上'}
- **循环吸附稳定性-材料回收率**: >82 %
  - 条件: {'循环次数': '5-10次解吸试验后'}
- **循环稳定性 — 5次循环后吸附容量保持**: 110 mg/g
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'pollutant': '无机磷', 'cycles': 5, 'desorption_condition': '0.1 mol/L NaOH甲醇溶液超声解吸'}
- **镧泄漏量 — 5次循环**: 5 mg/L
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'cycles': 5, 'measurement_type': '最大值上限'}

## 来源汇总

- literature: 10.1016/j.seppur.2023.123547
- patent
- patent: CN115040496A
- patent: CN115055171A
