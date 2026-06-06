# cellulose-nanocrystal

## 元数据

- **原型 ID**: cellulose-nanocrystal
- **知识条目数**: 930
- **性能数据数**: 95
- **机制描述数**: 35
- **工程约束数**: 75

## 仿生元数据

- **biomimetic_dimension**: 分子仿生
- **features**: ['双组分协同(-COOH)', '氨基孤对电子配位(-NH₂)', 'Ca²⁺离子交联三维网络', 'pH/水响应性溶胀收缩', '单层化学吸附主导']
- **applicability**: {'pH_range': [2, 5], 'temp_range': [297, 310], 'salinity': None}
- **engineering_constraints**: [{'constraint': 'pH操作窗口', 'relevance': 'high', 'explanation': '最优吸附pH为4，pH过低导致-COOH质子化削弱静电作用，需将体系严格控制在2-5范围内以维持官能团活性。'}, {'constraint': '湿态/干态机械强度', 'relevance': 'medium', 'explanation': '干燥后表面褶皱且强度略弱，实际工程中建议湿态操作或优化交联密度以维持珠体结构完整性与循环稳定性。'}, {'constraint': '交联剂依赖', 'relevance': 'medium', 'explanation': '依赖CaCl₂形成离子交联网络，交联程度直接影响溶胀率、内部传质速率与固液分离回收效率。'}]

## 仿生叙事

### problem_definition

自然界中生物大分子（如多糖与蛋白质）通过多官能团协同与特定金属离子结合以实现生理调控或解毒；对应水处理中Pb(II)的高效捕获、选择性去除及吸附剂便捷回收的工程挑战。

### biological_solution

进化出富含羧基与氨基的生物聚合物网络，利用静电吸引、配位键合及空间限域实现离子的高效固定；本设计通过羧基化壳聚糖与纳米纤维素双组分协同提供密集-COOH/-NH₂位点，结合Ca²⁺离子交联构建三维水凝胶网络，实现334.92 mg/g的高容量吸附与准二级化学吸附动力学。

### key_features

必须保留特征：双羧基化组分协同配位、氨基孤对电子结合、Ca²⁺离子交联三维网络、pH/水响应性溶胀收缩；可灵活调整特征：CYCS与CNC质量比、CaCl₂交联浓度、珠体粒径及表面孔隙结构。

### design_mapping

生物大分子多齿配位→CYCS/CNC双组分-COOH/-NH₂协同吸附位点；生物基质水合网络→CaCl₂离子交联水凝胶珠形态；细胞膜/基质离子交换→-COO⁻静电吸引与-NH₂配位机制。软约束建议：维持pH 2-5以保障官能团离子化状态；控制干燥-溶胀循环应力以防结构疲劳；优先采用湿珠形态以优化传质与回收。

### explainability_anchors

仿生故事线：从天然生物聚合物的多官能团离子捕获机制出发，抽象出“双组分协同+氨基配位+三维水合网络”的分子仿生范式；设计溯源：基于壳聚糖与纳米纤维素的天然生物骨架，通过羧基化改性提升溶解性与位点密度，利用Ca²⁺仿生交联原理构筑易分离水凝胶珠，完成从分子识别机制到宏观材料形态的跨尺度映射。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| 最大吸附容量 qmax — BC/PDA/La(OH)3复合材料 | 159.8 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 吸附容量对比 — BC/PDA/La(OH)3 vs BC/La(OH)3 vs BC/PDA vs BC | 159.8 vs 91.2 vs 12.6 vs 0 | mg/g | 无机磷 |  | patent |
| 循环稳定性 — 5次循环后吸附容量保持 | 110 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 实际水体吸附容量 | 143.4 | mg/g | 无机磷 | BC/PDA/La(OH)3-1 | patent |
| 实施例1-壳聚糖-ZIF-8-重氮化0.5g-吸附容量 | 70.7 | g/g | 二氯甲烷 | 壳聚糖-ZIF-8泡沫 | patent: CN121130847A |
| 实施例3-CNF-ZIF-8-高浓度MOF前驱体-吸附容量 | 87.6 | g/g | 二氯甲烷 | 纤维素纳米纤维-ZIF-8泡沫 | patent: CN121130847A |
| 实施例4-明胶-ZIF-8-TMCS疏水改性-吸附容量 | 81 | g/g | 二氯甲烷 | 明胶-ZIF-8泡沫 | patent: CN121130847A |
| 实施例5-明胶-ZIF-8-对甲苯磺酸重氮盐-吸附容量 | 88 | g/g | 二氯甲烷 | 明胶-ZIF-8泡沫 | patent: CN121130847A |
| 实施例6-明胶-ZIF-8-轻交联0.2g重氮盐-吸附容量 | 77.6 | g/g | 二氯甲烷 | 明胶-ZIF-8泡沫 | patent: CN121130847A |
| 对比例6-明胶-ZIF-8-过量交联1.0g重氮盐-吸附容量 | 54 | g/g | 二氯甲烷 | 明胶-ZIF-8泡沫 | patent: CN121130847A |
| 实施例7-明胶-ZIF-8(Zn)-吸附容量 | 77.6 | g/g | 二氯甲烷 | 明胶-ZIF-8泡沫(Zn2+) | patent: CN121130847A |
| 对比例7-明胶-ZIF-67(Co)-吸附容量 | 101 | g/g | 二氯甲烷 | 明胶-ZIF-67泡沫(Co2+) | patent: CN121130847A |
| 重氮化处理壳聚糖-MOF泡沫-广谱吸附容量范围 | 51.5-122 | g/g |  | 重氮化壳聚糖-ZIF-8泡沫 | patent: CN121130847A |
| 重氮化处理壳聚糖-MOF泡沫-对二氯甲烷吸附容量 | 107.1 | g/g | 二氯甲烷 | 重氮化壳聚糖-ZIF-8泡沫 | patent: CN121130847A |
| 重氮化处理壳聚糖-MOF泡沫-对柴油吸附容量 | 52 | g/g | 柴油 | 重氮化壳聚糖-ZIF-8泡沫 | patent: CN121130847A |
| 吸附剂对吸附容量的影响 | 有吸附剂时吸油容量显著提升 | None |  |  | patent: CN119488883A |
| 最大吸附容量 亚甲基蓝 纯溶液 | 113.64 | mg/g | 亚甲基蓝 (MB) | 吡啶酮双酸改性纤维素 | patent: CN108658160B |
| 最大吸附容量 结晶紫 纯溶液 | 120 | mg/g | 结晶紫 (CV) | 吡啶酮双酸改性纤维素 | patent: CN108658160B |
| 最大吸附容量 孔雀石绿 纯溶液 | 120 | mg/g | 孔雀石绿 (MG) | 吡啶酮双酸改性纤维素 | patent: CN108658160B |
| 最大吸附容量 曙红 纯溶液 | 2.52 | mg/g | 曙红 (Eosin) | 吡啶酮双酸改性纤维素 | patent: CN108658160B |

## 吸附机制

- **吸附机制 — 配位螯合**: La与磷酸根配位生成磷酸镧化合物
  - 条件: {'mechanism_type': '化学吸附/配位作用', 'active_component': 'La(OH)3纳米颗粒'}
- **吸附机制-π-π相互作用**: 偶氮基团带有π电子，可与油分子产生π-π相互作用，协同增加有机污染物捕获量
  - 条件: {'材料': '重氮化改性泡沫', '污染物': '有机溶剂/油类'}
- **选择性吸附机制**: 羧酸基团在中性或弱碱性条件下显负电性，通过强电负性与带正电的阳离子染料分子螯合，选择性吸附阳离子染料
  - 条件: {'material': '吡啶酮双酸改性纤维素', 'functional_group': '羧酸基团 (-COOH/-COO⁻)', 'optimal_condition': '中性或弱碱性 (pH 7-9)', 'mechanism': '静电作用 + 氢键 + 范德华力', 'selectivity_basis': '电荷选择性（阳离子 vs 阴离子染料）+ 分子结构匹配（共平面性）'}
- **吸附机制 — 配位螯合**: La与磷酸根配位生成磷酸镧化合物
  - 条件: {'mechanism_type': '化学吸附/配位作用', 'active_component': 'La(OH)3纳米颗粒'}
- **选择性吸附机制 Selective adsorption mechanism**: 羧酸基团在中性/弱碱性条件下显负电性，利用电负性与带正电阳离子染料螯合；同时受氢键、范德华力影响；染料分子平面性影响作用方式(共平面的亚甲基蓝比非共平面的结晶紫更易与吸附剂作用)
  - 条件: {'functional_group': '吡啶酮羧酸基团', 'charge_mechanism': '羧酸基团负电性 → 阳离子染料静电螯合', 'secondary_forces': '氢键、范德华力', 'structural_factor': '染料分子平面性(亚甲基蓝共平面 vs 结晶紫非共平面)'}
- **碳纳米管对BPA的吸附机制 Adsorption mechanism of CNTs for BPA**: BPA分子中两个苯环可通过π-π电子供体-受体机制平行吸附在CNT表面；三种吸附位点：表面、沟槽区、间隙孔；CNT吸附容量范围43.76-580 mg/g
  - 条件: {'capacity_range': '43.76-580 mg/g', 'adsorption_sites': ['表面', '沟槽区', '间隙孔'], 'mechanism': 'π-π电子供体-受体机制', 'orientation': '平行于管轴、圆周方向或对角线方向'}
  - 来源: literature: 10.1016/j.cej.2024.149414
- **BPA吸附的主要机制 Main adsorption mechanisms for BPA**: 六种主要机制：静电相互作用、π-π相互作用、疏水作用、酸碱作用、氢键、孔隙填充，以及这些机制的组合
  - 条件: {'mechanisms': ['静电相互作用(electrostatic interaction)', 'π-π相互作用(π-π interaction)', '疏水作用(hydrophobic interaction)', '酸碱作用(acid-base interaction)', '氢键(hydrogen bonding)', '孔隙填充(pore filling)']}
  - 来源: literature: 10.1016/j.cej.2024.149414
- **NF膜去除BPA的机制 NF membrane BPA removal mechanism**: NF膜通过尺寸排阻、吸附、静电排斥和Donnan效应的组合作用去除BPA；NF膜通常带负电荷(表面可离解基团电离)，与BPA阴离子产生静电排斥
  - 条件: {'mechanisms': ['尺寸排阻', '吸附', '静电排斥', 'Donnan效应'], 'membrane_charge': '通常带负电荷(表面可离解基团电离)', 'NF_removal': '>90% (多数)', 'integrated_processes': 'NF-Fenton, NF-臭氧化, NF-吸附可提高去除率'}
  - 来源: literature: 10.1016/j.cej.2024.149414
- **DFT和MD在BPA吸附机制研究中的应用 DFT and MD in BPA adsorption mechanism studies**: DFT可计算电子结构和吸附能(如rGO-BPA吸附能6.71 kcal/mol, GO-BPA 11.85 kcal/mol)；MD可模拟吸附动力学和分子间相互作用(如π-π堆积、色散力、氢键)；EDA可分解不同吸附力的贡献比例
  - 条件: {'DFT_application': '计算电子结构、吸附能、反应中间体、能量势垒', 'rGO_BPA_Ead': '6.71 kcal/mol (物理吸附为主)', 'GO_BPA_Ead': '11.85 kcal/mol', 'MD_application': '模拟吸附动力学、表面扩散、吸附构型稳定性', 'EDA': '能量分解分析，定量不同吸附力的贡献比例'}
  - 来源: literature: 10.1016/j.cej.2024.149414
- **MF膜去除BPA的机制 MF membrane BPA removal mechanism**: MF膜孔径(0.1-10μm)大于BPA分子尺寸(7.52Å)，BPA去除主要通过大颗粒吸附和膜表面吸附(非尺寸排阻)；去除率18-95%
  - 条件: {'membrane_pore_size': '0.1-10 μm', 'BPA_size': '7.52 Å (van der Waals直径)', 'mechanism': '吸附效应(大颗粒截留或膜表面吸附)，非尺寸排阻', 'removal_range': '18-95%', 'MF_rarely_used_alone': '常与其他技术联用'}
  - 来源: literature: 10.1016/j.cej.2024.149414

## 工程约束

- **循环稳定性 — 5次循环后吸附容量保持**: 110 mg/g
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'pollutant': '无机磷', 'cycles': 5, 'desorption_condition': '0.1 mol/L NaOH甲醇溶液超声解吸'}
- **镧泄漏量 — 5次循环**: 5 mg/L
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'cycles': 5, 'measurement_type': '最大值上限'}
- **pH适用范围**: 150 mg/g
  - 条件: {'material': 'BC/PDA/La(OH)3-1', 'pollutant': '无机磷', 'ph_range': '5.0-9.0', 'tested_ph_values': [5.0, 6.0, 7.0, 8.0, 9.0]}
- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-首次吸附量**: 70.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第1次'}
- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-20次循环后吸附量**: 61.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第20次', '衰减': '12.5%'}
- **未重氮化壳聚糖-MOF泡沫-循环吸附二氯甲烷-性能衰减**: 前8次循环吸附量迅速下降 None
  - 条件: {'pollutant': '二氯甲烷', 'material': '未重氮化壳聚糖-ZIF-8泡沫', '原因': '骨架结构塌陷，MOF颗粒脱落或团聚'}
- **实施例3配方（循环测试对象）**: 纤维素纳米纤维2.0g+埃洛石1.5g+玻璃纤维0.25g+PEI-ECH 0.5g/100g水+MTMS疏水改性3min None
  - 条件: {'polymer': '纤维素纳米纤维 2.0g', 'adsorbent': '埃洛石 1.5g', 'reinforcement': '玻璃纤维 0.25g', 'crosslinker': '聚酰胺-环氧氯丙烷 0.5g（替代FeCl₃）', 'conditions': '50°C, 5000rpm搅拌≥2h', 'hydrophobic': '甲基三甲氧基硅烷(MTMS)乙醇溶液浸泡3min', 'special': '10次循环分离测试对象，力学性能优于对比例3', 'pollutants_tested': ['石油醚', '二氯乙烷', '二氯甲烷', '三氯甲烷', '甲基红', '甲苯', '四氯化碳'], 'claim_scope': '权利要求1', 'biomass_polymer': ['卡拉胶', '海藻酸钠', '羧甲基纤维素', '明胶', '纤维素纳米纤维', '魔芋葡甘聚糖', '羟乙基纤维素', '壳聚糖', '阿拉伯树胶', '结冷胶', '淀粉']}
- **最佳吸附pH**: 8 None
  - 条件: {'material': '吡啶酮双酸改性纤维素', 'tested_pH_range': [5, 6, 7, 8, 9], 'pollutant': '亚甲基蓝 + 曙红（纯溶液及混合溶液）', 'conclusion': '综合考虑最佳pH为8'}
- **pH 2 极端酸性条件下的抑制作用**: H+优先与吡啶酮双酸改性纤维素上的吸附位点发生相互作用，对染料吸附产生抑制 None
  - 条件: {'material': '吡啶酮双酸改性纤维素', 'ph': 2, 'mechanism': 'H+竞争吸附位点'}
- **pH 12 极端碱性条件下的影响**: 强碱性条件下亚甲基蓝的结构和性质发生细微改变，影响吸附过程 None
  - 条件: {'material': '吡啶酮双酸改性纤维素', 'ph': 12, 'mechanism': '强碱改变亚甲基蓝分子结构'}

## 来源汇总

- literature
- literature: 10.1007/s10924-021-02312-1
- literature: 10.1007/s10924-023-02989-6
- literature: 10.1007/s11783-021-1515-2
- literature: 10.1007/s13762-021-03603-9
- literature: 10.1016/j.carbpol.2021.118044
- literature: 10.1016/j.carbpol.2021.118471
- literature: 10.1016/j.carbpol.2022.119563
- literature: 10.1016/j.cej.2022.138934
- literature: 10.1016/j.cej.2024.149414
- literature: 10.1016/j.ijbiomac.2022.09.148
- literature: 10.1016/j.ijbiomac.2023.123916
- literature: 10.1016/j.jcis.2021.05.071
- literature: 10.1016/j.jclepro.2021.127630
- literature: 10.1016/j.jece.2021.106626
- literature: 10.1016/j.jhazmat.2021.127516
- literature: 10.1016/j.jhazmat.2022.129965
- literature: 10.1016/j.jobab.2023.12.002
- literature: 10.1016/j.molliq.2020.114523
- literature: 10.1016/j.molliq.2020.115122
- literature: 10.1016/j.scitotenv.2021.150606
- literature: 10.1021/acs.iecr.1c04583
- literature: 10.1038/s41467-021-23388-2
- literature: 10.11980/j.issn.0254-508X.2021.11.011
- literature: 10.16085/j.issn.1000-6613.2021-0391
- literature: 10.19965/j.cnki.iwt.2022-1185
- literature: 10.3390/molecules29184317
- literature: 10.3969/j.issn.1001-9731.2022.10.023
- literature: 10.3969/j.issn.1006-1878.2022.02.012
- patent
- patent: CN108658160B
- patent: CN119488883A
- patent: CN121130847A
