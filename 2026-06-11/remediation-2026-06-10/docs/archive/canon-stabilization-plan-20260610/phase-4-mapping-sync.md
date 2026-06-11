# Phase 4: 索引同步补强

> 预计工作量：2-4 小时  
> 目的：检查 `feature-mapping.json` 是否与当前 canon 同步，避免候选召回和排序基于旧快照。  
> 停止点：只输出报告，不自动重写 `feature-mapping.json`。

---

## 1. 建议新增文件

```text
tools/verify_mapping_sync.py
```

---

## 2. 问题背景

当前 `ctx.query()` 的候选召回依赖：

- `feature-mapping.json`
- `feature_matching_rules.json`
- `pollutant_aliases.json`
- `pollutant_profiles.json`
- `prototypes_db/*.json`

如果 `feature-mapping.json` 没有随第二波提取和 canon 修复同步，可能出现：

- 低质量原型进入强排序；
- `needs_literature` 原型进入候选；
- 已恢复的富化数据未参与召回；
- direct evidence 与 canon 数据不一致。

本阶段只做检查和报告，不自动改写索引文件。

---

## 3. 检查内容

`tools/verify_mapping_sync.py` 至少检查：

1. `feature-mapping.json` 中引用的 prototype 都存在于 `prototypes_db/`。
2. `pollutant_prototype_map` 中引用的 prototype 都存在于 `prototypes_db/`。
3. `pollutant_prototype_map` 中污染物名称能被 `pollutant_aliases.json` 归一。
4. 强排序候选不能是：
   - `status=needs_literature`
   - 无 mechanism
   - 无可用 `基本原理`
   - 明确低覆盖且不能出 brief 的原型
5. 对 PFOA / SMX / BPA / Pb(II) 输出候选检查摘要。

---

## 4. 执行命令

```powershell
python -X utf8 tools\verify_mapping_sync.py
```

---

## 5. 验收标准

- [ ] 脚本能运行并输出报告。
- [ ] 报告列出过期映射或低质量候选。
- [ ] 报告明确是否建议重建 `feature-mapping.json`。
- [ ] 不自动修改 `feature-mapping.json`。
- [ ] 不破坏现有 ADRMATS 验收。

---

## 6. 输出格式

```text
Phase 4 完成
mapping sync 检查结果:
- prototype 引用缺失: <n>
- pollutant alias 无法归一: <n>
- 强排序低质量候选: <n>
- 是否建议重建 feature-mapping.json: 是 / 否

验收结果:
- verify_adrmats_delivery.py: <结果>
- validate_consistency.py: <结果>
- check_chimera.py: <结果>
```
