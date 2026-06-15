# Biomimetic Design Library Canon Stabilization Plan

> 执行对象：本地 AI / 本地工程代理  
> 项目分支：`feature/extraction-results`  
> 当前目标：先稳定 JSON canon 和 ADRMATS brief 接口可信度，再与 PG 同事对接  
> 禁止范围：不做 PG、不扩库、不批量提取、不 push

---

## 1. 总目标

把 `Biomimetic-design-library` 当前 JSON canon 修到三个标准：

1. **可重建**：重跑 `tools/build_prototypes_db.py` 不会丢 `基本原理`、`verification`、`active_features` 等富化字段。
2. **可调用**：`tools/biomimetic_context.py` 继续满足 ADRMATS 的 `ctx.query()` brief 接口。
3. **可信标注**：brief 中的 evidence、verification、honesty ledger 来自真实数据，而不是硬编码或宽松推断。

完成 Phase 3 后，可以和 PG 同事正式对接 schema / ETL 讨论。完成 Phase 4 后再对接更稳。

---

## 2. 总体约束

- 不要 push。
- 不要新增文献。
- 不要继续批量提取。
- 不要开始 PostgreSQL / PG schema / ETL 工作。
- 不要在完成 enrichment 导出与保护逻辑前重跑 `tools/build_prototypes_db.py`。
- 每个 Phase 完成后停下，输出：
  - 修改文件列表
  - 执行命令
  - 验证结果
  - 剩余风险

---

## 3. 阶段文件

按顺序执行：

1. [Phase 0：基线确认](phase-0-baseline.md)
2. [Phase 1：修接口可信度 P0 bug](phase-1-interface-trust.md)
3. [Phase 2：富化层分离](phase-2-enrichment-split.md)
4. [Phase 3：模拟重建验证](phase-3-rebuild-verification.md)
5. [Phase 4：索引同步补强](phase-4-mapping-sync.md)
6. [Phase 5：交接报告](phase-5-handoff-report.md)

---

## 4. 推荐对接节点

### 可以现在同步，但不要交 PG

可以向同事同步：

> 6 月 10 日已把 canon 从 6 月 9 日回退事故中基本修回：validate 0 error、chimera 0、MOF 252 条 non-unverified 恢复。当前还差富化层物理分离和接口证据标注修正。我会先完成这两个 P0，再把稳定 canon、验证输出和字段语义交给你推进 PG schema / ETL。

### 正式交接点

- **最低交接点**：Phase 3 完成。
- **更稳交接点**：Phase 4 完成。
- **不建议**：现在直接开始 PG。

---

## 5. 完成判定

本轮最低完成标准：

- [ ] Phase 0 完成：基线清楚。
- [ ] Phase 1 完成：接口证据标注可信。
- [ ] Phase 2 完成：enrichment 层导出。
- [ ] Phase 3 完成：模拟重建富化字段无损。
- [ ] 所有验收脚本通过。
- [ ] 输出给同事的交接报告。

完成这些后，再进入 PG / SSoT / ETL 工作。
