# Archive: Legacy Branch Snapshots (2026-06-11)

This branch contains point-in-time snapshots of all historical branches from the Biomimetic Design Library, captured on 2026-06-11 before branch cleanup.

## Directory Structure

Each subdirectory corresponds to a former branch:

| Directory | Original Branch | SHA | Description |
|-----------|----------------|-----|-------------|
| `main/` | `main` | `3fa831a` | Original main branch (basic scaffolding) |
| `feature-extraction-results/` | `feature/extraction-results` | `cbb7c59` | Data ingestion + ADRMATS integration (now → `adsorption/dev`) |
| `feature-library-enhancement/` | `feature/library-enhancement` | `53c7f4a` | Design rules + extraction toolchain (now merged into `adsorption/dev`) |
| `feature-biomimetic-story-v2/` | `feature/biomimetic-story-v2` | `d9627ac` | Extraction pipeline design (Phase 1-4) |
| `project-tracking/` | `project/tracking` | `d9627ac` | Project tracking mirror |
| `remediation-2026-06-10/` | `remediation/2026-06-10` | `a9a2db9` | Data remediation session |
| `release-v1.0/` | `release/v1.0` | `acdae26` | Release v1.0 snapshot |
| `release-v1.1/` | `release/v1.1` | `9dcb3a0` | Release v1.1 snapshot (pre-second-wave) |
| `wastewater-treatment-universal/` | `wastewater-treatment-universal` | `9356d57` | Universal water treatment design (now → `universal/main`) |

## Active Branches (as of 2026-06-11)

- **`adsorption/dev`** — Biomimetic adsorbent design library main development branch
- **`universal/main`** — General water treatment biomimetic library main branch
- **`main`** — GitHub default branch (to be updated after `adsorption/dev` stabilizes)
- **`feature/extraction-results`** — Temporary retention (pending confirmation before deletion)

## Notes

- These snapshots preserve the exact file trees at the time of archiving
- Git commit history is NOT preserved in this archive branch (it uses orphan commits)
- To restore a branch: `git checkout <sha-from-above>` or create a new branch from the corresponding commit
