#!/usr/bin/env python3
"""
PDA-coating performance_data PDF verification script.
Extracts real text quotes from source PDFs for each performance_data row.
"""

import json
import os
import re
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    import PyMuPDF as fitz

PROJECT = "/Users/panyao/Desktop/Biomimetic-design-library"
JSON_PATH = os.path.join(PROJECT, "prototypes_db/polydopamine-coating.json")

def find_pdf(source_file):
    """Find the actual PDF file path, handling ' 2' suffixes and path variations."""
    base = os.path.join(PROJECT, source_file)
    if os.path.exists(base):
        return base
    # Try with " 2" suffix
    root, ext = os.path.splitext(base)
    alt = root + " 2" + ext
    if os.path.exists(alt):
        return alt
    # Try searching by filename pattern
    fname = os.path.basename(source_file)
    fname_no_ext = os.path.splitext(fname)[0]
    for dirpath, dirnames, filenames in os.walk(os.path.join(PROJECT, "仿生文献库")):
        for f in filenames:
            if f.endswith(".pdf") and fname_no_ext in f:
                return os.path.join(dirpath, f)
    return None

def extract_page_text(pdf_path, page_num):
    """Extract text from a specific page (1-indexed)."""
    doc = fitz.open(pdf_path)
    try:
        if page_num <= len(doc):
            page = doc[page_num - 1]
            return page.get_text()
        # If page_num exceeds total pages, try last few pages
        for i in range(max(0, page_num - 3), len(doc)):
            page = doc[i]
            text = page.get_text()
            if text.strip():
                return text
        return doc[-1].get_text()
    finally:
        doc.close()

def extract_all_text(pdf_path):
    """Extract full text from PDF."""
    doc = fitz.open(pdf_path)
    try:
        return "\n".join(page.get_text() for page in doc)
    finally:
        doc.close()

def find_quote_in_text(full_text, search_terms, context_chars=300):
    """Find a sentence/paragraph containing the search terms."""
    lines = full_text.split('\n')
    
    # Try to find lines containing key terms
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean or len(line_clean) < 10:
            continue
        
        # Check if all search terms appear in nearby context
        context = '\n'.join(lines[max(0,i-2):min(len(lines),i+3)])
        all_found = True
        for term in search_terms:
            if term.lower() not in context.lower():
                all_found = False
                break
        
        if all_found:
            # Build a quote from surrounding lines
            quote_lines = []
            for j in range(max(0, i-1), min(len(lines), i+4)):
                l = lines[j].strip()
                if l:
                    quote_lines.append(l)
            quote = ' '.join(quote_lines)
            # Clean up
            quote = re.sub(r'\s+', ' ', quote).strip()
            if len(quote) > 500:
                quote = quote[:500] + "..."
            return quote
    
    # Fallback: search for just the value
    for i, line in enumerate(lines):
        for term in search_terms:
            if term in line:
                context_start = max(0, i-1)
                context_end = min(len(lines), i+3)
                quote_lines = [lines[j].strip() for j in range(context_start, context_end) if lines[j].strip()]
                quote = ' '.join(quote_lines)
                quote = re.sub(r'\s+', ' ', quote).strip()
                if len(quote) > 500:
                    quote = quote[:500] + "..."
                return quote
    
    return None

def find_page_for_value(pdf_path, value_str, hint_page=None):
    """Find which page contains the value, returning (page_num, text_snippet)."""
    doc = fitz.open(pdf_path)
    try:
        # First try the hint page
        if hint_page and hint_page <= len(doc):
            text = doc[hint_page - 1].get_text()
            if value_str in text:
                return hint_page, text
        
        # Search all pages
        for i, page in enumerate(doc):
            text = page.get_text()
            if value_str in text:
                return i + 1, text
        
        # Return hint page text as fallback
        if hint_page and hint_page <= len(doc):
            return hint_page, doc[hint_page - 1].get_text()
        return None, None
    finally:
        doc.close()

def process_row(row, idx):
    """Process a single performance_data row, returning updated row."""
    source_file = row.get("source_file", "")
    patent_number = row.get("patent_number", "")
    value = row.get("value", "")
    
    # CN114887602A - missing PDF
    if patent_number == "CN114887602A":
        row["verification"] = "missing_pdf"
        row["verification_quote"] = "PDF not available locally"
        row["source_locator"] = "N/A"
        return row
    
    pdf_path = find_pdf(source_file)
    if not pdf_path:
        print(f"  [WARN] Row {idx}: PDF not found for {source_file}")
        row["verification"] = "needs_review"
        row["verification_quote"] = "PDF file not found in local library"
        row["source_locator"] = "N/A"
        return row
    
    page_hint = row.get("page", 1)
    
    # Build search terms from the value
    # Extract numeric values from the value string
    numeric_vals = re.findall(r'[\d.]+', str(value))
    
    # Get full text for broader search
    full_text = extract_all_text(pdf_path)
    
    # Strategy: search for the key value(s) in the PDF
    quote = None
    found_page = None
    
    # Try searching for numeric values
    for num_val in numeric_vals[:3]:  # Try first 3 numeric values
        pg, pg_text = find_page_for_value(pdf_path, num_val, page_hint)
        if pg_text:
            # Find sentence containing this value
            search_terms = [num_val]
            # Add pollutant name if available
            pollutant = row.get("pollutant", "")
            if pollutant:
                search_terms.append(pollutant[:20])
            
            quote = find_quote_in_text(pg_text, search_terms)
            if quote:
                found_page = pg
                break
    
    # If no quote found with numeric, try broader search
    if not quote:
        # Try searching full text with multiple terms
        pollutant = row.get("pollutant", "")
        material = row.get("material", "")
        param = row.get("parameter", "")
        
        all_terms = []
        if numeric_vals:
            all_terms.append(numeric_vals[0])
        if pollutant:
            all_terms.append(pollutant[:15])
        
        if all_terms:
            quote = find_quote_in_text(full_text, all_terms)
            if quote:
                # Find page
                for num_val in numeric_vals[:1]:
                    pg, _ = find_page_for_value(pdf_path, num_val, page_hint)
                    if pg:
                        found_page = pg
                        break
    
    if quote:
        row["verification_quote"] = quote
        row["source_locator"] = f"p.{found_page}" if found_page else row.get("locator", "")
        row["verification"] = "partial"
    else:
        row["verification"] = "needs_review"
        row["verification_quote"] = f"Value '{value}' not found in PDF text extraction"
        row["source_locator"] = row.get("locator", "")
    
    return row

def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    perf_data = data["performance_data"]
    print(f"Processing {len(perf_data)} performance_data rows...")
    
    for i, row in enumerate(perf_data):
        print(f"\n--- Row {i}: {row.get('parameter', '')[:60]} ---")
        print(f"  Value: {row.get('value', '')}")
        print(f"  Source: {row.get('source_file', '')}")
        
        updated = process_row(row, i)
        
        vq = updated.get("verification_quote", "")
        print(f"  Quote: {vq[:120]}..." if len(vq) > 120 else f"  Quote: {vq}")
        print(f"  Status: {updated.get('verification', '')}")
    
    # Write back
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n\nDone. Updated {len(perf_data)} rows.")
    
    # Summary
    from collections import Counter
    statuses = Counter(row.get("verification", "") for row in perf_data)
    print(f"\nVerification status summary:")
    for status, count in statuses.most_common():
        print(f"  {status}: {count}")

if __name__ == "__main__":
    main()
