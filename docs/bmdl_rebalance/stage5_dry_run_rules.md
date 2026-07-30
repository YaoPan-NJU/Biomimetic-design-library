# Stage 5 Dry-Run Rules

**日期：** 2026-07-05
**状态：** Dry-run（不覆盖正式 match_weights）

---

## 一、规则定义

| 规则 | 条件 | 动作 | 影响条数 |
|------|------|------|---------|
| R1-quarantined | prototype_id in quarantined | weight=0, excluded | 0（match_weights 中无 quarantined 原型） |
| R2-no_source | basis 含 "no_source_evidence" | cap 0.3 | 44 |
| R3-exploratory | lane == "exploratory" | cap 0.3 | 25 |
| R4-non_direct | not direct_evidence and lane != "fact" | cap 0.5 | 15 |
| R5-retained | direct_evidence or lane == "fact" | 保留原权重 | 46 |

## 二、规则优先级

R1 > R2 > R3 > R4 > R5

## 三、特殊处理

### PDA/mussel 去重
- polydopamine-coating 和 mussel-foot-adhesion 存在数据重叠
- dry-run 中两者都保留但标注 "needs_dedup"
- Stage 5 正式版需合并：mussel-foot-adhesion 作为机制 root，PDA 作为材料实现

### chitosan/chitin/lobster 边界
- chitosan 霸榜（27 条 match, 21.8% after）
- Stage 5 正式版需评估是否将部分 chitosan match 迁移到 lobster-exoskeleton 或 insect-chitin

### bone-structure/oyster-shell 降权
- 两者当前 avg weight 0.86/0.84，但 17/14 条 match 中大量是 exploratory
- dry-run 后 avg 降至 0.482/0.371
- 降权幅度最大，符合潘老师"exploratory 溢权"诊断

## 四、不做的事

- 不新增 match_weights（Stage 5 正式版才做）
- 不覆盖 adrmats_export/match_export.json
- 不修改 ETL 或 query_candidates 代码
