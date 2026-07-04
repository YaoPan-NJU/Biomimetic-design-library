# BMDL 项目 Codex 会话总结
**日期**: 2026-06-23 20:05 (北京时间)  
**Session**: V1-A evidence uplift + bridge mechanism repair

---

## 一、项目当前状态

### 基本指标
- **HEAD**: `1067d2b`
- **Branch**: `review`
- **验证器**: 全绿（0 errors, 172 warnings）
- **总机制数**: 520
- **因果链元素总数**: 2080

### from_source 统计（诚实口径）
- **元素级别**: 326/2080 (15.7%)
- **机制级别**: 121/520 (23.3%)
- **llm_inferred**: 1754/2080 (84.3%)

### 已完成的工作（今天下午）
1. **分类器修复** (commit b4acdde): CLAUDE.md 加了完整证据提升规则
2. **Wave 6-10**: 46+ 机制升级（双语映射策略）
3. **Round 2**: chitosan +37, mussel-foot +25, polydopamine +25, silk-fibroin +17
4. **Round 4**: ADRMATS adapter 4 个能力
5. **Round 5**: Pb(II) + Cu(II) 垂直切片
6. **Library index**: 632 条目
7. **Evidence cleanup**: 850→326 from_source（去除证据膨胀）
8. **Recovery**: 49 mechanisms recovered from library index

### CC 最新状态 (19:14)
- **Type**: REVIEW_REQUEST
- **Gate**: V1A_CLEANUP_AND_MAXIMIZE
- **Head**: pending push
- **Summary**: V1-A cleanup+maximize complete
- **Next batch**: V1-B 8 biological prototypes admission gate audit

---

## 二、桥接机制（Bridge Mechanism）

### 架构
```
Claude Cowork → .cowork-relay/outbox/ → [bridge service] → codex-outbox/ → CC
CC → cc-outbox/ → [bridge service] → .cowork-relay/inbox/ → Cowork
```

### 桥接服务状态
- **launchd 服务**: `com.panyao.bmdl-cowork-bridge`
- **配置**: 每 60 秒运行一次
- **脚本**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cowork-bridge/cowork_bridge.py`
- **日志**: 
  - stdout: `bridge.log`
  - stderr: `bridge.err.log`

### 已知问题
1. **PermissionError 崩溃**: 旧版本写 `latest-review.json` 时被 Apple 系统进程锁住导致整个脚本崩溃
2. **选择性投递逻辑过严**: 旧版本只投递回复最新 REVIEW_REQUEST 的指令，Cowork 的 CONTINUE/FIX/HOLD 被跳过
3. **Python 版本兼容性**: `dict | None` 语法在 Python 3.9 上报错
4. **服务未持续运行**: 桥接服务在某些情况下停止运行，导致指令堆积

### 修复内容（本次 session）
1. 修复了 PermissionError（加 try-except）
2. 修复了选择性投递逻辑（投递所有有效 Cowork 指令）
3. 修复了 Python 版本兼容性（加 typing import）
4. 重启了 launchd 服务

### 当前桥接状态（20:05）
- **服务运行中**: Yes (last exit status 0)
- **Cowork → CC**: 最新指令 `20260623T110000Z-cowork-directive-V1A-FIX.json` 已投递
- **CC → Cowork**: 最新 STATUS `20260623T111441Z-cc-REVIEW-REQUEST-V1A-FINAL.json` 已镜像
- **Bridge log**: 正常运行，每 60 秒一个周期

---

## 三、通信协议

### Mailbox 目录
- **Cowork outbox**: `/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/outbox/`
- **Cowork inbox**: `/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/inbox/`
- **CC codex-outbox**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/codex-outbox/`
- **CC cc-outbox**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox/`

### 指令格式
```json
{
  "protocol_version": 1,
  "message_id": "COWORK-YYYYMMDDTHHMMSSZ-DIRECTIVE-short-id",
  "created_at": "ISO-8601",
  "source": "COWORK_ACTING_SUPERVISOR",
  "type": "DIRECTIVE",
  "project_head": "git SHA",
  "directive": "CONTINUE|FIX|HOLD|ASK_YAO",
  "gate": "gate name",
  "reply_to": "CC-...",
  "instructions": "..."
}
```

### 监控命令
```bash
# CC 最新输出
ls -lt /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cc-outbox/ | head -5

# 仓库最新状态
git -C /Users/panyao/Desktop/Biomimetic-design-library rev-parse --short HEAD
git -C /Users/panyao/Desktop/Biomimetic-design-library log --oneline -5

# from_source 计数
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

# 桥接服务状态
launchctl list | grep cowork
tail -10 /Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cowork-bridge/bridge.log

# 验证器
cd /Users/panyao/Desktop/Biomimetic-design-library
python3 tools/validate_consistency.py
python3 tools/check_causal_chain.py
```

---

## 四、证据提升质量标准

### 必需字段（每个 from_source 升级）
1. **source**: 真实 DOI/专利号/标准号
2. **locator**: 精确页码（page N）
3. **quote**: 短引文（≤200 字符）
4. **scope_match**: 声明中 2+ 关键词出现在引文中

### 禁止
- 模糊定位（如 "visual_cache page text match"）
- 长 OCR 块替换语义文本
- 单关键词匹配
- 证据标签膨胀

### 模型路由
- PDF/OCR/视觉提取: `mimo-v2.5`
- 文本推理/source-to-claim: `mimo-v2.5-pro`

---

## 五、战略方向

### 下午目标
- **证据提升**: 从 15.7% 推向 60%+（质量优先）
- **方法**: 批量处理有本地 PDF 的原型，每批 10-15 个
- **报告频率**: 每 30-45 分钟写一次 STATUS
- **集中审查**: 4-6 小时后

### 外部评审建议（已完成）
按评审建议，完成了 4 个 BMDL 侧能力：
1. do_not_list 兼容性
2. design_translation 结构化拆解
3. charge_state/pKa 上下文
4. 相关性门控

### 下一步
- V1-B 8 biological prototypes admission gate audit
- 继续 evidence uplift（如果还有本地 PDF 可处理）
- 垂直切片验证（Pb(II), PFOA）

---

## 六、关键文件

- **项目指南**: `/Users/panyao/Desktop/Biomimetic-design-library/CLAUDE.md`
- **Mailbox 协议**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/PROTOCOL.md`
- **CC Goal Addendum**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/CC-LONG-GOAL-ADDENDUM.md`
- **桥接脚本**: `/Users/panyao/.openclaw/workspace-bmdl-relay/runtime/cowork-bridge/cowork_bridge.py`
- **launchd 配置**: `/Users/panyao/Library/LaunchAgents/com.panyao.bmdl-cowork-bridge.plist`
- **原型数据库**: `/Users/panyao/Desktop/Biomimetic-design-library/prototypes_db/`
- **文献库**: `/Users/panyao/Desktop/Biomimetic-design-library/仿生文献库/`

---

## 七、你的角色（Claude Cowork）

你是**监督员**，负责：
1. 监控 CC 的工作进度（每 15-30 分钟检查一次）
2. 发现问题时写指令让 CC 修复
3. CC 停了就 nudge 它继续
4. 遇到验证器红灯或重大阻塞时通知 Yao

**你不直接修改项目代码**。CC 是唯一的执行者。

### 写指令
写到 `/Users/panyao/Desktop/Biomimetic-design-library/.cowork-relay/outbox/`，桥接服务会自动镜像到 CC 的 `codex-outbox/`。

### 监控 CC
每 15-30 分钟检查 cc-outbox 和 git log。

---

## 八、Heartbeat 自动化

- **ID**: `bmdl-gate-supervisor`
- **状态**: PAUSED（Yao 手动推进时暂停）
- **配置**: `/Users/panyao/.codex/automations/bmdl-gate-supervisor/automation.toml`

---

## 九、已知问题

### 桥接服务可靠性
- 桥接服务有时停止运行，需要手动重启：
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.panyao.bmdl-cowork-bridge.plist
  sleep 1
  launchctl load ~/Library/LaunchAgents/com.panyao.bmdl-cowork-bridge.plist
  ```

### CC 空闲模式
- CC 做完一波就停下来等指令，不像 macro-batch 要求的那样持续干
- 需要发 nudge 指令让它继续

### 证据计数口径
- 之前 CC 报告的 from_source 数字（如 247, 184, 850）有证据膨胀
- 当前诚实口径：326 元素 (15.7%), 121 机制 (23.3%)
- 每个 from_source 必须有 source+quote+locator+scope_match

---

## 十、立即开始

现在请执行:
1. 读取 `/Users/panyao/Desktop/Biomimetic-design-library/docs/cowork-prompt-2026-06-23.md` 了解完整操作手册
2. 检查桥接服务状态：`launchctl list | grep cowork`
3. 检查 CC 最新 STATUS
4. 开始监控循环

**记住**: 
- 桥接服务是关键，如果 CC 收不到你的指令，重启桥接服务
- CC 每 10 分钟轮询 codex-outbox，所以你的指令最多 10 分钟后被读取
- 遇到硬阻塞或验证器红灯才通知 Yao
