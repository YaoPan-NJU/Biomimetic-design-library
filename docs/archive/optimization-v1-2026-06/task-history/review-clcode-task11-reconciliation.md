# Task 11 — Reconciliation Fixes Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Fix 1: chlorella-cell-wall mechanisms[0] Removal (B03-CHL-001)

- **Removed:** `mechanisms[0]` — "藻类去除合成染料的三种机制" (Cheng2021 Pb²⁺ mislabeled as dye removal)
- **ref_doi:** 10.19824/j.cnki.cn32-1786/x.2021.0078
- **Before:** 13 mechanisms → **After:** 12 mechanisms
- **File:** `prototypes_db/chlorella-cell-wall.json`

## Fix 2: biomineralization-template Mechanism Narrowing (F02-BMT-003)

- **OLD name:** "生物矿化模板吸附机制（待文献支撑）"
- **OLD 基本原理:** "生物矿化通过有机模板控制无机晶体生长方向和形貌，形成的多级孔结构可作为吸附剂骨架"
- **NEW name:** "LanM@ZIF-8 稀土吸附机制"
- **NEW 基本原理:** "LanM 蛋白通过矿化过程引导 ZIF-8 框架生长，形成 LanM@ZIF-8 复合材料，其中 LanM 的金属结合位点提供对 Nd³⁺ 等稀土离子的选择性吸附能力"
- **Note added:** SCOPE_NARROWED marker
- **File:** `prototypes_db/biomineralization-template.json`

## Fix 3: CN114887602A PDF Recovery

- **Source:** Git object at commit `9ee5da0` (2026-06-06)
- **Restored to:** `仿生文献库/专利/2022-CN114887602A-聚多巴胺-纤维素-吸附-除磷.pdf` (839 KB)
- **PDA source_file:** Already correct from Task 8 path normalization
- **Rows affected:** `polydopamine-coating.json` performance_data[0-3] (phosphorus adsorption claims)
- **Status:** PDF now available for verification

## Summary

| fix | file | action |
|---|---|---|
| B03-CHL-001 | chlorella-cell-wall.json | Removed wrong-source mechanisms[0] |
| F02-BMT-003 | biomineralization-template.json | Narrowed mechanism to LanM@ZIF-8 scope |
| CN114887602A | 仿生文献库/专利/ | Restored PDF from Git, 839 KB |
