# COLLABORATION PROTOCOL

> 本文件是 Qoder 与 Claude Code 之间的协作契约。双方必须遵守。
> 最后更新：2026-06-17 by Qoder

---

## 1. 角色与决策层级

| 层级 | 角色 | 工具 | 权限 |
|------|------|------|------|
| L0 审批者 | Yao | 人 | 批准 Package B/C/D/E、scope 变更、原型存废 |
| L1 审查者 | Qoder | IDE Agent | 验收 Claude Code 产出、更新 decision queue、执行已批准的编辑、commit/push、分配任务 |
| L2 工人 | Claude Code | Terminal Agent | PDF 审计、路径验证、证据提取、报告生成。**不编辑 prototypes_db JSON** |

## 2. 文件沟通协议

### 2.1 任务板：docs/optimization-v1/COLLAB-BOARD.md

Qoder 写入，Claude Code 读取并执行。格式：

`markdown
## TASK-{NNN}: {title}
- status: assigned | in_progress | done | blocked
- priority: high | medium | low
- assigned_to: clcode | qoder
- input: {需要读取的文件}
- output: {需要产出的文件}
- deadline: {optional}
- notes: {补充说明}
`

### 2.2 交接文件：docs/optimization-v1/COLLAB-HANDOFF.md

双方交替写入，记录每次工作session的状态。格式：

`markdown
## {timestamp} - {actor: qoder|clcode}
- completed: {本次完成的事项}
- next: {下一步建议}
- blockers: {阻塞项}
- decisions_needed: {需要 Yao 决策的事项}
`

### 2.3 审计报告：docs/optimization-v1/review-clcode-*.md

Claude Code 产出的审计报告，按已有格式。

### 2.4 验收记录：docs/optimization-v1/review-qoder-acceptance-*.md

Qoder 对 Claude Code 报告的 spot-check 结果。

## 3. 工作流（一个完整循环）

`
Qoder                              Claude Code
  |                                     |
  |-- 写 COLLAB-BOARD.md 分配任务 ----->|
  |                                     |-- 读取 BOARD.md
  |                                     |-- 执行任务（读 PDF/JSON）
  |                                     |-- 产出 review-clcode-*.md
  |                                     |-- 更新 BOARD.md status=done
  |                                     |-- 写 COLLAB-HANDOFF.md
  |                                     |
  |-- 读取 HANDOFF.md <-----------------|
  |-- 读 review-clcode-*.md
  |-- spot-check 关键声明
  |-- 写 review-qoder-acceptance-*.md
  |-- 更新 decision queue status
  |-- 执行已批准的编辑
  |-- 写下一轮 BOARD.md 任务 --->
  |   ...循环...
`

## 4. Claude Code 的自主权限

### 可以自主执行（不需要 Qoder 确认）：
- 读取任何 JSON/PDF/MD 文件
- 生成审计报告到 
eview-clcode-*.md
- 路径验证和 PDF 文本提取
- 更新 BOARD.md 和 HANDOFF.md
- 对 enrichment mirror 做审计（不编辑）

### 需要 Qoder 确认（通过 BOARD.md blocked 状态）：
- 审计报告中涉及的 wrong_source 判定（Qoder spot-check）
- 任何 prototypes_db JSON 的编辑（必须由 Qoder 执行）
- verification 状态变更建议
- 新原型或 scope 变更

### 绝对禁止：
- 直接编辑 prototypes_db/*.json
- 运行 	ools/build_prototypes_db.py
- git commit/push
- 自行决定 Yao-level 的 scope 问题

## 5. 决策升级规则

| 场景 | Claude Code 动作 | Qoder 动作 |
|------|-----------------|-----------|
| 明确的 wrong_source（PDF 内容与声称完全不符） | 标记为 wrong_source + 提供 quote | 确认后执行删除 |
| 模糊的 scope 问题（如「鱼鳞是否包含鱼鳞生物炭」） | 标记为 needs_human_decision | 升级到 Yao |
| 缺失 PDF | 标记为 missing_pdf + 列出候选路径 | 决定是否下载或降级 |
| 数值可疑（极端值/单位混淆） | 标记为 needs_human_decision + 列出换算 | 决定是否降级 |
| enrichment 空白 | 从主 JSON 有来源支持的 mechanism 提取 | 验证后写入 |

## 6. 持续推进机制

### Qoder 侧（goal-driven）：
- 维护一个 goal list：清除 wrong-source  验证 enrichment  路径规范化  verification 升级
- 每轮验收后，自动从 goal list 取下一个任务写入 BOARD.md
- 只在需要 Yao 审批时暂停

### Claude Code 侧（task-driven）：
- 每次启动时读取 COLLAB-BOARD.md
- 执行所有 status=assigned 且 assigned_to=clcode 的任务
- 完成后标记 status=done 并写 HANDOFF.md
- 如果所有任务都完成，检查是否有 pending 的 enrichment/path 任务可自主推进

## 7. 当前 Goal List（Qoder 维护）

1. ~~[DONE] 第一层 wrong-source 清除（8 原型，150 条）~~
2. [NEXT] 更新 decision queue 中已清除项的状态为 pplied_wrong_source_removal
3. [ ] Claude Code: Enrichment mirror gap fill 审计
4. [ ] Claude Code: Missing PDF 路径验证（chitosan 99 项）
5. [ ] Claude Code: lotus-leaf 355 mechanisms 分组
6. [ ] Claude Code: cellulose-nanocrystal 材料分类
7. [ ] Qoder: 第二层 scope 决策呈现给 Yao
8. [ ] 应用 Package B 剩余项
9. [ ] 应用 Package C 排序安全标注
10. [ ] 应用 Package D 边界登记
