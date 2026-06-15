# 回家后执行计划 — Phase 8 Patch Gate 到 Phase 9

> 给本地 AI 的可执行计划。目标是先完成 Phase 8 patch gate，再启动 Phase 9，最后做最终验收。不要跳步。

## 目标

在家里电脑上完成：

1. 同步已提交的 Phase 8 patch。
2. 复跑 Phase 8 patch gate。
3. Phase 9 最终打包。
4. Phase 9 后 final acceptance review。
5. 满足入库条件后再合入或推送。

## 总体顺序

```text
1. 同步当前分支和 patch
2. 复跑 Phase 8 patch gate
3. 启动 Phase 9
4. 运行 Phase 9 总验收
5. 做 final acceptance review
6. 决定是否入库
```

## Task 1: 同步仓库状态

### Step 1.1 确认分支

```powershell
git status --short --branch
git log --oneline --decorate -n 8
```

期望：

```text
当前分支：opt/curation-grounding-v1
能看到：
333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题
53dff3c @ Phase 8: 失效边界补全 + DO-NOT 导出
437eb9f @ Phase 7.5: 修复接口候选排序诚实度 + pitcher-plant function 字段
```

如果看不到这三个 commit，不要继续 Phase 9。先同步分支。

### Step 1.2 检查工作区

```powershell
git status --short
```

如果有未提交修改，先判断是不是本地新改动。Phase 8 patch 已经应该在 `333b092` 中提交完成。历史上 Phase 8 patch 涉及：

```text
docs/optimization-v1/phase8-report.md
exports/adrmats_do_not.json
prototypes_db/plant-tannin.json
prototypes_db/silk-fibroin.json
prototypes_db/sulfate-reducing-bacteria.json
tools/check_boundary_guardrail.py
```

如果这些文件仍显示未提交，说明家里电脑没有正确同步 `333b092`，先停下来处理同步问题。

## Task 2: 验证 Phase 8 Patch

### Step 2.1 核查隐藏数值阈值

运行：

```powershell
python -X utf8 -c "import json; files=['prototypes_db/plant-tannin.json','prototypes_db/silk-fibroin.json']; bad=[]; 
for f in files:
 d=json.load(open(f,encoding='utf-8'))
 for mi,m in enumerate(d.get('mechanisms',[])):
  for bi,bc in enumerate((m.get('causal_chain') or {}).get('boundary_conditions') or []):
   if bc.get('basis')!='from_source':
    cond=bc.get('condition') or {}
    if cond.get('operator')!='qualitative' or cond.get('value') is not None:
     bad.append((f,mi,bi,bc.get('text'),cond))
print('bad=',bad); assert not bad"
```

期望：

```text
bad= []
```

### Step 2.2 核查 SRB boundary

运行：

```powershell
python -X utf8 -c "import json; d=json.load(open('prototypes_db/sulfate-reducing-bacteria.json',encoding='utf-8'));
for m in d.get('mechanisms',[]):
 for bc in (m.get('causal_chain') or {}).get('boundary_conditions') or []:
  if bc.get('text')=='SRB是严格厌氧菌，有氧环境完全失活':
   print(bc)
   assert bc.get('basis')=='llm_inferred'
   assert bc.get('verification')=='needs_review'
   assert bc.get('gate_level')=='soft'
   assert bc.get('locator') is None
   assert bc.get('quote') is None"
```

期望：断言不报错。

### Step 2.3 跑 Phase 8 patch gate

运行：

```powershell
python -X utf8 tools\check_boundary_guardrail.py
python -X utf8 tools\export_do_not.py
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\test_interface_honesty.py
python -X utf8 tools\check_translation_specificity.py
python -X utf8 tools\check_chimera.py --strict
python -X utf8 tools\validate_consistency.py
```

通过标准：

- `check_boundary_guardrail.py` 通过。
- `export_do_not.py` 成功生成 `exports/adrmats_do_not.json`。
- `verify_adrmats_delivery.py` 6/6 PASS。
- `test_interface_honesty.py` 3/3 PASS。
- `check_translation_specificity.py` 25/25 合格。
- `check_chimera.py --strict` 0 违规。
- `validate_consistency.py` 0 error。

### Step 2.4 核查导出与 canon 一致

运行：

```powershell
python -X utf8 -c "import json,glob; exported=json.load(open('exports/adrmats_do_not.json',encoding='utf-8')); excluded=set();
for sub in ['parked','materials_reference']:
 for f in glob.glob('prototypes_db/'+sub+'/*.json'):
  excluded.add(json.load(open(f,encoding='utf-8')).get('id'))
total=hard=soft=0
for f in glob.glob('prototypes_db/*.json'):
 d=json.load(open(f,encoding='utf-8')); pid=d.get('id')
 if pid in excluded: continue
 for m in d.get('mechanisms',[]):
  cc=m.get('causal_chain') or {}
  if not cc.get('transferable_principle'): continue
  for bc in cc.get('boundary_conditions') or []:
   total+=1
   if bc.get('gate_level')=='hard': hard+=1
   else: soft+=1
print('exported',len(exported),'canon',total,'hard',hard,'soft',soft)
assert len(exported)==total
assert sum(1 for x in exported if x.get('gate_level')=='hard')==hard"
```

期望：

```text
exported 62 canon 62 hard 0 soft 62
```

## Task 3: 确认 Phase 8 Patch Commit

Phase 8 patch 已应作为 `333b092` 存在。不要重复提交同一补丁。

```powershell
git log --oneline --decorate -n 3
git status --short
```

期望看到：

```text
333b092 @ Phase 8 patch: 修复 review 发现的 schema/护栏问题
工作区干净
```

如果 Phase 8 patch 是在家里电脑重新做的，而不是同步来的，则提交信息建议：

```powershell
git add docs/optimization-v1/phase8-report.md exports/adrmats_do_not.json prototypes_db/plant-tannin.json prototypes_db/silk-fibroin.json prototypes_db/sulfate-reducing-bacteria.json tools/check_boundary_guardrail.py
git commit -m "@ Phase 8 patch: fix boundary guardrail blind spots before Phase 9"
```

## Task 4: 启动 Phase 9

Phase 9 目标：最终打包、文档对齐、示例刷新、仓库治理。

### Phase 9 必做项

1. 生成或刷新 `examples/adrmats_briefs/` 中的示例 brief。
2. 重新生成 `exports/adrmats_do_not.json`。
3. 更新 `README.md`。
4. 更新 `docs/SUPPORT_SCOPE_AND_RISKS.md`。
5. 创建 `docs/optimization-v1/FINAL-report.md`。
6. 修复 `check_repo_hygiene.py` 当前暴露的治理问题。
7. 明确写清当前边界状态：
   - `hard DO-NOT = 0`
   - `soft caution = 62`
   - 不得把 soft caution 写成硬约束。

### Phase 9 不得做的事

- 不运行 `tools/build_prototypes_db.py`。
- 不把 `llm_inferred` 升级为 `verified`。
- 不为通过验收而删除 unresolved 风险。
- 不手改 `prototype.md`，如需刷新必须从 canon 生成。

## Task 5: Phase 9 总验收

Phase 9 完成后运行：

```powershell
python -X utf8 tools\verify_adrmats_delivery.py
python -X utf8 tools\check_boundary_guardrail.py
python -X utf8 tools\export_do_not.py
python -X utf8 tools\check_chimera.py --strict
python -X utf8 tools\check_causal_chain.py
python -X utf8 tools\check_translation_specificity.py
python -X utf8 tools\validate_consistency.py
python -X utf8 tools\check_repo_hygiene.py
```

通过标准：

- 所有命令 exit 0。
- `check_repo_hygiene.py` 必须 PASS。
- README / SUPPORT / FINAL-report 的统计与脚本输出一致。
- final examples 不把 `needs_review` 放进 facts 或强排序。
- `exports/adrmats_do_not.json` 与 canon 一致。

## Task 6: Phase 9 后 Final Review

Phase 9 通过后，把以下内容发给 Codex 或远程 AI 复核：

```text
Phase 8 patch commit:
Phase 9 commit:
git status --short --branch:
git log --oneline --decorate -n 8:
Phase 9 commands and outputs:
README/SUPPORT/FINAL-report 修改摘要:
exports/adrmats_do_not.json 统计:
remaining risks:
```

Final review 重点：

- 是否可以入库。
- 是否还有 blocker。
- 是否有夸大证据等级。
- 是否需要抽查 PDF 证据。

## Task 7: 入库判断

只有满足以下条件才允许入库：

- Phase 8 patch 已提交。
- Phase 9 已提交。
- 总验收全绿。
- `check_repo_hygiene.py` PASS。
- final review 没有 blocker。
- Yao 明确同意。
