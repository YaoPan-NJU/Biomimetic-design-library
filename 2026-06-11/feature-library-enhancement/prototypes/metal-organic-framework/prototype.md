---
id: "metal-organic-framework"
name: "Metal-Organic Framework"
category: "biomimetic_adsorbent"
features:
  - ultrahigh surface area (1000-7000 m2/g)
  - microporous to mesoporous tunable pore structure
  - hierarchical porosity
  - metal coordination capacity (open metal sites)
  - reactive oxygen species (ROS) generation for catalytic degradation
  - molecular sieving (pore-size-selective adsorption)
  - post-synthetic modification (PSM)
  - structural diversity (>90,000 reported structures)
  - photo/electro-catalytic activity
pollutants:
  - Pb2+
  - Hg2+
  - As(III)/As(V)
  - Cr(VI)
  - Cd2+
  - Cu2+
  - methylene blue
  - Congo red
  - tetracycline
  - bisphenol A
  - phosphate
  - perfluorooctanoic acid (PFOA)
adsorption_mechanisms:
  - coordinative interaction with open metal sites (OMS)
  - pore filling (physisorption in micro/mesopores)
  - electrostatic interaction (charged framework + ionic pollutants)
  - pi-pi stacking (aromatic linker + aromatic pollutants)
  - hydrogen bonding (functionalized linkers)
  - catalytic degradation (Fenton-like, photocatalytic)
  - molecular sieving (size-exclusion selective adsorption)
  - ion exchange (labile counterions in framework channels)
qmax_range: "200-1500 mg/g (heavy metals); 300-2000 mg/g (organic dyes); highly MOF-specific"
removal_rate: ">95% for most target pollutants under optimal conditions"
applicability:
  ph: "1-12 (MOF-dependent; Zr-MOFs stable pH 1-12; Zn/Cu-MOFs degrade below pH 3)"
  temperature: "0-300 C (thermal stability MOF-dependent; most stable to 300-400 C in inert atmosphere)"
  salinity: "any (some MOFs tolerant to high ionic strength; others undergo ligand exchange with Cl-)"
evidence_level: "high"
last_updated: "2026-06-05"
---

# Metal-Organic Framework

## 1. Biological Prototype Introduction

金属有机框架（Metal-Organic Frameworks, MOFs）是一类由金属离子/簇（金属节点，secondary building units, SBUs）与有机配体（linkers）通过配位键自组装形成的晶态多孔材料。虽然 MOF 本身并非生物材料，但其设计理念深度受益于生物矿化（biomineralization）和酶催化的仿生思想：正如生物体内金属离子与有机分子（蛋白质、多糖）通过精确的配位几何自组装形成具有复杂层次结构的功能矿物（如铁蛋白的铁核、硅藻的硅质壳体），MOF 的合成也利用金属-配体配位化学在分子水平上精确控制晶体结构。

自 1995 年 Yaghi 提出"网状化学"（reticular chemistry）概念以来，MOF 家族已扩展至超过 90,000 种已报道结构，比表面积从数百到超过 7,000 m2/g（如 MOF-210, NU-110），孔径从 3 埃（微孔）到数十纳米（介孔），覆盖了从小分子气体储存到药物递送的广泛应用范围。

在环境水处理领域，MOF 凭借其超高比表面积、可调孔径/孔化学、以及金属节点的不饱和配位位点（open metal sites, OMS），在重金属吸附、有机染料去除、药物降解和离子选择性捕获等方面展现出远超传统吸附剂（活性炭、沸石、树脂）的性能。特别是 Zr 基 MOF（如 UiO-66, MOF-808）和 Fe 基 MOF（如 MIL-53, MIL-101）因其优异的水稳定性和催化活性，已成为水处理 MOF 研究的标杆体系。

## 2. Adsorption Mechanism Details

### 2.1 不饱和金属位点配位吸附 (Open Metal Site Coordination)

**现象**: 许多 MOF 在活化（去除孔道中溶剂分子）后，金属节点上暴露出不饱和配位位点（open metal sites, OMS），这些位点可作为 Lewis 酸与含 O、N、S 的 Lewis 碱污染物分子（如 H2O、H2S、含氧阴离子、胺类）形成配位键，实现选择性吸附。

**分子基础**: 以经典的 HKUST-1（Cu3(BTC)2, BTC = 均苯三甲酸）为例，其 Cu2 paddle-wheel SBU 在活化后每个 Cu 原子上暴露一个轴向空配位点。该 OMS 可与 Pb2+、Hg2+ 等重金属离子发生配位交换（与框架中弱配位的 H2O 或溶剂分子交换），也可与含 S 官能团（如硫醇、硫醚）的分子形成强配位键。OMS 的配位强度遵循 HSAB 理论和 Irving-Williams 序列（CM-008）：Cu2+ 节点的 OMS 对 Pb2+ 的亲和力高于 Zn2+ 和 Cd2+。

**关键官能团**: 不饱和金属位点（Cu2+, Zr4+, Fe3+, Cr3+ 等节点的轴向空位）。

**仿生设计启示**: 通过在 MOF 合成中选择具有高配位数的金属节点（如 Zr6 簇的 12 配位、Cu2 paddle-wheel 的 4+1 配位），可在活化后保留 OMS。OMS 的密度和配位强度可通过选择不同金属和配体来精确调控，实现对特定重金属离子的选择性捕获。

### 2.2 孔道填充与尺寸筛分 (Pore Filling and Molecular Sieving)

**现象**: MOF 的晶体结构决定了其孔道尺寸分布极为狭窄（单分散），可精确至 0.1 埃的精度。这种"分子筛"特性使 MOF 能够根据分子/离子的动力学直径进行尺寸选择性吸附——小于孔径的分子可进入孔道被吸附，大于孔径的分子被截留。

**分子基础**: MOF 的孔径由配体长度和 SBU 几何决定。例如：MOF-5（Zn4O(BDC)3）孔径约 11 埃；UiO-66（Zr6O4(OH)4(BDC)6）微孔约 6 埃 + 8 埃双孔体系；MIL-101(Cr) 超大介孔约 29 埃 + 34 埃。通过选择不同长度的配体（从 BDC 到 BPDC 到 TPDC），可系统调控孔径大小（isoreticular 系列，如 IRMOF-1 到 IRMOF-16）。孔道填充机制包括范德华力（physisorption）、毛细凝聚（介孔中）和静电作用（带电框架与离子型污染物）。

**关键官能团**: 孔道表面化学（裸露的金属/配体表面、功能化基团如 -NH2, -SH, -SO3H）。

**仿生设计启示**: 这一机制直接仿生自生物体中酶蛋白的活性口袋——酶通过精确的三维结构创造一个尺寸和化学性质恰好匹配底物分子的微环境。类似地，MOF 的孔道可被设计为恰好容纳目标污染物分子的"分子笼子"，实现极高的选择性。功能化配体（如 NH2-BDC、SH-BDC）可在孔道内壁引入特异性官能团，进一步提升选择性。

### 2.3 催化降解 (Catalytic Degradation via ROS Generation)

**现象**: 含 Fe、Cu、Mn 等过渡金属的 MOF 可在 H2O2 或光照条件下催化产生活性氧物种（ROS），如羟基自由基（·OH）、超氧阴离子（·O2-）和单线态氧（1O2），将有机污染物（染料、药物、内分泌干扰物）氧化降解为小分子甚至矿化为 CO2 和 H2O。

**分子基础**: Fe 基 MOF（如 MIL-53(Fe)、MIL-88B(Fe)、MIL-101(Fe)）中的 Fe3+/Fe2+ 氧化还原对可催化类 Fenton 反应：

Fe2+ + H2O2 -> Fe3+ + ·OH + OH-（链引发）
Fe3+ + H2O2 -> Fe2+ + ·OOH + H+（链传递）

与传统均相 Fenton 试剂相比，MOF 中的金属节点被有机配体"固定"在晶体框架中，防止了金属离子的溶出损失，实现了催化活性的持久稳定。此外，MOF 的高比表面积确保了有机污染物与催化位点的密切接触。

部分 MOF（如 NH2-UiO-66、MIL-125-NH2）还具有光催化活性：其有机配体作为光敏剂吸收可见光，将电子转移至金属节点，产生活性自由基降解有机污染物。

**关键官能团**: 过渡金属节点（Fe3+/Fe2+, Cu2+/Cu+）+ 光活性配体（含 -NH2 修饰的芳香配体）。

**仿生设计启示**: 这一机制仿生自细胞色素 P450 酶的催化氧化机制——P450 通过血红素铁中心活化 O2 产生活性氧物种，氧化降解毒素和药物。MOF 中的金属节点充当了类似血红素中心的催化活性位点，有机配体框架则模拟了蛋白质骨架对活性位点的空间隔离和稳定作用。

### 2.4 静电与氢键相互作用

**现象**: 带电 MOF 框架（如阴离子框架 [In(BTC)2]- 或阳离子框架 [Zn(Im)2]+）可通过静电作用吸附带相反电荷的离子型污染物。功能化配体上的 -NH2、-OH、-SO3H 等基团可通过氢键辅助吸附。

**分子基础**: 部分 MOF 框架带有固有电荷（由金属/配体的化学计量比决定），需要抗衡离子（如 Na+、Cl-、NO3-）存在于孔道中维持电中性。这些抗衡离子可被目标离子型污染物通过离子交换机制替代。例如，带正电框架的 NO3- 抗衡离子可被 Cr2O7 2- 或 AsO4 3- 置换，实现阴离子污染物的选择性吸附。功能化配体（如 2-aminoterephthalic acid 中的 -NH2）可提供额外的氢键位点，增强对含氧阴离子和有机分子的亲和力。

**仿生设计启示**: 通过选择带电框架体系或引入功能化配体，可在 MOF 中构建类似于离子交换树脂的静电吸附机制，同时保留 MOF 的超高比表面积和可调孔径优势。

### Mechanism Summary Table

| 机制 | 类型 | 关键特征 | 目标污染物 | 强度 |
|------|------|----------|------------|------|
| OMS 配位 | 化学配位 | 不饱和金属位点 | Pb2+, Hg2+, As(III/V), 含 S/N 分子 | 强 (log K > 5) |
| 孔道填充 | 物理吸附 | 超高比表面积 | 有机染料、药物、VOC | 中 (van der Waals) |
| 分子筛分 | 物理筛选 | 精确孔径控制 | 尺寸差异的混合物 | 极高选择性 |
| 催化降解 | 化学降解 | Fenton/光催化 | 有机染料、药物、EDCs | 不可逆降解 |
| 静电/离子交换 | 物理-化学 | 带电框架 + 抗衡离子 | Cr2O7 2-, AsO4 3-, PO4 3- | 中-强 |
| 氢键 | 物理吸附 | -NH2, -OH, -SO3H 修饰 | 含氧阴离子、酚类 | 弱-中 |
| pi-pi 堆积 | 物理吸附 | 芳香配体 | 芳香族污染物 (BPA, PAHs) | 中 |

## 3. Structural Features

### Multi-scale Architecture

| 尺度 | 结构特征 | 尺寸范围 | 功能角色 |
|------|----------|----------|----------|
| 宏观 | MOF 晶体形貌（八面体、立方体、片状、棒状） | 0.1-100 um | 决定粉体流动性、成型加工性和固定床填充特性 |
| 介观 | 介孔/大孔缺陷和晶间孔（interparticle voids） | 2-50 nm | 提供传质快速通道，减少扩散阻力 |
| 微观 | 晶态孔道体系（cages, channels, windows） | 0.3-5 nm | 提供超高比表面积（1000-7000 m2/g）和分子筛分能力 |
| 纳米 | 金属节点-配体配位键（SBU + linker） | 0.1-0.5 nm | 定义框架拓扑、OMS 密度和孔道表面化学 |

### Structure-Function Relationship Analysis

1. **超高比表面积与吸附容量**: MOF 的核心优势在于其极高的比表面积（BET 法，通常 1000-7000 m2/g），远超传统吸附剂（活性炭 ~1000 m2/g，沸石 ~500 m2/g，硅胶 ~300 m2/g）。比表面积与吸附容量通常呈正相关——比表面积每增加 1000 m2/g，对有机染料的 qmax 可提高约 100-300 mg/g（DP-012）。但这一关系在高浓度下趋于饱和，因为孔道填充存在空间限制。

2. **孔道层次性与传质动力学**: 完美的单晶 MOF 仅含有微孔（< 2 nm），传质完全依赖微孔扩散（Knudsen 扩散），动力学极慢。实际应用中，通过引入介孔缺陷（defect engineering）、制备纳米级 MOF 晶体（缩短扩散路径）或构建层次孔 MOF（hierarchical MOF，如通过模板法引入介孔），可大幅提升传质速率。这一策略直接对应 DP-002（层次结构优势）设计原则——跨越宏观/介观/微观的多尺度孔隙同时优化传质和容量。

3. **OMS 密度与选择性**: 不饱和金属位点的密度由 SBU 几何和配体连接数决定。例如，HKUST-1 的 Cu2 paddle-wheel SBU 提供 1 个 OMS/Cu，而 MOF-74 的一维金属氧链提供 1 个 OMS/金属原子（更高密度）。OMS 密度越高，重金属吸附容量和选择性越强，但合成难度和水稳定性也面临更大挑战。

4. **水稳定性——关键瓶颈**: 许多 MOF（特别是 Zn 基、Cu 基）在水溶液中会发生配体水解或金属节点溶解，导致结构坍塌。水稳定性与金属-氧键的强度直接相关：Zr4+-O（键能 ~776 kJ/mol）> Cr3+-O（~530 kJ/mol）> Fe3+-O（~470 kJ/mol）> Cu2+-O（~343 kJ/mol）> Zn2+-O（~284 kJ/mol）。因此 Zr-MOF（UiO-66, MOF-808）和 Cr-MOF（MIL-101）在水处理中最为常用。

## 4. Reported Performance Data

| 污染物 | 材料形态 | qmax (mg/g) | 去除率 (%) | pH | 温度 (C) | 等温线模型 | 动力学模型 | 文献来源 |
|--------|----------|-------------|-----------|-----|---------|------------|-----------|----------|
| Pb2+ | UiO-66-NH2 (Zr-MOF) | 340.5 | >95 | 5.0 | 25 | Langmuir | Pseudo-second-order | Wang et al., 2017, Chem Eng J |
| Hg2+ | thiol-MOF-5 (SH-BDC linker) | 785.2 | >99 | 4.0 | 25 | Langmuir | Pseudo-second-order | Sun et al., 2018, J Am Chem Soc |
| As(V) | UiO-66 (Zr-MOF, defect-rich) | 210.8 | 93 | 7.0 | 25 | Freundlich | Pseudo-second-order | Li et al., 2019, Environ Sci Technol |
| Cr(VI) | MIL-101(Fe) (Fe-MOF) | 125.3 | 90 | 2.0 | 25 | Langmuir | Pseudo-second-order | Zhao et al., 2018, J Hazard Mater |
| 亚甲基蓝 | MIL-101(Cr) (Cr-MOF) | 1250.0 | >99 | 7.0 | 25 | Langmuir | Pseudo-first-order | Chen et al., 2017, Chem Eng J |
| 刚果红 | ZIF-8 (Zn-MOF) | 530.4 | 97 | 7.0 | 30 | Langmuir | Pseudo-second-order | Jiang et al., 2019, J Colloid Interface Sci |
| 四环素 | MIL-53(Fe) (Fe-MOF, 光催化) | N/A (降解) | >95 | 5.0 | 25 | N/A | N/A (降解动力学) | Guo et al., 2020, Appl Catal B |
| PFOA | UiO-66-(OH)2 (Zr-MOF) | 450.2 | 96 | 4.0 | 25 | Langmuir | Pseudo-second-order | Wang et al., 2021, Water Res |

**数据说明**: MOF 的吸附性能高度依赖于具体结构、活化条件和测试方法。表中数据为代表性文献中的最优值，不同研究组的结果可能存在显著差异。催化降解类性能不以 qmax 衡量，而以降解率表示。

## 5. Biomimetic Design Narrative

### 5.1 Problem Definition (Nature's Challenge)

生物体内存在大量需要精确分子识别和催化的场景：酶需要在数以万计的代谢物中精确识别特定底物并高效催化反应；铁蛋白（ferritin）需要在 Fe2+/Fe3+ 混合体系中选择性富集和储存铁离子；细胞膜离子通道需要在 Na+/K+ 浓度比 10:1 的背景下精确区分这两种离子。这些过程的核心挑战是：**如何在分子水平上精确控制一个三维空间的几何形状和化学环境，使之对目标分子具有极高的亲和力和选择性，同时排斥其他分子？**

### 5.2 Biological Solution (Evolutionary Strategy)

生物体通过数十亿年进化发展出了"配位自组装 + 精确空间控制"的策略：

1. **酶蛋白的活性口袋**: 酶通过蛋白质折叠创造出一个三维空间恰好容纳底物分子的"口袋"，口袋内壁的氨基酸残基以精确的几何排列提供氢键、静电和疏水相互作用，实现对底物的分子级识别。这种"锁-钥"模型（lock-and-key model）是分子选择性的生物基础。

2. **铁蛋白的金属矿化**: 铁蛋白（ferritin）是由 24 个蛋白质亚基自组装形成的中空球壳（外径 12 nm，内径 8 nm），内部可储存多达 4,500 个铁原子。其蛋白质壳层上的选择性通道仅允许 Fe2+ 通过，内部氧化酶位点将 Fe2+ 氧化为 Fe3+ 并沉淀为水合氧化铁矿物核。这一"选择性通道 + 内部储存"的策略启发了 MOF 的孔道选择性设计。

3. **生物矿化的配位自组装**: 生物矿物（如骨骼的羟基磷灰石、贝壳的文石）通过有机基质（蛋白质、多糖）上的功能基团（羧基、磷酸基）引导金属离子的定向成核和晶体生长，形成具有精确形貌和取向的无机矿物。MOF 的合成也利用了类似的金属-有机配位自组装策略，只是用有机配体替代了生物大分子。

### 5.3 Key Feature Extraction

**Must-keep (不可放弃的核心特征)**:
- 超高比表面积和孔容（决定吸附容量的上限）
- 精确可调的孔径（分子筛分选择性的基础）
- 不饱和金属位点（OMS）的化学可设计性（决定重金属选择性）
- 框架拓扑的可编程性（通过选择金属节点和配体来精确控制结构）
- 后合成修饰（PSM）能力（在不改变框架的前提下引入新功能基团）

**Adjustable (可调控的设计参数)**:
- 金属节点选择（Zr4+, Fe3+, Cu2+, Cr3+, Al3+ 等，影响水稳定性和 OMS 性质）
- 有机配体选择（BDC, BTC, BPDC, TPDC 等，影响孔径和孔化学）
- 功能化方式（预合成修饰 vs. 后合成修饰；-NH2, -SH, -SO3H, -OH 等基团）
- 晶体尺寸（从纳米级到毫米级，影响传质动力学和成型加工性）
- 缺陷工程（通过调节合成条件引入缺失配体缺陷，增加 OMS 密度和介孔比例）

### 5.4 Design Mapping (Bio-feature to Material Design)

| 生物特征 | 材料设计等价物 | 设计参数 |
|----------|--------------|----------|
| 酶蛋白活性口袋 | MOF 的晶态孔道（精确尺寸 + 功能化内壁） | 配体长度决定孔径, PSM 引入功能基团 |
| 铁蛋白选择性通道 | MOF 窗口尺寸控制（window aperture） | 选择不同配体控制 window size (3-20 埃) |
| 生物矿化配位自组装 | MOF 的金属-配体溶剂热/室温合成 | 金属:配体摩尔比, 温度 80-200 C, 溶剂 DMF/H2O |
| 细胞色素 P450 活性中心 | MOF 金属节点的 OMS 催化位点 | Fe/Cu-MOF 用于类 Fenton 催化降解 |
| 蛋白质折叠的多级结构 | MOF 的层次孔隙（微孔 + 介孔 + 大孔） | 模板法或缺陷工程引入介孔/大孔 |
| 铁蛋白的 Fe 储存与释放 | MOF 的可逆吸附-脱附循环 | pH 或竞争配体触发脱附再生 |

### 5.5 Explainability Anchors

**一句话仿生故事**: "我们模仿了自然界中酶蛋白'锁-钥匹配'的分子识别策略和铁蛋白'选择性通道+内部矿化'的金属富集机制，用金属离子和有机分子自组装出孔径精确可调的纳米级'分子笼子'（MOF），让它们像微型分子筛一样精准捕获水中的重金属和有机污染物。"

**设计溯源**: MOF 的设计理念本质上是"人工酶的活性口袋"——通过精确控制三维孔道的尺寸（分子筛分）和化学环境（OMS 配位、功能化基团）来实现对目标分子的高选择性识别和捕获。DP-008（选择性设计）原则指出，生物选择性源于精确的几何和化学互补性（锁-钥模型），MOF 通过其可编辑的晶体结构最忠实地复制了这一原理。DP-012（容量 vs. 动力学权衡）则反映了 MOF 设计中微孔（高容量但慢动力学）和介孔（快速但低容量）之间的固有矛盾，层次孔 MOF 是解决这一矛盾的主要策略。

## 6. Applicable Scenarios

**适用场景**:
- 含多种重金属混合废水中的目标金属选择性捕获（利用 OMS 的 HSAB 选择性和分子筛分）
- 含难降解有机污染物（抗生素、内分泌干扰物、全氟化合物）的深度处理（利用催化降解机制）
- 饮用水中痕量砷、汞、铅的深度去除（MOF 对 As/Hg/Pb 的极高亲和力，qmax 可达数百 mg/g）
- 含染料废水的高效脱色和降解（超高比表面积 + 孔道填充 + 催化降解协同作用）
- 放射性废水处理中 U(VI)、Cs+、Sr2+ 的选择性捕获（利用功能化配体的特异性识别）
- 气体分离和储存（CO2 捕获、H2 储存、CH4 纯化）——虽然非水处理范畴，但展示了 MOF 的多功能性
- 电化学和光催化水净化系统（MOF 作为光催化剂或电极修饰材料）

**不适用场景**:
- 大规模低成本市政污水处理：MOF 合成成本高（DP-014，有机配体和溶剂成本），难以与廉价活性炭和混凝沉淀竞争
- 高浓度强酸废水（pH < 2，除 Zr-MOF 外）：多数 MOF 在强酸中框架坍塌（配体质子化导致金属-配体键断裂）
- 需要长期连续运行的固定床工艺：MOF 粉体成型困难，机械强度低，在高压水流下易粉化
- 含高浓度悬浮物的原水：悬浮颗粒会堵塞 MOF 的微孔/介孔孔道，大幅降低吸附性能
- 对生物降解性有严格要求的场景：部分 MOF 含 Cr、Cd 等有毒金属节点，框架降解后可能释放有毒金属离子（DP-016）
- 极端碱性条件（pH > 12）：金属节点可能形成氢氧化物沉淀，破坏框架完整性

## 7. Related Prototypes

- **diatom-frustule (硅藻壳体)**: 硅藻壳体是天然的介孔二氧化硅材料，具有精确的层次孔结构（微孔到介孔）。硅藻壳体可视为"天然 MOF"——通过生物矿化过程形成的具有精确孔径控制的无机多孔材料。两者在分子筛分机制上同源，但 MOF 具有更高的化学可设计性和比表面积。

- **chitosan (壳聚糖)**: 壳聚糖作为天然生物高分子，可与 MOF 形成复合材料（chitosan@MOF 或 MOF@chitosan），利用壳聚糖的氨基功能化和成型加工性弥补 MOF 粉体难以操作的缺陷，同时壳聚糖的生物降解性提高了整体材料的环境友好性（DP-016）。两者在重金属吸附中可协同作用。

- **iron-oxidizing-bacteria (铁氧化细菌)**: 铁氧化细菌通过生物矿化过程产生含 Fe(III) 的矿物沉淀（如 schwertmannite, ferrihydrite），这些矿物具有类似 Fe-MOF 的 Fe-O 配位结构和表面活性位点。两者在催化降解（类 Fenton 反应）和砷吸附方面具有相似的机制，但铁氧化细菌产物成本更低、环境友好性更高。

## 8. Design Rules Integration

本节汇总金属有机框架相关的核心设计原则和条件-机制规则，为 MOF 吸附材料设计提供系统性指导。

### Condition-Mechanism Rules

| Rule ID | 规则标题 | 核心行为 | MOF 设计启示 |
|---------|----------|----------|-------------|
| CM-008 | Irving-Williams stability series | 二价金属配合物稳定性 Cu2+ > Ni2+ > Zn2+ | MOF 的 OMS 对 Cu2+ 的选择性高于 Zn2+/Cd2+ |
| CM-019 | Universal proton suppression | pH < 3 时 H+ 竞争所有配位位点 | 强酸条件下 MOF 的 OMS 吸附也被抑制 |

### Design Principle Rules

| Rule ID | 原则标题 | 核心内容 | 与 MOF 原型的关系 |
|---------|----------|----------|------------------|
| DP-002 | Hierarchical Structure Advantage | 多尺度孔隙同时优化传质和容量 | 层次孔 MOF（微孔+介孔）解决传质瓶颈 |
| DP-008 | Selectivity Design | 锁-钥模型 vs. 分子印迹 | MOF 的精确孔径控制实现了最接近锁-钥模型的合成选择性 |
| DP-009 | Recyclability by Design | 磁性分离 + 可逆吸附 | MOF 可复合 Fe3O4 纳米粒子实现磁分离再生 |
| DP-010 | Multi-Pollutant Synergistic Removal | 多机制协同去除多种污染物 | MOF 的 OMS + 孔填充 + 催化降解可同步去除重金属和有机物 |
| DP-012 | High Capacity vs Fast Kinetics | 微孔高容量但慢速 | 纳米 MOF 晶体 + 介孔缺陷是加速动力学的关键策略 |
| DP-013 | Selectivity vs Broad Spectrum | 高选择性 vs. 广谱去除 | MOF 可通过 PSM 定制选择性，但通用型 MOF 选择性有限 |
| DP-014 | Low Cost vs High Performance | 天然材料低成本 vs. 工程材料高性能 | MOF 代表了"高成本-高性能"端，经济性是规模化应用的瓶颈 |
| DP-015 | Ease of Synthesis vs Structural Control | 简单合成 vs. 精确控制 | MOF 的溶剂热合成提供精确结构控制，但规模化生产成本高 |
| DP-016 | Environmental Friendliness vs Efficiency | 环保性 vs. 性能 | 含 Cr/有毒金属节点的 MOF 存在环境风险，Zr/Fe-MOF 更环保 |

## 9. Representative MOF Families for Water Treatment

| MOF 家族 | 金属节点 | 典型配体 | 比表面积 (m2/g) | 水稳定性 | 典型应用 |
|----------|----------|----------|-----------------|----------|----------|
| UiO-66 系列 | Zr6O4(OH)4 | BDC, NH2-BDC | 1000-1600 | 极优 (pH 1-12) | 重金属吸附、磷酸盐去除 |
| MIL-101 系列 | Cr3+, Fe3+ | BDC | 2500-4000 | 优良 (pH 2-10) | 染料吸附、催化降解 |
| HKUST-1 | Cu2 (paddle-wheel) | BTC | 1500-2000 | 较差 (遇水降解) | OMS 配位、气体吸附 |
| ZIF-8 | Zn2+ | 2-甲基咪唑 | 1500-1800 | 中等 (碱性稳定) | 染料吸附、分子筛分 |
| MOF-74 | Mg2+, Zn2+, Ni2+ | DOBDC | 1000-1500 | 中等 | 超高 OMS 密度重金属吸附 |
| MOF-808 | Zr6 | BTC | 2000-2500 | 极优 (pH 1-12) | 大分子吸附、催化 |
| MIL-53 | Al3+, Fe3+, Cr3+ | BDC | 1000-1500 | 优良 (柔性框架) | 呼吸效应选择性吸附 |

## 10. Limitations and Future Directions

### Current Limitations

1. **水稳定性**: 大多数 MOF 在水溶液中会发生配体水解或金属溶出，仅 Zr-MOF 和部分 Fe/Cr-MOF 具有可接受的长期水稳定性。
2. **成本与规模化**: 有机配体（特别是含氟、含氨基功能化配体）和有机溶剂（DMF、DEF）的成本限制了 MOF 的大规模生产。
3. **成型加工性**: MOF 粉体难以直接用于固定床柱或膜组件，需要造粒、成型或负载于载体，此过程常导致孔道堵塞和性能下降。
4. **毒性金属释放风险**: 含 Cr、Cd 等有毒金属节点的 MOF 在降解后可能释放有害金属离子，限制了其在饮用水处理中的应用。

### Emerging Research Directions

1. **水稳定 Zr-MOF 系列**: UiO-66/67/68 系列因 Zr-O 键的极高键能（~776 kJ/mol）成为最被看好的水处理 MOF，通过缺陷工程和功能化配体可持续提升性能。
2. **MOF 膜与 MOF 混合基质膜 (MMM)**: 将 MOF 晶体嵌入聚合物膜基质中，结合 MOF 的选择性和聚合物的加工性，用于膜分离和膜催化水处理。
3. **MOF 衍生碳材料**: 将 MOF 高温碳化制备多孔碳（保留 MOF 的层次孔结构），兼具高比表面积和优异的化学/机械稳定性。
4. **机器学习辅助 MOF 筛选**: 利用大数据和机器学习从 >90,000 种已报道 MOF 中筛选最优候选材料，加速从结构发现到性能优化的周期。

## 11. MOF Functionalization Strategies for Water Treatment

| 功能化策略 | 引入基团 | 合成方法 | 目标污染物 | 性能提升 |
|-----------|----------|----------|-----------|----------|
| 氨基功能化 | -NH2 (NH2-BDC linker) | 预合成或 PSM | Pb2+, Cr(VI), CO2 | qmax 提高 30-100% |
| 巯基功能化 | -SH (SH-BDC linker) | 预合成 | Hg2+, Cd2+, Pb2+ | qmax 提高 200-500% (对 Hg) |
| 磺酸基功能化 | -SO3H | PSM (后磺化) | 碱性染料, 重金属 | 新增离子交换机制 |
| 缺陷工程 | 缺失配体 (missing-linker) | 调节剂法 (modulator) | As(V), PO4 3- | 增加 OMS 密度和介孔比例 |
| 金属交换 | 混合金属节点 | 一锅法或 PSM | 多金属选择性 | 可调 OMS 的 Lewis 酸性 |
| 磁性复合 | Fe3O4@MOF | 共沉淀 + MOF 生长 | 各类污染物 | 增加磁分离再生能力 |

## 11. References

1. **Furukawa, H., Cordova, K.E., O'Keeffe, M., Yaghi, O.M.** (2013). The chemistry and applications of metal-organic frameworks. *Science*, 341(6149), 1230444. -- MOF 领域的权威综述，系统总结了 MOF 的化学原理、结构多样性和在气体储存、分离、催化等领域的应用，提出了"网状化学"（reticular chemistry）的核心概念框架。

2. **Li, J.R., Sculley, J., Zhou, H.C.** (2012). Metal-organic frameworks for separations. *Chemical Reviews*, 112(2), 869-932. -- 全面综述了 MOF 在分子分离中的应用，包括气体分离、液相分离和手性拆分，深入讨论了孔径控制和表面化学功能化对分离选择性的影响。

3. **Wang, C., Liu, X., Keser Demir, N., Chen, J.P., Li, K.** (2016). Applications of water stable metal-organic frameworks. *Chemical Society Reviews*, 45(18), 5107-5134. -- 重点讨论了水稳定 MOF（特别是 Zr-MOF 和 Fe-MOF）在水处理中的应用，包括重金属吸附、染料去除和催化降解，分析了水稳定性与结构之间的关系。

4. **Sun, B., Reddy, E.P., Smirniotis, P.G.** (2020). Visible light-driven metal-organic frameworks for environmental remediation. *Environmental Science & Technology*, 54(18), 11088-11103. -- 综述了可见光驱动 MOF 光催化剂在环境修复中的应用，包括有机污染物降解、重金属还原和杀菌，分析了 MOF 光催化机制与结构-性能关系。

5. **Kukkar, P., Sharma, V., Kim, K.H., Deep, A.** (2021). Metal-organic frameworks for the removal of emergent organic pollutants from water and wastewater. *Science of the Total Environment*, 780, 146634. -- 系统综述了 MOF 对新兴有机污染物（药物、内分泌干扰物、全氟化合物、微塑料添加剂）的吸附和催化降解性能，讨论了 MOF 从实验室到实际水处理应用的挑战和前景。
