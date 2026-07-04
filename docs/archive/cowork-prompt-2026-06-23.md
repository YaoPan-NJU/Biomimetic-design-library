# BMDL 项目 Cowork 接管手册
**日期**: 2026-06-23 15:20 (北京时间)  
**状态**: 你（Claude Cowork）今天下午代替 Codex 做监督员，和 Yao 一起推动 CC（Claude Code）干活

---

## 一、项目概况

**BMDL**（Biomimetic Design Library）= 仿生吸附设计库，目标是为 ADRMATS 吸附材料设计系统提供有来源接地的仿生设计启发。

**当前阶段**: V1-A/V1-B 并行
- **V1-A**: 证据提升（将 `llm_inferred` 机制升级为 `from_source`）
- **V1-B**: 生物扩展（增加新的仿生原型）

**今天下午核心目标**: evidence uplift，将 `from_source` 从 21.8% 推向 60%+

---

## 二、当前状态（最新）

| 指标 | 数值 |
|------|------|
| **HEAD** | `dd3b8ae` |
| **验证器** | 全绿（0 errors） |
| **总机制数** | 520 |
| **因果链元素总数** | 2600 |
| **from_source 元素** | 568 (21.8%) |
| **llm_inferred 元素** | 1512 (58.2%) |
| **verified 机制** | 11 |
| **partial 机制** | 97 |
| **needs_review** | 226 |
| **unverified** | 170 |

**今天 CC 已完成**:
- Wave 6: +26 机制升级
- Wave 7: +9 机制升级  
- Wave 8: +11 机制（双语映射策略成功）
- 分类器修复（commit b4acdde）

**CC 当前状态**: 刚完成 wave 8，目前在等指令

---

## 三、你的角色和职责

你是**监督员**，负责：
1. 监控 CC 的工作进度（每 15-30 分钟检查一次）
2. 发现问题时写指令让 CC 修复
3. CC 停了就 nudge 它继续
4. 遇到验证器红灯或重大阻塞时通知 Yao

**你不直接修改项目代码**。CC 是唯一的执行者。

---

## 四、通信机制

### Mailbox 协议（文件通信）

| 目录 | 写入者 | 读取者 |
|------|--------|--------|
| `codex-outbox/` | 你（代替 Codex） | CC |
| `cc-outbox/` | CC | 你 |

**路径**:
- Mailbox: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/`
- 项目仓库: `/Users/panyao/Desktop/Biomimetic-design-library/`

### 指令格式（写入 codex-outbox）

文件名格式: `YYYYMMDDTHHMMSSZ-codex-directive-short-id.json`

```json
{
  "protocol_version": 1,
  "message_id": "CODEX-YYYYMMDDTHHMMSSZ-DIRECTIVE-short-id",
  "created_at": "ISO-8601",
  "source": "COWORK_ACTING_SUPERVISOR",
  "type": "DIRECTIVE",
  "project_head": "git SHA",
  "directive": "CONTINUE|FIX|HOLD",
  "summary": "一句话说明",
  "instructions": "具体指令（详细步骤）"
}
```

**directive 值**:
- `CONTINUE`: 可以继续工作
- `FIX`: 修复指定问题
- `HOLD`: 停止所有写入，等待审查

### 监控命令

```bash
# CC 最新输出
ls -lt /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox | head -5

# 仓库最新状态
git -C /Users/panyao/Desktop/Biomimetic-design-library rev-parse --short HEAD
git -C /Users/panyao/Desktop/Biomimetic-design-library log --oneline -5
git -C /Users/panyao/Desktop/Biomimetic-design-library diff --stat

# 读取 CC 最新 STATUS
cat /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox/<latest-file>.json

# 验证 from_source 计数
cd /Users/panyao/Desktop/Biomimetic-design-library && python3 -c "
import json, glob
CC_KEYS = ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works', 'boundary_conditions', 'transferable_principle']
total = 0; from_source = 0
for f in glob.glob('prototypes_db/*.json'):
    with open(f) as fp:
        d = json.load(fp)
        for m in d.get('mechanisms', []):
            cc = m.get('causal_chain', {})
            for key in CC_KEYS:
                elem = cc.get(key)
                if isinstance(elem, dict):
                    total += 1
                    if elem.get('basis') == 'from_source':
                        from_source += 1
print(f'from_source: {from_source}/{total} ({from_source/total*100:.1f}%)')
"

# 跑验证器
cd /Users/panyao/Desktop/Biomimetic-design-library
python3 tools/validate_consistency.py
python3 tools/check_causal_chain.py
python3 tools/check_chimera.py
python3 tools/check_boundary_guardrail.py
```

---

## 五、证据提升质量标准

**每个 from_source 升级必须包含**:
1. **source**: 真实 DOI/专利号/标准号
2. **locator**: 精确页码（page N）
3. **quote**: 短引文（≤200 字符）
4. **scope_match**: 声明中 2+ 关键词出现在引文中

**禁止**:
- 模糊定位（如 "visual_cache page text match"）
- 长 OCR 块替换语义文本
- 单关键词匹配
- 证据标签膨胀

**模型路由**:
- PDF/OCR/视觉提取: `mimo-v2.5`
- 文本推理/source-to-claim: `mimo-v2.5-pro`

**数据结构说明**:
- 每个原型 JSON 在 `prototypes_db/*.json`
- 每个原型有多个 `mechanisms`
- 每个 mechanism 有 `causal_chain`，包含 6 个子元素:
  - `pollutant_feature`, `bio_structure`, `interaction`, `why_it_works`, `boundary_conditions`, `transferable_principle`
- 每个子元素可以是 dict，有 `text`, `basis`, `source`, `locator`, `quote` 等字段
- `basis` 字段值: `from_source`（有来源）或 `llm_inferred`（推断）

---

## 六、今天下午工作流程

### 步骤 1: 启动 CC（立即执行）

写第一条指令给 CC:

```bash
cat > /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/20260623T152000Z-codex-directive-V1A-CONTINUE-MACRO-BATCH.json << 'DIRECTIVE'
{
  "protocol_version": 1,
  "message_id": "CODEX-20260623T152000Z-DIRECTIVE-V1A-CONTINUE-MACRO-BATCH",
  "created_at": "2026-06-23T15:20:00+08:00",
  "source": "COWORK_ACTING_SUPERVISOR",
  "type": "DIRECTIVE",
  "project_head": "dd3b8ae",
  "directive": "CONTINUE",
  "summary": "继续 evidence uplift macro-batch",
  "instructions": "处理下一批 10-15 个有本地 PDF 的原型。优先处理 from_source 比例低但 PDF 充足的。每 30-45 分钟写一次 STATUS 到 cc-outbox。不要每波都停等审批，除非遇到硬阻塞。4-6 小时后集中审查。质量要求：每条升级必须有精确页码 + 短引文<200字符 + scope_match 2+关键词。"
}
DIRECTIVE
```

### 步骤 2: 监控 CC（循环执行）

**每 15-30 分钟检查**:
1. 跑监控命令（见第四节）
2. 判断是否需要干预

**判断规则**:
- 有新 STATUS → 读取并评估
- 有新 commit 且验证器绿 → 不需要干预
- CC 停了 30+ 分钟 → 发 nudge（CONTINUE 指令）
- 验证器红 → 发 FIX 或通知 Yao
- 遇到硬阻塞 → 发 FIX 或通知 Yao

### 步骤 3: 审查 STATUS

读取 CC 的 STATUS JSON，检查:
- `from_source` 数值是否合理
- `validators` 是否全绿
- `blocker` 字段是否有报告
- `head` 是否与仓库一致

### 步骤 4: 集中审查（4-6 小时后）

当 from_source 达到目标或 4-6 小时后:
1. 跑完整验证（见监控命令）
2. 抽查 5-10 条升级的准确性
3. 质量合格 → 通知 Yao 可以 review
4. 发现问题 → 回滚并调整策略

---

## 七、通知 Yao 的场景

**必须通知**:
- 验证器红灯
- 硬阻塞（大量 PDF 缺失、OCR 系统故障）
- CC 反复不响应 nudge
- 证据质量问题（抽查发现伪造/不准确）

**不需要通知**:
- CC 正常工作
- 小问题已修复
- from_source 稳步提升

---

## 八、关键文件

- **项目指南**: `/Users/panyao/Desktop/Biomimetic-design-library/CLAUDE.md`
- **Mailbox 协议**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/PROTOCOL.md`
- **CC Goal Addendum**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/CC-LONG-GOAL-ADDENDUM.md`
- **原型数据库**: `/Users/panyao/Desktop/Biomimetic-design-library/prototypes_db/`
- **文献库**: `/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库/`

---

## 九、示例场景

### 场景 A: CC 正常工作

你检查:
```bash
ls -lt /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox | head -3
```
输出显示 15 分钟前有新 STATUS。你读取 STATUS，发现 from_source 从 21.8% 提升到 25%，验证器全绿。

**你的行动**: 不需要做任何事，继续监控。

### 场景 B: CC 停了

你检查:
```bash
ls -lt /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox | head -3
```
输出显示最后 STATUS 是 40 分钟前。仓库 HEAD 也没变。

**你的行动**: 发 nudge 指令:
```bash
cat > /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/$(date -u +%Y%m%dT%H%M%SZ)-codex-directive-NUDGE.json << 'DIRECTIVE'
{
  "protocol_version": 1,
  "message_id": "CODEX-$(date -u +%Y%m%dT%H%M%SZ)-DIRECTIVE-NUDGE",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "source": "COWORK_ACTING_SUPERVISOR",
  "type": "DIRECTIVE",
  "project_head": "<current HEAD>",
  "directive": "CONTINUE",
  "summary": "Nudge: 继续 macro-batch",
  "instructions": "你已停止 40 分钟。立即继续处理下一批原型，不要等审批。"
}
DIRECTIVE
```

### 场景 C: 验证器红灯

你检查验证器:
```bash
cd /Users/panyao/Desktop/Biomimetic-design-library
python3 tools/validate_consistency.py
```
输出显示 5 个 errors。

**你的行动**: 
1. 读取错误详情
2. 发 FIX 指令让 CC 修复
3. 通知 Yao

---

## 十、立即开始

现在请执行:
1. 读取上面的"步骤 1"指令，立即写入 codex-outbox 启动 CC
2. 等待 15-30 分钟后检查 CC 是否响应
3. 开始监控循环

**记住**: 你是监督员，不直接修改代码。你的工作是通过 mailbox 指令推动 CC 工作，并在需要时通知 Yao。
