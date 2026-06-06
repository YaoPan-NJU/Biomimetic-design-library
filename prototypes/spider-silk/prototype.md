# spider-silk

## 元数据

- **原型 ID**: spider-silk
- **知识条目数**: 142
- **性能数据数**: 4
- **机制描述数**: 4
- **工程约束数**: 4

## 仿生元数据

- **organism_scientific**: Nepenthes alata, Namib desert beetle, Cactus, Spider silk
- **biomimetic_dimension**: 结构仿生
- **features**: ['SHB/SHL图案化表面', '锥形不对称结构+梯度沟槽', '周期性纺锤结/接头结构', 'SLIPS超滑表面', '润湿性梯度', 'Laplace压力差驱动', '低接触角滞后']
- **applicability**: {'pH_range': None, 'temp_range': None, 'salinity': None}
- **engineering_constraints**: [{'constraint': '多重仿生制备复杂度', 'relevance': 'high', 'explanation': '从单仿生到四仿生设计，制备工艺复杂度呈指数级增长，需权衡协同增效与制造可行性。'}, {'constraint': 'SLIPS润滑剂固定', 'relevance': 'high', 'explanation': '猪笼草仿生SLIPS表面需解决润滑剂流失问题，如通过PDMS刷接枝固定硅油以维持长期超滑性能。'}, {'constraint': '亲疏水比例与阵列几何优化', 'relevance': 'medium', 'explanation': '甲虫仿生中SHL与SHB面积比需精确控制（如1:3），且仙人掌仿生中刺尖端角（15°）与排列方式（交替优于对称）直接影响液滴滑动时间与收集效率。'}]

## 仿生叙事

### problem_definition

自然界挑战：干旱/半干旱地区生物面临极度缺水，需从稀薄雾气中高效获取水分；水处理对应：传统雾水收集装置受限于空气动力学效率低、液滴易滞留或二次蒸发，难以实现高效捕获、定向输运与快速脱离的协同。

### biological_solution

进化策略：多种生物独立进化出高效集水微纳结构；关键机制：利用表面能梯度、Laplace压力差、润湿性图案化及超滑表面降低接触角滞后，驱动液滴定向移动；成功案例：纳米布甲虫亲疏水图案、仙人掌锥形梯度沟槽、蜘蛛丝周期性纺锤结、猪笼草SLIPS表面协同作用，使集水率跨越数个数量级（最高达81,250 mg h⁻¹ cm⁻²）。

### key_features

必须保留特征：微纳分级粗糙度、润湿性梯度（亲/疏水或超滑）、非对称几何形态（锥形/纺锤结）；可灵活调整特征：基底材料（织物/金属网/泡沫）、图案比例（如SHL:SHB=1:3）、阵列排列方式（对称/交替）、润滑剂固定策略。

### design_mapping

生物→材料映射：甲虫亲疏水峰谷→静电纺丝/光刻/喷涂制备的SHB/SHL图案化织物；仙人掌锥形刺→3D打印/kirigami人工刺阵列；蜘蛛丝纺锤结→异质结构微纤维/交叉纤维网；猪笼草SLIPS→PDMS刷接枝多孔表面。软约束建议：优先采用低成本成熟工艺（如纺织工业兼容的Cu沉积，成本$1.5/m²），控制结构特征尺寸以匹配~10 μm雾滴边界层，优化亲疏水比例与阵列间距以最大化Laplace压差与毛细力协同。

### explainability_anchors

仿生故事线：从单一生物原型（仅解决捕获或输运单一环节）向多重仿生（捕获+输运+存储三阶段优化）演进，揭示自然界‘分工协同’的集水智慧；设计溯源：所有高效FHD均回归流体力学与界面科学基本原理（Laplace方程、Furmidge方程、Cassie-Baxter态），仿生结构仅为物理机制的空间载体，可通过定量参数（如15°尖端角、Ra粗糙度差、0.16s脱离时间）直接指导工程放大与性能预测。

## 性能数据

| 参数 | 值 | 单位 | 污染物 | 材料 | 来源 |
|------|-----|------|--------|------|------|
| Cd(II)去除性能 Cd(II) removal | 100%去除; 20min达EPA安全标准(5ppb); 起始浓度1000ppb | % | Cd(II) | CNF/PEI@GOA | literature: 10.1016/j.cej.2021.128670 |
| Cr(VI)去除性能 Cr(VI) removal | 100%去除; 20min达EPA安全标准(100ppb); 起始浓度1000ppb | % | Cr(VI) | CNF/PEI@GOA | literature: 10.1016/j.cej.2021.128670 |
| Cu(II)去除性能 Cu(II) removal | 100%去除; 30min达安全标准; 起始浓度1000ppb | % | Cu(II) | CNF/PEI@GOA | literature: 10.1016/j.cej.2021.128670 |
| Pb(II)去除性能 Pb(II) removal | 100%去除; 40min达EPA安全标准(0ppb); 起始浓度1000ppb | % | Pb(II) | CNF/PEI@GOA | literature: 10.1016/j.cej.2021.128670 |

## 吸附机制

- **抗污染机制 Antifouling mechanism**: 超亲水/水下超疏油→Cassie态→油滴不粘附→浮力上升→简单水冲洗恢复
  - 条件: {'wettability': 'superhydrophilic/underwater superoleophobic with micro/nano-hierarchical structures', 'cassie_state': 'underwater Cassie state → stable and persistent antifouling', 'oil_rejection': 'larger coalesced droplets rejected by pores of skin layer', 'detachment': 'rejected droplets directly detach from superhydrophilic surface without deposition', 'buoyancy': 'resulting large droplets float up due to buoyancy', 'recovery': 'simple water rinsing for 10 s', 'reference': '[Page 9-10; Section 3.3.2]'}
  - 来源: literature: 10.1016/j.seppur.2021.119824
- **Cr(VI) XPS吸附机制**: Cr-N(III) 575.46+585.03eV; Cr-O(VI) 576.27+586.31eV; Cr=O(VI) 577.72+587.59eV; 氨基质子化-NH₃⁺(401.2eV)
  - 条件: {'material': 'CNF/PEI@GOA-Cr', 'Cr_2p': 'six peaks: Cr=O at 587.59 and 577.72 eV; Cr-O at 586.31 and 576.27 eV; Cr-N, Cr(III) at 585.03 and 575.46 eV', 'N_1s': 'new peaks at 401.25 eV (–NH₃⁺) and 400.15 eV (Cr–N)', 'O_1s': 'new peak at 531.05 eV (Cr-O, Cr=O)', 'mechanism': 'under acidic conditions, amino protonation → positive charge → electrostatic adsorption of Cr₂O₇²⁻/CrO₄²⁻; Cr(VI) chelated by N atoms → reduced to Cr(III)', 'reference': '[Page 6; Fig. 6a-c]'}
  - 来源: literature: 10.1016/j.cej.2021.128670
- **Cd(II) XPS吸附机制**: Cd-N 411.36eV(42.95%)+404.50eV(37.72%); Cd-O 404.65eV(57.05%)+531.28eV(39.15%)
  - 条件: {'material': 'CNF/PEI@GOA-Cd', 'Cd_2p': 'Cd-N at 411.36 eV (42.95%); Cd-O at 404.65 eV (57.05%)', 'N_1s': 'Cd-N at 404.50 eV (37.72%)', 'O_1s': 'Cd-O at 531.28 eV (39.15%)', 'mechanism': 'strong interaction between N and O of adsorbent and Cd(II) due to amino + carboxyl groups cooperation', 'reference': '[Page 6; Fig. 6d-f]'}
  - 来源: literature: 10.1016/j.cej.2021.128670
- **专化-协同机制 Specialization and cooperation mechanism**: Cd(II): 协同(氨基+羧基); Cr(VI): 专化(氨基主导); Cu/Pb: 专化(羧基主导)
  - 条件: {'cooperation': 'amino and carboxyl groups jointly assist Cd(II) adsorption', 'specialization_Cr': 'amino groups dominate Cr(VI) removal via electrostatic + chelation + redox', 'specialization_Cu_Pb': 'carboxyl groups dominate Cu(II) and Pb(II) chelation', 'design': 'balance of amino and carboxyl groups + high total density → rapid complete removal', 'reference': '[Page 8; Section 3.4]'}
  - 来源: literature: 10.1016/j.cej.2021.128670

## 工程约束

- **FRR与循环稳定性 Flux recovery and cycling**: FRR 99.98%; 8次循环无显著通量衰减 %
  - 条件: {'FRR': '99.98% after simple water rinsing', 'cycles': '8 cycles without significant flux decline', 'recovery_method': 'simple water rinsing for 10 s', 'mechanism': 'oil droplets/layer easily washed away; membrane fully recoverable', 'cryo_SEM': 'minimal oil adhesion; open pores retained; micro/nano-hierarchical structures visible', 'ATR_FTIR': 'recovered membrane spectra similar to pristine', 'XPS': 'C and S peaks recovered to pristine levels', 'reference': '[Page 9; Section 3.3.2]'}
  - 来源: literature: 10.1016/j.seppur.2021.119824
- **纺锤节构建机制——Rayleigh不稳定性**: 低粘度/低导电率→电场力无法完全克服表面张力→液膜断裂→液滴串→纺锤形→纺锤节纤维 None
  - 条件: {'mechanism': 'axial Rayleigh instability in whipping jet', 'high_concentration': '4-8 wt%: high conductivity → electric force stretches jet → uniform nanofibers', 'low_concentration': '3-3.5 wt%: low viscosity/conductivity → electric force cannot overcome surface tension → drops attached to fiber → spindle-knots', 'advantage': 'continuity, flexibility, controllability, nanoscale fabrication', 'vs_other_methods': 'vs fluid coating, dip-coating, microfluidic → electrospinning is simpler and more scalable', 'reference': '[Page 3-4; Section 3.1.1]'}
  - 来源: literature: 10.1016/j.seppur.2021.119824
- **两性官能团密度 Ampholytic functional group density**: 氨基6.93 mmol/g; 羧基5.81 mmol/g (CNF/PEI@GOA); PEI@GOA: 氨基9.08, 羧基4.96 mmol/g mmol/g
  - 条件: {'material': 'CNF/PEI@GOA (amphoteric bionic fibers)', 'amino_density': '6.93 mmol·g⁻¹', 'carboxyl_density': '5.81 mmol·g⁻¹', 'PEI@GOA_amino': '9.08 mmol·g⁻¹', 'PEI@GOA_carboxyl': '4.96 mmol·g⁻¹', 'method': 'acid-base titration (Fig. 3c) + XPS', 'balance': 'amino and carboxyl groups well balanced in CNF/PEI@GOA', 'reference': '[Page 5; Section 3.1]'}
  - 来源: literature: 10.1016/j.cej.2021.128670
- **再生性能 Regeneration**: 5次循环去除率>99% %
  - 条件: {'material': 'CNF/PEI@GOA', 'cycles': '5', 'removal_rate': '>99%', 'reference': '[Page 6; Section 3.2]'}
  - 来源: literature: 10.1016/j.cej.2021.128670

## 来源汇总

- literature: 10.1002/adfm.202200359
- literature: 10.1002/advs.202103965
- literature: 10.1007/s40242-021-0010-4
- literature: 10.1016/j.cej.2021.128670
- literature: 10.1016/j.seppur.2021.119824
- literature: 10.34133/2022/9895418
