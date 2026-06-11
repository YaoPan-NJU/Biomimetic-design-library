# AI 协作监督协议

> 适用范围：本仓库 ADRMATS 可交付化阶段
> 角色：Codex 负责监督、复核、决策；coffee-cli 负责执行、提交、推送、回报
> 目标：让工作沿 `docs/ADRMATS_DELIVERY_PLAN.md` 连续推进，但每个关键节点都有证据、可复查、可暂停。

---

## 1. 三个文件的职责

| 文件 | 谁写 | 谁读 | 用途 |
|---|---|---|---|
| `docs/AI_COORDINATION_PROTOCOL.md` | 人/Codex | Codex + coffee-cli | 固定协作规则，不频繁改 |
| `docs/AI_SUPERVISOR_DIRECTIVE.md` | Codex | coffee-cli | 当前监督决策：继续、暂停、修复、补 push、人工复查 |
| `docs/AI_AGENT_PROGRESS.md` | coffee-cli | Codex + 人 | 当前执行状态、命令结果、commit、风险、下一步 |

`AI_SUPERVISOR_DIRECTIVE.md` 的优先级高于本地 AI 的自我计划。若它与 coffee-cli 当前计划冲突，以监督指令为准。

---

## 2. coffee-cli 的工作循环

coffee-cli 必须按以下循环工作：

1. 开始工作前读取：
   - `docs/ADRMATS_DELIVERY_PLAN.md`
   - `docs/AI_COORDINATION_PROTOCOL.md`
   - `docs/AI_SUPERVISOR_DIRECTIVE.md`
   - `docs/AI_AGENT_PROGRESS.md`
2. 如果监督指令状态是 `PAUSE`、`FIX_REQUIRED`、`PUSH_REQUIRED`、`HUMAN_REVIEW_REQUIRED`，先执行监督指令，不得进入下一个 milestone。
3. 每完成一个关键动作，更新 `docs/AI_AGENT_PROGRESS.md`。
4. 每完成一个 milestone，必须：
   - 运行该 milestone 的验收命令；
   - commit；
   - push；
   - 更新 `docs/AI_AGENT_PROGRESS.md`；
   - 停在人工/Codex 复查点，不自动跨 milestone 继续。

---

## 3. 状态枚举

监督状态只能使用以下值：

| 状态 | 含义 | coffee-cli 行为 |
|---|---|---|
| `CONTINUE` | 可继续当前 milestone | 按 delivery plan 执行 |
| `PAUSE` | 暂停 | 不再改文件，更新 progress 后等待 |
| `FIX_REQUIRED` | 发现必须修的问题 | 只修指定问题，不扩展范围 |
| `PUSH_REQUIRED` | 有 commit 未推送 | 先 push，再回报 |
| `HUMAN_REVIEW_REQUIRED` | 进入人工复查 | 停止进入下一 milestone |
| `DELIVERY_COMPLETE` | v0.1 已交付 | 停止执行 |

---

## 4. 必须保留的证据

每次回报都必须包含：

- 当前 milestone
- 最新 commit hash
- 是否已 push
- 工作区是否干净
- 实际运行命令
- 通过项
- 失败项
- 剩余风险
- 下一步只做什么

不允许用“已完成 Phase”代替证据。

---

## 5. 禁止事项

- 禁止手写 brief 冒充接口输出。
- 禁止 feature-based inspiration 伪装成 direct evidence。
- 禁止未通过验收脚本就进入下一个 milestone。
- 禁止 README、HANDOFF、ADRMATS_INTEGRATION、DELIVERY_PLAN 维护互相矛盾的状态。
- 禁止批量扩库来掩盖接口契约、schema、标准化、验证脚本的问题。
