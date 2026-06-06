# alginate

## 元数据

- **原型 ID**: alginate
- **知识条目数**: 284
- **性能数据数**: 50
- **机制描述数**: 12
- **工程约束数**: 26

## 仿生元数据

- **organism_scientific**: Phaeophyceae
- **biomimetic_dimension**: 结构仿生
- **features**: ['蛋盒结构交联', '三维网状多孔结构', '丰富含氧官能团(-COOH, -OH)', 'pH敏感性', '高保水性', '生物相容性']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '机械性能与成胶稳定性', 'relevance': 'high', 'explanation': '文献指出SA水凝胶在实际应用中需解决机械性能不足和成胶稳定性问题，以维持结构完整性'}, {'constraint': '重复利用与回收', 'relevance': 'high', 'explanation': '文献强调需解决水凝胶吸附后的重复利用和回收问题，以降低工程应用成本并避免二次污染'}, {'constraint': '吸附性能进一步提升', 'relevance': 'medium', 'explanation': '尽管部分复合水凝胶吸附量极高，但文献仍将吸附性能的进一步提升列为未来研究方向'}]

## 仿生叙事

### problem_definition

自然界中褐藻需在海洋动态环境中维持结构稳定并高效富集离子；水处理领域亟需高效、低成本、可再生且环保的吸附材料以去除重金属和染料等复杂污染物。

### biological_solution

褐藻进化出富含G单元和M单元的海藻酸钠天然阴离子多糖，利用G单元上的羧基与二价阳离子（如Ca²⁺）发生离子置换，形成稳定的'蛋盒结构'(egg-box model)三维网络。这种天然交联机制和模拟细胞外基质的物理环境，赋予了材料优异的离子结合能力、高保水性和结构稳定性。

### key_features

必须保留特征：G单元与二价阳离子的'蛋盒结构'离子交联机制、骨架上丰富的含氧官能团（-COOH, -OH）；可灵活调整特征：复合无机纳米材料（如TiO₂、高岭土、凹凸棒土）或接枝有机聚合物（如PAA）以调控孔隙率、机械强度和特异性吸附位点。

### design_mapping

生物海藻酸钠多糖映射为SA基复合水凝胶材料；天然'蛋盒'离子交联映射为Ca²⁺等交联剂构建的水凝胶网络节点；细胞外基质三维环境映射为高保水、多孔的水凝胶传质骨架。软约束建议：可通过引入无机粘土或纳米颗粒增强机械性能，利用接枝共聚（如SA-g-PAA）大幅增加官能团密度以提升吸附容量。

### explainability_anchors

仿生故事线：从海洋褐藻的抗逆流结构维持与离子富集机制，到'蛋盒结构'水凝胶的仿生设计，再到高效重金属/染料吸附材料的工程实现。设计溯源：SA的G单元-COOH与Ca²⁺的配位化学直接映射为水凝胶的交联节点，天然多糖的三维网络映射为污染物的传质与吸附通道，实现了从生物大分子组装到宏观水处理材料的跨尺度设计。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| SA-CCS-LS@Fe3O4-1.5对中性红脱除率 NR removal by SA-CCS-LS@Fe3O4-1.5 | 95%以上 | % |  |  | patent: CN117654453A |
| SA-CCS-LS@Fe3O4-1.5-0.6对三种伯氨基染料脱除率 removal rates of optimized adsorbent | 中性红98.82%，刚果红97.54%，活性黑-5 95.77% | % |  |  | patent: CN117654453A |
| 脱除率计算公式 removal rate formula | Re% = (C0 - Ce) / C0 × 100% | % |  |  | patent: CN117654453A |
| 吸附剂对吸附容量的影响 | 有吸附剂时吸油容量显著提升 | None |  |  | patent: CN119488883A |
| 凹凸棒土有机改性对去除率的影响 Effect of attapulgite organic modification on removal rate | 未对凹凸棒土改性时，复合材料对重金属离子去除率降低 | None |  |  | patent |
| 活性炭改性对去除率的影响 Effect of activated carbon modification on removal rate | 未对活性炭改性时，复合材料对磺胺类抗生素去除率降低 | None |  |  | patent |
| SA-CCS-LS@Fe3O4-1.5对中性红脱除率 Removal rate of neutral red by SA-CCS-LS@Fe3O4-1.5 | >95% | % | 中性红(neutral red, 522nm) | SA-CCS-LS@Fe3O4-1.5 | patent |
| SA-CCS-LS@Fe3O4-1.5-0.6对中性红脱除率(最优) Removal rate of neutral red by optimal adsorbent | 98.82 | % | 中性红(neutral red, 522nm) | SA-CCS-LS@Fe3O4-1.5-0.6(最优配方) | patent |
| SA-CCS-LS@Fe3O4-1.5-0.6对刚果红脱除率 Removal rate of Congo red by optimal adsorbent | 97.54 | % | 刚果红(Congo red, 498nm) | SA-CCS-LS@Fe3O4-1.5-0.6 | patent |
| SA-CCS-LS@Fe3O4-1.5-0.6对活性黑-5脱除率 Removal rate of reactive black-5 by optimal adsorbent | 95.77 | % | 活性黑-5(reactive black-5, 600nm) | SA-CCS-LS@Fe3O4-1.5-0.6 | patent |
| 脱除率计算公式 Removal rate calculation formula | Re% = (C0-Ce)/C0 × 100% | None |  |  | patent |
| 凹凸棒土有机改性对去除率的影响 Effect of attapulgite organic modification on removal rate | 未对凹凸棒土改性时，复合材料对重金属离子去除率降低 | None |  |  | patent |
| 活性炭改性对去除率的影响 Effect of activated carbon modification on removal rate | 未对活性炭改性时，复合材料对磺胺类抗生素去除率降低 | None |  |  | patent |
| CA/KCB气凝胶对Pb²⁺的最大吸附容量 | 664.6 | mg/g | Pb(II) | CA/KCB composite aerogel (KMnO4-modified cotton stalk biochar + calcium alginate) | literature: 10.1016/j.ijbiomac.2025.140801 |
| GO/海藻酸水凝胶膜对Cr(III)和Pb(II)的吸附容量 | Cr(III): 118.6, Pb(II): 327.9 | mg/g |  | Graphene oxide/alginate hydrogel membranes (GAHMs) | literature: 10.1016/j.ijbiomac.2025.140801 |
| 壳聚糖/三聚氰胺/海藻酸气凝胶对Pb(II)的吸附容量 | 1331.6 | mg/g | Pb(II) | Alginate/melamine/chitosan aerogel | literature: 10.1016/j.ijbiomac.2025.140801 |
| ZIF-8/SC水凝胶对环丙沙星的吸附容量 | 2887 | mg/g | Ciprofloxacin (CIP) | ZIF-8/SC three-dimensional polysaccharide-based MOF hydrogel | literature: 10.1016/j.ijbiomac.2025.140801 |
| NiFe₂O₄@Ca-alginate对MB和Rh6G的吸附容量 | MB: 1243, Rh6G: 845 | mg/g |  | NiFe₂O₄@Ca-alginate anisotropic plate-like particles | literature: 10.1016/j.ijbiomac.2025.140801 |
| Alginate@PEI对Cr(VI)的吸附容量 | 431.6 | mg/g | Cr(VI) | Alginate@PEI core-shell/bead-like adsorbent | literature: 10.1016/j.ijbiomac.2025.140801 |
| SA/PEI-0.25蜂窝弹性气凝胶对Cr(VI)和Cd(II)的吸附容量 | Cr(VI): 678.67, Cd(II): 464.23 | mg/g |  | SA/PEI-0.25 three-dimensional honeycomb elastic amino-functionalized aerogels | literature: 10.1016/j.ijbiomac.2025.140801 |

## 吸附机制

- **吸附机制分析 adsorption mechanism**: LS和CCS与环氧氯丙烷交联修饰氨基；SA和CCS的羧酸盐基团与Ca²⁺交联；CCS的氨基/羧基和PEI的亚胺基提供吸附位点；LS的磺酸基增强配位
  - 条件: {'交联机制': '环氧氯丙烷交联LS/CCS/SA的氨基', '凝胶化': 'Ca²⁺与羧酸盐基团（SA/CCS/LS）交联形成蛋盒结构', '吸附位点': 'CCS的氨基+羧基、PEI的亚胺基、LS的磺酸基', '选择性来源': '伯氨基染料与吸附剂的特异性作用'}
- **蛋盒结构交联机制 egg-box crosslinking mechanism**: 海藻酸钠通过G单元羧基与Ca²⁺配位形成'蛋盒'结构三维网络凝胶
  - 条件: {'来源': '海洋褐藻细胞壁天然交联机制', '关键基团': '海藻酸钠G单元上的羧酸盐基团(COO⁻)', '交联离子': 'Ca²⁺', '结构': '三维网络水凝胶', '证据': 'FTIR中羧酸盐峰从1421cm⁻¹迁移至1409cm⁻¹，567cm⁻¹出现Ca²⁺交联峰'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **Fe3+改性活性炭吸附磺胺类抗生素的机制 Mechanism of Fe3+-modified activated carbon adsorbing sulfonamide antibiotics**: 以化学吸附为主
  - 条件: {'pollutant': '磺胺类抗生素', 'adsorption_type': '化学吸附为主', 'contributing_factors': '比表面积增大、含氧官能团增多'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **Fe3+改性活性炭吸附磺胺类抗生素的机制 Mechanism of Fe3+-modified activated carbon adsorbing sulfonamide antibiotics**: 以化学吸附为主
  - 条件: {'pollutant': '磺胺类抗生素', 'adsorption_type': '化学吸附为主', 'contributing_factors': '比表面积增大、含氧官能团增多'}
- **海藻酸钠水凝胶的吸附机制分类**: 物理吸附（范德华力+氢键）和化学吸附（共价键+离子交换+表面络合）
  - 条件: {'physical_adsorption': '多孔结构和亲水基团提供大比表面积，范德华力和氢键作用', 'chemical_adsorption': '带负电-COOH与阳离子/阳离子染料交换形成稳定配合物', 'covalent_bonding': '氨基与羧基脱水缩合形成酰胺键', 'characterization': 'XRD, FT-IR, zeta potential表征'}
  - 来源: literature: 10.1016/j.ijbiomac.2025.140801
- **吸附机制——化学吸附+静电作用**: 准二级动力学+Langmuir→化学吸附为主；-COO⁻与Pb²⁺静电吸引+配位；CNF增加负电荷→增强静电吸附
  - 条件: {'kinetics': 'pseudo-second-order → chemical adsorption', 'isotherm': 'Langmuir → monolayer', 'mechanism': 'electrostatic attraction + coordination', 'functional_groups': ['-COO⁻ (carboxylate)', '-OH (hydroxyl)'], 'CNF_enhancement': 'additional negative charges increase electrostatic attraction', 'ref': '[Page 1; abstract; Section 1]'}
  - 来源: literature: 10.1016/j.molliq.2020.115122
- **海藻酸盐的吸附机制类型**: 静电相互作用、离子交换、配位螯合、化学还原（Cr(VI)→Cr(III)）、光催化还原、氢键、范德华力
  - 条件: {'electrostatic': '质子化/去质子化调控表面电荷', 'ion_exchange': '重金属置换凝胶中的Ca²⁺（egg-box模型）', 'complexation': '与-COOH/-OH/-NH₂等官能团配位', 'reduction': 'Cr(VI)被还原为Cr(III)（PEI/海藻酸盐膜）', 'characterization': 'FTIR, SEM-EDX, XPS确认机制'}
  - 来源: literature: 10.5004/dwt.2022.28834
- **吸附机理——疏水亲油+毛细管力**: 疏水亲油性(硅烷改性)+气凝胶多孔结构的毛细管吸收力→协同选择性吸油
  - 条件: {'mechanism': 'hydrophobic-oleophilic nature + capillary absorption force of porous structure', 'process': 'oil droplets contact surface → absorbed and penetrate aerogel; water droplets stay on surface', 'synergy': 'physical adsorption (capillary) + surface chemistry (hydrophobic modification)', 'reference': '[Page 4; Section 2.5.10, Page 10; Section 3.5]'}
  - 来源: literature: 10.1016/j.jhazmat.2022.129965

## 工程约束

- **循环再生性能 cycling stability**: 5次循环后中性红相对脱除率98.82%，刚果红98.19% %
  - 条件: {'吸附剂': 'SA-CCS-LS@Fe3O4-1.5-0.6', '解吸剂': '0.1M NaOH', '循环次数': '5次', '后处理': '解吸后冻干72h', '基准': '第一次使用脱除率为100%'}
- **实施例3配方（循环测试对象）**: 纤维素纳米纤维2.0g+埃洛石1.5g+玻璃纤维0.25g+PEI-ECH 0.5g/100g水+MTMS疏水改性3min None
  - 条件: {'polymer': '纤维素纳米纤维 2.0g', 'adsorbent': '埃洛石 1.5g', 'reinforcement': '玻璃纤维 0.25g', 'crosslinker': '聚酰胺-环氧氯丙烷 0.5g（替代FeCl₃）', 'conditions': '50°C, 5000rpm搅拌≥2h', 'hydrophobic': '甲基三甲氧基硅烷(MTMS)乙醇溶液浸泡3min', 'special': '10次循环分离测试对象，力学性能优于对比例3', 'pollutants_tested': ['石油醚', '二氯乙烷', '二氯甲烷', '三氯甲烷', '甲基红', '甲苯', '四氯化碳'], 'claim_scope': '权利要求1', 'biomass_polymer': ['卡拉胶', '海藻酸钠', '羧甲基纤维素', '明胶', '纤维素纳米纤维', '魔芋葡甘聚糖', '羟乙基纤维素', '壳聚糖', '阿拉伯树胶', '结冷胶', '淀粉']}
- **海藻酸钙交联凹凸棒土-沸石微球制备 Calcium alginate crosslinked attapulgite-zeolite microsphere preparation**: 沸石粉15-20份 + 海藻酸钠溶液(1-2%, 1:10加入) + 有机改性凹凸棒土, 35-45°C搅拌1-2h, 滴加CaCl2(0.1-0.2mol/L), 继续搅拌8-10h None
  - 条件: {'zeolite': '预处理沸石粉 15-20份', 'sodium_alginate': '浓度1-2%，按1:10加入沸石粉中', 'attapulgite': '有机改性凹凸棒土', 'crosslinker': '氯化钙溶液 浓度0.1-0.2mol/L', 'temperature': '35-45°C水浴', 'mixing_time': '混合搅拌1-2h + 滴加CaCl2后继续搅拌8-10h'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性 None
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **循环使用性能 Cycling performance**: 洗脱后循环使用多次，饱和吸附量几乎不下降 None
  - 条件: {'regeneration': '洗脱后循环使用', 'stability': '多次循环后饱和吸附量几乎不下降'}
- **循环使用性能 Cycling stability**: 5次循环后中性红相对脱除率从100%降至98.82%，刚果红从100%降至98.19% %
  - 条件: {'material': 'SA-CCS-LS@Fe3O4-1.5-0.6', 'regeneration': '0.1M NaOH + 冻干72h', 'cycles': 5, 'neutral_red_retention': '98.82%', 'congo_red_retention': '98.19%'}
- **再生方法 Regeneration method**: 0.1M NaOH溶液解吸 + 冻干72h None
  - 条件: {'regeneration_solution': '0.1 M NaOH', 'post_treatment': '冻干72h', 'condition': '25°C, 120rpm'}
- **海藻酸钙交联凹凸棒土-沸石微球制备 Calcium alginate crosslinked attapulgite-zeolite microsphere preparation**: 沸石粉15-20份 + 海藻酸钠溶液(1-2%, 1:10加入) + 有机改性凹凸棒土, 35-45°C搅拌1-2h, 滴加CaCl2(0.1-0.2mol/L), 继续搅拌8-10h None
  - 条件: {'zeolite': '预处理沸石粉 15-20份', 'sodium_alginate': '浓度1-2%，按1:10加入沸石粉中', 'attapulgite': '有机改性凹凸棒土', 'crosslinker': '氯化钙溶液 浓度0.1-0.2mol/L', 'temperature': '35-45°C水浴', 'mixing_time': '混合搅拌1-2h + 滴加CaCl2后继续搅拌8-10h'}
- **海藻酸钙微球吸附重金属的机制 Heavy metal adsorption mechanism of calcium alginate microspheres**: 海藻酸钙中大量负电荷羧酸根离子能与Pb2+和Cd2+结合，生成藻酸重金属盐沉淀储存在囊腔内，与沸石活性点相互独立，削弱铅镉相互抑制性 None
  - 条件: {'pollutants': ['Pb2+', 'Cd2+'], 'mechanism': '羧酸根离子配位 + 沉淀储存', 'structural_advantage': '囊腔储存与沸石活性点独立，削弱竞争抑制'}
- **循环使用性能 Cycling performance**: 洗脱后循环使用多次，饱和吸附量几乎不下降 None
  - 条件: {'regeneration': '洗脱后循环使用', 'stability': '多次循环后饱和吸附量几乎不下降'}

## 来源汇总

- literature: 10.1007/s10924-021-02312-1
- literature: 10.1016/j.ijbiomac.2025.140801
- literature: 10.1016/j.jhazmat.2022.129965
- literature: 10.1016/j.molliq.2020.115122
- literature: 10.1039/d1ra09193j
- literature: 10.16454/j.cnki.issn.1001-0564.2022.04.014
- literature: 10.5004/dwt.2022.28834
- patent
- patent: CN117654453A
- patent: CN119488883A
