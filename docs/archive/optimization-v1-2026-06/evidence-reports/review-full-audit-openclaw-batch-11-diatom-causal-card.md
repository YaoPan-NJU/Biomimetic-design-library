status: ready_for_codex_acceptance
worker: OpenClaw/xiaomi-mimo-v2.5
completed_at: 2026-06-17 13:35:45 CST

---

# Batch 11 — Diatom Frustule Causal Card Audit & Proposal

## 1. Current-State Audit & Target Field Path

### Current JSON state

`prototypes_db/diatom-frustule.json` has **10 mechanisms**, **none** with a qualified `causal_chain` card. All mechanisms have `verification: "needs_review"` and no `causal_chain` field. The prototype also lacks boundary conditions.

**Boundary rules present:**
- `B09-DIAT-002`: "Duplicate rows inflate evidence coverage. Do not count as independent evidence."
- `B09-DIAT-005`: "Arachnoidiscus wheel-hub paper is structural-mechanics biomimicry, not water-treatment adsorption."

### Target field path

**Mechanism index 0: "CA/DE缩合机理"** — This is the strongest surviving source-specific mechanism. It corresponds to the Du et al. 2021 paper (DOI: 10.11862/CJIC.2021.025) and describes a concrete, experimentally verified surface modification and adsorption mechanism for modified diatomite removing heavy metals.

**Proposed location:** `mechanisms[0].causal_chain` (replacing the current empty structure)

**Rationale:** This mechanism has the highest evidence density — XPS characterization, pH-effect studies, FTIR confirmation, and explicit maximum adsorption capacity data. It is source-specific (not generic) and directly addresses the prototype's core claim (modified diatomite adsorption).

---

## 2. Source-by-Source Evidence Table

| # | Source PDF | Locator | Verbatim Quote | Supports |
|---|-----------|---------|----------------|----------|
| 1 | `仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf` | p.1, Abstract | "以APTES、CA制备的氨基/羧基缩合修饰硅藻土吸附剂对Pb²⁺、Cd²⁺最大吸附容量分别为485、462 mg·g⁻¹" | `bio_structure`: modified diatomite with –NH₂/–COOH functional groups; `pollutant_feature`: Pb²⁺/Cd²⁺ heavy metal cations |
| 2 | Same PDF | p.5, §2.5 | "MPTS醇解形成Si—OH，与硅藻土表面的Si—OH发生脱水缩合反应…进而接枝于硅藻土表面，而带有巯基末端暴露分子末端，起到吸附重金属离子的目的" | `interaction`: Si–OH condensation grafting + terminal –SH/–NH₂/–COOH coordination with metal ions |
| 3 | Same PDF | p.5, §2.5 | "APTES醇解形成Si—OH，与硅藻土表面的Si—OH发生脱水缩合反应，接枝于硅藻土表面，带有氨基末端的APTES暴露在外表面，与CA表面的—COOH、—OH基团进行缩合" | `bio_structure` (mechanism): two-step silane condensation → amino/carboxyl surface functionalization |
| 4 | Same PDF | p.6, §2.6.1 | "当离子初始浓度较小时，吸附剂表面—SH、—OH、—COOH、—NH₂/—COOH等活性官能团含量相对过剩，对溶液中重金属离子的配位作用明显" | `interaction`: coordination between surface functional groups and metal cations |
| 5 | Same PDF | p.7, §2.6.1 | "样品MP/DE和CA/DE对Pb²⁺、Cd²⁺的最大吸附容量分别为396、365 mg·g⁻¹和485、462 mg·g⁻¹" | Performance verification of mechanism effectiveness |
| 6 | Same PDF | p.7, §2.6.2 | "当pH值增大至6~8时，样品MP/DE对Pb²⁺、Cd²⁺的最大去除率分别为100%、99.8%，样品CA/DE对Pb²⁺、Cd²⁺的最大去除率分别为100%、98.5%" | `boundary_conditions`: optimal pH range 6–8 |
| 7 | Same PDF | p.7, §2.6.2 | "在pH≤3的条件下，样品对Pb²⁺、Cd²⁺离子去除率较低" | `boundary_conditions`: pH ≤ 3 suppresses adsorption |
| 8 | Same PDF | p.7, §2.6.2 | "当溶液pH>9时，溶液中将产生大量的OH⁻，会与Pb²⁺、Cd²⁺离子逐渐生成Pb(OH)₂、Cd(OH)₂沉淀，形成假吸附" | `boundary_conditions`: pH > 9 causes precipitation (false adsorption) |
| 9 | Same PDF | p.7, §2.7 | "CA/DE样品对于Pb²⁺的吸附存在—NH₂、—COO⁻与Pb²⁺的配位键、化学键的形成…该吸附过程以化学吸附为主" | `why_it_works`: chelation/coordination is the dominant mechanism; `interaction` confirmed by XPS |
| 10 | Same PDF | p.7, §2.7 | "—NH—信号峰减弱，表明N失电子或孤对电子被共用，在406.73 eV处形成一个新的信号峰，为RNH₂-Mn⁺配位键的特征信号峰" | XPS evidence for coordination bonding (verification anchor) |
| 11 | `仿生文献库/3rd/第C组-零数据原型/C1 - 仿硅藻多孔材料（4 篇）/2024-Qin-diatomite-heavy-metal-adsorption.pdf` | p.5, §4.1 | "波数为3 451 cm⁻¹的特征吸收峰波数发生了变化，这说明了改性硅藻土中的O-H键参与了铅离子的吸附过程" | Corroborates Si–OH role in Pb²⁺ adsorption (second source) |
| 12 | Same PDF (Qin 2024) | p.1, Abstract | "改性硅藻土掺量为4 g/L、吸附时间为40 min、温度设置为30℃，pH值设定为5，初始浓度均设定为200 mg/L时，改性硅藻土的吸附效果达到较佳" | Boundary conditions (operational parameters) from independent source |
| 13 | `仿生文献库/论文/第3组-多孔结构/2022-Roychoudhury-diatom-biosilica-porous-shell-review 2.pdf` | p.12, §3 | "diatoms have been utilized to develop diverse methods such as biotransformation, biomineralization, bioaccumulation, and biosorption… the frustule, or silica cell wall, is a tough layer composed of amorphous silica adorned with nano- to micro-sized pores" | `bio_structure`: biological frustule architecture (hierarchical porous SiO₂) |
| 14 | Same PDF (Roychoudhury 2022) | p.14, §3.3 | "chemically modified diatom-based biosilica microparticles with self-assembled monolayers of 3-mercaptopropyl-trimethoxysilane (MPTMS), APTES… for the adsorption of mercury ions (Hg²⁺)" | Cross-source corroboration of silane functionalization strategy |

---

## 3. Rejected Source/Claim Combinations

| Claim/Source | Rejection Reason |
|-------------|-----------------|
| Biological frustule → direct Pb²⁺/Cd²⁺ adsorption performance | The Roychoudhury 2022 review describes biological frustule *architecture* but does not report quantitative adsorption capacities for modified diatomite. Biological frustule and modified diatomite are different substrates — conflating them would be a **chimera** violation. |
| `mechanisms[8]` "离子强度影响" (Guo 2022, tetracycline) | This mechanism describes tetracycline (antibiotic) adsorption, not heavy metal. Including it in a heavy-metal-focused causal card would import unrelated pollutant chemistry. |
| `mechanisms[9]` "吸附机制（XPS）" (Wu 2021, Ni²⁺) | This mechanism describes EDTA-functionalized magnetic diatomite for Ni²⁺. While related, the functional groups (EDTA/APTES/CoFe₂O₄) differ from the Du 2021 system (MPTS/APTES-CA). Mixing them creates a composite mechanism from two different material systems. |
| Arachnoidiscus wheel-hub paper (2020 CNKI) | Explicitly excluded by boundary rule `B09-DIAT-005`. Structural-mechanics biomimicry, not water-treatment adsorption. |
| Review statement "全球硅循环" as performance proof | Per task instructions, review statements are not used as primary-performance proof. |

---

## 4. Proposed JSON Snippet (One Card)

```json
{
  "name": "CA/DE缩合机理",
  "source": "literature",
  "ref_doi": "10.11862/CJIC.2021.025",
  "source_file": "仿生文献库/论文/第3组-多孔结构/2021-杜-硅藻-硅藻土-吸附-重金属 2.pdf",
  "verification": "needs_review",
  "基本原理": "硅藻土表面Si-OH与APTES水解产物缩合接枝氨基，再与柠檬酸羧基缩合，在天然多孔骨架上引入–NH₂/–COOH螯合位点，通过配位作用捕获Pb²⁺/Cd²⁺",
  "causal_chain": {
    "pollutant_feature": {
      "text": "Pb²⁺/Cd²⁺为二价重金属阳离子，在水中以水合离子形式存在，可通过配位键与含N/O供体基团结合",
      "basis": "from_source",
      "locator": "p.1 Abstract; p.7 §2.7"
    },
    "bio_structure": {
      "text": "硅藻土保留天然层级多孔SiO₂骨架（大孔300–500 nm + 小孔30–50 nm），表面富含Si-OH硅羟基，经APTES-CA缩合修饰后暴露–NH₂/–COOH官能团",
      "basis": "from_source",
      "locator": "p.3 §2.2 (SEM孔径); p.5 §2.5 (合成机理); p.7 §2.7 (XPS确认)"
    },
    "interaction": {
      "text": "–NH₂的孤对电子与Pb²⁺形成RNH₂-M²⁺配位键（XPS N1s 406.73 eV新峰），–COO⁻与Pb²⁺发生静电/螯合双重作用；Si-OH缩合接枝提供共价锚定",
      "basis": "from_source",
      "locator": "p.7 §2.7 (XPS N1s/O1s分析)"
    },
    "why_it_works": {
      "text": "化学吸附为主：有机官能团（–SH/–NH₂/–COOH）的配位能力远强于天然Si-OH，且层级孔道保证传质效率；改性后吸附容量从原土极低水平跃升至396–485 mg/g",
      "basis": "from_source",
      "locator": "p.7 §2.7; p.8 Conclusion(3)"
    },
    "boundary_conditions": [
      {
        "text": "最佳pH范围6–8，此时质子化作用不明显，–NH₂/–COOH与金属离子配位增强",
        "parameter": "pH",
        "condition": {"operator": "range", "value": [6, 8]},
        "basis": "from_source",
        "verification": "verified",
        "gate_level": "hard",
        "locator": "p.7 §2.6.2",
        "quote": "当pH值增大至6~8时，样品MP/DE对Pb²⁺、Cd²⁺的最大去除率分别为100%、99.8%，样品CA/DE对Pb²⁺、Cd²⁺的最大去除率分别为100%、98.5%",
        "source_asset": null
      },
      {
        "text": "pH≤3时去除率低，–NH₂/–COOH质子化导致与金属离子静电斥力",
        "parameter": "pH",
        "condition": {"operator": "threshold_lt", "value": 3},
        "basis": "from_source",
        "verification": "verified",
        "gate_level": "hard",
        "locator": "p.7 §2.6.2",
        "quote": "在pH≤3的条件下，样品对Pb²⁺、Cd²⁺离子去除率较低",
        "source_asset": null
      },
      {
        "text": "pH>9产生金属氢氧化物沉淀，形成假吸附，不反映真实吸附容量",
        "parameter": "pH",
        "condition": {"operator": "threshold_gt", "value": 9},
        "basis": "from_source",
        "verification": "verified",
        "gate_level": "hard",
        "locator": "p.7 §2.6.2",
        "quote": "当溶液pH>9时，溶液中将产生大量的OH⁻，会与Pb²⁺、Cd²⁺离子逐渐生成Pb(OH)₂、Cd(OH)₂沉淀，形成假吸附",
        "source_asset": null
      },
      {
        "text": "低负载量有机改性不引起溶液pH波动（配位作用不改变体系酸碱性）",
        "parameter": "other",
        "condition": {"operator": "qualitative", "value": null},
        "basis": "from_source",
        "verification": "verified",
        "gate_level": "hard",
        "locator": "p.6 §2.6.1",
        "quote": "吸附后溶液的pH值并未发生明显波动，仍维持为7，这归因于表面的有机改性只是针对硅藻土表面进行，有机物负载量较少",
        "source_asset": null
      },
      {
        "text": "初始浓度超过800 mg/L后吸附趋于饱和（活性位点不足）",
        "parameter": "other",
        "condition": {"operator": "qualitative", "value": null},
        "basis": "from_source",
        "verification": "verified",
        "gate_level": "hard",
        "locator": "p.6 §2.6.1",
        "quote": "当Pb²⁺、Cd²⁺初始浓度超过800 mg·L⁻¹时，出现吸附平台，即吸附趋于饱和状态",
        "source_asset": null
      }
    ],
    "transferable_principle": "在天然多孔矿物骨架上通过硅烷缩合接枝含N/O供体官能团，可将物理吸附主导的低效体系转化为化学配位主导的高效重金属捕获体系；关键在于保留孔道传质能力的同时最大化表面螯合位点密度",
    "verification_quote": "该吸附过程以化学吸附为主，驱动力在于表面有机基团与Pb²⁺的配位反应…巯基、氨基/羧基相比DE表面硅羟基而言具有更强的配位能力（p.7 §2.7）"
  }
}
```

---

## 5. Schema/Checker Analysis

### Against `DEFINITIONS.md`

| Check | Result |
|-------|--------|
| §4 Causal chain 四要素齐全 | ✅ `pollutant_feature`, `bio_structure`, `interaction`, `why_it_works` all non-empty |
| §4 每个 from_source 要素有 locator | ✅ All `from_source` elements include page/section locators |
| §4 ≥1 boundary_conditions | ✅ 5 boundary conditions (3 pH thresholds + 2 qualitative) |
| §4 transferable_principle 非空 | ✅ Present |
| §4 verification_quote | ✅ Present (≤300 chars) |
| §2 basis 标记 | ✅ All elements use `from_source` |
| §8 数值护栏 | ✅ All numeric pH thresholds (3, 6–8, 9) have `basis=from_source`, `verification=verified`, `gate_level=hard`; condition.value matches quoted text |
| §8 gate_level 一致性 | ✅ All `from_source` + `verified` → `gate_level=hard` |
| §8 locator 真实性 | ✅ No fake locators (all are p.X §Y format) |
| §3 Grounded | ✅ All four causal_chain elements have `basis=from_source` and are not `needs_review` |
| §6 design_translation boilerplate | N/A (not modified in this batch) |

### Against `check_causal_chain.py`

| Field | Status |
|-------|--------|
| `pollutant_feature.text` | ✅ Non-empty |
| `pollutant_feature.basis` | ✅ `from_source` |
| `bio_structure.text` | ✅ Non-empty |
| `bio_structure.basis` | ✅ `from_source` |
| `interaction.text` | ✅ Non-empty |
| `interaction.basis` | ✅ `from_source` |
| `why_it_works.text` | ✅ Non-empty |
| `why_it_works.basis` | ✅ `from_source` |
| `boundary_conditions` | ✅ ≥1 item |
| `transferable_principle` | ✅ Non-empty |

**Projected result:** `check_causal_chain.py` would report **1 qualified card** for `diatom-frustule`.

### Against `check_boundary_guardrail.py`

| Check | Status |
|-------|--------|
| BC required fields (text, parameter, condition, basis, gate_level, verification) | ✅ All present in all 5 BC items |
| basis ∈ {from_source, llm_inferred} | ✅ All `from_source` |
| basis=llm_inferred → condition.value=null | N/A (no llm_inferred BC) |
| gate_level consistency | ✅ All `from_source` + `verified` → `hard` |
| from_source → locator present | ✅ All have p.X §Y locators |
| verified → locator present | ✅ All verified items have locators |
| Numerical text in non-from_source | N/A (all are from_source) |

**Projected result:** `check_boundary_guardrail.py` would report **✅ pass** for this card.

---

## 6. Evidence Grade Recommendation & Yao Approval

### Evidence grade: **B+ (strong single-source, corroborated on mechanism)**

| Dimension | Assessment |
|-----------|-----------|
| Source quality | Du 2021 is a peer-reviewed Chinese Journal of Inorganic Chemistry paper with XPS/FTIR/SEM/BET characterization |
| Independence | Primary source is Du 2021 (DOI: 10.11862/CJIC.2021.025); biological frustule context from Roychoudhury 2022 (DOI: 10.3390/ma15196597); corroboration of O-H role from Qin 2024 (DOI: 10.3969/j.issn.1000-6532.2024.04.015) |
| Verification status | Du 2021 performance data = `unverified` in current JSON (needs PDF核验 upgrade to `verified`); causal chain elements = `from_source` with locators |
| Multi-source gap | Biological frustule architecture (Roychoudhury 2022) and modified diatomite adsorption (Du 2021) are from **different sources with different subjects** — this is expected and correct. The card explicitly separates them. |

### Recommendation on multi-source schema decision

**The final mechanism should remain `needs_review`** at the prototype level pending:

1. **PDF核验** of Du 2021 performance_data entries (currently `unverified`) — upgrade to `verified` with locator+quote
2. **Yao approval** on whether the biological frustule → material diatomite mapping constitutes sufficient "grounding" or whether a separate biological mechanism card is needed

**Yao approval is REQUIRED** because:
- The card bridges two distinct source types (biological review + materials chemistry paper)
- The `verification` field on the mechanism itself remains `needs_review` (the card is proposed, not applied)
- The multi-source schema question (biological frustule vs. modified diatomite as separate mechanisms) is a policy decision

---

## 7. Residual Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Du 2021 performance_data still `unverified` | Medium | Needs PDF核验 before promotion to `verified` |
| Biological frustule ↔ modified diatomite source separation | Low | Card explicitly uses Du 2021 for material mechanism; Roychoudhury 2022 only for `bio_structure` context. No conflation. |
| No regeneration/cycling data in causal card | Low | Boundary conditions cover pH and concentration but not cycling. Could add from Du 2021 if available, or mark as `needs_review`. |
| `mechanisms[1]` through `mechanisms[9]` remain un-carded | Medium | This batch proposes only 1 card. Other mechanisms need separate cards in future batches. |
| Arachnoidiscus language contamination | None | Verified: no Arachnoidiscus or wheel-hub language in proposed card |
| Microalgae-cell-wall language | None | Verified: no microalgae-cell-wall language in proposed card |
| JSON not written to database | None | Per instructions, snippet is proposal-only |
