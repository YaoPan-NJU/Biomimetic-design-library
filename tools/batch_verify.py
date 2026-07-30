#!/usr/bin/env python3
"""
Batch verify performance_data and mechanisms by extracting quotes from local PDFs.
Uses pdfplumber for text extraction and keyword matching for quote finding.
"""

import json
import os
import re
import glob
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Run: pip install pdfplumber")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_DIR = REPO_ROOT / 'prototypes_db'
PDF_ROOT = REPO_ROOT / '仿生文献库'


def find_pdf(source_file):
    """Find local PDF matching source_file path (with fuzzy matching)."""
    if not source_file:
        return None
    bn = os.path.basename(source_file)
    if not bn:
        return None
    
    # Strategy 1: exact match
    all_pdfs = glob.glob(str(PDF_ROOT / '**/*.pdf'), recursive=True)
    for p in all_pdfs:
        if os.path.basename(p) == bn:
            return p
    
    # Strategy 2: stem match (ignore " 2.pdf"/" 3.pdf" suffix)
    stem = re.sub(r'\s*[23]\.pdf$', '.pdf', bn)
    for p in all_pdfs:
        pbn = os.path.basename(p)
        pstem = re.sub(r'\s*[23]\.pdf$', '.pdf', pbn)
        if pstem == stem:
            return p
    
    # Strategy 3: author+year match
    m = re.match(r'(\d{4})-([A-Za-z\u4e00-\u9fff]+)', bn)
    if m:
        author = m.group(2).lower()
        year = m.group(1)
        for p in all_pdfs:
            pbn = os.path.basename(p).lower()
            if author in pbn and year in pbn:
                return p
    
    return None


def extract_pdf_text(pdf_path, max_pages=None):
    """Extract text from PDF using pdfplumber."""
    try:
        text_by_page = {}
        with pdfplumber.open(pdf_path) as pdf:
            pages = pdf.pages if max_pages is None else pdf.pages[:max_pages]
            for i, page in enumerate(pages):
                text = page.extract_text()
                if text:
                    text_by_page[i + 1] = text
        return text_by_page
    except Exception as e:
        print(f"  [WARN] Failed to read {pdf_path}: {e}")
        return {}


def find_quote_in_text(text_by_page, search_terms, max_quote_len=300):
    """Find the best matching sentence from PDF text."""
    if not text_by_page or not search_terms:
        return None, None
    
    # Split text into sentences
    all_sentences = []
    for page_num, text in text_by_page.items():
        # Split on sentence boundaries
        sentences = re.split(r'(?<=[。！？；\.\!\?])\s+', text.replace('\n', ' '))
        for s in sentences:
            s = s.strip()
            if 20 < len(s) < max_quote_len:
                all_sentences.append((page_num, s))
    
    # Score each sentence by keyword matches
    best_score = 0
    best_page = None
    best_sent = None
    
    for page_num, sent in all_sentences:
        sent_lower = sent.lower()
        score = 0
        for term in search_terms:
            if term.lower() in sent_lower:
                score += len(term)  # longer terms score higher
        
        if score > best_score:
            best_score = score
            best_page = page_num
            best_sent = sent
    
    if best_score >= 3:  # minimum threshold
        return best_sent, f"p.{best_page}"
    return None, None


def verify_prototype(json_path, field='performance_data'):
    """Verify all needs_review rows in a prototype JSON."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    pid = data.get('id', json_path.stem)
    items = data.get(field, [])
    
    if field == 'mechanisms':
        # mechanisms is a flat list in the JSON
        pass
    
    verified = 0
    skipped_no_pdf = 0
    skipped_no_match = 0
    already_done = 0
    
    for item in items:
        v = item.get('verification', 'unverified')
        if v not in ('needs_review', 'unverified'):
            already_done += 1
            continue
        
        source_file = item.get('source_file', '')
        pdf_path = find_pdf(source_file)
        
        if not pdf_path:
            skipped_no_pdf += 1
            continue
        
        # Build search terms from item fields
        if field == 'performance_data':
            terms = []
            for k in ['pollutant', 'parameter', 'material', 'value']:
                val = item.get(k, '')
                if val:
                    # Extract key terms (numbers, chemical names)
                    terms.extend(re.findall(r'[A-Z][a-z]{2,}|\d+\.?\d*|[A-Z]\([IVX]+\)', str(val)))
                    if item.get('pollutant'):
                        terms.append(str(item['pollutant'])[:30])
            search_terms = list(set(terms))[:10]
        else:  # mechanisms
            name = item.get('name', '')
            desc = item.get('description', '')
            terms = re.findall(r'[A-Z][a-z]{2,}|\d+\.?\d*|[\u4e00-\u9fff]{2,}', f'{name} {desc}')
            search_terms = list(set(terms))[:10]
        
        if not search_terms:
            skipped_no_match += 1
            continue
        
        # Extract PDF text and find quote
        text_by_page = extract_pdf_text(pdf_path)
        quote, locator = find_quote_in_text(text_by_page, search_terms)
        
        if quote:
            item['verification_quote'] = quote
            item['source_locator'] = locator
            item['verification'] = 'partial'
            verified += 1
        else:
            skipped_no_match += 1
    
    # Save
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    return {
        'prototype': pid,
        'field': field,
        'total': len(items),
        'already_done': already_done,
        'verified_this_run': verified,
        'skipped_no_pdf': skipped_no_pdf,
        'skipped_no_match': skipped_no_match
    }


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else ['chitosan', 'cell-membrane-ion-channel']
    
    print(f"Batch verification for: {', '.join(targets)}")
    print(f"PDF root: {PDF_ROOT}")
    print(f"Total PDFs available: {len(glob.glob(str(PDF_ROOT / '**/*.pdf'), recursive=True))}")
    print()
    
    results = []
    for target in targets:
        json_path = DB_DIR / f'{target}.json'
        if not json_path.exists():
            print(f"SKIP: {json_path} not found")
            continue
        
        # Verify performance_data
        r_perf = verify_prototype(json_path, 'performance_data')
        results.append(r_perf)
        print(f"  {target} performance_data: {r_perf['verified_this_run']} verified, "
              f"{r_perf['already_done']} already done, "
              f"{r_perf['skipped_no_pdf']} no PDF, "
              f"{r_perf['skipped_no_match']} no match")
        
        # Verify mechanisms
        r_mech = verify_prototype(json_path, 'mechanisms')
        results.append(r_mech)
        print(f"  {target} mechanisms: {r_mech['verified_this_run']} verified, "
              f"{r_mech['already_done']} already done, "
              f"{r_mech['skipped_no_pdf']} no PDF, "
              f"{r_mech['skipped_no_match']} no match")
    
    # Summary
    total_verified = sum(r['verified_this_run'] for r in results)
    total_perf = sum(r['total'] for r in results if r['field'] == 'performance_data')
    total_mech = sum(r['total'] for r in results if r['field'] == 'mechanisms')
    perf_done = sum(r['verified_this_run'] + r['already_done'] for r in results if r['field'] == 'performance_data')
    mech_done = sum(r['verified_this_run'] + r['already_done'] for r in results if r['field'] == 'mechanisms')
    
    print(f"\n=== Summary ===")
    print(f"  New verified: {total_verified}")
    print(f"  Performance: {perf_done}/{total_perf} ({100*perf_done//max(total_perf,1)}%)")
    print(f"  Mechanisms: {mech_done}/{total_mech} ({100*mech_done//max(total_mech,1)}%)")


if __name__ == '__main__':
    main()
