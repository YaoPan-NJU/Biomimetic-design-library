---
id: chitosan
name: 壳聚糖（Chitosan）
category: 仿生材料
organism: Crustacea (甲壳类外骨骼几丁质)
biomimetic_dimension: 分子仿生
features:
  - 亲水性
  - 正电表面
  - 氨基
  - 金属配位能力
pollutants:
  - Al(III)
  - As(III)
  - As(V)
  - CR
  - Cd(II)
  - Cr(VI)
  - Cr(铬)
  - Cu(II)
  - Cu2+
  - F-
  - FD&C Red 40染料
  - Hg(II)
  - MB (methylene blue)
  - Microplastics
  - Mn2+
  - PO43-
  - PO43- (磷酸根)
  - PO₄³⁻
  - Pb(II)
  - Pb2+
  - Reactive Blue 19
  - Sb(锑)
  - TiO2 nanoparticles
  - U(VI)
  - acid blue-113 (anionic dye)
  - methyl orange (MO)
  - reactive dyes
  - tetracycline
  - triclosan (TCS)
  - 二氯甲烷
  - 亚甲基蓝(MB)阳离子染料
  - 双酚A（BPA）
  - 壬基酚
  - 柴油
  - 活性黑5(RB5)
adsorption_mechanisms:
  - 壳聚糖氨基/羟基多齿螯合与静电吸附
  - 金属离子络合机制 Metal ion complexation mechanism
  - pHpzc对吸附机制的影响 pHpzc effect on adsorption mechanism
  - 表面沉淀机制 Surface precipitation mechanism
  - FTIR表征——吸附前后对比
  - XPS表征——C 1s和N 1s
  - 制备方法
  - 吸附机制——综合分析
  - CS/GO复合物对MB吸附的π-π堆积机制
  - 壳聚糖对阴离子染料的吸附机制
qmax_range: "1.0-2230.0 mg/g"
applicability:
  pH_range: [3.0, 7.0]
  temp_range: null
  salinity: low_to_moderate
evidence_level: low
# provenance: 51 papers, 115 verified, 134 unverified
# coverage: normal
# status: active
---
# 壳聚糖（Chitosan）

## 1. 生物原型简介

**问题定义**：自然界中甲壳生物利用甲壳素/壳聚糖的氨基与多糖网络捕获金属离子，结合天然矿物的微孔结构实现物质富集；对应水处理中低浓度磷酸盐去除困难、传统吸附剂容量有限且易发生金属溶出二次污染的挑战。

**生物策略**：进化策略借鉴天然高分子（壳聚糖）的柔性链段与丰富官能团（乙酰胺基）提供高活性改性位点，结合天然沸石的刚性多孔骨架提供高比表面积与快速传质通道；关键机制为La(OH)3在复合基质表面均匀沉淀，通过内球配合与离子交换特异性捕获磷酸根；成功案例为La-MZ/CTS在pH 6、25°C下实现27.9 mg/g吸附容量，较未负载材料提升近10倍，且镧溶出量极低，验证了该仿生策略的高效性与稳定性。

## 2. 吸附机制详解

### 机制1：壳聚糖氨基/羟基多齿螯合与静电吸附

**描述**：La(OH)3与磷酸盐结合形成内球配合物进行除磷
**关键官能团**：['-NH-（亚氨基）', '壳聚糖氨基/羟基', '-PO₄³⁻（磷酸基）', '-OH（羟基）', '-NH₂（氨基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.13671/j.hjkxxb.2020.0407

### 机制2：金属离子络合机制 Metal ion complexation mechanism

**描述**：主机制：壳聚糖自由-NH2和-OH上的孤对电子捐赠给缺电子金属阳离子的D轨道形成络合物/螯合物；桥模型（多氨基链间/链内络合）和 pendant模型（氨基悬挂式附着）
**关键官能团**：['-NH-（亚氨基）', '壳聚糖氨基/羟基', '配位/螯合位点', '-OH（羟基）', '-NH₂（氨基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1016/j.carbpol.2020.117000

### 机制3：pHpzc对吸附机制的影响 pHpzc effect on adsorption mechanism

**描述**：pHpzc值取决于具体壳聚糖改性方式；一般CCS pHpzc约5-6，PACCS pHpzc约4-5
**关键官能团**：['-NH-（亚氨基）', '离子交换位点', '静电作用位点', '壳聚糖氨基/羟基', '配位/螯合位点', '-OH（羟基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1016/j.carbpol.2020.117000

### 机制4：表面沉淀机制 Surface precipitation mechanism

**描述**：仅Cr(III)观察到沉淀（因Cr(OH)3第一稳定常数远高于其他离子）；其他离子（Cu, Zn, Ni, Pb, Cd, Mn, Co）遵循络合、离子交换和静电机制
**关键官能团**：['-NH-（亚氨基）', '离子交换位点', '静电作用位点', '壳聚糖氨基/羟基', '配位/螯合位点', '-OH（羟基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1016/j.carbpol.2020.117000

### 机制5：FTIR表征——吸附前后对比

**描述**：吸附后：3446→3429 cm⁻¹偏移(Pb与-COO⁻静电/配位)；2923/2854/1641/1383/1049 cm⁻¹峰强度显著降低→Pb与-COO⁻和-NHCOO⁻形成静电和配位键
**关键官能团**：['-NH-（亚氨基）', '离子交换位点', '静电作用位点', '壳聚糖氨基/羟基', '-COO⁻（羧基阴离子）', '配位/螯合位点', '-OH（羟基）', '-O-（醚键）']
**来源**：DOI 10.1016/j.molliq.2020.114523

### 机制6：XPS表征——C 1s和N 1s

**描述**：C 1s：284.7(C-O)/286.55(C=O)/288.45(COO⁻)→吸附前后无显著变化→Pb不与C配位；N 1s：吸附前399.8 eV(-NH₂)→吸附后三峰399.55(-NH₂)/400.2(-NH₃⁺)/400.7(O=C-N)→N原子孤对电子与Pb形成共价键
**关键官能团**：['-NH-（亚氨基）', '离子交换位点', '静电作用位点', '壳聚糖氨基/羟基', '-COO⁻（羧基阴离子）', '配位/螯合位点', '-OH（羟基）', '-S-（硫醚键）', '-O-（醚键）', '-C=O（羰基）']
**来源**：DOI 10.1016/j.molliq.2020.114523

### 机制7：制备方法

**描述**：羧基化壳聚糖(CYCS)+羧基化纳米纤维素(CNC)在CaCl₂溶液中螯合交联→形成水凝胶珠；CYCS通过壳聚糖羧甲基取代获得→取代度>60%；成本显著低于CMCS
**关键官能团**：['-NH-（亚氨基）', '离子交换位点', '-COOH（羧基）', '静电作用位点', '壳聚糖氨基/羟基', '配位/螯合位点', '纤维素羟基', '-OH（羟基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1016/j.molliq.2020.114523

### 机制8：吸附机制——综合分析

**描述**：化学吸附为主(PSO拟合+XPS证据)；-COO⁻与Pb²⁺静电吸引+配位；-NH₂孤对电子与Pb形成共价键；可能生成碳酸铅/氧化铅沉淀；三种官能团(-OH/-COO⁻/-NH₂)协同参与
**关键官能团**：['离子交换位点', '-OH: electrostatic', '静电作用位点', '-COO⁻: electrostatic + coordination', '壳聚糖氨基/羟基', '-COO⁻（羧基阴离子）', '配位/螯合位点', '-OH（羟基）', '-O-（醚键）', '-NH2: lone pair electron sharing']
**来源**：DOI 10.1016/j.molliq.2020.114523

## 3. 结构特征与结构-功能关系

必须保留特征：壳聚糖的氨基/羟基官能团网络、沸石的刚性多孔骨架、La(OH)3活性位点的均匀分布、内球配合吸附机制；可灵活调整特征：焙烧温度与时间（调控孔径与结晶度）、镧负载浓度（优化至5 mg/L）、复合基质比例（平衡机械强度与吸附容量）。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| PO43- (磷酸根) | La-MZ/CTS (镧负载沸石壳聚糖复 | 27.9 | 6 | literature: 10.13671/j.hjkxxb. | ❓ |
| PO43- | MZ/CTS (沸石壳聚糖复合材料，未负 | 4.80 | - | literature: 10.13671/j.hjkxxb. | ❓ |
| 壬基酚 |  | La-MZ/CTS: 27.90 mg/ | - | literature: 10.13671/j.hjkxxb. | ❓ |
| Cu(II) |  | 铜离子浓度越高，在相同条件下去除百分比越 | - | literature: 10.1016/j.cjche.20 | ⚠️ |
| 壬基酚 |  | 增加吸附剂投加量→Cu去除率增加；最大C | - | literature: 10.1016/j.cjche.20 | ⚠️ |
| 壬基酚 | 铝基金属有机框架/海藻酸钠-壳聚糖复合珠 | 139.9 mg/g（298K） | - | literature: 10.1016/j.chemosph | ❓ |
| 壬基酚 | 沥青衍生超高比表面积活性炭(AS) | 1113 mg/g | - | literature: 10.1016/j.chemosph | ⚠️ |
| 壬基酚 | H₃PO₄活化阿甘坚果壳活性炭(AC-H | 1250 mg/g（293K） | - | literature: 10.1016/j.chemosph | ❓ |
| Cu(II) |  | 纯壳聚糖珠溶胀率39.8%，戊二醛交联后 | - | literature: 10.1016/j.seta.202 | ❓ |
| Pb(II) | γ-Fe₃O₄嵌入壳聚糖/纤维素珠 | Cu(II) 88.21, Cd(II) | - | literature: 10.1016/j.seta.202 | ❓ |
| Pb(II) | 壳聚糖纳米纤维膜+TiO₂纳米颗粒 | 嵌入型TiO₂: Cu(II) 710. | - | literature: 10.1016/j.seta.202 | ❓ |
| Cu(II) | ZIF-67改性纤维素/壳聚糖气凝胶 | BET从8.4增至268.7 m²/g， | - | literature: 10.1016/j.seta.202 | ❓ |
| Cu(II) |  | 纯壳聚糖: 80.71 mg/g; 壳聚 | - | literature: 10.1016/j.carbpol. | ❓ |
| Cd(II) |  | Chitosan-GLA: 124→40 | - | literature: 10.1016/j.carbpol. | ❓ |
| As(V) |  | Ag(I)-imprinted CT/T | - | literature: 10.1016/j.carbpol. | ❓ |
| Pb(II) | CYCS/CNC hydrogel be | 334.92 | - | literature: 10.1016/j.molliq.2 | ⚠️ |
| Pb(II) | CYCS/CNC hydrogel be | 297K 333.94; 303K 33 | - | literature: 10.1016/j.molliq.2 | ⚠️ |
| FD&C Red 40染料 | 壳聚糖粉末 | DD从42%增至84%时，FD&C Re | - | literature: 10.3390/molecules2 | ❓ |
| Cd(II) | 壳聚糖/海藻酸盐复合物 | Cu(II)从66%提升至81%，Cd( | - | literature: 10.3390/molecules2 | ❓ |
| Cd(II) | 壳聚糖/活性炭复合物 | CS/AC: 52.63 mg/g, A | - | literature: 10.3390/molecules2 | ❓ |
| 亚甲基蓝(MB)阳离子染料 | 壳聚糖/氧化石墨烯复合物 | 超过1000 mg/g | - | literature: 10.3390/molecules2 | ❓ |
| 活性黑5(RB5) | 壳聚糖(不同DD和形态) | 水凝胶珠形式DD 90%时吸附容量155 | - | literature: 10.3390/molecules2 | ❓ |
| As(V) |  | Fe-壳聚糖微球: As(V) 120. | - | literature: 10.1016/j.ijbiomac | ❓ |
| As(V) |  | Fe(III)-壳聚糖对As(V)去除效 | - | literature: 10.1016/j.ijbiomac | ❓ |
| As(V) |  | 交联度增加可增强机械强度但可能降低吸附容 | - | literature: 10.1016/j.ijbiomac | ❓ |
| As(III) | 硫醇功能化壳聚糖 | pH 3-10范围内去除效率99% | - | literature: 10.1016/j.ijbiomac | ❓ |
| As(V) | 壳聚糖电纺纳米纤维膜 | 壳聚糖电纺纳米纤维膜通过外球表面配合机制 | - | literature: 10.1016/j.ijbiomac | ❓ |
| 壬基酚 |  | 最大吸附容量50 mg/g(Brion- | - | literature: 10.1016/j.ijbiomac | ❓ |
| As(V) |  | 三步机制：扩散→氧化→吸附；As(III | - | literature: 10.1016/j.ijbiomac | ⚠️ |
| PO₄³⁻ | polyaminated chitosa | 103.96 | - | literature: 10.1016/j.carbpol. | ❓ |
| ... | ... | ... | ... | ... | 共 102 条 |

## 5. 适用场景

**约束条件**：
- 最佳pH值 Optimal pH: 6 None
- pH范围限制 pH constraint: 仅测试pH 4-6，pH>6未研究(因Cu²⁺沉淀) None
- 酸洗脱再生效率 Acid eluent desorption efficiency: 0.5M HCl洗脱: Cd 98.94%, Pb 97.50%（戊二醛交联+聚苯胺接枝壳聚糖珠），4次循环后吸附容量不变 percent
- EDTA洗脱vs酸洗脱 EDTA vs acid eluents for regeneration: EDTA作为洗脱剂时吸附容量几乎不变；使用HNO3/H2SO4/HCl时后续循环吸附容量显著降低（壳聚糖分解） None
- TGA热稳定性: CYCS失重83.8%；CNC失重72.7%；CYCS/CNC失重60.3%→交联提高热稳定性；三阶段失重：30-150°C(水分蒸发)/220-380°C(壳聚糖分解)/390-780°C(进一步分解+CO₂+H₂O) %
- 3D GO/壳聚糖复合物稳定性与可循环性: 高分子量壳聚糖+3D GO可实现5次循环90%吸附容量；壳聚糖/GO海绵>80%再生效率5次循环 %
- 壳聚糖复合物的再生挑战: NaOH/酸处理导致壳聚糖逐步水解，吸附容量随循环次数降低 None
- pH对砷吸附的影响 pH effect on arsenic adsorption: As(V)吸附随pH升高先增后减(最优pH 6.7)；As(III)在pH 5-9范围内吸附不受pH影响(因中性态)，pH>9时吸附下降 None
- 壳聚糖基吸附剂的砷解吸与再生 As desorption and regeneration of chitosan-based sorbents: 0.1 M NaOH作为解吸剂可恢复>90%砷去除效率；碱性介质中壳聚糖表面电荷中和导致砷解吸 None
- 壳聚糖的热稳定性 Thermal stability of chitosan-based sorbents: 原始壳聚糖热降解分两阶段：30-220°C(水分和挥发物去除)和230-545°C(糖苷键断裂、脱乙酰、聚合物骨架分解)；改性壳聚糖在500-800°C第三阶段降解 None

## 6. 相关原型

- chlorella-cell-wall
- mussel-foot-adhesion
- mycelium
- plant-tannin
- polydopamine-coating

## 参考文献

[1] DOI: 10.1007/s10311-023-01563-9
[2] DOI: 10.1007/s10924-021-02312-1
[3] DOI: 10.1007/s13762-021-03603-9
[4] DOI: 10.1016/j.carbpol.2020.117000
[5] DOI: 10.1016/j.carbpol.2021.118625
[6] DOI: 10.1016/j.carbpol.2021.118671
[7] DOI: 10.1016/j.carbpol.2022.119383
[8] DOI: 10.1016/j.cej.2022.138934
[9] DOI: 10.1016/j.chemosphere.2020.129273
[10] DOI: 10.1016/j.cjche.2020.07.066
[11] DOI: 10.1016/j.ijbiomac.2021.08.047
[12] DOI: 10.1016/j.ijbiomac.2021.10.050
[13] DOI: 10.1016/j.jece.2022.108048
[14] DOI: 10.1016/j.jhazmat.2020.124347
[15] DOI: 10.1016/j.jhazmat.2022.129112
[16] DOI: 10.1016/j.molliq.2020.114523
[17] DOI: 10.1016/j.molliq.2023.122763
[18] DOI: 10.1016/j.rechem.2024.101332
[19] DOI: 10.1016/j.scitotenv.2021.150606
[20] DOI: 10.1016/j.seta.2020.100951
[21] DOI: 10.13550/j.jxhg.20210304
[22] DOI: 10.13671/j.hjkxxb.2020.0407
[23] DOI: 10.14028/j.cnki.1003-3726.2021.02.007
[24] DOI: 10.15898/j.ykcs.202208230155
[25] DOI: 10.19965/j.cnki.iwt.2022-1185
[26] DOI: 10.3390/molecules26030594
[27] DOI: 10.3390/toxics10090500
[28] DOI: 10.3969/j.issn.1001-9731.2022.10.023
[29] 专利: CN109351339A
[30] 专利: CN114873705A
[31] 专利: CN117654453A
[32] 专利: CN119488883A
[33] 专利: CN121130847A
