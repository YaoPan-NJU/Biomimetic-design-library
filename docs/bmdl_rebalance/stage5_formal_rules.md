# Stage 5 Formal Rules

**日期：** 2026-07-05
**状态：** 正式候选（match_export_stage5.json）

---

## 一、规则定义

| 规则 | 条件 | 动作 | 影响条数 |
|------|------|------|---------|
| R1-quarantined | prototype_id in quarantined | weight=0, excluded | 0 |
| R2-no_source | basis 含 "no_source_evidence" | cap 0.3 | 44 |
| R3-exploratory | lane == "exploratory" | cap 0.3 | 25 |
| R4-bone-lead | bone-structure + lead + non-direct | cap 0.5 | 14 |
| R5-oyster-non-direct | oyster-shell + non-direct | cap 0.5 | 12 |
| R6-generic-non-direct | not direct + lane != "fact" | cap 0.5 | 15 |
| R7-retained | direct evidence or fact lane | retain original | 46 |
| R8-new-PFOA | plant-lignocellulosic + PFOA | new weight 0.6 | +1 |
| R9-new-BPA | plant-lignocellulosic + BPA | new weight 0.65 | +1 |
| R10-dedup-PDA | PDA + pollutant in mussel overlap | cap 0.3 | 3 |

## 二、规则优先级

R1 > R2 > R3 > R4/R5 > R6 > R7 > R8/R9 > R10

## 三、与 dry-run 的差异

| 差异 | Dry-run | Formal |
|------|---------|--------|
| bone-structure lead | 批量 cap 0.5 | 逐条：fact+direct retain, lead non-direct cap 0.5 |
| oyster-shell | 批量 cap 0.3 (exploratory) | 逐条：direct retain, non-direct cap 0.5 |
| PFOA/BPA | 全 cap 0.3 | 新增 plant-lignocellulosic PFOA 0.6 / BPA 0.65 |
| PDA/mussel | 未处理 | PDA 在重叠污染物上 cap 0.3 |
| chitosan | 批量 cap | 不机械迁移（evidence-based 霸榜） |
