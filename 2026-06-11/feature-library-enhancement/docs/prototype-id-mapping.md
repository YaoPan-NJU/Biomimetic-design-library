# Prototype ID Mapping Table

> Generated: 2026-06-05
> Purpose: Reconcile the 33 canonical prototype IDs (from `feature-mapping.json#prototype_metadata`)
>          with the 30 pipeline-generated IDs (directories containing `prototype.md`).
> Reference: docs/superpowers/specs/2026-06-05-library-enhancement-design.md Section 4.3

---

## Summary Statistics

| Category | Count | Description |
|----------|-------|-------------|
| Exact match | 12 | Pipeline ID identical to canonical ID |
| Merge | 11 | Pipeline ID is a variant; merge content into canonical directory |
| Keep-both | 2 | Both IDs represent genuinely different concepts |
| New-prototype | 5 | Pipeline generated a new prototype with no canonical counterpart |
| No-pipeline-match | 7 | Canonical prototype has no corresponding pipeline output |

**Total canonical IDs:** 33
**Total pipeline IDs:** 30

---

## Complete Mapping Table

### 1. Exact Matches (12)

These pipeline IDs are identical to the canonical IDs. No action needed beyond keeping the existing `prototype.md` content.

| # | Canonical ID | Pipeline ID | Action | Notes |
|---|-------------|-------------|--------|-------|
| 1 | lotus-leaf | lotus-leaf | exact-match | Both dirs have .gitkeep + prototype.md |
| 2 | mussel-foot-adhesion | mussel-foot-adhesion | exact-match | Both dirs have .gitkeep + prototype.md |
| 3 | iron-oxidizing-bacteria | iron-oxidizing-bacteria | exact-match | Both dirs have .gitkeep + prototype.md |
| 4 | mycelium | mycelium | exact-match | Both dirs have .gitkeep + prototype.md |
| 5 | namib-beetle | namib-beetle | exact-match | Both dirs have .gitkeep + prototype.md |
| 6 | oyster-shell | oyster-shell | exact-match | Both dirs have .gitkeep + prototype.md |
| 7 | polydopamine-coating | polydopamine-coating | exact-match | Both dirs have .gitkeep + prototype.md |
| 8 | scallop-shell | scallop-shell | exact-match | Both dirs have .gitkeep + prototype.md |
| 9 | shark-skin | shark-skin | exact-match | Both dirs have .gitkeep + prototype.md |
| 10 | spider-silk | spider-silk | exact-match | Both dirs have .gitkeep + prototype.md |
| 11 | sulfate-reducing-bacteria | sulfate-reducing-bacteria | exact-match | Both dirs have .gitkeep + prototype.md |
| 12 | magnetic-bacteria | magnetic-bacteria | exact-match | Both dirs have .gitkeep + prototype.md |

### 2. Merge into Canonical (11)

Pipeline generated a longer, application-specific variant ID. Content should be merged into the canonical (shorter, more general) directory. The pipeline-only directory should be removed after merge.

| # | Canonical ID (keep) | Pipeline ID (merge from) | Action | Rationale |
|---|---------------------|-------------------------|--------|-----------|
| 1 | chitosan | chitosan-adsorbent | merge | "chitosan" is more general; allows future expansion beyond adsorption |
| 2 | alginate | alginate-adsorbent | merge | "alginate" is more general; same reasoning as chitosan |
| 3 | cellulose-nanocrystal | cellulose-adsorbent | merge | "cellulose-nanocrystal" is more precise (specifies the form); pipeline used generic "cellulose-adsorbent" |
| 4 | metal-organic-framework | mof-adsorbent | merge | "metal-organic-framework" is the full canonical name; "mof-adsorbent" is abbreviation + application suffix |
| 5 | starch-granule | starch-adsorbent | merge | "starch-granule" describes the structural form; "starch-adsorbent" is application-specific |
| 6 | silk-fibroin | silkworm-silk | merge | "silk-fibroin" names the specific protein; "silkworm-silk" names the source organism + material |
| 7 | water-strider-leg | water-strider | merge | "water-strider-leg" is more specific (identifies the functional organ); pipeline dropped "-leg" |
| 8 | superhydrophobic-artificial | superhydrophobic-surface | merge | "superhydrophobic-artificial" is canonical; "superhydrophobic-surface" is a synonym |
| 9 | pitcher-plant-slippery-surface | slips-surface | merge | "pitcher-plant-slippery-surface" identifies the biological origin; "slips-surface" is abbreviation only |
| 10 | mangrove-root | mangrove | merge | "mangrove-root" identifies the functional organ; "mangrove" is the organism only |
| 11 | wood-xylem | wood-structure | merge | "wood-xylem" is anatomically precise; "wood-structure" is vague |

### 3. Keep Both (2)

Both the canonical and pipeline IDs represent genuinely different concepts and should coexist as separate prototypes.

| # | Canonical ID | Pipeline ID | Action | Rationale |
|---|-------------|-------------|--------|-----------|
| 1 | diatom-frustule | diatom-microspheres | keep-both | "diatom-frustule" = natural silica shell structure; "diatom-microspheres" = synthetic microspheres mimicking diatom morphology. Different biomimetic levels. |
| 2 | fish-scale-hydroxyapatite | hydroxyapatite-adsorbent | keep-both | "fish-scale-hydroxyapatite" = fish-scale-derived HAP with hierarchical pores; "hydroxyapatite-adsorbent" = general HAP adsorbent regardless of source. Different scope. |

**Note on diatom-microspheres:** This pipeline ID also has partial overlap with `diatom-inspired-porous` (canonical). However, `diatom-inspired-porous` focuses on the porous structure concept, while `diatom-microspheres` focuses on the spherical form factor. All three can coexist:
- `diatom-frustule` -- the natural biological structure
- `diatom-inspired-porous` -- bio-inspired porous design concept
- `diatom-microspheres` -- synthetic microsphere implementation

### 4. New Prototypes from Pipeline (5)

Pipeline generated prototypes that have no corresponding canonical directory. These are genuine new additions to the library. A new canonical directory (with .gitkeep) should be created for each after content review.

| # | Pipeline ID | Action | Description | Feature-mapping coverage |
|---|------------|--------|-------------|--------------------------|
| 1 | biochar-adsorbent | new-prototype | Biochar-based adsorbent materials | Not in current feature-mapping.json; requires new entry |
| 2 | biomineralization-template | new-prototype | Biomineralization template mechanisms | Not in current feature-mapping.json; overlaps with existing "biomineralization template" feature |
| 3 | dna-aptamer | new-prototype | DNA aptamer-based selective binding | Not in current feature-mapping.json; fits Phase 2 expansion (bio-inspired synthetic) |
| 4 | molecularly-imprinted-polymer | new-prototype | Molecularly imprinted polymers for selective adsorption | Not in current feature-mapping.json; fits Phase 2 expansion (bio-inspired synthetic) |
| 5 | chlorella | new-prototype | Whole chlorella cells as adsorbent | Partially overlaps with canonical `chlorella-cell-wall`; see special note below |

**Special note on `chlorella` vs `chlorella-cell-wall`:** The pipeline generated `chlorella` (whole cell) while the canonical ID is `chlorella-cell-wall` (specific cell wall component). These may warrant keep-both treatment since whole-cell adsorption and cell-wall-only adsorption have different mechanisms and application conditions. Pending content review to make final determination.

### 5. No Pipeline Match (7)

Canonical prototypes that have no corresponding pipeline-generated content. These require manual content creation or future pipeline runs.

| # | Canonical ID | Action | Notes |
|---|-------------|--------|-------|
| 1 | bone-structure | no-pipeline-match | Hierarchical pore structure + ion exchange; referenced in feature-mapping for Cd, F, Sr |
| 2 | cactus-spine | no-pipeline-match | Gradient wetting on conical spines; referenced in feature-mapping for oil, self-cleaning |
| 3 | cell-membrane-ion-channel | no-pipeline-match | Molecular sieving; referenced in feature-mapping for selectivity |
| 4 | coral-skeleton | no-pipeline-match | Macroporous structure + biomineralization template |
| 5 | diatom-inspired-porous | no-pipeline-match | Bio-inspired mesoporous design concept |
| 6 | lobster-exoskeleton | no-pipeline-match | Fibrous/chitin structure |
| 7 | plant-tannin | no-pipeline-match | Catechol + pi-electron system; referenced for Hg, aromatic compounds |

---

## Action Summary

### Immediate Actions (Phase 0)

1. **For exact-match entries (12):** Keep existing directories as-is. No migration needed.

2. **For merge entries (11):**
   - Copy `prototype.md` content from pipeline directory into canonical directory
   - If canonical directory already has content, merge (not overwrite)
   - Delete pipeline-only directory after merge
   - Remove the pipeline ID from any future references

3. **For keep-both entries (2):**
   - Create new canonical directory for `diatom-microspheres` (with .gitkeep + move prototype.md)
   - Create new canonical directory for `hydroxyapatite-adsorbent` (with .gitkeep + move prototype.md)
   - Update `feature-mapping.json` to include new entries

4. **For new-prototype entries (5):**
   - Review content quality of each pipeline prototype.md
   - Create canonical directories for accepted prototypes
   - Add accepted prototypes to `feature-mapping.json`
   - Tag with appropriate features and biomimetic dimensions

5. **For no-pipeline-match entries (7):**
   - Queue for manual content creation or next pipeline run
   - Prioritize by feature-mapping reference frequency

### Post-Merge Cleanup

After all merges, the `prototypes/` directory should contain:
- 33 original canonical directories
- 2 new keep-both directories (`diatom-microspheres`, `hydroxyapatite-adsorbent`)
- 5 new-prototype directories (pending review: `biochar-adsorbent`, `biomineralization-template`, `dna-aptamer`, `molecularly-imprinted-polymer`, `chlorella`)
- Total: 33-40 directories, each with .gitkeep and prototype.md

---

## Naming Convention Rules (for future reference)

Per spec Section 4.3:

1. **Prefer shorter, more general IDs** -- e.g., `chitosan` over `chitosan-adsorbent`. This allows expansion beyond adsorption applications.
2. **Use anatomically precise terms when the organ/structure is the key** -- e.g., `water-strider-leg` (not `water-strider`), `mangrove-root` (not `mangrove`).
3. **Use full scientific names over abbreviations** -- e.g., `metal-organic-framework` (not `mof`).
4. **Biological source + functional component** format where applicable -- e.g., `fish-scale-hydroxyapatite`, `cellulose-nanocrystal`.
5. **No application suffix** unless the prototype is inherently application-specific -- avoid `-adsorbent`, `-filter`, etc.
