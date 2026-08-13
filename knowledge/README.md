# 规范化知识层

`graph.jsonl` 是本库当前唯一的机器可读事实源；`schema.json` 定义实体类型、关系类型和受控词表。

每行记录是以下三种操作之一：

```json
{"op":"create","id":"...","type":"...","properties":{}}
{"op":"update","id":"...","properties":{}}
{"op":"relate","from":"...","rel":"...","to":"...","properties":{}}
```

ID 必须稳定、可读，并使用小写字母、数字和下划线。已发布 ID 不因名称变化而修改。

## 内容纪律

- `BiologicalPrototype` 表示自然原型，`BiologicalMechanism` 表示真正被借鉴的机制，两者不能混用。
- `DesignMapping` 是核心知识单元：它说明一种机制在特定设计问题和工况下如何转译为工程模块、杠杆和参数。
- `DesignModule` 使用统一结构表达材料、微生物、组件、反应器、系统和控制层。
- `AssemblyPattern` 只组合已有模块，并显式记录模块接口、约束与验证状态。
- `EvidenceClaim` 必须引用 `EvidenceSource`；本地构思文档只能支撑“设计假设存在”，不能使工程结论变成已验证。
- ML 或 LLM 生成的候选默认是 `unverified`，通过文献、仿真、实验或实测后才允许升级。

## 常用命令

```powershell
python scripts/knowledge.py validate
python scripts/knowledge.py query --type DesignModule --where layer=control
python scripts/knowledge.py design --consumer reactor_design --process A2O --problem low_cn
python scripts/knowledge.py show --id assembly_adaptive_a2o_reactor
python scripts/knowledge.py generate
```

`generated/` 中的矩阵视图由脚本生成，请勿手工维护。
