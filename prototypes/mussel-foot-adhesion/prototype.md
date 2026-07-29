---
id: mussel-foot-adhesion
name: 贻贝足丝（Mussel Foot Adhesion）
category: 动物
organism: Mytilus spp.
biomimetic_dimension: 分子仿生
features:
  - 疏水性
  - 邻苯二酚基团
  - 金属配位能力
  - π电子体系
  - 湿态粘附
pollutants:
  - Carmine (胭脂红)
  - Co(II)
  - Co2+
  - CrO42-
  - Cu2+
  - Fe2+
  - Ge(IV)
  - Hg(II)
  - Ni(II)
  - Ni2+
  - Pb(II)
  - SMX
  - U(VI)
  - 铀 U(VI)
  - 铀(U)
adsorption_mechanisms:
  - 贻贝足丝DOPA儿茶酚-金属多齿配位与胺基静电黏附
  - 磷酸胆碱仿生机制 Phosphorylcholine biomimetic mechanism
  - PDA自聚合形成机制 PDA self-polymerization mechanism
  - PDA涂层 vs 传统涂层技术对比 PDA coating vs traditional coating techniques
  - 多巴胺辅助共沉积机制 Dopamine-assisted co-deposition mechanism
  - 三种驱动力协同机制
  - 染料絮凝实验——盐浓度效应确认静电机制
  - 疏水改性方法分类
  - CVD法均匀性问题
  - 疏水改性材料分布统计
qmax_range: "1.0-1194.4 mg/g"
applicability:
  pH_range: [3.0, 6.8]
  temp_range: null
  salinity: moderate
evidence_level: medium
# provenance: 27 papers, 33 verified, 115 unverified
# coverage: normal
# status: active
---
# 贻贝足丝（Mussel Foot Adhesion）

## 1. 生物原型简介

**问题定义**：自然界挑战：生物体在复杂水环境中需维持表面干燥、清洁或定向导流（如荷叶防污、鱼鳞防油粘附）；水处理对应：含油废水及表面活性剂稳定乳液分离面临膜污染严重、通量快速衰减、油水界面张力高及传统材料选择性差等工程难题。

**生物策略**：进化策略：生物通过微纳多级粗糙结构与表面化学修饰的协同，精准调控固-液-气/油三相界面能，实现超疏水/超亲水/各向异性润湿；关键机制：基于Wenzel/Cassie-Baxter润湿模型与Young-Laplace入侵压力控制，结合PDA通用粘附化学、光催化降解与动态配位键；成功案例：荷叶微纳蜡质层实现超疏水自清洁，鱼鳞定向微乳突捕获水膜实现水下超疏油，贻贝足丝PDA实现材料表面快速通用功能化。

## 2. 吸附机制详解

### 机制1：贻贝足丝DOPA儿茶酚-金属多齿配位与胺基静电黏附

**描述**：两性离子通过静电作用可结合多达8个水分子，而PEG每个重复单元(-CH2CH2O-)仅能通过氢键结合1个水分子
**关键官能团**：['静电作用位点', 'PEG醚键', '氢键位点', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1039/d1cs00658d

### 机制2：磷酸胆碱仿生机制 Phosphorylcholine biomimetic mechanism

**描述**：磷酸甜菜碱基两性离子聚合物被视为仿生抗污材料，因其具有通常存在于细胞膜外层的磷酸胆碱头基
**关键官能团**：['-S-（硫醚键）', '-PO₄³⁻（磷酸基）', '-O-（醚键）']
**来源**：DOI 10.1039/d1cs00658d

### 机制3：PDA自聚合形成机制 PDA self-polymerization mechanism

**描述**：氧化条件下羟基自发去质子化形成多巴胺醌，经亲核分子内环化变为leukodopaminechrome，再经进一步氧化重排形成5,6-二羟基吲哚或5,6-吲哚醌，最终通过2,3,4,7位分支反应交联形成类真黑素聚合物PDA
**关键官能团**：['PAM酰胺基', '吲哚环', '聚多巴胺（PDA）邻苯二酚/胺基', '-OH（羟基）', '-NH₂（氨基）', '-S-（硫醚键）', '邻苯二酚（catechol）', '-O-（醚键）']
**来源**：DOI 10.1039/d1cs00658d

### 机制4：PDA涂层 vs 传统涂层技术对比 PDA coating vs traditional coating techniques

**描述**：PDA可沉积于任何表面（有机/无机、亲水/疏水、块状/纤维状/颗粒状、金属/聚合物/活细胞），而SAM仅限贵金属表面（Cu/Pt/Ag/Au）通过巯基金属键或氧化物表面通过烷基硅烷；LbL需多步沉积且耗时费力
**关键官能团**：['硅烷偶联剂', '聚多巴胺（PDA）邻苯二酚/胺基', '-SH（巯基）', '-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1039/d1cs00658d

### 机制5：多巴胺辅助共沉积机制 Dopamine-assisted co-deposition mechanism

**描述**：多巴胺辅助共沉积涉及多巴胺与第二组分之间的单/多共价或非共价相互作用。共价共沉积提供更强网络以促进涂层稳定性。poly(SBMA)通过去质子化酚基与季铵的局部静电作用与PDA交互；poly(MPC)通过酚-磷脂氢键和阳离子-π相互作用与PDA交互
**关键官能团**：['PAM酰胺基', '静电作用位点', '-O-（醚键）', '聚多巴胺（PDA）邻苯二酚/胺基', '-NH₂（氨基）', '氢键位点', '-S-（硫醚键）', '邻苯二酚（catechol）', '季铵基团']
**来源**：DOI 10.1039/d1cs00658d

### 机制6：三种驱动力协同机制

**描述**：静电吸引/排斥(主导) + π-π堆积 + 氢键→协同或竞争效应→决定选择性吸附
**关键官能团**：['π-π堆积位点', '静电作用位点', '氢键位点']
**来源**：DOI 10.1016/j.cej.2021.129237

### 机制7：染料絮凝实验——盐浓度效应确认静电机制

**描述**：KCl浓度从1→50→100mM: 絮凝量随盐浓度增加而降低→静电屏蔽效应→与ITC结果一致
**来源**：DOI 10.1016/j.cej.2021.129237

### 机制8：疏水改性方法分类

**描述**：CVD, AHSM, Dip coating, Carbonization
**关键官能团**：['-S-（硫醚键）', '-O-（醚键）']
**来源**：DOI 10.1016/j.carbpol.2022.120242

## 3. 结构特征与结构-功能关系

必须保留特征：微纳复合粗糙度、低/高表面能化学组分、三相界面润湿态（Cassie-Baxter态）的精准调控；可灵活调整特征：基底材质（织物/金属网格/海绵）、功能涂层（PDA/PDMS/ZIF-8/水凝胶）、智能响应机制（光催化自清洁/配位自修复/Janus膜翻转切换）。

## 4. 已报道性能数据

| 污染物 | 材料 | qmax/去除率 | pH | 来源 | 核查 |
|--------|------|-------------|-----|------|------|
| SMX |  | MI-PDA/PDS体系对SMX去除率> | 6.8 | literature: 10.1016/j.apcatb.2 | ✅ |
| 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | >50 | ≥5 | patent: CN105413659B | ⚠️ |
| 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | >90 | ≥5 | patent: CN105413659B | ❓ |
| 铀 U(VI) | 聚多巴胺包覆Fe3O4磁性仿生吸附剂 | 97.3 | 3.0 | patent: CN105413659B | ❓ |
| Cu2+ | PDA-Fe3O4@CS | 12.5 | - | patent: CN113042006A | ❓ |
| CrO42- | PDA-Fe3O4@CS | 114.88 | - | patent: CN113042006A | ❓ |
| Cu2+ |  | PDA:CS=1:4→12.5mg/g; | - | patent: CN113042006A | ❓ |
| CrO42- |  | PDA:CS=1:4→114.88mg/ | - | patent: CN113042006A | ❓ |
| 铀(U) | PDA改性PAO薄膜 | 403.21 | 5.0 | patent: CN114849661A | ❓ |
| U(VI) |  | 改性时间4h→403.085mg/g;  | - | patent: CN114849661A | ❓ |
| U(VI) |  | qt = (C0 - Ce) × V / | - | patent: CN114849661A | ❓ |
| U(VI) |  | >72 | - | patent: CN115055171A | ✅ |
| Hg(II) | HAp/Fe3O4/PDA | 51.73 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Co(II) | HAp/Fe3O4/PDA | 49.32 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Ni(II) | HAp/Fe3O4/PDA | 48.09 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Hg(II) | HAp/Fe3O4/PDA | 94.36 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Co(II) | HAp/Fe3O4/PDA | 93.66 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Ni(II) | HAp/Fe3O4/PDA | 92.36 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Hg(II) | HAp/Fe3O4/PDA | 90.14 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Co(II) | HAp/Fe3O4/PDA | 88.84 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Ni(II) | HAp/Fe3O4/PDA | 87.46 | 6 | literature: 10.1016/j.jece.202 | ✅ |
| Pb(II) | MnO2/PDA/Fe3O4 fiber | 196.67 | 5.0 | literature: 10.1016/j.apsusc.2 | ✅ |
| Pb(II) | MnO2/PDA/Fe3O4 fiber | 200.45 | 5.0 | literature: 10.1016/j.apsusc.2 | ✅ |
| Pb(II) | MnO2/PDA/Fe3O4 fiber | 205.07 | 5.0 | literature: 10.1016/j.apsusc.2 | ✅ |
| Fe2+ | COF@PDA | 204.9 | 6 | literature: 10.1016/j.cej.2020 | ✅ |
| Co2+ | COF@PDA | 194.2 | - | literature: 10.1016/j.cej.2020 | ✅ |
| Ni2+ | COF@PDA | 207.5 | - | literature: 10.1016/j.cej.2020 | ✅ |
| Ni(II) |  | Fe2+: ~98%, Co2+: ~9 | - | literature: 10.1016/j.cej.2020 | ✅ |
|  |  | 55.4 | - | literature: 10.1016/j.cej.2020 | ✅ |
|  |  | 31.4 | - | literature: 10.1016/j.cej.2020 | ✅ |
| ... | ... | ... | ... | ... | 共 41 条 |

## 5. 适用场景

**约束条件**：
- m-CPMCA燃烧再生循环: 86 % (retained after 7 cycles)
- MI-PDA的循环稳定性 Cycling stability of MI-PDA: 连续4次循环后催化活性仍保持>71%，吸附性能无明显衰减；催化剂形貌和化学结构在激活PDS后保持稳定 None
- pH响应润湿性反转机制 pH-responsive wettability reversal mechanism: 可离子化和可水解聚合物响应pH变化质子化/去质子化，改变水合状态，在亲水和疏水间切换 None
- 多巴胺水溶液pH调节 / Dopamine solution pH adjustment: pH 7.5-9.5（较佳范围）；pH 8.5（最佳） None
- 反应温度 / Reaction temperature: 20-40°C（较佳范围）；30°C（最佳） °C
- 铀去除率 Uranium removal rate (pH≥5): >90 %
- 特定条件下去除率 Removal rate at pH 3.0: 97.3 %
- 循环复用性能 Cycling stability: 3次循环后吸附性能无明显降低 None
- 适用pH范围 Applicable pH range: 1-6.5 None
- 吸附操作温度 Adsorption operating temperature: 25±0.2 °C

## 6. 相关原型

- bile-salt-mixed-micelle-solubilization
- cactus-spine
- chitosan
- errg-bpa-endocrine-receptor
- fabp4-fatty-acid-pfas-binding

## 参考文献

[1] DOI: 10.1016/j.apcatb.2023.122852
[2] DOI: 10.1016/j.apsusc.2020.148379
[3] DOI: 10.1016/j.cej.2020.127837
[4] DOI: 10.1016/j.jece.2021.105709
[5] DOI: 10.1016/j.jhazmat.2020.124347
[6] DOI: 10.13373/j.cnki.cjrm.XY21060036
[7] DOI: 10.13550/j.jxhg.20220633
[8] 专利: CN105413659B
[9] 专利: CN113042006A
[10] 专利: CN114570339A
[11] 专利: CN114849661A
[12] 专利: CN115055171A
