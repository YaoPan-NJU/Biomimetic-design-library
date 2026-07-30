# Claude Code Task 69-73: 原型扩展 (24->36) + 全量验证 + 文档交接

## 执行模式

自主连续执行全部步骤。只在以下情况停下：
1. build 或 check_chimera 报出你无法修复的错误
2. 某个文件 schema 不符合预期且你无法判断如何处理
3. git push 失败（认证/网络问题）
4. MIMO API 全部 key 返回 401/403（认证失败）

其他情况（个别行 not_found、API 重试失败、CAJ 跳过、某个原型 0 行待验证）一律自主处理并记录，不停下。

## 背景

Task 64-68 刚完成：基础设施修复 + 13 原型多模态验证（24 perf verified, 19 not_found, 6 errors）。当前 24 个活跃原型，perf 93% / mech 50% 覆盖率。

用户要求扩展数据库广度：将所有已有原型（分离层、停放层、仅有描述文档的）全部激活。目标：24 -> 36 个活跃原型。然后对新激活的原型运行多模态验证。

---

## 步骤 1: 激活已有原型 (+6)

### 1.1 复制 5 个分离层原型到主目录

```bash
copy prototypes_db\separation\cactus-spine.json prototypes_db\cactus-spine.json
copy prototypes_db\separation\lotus-leaf.json prototypes_db\lotus-leaf.json
copy prototypes_db\separation\shark-skin.json prototypes_db\shark-skin.json
copy prototypes_db\separation\superhydrophobic-artificial.json prototypes_db\superhydrophobic-artificial.json
copy prototypes_db\separation\water-strider-leg.json prototypes_db\water-strider-leg.json
```

### 1.2 复制 1 个停放原型到主目录

```bash
copy prototypes_db\parked\namib-beetle.json prototypes_db\namib-beetle.json
```

验证：`dir prototypes_db\*.json | find /c ".json"` 应返回 30。

---

## 步骤 2: 为 6 个 markdown-only 原型创建最小 DB entry

以下 6 个原型在 `prototypes/` 下有 markdown 描述但没有 DB entry：
- alginate
- cellulose-nanocrystal
- diatom-inspired-porous
- metal-organic-framework
- silkworm-silk
- starch-granule

对每个原型：
1. 读取 `prototypes/{name}/` 目录下的 .md 文件
2. 提取 organism（生物名称）、category（分类）、brief_description
3. 如果 markdown 中有明确的机制描述段落，提取为 mechanisms 条目
4. 创建 `prototypes_db/{name}.json`

schema:
```json
{
  "id": "{name}",
  "organism": {
    "common": "{通用名}",
    "scientific": "{学名，无则留空}"
  },
  "category": "{biopolymer/biomineral/microorganism/structural/functional 之一}",
  "brief_description": "{一句话描述}",
  "performance_data": [],
  "mechanisms": [],
  "engineering_constraints": [],
  "boundary_rules": [],
  "verification": "unverified",
  "source_status": "pending_extraction",
  "notes": "Skeleton entry from markdown description. Awaiting literature extraction."
}
```

分类参考：
- alginate: biopolymer（海藻酸钠，海藻提取物）
- cellulose-nanocrystal: biopolymer（纤维素纳米晶，植物细胞壁）
- diatom-inspired-porous: structural（仿生硅藻多孔结构）
- metal-organic-framework: structural（MOF，受生物启发的合成框架）
- silkworm-silk: biopolymer（蚕丝蛋白）
- starch-granule: biopolymer（淀粉颗粒）

每个文件创建后用 `python -X utf8 -c "import json; json.load(open('prototypes_db/{name}.json'))"` 验证合法性。

验证：`dir prototypes_db\*.json | find /c ".json"` 应返回 36。

---

## 步骤 3: 运行 build 并确认路由正确

```bash
python -X utf8 tools/build_prototypes_db.py
```

确认：
- 无报错
- 新激活的 6 个原型（cactus-spine, lotus-leaf, shark-skin, superhydrophobic, water-strider, namib-beetle）的 verification_quote 和 verification 状态未被覆盖
- 6 个 skeleton 原型未被 build 覆盖为空（如果 build 不认识它们，应该不动）

如果 build 覆盖了 skeleton 原型（把 mechanisms 清空了），需要修改 build 脚本跳过没有提取源的 prototype，或在 build 前添加路由排除。

---

## 步骤 4: 对新激活的 6 个原型运行多模态验证 (254 行)

按从小到大顺序运行：

```bash
python -X utf8 tools/multimodal_verify.py namib-beetle
python -X utf8 tools/multimodal_verify.py cactus-spine
python -X utf8 tools/multimodal_verify.py shark-skin
python -X utf8 tools/multimodal_verify.py lotus-leaf
python -X utf8 tools/multimodal_verify.py water-strider-leg
python -X utf8 tools/multimodal_verify.py superhydrophobic-artificial
```

预计数据量：
- namib-beetle: 16 mech (~8 min)
- cactus-spine: 11 mech (~5 min)
- shark-skin: 31 mech (~15 min)
- lotus-leaf: 49 mech (~25 min)
- water-strider-leg: 61 mech (~30 min)
- superhydrophobic-artificial: 8 perf + 78 mech (~45 min)
- 合计: 254 行, 预计 ~2 小时

注意：这些原型的 PDF 匹配情况未知。如果 `find_pdf` 找不到对应 PDF，该行会记入 no_pdf 统计。某些原型可能大量行无法验证——这是正常的，记入报告即可。

---

## 步骤 5: 重跑 Task 64-68 中未成功的行

对以下原型重跑 multimodal_verify（这些原型有 19 not_found + 6 errors，重跑时 retry 机制可能改善结果）：

```bash
python -X utf8 tools/multimodal_verify.py chitosan
python -X utf8 tools/multimodal_verify.py cell-membrane-ion-channel
```

增量保存会跳过已完成的行，只重跑 needs_review/unverified 的行。

---

## 步骤 6: 校验

```bash
python -X utf8 tools/build_prototypes_db.py
python -X utf8 tools/check_chimera.py --strict
python -X utf8 tools/validate_consistency.py
```

### 验证 verification_quote 保留

```bash
python -X utf8 -c "
import json, os
db = 'prototypes_db'
for f in sorted(os.listdir(db)):
    if not f.endswith('.json'): continue
    d = json.load(open(os.path.join(db,f),'r',encoding='utf-8'))
    pq = sum(1 for p in d.get('performance_data',[]) if p.get('verification_quote'))
    mq = sum(1 for m in d.get('mechanisms',[]) if m.get('verification_quote'))
    if pq + mq > 0:
        print(f'{f}: perf_quote={pq} mech_quote={mq}')
"
```

---

## 步骤 7: 统计最终数据

```bash
python -X utf8 -c "
import json, os
db = 'prototypes_db'
tp=tm=vp=vm=qp=qm=active=pending=0
for f in sorted(os.listdir(db)):
    if not f.endswith('.json'): continue
    d = json.load(open(os.path.join(db,f),'r',encoding='utf-8'))
    active += 1
    if d.get('source_status') == 'pending_extraction': pending += 1
    for p in d.get('performance_data',[]):
        tp += 1
        if p.get('verification') in ('partial','verified','corroborated','done'): vp += 1
        if p.get('verification_quote'): qp += 1
    for m in d.get('mechanisms',[]):
        tm += 1
        if m.get('verification') in ('partial','verified','corroborated','done'): vm += 1
        if m.get('verification_quote'): qm += 1
print(f'active_prototypes={active} (pending_extraction={pending})')
print(f'performance_data: {vp}/{tp} verified ({100*vp//max(tp,1)}%), {qp} with quotes')
print(f'mechanisms: {vm}/{tm} verified ({100*vm//max(tm,1)}%), {qm} with quotes')
print(f'total_verified={vp+vm}/{tp+tm} ({100*(vp+vm)//max(tp+tm,1)}%)')
"
```

记录这些数字，后面更新文档要用。

---

## 步骤 8: 更新 README.md

更新 README.md 中"当前状态"部分的数据表。将以下数值替换为步骤 7 的实际数据：

- active 原型数: 改为实际数量 (预期 36)
- 机制总数: 改为实际数量
- 机制已验证: 改为实际数量和百分比
- performance_data 已验证行: 改为实际数量和百分比
- 添加一行: pending_extraction 原型数
- 更新"整改进度"描述，提及 Task 69-73 原型扩展

---

## 步骤 9: 更新交接文档

### 9.1 追加 COLLAB-HANDOFF.md

在 `docs/optimization-v1/COLLAB-HANDOFF.md` 末尾追加：

```markdown
## 2026-06-18 ~XX:00 CST - claude-code (Task 69-73)
- completed:
  - Task 64-68: infra fix + 13 prototype multimodal verify (24 perf verified)
  - Task 69-73: prototype expansion 24->36 + verify 6 new prototypes + doc update
  - activated: 5 separation (cactus/lotus/shark/superhydrophobic/water-strider) + 1 parked (namib-beetle)
  - created: 6 skeleton entries (alginate/cellulose/diatom-inspired/MOF/silkworm/starch)
  - multimodal verify: 6 new prototypes (XXX verified, XXX not_found, XXX errors)
- current_state:
  - active prototypes: XX
  - performance_data: XX/XX verified (XX%), XX with PDF quotes
  - mechanisms: XX/XX verified (XX%), XX with PDF quotes
  - pending_extraction: 6 (awaiting litextract)
  - chimera: 0 violations, consistency: 0 errors
- next:
  - P0: litextract 提取 6 个 pending_extraction 原型
  - P0: 解决 mechanisms 无 PDF 匹配问题 (检查 source_file 路径 / DOI 下载)
  - P1: mechanisms 覆盖率继续推高
  - P2: check_causal_chain / check_boundary_guardrail 达标
- blockers: none
- decisions_needed: none
```

（XX 用步骤 7 的实际数据替换）

### 9.2 创建 Codex 交接提示词

创建 `docs/optimization-v1/CODEX-HANDOFF-PROMPT.md`:

```
你是 Codex/QoderWork，即将接手仿生设计库项目的持续推进工作。

== 项目概况 ==
- 仓库: Biomimetic-design-library, review 分支
- 定位: 仿生水处理设计参考库 (ADRMATS 系统)，不设计材料，只提供仿生设计灵感
- 当前规模: XX 个活跃原型 (其中 6 个 pending_extraction)

== 最近完成的工作 ==
Task 64-68: 修复 build merge_with_existing 保留 verification_quote; 修复 multimodal_verify (增量保存+API重试+missing_pdf); 13 原型多模态验证
Task 69-73: 原型扩展 24->36; 激活 5 分离+1 停放原型; 6 个 skeleton entry; 新原型验证; 文档更新

== 当前数据状态 ==
- active prototypes: XX (6 pending_extraction)
- performance_data: XX/XX verified (XX%)
- mechanisms: XX/XX verified (XX%)
- chimera: 0 violations
- consistency: 0 errors

== 待推进工作 ==
P0:
- 对 6 个 pending_extraction 原型执行 litextract 提取 (tools/litextract/)
  文献库: 仿生文献库/ 下 623 篇 PDF
  需要: MIMO_API_KEY 或 OpenAI key 配置在 .env
- 解决 mechanisms 无 PDF 匹配: 检查 source_file 路径 / 用 DOI+Sci-Hub 下载

P1:
- mechanisms 覆盖率从 XX% 继续推高 (multimodal_verify.py)
- 边界条件从 soft caution 升级为 hard DO-NOT (需 PDF 提取阈值)

P2:
- check_causal_chain.py / check_boundary_guardrail.py 24 原型未达标

== 关键脚本 ==
- python -X utf8 tools/build_prototypes_db.py
- python -X utf8 tools/multimodal_verify.py {prototype_name}
- python -X utf8 tools/check_chimera.py --strict
- python -X utf8 tools/validate_consistency.py

== 关键约束 ==
- 所有 Python 命令加 -X utf8
- build 会重新生成所有 JSON, merge_with_existing 保留 verification_quote/source_locator
- multimodal_verify.py 使用 mimo-v2.5 (max_tokens>=4096, 双 key 轮询)
- canon 冻结原则: 不直接编辑已由 litextract 填充的字段
- review 分支, push 到 origin/review

== 文件位置 ==
- 交接文档: docs/optimization-v1/COLLAB-HANDOFF.md
- 任务指令: docs/optimization-v1/CLAUDE-CODE-TASK-*.md
- 文献库: 仿生文献库/ (623 篇)
```

（XX 用实际数据替换）

---

## 步骤 10: 提交推送

```bash
git add -A
git commit -m "data: expand prototypes 24->36 + multimodal verify new prototypes + update docs (Task 69-73)"
git push origin review
```

完成后报告：
- 最终原型数量和覆盖率
- 新增 12 个原型各自的验证结果
- 校验结果
- 推送确认
