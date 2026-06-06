# chitosan

## 元数据

- **原型 ID**: chitosan
- **知识条目数**: 1043
- **性能数据数**: 126
- **机制描述数**: 58
- **工程约束数**: 112

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
| SA-CCS-LS@Fe3O4-1.5对中性红脱除率 NR removal by SA-CCS-LS@Fe3O4-1.5 | 95%以上 | % |  |  | patent: CN117654453A |
| SA-CCS-LS@Fe3O4-1.5-0.6对三种伯氨基染料脱除率 removal rates of optimized adsorbent | 中性红98.82%，刚果红97.54%，活性黑-5 95.77% | % |  |  | patent: CN117654453A |
| 脱除率计算公式 removal rate formula | Re% = (C0 - Ce) / C0 × 100% | % |  |  | patent: CN117654453A |
| pH对Sb去除率的影响 Effect of pH on Sb removal | pH 1-7范围内Sb去除率均>80%，最高93.12%(pH=1)；pH=9时降至46.56% | % | Sb(锑) | 磁改性羧甲基壳聚糖复配絮凝剂(C-FeS) | patent |
| pH对Cr去除率的影响 Effect of pH on Cr removal | pH 1-9范围内C-FeS对Cr去除始终>85%；PFS也>85%；PAC<22%(pH=9) | % | Cr(铬) | 磁改性羧甲基壳聚糖复配絮凝剂(C-FeS) | patent |
| 反应时间对Sb去除的影响(实施例1, pH=5) Effect of reaction time on Sb removal (Example 1, pH=5) | 5min: 82.5%；10min: 92.85%(最大) | % | Sb(锑) |  | patent |
| 反应时间对Cr去除的影响(实施例1, pH=5) Effect of reaction time on Cr removal (Example 1, pH=5) | 5min: 75%；10min: 81% | % | Cr(铬) |  | patent |
| 5min内去除率>80%的工程意义 Engineering significance of >80% removal in 5min | 较低投加量(0.5-1.5g/L)下，5min内可将废水中重金属含量降低80%以上，10min内去除率提高至90%以上 | % |  |  | patent |
| 对比例与实施例的Sb去除时间对比(图5) Sb removal time comparison (Figure 5) | 只有实施例1(C-FeS)可在5min内达81.5%+；对比例1-5(壳聚糖基/其他絮凝剂)反应时间显著增加 | None |  |  | patent |

## 吸附机制

- **吸附机制-π-π相互作用**: 偶氮基团带有π电子，可与油分子产生π-π相互作用，协同增加有机污染物捕获量
  - 条件: {'材料': '重氮化改性泡沫', '污染物': '有机溶剂/油类'}
- **吸附机制分析 adsorption mechanism**: LS和CCS与环氧氯丙烷交联修饰氨基；SA和CCS的羧酸盐基团与Ca²⁺交联；CCS的氨基/羧基和PEI的亚胺基提供吸附位点；LS的磺酸基增强配位
  - 条件: {'交联机制': '环氧氯丙烷交联LS/CCS/SA的氨基', '凝胶化': 'Ca²⁺与羧酸盐基团（SA/CCS/LS）交联形成蛋盒结构', '吸附位点': 'CCS的氨基+羧基、PEI的亚胺基、LS的磺酸基', '选择性来源': '伯氨基染料与吸附剂的特异性作用'}
- **蛋盒结构交联机制 egg-box crosslinking mechanism**: 海藻酸钠通过G单元羧基与Ca²⁺配位形成'蛋盒'结构三维网络凝胶
  - 条件: {'来源': '海洋褐藻细胞壁天然交联机制', '关键基团': '海藻酸钠G单元上的羧酸盐基团(COO⁻)', '交联离子': 'Ca²⁺', '结构': '三维网络水凝胶', '证据': 'FTIR中羧酸盐峰从1421cm⁻¹迁移至1409cm⁻¹，567cm⁻¹出现Ca²⁺交联峰'}
- **PDA吸附机制-姜黄素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + 形成羰基键', 'description': 'PDA与姜黄素分子产生物理吸附（π-π*电子跃迁）和化学吸附（羰基键）'}
- **PDA吸附机制-番茄红素**: None
  - 条件: {'mechanism': 'π-π*电子跃迁 + michael加成反应', 'description': 'PDA与番茄红素分子产生物理吸附（π-π*电子跃迁）和化学吸附（michael加成反应）'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **Fe3+改性活性炭吸附磺胺类抗生素的机制 Mechanism of Fe3+-modified activated carbon adsorbing sulfonamide antibiotics**: 以化学吸附为主
  - 条件: {'pollutant': '磺胺类抗生素', 'adsorption_type': '化学吸附为主', 'contributing_factors': '比表面积增大、含氧官能团增多'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **Fe3+改性活性炭吸附磺胺类抗生素的机制 Mechanism of Fe3+-modified activated carbon adsorbing sulfonamide antibiotics**: 以化学吸附为主
  - 条件: {'pollutant': '磺胺类抗生素', 'adsorption_type': '化学吸附为主', 'contributing_factors': '比表面积增大、含氧官能团增多'}
- **酸浸碳/壳聚糖/FeCl3吸附机制 Acid-leached carbon/chitosan/FeCl3 mechanisms**: 41.9 mg/g (Langmuir); 机制: H键、FeCl3引入Cl-与NO3-离子交换、酸性介质中质子化羟基/氨基/Fe静电作用
  - 条件: {'material': 'granular adsorbent composed of acid-leached carbon waste, chitosan, and FeCl3'}
  - 来源: literature: 10.1016/j.carbpol.2021.118625

## 工程约束

- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-首次吸附量**: 70.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第1次'}
- **重氮化处理壳聚糖-MOF泡沫-循环吸附二氯甲烷-20次循环后吸附量**: 61.7 g/g
  - 条件: {'pollutant': '二氯甲烷', 'material': '重氮化壳聚糖-ZIF-8泡沫', '循环次数': '第20次', '衰减': '12.5%'}
- **未重氮化壳聚糖-MOF泡沫-循环吸附二氯甲烷-性能衰减**: 前8次循环吸附量迅速下降 None
  - 条件: {'pollutant': '二氯甲烷', 'material': '未重氮化壳聚糖-ZIF-8泡沫', '原因': '骨架结构塌陷，MOF颗粒脱落或团聚'}
- **循环再生性能 cycling stability**: 5次循环后中性红相对脱除率98.82%，刚果红98.19% %
  - 条件: {'吸附剂': 'SA-CCS-LS@Fe3O4-1.5-0.6', '解吸剂': '0.1M NaOH', '循环次数': '5次', '后处理': '解吸后冻干72h', '基准': '第一次使用脱除率为100%'}
- **番茄红素光稳定性提升**: 97.98 %
  - 条件: {'material': 'HPDA@LYC（纳米包埋后）', 'control': '番茄红素粉末（未包埋）', 'light_condition': '室内散射光全光照射', 'duration': '12h', 'temperature': '25°C', 'control_retention': '83.75%', 'improvement': '从83.75%提升至97.98%'}
- **PDA的pH敏感性机制**: None None
  - 条件: {'mechanism': '聚多巴胺在肿瘤微酸性环境中可解聚', 'application': '响应肿瘤部位pH值，提高肿瘤胞内有效脂溶性色素浓度'}
- **pH对Sb去除率的影响 Effect of pH on Sb removal**: pH 1-7范围内Sb去除率均>80%，最高93.12%(pH=1)；pH=9时降至46.56% %
  - 条件: {'pollutant': 'Sb(锑)', 'material': '磁改性羧甲基壳聚糖复配絮凝剂(C-FeS)', 'initial_concentration': '200 μg/L', 'dosage': '0.1g/100mL(1g/L)', 'contact_time': '30 min', 'ph_range_optimal': '1-7', 'comparison_PAC': '始终<34.92%', 'comparison_PFS': '最高52.38%(pH=7)'}
- **pH对Cr去除率的影响 Effect of pH on Cr removal**: pH 1-9范围内C-FeS对Cr去除始终>85%；PFS也>85%；PAC<22%(pH=9) %
  - 条件: {'pollutant': 'Cr(铬)', 'material': '磁改性羧甲基壳聚糖复配絮凝剂(C-FeS)', 'initial_concentration': '10 mg/L', 'dosage': '0.1g/100mL(1g/L)', 'contact_time': '30 min', 'ph_range': '1-9'}
- **反应时间对Sb去除的影响(实施例1, pH=5) Effect of reaction time on Sb removal (Example 1, pH=5)**: 5min: 82.5%；10min: 92.85%(最大) %
  - 条件: {'pollutant': 'Sb(锑)', 'initial_concentration': '200 μg/L', 'pH': 5, 'dosage': '0.1g/100mL', 'comparison': 'PAC和PFS在5min时去除率远低于C-FeS'}
- **反应时间对Cr去除的影响(实施例1, pH=5) Effect of reaction time on Cr removal (Example 1, pH=5)**: 5min: 75%；10min: 81% %
  - 条件: {'pollutant': 'Cr(铬)', 'initial_concentration': '10 mg/L', 'pH': 5, 'dosage': '0.1g/100mL', 'comparison': 'PFS在5min时为55%'}

## 来源汇总

- literature: 10.1007/s10311-023-01563-9
- literature: 10.1007/s10924-021-02312-1
- literature: 10.1007/s11771-021-4724-8
- literature: 10.1007/s13762-021-03603-9
- literature: 10.1016/j.carbpol.2020.117000
- literature: 10.1016/j.carbpol.2021.118604
- literature: 10.1016/j.carbpol.2021.118625
- literature: 10.1016/j.carbpol.2021.118671
- literature: 10.1016/j.carbpol.2022.119153
- literature: 10.1016/j.cej.2022.138934
- literature: 10.1016/j.cej.2024.149414
- literature: 10.1016/j.chemosphere.2020.129273
- literature: 10.1016/j.chemosphere.2021.130927
- literature: 10.1016/j.cjche.2020.07.066
- literature: 10.1016/j.ijbiomac.2021.04.158
- literature: 10.1016/j.ijbiomac.2021.08.047
- literature: 10.1016/j.ijbiomac.2021.10.050
- literature: 10.1016/j.jece.2022.108048
- literature: 10.1016/j.matlet.2022.131670
- literature: 10.1016/j.molliq.2020.114523
- literature: 10.1016/j.rechem.2024.101332
- literature: 10.1016/j.scitotenv.2021.150606
- literature: 10.1016/j.seta.2020.100951
- literature: 10.1039/d2ma00320a
- literature: 10.1039/d2ra07112f
- literature: 10.13550/j.jxhg.20210304
- literature: 10.13671/j.hjkxxb.2020.0407
- literature: 10.13801/j.cnki.fhclxb.20211105.003
- literature: 10.13822/j.cnki.hxsj.2022008755
- literature: 10.14028/j.cnki.1003-3726.2021.02.007
- literature: 10.15898/j.ykcs.202208230155
- literature: 10.16865/j.cnki.1000-7555.2021.0165
- literature: 10.19817/j.cnki.issn1006-3536.2022.12.044
- literature: 10.19965/j.cnki.iwt.2022-1185
- literature: 10.3390/molecules26030594
- literature: 10.3390/molecules29184317
- literature: 10.3969/j.issn.0253-6099.2021.03.034
- literature: 10.3969/j.issn.1001-9731.2022.10.023
- patent
- patent: CN115040496A
- patent: CN117654453A
- patent: CN119488883A
- patent: CN121130847A
