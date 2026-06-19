# Task 15 — Lotus-Leaf Scope Split Report

status: completed
actor: Claude Code
completed_at: 2026-06-17

## Scope Split Execution

**Yao decision:** B — keep lotus-specific + wetting-theory

### Mechanisms

| category | before | after |
|---|---|---|
| lotus-specific | 32 | 32 (kept) |
| wetting-theory | 17 | 17 (kept) |
| membrane | 108 | 0 (removed) |
| superhydrophobic-general | 133 | 0 (removed) |
| antibacterial | 31 | 0 (removed) |
| oil-water-separation | 18 | 0 (removed) |
| other | 11 | 0 (removed) |
| **Total** | **346** | **49** |

**Removed: 297 mechanisms** (85.8%)

### Performance Data

| index | action | reason |
|---|---|---|
| [0] | marked knowledge_gap | PDF missing (Zheng2024) |
| [1] | marked knowledge_gap | PDF missing (Khan2022) |
| [2] | marked knowledge_gap | PDF missing (Usman2021) |
| [3] | marked scope_mismatch | Li2023 oil-water review, not lotus |

### Wetting-Theory Items Kept (17)

Fundamental models and definitions:
- Young方程/Wenzel模型/Cassie-Baxter模型
- 润湿理论基础
- Cassie-Baxter态机制
- Wenzel方程粗糙度放大效应
- 润湿状态转变：Cassie-Baxter到Wenzel
- 接触角润湿性定义
- 超疏水阈值接触角
- 超疏水材料定义与润湿理论
- 超疏水/亲水接触角边界定义
- 特殊润湿性分类
- 全疏水性(omniphobicity)的Cassie-Baxter机制
- 表面能变化与润湿性转变机制
- Young-Laplace方程分析
- 超疏水材料构建基本原理
- 超疏水表面接触角阈值
- 润湿理论模型在本研究中的应用
- 其他表面能/粗糙度基础项

## Files Modified

- `prototypes_db/separation/lotus-leaf.json`
