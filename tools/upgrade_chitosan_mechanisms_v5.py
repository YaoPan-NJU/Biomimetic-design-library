#!/usr/bin/env python3
"""
Upgrade llm_inferred mechanisms in chitosan.json with real evidence.
Version 5: Fixed scope_match to be a proper list.
"""

import json
import os
import re
from typing import Dict, List, Optional, Tuple

# Paths
CHITOSAN_JSON = '/Users/panyao/Desktop/Biomimetic-design-library/prototypes_db/chitosan.json'
EXTRACTIONS_DIR = '/Users/panyao/Desktop/Biomimetic-design-library/tools/litextract/outputs/extractions/论文/json'

# Minimum keyword length
MIN_KEYWORD_LENGTH = 3

# Stop words
STOP_WORDS = {
    'the', 'and', 'for', 'with', 'from', 'that', 'this', 'are', 'was', 'were',
    'been', 'have', 'has', 'had', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'can', 'shall', 'its', 'not', 'but', 'all',
    'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such',
    'than', 'too', 'very', 'just', 'also', 'now', 'then', 'here', 'there',
    'when', 'where', 'why', 'how', 'what', 'which', 'who', 'whom', 'whose',
    'if', 'because', 'until', 'while', 'of', 'at', 'by', 'in', 'to', 'on',
    'about', 'against', 'between', 'through', 'during', 'before', 'after',
    'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again',
    'further', 'once', 'into', 'onto', 'upon', 'is', 'am', 'be', 'being',
    'do', 'doing', 'need', 'dare', 'ought', 'used', 'it', 'itself', 'they',
    'them', 'their', 'themselves', 'he', 'him', 'his', 'himself', 'she',
    'her', 'hers', 'herself', 'we', 'us', 'our', 'ours', 'ourselves',
    'you', 'your', 'yours', 'yourself', 'yourselves', 'i', 'me', 'my',
    'mine', 'myself', 'very', 'really', 'quite', 'just', 'already', 'still',
    'well', 'back', 'even', 'still', 'also', 'however', 'although', 'though',
    'since', 'because', 'therefore', 'thus', 'hence', 'consequently',
    'between', 'among', 'within', 'without'
}

CHINESE_STOP = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个',
                '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好',
                '自己', '这', '他', '她', '它', '们', '那', '被', '从', '把', '让', '用', '对',
                '与', '以', '及', '等', '但', '或', '而', '如', '所', '之', '其', '这个', '那个',
                '什么', '怎么', '为什么', '哪里', '哪个', '多少', '几', '谁', '怎样', '什么样'}

# Known chemical terms to preserve as-is
CHEMICAL_TERMS = {
    'chitosan', 'chitin', 'alginate', 'cellulose', 'collagen', 'gelatin',
    '壳聚糖', '甲壳素', '海藻酸', '纤维素', '胶原蛋白', '明胶',
    'amine', 'hydroxyl', 'carboxyl', 'phosphate', 'sulfate', 'nitrate',
    '氨基', '羟基', '羧基', '磷酸', '硫酸', '硝酸', '盐酸',
    'chelation', 'complexation', 'adsorption', 'absorption', 'precipitation',
    '螯合', '配位', '吸附', '吸收', '沉淀',
    'protonation', 'deprotonation', 'electrostatic', 'coordination',
    '质子化', '去质子化', '静电', '配位',
    'HSAB', 'pHpzc', 'FTIR', 'XPS', 'XRD', 'SEM', 'TEM', 'BET',
    'Langmuir', 'Freundlich', 'pseudo', 'isotherm', 'kinetic',
    'Irving-Williams', 'TiO2', 'SiO2', 'Al2O3', 'Fe3O4', 'ZnO', 'CuO',
    'Ag', 'Au', 'Pt', 'Pd', 'Cu', 'Pb', 'Zn', 'Ni', 'Hg', 'Cd', 'Cr',
    'Co', 'Mn', 'Fe', 'Al', 'Na', 'K', 'Ca', 'Mg', 'La', 'Ce'
}


def load_extraction_by_doi(doi: str) -> Optional[dict]:
    """Find extraction JSON by DOI."""
    if not doi or doi.startswith('patent') or doi.startswith('仿生文献库'):
        return None
    for fname in os.listdir(EXTRACTIONS_DIR):
        if not fname.endswith('.json'):
            continue
        fpath = os.path.join(EXTRACTIONS_DIR, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data.get('bibliographic_metadata', {}).get('doi') == doi:
                return data
        except Exception:
            continue
    return None


def load_extraction_by_source_file(source_file: str) -> Optional[dict]:
    """Find extraction JSON by source_file name."""
    if not source_file:
        return None
    basename = os.path.basename(source_file)
    name_no_ext = os.path.splitext(basename)[0]
    extraction_path = os.path.join(EXTRACTIONS_DIR, name_no_ext + '.json')
    if os.path.exists(extraction_path):
        with open(extraction_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    clean_name = re.sub(r'\s+\d+$', '', name_no_ext)
    extraction_path = os.path.join(EXTRACTIONS_DIR, clean_name + '.json')
    if os.path.exists(extraction_path):
        with open(extraction_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def extract_keywords(text: str) -> List[str]:
    """Extract meaningful keywords from text as a list."""
    keywords = []

    # Chinese terms (2+ chars, exclude stop words)
    chinese_terms = re.findall(r'[一-鿿]+', text)
    for term in chinese_terms:
        if len(term) >= 2 and term not in CHINESE_STOP:
            keywords.append(term)

    # Extract chemical terms first (preserve case)
    for term in CHEMICAL_TERMS:
        if term.lower() in text.lower() or term in text:
            if term not in keywords:
                keywords.append(term)

    # English terms (3+ chars, complete words only)
    english_pattern = r'\b[a-zA-Z][a-zA-Z\-]{2,}\b'
    english_terms = re.findall(english_pattern, text)
    for term in english_terms:
        term_lower = term.lower()
        if len(term) >= MIN_KEYWORD_LENGTH and term_lower not in STOP_WORDS:
            if term not in CHEMICAL_TERMS and term_lower not in {t.lower() for t in CHEMICAL_TERMS}:
                if term not in keywords:
                    keywords.append(term)

    return keywords


def find_scope_match_from_existing(verification_quote: str, claim_text: str) -> List[str]:
    """Extract scope_match keywords from existing verification_quote."""
    if not verification_quote or not claim_text:
        return []

    claim_keywords = extract_keywords(claim_text)
    if not claim_keywords:
        return []

    quote_lower = verification_quote.lower()
    matched = []
    for kw in claim_keywords:
        if len(kw) < MIN_KEYWORD_LENGTH:
            continue
        # Use word boundary matching for English terms
        if re.search(r'\b' + re.escape(kw.lower()) + r'\b', quote_lower):
            if kw not in matched:
                matched.append(kw)
        elif kw.lower() in quote_lower:
            if kw not in matched:
                matched.append(kw)

    return matched[:5]


def find_evidence_from_extraction(claim_text: str, extraction: dict,
                                  max_quote_len: int = 200) -> Optional[Tuple[str, str, str, List[str]]]:
    """Find supporting evidence from extraction JSON."""
    if not extraction:
        return None

    keywords = extract_keywords(claim_text)
    if not keywords:
        return None

    evidences = []
    for ki in extraction.get('knowledge_items', []):
        for ev in ki.get('evidence', []):
            page = ev.get('page', 0)
            locator = ev.get('locator', '')
            text = ev.get('evidence_text', '')
            if text:
                evidences.append((page, locator, text))

    if not evidences:
        return None

    best_match = None
    best_score = 0

    for page, locator, text in evidences:
        text_lower = text.lower()

        matched_keywords = []
        for kw in keywords:
            if len(kw) < MIN_KEYWORD_LENGTH:
                continue
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', text_lower):
                if kw not in matched_keywords:
                    matched_keywords.append(kw)
            elif kw.lower() in text_lower:
                if kw not in matched_keywords:
                    matched_keywords.append(kw)

        if len(matched_keywords) < 2:
            continue

        score = len(matched_keywords) * 2

        mech_terms = ['mechanism', 'adsorption', 'chelation', 'complexation', 'electrostatic',
                      'coordination', 'interaction', 'binding', 'protonation', 'deprotonation',
                      'functional group', 'amine', 'hydroxyl', 'metal ion', 'chitosan',
                      'NH2', 'OH', 'pH', 'HSAB', 'chelate', 'ligand',
                      '螯合', '配位', '吸附', '静电', '氢键', '氨基', '羟基', '官能团',
                      '质子化', '去质子化', '机制', '机理']
        score += sum(0.5 for t in mech_terms if t.lower() in text_lower)

        if len(text) > 100:
            score += 1

        if score > best_score:
            best_score = score
            best_match = (page, locator, text, matched_keywords)

    if best_match and best_score >= 4:
        page, locator, text, matched_keywords = best_match
        quote = text[:max_quote_len]
        if len(text) > max_quote_len:
            last_period = quote.rfind('. ')
            if last_period > max_quote_len * 0.7:
                quote = quote[:last_period + 1]
            else:
                quote = quote.rstrip() + '...'
        page_str = f"page {page}" if page else "page unknown"
        scope_match = [kw for kw in matched_keywords if len(kw) >= MIN_KEYWORD_LENGTH][:5]
        return page_str, locator, quote, scope_match

    return None


def upgrade_mechanism_hybrid(mech: dict, extraction: Optional[dict]) -> Tuple[dict, bool]:
    """Upgrade mechanism using hybrid approach."""
    upgraded = False
    cc = mech.get('causal_chain', {})

    existing_quote = cc.get('verification_quote', '')
    existing_locator = cc.get('source_locator', '')

    for field in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
        if field not in cc:
            continue
        field_data = cc[field]
        if not isinstance(field_data, dict) or field_data.get('basis') != 'llm_inferred':
            continue
        claim_text = field_data.get('text', '')
        if not claim_text:
            continue

        # Strategy 1: Use existing verification_quote
        if existing_quote:
            scope_match = find_scope_match_from_existing(existing_quote, claim_text)
            if len(scope_match) >= 2:
                field_data['basis'] = 'from_source'
                field_data['locator'] = existing_locator or 'from mechanism verification_quote'
                field_data['quote'] = existing_quote[:200]
                field_data['scope_match'] = scope_match  # This is already a list
                field_data['source_asset'] = ''
                upgraded = True
                continue

        # Strategy 2: Try extraction
        if extraction:
            evidence = find_evidence_from_extraction(claim_text, extraction)
            if evidence:
                page_str, locator, quote, scope_match = evidence
                field_data['basis'] = 'from_source'
                field_data['locator'] = page_str
                field_data['quote'] = quote
                field_data['scope_match'] = scope_match  # This is already a list
                field_data['source_asset'] = extraction.get('bibliographic_metadata', {}).get('file_name', '')
                upgraded = True

    # Boundary conditions
    for bc in cc.get('boundary_conditions', []):
        if not isinstance(bc, dict) or bc.get('basis') != 'llm_inferred':
            continue
        claim_text = bc.get('text', '')
        if not claim_text:
            continue

        if existing_quote:
            scope_match = find_scope_match_from_existing(existing_quote, claim_text)
            if len(scope_match) >= 2:
                bc['basis'] = 'from_source'
                bc['locator'] = existing_locator or 'from mechanism verification_quote'
                bc['quote'] = existing_quote[:200]
                bc['scope_match'] = scope_match  # This is already a list
                bc['source_asset'] = ''
                upgraded = True
                continue

        if extraction:
            evidence = find_evidence_from_extraction(claim_text, extraction)
            if evidence:
                page_str, locator, quote, scope_match = evidence
                bc['basis'] = 'from_source'
                bc['locator'] = page_str
                bc['quote'] = quote
                bc['scope_match'] = scope_match  # This is already a list
                bc['source_asset'] = extraction.get('bibliographic_metadata', {}).get('file_name', '')
                upgraded = True

    return mech, upgraded


def main():
    with open(CHITOSAN_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    mechs = data.get('mechanisms', [])
    extraction_cache = {}
    upgraded_count = 0
    total_llm = 0

    for i, mech in enumerate(mechs):
        cc = mech.get('causal_chain', {})

        has_llm = False
        for field in ['pollutant_feature', 'bio_structure', 'interaction', 'why_it_works']:
            if isinstance(cc.get(field), dict) and cc[field].get('basis') == 'llm_inferred':
                has_llm = True
                break
        if not has_llm:
            for bc in cc.get('boundary_conditions', []):
                if isinstance(bc, dict) and bc.get('basis') == 'llm_inferred':
                    has_llm = True
                    break
        if not has_llm:
            continue

        total_llm += 1
        doi = mech.get('ref_doi') or cc.get('source_doi')
        source_file = mech.get('source_file')
        cache_key = doi or source_file

        if cache_key in extraction_cache:
            extraction = extraction_cache[cache_key]
        else:
            extraction = None
            if doi and not doi.startswith('patent') and not doi.startswith('仿生文献库'):
                extraction = load_extraction_by_doi(doi)
            if not extraction and source_file:
                extraction = load_extraction_by_source_file(source_file)
            extraction_cache[cache_key] = extraction

        mech, upgraded = upgrade_mechanism_hybrid(mech, extraction)
        if upgraded:
            upgraded_count += 1
            print(f"  [{i}] {mech['name'][:50]}: UPGRADED")
        else:
            print(f"  [{i}] {mech['name'][:50]}: no upgrade")

    print(f"\nSummary: {upgraded_count}/{total_llm} mechanisms upgraded")

    with open(CHITOSAN_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved to {CHITOSAN_JSON}")


if __name__ == '__main__':
    main()
