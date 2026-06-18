# Claude Code Task 64-68: 基础设施修复 + 多模态 PDF 引文验证

## 背景

Qoder 审阅发现三个系统性缺陷，必须在批量验证前修复：

1. **build_prototypes_db.py** 的 `merge_with_existing` 不保留 `verification_quote` 和 `source_locator`，下次 build 会丢失所有验证引文
2. **multimodal_verify.py** 缺少增量保存（崩溃丢数据）、跳过 `missing_pdf` 行、无 API 重试
3. 修复后运行 `multimodal_verify.py` 验证 6 个原型共 249 行

## 硬性约束

- 每个文件修改后必须 `git diff` 确认改动已落盘
- 禁止声称完成但实际未修改
- `multimodal_verify.py` 运行前先确认 `.env` 中 `MIMO_API_KEY` 已配置
- 所有 Python 命令必须加 `-X utf8` 标志
- 纯文本操作，不使用特殊字符

## 当前待验证数量

```
chitosan:                  perf=9,  mech=82,  subtotal=91
mussel-foot-adhesion:      perf=0,  mech=50,  subtotal=50
polydopamine-coating:      perf=0,  mech=28,  subtotal=28
spider-silk:               perf=0,  mech=20,  subtotal=20
silk-fibroin:              perf=0,  mech=12,  subtotal=12
fish-scale-hydroxyapatite:  perf=0,  mech=48,  subtotal=48
TOTAL:                                       249
```

---

## Task 64: 修复 build_prototypes_db.py 的 merge_with_existing

目标文件: `tools/build_prototypes_db.py`

问题: `merge_with_existing` 函数保留 `verification` 状态，但不保留 `verification_quote` 和 `source_locator`。下次 build 会丢失所有验证引文。

### 修复 1 - mechanisms 合并区 (约 line 374-376)

找到这段代码:

```python
            old_ver = old_m.get('verification', 'unverified')
            if old_ver and old_ver != 'unverified':
                new_m['verification'] = old_ver
```

在它后面（同一缩进，在 `if old_m:` 块内）添加:

```python
            # 保留旧的验证引文字段
            for vfield in ['verification_quote', 'source_locator']:
                old_val = old_m.get(vfield)
                if old_val:
                    new_m[vfield] = old_val
```

### 修复 2 - performance_data 合并区 (约 line 400)

找到这行:

```python
            for field in ['source', 'ref_doi', 'source_file', 'page', 'locator']:
```

改为:

```python
            for field in ['source', 'ref_doi', 'source_file', 'page', 'locator', 'verification_quote', 'source_locator']:
```

### 验证

```bash
python -X utf8 tools/build_prototypes_db.py
```

确认无报错。然后检查 cell-membrane-ion-channel.json 中已有 `verification_quote` 的行没有被清空:

```bash
python -X utf8 -c "import json; d=json.load(open('prototypes_db/cell-membrane-ion-channel.json','r',encoding='utf-8')); q=[p for p in d.get('performance_data',[]) if p.get('verification_quote')]; print(f'rows_with_quote={len(q)}')"
```

如果输出 rows_with_quote 大于 0，说明保留成功。

---

## Task 65: 修复 multimodal_verify.py 三个缺陷

目标文件: `tools/multimodal_verify.py`

### 修复 1 - missing_pdf 纳入验证范围 (约 line 270)

找到:

```python
        if v not in ('needs_review', 'unverified'):
```

改为:

```python
        if v not in ('needs_review', 'unverified', 'missing_pdf'):
```

### 修复 2 - API 重试机制 (约 line 212-250)

第一步: 修改 `verify_row_with_api` 函数签名（约 line 212）:

找到:

```python
def verify_row_with_api(client, row, pdf_path, field='performance_data', max_pages=15):
```

改为:

```python
def verify_row_with_api(client_pool, row, pdf_path, field='performance_data', max_pages=15):
```

第二步: 将 API 调用部分（约 line 233-250）:

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

第三步: 修改调用处（约 line 285-289）:

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

### 修复 3 - 增量保存 (约 line 308-312)

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
        
        # 增量保存: 每处理 5 行写一次
        if (verified + not_found + errors) % 5 == 0:
            with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f"\n  [checkpoint: {verified} verified, {not_found} not_found, {errors} errors]", flush=True)
    
    # 最终保存
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
```

### 验证

```bash
python -X utf8 -c "import py_compile; py_compile.compile('tools/multimodal_verify.py', doraise=True); print('Syntax OK')"
```

然后用 cell-membrane-ion-channel 做快速测试（只有少量行需要验证）:

```bash
python -X utf8 tools/multimodal_verify.py cell-membrane-ion-channel
```

确认脚本能正常运行、API 重试和增量保存生效。

---

## Task 66: 运行 chitosan 验证 (91 行)

chitosan 是最大的原型（9 perf + 82 mech = 91 行），预计 30-45 分钟。

```bash
python -X utf8 tools/multimodal_verify.py chitosan
```

不要中断，让脚本跑完。增量保存每 5 行触发一次，中途崩溃不会丢失全部进度。

---

## Task 67: 运行剩余 5 个原型验证 (158 行)

依次运行（每个独立运行，不要并行）:

```bash
python -X utf8 tools/multimodal_verify.py mussel-foot-adhesion
python -X utf8 tools/multimodal_verify.py polydopamine-coating
python -X utf8 tools/multimodal_verify.py spider-silk
python -X utf8 tools/multimodal_verify.py silk-fibroin
python -X utf8 tools/multimodal_verify.py fish-scale-hydroxyapatite
```

注意:
- mussel 50 + PDA 28 + spider 20 + silk 12 + fish-scale 48 = 158 行
- mussel 和 PDA 的专利 PDF 在 `仿生文献库/专利/` 目录（如 CN105413659B.pdf 等）
- 预计每个原型 10-20 分钟

---

## Task 68: 全量校验 + commit + push

### 步骤 1: 运行三件套校验

```bash
python -X utf8 tools/build_prototypes_db.py
python -X utf8 tools/check_chimera.py --strict
python -X utf8 tools/validate_consistency.py
```

关键: build 之后检查 verification_quote 是否被保留:

```bash
python -X utf8 -c "
import json
protos = ['chitosan','mussel-foot-adhesion','polydopamine-coating','spider-silk','silk-fibroin','fish-scale-hydroxyapatite']
for name in protos:
    d = json.load(open(f'prototypes_db/{name}.json','r',encoding='utf-8'))
    perf_q = sum(1 for p in d.get('performance_data',[]) if p.get('verification_quote'))
    mech_q = sum(1 for m in d.get('mechanisms',[]) if m.get('verification_quote'))
    pv = sum(1 for p in d.get('performance_data',[]) if p.get('verification') in ('partial','verified','corroborated'))
    mv = sum(1 for m in d.get('mechanisms',[]) if m.get('verification') in ('partial','verified','corroborated'))
    print(f'{name}: perf_quote={perf_q} mech_quote={mech_q} perf_verified={pv} mech_verified={mv}')
"
```

### 步骤 2: 创建报告

创建 `docs/optimization-v1/review-clcode-task64-68.md`，内容包括:
- 每个 Task 完成状态
- 修复前后的代码变更（git diff 摘要）
- 每个原型的验证结果（verified / not_found / errors）
- 校验结果（build / chimera / consistency）
- verification_quote 保留确认
- 遇到的问题

### 步骤 3: 提交推送

```bash
git add -A
git commit -m "data: multimodal PDF verification - infra fix + 6 prototypes (Task 64-68)"
git push origin review
```

完成后报告最终状态。
