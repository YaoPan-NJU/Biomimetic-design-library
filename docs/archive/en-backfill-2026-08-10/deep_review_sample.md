
## decarboxylase-carbanion-activation（3 机制）
- organism_src: Methanothermobacter thermautotrophicus / Saccharomyces cerevisiae（OMPDC 乳清苷 5'-磷酸脱羧酶，EC 4.1.1.23）
- organism_en : Methanothermobacter thermautotrophicus / Saccharomyces cerevisiae (OMPDC orotidine 5'-phosphate decarboxylase, EC 4.1.1.23)

--- 机制 0 ---
**name** 中: 活性位点交替电荷阵列对羧酸底物的基态去稳定化（静电应力）
name_en: Ground-state destabilization of carboxylate substrates by an alternating charge array in the active site (electrostatic stress)
**description** 中: Methanothermobacter thermautotrophicus OMPDC（MtODCase）为 TIM 桶折叠同源二聚体（PDB 1DV7，KEYWDS: TIM barrel, dimer；配体游离态 1.8 Å，6-氮杂尿苷 5'-磷酸复合物 1DVJ 1.5 Å）；活性位点具独特交替电荷阵列（Lys-Asp-Lys-Asp）；抑制剂 6-azaUMP（配体 UP6）在 PDB 1DVJ 中与 ASP A 20、LYS A 42、LYS A 72、MET A 126、SER A 127、PRO A 180、GLN A 185、GLY A 202、ARG A 203 接触（chain A，PDB 编号）。量子力学/分子动力学计算表明催化能力几乎完全来自对底物反应部分的去稳定化（基态去稳定化），由磷酸与核糖基团的强结合补偿（Jencks Circe 效应）
description_en: Methanothermobacter thermautotrophicus OMPDC (MtODCase) is a TIM-barrel-fold homodimer (PDB 1DV7, KEYWDS: TIM barrel, dimer; ligand-free form 1.8 Å, 6-azauridine 5'-phosphate complex 1DVJ at 1.5 Å); the active site bears a distinctive alternating charge array (Lys-Asp-Lys-Asp); the inhibitor 6-azaUMP (ligand UP6) in PDB 1DVJ contacts ASP A 20, LYS A 42, LYS A 72, MET A 126, SER A 127, PRO A 180, G
**tp** 中: 预组织的互补电荷/氢键阵列可以「远端锚定部分强结合 + 反应性头基静电活化（基态去稳定化，Circe 效应）」的策略高效催化转化羧酸底物；该「锚定补偿的头基活化」策略在原理层可外推至其他羧酸头基的活化与转化
tp_en: A preorganized array of complementary charges/hydrogen bonds can efficiently catalyze the transformation of carboxylate substrates via the strategy of strong binding of the distal anchoring moiety plus electrostatic activation of the reactive headgro

--- 机制 1 ---
**name** 中: 过渡态电荷稳定化与质子递送（过渡态类似物结构证据）
name_en: Transition-state charge stabilization and proton delivery (structural evidence from a transition-state analogue)
**description** 中: 酿酒酵母重组 OMPDC（Miller 2000，TIM 桶折叠，配体结合位点近桶开口端）与提议的过渡态类似物 6-羟基尿苷 5'-磷酸（BMP）复合时，蛋白环运动几乎完全包埋配体；Lysine-93（酿酒酵母 OMPDC 编号）被锚定于优化与嘧啶环 C-6 发展负电荷之静电相互作用的位置，并递送取代产物 C-6 羧基的质子；活性位点对 O-2/O-4 的氢键协助离域过渡态负电荷。注意：Lysine-93 为酿酒酵母酶编号，与 PDB 1DV7/1DVJ 的 Methanothermobacter 酶编号（如 Lys 72）分属不同物种同源酶，此处不做跨物种编号换算
description_en: When recombinant Saccharomyces cerevisiae OMPDC (Miller 2000, TIM-barrel fold, ligand-binding site near the barrel opening) is complexed with the proposed transition-state analogue 6-hydroxyuridine 5'-phosphate (BMP), protein loop movements almost completely bury the ligand; Lysine-93 (Saccharomyces cerevisiae OMPDC numbering) is anchored in a position that optimizes electrostatic interaction with
**tp** 中: 在羧酸反应位点以正确几何关系安置质子给体与静电稳定基团，同步完成过渡态电荷稳定化（含碳负离子特征）与质子递送，是高效脱羧的化学核心；该「电荷稳定 + 质子接力」头基活化逻辑在原理层可转译至羧酸头基化学
tp_en: Placing a proton donor and electrostatic-stabilizing groups at the carboxylate reaction site with the correct geometric relationship, so as to simultaneously achieve transition-state charge stabilization (including carbanion character) and proton del

--- 机制 2 ---
**name** 中: 催化效能定量基准与物理化学上限（proficiency）
name_en: Quantitative benchmark of catalytic proficiency and the physicochemical ceiling (proficiency)
**description** 中: OMPDC 是迄今报道催化效能最高的酶：乳清酸在中性水溶液、室温下自发脱羧半衰期约 7800 万年，OMPDC 将反应速率提高 10^17 倍，估算对过渡态（变化底物）的结合解离常数小于 5×10⁻²⁴ M；而不同底物对应的 proficient 酶反应 kcat/Km 被限制在仅约 600 倍的窄范围内，提示酶催化效能存在共同物理化学上限
description_en: OMPDC is the most catalytically proficient enzyme reported to date: orotate decarboxylates spontaneously in neutral aqueous solution at room temperature with a half-life of about 78 million years, OMPDC accelerates the reaction rate by 10^17-fold, and the estimated dissociation constant for the altered substrate (transition state) is less than 5x10^-24 M; meanwhile, the kcat/Km of proficient enzym
**tp** 中: 以速率增强因子与过渡态结合常数对「自发反应极慢 → 酶促极快」的定量锚定，为羧酸头基的活化与转化潜力提供可迁移评价框架：头基反应无催化时动力学障碍越大，预组织活性位点的催化设计空间越大；proficient 酶 kcat/Km 约 600 倍收敛的共同上限则提示，向非天然底物外推不可预设等效率
tp_en: The quantitative anchoring of extremely slow spontaneous reaction versus extremely fast enzymatic reaction via rate-enhancement factors and transition-state binding constants provides a transferable evaluation framework for the activation and transfo

## kcsa-potassium-channel-selectivity-filter（2 机制）
- organism_src: Streptomyces lividans（KcsA 钾离子通道，链霉菌源四聚体膜蛋白）
- organism_en : Streptomyces lividans (KcsA potassium channel, a Streptomyces-derived tetrameric membrane protein)

--- 机制 0 ---
**name** 中: 选择性过滤器主链羰基氧笼对脱水 K⁺ 的几何配位（脱水选择性核心机制）
name_en: Geometric coordination of dehydrated K+ by the main-chain carbonyl oxygen cage in the selectivity filter (core mechanism of dehydration selectivity)
**description** 中: KcsA 选择性过滤器以主链羰基氧原子围成的方反棱柱配位笼识别脱水 K⁺：羰基氧笼在每个 K⁺ 结合位点形成与水合水极为相似的方反棱柱配位，等效替代水合壳，使 K⁺ 在脱水后被几何与能量匹配地稳定配位
description_en: The KcsA selectivity filter recognizes dehydrated K+ through a square antiprism coordination cage formed by main-chain carbonyl oxygen atoms. The carbonyl oxygen cage forms a square antiprism coordination at each K+ binding site that closely resembles the hydrated shell of ligated water, effectively replacing the hydration shell, so that K+ is stably coordinated with geometric and energetic matchi
**tp** 中: 预组织、刚性且几何精确的配位笼可通过'先脱水、再以与水合水几何相似的配位替代水合壳'的方式，按尺寸与配位能匹配选择性识别目标离子
tp_en: A preorganized, rigid, and geometrically precise coordination cage can selectively recognize target ions by size and coordination-energy matching, through a strategy of first dehydrating the ion and then replacing the hydration shell with coordinatio

--- 机制 1 ---
**name** 中: 刚性预组织选择性过滤器按尺寸-脱水能区分 K⁺ 与 Na⁺（结构基础先例）
name_en: Size-dehydration-energy discrimination of K+ versus Na+ by the rigid preorganized selectivity filter (structural basis precedent)
**description** 中: KcsA 四聚体在孔外端托举一条仅约 12 Å 长的窄选择性过滤器，由签名序列主链羰基氧排列而成；该过滤器被结构约束保持张开，配位 K⁺ 但不配位更小的 Na⁺，是裸离子尺寸-脱水能选择性的经典结构生物学先例
description_en: The KcsA tetramer carries a narrow selectivity filter only about 12 Å long at the extracellular end of the pore, formed by the main-chain carbonyl oxygen atoms of the signature sequence. The filter is held open by structural constraints, coordinating K+ but not the smaller Na+, and serves as a classic structural biology precedent of naked-ion size-dehydration-energy selectivity.
**tp** 中: 刚性、由结构约束预组织张开的窄配位孔道可按离子尺寸与配位几何匹配区分目标离子与更小/失配离子，实现尺寸-脱水能选择
tp_en: A rigid, structurally constrained and preorganized narrow coordination pore can distinguish target ions from smaller or mismatched ions by ion size and coordination geometry matching, thereby achieving size-dehydration-energy selectivity.

## fcrn-ph-dependent-fc-recycling（2 机制）
- organism_src: Rattus norvegicus（大鼠新生 Fc 受体 FcRn/FCGRT，MHC I 类相关受体，与 β2-微球蛋白结合，识别 IgG Fc）
- organism_en : Rattus norvegicus (rat neonatal Fc receptor FcRn/FCGRT, MHC class I-related receptor that binds beta-2-microglobulin and recognizes the IgG Fc)

--- 机制 0 ---
**name** 中: 组氨酸质子化介导的 pH 门控可逆结合-释放（分子开关）
name_en: Histidine protonation-mediated pH-gated reversible binding-release (molecular switch)
**description** 中: FcRn 经其 α2 与 β2-微球蛋白结构域界面识别 IgG Fc 的 Cγ2-Cγ3 界面；该界面两侧分布可滴定组氨酸（IgG Fc His310、His433 位于 CH2-CH3 交界，FcRn 重链 His250、His251）。酸性内体（pH 6.0-6.5）下组氨酸质子化形成可滴定盐桥，高亲和结合 Fc；中性血液（pH 7.0-7.5）下去质子化、盐桥断裂，亲和力下降约两个数量级并释放 Fc，构成 pH 门控的结合-释放分子开关
description_en: FcRn recognizes the Cγ2-Cγ3 interface of the IgG Fc through the interface between its α2 and β2-microglobulin domains; titratable histidines flank this interface (IgG Fc His310 and His433 at the CH2-CH3 boundary, and FcRn heavy chain His250 and His251). Under acidic endosomal conditions (pH 6.0-6.5), histidine protonation forms titratable salt bridges that bind Fc with high affinity. At neutral bl
**tp** 中: 在识别界面布置 pKa 落于捕获 pH 与再生 pH 之间的可滴定基团（如组氨酸咪唑基），使其质子化态形成、去质子化态断裂与靶标的盐桥/氢键相互作用，即可用 pH 摆动可逆切换结合亲和力（约两个数量级），实现酸性结合、中性释放
tp_en: Place titratable groups (e.g., the histidine imidazole group) with pKa between the capture pH and the regeneration pH at the recognition interface, so that their protonated state forms and their deprotonated state disrupts salt bridge/hydrogen bond i

--- 机制 1 ---
**name** 中: 内体-循环 pH 双区室回收循环（吸附-再生循环原型）
name_en: Endosomal-circulatory pH two-compartment recycling loop (adsorption-regeneration cycle archetype)
**description** 中: FcRn 作为 β2-微球蛋白依赖性保护受体，在胞吞空泡（酸性）结合 IgG，将其重定向回循环、避免溶酶体分解代谢；饱和时未结合 IgG 进入溶酶体降解。酸性内体结合、中性血液释放的 pH 依赖门控驱动 IgG 回收循环并延长血清半衰期
description_en: As a β2-microglobulin-dependent protective receptor, FcRn binds IgG in acidic endocytic vacuoles, redirecting it back to circulation and sparing it from lysosomal catabolism; when saturated, unbound IgG enters lysosomes for degradation. This pH-dependent gating of acidic endosomal binding and neutral blood release drives the IgG recycling cycle and extends serum half-life.
**tp** 中: 以 pH 双区室（酸性捕获、中性释放）驱动受体反复结合-释放底物并将其从降解途径回收，可构成循环式吸附-再生操作：在捕获 pH 吸附靶标、在再生 pH 脱附回收吸附剂与靶标，循环再利用
tp_en: Driving a receptor to repeatedly bind and release a substrate and recover it from the degradation pathway using a pH two-compartment scheme (acidic capture, neutral release) constitutes a cyclic adsorption-regeneration operation: adsorb the target at

## lanmodulin-lanthanide-coordination（2 机制）
- organism_src: Methylorubrum extorquens AM1（lanmodulin, LanM；兼引 Hansschlegelia quercus LanM 同源蛋白）
- organism_en : Methylorubrum extorquens AM1 (lanmodulin, LanM; also citing the homologous Hansschlegelia quercus LanM protein)

--- 机制 0 ---
**name** 中: EF-hand 预组织羧酸配位几何对 Ln³⁺ 的选择性识别
name_en: Selective recognition of Ln3+ by preorganized EF-hand carboxylate coordination geometry
**description** 中: Lanmodulin（Methylorubrum extorquens AM1，117 残基，约 12.5 kDa，周质）含四个 EF-hand 基序，以高密度羧酸配体（Asp/Glu 侧链羧基与骨架羰基氧）预组织配位口袋结合 Ln3+/Y3+；Y3+ 复合物溶液 NMR 结构为 PDB 6MI5；结合耦合金属依赖的折叠构象变化，对 Ln3+ 与 Y3+ 相对 Ca2+ 的选择性达 10^8 倍，亲和力达皮摩尔级
description_en: Lanmodulin (Methylorubrum extorquens AM1, 117 residues, ~12.5 kDa, periplasmic) contains four EF-hand motifs and binds Ln3+/Y3+ through preorganized coordination pockets bearing high-density carboxylate ligands (Asp/Glu side-chain carboxyl groups and backbone carbonyl oxygens); the solution NMR structure of the Y3+ complex is PDB 6MI5. Binding is coupled to metal-dependent conformational changes i
**tp** 中: 与硬三价阳离子几何/静电互补的预组织高密度羧酸配位口袋（EF-hand 式），配合金属依赖折叠的构象预组织，可在水相实现皮摩尔级亲和与超高 Ln3+/Ca2+ 选择性
tp_en: A preorganized high-density carboxylate coordination pocket (EF-hand style) that is geometrically/electrostatically complementary to hard trivalent cations, combined with metal-dependent conformational preorganization during folding, can achieve pico

--- 机制 1 ---
**name** 中: 第二配位层羧酸位移对 Ln³⁺ 半径的读出与金属敏感二聚化
name_en: Readout of Ln3+ ionic radius via second-coordination-shell carboxylate shifts and metal-sensitive dimerization
**description** 中: Hansschlegelia quercus LanM（Hans-LanM）结合 Ln3+ 后形成二聚体，二聚强度对 Ln3+ 离子半径敏感（La3+ 诱导二聚体比 Dy3+ 诱导二聚体紧逾 100 倍）；X 射线结构（PDB 8FNS Nd3+、PDB 8DQ2 La3+，均于 pH 7 结合态测定）显示皮米级离子半径差异经配位层羧酸位移（carboxylate shift）重排第二配位层氢键网络而传递至四级结构；原型 Methylorubrum extorquens AM1 LanM 的 Nd3+ 结合结构为 PDB 8FNS
description_en: Hansschlegelia quercus LanM (Hans-LanM) forms a dimer upon binding Ln3+, and the dimer strength is sensitive to the Ln3+ ionic radius (La3+-induced dimers are over 100-fold tighter than Dy3+-induced dimers); X-ray structures (PDB 8FNS with Nd3+, PDB 8DQ2 with La3+, both determined in the bound state at pH 7) show that picometer-scale differences in ionic radius are transmitted to the quaternary st
**tp** 中: 细微几何差异（皮米级离子半径）可经第一配位层配位与第二配位层氢键网络读出并放大至寡聚态与宏观结合强度变化；耦合金属结合的 pH 依赖性，构成选择性可逆捕获的原理
tp_en: Subtle geometric differences (picometer-scale ionic radius) can be read out through first-coordination-shell coordination and the second-coordination-shell hydrogen-bond network, and amplified into changes in oligomeric state and macroscopic binding 

## errg-bpa-endocrine-receptor（2 机制）
- organism_src: Homo sapiens（人源雌激素相关受体 γ ERRγ, NR3B3）
- organism_en : Homo sapiens estrogen-related receptor gamma (ERRgamma, NR3B3)

--- 机制 0 ---
**name** 中: 双酚 A 的双酚羟基氢键锚定与狭长疏水口袋接触
name_en: Hydrogen-bond anchoring of the two bisphenol A phenolic hydroxyls and elongated hydrophobic pocket contacts
**description** 中: 人源 ERRγ LBD（PDB 2E2R，分辨率 1.60 Å，Rfree 0.197，chain A）结合 BPA（配体 2OH，即 4,4'-propane-2,2-diyldiphenol，chain A 残基 1401）：BPA 两个酚羟基中一个同时与 Glu275 和 Arg316 氢键，另一个与 Asn346 氢键，周围疏水接触（尤其 Tyr326）完成强结合；结合位点 AC1 含 11 个残基（Leu268、Ala272、Glu275、Met306、Leu309、Arg316、Tyr326、Leu345、Asn346、Ile349、Phe435）。异丙叉桥与两苯环占据狭长疏水口袋。残基编号与 UniProt P62508（ERR3_HUMAN，chain A 222-458）一一对应，无偏移
description_en: The human ERRgamma LBD (PDB 2E2R, 1.60 Å resolution, Rfree 0.197, chain A) binds BPA (ligand 2OH, i.e., 4,4'-propane-2,2-diyldiphenol, chain A residue 1401): of the two BPA phenolic hydroxyls, one forms hydrogen bonds simultaneously with Glu275 and Arg316 while the other hydrogen-bonds Asn346, and surrounding hydrophobic contacts (especially Tyr326) complete the strong binding. Binding site AC1 co
**tp** 中: 与两酚羟基几何互补的预组织成对极性锚（羧酸根/胍基型与酰胺型氢键基序）加上与双酚骨架形状互补的预组织疏水腔，可在无金属参与下方向性强结合双酚类分子
tp_en: A preorganized pair of polar anchors geometrically complementary to the two phenolic hydroxyls (carboxylate/guanidinium-type and amide-type hydrogen-bonding motifs) combined with a preorganized hydrophobic cavity complementary to the bisphenol backbo

--- 机制 1 ---
**name** 中: 组成型激活孤儿受体的预组织口袋与双酚骨架形状读出
name_en: Preorganized pocket and bisphenol-backbone shape readout of a constitutively active orphan receptor
**description** 中: ERRγ 是孤儿核受体（内源配体未知）与组成型转录激活因子；其 LBD 疏水口袋在 apo 形式即为预组织构象。BPA 结合受体腔而口袋内部结构与 apo 形式相比无任何改变，并维持激活螺旋（helix 12）活性构象从而保留组成型活性（Matsushima 2007 摘要），故 ERRγ 对 BPA 的识别以预组织口袋形状读出为主。亲和力与选择性具定量窗口：BPA 结合 ERRγ 的 IC50 为 13.1 nM（[3H]4-OHT 示踪竞争实验），4-壬基酚与己烯雌酚弱 5-50 倍（Takayanagi 2006 摘要）。对类似物 4-α-枯基酚报道有诱导契合结合成分（Matsushima 2008 BBRC），显示形状读出并非绝对刚性锁钥
description_en: ERRgamma is an orphan nuclear receptor (endogenous ligand unknown) and a constitutive transcriptional activator; its LBD hydrophobic pocket is preorganized in the apo form. Upon BPA binding to the receptor cavity, the internal pocket structure is unchanged relative to the apo form, and the active conformation of the activation helix (helix 12) is maintained, preserving constitutive activity (Matsu
**tp** 中: 组成型孤儿受体的预组织刚性口袋通过形状读出实现对特定双酚分子的高亲和识别；口袋预组织与腔形互补原则可独立于蛋白骨架移植到人工孔腔
tp_en: The preorganized rigid pocket of a constitutively active orphan receptor achieves high-affinity recognition of specific bisphenol molecules via shape readout; the principle of pocket preorganization and cavity-shape complementarity can be transplante

## sulfate-reducing-bacteria（1 机制）
- organism_src: Sulfate-Reducing Bacteria (SRB)
- organism_en : Sulfate-Reducing Bacteria (SRB)

--- 机制 0 ---
**name** 中: SRB硫酸盐还原三步酶促机理
name_en: Three-step enzymatic mechanism of sulfate reduction in SRB
**description** 中: SO₄²⁻ →(sat, ATP) APS →(APS还原酶, 2e⁻) SO₃²⁻ →(CBS, 6e⁻) H₂S；消耗大量H⁺→提升水体pH
description_en: SO₄²⁻ goes to APS via sat with ATP, then APS is reduced to SO₃²⁻ by APS reductase with 2e⁻, and finally SO₃²⁻ is reduced to H₂S via CBS with 6e⁻; the process consumes large amounts of H⁺, thereby raising the pH of the water body
**tp** 中: 利用微生物硫酸盐还原产生S²⁻进行金属硫化物沉淀，是厌氧条件下去除软酸金属的高效生物策略
tp_en: Using microbial sulfate reduction to generate S2- for metal sulfide precipitation is an efficient biological strategy for removing soft-acid heavy metals under anaerobic conditions.

## bird-feather-keratin（1 机制）
- organism_src: Aves (bird feathers)
- organism_en : Aves (bird feathers)

--- 机制 0 ---
**name** 中: 羽毛角蛋白巯基/氨基软酸重金属配位
name_en: Feather keratin thiol/amino coordination of soft-acid heavy metals
**description** 中: Keratin cysteine coordination: cysteine-rich keratin provides thiol (-SH) groups for heavy metal coordination, especially for soft metals like Hg²⁺, Ag⁺, Pb²⁺
description_en: Keratin cysteine coordination: cysteine-rich keratin provides thiol (-SH) groups for heavy metal coordination, especially for soft metals like Hg2+, Ag+, Pb2+
**tp** 中: Keratin cysteine thiol groups provide high-affinity binding for soft heavy metals
tp_en: Keratin cysteine thiol groups provide high-affinity binding for soft heavy metals

## mammalian-lung-murray-law-branching（2 机制）
- organism_src: Homo sapiens（哺乳动物肺支气管树；Weibel 人肺形态测量）
- organism_en : Homo sapiens (mammalian lung bronchial tree; Weibel human lung morphometry)

--- 机制 0 ---
**name** 中: Murray 律立方递减分级传质网络（最小功原理）
name_en: Murray-law cubic-decrement hierarchical mass-transfer network (minimum-work principle)
**description** 中: 哺乳动物肺支气管树以对称二叉分支将主干逐级细分为约 3 亿末端交换单元，分支半径按 Murray 律（平均流量正比于半径立方）递减；该几何源自 Murray 1926 最小功原理——在泵送功耗与代谢/血液体积代价间取最小总代价，使分支管网逼近全局最优、逐级维持恒定单位输运代价，是长程低驱动力输运的几何最优模板
description_en: The mammalian lung bronchial tree successively subdivides the main trunk into about 300 million terminal exchange units through symmetric dichotomous branching, with branch radii decreasing according to Murray's law (mean flow proportional to the cube of the radius). This geometry originates from the Murray 1926 minimum-work principle, which minimizes the total cost between pumping work and metabo
**tp** 中: 对称二叉分支管网中，令分支半径立方正比于流量（Murray 律），可在逐级保持恒定单位输运代价的同时，以最小构造-维持代价将流体分配至广布传质末端，是长程低驱动力输运的几何最优模板
tp_en: In a symmetric dichotomous branching network, making the cube of the branch radius proportional to flow (Murray's law) distributes fluid to widely distributed mass-transfer terminals at minimum construction-maintenance cost while maintaining a consta

--- 机制 1 ---
**name** 中: 人肺约 23 级对称二叉分支至约 3 亿肺泡末端的形态测量几何
name_en: Morphometric geometry of the human lung with about 23 generations of symmetric dichotomous branching to about 300 million alveolar terminals
**description** 中: Weibel 人肺形态测量（1962/1963）确立：气道平均约 23 级对称二叉分支，终止于约 3 亿肺泡（配约 1400 万肺泡管、约 2800 亿毛细血管段），逐级气道与血管直径遵循'最优'尺寸，交换面积约 40-80 m²；该形态测量是 Murray 律分支几何在哺乳动物肺的器官级实例
description_en: Weibel's human lung morphometry (1962/1963) established that the airways undergo about 23 generations of symmetric dichotomous branching on average, terminating in about 300 million alveoli (with about 14 million alveolar ducts and about 280 billion capillary segments); the diameters of airways and vessels at successive levels follow 'optimal' sizes, and the exchange area is about 40-80 m2. This m
**tp** 中: 约 23 级对称二叉分支将单一主干逐级细分为约 3 亿末端交换单元，逐级直径遵循最优尺寸，在巨大交换面积与低驱动力间取得平衡，为分级孔道吸附床提供级数-径缩-末端面积的几何标度参照
tp_en: About 23 generations of symmetric dichotomous branching successively subdivide a single trunk into about 300 million terminal exchange units, with diameters at each level following optimal sizes and balancing a huge exchange area against a low drivin

## magnetic-bacteria（1 机制）
- organism_src: Magnetotactic bacteria (MTB)
- organism_en : Magnetotactic bacteria (MTB)

--- 机制 0 ---
**name** 中: 磁小体磁分离吸附
name_en: Magnetosome magnetic separation and adsorption
**description** 中: 磁性细菌的磁小体（Fe₃O₄ 纳米颗粒）提供磁分离能力，细菌表面官能团提供吸附位点
description_en: The magnetosomes of magnetotactic bacteria (Fe3O4 nanoparticles) provide magnetic separation capability. Functional groups on the bacterial surface provide adsorption sites.
**tp** 中: 磁性细菌磁小体提供磁分离 + 细菌表面官能团吸附（placeholder）
tp_en: Magnetosomes of magnetotactic bacteria provide magnetic separation, and functional groups on the bacterial surface provide adsorption (placeholder).

## psts-phosphate-binding-protein（2 机制）
- organism_src: Escherichia coli（PstS 磷酸盐结合蛋白）
- organism_en : Escherichia coli (PstS phosphate-binding protein)

--- 机制 0 ---
**name** 中: 预组织氢键给体阵列对四面体磷酸根的几何识别
name_en: Geometric recognition of tetrahedral phosphate by a preorganized hydrogen-bond donor array
**description** 中: 大肠杆菌 PstS/PBP 以预组织中性氢键给体阵列（Thr10、Ser38、Ser139 侧链羟基与骨架酰胺 NH，Asp56 起关键定位作用）识别四面体磷酸根 PO4；磷酸根埋藏于两结构域间裂隙，无金属离子直接配位氧阴离子（PDB 1PBP 非水配体仅 PO4）。1PBP 为 T141D 定点突变体，沉积记录第 141 位为工程化 Asp141，野生型该位为 Thr141
description_en: Escherichia coli PstS/PBP recognizes the tetrahedral phosphate anion PO4 via a preorganized array of neutral hydrogen-bond donors, including the side-chain hydroxyls of Thr10, Ser38, and Ser139 and backbone amide NH groups, with Asp56 playing a key positioning role. The phosphate is buried in the cleft between the two domains, and no metal ion directly coordinates the oxyanion (in PDB 1PBP, PO4 is
**tp** 中: 预组织且与四面体氧阴离子几何互补的中性氢键给体阵列，配合埋藏低介电结构域裂隙，可在无金属或阳离子参与下通过方向性与几何匹配选择性识别该氧阴离子头基；给体阵列的电荷/质子化状态可微调对底物质子化形态的识别
tp_en: A preorganized array of neutral hydrogen-bond donors that is geometrically complementary to a tetrahedral oxyanion, combined with a buried low-dielectric domain cleft, can selectively recognize the oxyanion head group through directional and geometri

--- 机制 1 ---
**name** 中: 四面体磷酸根识别的跨物种保守（原理先例）
name_en: Cross-species conservation of tetrahedral phosphate recognition (principle precedent)
**description** 中: 产气荚膜梭菌磷酸盐结合蛋白 PBP-1 以保守 Ser/Thr 氢键给体阵列识别四面体磷酸根（PDB 4Q8R SITE AC1：Ser11、Thr12、Ser13、Ser41、Ser59、Ser129 等），与大肠杆菌 PBP 几何保守，为预组织氢键给体阵列识别四面体氧阴离子在 PstS/PBP 家族内保守提供结构生物学先例
description_en: The phosphate-binding protein PBP-1 from Clostridium perfringens recognizes tetrahedral phosphate via a conserved Ser/Thr hydrogen-bond donor array (PDB 4Q8R SITE AC1: Ser11, Thr12, Ser13, Ser41, Ser59, Ser129, etc.) and is geometrically conserved with the Escherichia coli PBP. This provides a structural-biology precedent for the conservation of preorganized hydrogen-bond donor array recognition o
**tp** 中: 预组织中性氢键给体阵列选择性识别四面体氧阴离子的原理在周质磷酸盐结合蛋白家族内保守，可脱离特定蛋白骨架移植
tp_en: The principle that a preorganized neutral hydrogen-bond donor array selectively recognizes tetrahedral oxyanions is conserved within the periplasmic phosphate-binding protein family, and can be transplanted independently of a specific protein scaffol