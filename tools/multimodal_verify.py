#!/usr/bin/env python3
"""
Multimodal PDF Verification Script (mimo-v2.5, dual-key rotation)

Uses PyMuPDF + mimo-v2.5 API to verify performance_data rows
by reading PDF page images and extracting matching quotes.

Follows LitExtract principles:
- Evidence from PDF only, no LLM inference
- Preserve original precision and units
- Page + table/figure locator
- Quality marking

Usage:
  python tools/multimodal_verify.py chitosan
  python tools/multimodal_verify.py chitosan cell-membrane-ion-channel mussel-foot-adhesion
"""

import json
import os
import re
import sys
import glob
import base64
import time
import itertools
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install PyMuPDF")
    sys.exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai not installed. Run: pip install openai")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_DIR = REPO_ROOT / 'prototypes_db'
PDF_ROOT = REPO_ROOT / '仿生文献库'
ENV_FILE = REPO_ROOT / 'tools' / 'litextract' / '.env'

MIMO_BASE_URL = 'https://token-plan-cn.xiaomimimo.com/v1'
MIMO_MODEL = 'mimo-v2.5'


def load_api_keys():
    if not ENV_FILE.exists():
        print(f"ERROR: {ENV_FILE} not found.")
        sys.exit(1)
    keys = []
    with open(ENV_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('MIMO_API_KEY') and '=' in line and 'your_' not in line:
                val = line.split('=', 1)[1].strip()
                if val:
                    keys.append(val)
    if not keys:
        print("ERROR: No valid MIMO_API_KEY found in .env")
        sys.exit(1)
    # Validate keys with a minimal API call
    valid_keys = []
    for i, key in enumerate(keys):
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key, base_url=MIMO_BASE_URL)
            client.chat.completions.create(
                model=MIMO_MODEL,
                messages=[{'role': 'user', 'content': 'hi'}],
                max_tokens=5,
                temperature=0,
            )
            valid_keys.append(key)
            print(f"  Key {i+1}: valid")
        except Exception as e:
            print(f"  Key {i+1}: INVALID ({str(e)[:60]})")
    if not valid_keys:
        print("ERROR: No valid API keys found")
        sys.exit(1)
    print(f"  Using {len(valid_keys)}/{len(keys)} valid key(s)")
    return valid_keys


def make_client_pool(api_keys):
    clients = [OpenAI(api_key=key, base_url=MIMO_BASE_URL) for key in api_keys]
    return itertools.cycle(clients)


def find_pdf(source_file):
    if not source_file:
        return None
    bn = os.path.basename(source_file)
    if not bn:
        return None
    all_pdfs = glob.glob(str(PDF_ROOT / '**/*.pdf'), recursive=True)
    for p in all_pdfs:
        if os.path.basename(p) == bn:
            return p
    stem = re.sub(r'\s*[23]\.pdf$', '.pdf', bn)
    for p in all_pdfs:
        pstem = re.sub(r'\s*[23]\.pdf$', '.pdf', os.path.basename(p))
        if pstem == stem:
            return p
    m = re.match(r'(\d{4})-([A-Za-z\u4e00-\u9fff]+)', bn)
    if m:
        author, year = m.group(2).lower(), m.group(1)
        for p in all_pdfs:
            pbn = os.path.basename(p).lower()
            if author in pbn and year in pbn:
                return p
    return None


def pdf_pages_to_images(pdf_path, pages=None, dpi=120):
    images = []
    try:
        doc = fitz.open(pdf_path)
        if pages is None:
            pages = list(range(min(len(doc), 30)))
        for page_num in pages:
            if page_num >= len(doc):
                break
            page = doc[page_num]
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
            b64 = base64.b64encode(pix.tobytes("png")).decode('utf-8')
            images.append({'page_num': page_num + 1, 'b64': b64})
        doc.close()
    except Exception as e:
        print(f"  [WARN] Failed to convert {pdf_path}: {e}")
    return images


SYSTEM_MSG = (
    "You are a scientific literature verification agent. "
    "You read PDF page images and find specific data points. "
    "You MUST respond with valid JSON only. No explanation, no markdown, no extra text. "
    "Output ONLY a single JSON object."
)


def build_perf_prompt(row):
    pollutant = row.get('pollutant', '')
    parameter = row.get('parameter', '')
    value = row.get('value', '')
    material = row.get('material', '')
    conditions = row.get('conditions', '')
    return (
        "Find this data point in the PDF page images below.\n\n"
        f"DATA POINT:\n"
        f"- Pollutant: {pollutant}\n"
        f"- Parameter: {parameter}\n"
        f"- Reported Value: {value}\n"
        f"- Material: {material}\n"
        f"- Conditions: {conditions}\n\n"
        "Find the EXACT text in the PDF that reports this data point. "
        "Extract the quote VERBATIM from the PDF. Note page number and location.\n\n"
        "Respond with this JSON object:\n"
        '{"found": true, "quote": "exact text from PDF", "page": 0, '
        '"locator": "Table X / Figure Y / p.N", "quality": "reliable"}\n\n'
        'If not found in the PDF:\n'
        '{"found": false, "quote": "", "page": 0, "locator": "", "quality": "not_found"}\n\n'
        "Rules: Quote must be exactly as written in the PDF. Do not generate or infer. "
        "For tables quote row/column header + value. For figures quote caption or axis label."
    )


def build_mech_prompt(row):
    name = row.get('name', '')
    desc = row.get('description', '')
    return (
        "Find evidence for this mechanism in the PDF page images below.\n\n"
        f"MECHANISM:\n- Name: {name}\n- Description: {desc}\n\n"
        "Respond with this JSON object:\n"
        '{"found": true, "quote": "exact supporting text from PDF", "page": 0, '
        '"locator": "Table X / Figure Y / p.N", "quality": "reliable"}\n\n'
        'If not found:\n'
        '{"found": false, "quote": "", "page": 0, "locator": "", "quality": "not_found"}\n\n'
        "Rules: Quote must be exactly as in the PDF. Do not infer or generate."
    )


def build_bc_prompt(bc_text, parameter, gate_level, mechanism_name):
    return (
        "Find evidence for this boundary condition in the PDF page images below.\n\n"
        f"BOUNDARY CONDITION:\n"
        f"- Text: {bc_text}\n"
        f"- Parameter: {parameter}\n"
        f"- Gate Level: {gate_level}\n"
        f"- Parent Mechanism: {mechanism_name}\n\n"
        "Find the EXACT text in the PDF that supports or describes this boundary condition. "
        "Extract the quote VERBATIM from the PDF. Note page number and location.\n\n"
        "Respond with this JSON object:\n"
        '{"found": true, "quote": "exact text from PDF", "page": 0, '
        '"locator": "Table X / Figure Y / Section Z / p.N", "quality": "reliable"}\n\n'
        'If not found in the PDF:\n'
        '{"found": false, "quote": "", "page": 0, "locator": "", "quality": "not_found"}\n\n'
        "Rules: Quote must be exactly as written in the PDF. Do not generate or infer. "
        "Look for parameter ranges, conditions, limitations, or constraints."
    )


def parse_json_response(text):
    """Robustly extract JSON from model response (handles reasoning text)."""
    text = text.strip()
    
    # Strategy 1: Direct JSON parse
    try:
        return json.loads(text)
    except:
        pass
    
    # Strategy 2: JSON in code block
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except:
            pass
    
    # Strategy 3: Find outermost { ... } pair
    brace_start = text.find('{')
    if brace_start >= 0:
        # Find matching closing brace (handle nested braces)
        depth = 0
        for i in range(brace_start, len(text)):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[brace_start:i + 1])
                    except:
                        break
    
    # Strategy 4: Find any JSON-like object with "found" key
    m = re.search(r'\{[^{}]*"found"\s*:\s*(true|false)[^{}]*\}', text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except:
            pass
    
    return None


def verify_row_with_api(client_pool, row, pdf_path, field='performance_data', max_pages=15):
    if field == 'performance_data':
        user_prompt = build_perf_prompt(row)
    elif field == 'boundary_conditions':
        user_prompt = build_bc_prompt(
            row.get('text', ''), row.get('parameter', ''),
            row.get('gate_level', 'soft'), row.get('name', ''))
    else:
        user_prompt = build_mech_prompt(row)
    
    images = pdf_pages_to_images(pdf_path, pages=list(range(max_pages)), dpi=120)
    if not images:
        return {'found': False, 'quality': 'not_found', 'error': 'no images'}
    
    # Build multimodal message with system message
    messages = [{'role': 'system', 'content': SYSTEM_MSG}]
    user_content = [{'type': 'text', 'text': user_prompt}]
    for img in images[:10]:
        user_content.append({
            'type': 'image_url',
            'image_url': {'url': f"data:image/png;base64,{img['b64']}"}
        })
        user_content.append({'type': 'text', 'text': f"[Page {img['page_num']}]"})
    messages.append({'role': 'user', 'content': user_content})
    
    for attempt in range(3):
        client = next(client_pool)
        try:
            response = client.chat.completions.create(
                model=MIMO_MODEL,
                messages=messages,
                max_tokens=8192,
                temperature=0,
                extra_body={"enable_thinking": False},
            )

            finish_reason = response.choices[0].finish_reason if response.choices else ''
            result_text = response.choices[0].message.content.strip() if response.choices else ''
            parsed = parse_json_response(result_text)

            if parsed:
                return parsed

            # Only do truncation retry if we actually got a truncated response (not on error)
            if finish_reason == 'length' and result_text and attempt < 2:
                print(f" [truncated, retrying with 16384 tokens]", end='', flush=True)
                try:
                    response = client.chat.completions.create(
                        model=MIMO_MODEL,
                        messages=messages,
                        max_tokens=16384,
                        temperature=0,
                        extra_body={"enable_thinking": False},
                    )
                    result_text = response.choices[0].message.content.strip()
                    parsed = parse_json_response(result_text)
                    if parsed:
                        return parsed
                except Exception as e2:
                    print(f" [retry-16k:{str(e2)[:30]}]", end='', flush=True)

            return {'found': False, 'quality': 'parse_error', 'raw': result_text[:300]}

        except Exception as e:
            if attempt < 2:
                print(f" [r{attempt+1}:{str(e)[:30]}]", end='', flush=True)
                time.sleep(1)
            else:
                return {'found': False, 'quality': 'error', 'error': str(e)}


def find_pdf_by_doi(doi, pdf_root=None):
    """用 DOI 匹配本地 PDF。先检查 visual_cache 中的 DOI，再模糊匹配文件名。"""
    if not doi:
        return None
    root = Path(pdf_root) if pdf_root else PDF_ROOT
    doi_norm = doi.lower().strip()

    # 策略1：搜索 visual_cache.json 中的 DOI 字段
    for cache_file in glob.glob(str(root / '**/*_visual_cache.json'), recursive=True):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache = json.load(f)
            meta = cache.get('stage0', {}).get('metadata', {})
            cache_doi = str(meta.get('doi', '') or '').lower().strip()
            if cache_doi and doi_norm in cache_doi:
                pdf_path = cache_file.replace('_visual_cache.json', '.pdf')
                if os.path.exists(pdf_path):
                    return pdf_path
        except:
            continue

    # 策略2：用 Crossref API 获取标题，然后模糊匹配文件名
    try:
        import urllib.request
        url = f"https://api.crossref.org/works/{doi_norm}"
        req = urllib.request.Request(url, headers={'User-Agent': 'BMDL-Verify/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        title = data['message']['title'][0].lower()
        author = data['message'].get('author', [{}])[0].get('family', '').lower()
        year = str(data['message'].get('published', {}).get('date-parts', [[None]])[0][0])

        all_pdfs = glob.glob(str(root / '**/*.pdf'), recursive=True)
        for p in all_pdfs:
            pbn = os.path.basename(p).lower()
            if year in pbn and author in pbn:
                return p
        title_words = [w for w in title.split() if len(w) > 3][:3]
        for p in all_pdfs:
            pbn = os.path.basename(p).lower()
            if all(w in pbn for w in title_words):
                return p
    except Exception as e:
        print(f"  [DOI match] Crossref fallback failed for {doi}: {e}")

    return None


def verify_boundary_conditions(json_path, client_pool, target_mech_indices=None):
    """验证机制中的 boundary_conditions（仅 basis=llm_inferred 的）。"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pid = data.get('id', Path(json_path).stem)
    mechanisms = data.get('mechanisms', [])

    stats = {'verified': 0, 'not_found': 0, 'no_pdf': 0, 'errors': 0, 'skipped': 0}
    pdf_cache = {}

    for mi, mech in enumerate(mechanisms):
        if target_mech_indices and mi not in target_mech_indices:
            continue

        cc = mech.get('causal_chain', {})
        bcs = cc.get('boundary_conditions', [])
        mech_name = mech.get('name', '')

        source_file = str(mech.get('source_file') or '').strip()
        doi = str(mech.get('ref_doi') or '').strip()

        pdf_path = None
        if source_file:
            pdf_path = find_pdf(source_file)
        if not pdf_path and doi:
            pdf_path = find_pdf_by_doi(doi)

        if not pdf_path:
            for bc in bcs:
                if bc.get('basis') == 'llm_inferred':
                    stats['no_pdf'] += 1
            continue

        if pdf_path not in pdf_cache:
            print(f"\n  PDF: {os.path.basename(pdf_path)} (mech[{mi}] {mech_name[:40]})")
            pdf_cache[pdf_path] = True

        for bi, bc in enumerate(bcs):
            if bc.get('basis') != 'llm_inferred':
                stats['skipped'] += 1
                continue

            bc_text = bc.get('text', '')
            parameter = bc.get('parameter', '')
            gate_level = bc.get('gate_level', 'soft')

            label = bc_text[:60] if bc_text else parameter
            print(f"  [{pid}] mech[{mi}] bc[{bi}] {label}...", end='', flush=True)

            result = verify_row_with_api(client_pool,
                                         {'text': bc_text, 'parameter': parameter,
                                          'name': mech_name, 'gate_level': gate_level},
                                         pdf_path, field='boundary_conditions')

            if result.get('found') and result.get('quote'):
                bc['basis'] = 'from_source'
                bc['source'] = doi or os.path.basename(pdf_path)
                bc['quote'] = result['quote']
                bc['locator'] = result.get('locator', f"p.{result.get('page', '?')}")
                bc['verification_method'] = 'pdf_visual_reading'
                stats['verified'] += 1
                print(f" ✅ from_source (p.{result.get('page', '?')})")
            elif result.get('quality') == 'not_found':
                bc['verification_method'] = 'pdf_not_found'
                stats['not_found'] += 1
                print(f" NOT_FOUND")
            else:
                bc['verification_method'] = 'pdf_error'
                stats['errors'] += 1
                print(f" ERROR: {result.get('error', '')[:60]}")

            time.sleep(0.5)

        # 每 5 条 checkpoint
        total_processed = stats['verified'] + stats['not_found'] + stats['errors']
        if total_processed > 0 and total_processed % 5 == 0:
            with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f"\n  [checkpoint: {stats['verified']} verified, {stats['not_found']} not_found, {stats['errors']} errors]", flush=True)

    # 最终写入
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    return {'prototype': pid, **stats}


def verify_prototype(json_path, client_pool, field='performance_data'):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pid = data.get('id', json_path.stem)
    items = data.get(field, [])

    verified = 0
    not_found = 0
    skipped_no_pdf = 0
    already_done = 0
    errors = 0

    pdf_cache = {}

    for i, item in enumerate(items):
        v = item.get('verification', 'unverified')
        if v not in ('needs_review', 'unverified', 'missing_pdf'):
            already_done += 1
            continue

        source_file = item.get('source_file', '')
        pdf_path = find_pdf(source_file)

        if not pdf_path:
            skipped_no_pdf += 1
            continue

        if pdf_path not in pdf_cache:
            print(f"\n  PDF: {os.path.basename(pdf_path)}")
            pdf_cache[pdf_path] = True

        label = item.get('parameter', item.get('name', ''))[:60]
        print(f"  [{i+1}/{len(items)}] {label}...", end='', flush=True)

        result = verify_row_with_api(client_pool, item, pdf_path, field)

        if result.get('found') and result.get('quote'):
            item['verification_quote'] = result['quote']
            item['source_locator'] = result.get('locator', f"p.{result.get('page', '?')}")
            item['verification'] = 'partial'
            verified += 1
            print(f" OK (p.{result.get('page', '?')})")
        elif result.get('quality') == 'not_found':
            not_found += 1
            print(f" NOT_FOUND")
        elif result.get('quality') == 'parse_error':
            errors += 1
            raw = result.get('raw', '')[:100]
            print(f" PARSE_ERROR: {raw}")
        else:
            errors += 1
            print(f" ERROR: {result.get('error', 'unknown')[:60]}")

        time.sleep(0.5)

        if (verified + not_found + errors) % 5 == 0:
            with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            print(f"\n  [checkpoint: {verified} verified, {not_found} not_found, {errors} errors]", flush=True)

    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    return {
        'prototype': pid, 'field': field, 'total': len(items),
        'already_done': already_done, 'verified': verified,
        'not_found': not_found, 'no_pdf': skipped_no_pdf, 'errors': errors
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Multimodal PDF verification')
    parser.add_argument('targets', nargs='*', default=['chitosan'])
    parser.add_argument('--field', choices=['performance_data', 'mechanisms', 'boundary_conditions'],
                        default='boundary_conditions')
    args = parser.parse_args()

    api_keys = load_api_keys()
    client_pool = make_client_pool(api_keys)

    print(f"=== Multimodal Verification ({args.field}) ===")
    print(f"Targets: {', '.join(args.targets)}")
    print(f"Model: {MIMO_MODEL} (multimodal)")
    print(f"Keys: {len(api_keys)}")
    print(f"PDFs: {len(glob.glob(str(PDF_ROOT / '**/*.pdf'), recursive=True))} files")
    print()

    all_results = []
    for target in args.targets:
        json_path = DB_DIR / f'{target}.json'
        if not json_path.exists():
            print(f"SKIP: {json_path} not found")
            continue

        if args.field == 'boundary_conditions':
            r = verify_boundary_conditions(json_path, client_pool)
            all_results.append(r)
            print(f"\n  Result: {r['verified']} verified, {r['not_found']} not_found, "
                  f"{r['no_pdf']} no_pdf, {r['skipped']} skipped, {r['errors']} errors")
        else:
            print(f"\n--- {target} {args.field} ---")
            r = verify_prototype(json_path, client_pool, args.field)
            all_results.append(r)
            print(f"\n  Result: {r['verified']} verified, {r['already_done']} done, "
                  f"{r['not_found']} not found, {r['no_pdf']} no PDF, {r['errors']} errors")

    total_new = sum(r['verified'] for r in all_results)
    total_nf = sum(r.get('not_found', 0) for r in all_results)
    total_err = sum(r.get('errors', 0) for r in all_results)
    print(f"\n=== SUMMARY ===")
    print(f"  New verified: {total_new}")
    print(f"  Not found: {total_nf}")
    print(f"  Errors: {total_err}")


if __name__ == '__main__':
    main()
