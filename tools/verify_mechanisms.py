#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mechanism Verification Script
Adds verification_quote and source_locator to mechanism entries by matching ref_doi to local PDFs.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/panyao/Desktop/Biomimetic-design-library")
DOI_MAP_PATH = PROJECT_ROOT / "docs/optimization-v1/_w1_doi_map.json"
TARGET_FILES = [
    PROJECT_ROOT / "prototypes_db/chitosan.json",
    PROJECT_ROOT / "prototypes_db/mussel-foot-adhesion.json",
]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def extract_pdf_text(pdf_path):
    """Extract text from PDF using pdftotext."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=30, encoding="utf-8", errors="replace"
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        return None
    except Exception as e:
        print(f"  [WARN] pdftotext failed for {pdf_path}: {e}")
        return None

def derive_source_locator(filename):
    """Derive AuthorYear prefix from filename, e.g. '2021-Zhang-chitosan...' → 'Zhang2021'."""
    basename = Path(filename).stem
    # Pattern: year-author-...
    m = re.match(r'(\d{4})-([A-Za-z\u4e00-\u9fff]+)', basename)
    if m:
        year, author = m.group(1), m.group(2)
        return f"{author}{year}"
    # CNKI pattern: year-中国author-...
    m = re.match(r'(\d{4})-([\u4e00-\u9fff]+)', basename)
    if m:
        year, author = m.group(1), m.group(2)
        return f"{author}{year}"
    return basename

def extract_keywords(name, description):
    """Extract search keywords from mechanism name and description."""
    text = f"{name or ''} {description or ''}"
    # Remove common filler words
    # Split on common delimiters
    words = re.split(r'[,;，；、\s()（）/\-]+', text)
    # Filter: min length 2, skip common stop words
    stop_words = {'的', '和', '与', '在', '对', '为', '是', '通过', '及', '等',
                  '或', '可', '从', '到', '由', '中', '上', '下', '其', '这',
                  'the', 'of', 'and', 'in', 'to', 'for', 'with', 'by', 'on',
                  'at', 'from', 'an', 'a', 'is', 'are', 'was', 'were', 'be',
                  'or', 'as', 'that', 'this', 'which', 'has', 'have', 'had',
                  'can', 'may', 'will', 'do', 'does', 'did', 'not', 'no',
                  'but', 'if', 'so', 'than', 'more', 'other', 'into'}
    keywords = []
    for w in words:
        w = w.strip()
        if len(w) >= 2 and w.lower() not in stop_words:
            keywords.append(w)
    return keywords[:15]  # limit to top 15 keywords

def find_quote_in_text(pdf_text, keywords, description, max_len=500):
    """Find a relevant sentence/paragraph in PDF text matching mechanism keywords."""
    if not pdf_text:
        return None

    # Split into sentences (handle both Chinese and English)
    # For Chinese: split on 。！？；\n
    # For English: split on . ! ? followed by space/newline
    sentences = re.split(r'(?<=[。！？；\n.!?])\s*', pdf_text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    # Score each sentence by keyword matches
    scored = []
    desc_lower = (description or "").lower()
    for sent in sentences:
        sent_lower = sent.lower()
        score = 0
        matched_kws = []
        for kw in keywords:
            kw_lower = kw.lower()
            if kw_lower in sent_lower:
                # Longer keywords get higher weight
                score += len(kw)
                matched_kws.append(kw)
        # Bonus if sentence contains key phrases from description
        if desc_lower and len(desc_lower) > 5:
            desc_words = set(re.split(r'[,;，；、\s()（）/]+', desc_lower))
            desc_words = {w for w in desc_words if len(w) >= 3}
            for dw in desc_words:
                if dw in sent_lower:
                    score += 3
        if score > 0:
            scored.append((score, sent, matched_kws))

    if not scored:
        return None

    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_sent, matched = scored[0]

    # Need at least 2 keyword matches or a long keyword match
    if best_score < 4:
        return None

    # Expand to include surrounding context for a better quote
    # Find the position in pdf_text and grab a wider window
    pos = pdf_text.find(best_sent[:80])
    if pos >= 0:
        # Expand to full sentence boundaries
        start = max(0, pos - 100)
        end = min(len(pdf_text), pos + len(best_sent) + 100)
        # Find sentence boundaries
        # Look back for sentence start
        for i in range(pos, start, -1):
            if pdf_text[i] in '。！？；\n':
                start = i + 1
                break
        # Look forward for sentence end
        for i in range(pos + len(best_sent), end):
            if pdf_text[i] in '。！？；\n':
                end = i + 1
                break
        expanded = pdf_text[start:end].strip()
        if len(expanded) > 20:
            best_sent = expanded

    # Truncate if too long
    if len(best_sent) > max_len:
        best_sent = best_sent[:max_len] + "..."

    return best_sent

def process_file(json_path, doi_map):
    """Process a single JSON file, adding verification_quote and source_locator to mechanisms."""
    data = load_json(json_path)
    mechanisms = data.get("mechanisms", [])

    # Group mechanisms by ref_doi for batch PDF processing
    doi_groups = {}
    for i, mech in enumerate(mechanisms):
        if mech.get("verification") != "needs_review":
            continue
        ref_doi = mech.get("ref_doi")
        if not ref_doi:
            continue
        if ref_doi not in doi_map:
            continue
        if ref_doi not in doi_groups:
            doi_groups[ref_doi] = []
        doi_groups[ref_doi].append(i)

    print(f"\n{'='*60}")
    print(f"Processing: {json_path.name}")
    print(f"Total mechanisms: {len(mechanisms)}")
    print(f"needs_review with DOI in map: {sum(len(v) for v in doi_groups.values())}")
    print(f"Unique DOIs to process: {len(doi_groups)}")

    stats = {"partial": 0, "unchanged": 0, "pdf_fail": 0}
    sample_quotes = []

    for doi, indices in doi_groups.items():
        pdf_rel = doi_map[doi]
        pdf_path = PROJECT_ROOT / pdf_rel
        if not pdf_path.exists():
            # Try without the ./ prefix
            pdf_path = PROJECT_ROOT / pdf_rel.lstrip("./")
        if not pdf_path.exists():
            print(f"  [SKIP] PDF not found: {pdf_rel}")
            stats["pdf_fail"] += len(indices)
            continue

        source_loc = derive_source_locator(pdf_rel)
        print(f"\n  DOI: {doi}")
        print(f"  PDF: {pdf_path.name}")
        print(f"  Source locator prefix: {source_loc}")
        print(f"  Mechanisms to verify: {len(indices)}")

        # Extract PDF text once per DOI
        pdf_text = extract_pdf_text(pdf_path)
        if not pdf_text:
            print(f"  [SKIP] Could not extract text from PDF")
            stats["pdf_fail"] += len(indices)
            continue

        print(f"  PDF text length: {len(pdf_text)} chars")

        for idx in indices:
            mech = mechanisms[idx]
            name = mech.get("name", "")
            desc = mech.get("description", "")

            keywords = extract_keywords(name, desc)
            quote = find_quote_in_text(pdf_text, keywords, desc)

            if quote:
                mech["verification_quote"] = quote
                mech["source_locator"] = f"{source_loc}"
                mech["verification"] = "partial"
                stats["partial"] += 1
                if len(sample_quotes) < 5:
                    sample_quotes.append({
                        "mechanism": name[:60],
                        "quote": quote[:150],
                        "source_locator": source_loc,
                        "doi": doi
                    })
                print(f"    ✅ {name[:50]}... → partial")
            else:
                stats["unchanged"] += 1
                print(f"    ❌ {name[:50]}... → no match")

    # Update provenance_summary
    provenance = data.get("provenance_summary", {})
    # Count actual verifications
    total_mechs = len(mechanisms)
    verified_count = sum(1 for m in mechanisms if m.get("verification") == "verified")
    partial_count = sum(1 for m in mechanisms if m.get("verification") == "partial")
    needs_review_count = sum(1 for m in mechanisms if m.get("verification") == "needs_review")

    provenance["n_mechanisms"] = total_mechs
    provenance["n_mechanisms_verified"] = verified_count
    provenance["n_mechanisms_partial"] = partial_count
    provenance["n_mechanisms_needs_review"] = needs_review_count
    data["provenance_summary"] = provenance

    # Save
    save_json(json_path, data)

    return stats, sample_quotes

def main():
    doi_map = load_json(DOI_MAP_PATH)
    print(f"Loaded DOI map: {len(doi_map)} entries")

    all_stats = {}
    all_samples = []

    for target in TARGET_FILES:
        if not target.exists():
            print(f"[ERROR] File not found: {target}")
            continue
        stats, samples = process_file(target, doi_map)
        all_stats[target.name] = stats
        all_samples.extend(samples)

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for fname, stats in all_stats.items():
        print(f"\n{fname}:")
        print(f"  → partial: {stats['partial']}")
        print(f"  → unchanged: {stats['unchanged']}")
        print(f"  → pdf_fail: {stats['pdf_fail']}")

    if all_samples:
        print(f"\nSample quotes (up to 5):")
        for i, s in enumerate(all_samples, 1):
            print(f"\n  {i}. [{s['source_locator']}] {s['mechanism']}")
            print(f"     DOI: {s['doi']}")
            print(f"     Quote: {s['quote']}")

    return all_stats

if __name__ == "__main__":
    main()
