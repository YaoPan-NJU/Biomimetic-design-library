# Claude Code 统一任务（最终轮）

> 前置条件：HEAD = a29872d，review 分支
> 执行顺序：Task 1 → Task 2
> Task 1 用 mimo-v2.5 多模态（PDF 精读），Task 2 同
> 完成后 BMDL 所有剩余项穷尽，可交付

---

## Task 1：keyword_match BC 升级为 from_source（138条）

### 问题

138 条 BC 当前 `basis=corroborated`、`verification_method=keyword_match`——上一轮用 PKB 关键词匹配升级的。这些 BC 文本具体（avg 24字，96条 >=25字），有 115 条有 ref_doi/source_file，PDF 精读成功率高。

### 执行

用 `multimodal_verify.py --field boundary_conditions`，但需要**只处理 keyword_match 的 BC**。

修改 `verify_boundary_conditions` 函数的过滤条件，在遍历 BC 时增加：
```python
if bc.get('basis') != 'corroborated':
    continue
vm = bc.get('verification_method', '') or ''
if vm != 'keyword_match':
    continue
```

或者写一个独立脚本，调用 `verify_row_with_api` 逐条处理。

### 分布

| 原型 | BC 数 | 有引用 |
|------|-------|--------|
| chitosan | 90 | 大部分有 |
| chlorella-cell-wall | 13 | |
| mussel-foot-adhesion | 6 | |
| 其他 15 个原型 | 29 | |
| **合计** | **138** | **115 有引用** |

### 成功标准

- 找到 PDF 原文 → `basis` 改为 `from_source`，填写 `source`/`quote`/`locator`，`verification_method` 改为 `pdf_visual_reading`
- PDF 中未找到 → 保持 `corroborated` + `keyword_match`，不改
- 无引用的 23 条 → 跳过

### 并发

可开 2-3 个子 agent，按原型分组：
- Agent A: chitosan (90条)
- Agent B: chlorella + mussel + bacterial-cellulose + plant-lignocellulosic + plant-tannin + starch (24条)
- Agent C: 其余 (24条)

mimo-v2.5 多模态，max_tokens=8192，enable_thinking=False，3 agent × 1 并发 = 3，远低于 12 上限。

### commit

`verify(v1.0): {n} keyword_match BCs upgraded to from_source`

---

## Task 2：unverified 机制升级为 partial（147条）

### 问题

168 条机制 `verification=unverified`，其中 147 条有 ref_doi/source_file。全部集中在 5 个背景原型。

### 执行

用 `multimodal_verify.py --field mechanisms`，过滤 `verification=unverified` 的机制。

在 `verify_prototype` 函数中修改过滤条件：
```python
v = item.get('verification', 'unverified')
if v != 'unverified':
    continue
```

### 分布

| 原型 | 机制数 |
|------|--------|
| superhydrophobic-artificial | 59 |
| water-strider-leg | 52 |
| lotus-leaf | 28 |
| shark-skin | 18 |
| cactus-spine | 11 |
| **合计** | **168（147有引用）** |

### 成功标准

- PDF 中找到机制相关描述 → `verification` 改为 `partial`，填写 `verification_quote`/`source_locator`
- PDF 中未找到 → 保持 `unverified`
- 无引用的 21 条 → 跳过

### 并发

5 个原型可分 2-3 组：
- Agent A: superhydrophobic-artificial (59) + cactus-spine (11) = 70
- Agent B: water-strider-leg (52) + shark-skin (18) = 70
- Agent C: lotus-leaf (28) = 28（可合并到 B）

### commit

`verify(v1.0): {n} unverified mechanisms upgraded to partial`

---

## 完成后的最终状态

做完 Task 1 + Task 2 后，所有剩余项穷尽：

| 剩余项 | 数量 | 状态 |
|--------|------|------|
| keyword_match BC | 138 → 尝试 PDF 升级 | ✅ 穷尽 |
| unverified 机制 | 168 → 尝试 PDF 升级 | ✅ 穷尽 |
| unverifiable_generic_text BC | 170 | 占位句，无法改进 |
| pdf_not_found BC | 125 | 已检查，PDF 中无对应内容 |
| no_reference_available BC | 41 | 无引用 |
| 缺 fg/ks | 82+53 | 背景原型物理机制，合理为空 |
| 有机污染物画像 | 44种（含20种有机） | ✅ 已完成 |

**BMDL 所有可做的提升全部穷尽，可交付。**

---

## 注意事项

- Task 1 和 Task 2 都是 PDF 精读，用 mimo-v2.5 多模态
- max_tokens=8192，enable_thinking=False，temperature=0
- 失败自动重试 3 次，禁止跳过
- 每完成一个原型 commit + checkpoint
- 完成后推送 `git push origin review`
