#!/usr/bin/env python3
"""
Canon recovery library (M1): stable record identity + ambiguity gate + ledger writer.

Identity is matched per PROJECT-RECOVERY-DESIGN §6.2 — NEVER by array index.
Zero or multiple plausible matches => ambiguous; the caller escalates, never guesses.

Performance identity priority:
  perf_1: prototype + normalized source-id (doi/patent/standard) + normalized param + value + material
  perf_2: source basename + param + value + material
  perf_3: normalized fingerprint excluding mutable evidence fields

Mechanism identity priority:
  mech_1: prototype + normalized doi + normalized name + description fingerprint
  mech_2: source basename + normalized name
  mech_3: normalized name + description fingerprint
"""
import json
import os
import re
import hashlib
import datetime
import threading

LEDGER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "registries", "canon-recovery-ledger.jsonl",
)
_ledger_lock = threading.Lock()

MUTABLE_EVIDENCE_FIELDS = {
    "verification", "verification_quote", "source_locator", "locator", "page",
    "confidence", "basis",
}


def _norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def _norm_value(s):
    """Normalize a numeric value: strip units/space, keep the number core."""
    s = _norm(s)
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    return m.group(0) if m else s


def _source_id(row):
    return _norm(row.get("ref_doi") or row.get("patent_number") or row.get("standard_number") or row.get("source") or "")


def _basename(path):
    return os.path.basename(str(path or "")).strip().lower()


# ---------------------------------------------------------------- performance identity

def perf_fingerprint(row, include_mutable=False):
    base = {
        "parameter": _norm(row.get("parameter")),
        "value": _norm_value(row.get("value")),
        "material": _norm(row.get("material")),
        "unit": _norm(row.get("unit")),
        "source_id": _source_id(row),
        "source_basename": _basename(row.get("source_file")),
    }
    if include_mutable:
        base["verification"] = _norm(row.get("verification"))
    key = "|".join(f"{k}={base[k]}" for k in sorted(base))
    return base, hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def match_perf(prototype_id, candidate, canon):
    """Return list of plausible canon performance rows matching `candidate`.
    Caller treats len==0 => no match, len>1 => AMBIGUOUS (escalate), len==1 => match."""
    cf, _ = perf_fingerprint(candidate)
    rows = [p for p in canon.get("performance_data", []) if isinstance(p, dict)]
    hits = []
    for r in rows:
        rf, _ = perf_fingerprint(r)
        # perf_1: full identity
        if (cf["parameter"] == rf["parameter"] and cf["value"] == rf["value"]
                and cf["material"] == rf["material"] and cf["source_id"] == rf["source_id"]
                and cf["source_id"]):
            hits.append(r); continue
        # perf_2: source basename + param + value + material
        if (cf["source_basename"] and cf["source_basename"] == rf["source_basename"]
                and cf["parameter"] == rf["parameter"] and cf["value"] == rf["value"]
                and cf["material"] == rf["material"]):
            hits.append(r); continue
        # perf_3: fingerprint excluding mutable evidence fields (already excludes them)
        if (cf["parameter"] == rf["parameter"] and cf["value"] == rf["value"]
                and cf["material"] == rf["material"] and cf["unit"] == rf["unit"]):
            hits.append(r); continue
    # de-dup identical object identity (same dict referenced once)
    seen = set(); uniq = []
    for h in hits:
        i = id(h)
        if i not in seen:
            seen.add(i); uniq.append(h)
    return uniq


# ---------------------------------------------------------------- mechanism identity

def mech_fingerprint(row):
    base = {
        "name": _norm(row.get("name")),
        "desc": _norm((row.get("description") or "")[:160]),
        "source_id": _source_id(row),
        "source_basename": _basename(row.get("source_file")),
    }
    key = "|".join(f"{k}={base[k]}" for k in sorted(base))
    return base, hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def match_mech(prototype_id, candidate, canon):
    mechs = canon.get("mechanisms", [])
    if isinstance(mechs, dict):
        mechs = list(mechs.values())
    mechs = [m for m in mechs if isinstance(m, dict)]
    cf, _ = mech_fingerprint(candidate)
    hits = []
    for m in mechs:
        mf, _ = mech_fingerprint(m)
        if (cf["name"] == mf["name"] and cf["source_id"] == mf["source_id"] and cf["source_id"]):
            hits.append(m); continue
        if (cf["source_basename"] and cf["source_basename"] == mf["source_basename"]
                and cf["name"] == mf["name"] and cf["name"]):
            hits.append(m); continue
        if cf["name"] and cf["name"] == mf["name"] and cf["desc"] == mf["desc"] and cf["desc"]:
            hits.append(m); continue
    seen = set(); uniq = []
    for h in hits:
        i = id(h)
        if i not in seen:
            seen.add(i); uniq.append(h)
    return uniq


# ---------------------------------------------------------------- ambiguity gate

class Ambiguity:
    """Wraps a match result to express zero/multiple => ambiguous (never guess)."""
    def __init__(self, canon, candidate, matches):
        self.canon = canon
        self.candidate = candidate
        self.matches = matches

    @property
    def is_ambiguous(self):
        return len(self.matches) != 1

    @property
    def status(self):
        n = len(self.matches)
        return "zero" if n == 0 else ("multiple" if n > 1 else "unique")

    def unique(self):
        """Return the single match, or None if ambiguous/none. Caller must check is_ambiguous first."""
        return self.matches[0] if len(self.matches) == 1 else None


# ---------------------------------------------------------------- verification upgrade gate

class UpgradeDecision:
    ALLOW_PARTIAL = "allow_partial"
    ALLOW_VERIFIED = "allow_verified"
    BLOCK = "block"


def can_upgrade_verification(current, candidate_source_identity, keyword_overlap,
                             quote, locator, scope_match, n_independent_sources=1):
    """13dfdbf guard: DOI equality + keyword overlap identify a CANDIDATE, not evidence.
    Upgrade requires claim-supporting evidence: quote + locator + scope match.
    `corroborated` needs >=2 independent sources."""
    # never downgrade a refuted / never resurrect removed rows (caller guards refuted separately)
    if current in ("refuted",):
        return UpgradeDecision.BLOCK
    if not scope_match:
        return UpgradeDecision.BLOCK
    if not quote or not locator:
        return UpgradeDecision.BLOCK
    if n_independent_sources >= 2:
        return UpgradeDecision.ALLOW_VERIFIED
    return UpgradeDecision.ALLOW_PARTIAL


# ---------------------------------------------------------------- field-merge precedence

def merge_field(current_value, incoming_value, incoming_basis, current_basis):
    """Field precedence (design §6.3): empty never overwrites non-empty; later partial
    does not override earlier accepted unless incoming carries claim-supporting evidence.
    Returns (value, changed)."""
    cur_truthy = bool(current_value)
    inc_truthy = bool(incoming_value)
    if not inc_truthy:
        return current_value, False
    if not cur_truthy:
        return incoming_value, True
    # both non-empty: incoming wins only if it is from_source/direct and current is weaker
    if incoming_basis == "from_source" and current_basis not in ("from_source", "review", "openclaw_candidate"):
        return incoming_value, True
    if incoming_basis == "review" and current_basis not in ("from_source", "review", "openclaw_candidate"):
        return incoming_value, True
    return current_value, False


# ---------------------------------------------------------------- ledger writer

_refuted_index = None


def _refuted_rows(refuted_path):
    """Parse docs/registries/refuted-log.md into a set of source tokens (DOIs / identifiers)."""
    global _refuted_index
    if _refuted_index is not None:
        return _refuted_index
    keys = set()
    if refuted_path and os.path.exists(refuted_path):
        for line in open(refuted_path, encoding="utf-8"):
            if "wrong_source" not in line:
                continue
            for tok in re.findall(r"\| ([^|]+?) \|", line):
                tok = tok.strip()
                if tok:
                    keys.add(tok)
    _refuted_index = keys
    return keys


def would_resurrect_refuted(entry, refuted_path):
    """True if an entry would RESTORE data whose source token appears in the refuted log."""
    if entry.get("disposition") != "restored":
        return False
    tokens = [entry.get("local_file") or ""]
    ident = entry.get("record_identity", {})
    if isinstance(ident, dict):
        tokens.append(ident.get("key", ""))
    tokens.append(entry.get("quote") or "")
    refuted = _refuted_rows(refuted_path)
    return any(str(t).strip() in refuted for t in tokens if str(t).strip())


def write_ledger_entry(entry, ledger_path=None):
    """Append one recovery-ledger entry (JSONL), conforming to canon-recovery-ledger.schema.json.
    Refuses to write an entry that would resurrect a refuted row."""
    ledger_path = ledger_path or LEDGER_PATH
    required = {"id", "prototype_id", "field_path", "record_identity", "disposition", "basis", "applied_commit"}
    missing = required - set(entry.keys())
    if missing:
        raise ValueError(f"ledger entry missing required fields: {missing}")
    refuted_path = os.path.join(os.path.dirname(ledger_path), "refuted-log.md")
    if would_resurrect_refuted(entry, refuted_path):
        raise ValueError(f"entry would resurrect a refuted row: {entry['prototype_id']} {entry['field_path']}")
    os.makedirs(os.path.dirname(ledger_path), exist_ok=True)
    with _ledger_lock:
        with open(ledger_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return ledger_path
