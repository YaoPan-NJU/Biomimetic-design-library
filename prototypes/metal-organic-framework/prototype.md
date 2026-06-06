# metal-organic-framework

## 元数据

- **原型 ID**: metal-organic-framework
- **知识条目数**: 950
- **性能数据数**: 78
- **机制描述数**: 54
- **工程约束数**: 81

## 仿生元数据

- **biomimetic_dimension**: 分子仿生
- **features**: ['多重非共价相互作用', '可设计溶剂', '阴阳离子组合调控', '磁性分离', '表面功能化', '核壳结构']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '物理涂层稳定性', 'relevance': 'high', 'explanation': '物理涂层在接触有机溶剂或复杂水体时易脱落，需采用化学键合（如硅烷化、点击化学）或聚合（PIL）以提高材料稳定性和重复使用性。'}, {'constraint': '孔道阻塞与比表面积平衡', 'relevance': 'medium', 'explanation': '在MOF等多孔骨架材料中引入IL可能占据孔道导致比表面积降低，需平衡IL功能化程度与孔道保留以维持吸附容量。'}, {'constraint': '合成复杂性与成本', 'relevance': 'medium', 'explanation': '化学键合和PIL聚合涉及多步反应和特定试剂（如硅烷偶联剂、交联剂），增加了材料制备的复杂性和成本。'}]

## 仿生叙事

### problem_definition

自然界中生物受体通过多重非共价相互作用实现对特定分子的高选择性识别；在水处理中，面对复杂水体中的重金属、染料和有机污染物，传统吸附材料缺乏精确的分子识别能力和易分离特性。

### biological_solution

进化策略：生物大分子通过氢键、静电、疏水作用和π-π堆积等多重弱相互作用实现高选择性结合。关键机制：离子液体（IL）作为“可设计溶剂”，通过阳离子（如咪唑鎓）和阴离子的灵活组合，精确调控亲疏水性、静电、氢键和π-π相互作用，模拟生物受体的多重识别机制。成功案例：IL功能化磁性纳米粒子（IL-MNPs）结合碳基材料（GO/CNTs），利用多重相互作用实现对Cr(VI)、Cd(II)等重金属及有机污染物的高效选择性吸附与磁分离。

### key_features

必须保留特征：IL的多重相互作用位点（疏水/离子交换/静电/氢键/π-π）和Fe3O4的超顺磁性。可灵活调整特征：IL的阳离子/阴离子类型、修饰骨架材料（裸Fe3O4/硅基/碳基/MOFs/MIPs等）、IL固定化方式（物理涂层/直接化学法/间接化学法/PIL聚合）。

### design_mapping

生物→材料映射：生物受体的多重识别位点 → IL的阴阳离子组合及多重非共价相互作用网络；生物体的磁性导航（如趋磁细菌） → Fe3O4磁性核。软约束建议：优先采用化学键合（如Si-IL或点击化学）替代物理涂层以确保长期稳定性；在多孔骨架（如MOFs）中修饰IL时，需控制修饰密度以防孔道堵塞；利用碳基材料（GO/CNTs）的高比表面积与IL协同提升萃取效率。

### explainability_anchors

仿生故事线：从生物分子的“多重弱相互作用协同识别”到离子液体的“可设计多重相互作用网络”，实现从自然识别机制到人工合成溶剂的跨越。设计溯源：IL-MNPs的设计灵感源于对生物分子识别机制的化学模拟，通过模块化组装（磁性核+骨架+IL功能层）实现吸附选择性与操作便捷性（磁分散固相萃取）的统一。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
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
| Cu(II)配位壳聚糖磁性材料对RBR的吸附容量 | 880.84 | mg/g | 活性亮红(RBR) | Cu(II)配位壳聚糖基磁性材料(CTS-Cu@SiO₂@Fe₃O₄) | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 磁性黄原酸盐改性壳聚糖对阳离子偶氮染料吸附容量 | MB: 197.8 mg/g, SO: 169.8 mg/g | mg/g |  | 磁性黄原酸盐改性壳聚糖 | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 壳聚糖凝胶珠对刚果红和直接黄染料的吸附容量 | CR: 1597 mg/g, DY: 1447 mg/g | mg/g |  | 二铵酒石酸盐改性壳聚糖凝胶珠(交联) | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 壳聚糖/膨润土复合物对染料吸附容量 | AR: 362.1 mg/g, MB: 496.5 mg/g | mg/g |  | 壳聚糖/膨润土混合复合物 | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 壳聚糖/聚丙烯酸/GO复合水凝胶对染料吸附容量 | MB: 296.5 mg/g, FY3: 280.3 mg/g | mg/g |  | 壳聚糖/聚丙烯酸/GO复合物理水凝胶 | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 磁性壳聚糖对SY染料吸附容量 | 769.23 | mg/g | SY染料 | 阳离子聚合物改性磁性壳聚糖珠(Fe₃O₄-CS/PDAC) | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 磁性壳聚糖复合物同时去除MB和MO的吸附容量 | 638.6 | mg/g |  | Fe₃O₄-CS复合物 | literature: 10.1016/j.ijbiomac.2021.04.158 |
| 聚丙烯酰胺/壳聚糖/Fe3O4复合水凝胶对MB吸附容量 | 1603 | mg/g | 亚甲基蓝(MB) | 聚丙烯酰胺/壳聚糖/Fe3O4复合水凝胶（Fe3O4原位合成） | literature: 10.1016/j.ijbiomac.2021.04.158 |
| ZIF-8@壳聚糖/PVA纳米纤维对MG吸附容量 | 1000 | mg/g | 孔雀石绿(MG) | 珍珠项链状ZIF-8@壳聚糖/PVA纳米纤维 | literature: 10.1016/j.ijbiomac.2021.04.158 |

## 吸附机制

- **吸附机制-π-π相互作用**: 偶氮基团带有π电子，可与油分子产生π-π相互作用，协同增加有机污染物捕获量
  - 条件: {'材料': '重氮化改性泡沫', '污染物': '有机溶剂/油类'}
- **壳聚糖的七种染料吸附机制**: 离子交换、络合、配位/螯合、静电相互作用、酸碱相互作用、氢键、疏水相互作用
  - 条件: {'material': '壳聚糖(CS)及其改性衍生物', 'functional_groups': '-OH和-NH₂基团', 'pH_dependence': 'pH变化可改变吸附剂结构和染料分子结构，影响吸附机制'}
  - 来源: literature: 10.1016/j.ijbiomac.2021.04.158
- **Cu-MOF配位驱动吸附机理**: 189.3
  - 条件: {'pollutant': 'Cr(VI) (HCrO₄⁻形式)', 'material': '{[Cu(L)₀.₅(bpe)(H₂O)]NO₃·0.5H₂O}ₙ', 'optimal_ph': 6, 'mechanism': '离子交换(HCrO₄⁻与NO₃⁻交换)+配位取代(HCrO₄⁻取代配位水分子与金属配位)', 'thermodynamics': 'Ion exchange: ΔG₁=-4.184 kJ·mol⁻¹; Coordination: ΔG₂=-17.1544 kJ·mol⁻¹; Total: ΔG=-21.3384 kJ·mol⁻¹', 'interference': 'CO₃²⁻存在时吸附去除率下降23%', 'desorption_condition': '100°C和1 g·L⁻¹ KNO₃溶液(苛刻条件)', 'reference': 'Shao et al. [57]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **Cu-MOF配位驱动吸附机理**: 189.3
  - 条件: {'pollutant': 'Cr(VI) (HCrO₄⁻形式)', 'material': '{[Cu(L)₀.₅(bpe)(H₂O)]NO₃·0.5H₂O}ₙ', 'optimal_ph': 6, 'mechanism': '离子交换(HCrO₄⁻与NO₃⁻交换)+配位取代(HCrO₄⁻取代配位水分子与金属配位)', 'thermodynamics': 'Ion exchange: ΔG₁=-4.184 kJ·mol⁻¹; Coordination: ΔG₂=-17.1544 kJ·mol⁻¹; Total: ΔG=-21.3384 kJ·mol⁻¹', 'interference': 'CO₃²⁻存在时吸附去除率下降23%', 'desorption_condition': '100°C和1 g·L⁻¹ KNO₃溶液(苛刻条件)', 'reference': 'Shao et al. [57]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **Cu-MOF配位驱动吸附机理**: 189.3
  - 条件: {'pollutant': 'Cr(VI) (HCrO₄⁻形式)', 'material': '{[Cu(L)₀.₅(bpe)(H₂O)]NO₃·0.5H₂O}ₙ', 'optimal_ph': 6, 'mechanism': '离子交换(HCrO₄⁻与NO₃⁻交换)+配位取代(HCrO₄⁻取代配位水分子与金属配位)', 'thermodynamics': 'Ion exchange: ΔG₁=-4.184 kJ·mol⁻¹; Coordination: ΔG₂=-17.1544 kJ·mol⁻¹; Total: ΔG=-21.3384 kJ·mol⁻¹', 'interference': 'CO₃²⁻存在时吸附去除率下降23%', 'desorption_condition': '100°C和1 g·L⁻¹ KNO₃溶液(苛刻条件)', 'reference': 'Shao et al. [57]'}
  - 来源: literature: 10.11862/CJIC.2021.068
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

- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-首次吸附量**: 70.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第1次'}
- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-20次循环后吸附量**: 61.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第20次', '衰减': '12.5%'}
- **未重氮化壳聚糖-MOF泡沫-循环吸附二氯甲烷-性能衰减**: 前8次循环吸附量迅速下降 None
  - 条件: {'pollutant': '二氯甲烷', 'material': '未重氮化壳聚糖-ZIF-8泡沫', '原因': '骨架结构塌陷，MOF颗粒脱落或团聚'}
- **酸性条件吸附优势原理 Why acidic pH favors Cr(VI) adsorption**: 酸性条件下吸附剂表面易被H⁺质子化带正电，对带负电的HCrO₄⁻或Cr₂O₇²⁻亲和性高；碱性条件下OH⁻与CrO₄²⁻竞争吸附 None
  - 条件: {'acidic_forms': 'HCrO₄⁻ (低浓度), Cr₂O₇²⁻ (高浓度)', 'alkaline_form': 'CrO₄²⁻', 'implication': '文献中关于Cr(VI)吸附的研究主要是对HCrO₄⁻和Cr₂O₇²⁻的去除，对CrO₄²⁻去除研究较少'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **TMU-30对Cr(VI)宽pH吸附性能**: 95%去除(<10 min); qm=2.86 mol·mol⁻¹ None
  - 条件: {'pollutant': 'Cr(VI)', 'material': 'TMU-30 (Pb²⁼为中心, 1D菱形孔道0.71nm×0.68nm)', 'ph_range': 'pH=2-9均可快速高效吸附所有形态Cr(VI)', 'ph>9': '晶体结构开始变化', 'mechanism': '异烟酸N-氧化物(INO)基团的N原子与Cr(VI)的O原子之间静电相互作用', 'selectivity': '不能选择性区分CrO₄²⁻/MoO₄²⁻/WO₄²⁻', 'limitation': 'Pb²⁼为高毒性重金属，难以实际应用', 'reference': 'Aboutorabi et al. [47]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **ZIF-67/BC/CH气凝胶对Cr(VI)吸附及再生**: pH=6时最大吸附; 5次循环后保持72% None
  - 条件: {'pollutant': 'Cr(VI) and Cu(II)', 'material': 'ZIF-67/BC/CH (ZIF-67原位生长在细菌纤维素/壳聚糖复合气凝胶上)', 'optimal_ph': 6, 'regeneration': 'NaOH溶液(1 mol·L⁻¹)洗脱Cr(VI)', 'cycle_performance': '5次循环后对Cr(VI)去除效率保持初始值72%, Cu(II)保持81%', 'real_water_effect': '自来水或河水中吸附能力比去离子水下降(Ca²⁼/Mg²⁼等竞争吸附)', 'reference': 'Li et al. [61]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **nFe₃O₄@MIL-88A(Fe)/APTMS对Cr(VI)吸附及再生**: 5次循环后去除率仅下降3% %
  - 条件: {'pollutant': 'Cr(VI), Cd(II), Pb(II)', 'material': 'nFe₃O₄@MIL-88A(Fe)/APTMS (微波辅助后合成改性, 3-氨基丙基三甲氧基硅烷功能化)', 'ph_condition': 'pH<4时带正电荷,与Cr(VI)阴离子静电引力', 'selectivity': '对Cr(VI)有较高去除效率和选择性', 'regeneration': '连续5次循环后去除率仅下降3%', 'reference': 'Mahmoud et al. [81]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **PVDF/PAN/壳聚糖/UiO-66-NH₂纳米纤维膜长期稳定性**: 18小时超长去除时间; 稳定膜通量 h
  - 条件: {'material': 'PVDF/PAN/壳聚糖/UiO-66-NH₂纳米纤维膜(静电纺丝)', 'optimal_thickness': '50 μm', 'optimal_mof_content': '10%', 'performance': '超长去除时间(18h)和稳定的膜通量', 'application': '吸附+膜过滤双重去除', 'reference': 'Jamshidifard et al. [60]'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **BUT-39对Cr₂O₇²⁻吸附性能及再生问题**: 215 mg·g⁻¹
  - 条件: {'pollutant': 'Cr₂O₇²⁻', 'material': 'BUT-39 (Zr-MOF, T型配体含苯并咪唑基团)', 'mechanism': '咪唑N原子酸性质子化富集Cr₂O₇²⁻; Zr₆簇与Cr₂O₇²⁻之间氢键、配位键等强相互作用', 'regeneration_issue': '循环再生性较差(强相互作用导致难解吸)', 'note': '高吸附量但再生性差是trade-off'}
  - 来源: literature: 10.11862/CJIC.2021.068
- **MOF材料水稳定性提升策略**: 高价金属-含氧配体(Zr羧酸盐/Zr酚盐/Cr羧酸盐/Fe羧酸盐); pKa大的唑类配体(Zn咪唑盐/Ni吡唑盐); 提升疏水性 None
  - 条件: {'stable_types': ['锆羧酸盐/锆酚盐', '铬羧酸盐/铁羧酸盐', '锌咪唑盐/镍吡唑盐'], 'hydrophobicity_tradeoff': '提升疏水性有利于水稳定性但可能影响对水中重金属离子的吸附亲和力', 'key_factor': '提升MOF结构中金属配体间的配位键强度'}
  - 来源: literature: 10.11862/CJIC.2021.068

## 来源汇总

- literature: 10.1007/s11356-022-19829-0
- literature: 10.1016/j.aca.2022.339632
- literature: 10.1016/j.carbpol.2022.119153
- literature: 10.1016/j.ccr.2020.213554
- literature: 10.1016/j.ccr.2021.213970
- literature: 10.1016/j.cej.2024.149414
- literature: 10.1016/j.cej.2024.152932
- literature: 10.1016/j.ecoenv.2020.111577
- literature: 10.1016/j.ijbiomac.2021.04.158
- literature: 10.1016/j.ijbiomac.2022.09.148
- literature: 10.1016/j.jcis.2023.01.075
- literature: 10.1016/j.jece.2022.107394
- literature: 10.1016/j.jhazmat.2020.123655
- literature: 10.1016/j.jiec.2021.09.029
- literature: 10.1016/j.seppur.2023.123175
- literature: 10.1016/j.seppur.2023.124984
- literature: 10.1021/acs.est.1c01723
- literature: 10.11862/CJIC.2021.068
- literature: 10.11868/j.issn.1001-4381.2020.000559
- literature: 10.11896/cldb.19100039
- literature: 10.13957/j.cnki.tcxb.2023.04.004
- literature: 10.16085/j.issn.1000-6613-2021-1614
- literature: 10.16085/j.issn.1000-6613.2021-1614
- literature: 10.3390/molecules29184317
- patent: CN121130847A
