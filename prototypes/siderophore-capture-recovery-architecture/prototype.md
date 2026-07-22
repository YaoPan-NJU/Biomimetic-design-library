---
id: siderophore-capture-recovery-architecture
name: 铁载体两相高亲和捕获-受体回收架构（Siderophore Two-Phase High-Affinity Capture and Receptor-Mediated Recovery Architecture）
category: 微生物
organism: Escherichia coli（铁载体系统：肠杆菌素/ferrichrome 型；周质铁载体结合蛋白 FhuD（1EFD）与 FepB（3TLK））
biomimetic_dimension: 系统仿生
features:
  - 特异性识别
  - 传质强化
adsorption_mechanisms:
  - 分泌型铁载体对超低浓度三价铁的高亲和螯合捕获（捕获级）
  - 专一受体/周质结合蛋白介导的铁载体-铁复合物回收与再生（回收级）
applicability:
  pH_range: null
  temp_range: null
  salinity: null
evidence_level: low
# provenance: 2 papers, 10 verified, 0 unverified
# coverage: partial
# status: active
---
# 铁载体两相高亲和捕获-受体回收架构（Siderophore Two-Phase High-Affinity Capture and Receptor-Mediated Recovery Architecture）

## 1. 生物原型简介

**问题定义**：铁为多数细菌与真菌必需元素，但在有氧、近中性 pH 水中 Fe3+ 溶解度极低，游离 Fe3+ 活度常低至 fM 级。微生物须在超低浓度、并与大量竞争离子共存的水环境中高效捕获铁并加以回收。铁载体系统正是自然界对「超低浓度底物的高效捕获-回收」这一传质难题的架构方案。

**生物策略**：微生物铁载体系统采两级架构。捕获级：合成并分泌高亲和铁载体（如大肠杆菌肠杆菌素 enterobactin，三邻苯二酚型；ferrichrome/gallichrome，羟肟酸型），以多齿螯合 Fe3+ 形成铁载体-铁复合物，将超低浓度铁扫集浓缩（Loomis 1991 测定肠杆菌素与金属-肠杆菌素复合物的溶液平衡；Miethke 2007 摘要指出高亲和铁获取由铁载体依赖途径介导）。回收级：铁载体-铁复合物被外膜专一受体（FhuA 识别 ferrichrome 类、FepA 识别肠杆菌素）识别，经周质结合蛋白（FhuD/FepB）转运回收，随后铁被释放、铁载体循环再利用（PDB 1EFD：周质铁载体结合蛋白 FhuD 与 gallichrome 复合物，Nat Struct Biol 2000 p.287；PDB 3TLK：holo FepB 结合铁-肠杆菌素，关键词记 'siderophore transport'；Miethke 2007 摘要述及铁载体递送的铁摄取与其释放）。

## 2. 吸附机制详解

### 机制1：分泌型铁载体对超低浓度三价铁的高亲和螯合捕获（捕获级）

**描述**：微生物合成并分泌高亲和铁载体（如大肠杆菌肠杆菌素 enterobactin，三邻苯二酚型；ferrichrome/gallichrome，羟肟酸型），以多齿螯合剂在体相水中螯合超低浓度（fM 级）三价铁 Fe3+，形成铁载体-铁复合物并将铁扫集浓缩。PDB 3TLK 中 FepB 与 Fe(III) 及肠杆菌素共结晶，直接显示该捕获化学的对象为阳离子三价铁
**关键官能团**：['多齿螯合基团（enterobactin 邻苯二酚 / gallichrome 羟肟酸的 Fe3+ 配位基团）', '铁载体-铁螯合腔']
**来源**：DOI 10.1128/MMBR.00012-07

### 机制2：专一受体/周质结合蛋白介导的铁载体-铁复合物回收与再生（回收级）

**描述**：铁载体-铁复合物经外膜专一受体（FhuA 识别 ferrichrome 类、FepA 识别肠杆菌素）识别，由周质铁载体结合蛋白（FhuD/FepB）转运回收；回收对完整铁载体-铁复合物（holo/载附形式）具选择性，随后铁被释放、铁载体循环再利用。PDB 1EFD 为 FhuD 与 gallichrome 复合物，PDB 3TLK 为 holo FepB（结合铁-肠杆菌素）
**关键官能团**：['周质结合蛋白底物结合腔（FhuD/FepB 两结构域间裂隙）', 'holo（载附）构象识别界面']
**来源**：DOI 10.1128/MMBR.00012-07

## 3. 结构特征与结构-功能关系

必须保留：① 可分泌/可分散且可回收的高亲和捕获单元（在体相扫集超低浓度底物，消除向固定表面的扩散限制）；② 对「已载附底物的捕获单元」具选择性的专一回收界面（识别 holo/载附形式）；③ 捕获-回收两级解耦 + 捕获单元再生循环。可灵活调整：捕获单元的结合化学（须按目标底物独立设计）、载体形态（胶体/纳米/可溶）、回收级实现方式（膜/磁分离/捕获柱）、再生触发条件（pH/离子强度/竞争洗脱）。

## 4. 已报道性能数据

[待补充]

## 5. 适用场景

**约束条件**：
- 可溶周质蛋白形态: FhuD 约 29.7 kDa（1EFD 实体 1，29.68 kDa）、FepB 约 35.4 kDa（3TLK 实体 1，35.385 kDa），均为周质可溶结合蛋白；天然回收经跨膜受体与能量偶联，人工转译须以固载界面/分离级重建 None
- holo（载附）形式识别依赖: 回收级识别完整铁载体-铁复合物（holo 形式，3TLK 'holo FepB'）；游离铁或空载铁载体不被同等回收，固定化或界面重建须保留对载附形式的选择性 None
- 两级须闭环且捕获单元可再生: 架构传质优势依赖捕获单元回收完全且可再生循环、回收级对其选择性高于共存杂质，否则回收损耗与二次泄漏抵消捕获增益（定性） None

## 6. 相关原型

- asbt-bile-acid-elevator-transporter
- chlorophenol-hydroxylase-regioselective
- ddt-dehydrochlorinase-gst
- decarboxylase-carbanion-activation
- fcrn-ph-dependent-fc-recycling

## 参考文献

[待补充]
