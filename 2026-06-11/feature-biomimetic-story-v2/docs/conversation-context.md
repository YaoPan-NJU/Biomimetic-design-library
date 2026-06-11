# 仿生设计库项目 -- 完整对话上下文

> 本文档记录了从项目启动至今的所有对话上下文、设计决策和用户反馈。
> 目的：跨设备接力时，新会话可快速恢复项目认知。
> 最后更新：2026-06-04

---

## 一、项目背景与目标

### 1.1 项目概述
**项目名称**: Biomimetic Design Library（仿生设计库）
**GitHub**: https://github.com/YaoPan-NJU/Biomimetic-design-library
**核心目标**: 构建一个 AI 驱动的仿生水处理吸附材料设计系统的知识库。从341篇PDF文献中提取参数，填充33个仿生原型的结构化知识。

### 1.2 项目结构
```
Biomimetic-design-library/
├── prototypes/          # 33+个原型目录 (每个含prototype.md)
├── taxonomy/            # 三层分类体系 (organisms/pollutants/mechanisms)
├── templates/           # 原型模板
├── feature-mapping.json # 4层特征映射 (156条权重条目)
├── extraction/          # 文献提参流水线 (本项目核心)
│   ├── pipeline/        # 4个阶段实现
│   ├── prompts/         # 4个Jinja2 LLM提示模板
│   ├── tests/           # 32个测试
│   ├── config.py        # 配置 (含3路API负载均衡)
│   ├── llm_client.py    # 统一LLM客户端 (round-robin)
│   ├── run_pipeline.py  # CLI入口
│   └── .env             # API keys (不入库)
└── docs/                # 设计文档、执行报告、管理看板
```

### 1.3 用户核心偏好
- **对话语言**: 中文（用户明确要求："我用中文跟你对话"）
- **并行策略**: 不同API key + 不同模型同时跑同一种任务（不是同一个key分多路）
- **效率优先**: 额度充足，随意使用
- **先不管专利**: "先不用管专利交付的问题，我们先把这个库做全做好"
- **原型数量**: 用户认为30个可能少了，后续要迭代优化

---

## 二、对话历史完整记录

### Session 1（上一轮对话，已压缩）

#### 2.1 项目部署
- **用户请求**: 克隆 Biomimetic-design-library 并部署所有分支
- **结果**: 克隆完成，2个分支 (main, feature/biomimetic-story-v2)

#### 2.2 Superpowers Skills 安装
- **用户请求**: 安装 "superpowers" 为用户级 skills
- **结果**: 从 skills.sh 找到 obra/superpowers，安装全部14个skills到 ~/.qoderwork/skills/

#### 2.3 文件交互规则讨论
- **用户请求**: 了解 QoderWork 的文件访问能力
- **结果**: 对话解释了文件访问规则和交互方式

#### 2.4 项目分析与文献选择讨论（brainstorming）
- **用户请求**: 分析仿生设计库项目，讨论文献选择问题
- **文献库位置**: `/Users/panyao/Desktop/仿生文献库`
- **用户识别的问题**:
  1. 现有文献太偏"材料→应用"视角，缺少"生物→设计→材料"视角
  2. 方法论和标准文献缺失
  3. 搜索方向需要调整

#### 2.5 策略讨论（多轮 AskUserQuestion）
- **确认**: 三个问题都存在
- **策略**: 并行推进（利用现有文献 + 定向补充）
- **补充类型**: 方法论与标准、仿生设计综述、跨原型比较研究、仿生设计案例研究（全部4种）
- **原型范围**: 全部33个原型，不分优先级
- **设计方式**: 同步设计文献提参和提取流程
- **迭代方式**: Approach C（迭代细化）
- **用户关键建议**: 结合粗扫 + 精读样本来判断广度和深度（重要设计输入）

#### 2.6 API 配置
用户提供了三个API endpoint：
1. **阿里云 Coding Plan**: qwen3.6-plus (多模态), `https://coding.dashscope.aliyuncs.com/v1`
2. **阿里云按量付费**: qwen3.7-max (单模态), `https://dashscope.aliyuncs.com/compatible-mode/v1`
3. **小米 MiMo Token Plan**: Mimo-v2.5 (多模态), `https://token-plan-cn.xiaomimimo.com/v1`

#### 2.7 设计文档与实施计划
- **设计文档**: `docs/extraction-pipeline-design.md`
- **实施计划**: `docs/extraction-pipeline-plan.md`（13个任务）

#### 2.8 代码实现
- **结果**: 27个文件创建，4465行代码，31个测试全部通过
- **提交到**: feature/biomimetic-story-v2 分支

#### 2.9 项目交付
- 复制到桌面: `/Users/panyao/Desktop/Biomimetic-design-library/`
- 推送到 GitHub (通过 gh CLI)

#### 2.10 API 配置与连通性测试
- 用户在桌面 .env 填入 API key
- 同步到工作区
- 三个API全部连通

#### 2.11 Phase 1 首跑与并行问题
- **第一次**: 串行，太慢
- **第二次**: ThreadPoolExecutor 8×5=40并发 → 146/149 429错误
- **修复**: 加指数退避重试，降到3×2=6并发

#### 2.12 用户关键反馈（并行策略纠正）
> "我说的并行不是同一个Key分好几路，而是不同的key、不同的模型可以一起跑同一种任务，比如phase可以同时跑3.6-plus、3.7-max和mimo-v2.5"

这个反馈导致了架构重设计：
- `MODEL_ROUTING` 从 `str` 改为支持 `list`
- `LLMClient.from_task_type()` 加 round-robin 计数器
- 并发提升到 6×3=18（负载分散到3个API）

### Session 2（本轮对话）

#### 2.13 Phase 1 三路负载均衡重跑
- **第一次重跑**: 149/149成功，64次重试，301秒（但多个旧进程同时跑，部分文件混杂旧数据）
- **清理后重跑**: 
  - 优化：429重试时显式切换到不同provider（`exclude_provider`参数）
  - 结果：149/149成功，0错误，33次重试，324秒
  - Provider分布：dashscope 69, mimo 62, coding_plan 18

#### 2.14 Phase 1 质量评估
- **子任务分析发现**:
  - 30个JSON文件，149条提取全部成功
  - chitosan-adsorbent 和 chlorella 之前完全失败 → 优化后5/5成功
  - 机制字段65.8%为空（最大短板）
  - 定量数据极度匮乏（qmax 5.4%, 去除率 7.4%）
  - 5个原型完全无论文映射

#### 2.15 用户确认继续
- 用户评价：广度基本ok，但30个原型可能少了
- 指示：继续后续 Phase 2-4

#### 2.16 Phase 2-4 代码改造
- **config.py**: `deep_read` 和 `biomimetic_extract` 改为三路负载均衡
- **phase2_gap_analysis.py**: 加 ThreadPoolExecutor 并发 (6路) + 429重试 + provider切换
- **phase4_deep_extract.py**: 加并发 (4路) + 重试 + None安全访问 + qmax数值解析
- **writer.py**: feature-mapping.json 不存在时优雅跳过
- **测试更新**: 路由断言适配新配置，新增 exclude_provider 测试

#### 2.17 Phase 2 执行
- 结果：30/30原型分析完成，0错误，777秒
- 产出：30个 gap report JSON + supplementation-plan.md

#### 2.18 Phase 3 执行
- 结果：瞬间完成，336条搜索查询
- 分组：第9组-方法论(1条) + 第10组-仿生综述(322条) + 第11组-跨原型比较(13条)

#### 2.19 Phase 4 执行
- **第一次**: 5个ERROR - `'NoneType' object has no attribute 'get'`
  - 原因：LLM返回的 `performance_data` 字段为 null，`.get()` 在 None 上调用失败
  - 修复：加 None 安全访问 (`(s.get("performance_data") or {})`)
- **第二次**: `ValueError: could not convert string to float: '318.47 mg/g'`
  - 原因：qmax 值带单位，float() 无法解析
  - 修复：添加 `_safe_float()` 辅助函数，正则提取数字部分
- **第三次**: `FileNotFoundError: feature-mapping.json`
  - 原因：PROJECT_DIR 解析为 extraction/ 而非项目根
  - 修复：.env 中 PROJECT_DIR 改为绝对路径
- **最终运行**: 30/30全部成功，113个权重赋值，30个验证告警，1158秒

#### 2.20 全流程提交与推送
- 提交到 feature/biomimetic-story-v2
- 同步到桌面
- 32个测试全部通过

#### 2.21 执行报告与管理看板
- `docs/execution-report-2026-06-04.md`: 完整执行监控报告
- `docs/project-board.md`: 项目管理看板（已完成/待办/里程碑/接力指南）

#### 2.22 项目管理分支
- 新建 `project/tracking` 分支
- 推送到 GitHub

#### 2.23 对话上下文归档（本次操作）
- 创建本文档 `docs/conversation-context.md`
- 推送到 `project/tracking` 分支

---

## 三、关键技术决策记录

### 3.1 架构决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 流水线架构 | 4阶段串行 | 粗扫→差距→补充→深提，每阶段输入依赖上阶段输出 |
| 并发模型 | ThreadPoolExecutor | Python 3.9 原生支持，LLM调用为I/O密集 |
| 负载均衡 | Round-robin across providers | 用户要求不同API同时跑同一种任务 |
| 重试策略 | 指数退避 + provider切换 | 429时自动切换到不同API，避免重复命中限流 |
| LLM接口 | OpenAI-compatible SDK | 三个provider都兼容OpenAI接口 |
| PDF解析 | PyMuPDF (fitz) | 速度快，兼容性好 |
| 提示模板 | Jinja2 | 灵活，支持变量注入 |

### 3.2 模型路由策略

```python
MODEL_ROUTING = {
    "coarse_scan": ["coding_plan", "dashscope", "mimo"],       # 三路并行
    "performance_extract": ["coding_plan", "dashscope", "mimo"], # 三路并行
    "deep_read": ["coding_plan", "dashscope", "mimo"],          # 三路并行
    "biomimetic_extract": ["coding_plan", "dashscope", "mimo"], # 三路并行
    "weight_assign": "dashscope",      # 单路：推理打分需要一致性
    "multimodal_extract": "mimo",      # 单路：Mimo-v2.5 表格/图片
}
```

### 3.3 并发参数

| 阶段 | 原型并发 | 论文并发 | 说明 |
|------|----------|----------|------|
| Phase 1 | 6 | 3 | 6×3=18路，分散到3个API |
| Phase 2 | 6 | 3(内部) | 每个原型最多3篇精读 |
| Phase 4 | 4 | 3(内部) | 4×3=12路 + weight_assign |

### 3.4 已知Bug与修复历史

| Bug | 原因 | 修复 |
|-----|------|------|
| Python 3.9 类型注解不兼容 | `int \| None` 语法 | 添加 `from __future__ import annotations` |
| OpenAI SDK 空key报错 | .env未填 | 添加 `sk-placeholder` fallback |
| 429 大面积限流 | 40并发打单API | 降并发 + 三路负载均衡 |
| NoneType.get() | LLM返回null字段 | `(s.get("x") or {})` 安全访问 |
| float解析带单位 | "318.47 mg/g" | `_safe_float()` 正则提取 |
| feature-mapping.json找不到 | PROJECT_DIR解析错误 | .env改为绝对路径 |

---

## 四、用户反馈与偏好汇总

### 4.1 关键反馈（原文）

1. > "我用中文跟你对话"
2. > "前面一长段分析有很多，而且分点了，怎么用中文写的就很简略了？" — 中文分析不能比英文简略
3. > "先不用管专利交付的问题，我们先把这个库做全做好"
4. > "我说的并行不是同一个Key分好几路，而是不同的key、不同的模型可以一起跑同一种任务"
5. > "你帮我跑，但是由我先自己填好api key，然后你帮我自动测试，遇到问题就分析解决并重试继续，你对我的运行结果负责"
6. > "我感觉目前并行还不够"
7. > "其实我还在想30个原型是不是少了点，没关系，后面再迭代优化"
8. > "请输出执行的监控报告及详细的结果分析报告"
9. > "我建议在github新建一个branch，同步任务设计、任务状态、结果、计划进度以及待办清单等，方便我在不同的设备接力任务"
10. > "包括我们之前对话的上下文，都压缩一下，一并上传到新的那个branch里面"

### 4.2 工作风格偏好
- 中文对话，分析不要简略
- 信任AI执行，但要对结果负责（自动测试+重试）
- 效率优先，额度充足
- 跨设备工作，需要GitHub同步
- 关注产出质量，要求详细报告

---

## 五、当前项目状态快照

### 5.1 分支状态
- `main`: 原始项目骨架
- `feature/biomimetic-story-v2`: 全部代码 + 30个prototype.md + 执行报告 + 管理看板
- `project/tracking`: 项目管理文档（执行报告 + 看板 + 本上下文文档）

### 5.2 数据产出状态
- Phase 1 粗扫: 30个profile JSON ✅
- Phase 2 差距分析: 30个gap report ✅
- Phase 3 补充计划: 336条搜索查询 ✅
- Phase 4 深度提取: 30个prototype.md ✅
- Feature Mapping: 156/156 权重已更新 ✅
- 仿生叙事章节: 全部"[待补充]" ❌ (需要补充文献)

### 5.3 待办任务（优先级排序）
1. **[P0]** 用Phase 3搜索查询补充文献（5个零覆盖原型 + 14个零直接论文原型）
2. **[P0]** 统一原型命名体系（30个粗扫ID vs 51个目录ID）
3. **[P0]** 补充文献后重跑Phase 4，填充仿生叙事
4. **[P1]** 优化间接映射逻辑（减少噪音）
5. **[P1]** 扩展原型数量至50+
6. **[P2]** 增加全文深度提取比例
7. **[P2]** 新兴污染物补充（微塑料、PFAS等）

### 5.4 关键文件路径
- **工作区**: `/Users/panyao/.qoderworkcn/workspace/mpzh27rt8uc58fyx/Biomimetic-design-library/`
- **桌面**: `/Users/panyao/Desktop/Biomimetic-design-library/`
- **文献库**: `/Users/panyao/Desktop/仿生文献库/`
- **API配置**: `extraction/.env` (需手动填入3个key)

### 5.5 快速恢复命令
```bash
# 在新设备上恢复
git clone https://github.com/YaoPan-NJU/Biomimetic-design-library.git
cd Biomimetic-design-library
git checkout feature/biomimetic-story-v2  # 代码分支
# 或
git checkout project/tracking  # 仅看管理文档

# 填入API key后运行
cd extraction
# 编辑 .env 填入 CODING_PLAN_API_KEY, DASHSCOPE_API_KEY, MIMO_API_KEY
python3 run_pipeline.py phase1 phase2 phase3 phase4
```

---

## 六、环境信息

- **Python**: 3.9.6 (macOS Xcode系统Python)
- **pip**: 需要 `pip3` 或 `python3 -m pip`
- **依赖**: openai, PyMuPDF(fitz), pdfplumber, jinja2, python-dotenv, pytest
- **安装命令**: `python3 -m pip install openai PyMuPDF pdfplumber jinja2 python-dotenv pytest`
- **OS**: macOS (darwin)
