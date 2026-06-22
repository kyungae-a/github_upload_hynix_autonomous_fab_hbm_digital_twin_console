# P10 — Local Final Transaction, Deterministic Release Candidate, and Clean-Unzip Verification

## Purpose
Run producers and validators in correct order, package a reproducible v5.4 candidate, and verify it from a fresh extraction without pretending local CI evidence exists.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `release-productization-engineer`
- Independent reviewer: `cleanroom-release-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `Makefile`
- `scripts/package_release.py`
- `scripts/verify_clean_unzip.py`
- `validation/validate_release_manifest_v5_4.py`
- `release_manifest.json`
- `release/hynix-autonomous-fab-hbm-digital-twin-console.zip`
- `release/hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json`
- `docs/v5_4_build_state.json`

## Classes and functions to implement
- `clean_generated()`
- `run_local_release_transaction()`
- `freeze_artifacts()`
- `build_internal_manifest()`
- `package_without_regeneration()`
- `verify_clean_unzip(mode)`

## Input data
- validated source
- current-run engine/tool/local dashboard/screenshot/docs artifacts
- optional CI manifest

## Output data and evidence
- deterministic release candidate
- v5.4 internal/sidecar manifests
- clean-unzip receipts
- AWAITING_GITHUB_MEDIUM or READY status based on genuine CI evidence

## Dashboard change
Release captures exactly the validated dashboard and screenshots; packaging cannot regenerate or alter them.

## Implementation tickets
1. Order producers before validators, freeze before manifest, and package without regeneration.
2. Normalize ZIP paths/timestamps and exclude workflow overlays, caches, stale archives, and local absolute paths.
3. Write all required v5.4 manifest booleans from validator receipts, not constants.
4. If trusted CI evidence is absent, finish local gate at `AWAITING_GITHUB_MEDIUM`; do not set final READY.
5. Clean-unzip runs test, local validation, dashboard integrity, screenshot manifest validation, docs validation, and payload hash verification.

## Required tests
- Two packages from identical frozen artifacts have identical SHA-256.
- Manifest hash matches all entries and no self-reference is required.
- No pycache/pyc, traversal, absolute path, or stale release inside archive.
- Local missing CI evidence yields AWAITING_GITHUB_MEDIUM, not failure masking or fake READY.

## Validation commands
```bash
make demo-light
make demo-medium || true
make demo-heavy
make run-canonical
make run-variants
make run-public-tools
make dashboard
make screenshots
make test
make validate
make validate-medium
make package-release
make verify-clean-unzip
```

## Acceptance / Done criteria
- Local release is reproducible and clean-unzip valid.
- All non-CI v5.4 manifest flags are supported by receipts.
- Status truthfully distinguishes local candidate from GitHub-finalized release.

## Forbidden shortcuts
- Packaging before screenshots/docs
- Manifest before last producer
- Package step regenerating evidence
- READY without CI evidence
- Including `.codex` workflow or caches in product release

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
