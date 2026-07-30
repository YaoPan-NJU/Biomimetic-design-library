# Claude Code 自主任务: 基础设施修复 + 全量多模态 PDF 引文验证

## 执行模式

这是自主连续执行任务。请从头到尾按顺序完成所有步骤，不要在中间停下来等待人工确认。只有遇到下方"停止条件"中列出的情况才暂停并报告。

## 停止条件（遇到才停，其他一律自主处理）

**遇到以下情况必须停下并报告**:
1. `.env` 中没有 `MIMO_API_KEY`，或所有 API key 都返回 401/403（认证失败）
2. 修改脚本后出现你无法修复的 SyntaxError
3. `check_chimera.py --strict` 报出 chimera 违规（不要自行修改数据，报告给人工处理）
4. 某个 PDF 文件在项目中完全找不到（搜索了 `仿生文献库/`、`extraction/` 等所有目录都没有）

**以下情况不需要停，自主处理**:
- 个别行 API 超时/报错：脚本已有 3 次重试，重试后仍失败的记为 error，继续下一行
- 个别行返回 `not_found`：正常现象，PDF 中可能确实没有对应内容
- 某个原型 0 行待验证：跳过，在报告中注明
- 某个原型的 PDF 匹配不上：跳过该行，记入 `no_pdf` 统计，继续其他原型
- 专利 PDF 文件名带 CAJ 后缀：在报告中记录，跳过该行

---

## 步骤 1: 修复 build_prototypes_db.py

文件: `tools/build_prototypes_db.py`

### 1.1 mechanisms 合并区（约 line 374-376）

找到:
```python
            old_ver = old_m.get('verification', 'unverified')
            if old_ver and old_ver != 'unverified':
                new_m['verification'] = old_ver
```

在其后（同一缩进）添加:
```python
            for vfield in ['verification_quote', 'source_locator']:
                old_val = old_m.get(vfield)
                if old_val:
                    new_m[vfield] = old_val
```

### 1.2 performance_data 合并区（约 line 400）

找到:
```python
            for field in ['source', 'ref_doi', 'source_file', 'page', 'locator']:
```

改为:
```python
            for field in ['source', 'ref_doi', 'source_file', 'page', 'locator', 'verification_quote', 'source_locator']:
```

### 1.3 验证修复

```bash
python -X utf8 tools/build_prototypes_db.py
```

确认无报错，确认已有 verification_quote 的行未被清空:
```bash
python -X utf8 -c "import json; d=json.load(open('prototypes_db/cell-membrane-ion-channel.json','r',encoding='utf-8')); q=[p for p in d.get('performance_data',[]) if p.get('verification_quote')]; print(f'rows_with_quote={len(q)}')"
```

如果 rows_with_quote > 0，修复成功，继续下一步。

---

## 步骤 2: 修复 multimodal_verify.py

文件: `tools/multimodal_verify.py`

### 2.1 missing_pdf 纳入验证（约 line 270）

找到:
```python
        if v not in ('needs_review', 'unverified'):
```

改为:
```python
        if v not in ('needs_review', 'unverified', 'missing_pdf'):
```

### 2.2 API 重试（约 line 212-250）

第一步，修改函数签名（约 line 212）:

找到:
```python
def verify_row_with_api(client, row, pdf_path, field='performance_data', max_pages=15):
```

改为:
```python
def verify_row_with_api(client_pool, row, pdf_path, field='performance_data', max_pages=15):
```

第二步，将 API 调用块（约 line 233-250）:

找到:
```python
    try:
        response = client.chat.completions.create(
            model=MIMO_MODEL,
            messages=messages,
            max_tokens=4096,
            temperature=0
        )
        
        result_text = response.choices[0].message.content.strip()
        parsed = parse_json_response(result_text)
        
        if parsed:
            return parsed
        
        return {'found': False, 'quality': 'parse_error', 'raw': result_text[:300]}
        
    except Exception as e:
        return {'found': False, 'quality': 'error', 'error': str(e)}
```

替换为:
```python
    for attempt in range(3):
        client = next(client_pool)
        try:
            response = client.chat.completions.create(
                model=MIMO_MODEL,
                messages=messages,
                max_tokens=4096,
                temperature=0
            )
            
            result_text = response.choices[0].message.content.strip()
            parsed = parse_json_response(result_text)
            
            if parsed:
                return parsed
            
            return {'found': False, 'quality': 'parse_error', 'raw': result_text[:300]}
            
        except Exception as e:
            if attempt < 2:
                print(f" [retry {attempt+1}/3: {str(e)[:40]}]", end='', flush=True)
                time.sleep(2 ** attempt)
            else:
                return {'found': False, 'quality': 'error', 'error': str(e)}
```

第三步，修改调用处（约 line 285-289）:

找到:
```python
        client = next(client_pool)
        label = item.get('parameter', item.get('name', ''))[:60]
        print(f"  [{i+1}/{len(items)}] {label}...", end='', flush=True)
        
        result = verify_row_with_api(client, item, pdf_path, field)
```

改为:
```python
        label = item.get('parameter', item.get('name', ''))[:60]
        print(f"  [{i+1}/{len(items)}] {label}...", end='', flush=True)
        
        result = verify_row_with_api(client_pool, item, pdf_path, field)
```

### 2.3 增量保存（约 line 308-312）

找到:
```python
        time.sleep(0.5)
    
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
```

改为:
```python
        time.sleep(0.5)
        
        if (verified + not_found + errors) % 5 == 0:
            with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f"\n  [checkpoint: {verified} verified, {not_found} not_found, {errors} errors]", flush=True)
    
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
```

### 2.4 语法检查 + 快速测试

```bash
python -X utf8 -c "import py_compile; py_compile.compile('tools/multimodal_verify.py', doraise=True); print('Syntax OK')"
```

然后用 cell-membrane-ion-channel 快速测试（少量行）:
```bash
python -X utf8 tools/multimodal_verify.py cell-membrane-ion-channel
```

确认脚本能正常运行。如果有错误，修复后重新测试，直到通过。

---

## 步骤 3: 全量验证（13 个原型，282 行）

按从小到大顺序运行（先跑小的快速积累进度，大的放后面）。每个原型依次运行，不要并行。

```bash
python -X utf8 tools/multimodal_verify.py plant-tannin
python -X utf8 tools/multimodal_verify.py lobster-exoskeleton
python -X utf8 tools/multimodal_verify.py bone-structure
python -X utf8 tools/multimodal_verify.py iron-oxidizing-bacteria
python -X utf8 tools/multimodal_verify.py mycelium
python -X utf8 tools/multimodal_verify.py cell-membrane-ion-channel
python -X utf8 tools/multimodal_verify.py pitcher-plant-slippery-surface
python -X utf8 tools/multimodal_verify.py silk-fibroin
python -X utf8 tools/multimodal_verify.py spider-silk
python -X utf8 tools/multimodal_verify.py polydopamine-coating
python -X utf8 tools/multimodal_verify.py fish-scale-hydroxyapatite
python -X utf8 tools/multimodal_verify.py mussel-foot-adhesion
python -X utf8 tools/multimodal_verify.py chitosan
```

预计总时间 2-3 小时。增量保存每 5 行触发一次，中途崩溃不会丢失全部进度（重跑时会自动跳过已完成的行）。

注意事项:
- 专利 PDF 在 `仿生文献库/专利/` 目录下（如 CN105413659B.pdf）
- 某些 PDF 可能是 CAJ 格式，脚本无法读取，记入报告即可
- 某些行可能 `source_file` 路径不对，脚本会尝试模糊匹配，匹配不上的跳过

---

## 步骤 4: 校验

### 4.1 三件套

```bash
python -X utf8 tools/build_prototypes_db.py
python -X utf8 tools/check_chimera.py --strict
python -X utf8 tools/validate_consistency.py
```

### 4.2 验证 verification_quote 是否在 build 后保留

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

如果输出为空（0 个 quote），说明 build 覆盖了所有引文，这是严重问题，必须报告。

### 4.3 验证覆盖率统计

```bash
python -X utf8 -c "
import json, os
db = 'prototypes_db'
gp, gm, gpt, gmt = 0, 0, 0, 0
for f in sorted(os.listdir(db)):
    if not f.endswith('.json'): continue
    d = json.load(open(os.path.join(db,f),'r',encoding='utf-8'))
    for p in d.get('performance_data',[]):
        gpt += 1
        if p.get('verification') in ('partial','verified','corroborated','done'): gp += 1
    for m in d.get('mechanisms',[]):
        gmt += 1
        if m.get('verification') in ('partial','verified','corroborated','done'): gm += 1
print(f'performance_data: {gp}/{gpt} verified ({100*gp/max(gpt,1):.0f}%)')
print(f'mechanisms: {gm}/{gmt} verified ({100*gm/max(gmt,1):.0f}%)')
"
```

---

## 步骤 5: 报告 + 提交

### 5.1 创建报告

创建 `docs/optimization-v1/review-clcode-infra-fix-and-verify.md`，内容包括:

1. **代码修复摘要**: build_prototypes_db.py 和 multimodal_verify.py 各改了什么
2. **验证结果**: 每个原型的 verified / not_found / errors / no_pdf 数量
3. **校验结果**: build / chimera / consistency 是否通过
4. **verification_quote 保留确认**: build 后有多少行保留了 quote
5. **覆盖率**: 验证前后 performance_data 和 mechanisms 的覆盖率对比
6. **问题记录**: 遇到的所有异常和跳过的行

### 5.2 提交推送

```bash
git add -A
git commit -m "data: infra fix (merge quote preserve + verify retry/save) + multimodal verify 13 prototypes"
git push origin review
```

### 5.3 最终报告

报告最终状态:
- 修改了哪些文件
- 验证了多少行，成功率多少
- 有哪些原型/行失败了，原因是什么
- 校验是否全部通过
- 覆盖率提升情况
