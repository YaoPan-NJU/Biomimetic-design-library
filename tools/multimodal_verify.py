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
    print(f"  Loaded {len(keys)} API key(s)")
    return keys


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
    targets = sys.argv[1:] if len(sys.argv) > 1 else ['chitosan']
    api_keys = load_api_keys()
    client_pool = make_client_pool(api_keys)
    
    print(f"=== Multimodal Verification ===")
    print(f"Targets: {', '.join(targets)}")
    print(f"Model: {MIMO_MODEL}")
    print(f"Keys: {len(api_keys)}")
    print(f"PDFs: {len(glob.glob(str(PDF_ROOT / '**/*.pdf'), recursive=True))} files")
    print()
    
    all_results = []
    for target in targets:
        json_path = DB_DIR / f'{target}.json'
        if not json_path.exists():
            print(f"SKIP: {json_path} not found")
            continue
        
        print(f"\n--- {target} performance_data ---")
        r = verify_prototype(json_path, client_pool, 'performance_data')
        all_results.append(r)
        print(f"\n  Result: {r['verified']} verified, {r['already_done']} done, "
              f"{r['not_found']} not found, {r['no_pdf']} no PDF, {r['errors']} errors")
        
        print(f"\n--- {target} mechanisms ---")
        r2 = verify_prototype(json_path, client_pool, 'mechanisms')
        all_results.append(r2)
        print(f"\n  Result: {r2['verified']} verified, {r2['already_done']} done, "
              f"{r2['not_found']} not found, {r2['no_pdf']} no PDF, {r2['errors']} errors")
    
    total_new = sum(r['verified'] for r in all_results)
    total_done = sum(r['already_done'] for r in all_results)
    total_nf = sum(r['not_found'] for r in all_results)
    total_err = sum(r['errors'] for r in all_results)
    print(f"\n=== SUMMARY ===")
    print(f"  New verified: {total_new}")
    print(f"  Previously done: {total_done}")
    print(f"  Not found: {total_nf}")
    print(f"  Errors: {total_err}")


if __name__ == '__main__':
    main()
