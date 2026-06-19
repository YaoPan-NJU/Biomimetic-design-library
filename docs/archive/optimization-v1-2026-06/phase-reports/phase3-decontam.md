# Phase 3 — 污染处置日志

> 以下机制条目因主体与所在原型身份不一致（§1.5 chimera 判定）而被删除。

- mussel-foot-adhesion: 删除 mechanism "Mechanisms of Heavy Metal Removal by Nanocellulose" (命中 "cellulose")
- mussel-foot-adhesion: 删除 mechanism "盐浓度升高→静电屏蔽→焓值降低" (命中 "CNC")
- mussel-foot-adhesion: 删除 mechanism "π-π堆积vs氢键——PD-CNC对MO/RB/CV去除差异" (命中 "CNC")
- mussel-foot-adhesion: 删除 mechanism "ITC确认PD-CNC额外吸附→非纯静电" (命中 "CNC")
- mussel-foot-adhesion: 删除 mechanism "MB/RB/CV结构差异→选择性机制解释" (命中 "CNC")
- mussel-foot-adhesion: 删除 mechanism "天然生物质双亲材料：预润湿切换实现按需分离" (命中 "纤维素")
- spider-silk: 删除 mechanism "荷叶超疏水仿生：微纳层级结构+WCA/WSA" (命中 "荷叶")
- spider-silk: 删除 mechanism "水下超疏气/超亲气仿生：鱼鳞+荷叶" (命中 "荷叶")
- spider-silk: 删除 mechanism "仿荷叶PS纳米纤维/微球复合超疏水表面接触角" (命中 "荷叶")
- spider-silk: 删除 mechanism "仿生集水生物原型及机制" (命中 "猪笼草")
- spider-silk: 删除 mechanism "HHNCM亲水-疏水纳米纤维铜网（三仿生：甲虫+蜂窝网+猪笼草）" (命中 "猪笼草")

总计删除: 11 条


## Phase 3 第二轮：performance_data + narrative 清理

- mussel-foot-adhesion: DELETE perf[0] pollutant=, material= (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[1] pollutant=, material=Amino-functionalized Bacterial Nanocellulose (BNC) (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[2] pollutant=, material=Hybrid Fe3O4/BNC nanocomposites (Spherical particl (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[3] pollutant=Methylene Blue (MB), material=Soy protein-grafted CNF/hydroxyapatite nanocomposi (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[4] pollutant=Methylene Blue (MB), material=CMC/MAA/HAp hybrid material (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[5] pollutant=Methylene Blue, material=Porous 3D sponge from rGO, vitamin C, and CNCs (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[6] pollutant=Methylene Blue (MB) and Congo Red (CR), material=CNF/graphene nanosheets hybrid aerogel (Ratio 3:1) (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[8] pollutant=, material=MCGA (cellulose/graphene aerogel) (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[9] pollutant=, material=Nanocellulose/alumina composite aerogel (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[34] pollutant=, material=MCC10 (MCC-PDA-PEI/CS-PDA-PEI) (命中 "cellulose")
- mussel-foot-adhesion: DELETE perf[35] pollutant=, material=未改性MCC/CS (命中 "cellulose")
- mussel-foot-adhesion: DELETE narrative paper_id=Salama2021_nanocellulose_water_treatment (命中 "纤维素")
- mussel-foot-adhesion: DELETE narrative paper_id=Gao2022_Nanocellulose_Aerogel_OilWater_Review (命中 "纤维素")
- mussel-foot-adhesion: DELETE narrative paper_id=2021-Mohammed-selective-adsorption-dye-CNC (命中 "纤维素")
- polydopamine-coating: DELETE narrative paper_id=Xiong2023_APP_biomimetic_membrane (命中 "stenocara")
- spider-silk: DELETE narrative paper_id=2022-Yong-femtosecond-laser-superwettability-revie (命中 "荷叶")
- spider-silk: DELETE narrative paper_id=2021-Penetration-separation-membrane-hierarchical- (命中 "荷叶")
- spider-silk: DELETE narrative paper_id=Yu2022_Fog_Harvesting_Devices_Multiple_Creatures_R (命中 "猪笼草")
- spider-silk: DELETE narrative paper_id=yu2022_fog_harvesting_biomimetic_review (命中 "猪笼草")

总计删除: 19 条

## Phase 3 第三轮：mechanism_instances 清理

### check_chimera.py 扩展
- 新增 `mechanism_instances` 字段扫描（与 mechanisms 同逻辑）

### mussel-foot-adhesion
- 删除全部 22 条 mechanism_instances（含 1 条纤维素命中 + 21 条非贻贝机制描述，如超疏水织物接触角等）
- mechanism_instances 字段整体移除

### polydopamine-coating
- 19 条 mechanism_instances 无 blocklist 命中，保留
