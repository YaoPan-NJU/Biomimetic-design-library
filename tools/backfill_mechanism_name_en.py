#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backfill English fields for all prototypes in prototypes_db/*.json.

Adds (pure additive — preserves existing schema & audit trail):
  - Prototype.organism.scientific_en   (English organism scientific name)
  - Mechanism.name_en                  (concise English mechanism name)
  - Mechanism.description_en           (English abstract of `description`)
  - Mechanism.causal_chain.transferable_principle_en  (English summary of TP)

BMDL rules honored:
  - Dry-run by default: prints the planned change, writes nothing.
    Pass --write to actually mutate the canonical JSON.
  - Surgical: only adds *_en keys; never edits existing fields.
  - LLM via DashScope (OpenAI-compatible). Reads DASHSCOPE_API_KEY /
    DASHSCOPE_BASE_URL from env or a --env .env file.

Usage:
  python -X utf8 tools/backfill_mechanism_name_en.py --dry-run
  python -X utf8 tools/backfill_mechanism_name_en.py --write
  python -X utf8 tools/backfill_mechanism_name_en.py --env /path/adrmats/.env --write
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_HERE = Path(os.path.abspath(__file__)).parent
_PROJECT_ROOT = _HERE.parent
PROTO_DIR = _PROJECT_ROOT / "prototypes_db"

DEFAULT_MODEL = "qwen3.7-max"
DEFAULT_BASE_URL = "https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"

# ---------------------------------------------------------------------------
# LLM helpers
# ---------------------------------------------------------------------------

def _load_env(path: str) -> None:
    if not path:
        return
    envf = Path(path)
    if not envf.exists():
        print(f"[warn] env file not found: {envf}", file=sys.stderr)
        return
    for line in envf.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def _make_client():
    from openai import OpenAI
    api_key = os.getenv("DASHSCOPE_API_KEY", "")
    base_url = os.getenv("DASHSCOPE_BASE_URL", DEFAULT_BASE_URL)
    if not api_key:
        raise RuntimeError("DASHSCOPE_API_KEY not set. Pass --env or export it.")
    return OpenAI(api_key=api_key, base_url=base_url, timeout=300, max_retries=3)


def _translate_prototype(client, model: str, proto: dict, chunk_size: int = 0) -> dict:
    """Translate one prototype's English fields across possibly multiple LLM calls.

    Returns:
        {
          "organism_scientific_en": str,
          "mechanisms": [ {idx, mechanism_id, name_en, description_en, transferable_principle_en}, ... ]
        }
    """
    mech_payload = []
    for idx, m in enumerate(proto.get("mechanisms", [])):
        cc = m.get("causal_chain", {})
        if not isinstance(cc, dict):
            cc = {}
        mech_payload.append({
            "idx": idx,
            "mechanism_id": m.get("mechanism_id", ""),
            "name": m.get("name", ""),
            "description": m.get("description", ""),
            "transferable_principle": cc.get("transferable_principle", ""),
        })

    organism = proto.get("organism", {})
    if isinstance(organism, dict):
        organism_sci = organism.get("scientific", "")
    else:
        organism_sci = str(organism)

    # Split into chunks when the corpus is large (prototype-level single-shot
    # truncates: 110-mechanism chitosan output ~59K chars > 8192-token budget).
    chunks = [mech_payload]
    if chunk_size and len(mech_payload) > chunk_size:
        chunks = [mech_payload[i:i + chunk_size] for i in range(0, len(mech_payload), chunk_size)]

    def _call(mech_chunk):
        prompt = f"""You are translating curated biomimetic-library content from Chinese to English.
Translate faithfully, preserving technical terms, mechanism names, and the causal logic.
Output STRICT JSON only.

Input:
- prototype name_zh: {proto.get('name_zh', '')}
- prototype name_en: {proto.get('name_en', '')}
- organism scientific: {organism_sci}
- mechanisms: {json.dumps(mech_chunk, ensure_ascii=False)}

Output JSON schema:
{{
  "organism_scientific_en": "English scientific name of organism (Latin + plain English, no Chinese)",
  "mechanisms": [
    {{
      "idx": "same integer index as input",
      "mechanism_id": "same as input",
      "name_en": "concise English mechanism name (one phrase, no Chinese)",
      "description_en": "English abstract of the mechanism description (2-4 sentences, no Chinese)",
      "transferable_principle_en": "English summary of the transferable principle (2-3 sentences, no Chinese)"
    }}
  ]
}}

Rules:
- Keep idx and mechanism_id identical to input.
- Output mechanisms in the SAME order as input.
- NO Chinese characters in any output field.
- Do NOT invent facts; translate what is given.
- If a mechanism input is empty, output empty string for that field.
- Return ONLY the JSON, no markdown fence."""
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8192,
            temperature=0.2,
        )
        content = resp.choices[0].message.content or ""
        return _parse_json(content)

    acc = None
    for i, chunk in enumerate(chunks):
        parsed = _call(chunk)
        if acc is None:
            acc = parsed
        else:
            # merge mechanisms; keep first organism (all chunks echo it)
            acc["mechanisms"] = acc.get("mechanisms", []) + parsed.get("mechanisms", [])
    if acc is None:
        acc = {}
    return acc


def _parse_json(content: str) -> dict:
    """Tolerant JSON parse (strip fences, fix trailing commas)."""
    import re
    if "```json" in content:
        content = content.split("```json")[1].split("```")[0].strip()
    elif "```" in content:
        content = content.split("```")[1].split("```")[0].strip()
    content = re.sub(r",\s*}", "}", content)
    content = re.sub(r",\s*]", "]", content)
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass
    # last valid balanced boundary
    try:
        depth = 0
        last_valid = 0
        in_str = False
        esc = False
        for i, ch in enumerate(content):
            if esc:
                esc = False
                continue
            if ch == "\\":
                esc = True
                continue
            if ch == '"':
                in_str = not in_str
                continue
            if in_str:
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    last_valid = i + 1
        if last_valid:
            return json.loads(content[:last_valid])
    except json.JSONDecodeError:
        pass
    # Last resort: extract individual balanced {...} objects (copes with a
    # truncated trailing string / missing closing bracket).
    objs = _extract_objects(content)
    if objs:
        organism_scientific_en = ""
        mechanisms = []
        lang = {"organism_scientific_en": "", "mechanisms": mechanisms}
        for obj in objs:
            if isinstance(obj, dict):
                if obj.get("organism_scientific_en") and not organism_scientific_en:
                    organism_scientific_en = obj["organism_scientific_en"]
                if "mechanisms" in obj and isinstance(obj["mechanisms"], list):
                    mechanisms.extend(o for o in obj["mechanisms"] if isinstance(o, dict))
        lang["organism_scientific_en"] = organism_scientific_en
        return lang
    raise


def _extract_objects(content: str) -> list:
    """Extract every balanced top-level {...} object from a possibly-truncated string."""
    objs = []
    depth = 0
    start = -1
    in_str = False
    esc = False
    for i, ch in enumerate(content):
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                try:
                    objs.append(json.loads(content[start:i + 1]))
                except json.JSONDecodeError:
                    pass
                start = -1
    return objs


# ---------------------------------------------------------------------------
# Apply / preview
# ---------------------------------------------------------------------------

def _apply_en_fields(proto: dict, trans: dict) -> dict:
    """Return a copy of proto with *_en fields added (no mutation of original)."""
    import copy
    p = copy.deepcopy(proto)

    org = p.get("organism")
    if isinstance(org, dict) and trans.get("organism_scientific_en"):
        org["scientific_en"] = trans["organism_scientific_en"]
        p["organism"] = org

    mech_list = p.get("mechanisms", [])
    trans_mech = trans.get("mechanisms", [])
    # Match by idx (stable index) when present; fall back to array position.
    # mechanism_id is frequently None across the corpus, so idx (LLM keeps
    # order) is the reliable key. Handles both int and numeric-string idx.
    for me in trans_mech:
        midx = me.get("idx")
        if isinstance(midx, str) and midx.isdigit():
            midx = int(midx)
        m = None
        if isinstance(midx, int):
            if 0 <= midx < len(mech_list):
                m = mech_list[midx]
        if m is None:
            # fall back to scanning by mechanism_id
            _mid = me.get("mechanism_id")
            for _m in mech_list:
                if _m.get("mechanism_id") and _m.get("mechanism_id") == _mid:
                    m = _m
                    break
        if m is None:
            continue
        if me.get("name_en"):
            m["name_en"] = me["name_en"]
        if me.get("description_en"):
            m["description_en"] = me["description_en"]
        cc = m.get("causal_chain")
        if isinstance(cc, dict) and me.get("transferable_principle_en"):
            cc["transferable_principle_en"] = me["transferable_principle_en"]
            m["causal_chain"] = cc
    return p


def _diff_summary(proto: dict, new: dict) -> list:
    """Return list of short change lines describing the planned additions."""
    lines = []
    org = proto.get("organism", {})
    if isinstance(org, dict) and not org.get("scientific_en") and new.get("organism", {}).get("scientific_en"):
        lines.append(f"  organism.scientific_en = {new['organism']['scientific_en'][:70]}")
    old_mechs = proto.get("mechanisms", [])
    new_mechs = new.get("mechanisms", [])
    # Align by position (corpus mechanism_id is often missing).
    for i in range(max(len(old_mechs), len(new_mechs))):
        om = old_mechs[i] if i < len(old_mechs) else {}
        nm = new_mechs[i] if i < len(new_mechs) else {}
        added = []
        if not om.get("name_en") and nm.get("name_en"):
            added.append("name_en")
        if not om.get("description_en") and nm.get("description_en"):
            added.append("description_en")
        oc = om.get("causal_chain", {})
        nc = nm.get("causal_chain", {})
        if isinstance(oc, dict) and isinstance(nc, dict) and not oc.get("transferable_principle_en") and nc.get("transferable_principle_en"):
            added.append("tp_en")
        if added:
            label = nm.get("mechanism_id") or f"#{i}"
            lines.append(f"  [{label}] +{','.join(added)}")
    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Backfill English fields in BMDL prototypes")
    ap.add_argument("--write", action="store_true", help="Write changes to JSON (default: dry-run)")
    ap.add_argument("--env", default="", help="Path to a .env file supplying DASHSCOPE_API_KEY")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"LLM model (default: {DEFAULT_MODEL})")
    ap.add_argument("--limit", type=int, default=0, help="Process at most N prototypes (for pilot)")
    ap.add_argument("--only", default="", help="Comma-separated prototype ids to process (pilot)")
    ap.add_argument("--chunk-size", type=int, default=0,
                    help="Split large prototypes into chunks of N mechanisms (avoids output truncation)")
    args = ap.parse_args()

    _load_env(args.env)
    client = _make_client()

    files = sorted(PROTO_DIR.glob("*.json"))
    if args.only:
        only = {s.strip() for s in args.only.split(",") if s.strip()}
        files = [f for f in files if f.stem in only]
    if args.limit:
        files = files[:args.limit]

    print(f"== Backfill English fields ({'WRITE' if args.write else 'DRY-RUN'}) ==")
    print(f"   prototypes: {len(files)}, model: {args.model}")

    total_changed = 0
    for fname in files:
        with open(fname, encoding="utf-8") as f:
            proto = json.load(f)
        pid = proto.get("id", fname.stem)
        try:
            trans = _translate_prototype(client, args.model, proto, chunk_size=args.chunk_size)
        except Exception as e:
            print(f"[{pid}] LLM ERROR: {e}", file=sys.stderr)
            continue
        new = _apply_en_fields(proto, trans)
        diff = _diff_summary(proto, new)
        if not diff:
            print(f"[{pid}] no change (already has en fields)")
            continue
        total_changed += 1
        print(f"[{pid}] {len(proto.get('mechanisms', []))} mechanisms:")
        for line in diff:
            print(line)
        if args.write:
            with open(fname, "w", encoding="utf-8") as f:
                json.dump(new, f, ensure_ascii=False, indent=2)
                f.write("\n")

    print(f"\n== Done. {total_changed}/{len(files)} prototypes changed. "
          f"{'WRITTEN to disk' if args.write else 'dry-run only (pass --write to commit)'} ==")


if __name__ == "__main__":
    main()