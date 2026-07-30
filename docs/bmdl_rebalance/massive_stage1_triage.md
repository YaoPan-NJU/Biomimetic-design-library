# Massive Stage 1 — 19 个不可达原型 Triage 与接线提案

**日期：** 2026-07-29
**分支：** `massive`（基于 `expand`）
**目的：** 修复"保存粒度不统一"——prototype JSON 已完整但从未生成映射包，导致 `query()` 加载 89 个却 19 个永远匹配不到。

---

## 一、分类总览（19 个）

| # | 原型 | 类别 | 接地强度 | 归类 | 处置 |
|---|------|------|----------|------|------|
| 1 | moda-oxyanion-geometric-recognition | 微生物/分子仿生 | from_source(钼酸根/硫酸根 PDB) | G1 接线 | 天然氧阴离子→lead；PFBS→exploratory |
| 2 | fabp4-fatty-acid-pfas-binding | 动物/分子仿生 | verified(PDB 9MIW 直接 PFOA 结合) | G1 接线 | PFOA→exploratory(结合非吸附) |
| 3 | hl-fabp-liver-fatty-acid-pfas-binding | 动物/分子仿生 | needs_review(PFOA/PFNA 结合) | G1 接线 | PFOA/PFOS→exploratory |
| 4 | cell-membrane-ion-channel | 仿生材料/功能仿生 | from_source/partial, 14 perf | G1 接线 | 分子筛分/离子选择→lead |
| 5 | plant-lignocellulosic-architecture | 植物 | partial, 12 perf(BPA/PFOA/Cd) | G1 接线 | BPA/PFOA/Cd→lead(与旧 match_weights 一致) |
| 6 | scallop-shell | 动物/过程仿生 | partial(CaCO₃,类牡蛎) | G1 接线 | Pb/Cu/Cd/PO₄→lead |
| 7 | rice-husk-phytolith | 植物 | partial(硅醇基) | G1 接线 | 重金属/PO₄→exploratory |
| 8 | bird-feather-keratin | 动物 | llm_inferred(无源) | G2 弱接线 | 软酸金属(Hg/Pb)→exploratory≤0.3 |
| 9 | fungal-biosorption | 真菌 | llm_inferred | G2 弱接线 | 重金属→exploratory≤0.3 |
| 10 | insect-chitin | 动物 | llm_inferred(几丁质) | G2 弱接线 | 重金属/染料→exploratory≤0.3 |
| 11 | microbial-exopolysaccharide | 微生物 | llm_inferred | G2 弱接线 | 重金属/阳离子染料→exploratory≤0.3 |
| 12 | spider-silk | 节肢动物/结构仿生 | partial(嵌合污染) | G4 谨慎接线 | 仅 Cd/Cr(VI)/Cu/Pb 干净机制→exploratory；标注嵌合待清理 |
| 13 | cactus-spine | 形态仿生 | unverified(集雾/Janus) | G3 背景 | 仅 use_case 超疏水/集水；不进吸附 |
| 14 | namib-beetle | 动物/结构仿生 | partial(集雾) | G3 背景 | 仅 use_case 集水/超疏水 |
| 15 | plant-wax-cuticle | 植物/超疏水 | llm_inferred(超疏水) | G3 背景 | 仅 use_case 超疏水/油水；不进吸附 |
| 16 | biomineralization-template | 仿生材料 | placeholder/needs_literature | G5 延后 | 占位符，query 已过滤；留 Track 2 |
| 17 | coral-skeleton | 动物 | placeholder | G5 延后 | 占位符；留 Track 2 |
| 18 | dna-aptamer | 仿生材料 | placeholder/needs_literature | G5 延后 | 占位符；留 Track 2 |
| 19 | mycelium | 微生物 | placeholder/needs_literature | G5 延后 | 占位符；留 Track 2 |

**统计：** G1 接线 7 + G2 弱接线 4 + G3 背景 3 + G4 谨慎 1 = **15 个接线**；G5 占位符延后 4 个（正确地不接线，query 本就过滤 placeholder）。

---

## 二、接线提案（Proponent 提案，待 Skeptic 对抗核验）

> 权重规则：exploratory/无源 ≤0.3；non-direct lead ≤0.5；有真实吸附容量数据方可 lead/direct。有机污染物即使给权重，query() 有机域门控仍会强制 lane=exploratory（honesty 由引擎计算，map 权重仅作排序信号）。

### G1（source-grounded）
- **moda** → `硫酸根`/`SO4²⁻`(几何天然近似, lead 0.5)、`PO43-`(四面体氧阴离子类比, exploratory 0.35)、`PFBS`(磺酸头基类比, exploratory 0.3)；feature_matching_rules: 新增"氧阴离子几何识别"接口。
- **fabp4** → `PFOA`(exploratory 0.5, 有 PDB 直接结合但非吸附)、`PFOS/PFAS`(exploratory 0.35)；接入"氟碳链"修正。
- **hl-fabp** → `PFOA`/`PFOS`(exploratory 0.3)；接入"氟碳链"修正。
- **cell-membrane-ion-channel** → feature `分子筛分`(lead 0.5)、interaction `离子交换`/`孔道限域`；`壬基酚`(perf 支撑, exploratory)。
- **plant-lignocellulosic-architecture** → `BPA`(lead 0.6)、`PFOA`(lead 0.6)、`Cd(II)`(lead 0.5)——补齐与旧 match_weights 的一致性；带 biochar/AC scope caveat。
- **scallop-shell** → `Pb(II)`/`Cu(II)`(lead 0.5)、`Cd(II)`(exploratory 0.4)、`PO43-`(exploratory 0.3)。
- **rice-husk-phytolith** → 重金属(exploratory 0.35)、`PO43-`(exploratory 0.3)。

### G2（llm_inferred 生物吸附族，全 exploratory ≤0.3）
- **bird-feather-keratin** → 软酸金属 `Hg(II)`/`Pb(II)`(0.3)；interaction 软酸配位。
- **fungal-biosorption** / **insect-chitin** / **microbial-exopolysaccharide** → `重金属`类(0.3)；insect-chitin/exopolysaccharide 另接阳离子染料(0.3)。

### G3（背景/表面物理，仅 use_case，不进吸附匹配）
- **cactus-spine** / **namib-beetle** / **plant-wax-cuticle** → `use_case_to_prototype` 的 `超疏水`/`油水分离`/`集水`；显式 background 标注。

### G4（嵌合谨慎）
- **spider-silk** → 仅接干净重金属机制 `Cr(VI)`/`Cd(II)`/`Cu(II)`/`Pb(II)`(exploratory 0.3)；标注"含超疏水/油水/集雾嵌合，Track 2 清理"。

### 氟碳链误指修正（feature_matching_rules `molecular_feature_to_prototype.氟碳链`）
- 现指 `lotus-leaf`/`superhydrophobic-artificial`(超疏水,与 PFAS 分子识别无关)。
- 改为：主指 `hsa-`/`fabp4-`/`ntcp-`/`hl-fabp-`(PFAS 分子识别蛋白)，超疏水降权或移出。

---

## 三、待 Skeptic 联网核验的高风险主张
1. fabp4→PFOA：DOI 10.1021/jacsau.5c00504 / PDB 9MIW 是否真实存在且为 FABP4-PFOA 直接结合？
2. moda 氧阴离子识别（钼酸根/硫酸根）作为 PFBS 磺酸头基识别脚手架——几何类比是否成立还是过度外推？
3. plant-lignocellulosic BPA/PFOA 容量的合法性（stage7 声称 PDF 验证）。
4. 全表跨污染物误配审计：不得重蹈姊妹项目点名的 4 类错误（PFOA 画"芳香环"、磷酸根错配 As(III)、As(III) 错配丝素、染料/Cr→有机物迁移）。
