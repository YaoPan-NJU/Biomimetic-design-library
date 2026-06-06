# fish-scale-hydroxyapatite

## 元数据

- **原型 ID**: fish-scale-hydroxyapatite
- **知识条目数**: 258
- **性能数据数**: 20
- **机制描述数**: 4
- **工程约束数**: 28

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
| 鱼鳞羟基磷灰石对酸性品红最大吸附容量（最优） | 478 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 盐酸浓度对吸附容量的影响-0.1mol/L | 478 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 盐酸浓度对吸附容量的影响-0.5mol/L | 386 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 盐酸浓度对吸附容量的影响-1mol/L | 356 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 第一步NaOH处理温度对吸附容量的影响-50°C | 423 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 第一步NaOH处理温度对吸附容量的影响-70°C（最优） | 478 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 第一步NaOH处理温度对吸附容量的影响-100°C | 450 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 干燥方式对吸附容量的影响-冷冻干燥 | 478 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 干燥方式对吸附容量的影响-热风烘干 | 430 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 干燥方式对吸附容量的影响-自然风干 | 462 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 吸附容量最低值 | 356 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent: CN114849640A |
| 实施例1酸性品红吸附容量(最优条件) Adsorption capacity of acid fuchsine (Example 1, optimal) | 478 | mg/g | 酸性品红 | 鱼鳞提取羟基磷灰石 | patent |
| 实施例2酸性品红吸附容量(HCl 0.5mol/L) Adsorption capacity (Example 2, HCl 0.5mol/L) | 386 | mg/g | 酸性品红 |  | patent |
| 实施例3酸性品红吸附容量(HCl 1mol/L) Adsorption capacity (Example 3, HCl 1mol/L) | 356 | mg/g | 酸性品红 |  | patent |
| 实施例4酸性品红吸附容量(NaOH 50°C) Adsorption capacity (Example 4, NaOH 50°C) | 423 | mg/g | 酸性品红 |  | patent |
| 实施例5酸性品红吸附容量(NaOH 100°C) Adsorption capacity (Example 5, NaOH 100°C) | 450 | mg/g | 酸性品红 |  | patent |
| 实施例6酸性品红吸附容量(烘干) Adsorption capacity (Example 6, oven drying) | 430 | mg/g | 酸性品红 |  | patent |
| 实施例7酸性品红吸附容量(风干) Adsorption capacity (Example 7, air drying) | 462 | mg/g | 酸性品红 |  | patent |
| 静态吸附Langmuir qmax | 1013.96 | mg/g | Ciprofloxacin (CIP) | DPBC | literature: 10.1016/j.chemosphere.2021.131962 |
| 固定床动态吸附容量 | 880.53 | mg/g |  | DPBC | literature: 10.1016/j.chemosphere.2021.131962 |

## 吸附机制

- **荷叶超疏水仿生机制 Lotus leaf superhydrophobic biomimetic mechanism**: 荷叶表面具有微米级沟槽和纳米级蜡管层级结构，低滚动角使水滴滚动并带走灰尘，实现自清洁效应
  - 条件: {'biological_source': 'lotus leaf', 'mechanism': 'hierarchical roughness + wax layer', 'property': 'superhydrophobicity, self-cleaning'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **鱼鳞水下超疏油仿生机制 Fish scale underwater superoleophobic mechanism**: 鱼鳞表面的黏液层通过蛋白质吸水形成，能排斥有机物质包括油污；鱼鳞还具有微乳突结构增加粗糙度
  - 条件: {'biological_source': 'fish scale', 'mechanism': 'mucus layer water absorption + micropapillae roughness', 'property': 'underwater superoleophobicity, self-cleaning'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **沙漠甲虫Janus双面润湿仿生机制 Namib beetle Janus biomimetic mechanism**: 沙漠甲虫背部具有亲水侧（从雾中收集水分）和疏水侧（将水分导向嘴部）的双面异质结构
  - 条件: {'biological_source': 'Namib beetle', 'mechanism': 'hydrophilic bump + hydrophobic groove dual-surface', 'property': 'Janus wettability'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **八重协同吸附机制**: 疏水+π-π+π-π EDA+阳离子交换+氢键+孔填充+静电+阳阳-π
  - 条件: {'hydrophobic': 'CIP aromatic ring + DPBC graphene structure; CIP最低溶解度在pH 7→最大吸附在pH 5-8一致', 'pi_pi': 'CIP aromatic ring + DPBC graphene structure stacking', 'pi_pi_EDA': 'F on CIP as π-acceptor, -OH on DPBC as π-donor', 'cation_exchange': 'protonated CIP amino groups exchange with H⁺ of surface acidic groups; H⁺ released (pH decreased during adsorption at pH<pKa1)', 'hydrogen_bonding': 'CIP phenolic acid proton ↔ DPBC carbonyl/carboxylate oxygen', 'pore_filling': 'micropores matching CIP molecule size → high-energy physical adsorption centers', 'electrostatic': 'pH-dependent; important but not dominant', 'cation_pi': 'protonated CIP amino groups ↔ DPBC π-electron-rich structure', 'dominant': 'hydrophobic interaction predominates (ΔG 0 to -20 kJ/mol → physisorption)', 'ref': '[Page 7-8; 3.8节; Fig 7]'}
  - 来源: literature: 10.1016/j.chemosphere.2021.131962

## 工程约束

- **NaOH处理温度对吸附性能的影响 Effect of NaOH treatment temperature on adsorption**: 50°C: 423mg/g < 70°C: 478mg/g > 100°C: 450mg/g None
  - 条件: {'optimal_temp': '70°C', 'trend': '50°C→70°C提升，70°C→100°C略有下降'}
- **全疏膜(Superamphiphobic)：激光蚀刻+PTFE/FS-61喷涂**: 激光蚀刻→金属基材→微纳结构→增大氟碳涂层表面积→提高机械稳定性。PTFE/FS-61喷涂→全疏表面→耐酸碱→即使表面物理损伤后仍保持低表面能液体排斥。可降解全疏膜：PCL-b-PTFOA纳米纤维→37°C/pH 7.0→米曲霉酶降解→PCL降解但PTFOA不溶→表面粗糙度和氟含量随降解时间增加→生物降解+全疏 None
  - 条件: {'laser_etching': '金属基材→微纳结构→增大涂层表面积→提高机械稳定', 'PTFE_FS61': '喷涂→全疏→耐酸碱→损伤后仍排斥低表面能液体', 'biodegradable': 'PCL-b-PTFOA→37°C/pH7→米曲霉酶降解→PCL降解→PTFOA保留→粗糙度↑+F含量↑', 'advantage': '可降解+全疏→环保可持续'}
  - 来源: literature: 10.1007/s10853-022-07945-8
- **智能响应膜：光/pH/温度/等离子体可切换润湿性**: 1）光响应：TiO₂光催化→UV照射→亲水+光降解有机物→MB可被完全降解。TiO₂@PVDF/PAN核壳→避免TiO₂团聚→UV 1h→分解87%罗丹明B。2）pH响应：PVDF-g-PAA树状纤维→中性水中超亲水+水下疏油→pH 2.0中疏水+超亲油；SNP/DA-TiO₂/PI膜→pH≥12时从超疏水变为超亲水。3）可逆切换：Cu网+Au+疏水分子→O₂等离子体→超亲水/水下超疏油→加热→恢复→可逆双向分离 None
  - 条件: {'photoresponsive': 'TiO₂→UV→亲水+光降解→MB完全降解', 'TiO2_PVDF_PAN': '核壳→UV 1h→分解87%罗丹明B', 'pH_responsive_PVDF_PAA': '中性→超亲水+水下疏油；pH2→疏水+超亲油', 'pH_responsive_SNP_DA_TiO2_PI': 'pH≥12→从超疏水变超亲水', 'reversible_Cu_mesh': 'O₂等离子体→超亲水/水下超疏油→加热→恢复→可逆', 'advantage': '灵活性→适应不同应用场景'}
  - 来源: literature: 10.1007/s10853-022-07945-8
- **仿生PVDF-SiO₂多尺度粗糙度→耐循环超疏水**: PVDF+SiO₂→电纺→多尺度粗糙结构→防止水滴进入→优异多循环性能+稳定超疏水性。克服小孔径膜处理高粘油的挑战→多尺度结构使高粘油仍可通过 None
  - 条件: {'material': 'PVDF+SiO₂纳米纤维', 'method': '电纺法', 'structure': '多尺度粗糙结构', 'performance': '稳定超疏水+多循环性能', 'challenge_solved': '高粘油通过小孔径→多尺度结构辅助'}
  - 来源: literature: 10.1007/s10853-022-07945-8
- **全亲膜(Superamphiphilic)：GPTE-ODA自修复+TCG光催化**: 1）GPTE-ODA涂覆织物→全亲(水和油CA均0°)→表面张力18.4-50.8 mN/m→<1s完全扩散→水预湿后油仍可在<1min扩散进入→自修复水下超亲油性。2）TiO₂/Co₃O₄/GO(TCG)涂覆不锈钢网→全亲(空气)→水下超疏油(OCA>150°)→光催化活性→有机污染物原位降解→一步乳液分离+高效水回收 None
  - 条件: {'GPTE_ODA': '全亲→水油CA均0°→<1s扩散→自修复', 'surface_tension_range': '18.4-50.8 mN/m', 'TCG': 'TiO₂/Co₃O₄/GO→全亲+水下超疏油+光催化→一步分离+降解', 'advantage': '双向分离+自修复+光催化'}
  - 来源: literature: 10.1007/s10853-022-07945-8
- **MOF水稳定性关键因素**: Higher ligand basicity → greater metal-ligand bond strength → better stability; 6-coordinate (octahedral) > 4-coordinate (tetrahedral); higher oxidation state → higher stability None
  - 条件: {'vulnerable': 'Zn-based MOFs (IRMOF-1) most moisture-sensitive due to soft metal-oxygen coordination bonds vulnerable to hydrolysis', 'stable_examples': 'Pyrazole (pKa 19.8) and imidazole (pKa 18.6) ligands exhibit higher chemical resistance to water than carboxylate-based MOFs', 'MOF_count': 'Tens of thousands of MOFs developed, but only ~100 demonstrated as porous and hydrophobic', 'limitation': 'MOF-incorporated membranes only used for DCMD and VMD; limited works on MOF-nanofiber for MD due to hydrothermal instability'}
  - 来源: literature: 10.3390/membranes13080727
- **荷叶超疏水仿生机制 Lotus leaf superhydrophobic biomimetic mechanism**: 荷叶表面具有微米级沟槽和纳米级蜡管层级结构，低滚动角使水滴滚动并带走灰尘，实现自清洁效应 None
  - 条件: {'biological_source': 'lotus leaf', 'mechanism': 'hierarchical roughness + wax layer', 'property': 'superhydrophobicity, self-cleaning'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **鱼鳞水下超疏油仿生机制 Fish scale underwater superoleophobic mechanism**: 鱼鳞表面的黏液层通过蛋白质吸水形成，能排斥有机物质包括油污；鱼鳞还具有微乳突结构增加粗糙度 None
  - 条件: {'biological_source': 'fish scale', 'mechanism': 'mucus layer water absorption + micropapillae roughness', 'property': 'underwater superoleophobicity, self-cleaning'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **超疏水膜适用体系 Superhydrophobic membrane application**: 超疏水膜适用于水包油(water-in-oil)体系，油渗透膜而水被排斥 None
  - 条件: {'membrane_type': 'superhydrophobic', 'system': 'water-in-oil emulsion/mixture', 'mechanism': 'oil penetrates, water repelled'}
  - 来源: literature: 10.1007/s11783-021-1515-2
- **超疏油膜适用体系 Superoleophobic membrane application**: 超疏油膜适用于油包水(oil-in-water)体系，水渗透膜而油被排斥 None
  - 条件: {'membrane_type': 'superoleophobic', 'system': 'oil-in-water emulsion/mixture', 'mechanism': 'water passes, oil repelled'}
  - 来源: literature: 10.1007/s11783-021-1515-2

## 来源汇总

- literature: 10.1002/smll.202204624
- literature: 10.1007/s10853-022-07945-8
- literature: 10.1007/s11783-021-1515-2
- literature: 10.1016/j.chemosphere.2021.131962
- literature: 10.1021/acsami.0c18794
- literature: 10.3390/membranes13080727
- literature: 10.34133/2022/9895418
- patent
- patent: CN114849640A
- 鱼鳞(草鱼)
