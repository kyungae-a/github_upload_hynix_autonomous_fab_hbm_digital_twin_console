# P00 — Baseline Integrity, In-Place Upgrade Boundary, and Authority Reset

## Purpose
Establish the current v5.3 release as a strong but non-authoritative baseline, reproduce all five v5.4 gaps, and remove runtime/frontend mechanisms that can self-certify READY.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `baseline-auditor`
- Independent reviewer: `baseline-integrity-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `docs/v5_4_build_state.json`
- `docs/current_v5_3_product_gap_audit.md`
- `docs/current_v5_3_baseline_receipts.json`
- `twin_core/scenario_runner.py`
- `frontend/app.js`
- `validation/validate_v5_4_authority_boundary.py`
- `tests/test_v5_4_authority_boundary.py`
- `Makefile`

## Classes and functions to implement
- `collect_baseline_receipts()`
- `remove_runtime_phase_certification()`
- `load_build_status_from_generated_state()`
- `validate_no_product_self_certification()`

## Input data
- attached v5.3 release tree
- v5.3 sidecar manifest
- current Make outputs
- source directive and contract lock

## Output data and evidence
- reproducible baseline audit JSON/Markdown
- v5.4 state initialized at REWORK_REQUIRED/P00
- product runtime free of phase PASS writes
- frontend status derived from state/evidence rather than constant

## Dashboard change
Keep current pages operational, but replace hard-coded READY with explicit `REWORK_REQUIRED`/`IN_PROGRESS` state loaded from generated status data. Never use READY as a missing-data fallback.

## Implementation tickets
1. Recompute archive/entry hashes and run current `make test` and `make validate`; record return codes without converting legacy PASS into v5.4 acceptance.
2. Delete `phase_receipts()` from product execution paths. If historical phase receipts are kept for archive reading, make them read-only legacy data and never regenerate them.
3. Remove all hard-coded `READY_FOR_GITHUB_REVIEW` assignments/fallbacks from frontend and scenario runner.
4. Create a focused authority validator that rejects any engine/runtime module writing `docs/v5_4_build_state.json`, phase PASS receipts, or final READY.
5. Do not create a nested product clone. Apply the workflow in the current repository root.

## Required tests
- Runtime demo does not mutate authoritative v5.4 state.
- Missing build status renders UNKNOWN/REWORK_REQUIRED, never READY.
- Injected `phase_receipts()` call or READY literal in production frontend is rejected.
- Existing light tests remain green.

## Validation commands
```bash
pytest -q tests/test_v5_4_authority_boundary.py
python validation/validate_v5_4_authority_boundary.py --strict
make test
```

## Acceptance / Done criteria
- Five gaps are reproduced with code/evidence paths.
- v5.4 state begins at P00 and legacy READY is explicitly untrusted.
- Product runtime cannot approve its own implementation.

## Forbidden shortcuts
- Editing old PASS JSON to claim completion
- Nested repo copy
- Deleting working evidence instead of refactoring
- Changing public-model/non-signoff boundary

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
