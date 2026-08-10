# BMDL 英文标量字段补全 — Dry-run 预览

> 生成时间：2026-08-10 | 范围：102 原型 / 632 机制 | 方式：Claude 直接翻译（未调用 DashScope API）

## 1. 总体统计

| 英文字段 | 新增数 | 说明 |
|---|---|---|
| `organism.scientific_en` | 102/102 | 英文物种名 |
| `mechanism.name_en` | 632/632 | 英文机制名 |
| `mechanism.description_en` | 625/632 | 英文机制描述（7 个源为空→空串） |
| `causal_chain.transferable_principle_en` | 632/632 | 英文可转译原理 |

**合计新增英文字段：1991 处**（纯新增，不改动任何既有字段）

## 2. 质量检查结果

- 机制数与源文件完全对齐（632/632），`idx` 数组下标连续一致
- 无中文字符、无全角标点残留（正则全量扫描）
- 源字段为空 → 英文输出空串（7 个 description）
- 源字段非空 → 英文输出非空
- 忠实翻译：保留 PDB ID、基因名、物种学名、化学式、数字、单位、文献引用
- 源字段本身已是英文的按忠实原则原样保留：organism 34 个、name 16 个、description 67 个、tp 10 个

## 3. 预期改动范围（surgical）

- 每个原型仅新增 4 类 `*_en` 键，紧邻对应中文源键之后
- 已验证：文本级插入，`git diff` **只有新增行，0 行删改**（不格式化、不重排）
- 不触碰：`mechanisms` 顺序、`causal_chain` 其他要素、`boundary_rules`、`narrative`、`honesty_ledger` 等一切既有内容

## 4. 抽查翻译示例（中英对照）

### oat4-organic-anion-transporter（3 机制）

- **organism** → `Homo sapiens OAT4 organic anion transporter`

**机制 0**：
- name 中：`阴离子头基与芳香-阳离子底物口袋的两点位识别（硫酸结合型有机阴离子）`
- name_en：`Two-point recognition of anionic head group by an aromatic-cationic substrate pocket (sulfate-conjugated organic anions)`
- description 中：人 OAT4（SLC22A11，550 氨基酸残基、12 跨膜域）表达于肾近端小管顶端膜与胎盘，以高亲和力、钠离子非依赖方式转运硫酸结合型有机阴离子：雌酮硫酸酯 E1S（Km 1.01 µM）与硫酸脱氢表雄酮 DHEAS（Km 0.63 µ...
- description_en：Human OAT4 (SLC22A11; 550 amino acid residues, 12 transmembrane domains), expressed on the apical membrane of renal proximal tubule cells and in placenta, trans...
- tp 中：阳离子/极性头基锚加芳香-疏水骨架笼的两点位识别构型，可以钠离子非依赖方式识别化学结构多样的阴离子分子；头基化学（硫酸结合物优先于葡萄糖醛酸结合物）与阴离子电荷是选择性的关键决定因素
- tp_en：A two-point recognition configuration of a cationic/polar head-group anchor plus an aromatic-hydrophobic scaffold cage can recogni...

### polydopamine-coating（35 机制）

- **organism** → `Mytilus edulis (blue mussel)`

**机制 0**：
- name 中：`聚多巴胺儿茶酚/胺基多价协同表面黏附`
- name_en：`Polydopamine catechol/amino multivalent synergistic surface adhesion`
- description 中：疏水材料减少细菌黏附+抗菌材料主动杀菌，实现长效抗菌
- description_en：Hydrophobic materials reduce bacterial adhesion, while antibacterial materials actively kill bacteria, achieving long-lasting antibacterial performance.
- tp 中：基于机制: 超疏水抗菌表面'双重保险'原理
- tp_en：Based on the mechanism: the 'double insurance' principle of superhydrophobic antibacterial surfaces.

### water-strider-leg（52 机制）

- **organism** → `Gerridae (water striders)`

**机制 0**：
- name 中：`水黾腿微纳刚毛疏水蜡质层气垫超疏水承载`
- name_en：`Superhydrophobic load-bearing of water strider legs via micro/nano setae, hydrophobic waxy layer, and air cushion`
- description 中：超疏水材料是指水的接触角超过150°，滞后角低于10°的表面材料
- description_en：Superhydrophobic materials are surface materials on which the water contact angle exceeds 150 degrees and the contact angle hysteresis is below 10 degrees.
- tp 中：水黾腿微纳刚毛+疏水蜡质层
- tp_en：Micro/nano setae on water strider legs combined with a hydrophobic waxy layer.

### bone-structure（4 机制）

- **organism** → `Mammalian bone`

**机制 0**：
- name 中：`骨羟基磷灰石钙离子交换与表面配位`
- name_en：`Calcium ion exchange and surface coordination of bone hydroxyapatite`
- description 中：壳聚糖/HAp纳米纤维膜(静电纺丝)：Pb(II) 296.7 mg/g、Co(II) 180.2 mg/g、Ni(II) 213.8 mg/g，5次循环无明显下降；HAp/PU复合泡沫(50%HAp)：Pb(II) 150 mg/g；nH...
- description_en：Chitosan/HAp nanofiber membranes (electrospinning) achieved Pb(II) 296.7 mg/g, Co(II) 180.2 mg/g, and Ni(II) 213.8 mg/g, with no significant decline over 5 cycl...
- tp 中：基于机制: HAp膜重金属去除性能
- tp_en：Based on the mechanism: heavy metal removal performance of HAp membranes.

### beta-cyclodextrin-hostguest-inclusion（1 机制）

- **organism** → `Cyclodextrin: a naturally occurring cyclic oligosaccharide formed by enzymatic cyclization of amylose (a plant polysaccharide of α-D-glucopyranose units linked α-1,4) by bacterial CGTase; β-CD is a macrocycle of 7 glucose units with a hydrophobic inner cavity and a hydrophilic outer rim`

**机制 0**：
- name 中：`β-环糊精疏水内腔的主客体包结识别`
- name_en：`Host-guest inclusion recognition by the hydrophobic inner cavity of β-cyclodextrin`
- description 中：β-环糊精由 7 个 α-D-葡萄糖以 α-1,4 连接成锥筒，外缘羟基亲水、内腔疏水；水相中经疏水效应与范德华/尺寸互补将芳香或疏水客体（如双酚 A、氯酚、多环麝香、紫外过滤剂等）包结进内腔形成 1:1（或 2:1）主客体复合物，客体自体...
- description_en：β-Cyclodextrin is a truncated cone formed by 7 α-D-glucose units linked via α-1,4 bonds, with a hydrophilic outer rim of hydroxyls and a hydrophobic inner cavit...
- tp 中：两亲环状寡糖以疏水内腔 + 尺寸/形状互补包结疏水芳香客体；交联为多孔聚合物即得快速、可再生、耐基质的广谱微污染物吸附材料；选择性上限受 1:1 容量与广谱疏水包结约束。
- tp_en：An amphiphilic cyclic oligosaccharide includes hydrophobic aromatic guests via its hydrophobic cavity plus size/shape complementar...

### bacterial-cellulose（2 机制）

- **organism** → `Acetobacter xylinum`

**机制 0**：
- name 中：`细菌纤维素纳米纤维网物理筛分与表面羟基吸附`
- name_en：`Physical sieving by bacterial cellulose nanofiber network and surface hydroxyl adsorption`
- description 中：3D nanofiber network: BC ultrafine nanofibers (10-100 nm) form interconnected porous structure acting as ideal barrier m...
- description_en：3D nanofiber network: BC ultrafine nanofibers (10-100 nm) form interconnected porous structure acting as ideal barrier matrix, allowing water molecules to pass ...
- tp 中：3D nanofiber network from microbial fermentation provides hierarchical porous structure for filtrati...
- tp_en：3D nanofiber network from microbial fermentation provides hierarchical porous structure for filtration and adsorption
