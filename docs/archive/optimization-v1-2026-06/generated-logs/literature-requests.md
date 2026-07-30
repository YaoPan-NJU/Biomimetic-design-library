# Phase 8 — C 档文献检索请求清单

> 以下 5 个原型本地无对口文献，需学生下载后按 A 档核验。

| prototype_id | 待支撑的断言 | 为何高风险 | 检索词（中文） | 检索词（English 布尔式） | 建议数据库 | 期望证据 |
|---|---|---|---|---|---|---|
| coral-skeleton | 珊瑚骨骼 CaCO₃ 可通过离子交换/沉淀去除重金属和磷酸盐 | 若机制不成立，ADRMATS 可能选出在目标工况下溶解的珊瑚基材料 | 珊瑚骨骼 羟基磷灰石 吸附 重金属 | ("coral skeleton" OR "coralline") AND ("hydroxyapatite" OR "CaCO3") AND ("adsorption" OR "removal") AND ("heavy metal" OR "phosphate") | Web of Science | CaCO₃/羟基磷灰石吸附重金属的实验数据 |
| coral-skeleton | 煅烧温度影响珊瑚 CaCO₃ 晶型转变和吸附性能 | 温度参数缺失导致无法指导材料合成 | 珊瑚 煅烧 晶型 吸附 | ("coral") AND ("calcination" OR "thermal treatment") AND ("crystal phase" OR "aragonite") AND ("adsorption") | Web of Science | 煅烧条件→晶型→吸附性能 |
| magnetic-bacteria | 趋磁细菌磁小体可作为磁性吸附剂实现磁分离回收 | 若磁小体不稳或功能化困难，材料无法回收 | 趋磁细菌 磁小体 吸附 功能化 | ("magnetotactic bacteria" OR "magnetosome") AND ("adsorption" OR "functionalization") AND ("heavy metal" OR "water treatment") | Web of Science | 磁小体提取、功能化、吸附性能 |
| magnetic-bacteria | 磁小体外膜功能基团可捕获污染物 | 功能基团密度和选择性未知 | 磁小体 外膜 表面修饰 | ("magnetosome") AND ("surface modification" OR "functionalization") AND ("catechol" OR "amine") AND ("adsorption") | Web of Science | 磁小体表面功能化数据 |
| pitcher-plant | 猪笼草 SLIPS 策略在高流速下润滑液可能被冲刷 | 若润滑液不稳，防污应用会失效 | 猪笼草 超滑 润滑液 稳定性 | ("Nepenthes" OR "pitcher plant") AND ("SLIPS" OR "slippery liquid-infused") AND ("stability" OR "durability" OR "lubricant loss") | Web of Science | 润滑液流失速率和补充机制 |
| lobster-exoskeleton | 壳聚糖珠(Chitosan beads)六种吸附机制 | 需要 chitosan beads 吸附重金属的对口论文 | 壳聚糖珠 吸附 重金属 机制 | ("chitosan bead" OR "chitosan sphere") AND ("adsorption" OR "mechanism") AND ("heavy metal" OR "Cu" OR "Pb" OR "Cd") | Web of Science | chitosan beads 的吸附机制分析 |
| spider-silk | 蜘蛛丝抗污染机制 | 需要蜘蛛丝蛋白抗污的对口论文 | 蜘蛛丝 抗污染 蛋白 | ("spider silk" OR "spidroin") AND ("antifouling" OR "anti-biofouling") AND ("protein" OR "surface") | Web of Science | 蜘蛛丝抗污性能数据 |
| dna-aptamer | DNA适配体在不同pH/温度/离子强度下的结合稳定性 | 适配体构象敏感，失效边界未知可能导致错误选材 | DNA适配体 稳定性 温度 pH 离子强度 | ("DNA aptamer") AND ("stability" OR "thermal stability" OR "pH stability") AND ("binding" OR "affinity" OR "dissociation") | Web of Science | 适配体在不同工况下的结合常数和构象稳定性 |

## 下载后操作

1. PDF 放入 `仿生文献库/` 对应目录
2. 更新对应 prototype JSON 的 `source_file` 字段
3. 按 A 档核验：开 PDF 定位断言 → 填 `locator` + `quote` → `verification=verified`
