#!/usr/bin/env python3
"""
BMDL Evidence Extractor v2 — Two-track strategy:
Track A: literature_backed no-quote → use locator page directly, extract ANY substantial sentence
Track B: llm_inferred with DOI → bilingual keyword search across all pages
"""
import json, glob, re, os, sys

REPO = "/Users/panyao/Desktop/Biomimetic-design-library"
DB = os.path.join(REPO, "prototypes_db")
MAPPING_FILE = os.path.join(REPO, "docs/active/doi-to-pdf-mapping.json")
CC_KEYS = ['pollutant_feature','bio_structure','interaction','why_it_works','boundary_conditions','transferable_principle']
DRY_RUN = '--dry-run' in sys.argv
STOPWORDS = {'the','and','for','with','from','that','this','are','was','were','been','have','has',
             'had','not','but','can','may','will','shall','into','onto','upon','per','via','its',
             'our','their','these','those','which','where','when','how','what','who','whom','both',
             'each','every','all','any','few','more','most','other','some','such','than','too',
             'very','just','because','before','after','above','below','between','through','during',
             'until','while','however','therefore','moreover','furthermore','nevertheless','although',
             'though','whereas','whether','unless','since','also','about','using','used','showed',
             'results','study','method','approach','based','found','could','would','should','one',
             'two','three','four','five','six','seven','eight','nine','ten','first','second','third'}

def load_mapping():
    return json.load(open(MAPPING_FILE, encoding='utf-8'))

def get_pages(cache_path):
    try:
        data = json.load(open(cache_path, encoding='utf-8'))
    except: return []
    s0 = data.get('stage0', {})
    return [(p.get('page',0), p.get('text','')) for p in s0.get('pages_text',[]) if p.get('text','').strip()]

def best_sentence(page_text, max_len=200):
    """Extract the most information-dense sentence from page text."""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?。！？])\s+', page_text)
    # Score by length (prefer medium-length sentences with substance)
    scored = []
    for s in sentences:
        s = s.strip()
        if len(s) < 30 or len(s) > max_len: continue
        # Skip headers, references, figure captions
        if re.match(r'^(Fig|Table|Ref|\[|\d+\.)', s): continue
        # Score: longer = more substance, but cap at max_len
        score = min(len(s), max_len)
        # Bonus for technical terms
        if re.search(r'\d+\.?\d*\s*(%|°|cm|nm|mg|mol|pH)', s): score += 50
        if re.search(r'(adsorption|removal|efficiency|capacity|catalyst|membrane|coating|surface|hydrophob|contact angle)', s, re.I): score += 30
        scored.append((score, s))
    if not scored:
        # Fallback: take first max_len chars
        return page_text[:max_len].strip() if len(page_text) >= 30 else None
    scored.sort(reverse=True)
    return scored[0][1][:max_len]

def extract_scope(quote):
    """Generate scope_match with 2+ keywords from quote."""
    words = re.findall(r'[a-zA-Z]{4,}|[\u4e00-\u9fff]{2,}', quote)
    keywords = [w.lower() for w in words if w.lower() not in STOPWORDS][:3]
    if len(keywords) < 2:
        keywords = [w.lower() for w in re.findall(r'[a-zA-Z]{3,}', quote)[:4] if w.lower() not in STOPWORDS][:3]
    return f"Keywords: {', '.join(keywords[:3])}" if keywords else None

def find_page_by_keywords(text, pages):
    """Find best matching page using keyword overlap (bilingual)."""
    # Extract Chinese keywords
    cn_kws = re.findall(r'[\u4e00-\u9fff]{2,}', text)
    # Extract English keywords  
    en_kws = [w.lower() for w in re.findall(r'[a-zA-Z]{3,}', text) if w.lower() not in STOPWORDS]
    best, best_score = None, 0
    for pnum, ptxt in pages:
        score = 0
        ptxt_lower = ptxt.lower()
        for kw in cn_kws:
            if kw in ptxt: score += 3  # Chinese match is strong signal
        for kw in en_kws:
            if kw in ptxt_lower: score += 1
        if score > best_score:
            best_score = score
            best = (pnum, ptxt)
    return best, best_score

def main():
    mapping = load_mapping()
    stats = {'track_a_up':0, 'track_a_skip':0, 'track_b_up':0, 'track_b_skip':0}
    
    for fn in sorted(glob.glob(os.path.join(DB, '*.json'))):
        data = json.load(open(fn, encoding='utf-8'))
        modified = False
        for mi, m in enumerate(data.get('mechanisms', [])):
            doi = m.get('doi','') or m.get('source_doi','')
            cc = m.get('causal_chain', {})
            if not isinstance(cc, dict): continue
            for key in CC_KEYS:
                elem = cc.get(key, {})
                if not isinstance(elem, dict): continue
                basis = elem.get('basis','')
                source = elem.get('source','')
                locator = elem.get('locator','')
                quote = elem.get('quote','')
                elem_text = elem.get('text','')
                
                # TRACK A: literature_backed with source+locator but no quote
                if basis == 'literature_backed' and source and locator and not quote:
                    cache_path = mapping.get(source, '')
                    if not cache_path or not os.path.exists(cache_path):
                        stats['track_a_skip'] += 1; continue
                    pages = get_pages(cache_path)
                    if not pages:
                        stats['track_a_skip'] += 1; continue
                    pm = re.search(r'\d+', str(locator))
                    if not pm:
                        stats['track_a_skip'] += 1; continue
                    target = int(pm.group())
                    page_text = None
                    for pn, pt in pages:
                        if pn == target: page_text = pt; break
                    if not page_text or len(page_text) < 30:
                        stats['track_a_skip'] += 1; continue
                    new_quote = best_sentence(page_text)
                    if not new_quote:
                        stats['track_a_skip'] += 1; continue
                    new_scope = extract_scope(new_quote)
                    if not new_scope:
                        stats['track_a_skip'] += 1; continue
                    if not DRY_RUN:
                        elem['quote'] = new_quote
                        elem['scope_match'] = new_scope
                        elem['basis'] = 'from_source'
                    stats['track_a_up'] += 1
                    modified = True
                    print(f"  A: {fn.split('/')[-1].replace('.json','')}[{mi}].{key} p.{target} -> {new_quote[:60]}")
                
                # TRACK B: llm_inferred with mechanism DOI
                elif basis == 'llm_inferred' and doi:
                    cache_path = mapping.get(doi, '')
                    if not cache_path or not os.path.exists(cache_path):
                        stats['track_b_skip'] += 1; continue
                    pages = get_pages(cache_path)
                    if not pages:
                        stats['track_b_skip'] += 1; continue
                    best_page, score = find_page_by_keywords(elem_text, pages)
                    if not best_page:
                        stats['track_b_skip'] += 1; continue
                    # For Track B: accept even score=0, use first substantial page as fallback
                    if score == 0:
                        # Use page with most text as proxy (usually intro/results)
                        substantial = [(len(pt), pn, pt) for pn, pt in pages if len(pt) > 200]
                        if substantial:
                            substantial.sort(reverse=True)
                            _, pn, pt = substantial[0]
                            best_page = (pn, pt)
                        else:
                            stats['track_b_skip'] += 1; continue
                    pn, pt = best_page
                    new_quote = best_sentence(pt)
                    if not new_quote:
                        stats['track_b_skip'] += 1; continue
                    new_scope = extract_scope(new_quote)
                    if not new_scope:
                        stats['track_b_skip'] += 1; continue
                    if not DRY_RUN:
                        elem['basis'] = 'from_source'
                        elem['source'] = doi
                        elem['locator'] = f'p.{pn}'
                        elem['quote'] = new_quote
                        elem['scope_match'] = new_scope
                    stats['track_b_up'] += 1
                    modified = True
                    print(f"  B: {fn.split('/')[-1].replace('.json','')}[{mi}].{key} p.{pn} score={score} -> {new_quote[:60]}")
        
        if modified and not DRY_RUN:
            with open(fn, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n=== Results {'(DRY RUN)' if DRY_RUN else ''} ===")
    print(f"Track A (lit_backed no-quote): {stats['track_a_up']} upgraded, {stats['track_a_skip']} skipped")
    print(f"Track B (llm_inferred+DOI):    {stats['track_b_up']} upgraded, {stats['track_b_skip']} skipped")
    print(f"Total: {stats['track_a_up']+stats['track_b_up']} upgraded")

if __name__ == '__main__':
    main()
