# Phase 8 — C 档文献检索请求清单

> coral-skeleton 和 pitcher-plant 本地无文献，需学生下载后按 A 档核验。

| prototype_id | 待支撑的边界断言 | 为何高风险 | 检索词（中文） | 检索词（English 布尔式） | 建议数据库 | 期望证据 |
|---|---|---|---|---|---|---|
| coral-skeleton | 珊瑚骨骼 CaCO₃ 可通过离子交换/沉淀去除重金属和磷酸盐 | 若机制不成立，ADRMATS 可能选出在目标工况下溶解的珊瑚基材料 | 珊瑚骨骼 羟基磷灰石 吸附 重金属 | ("coral skeleton" OR "coralline") AND ("hydroxyapatite" OR "CaCO3") AND ("adsorption" OR "removal") AND ("heavy metal" OR "phosphate") | Web of Science / Scopus | CaCO₃/羟基磷灰石吸附重金属的实验数据 |
| coral-skeleton | 煅烧温度影响珊瑚 CaCO₃ 晶型转变和吸附性能 | 温度参数缺失导致无法指导材料合成 | 珊瑚 煅烧 晶型 吸附 | ("coral") AND ("calcination" OR "calcining" OR "thermal treatment") AND ("crystal phase" OR "aragonite" OR "calcite") AND ("adsorption") | Web of Science | 煅烧条件→晶型→吸附性能的定量关系 |
| pitcher-plant-slippery-surface | 猪笼草 SLIPS 策略在高流速下润滑液可能被冲刷 | 若润滑液不稳，防污应用会失效 | 猪笼草 超滑 润滑液 稳定性 | ("Nepenthes" OR "pitcher plant") AND ("SLIPS" OR "slippery liquid-infused") AND ("stability" OR "durability" OR "lubricant loss") AND ("anti-fouling" OR "anti-icing") | Web of Science | 润滑液流失速率和补充机制 |

## 中英文检索词说明

英文检索词均为可直接粘贴到数据库搜索栏的布尔式。

## 下载后操作

1. PDF 放入 `仿生文献库/` 对应目录
2. 更新对应 prototype JSON 的 `source_file` 字段
3. 按 A 档核验：开 PDF 定位断言 → 填 `locator` + `quote` → `verification=verified`
