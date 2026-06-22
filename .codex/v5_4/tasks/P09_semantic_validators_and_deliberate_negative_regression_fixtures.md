# P09 — Semantic Validators and Deliberate Negative Regression Fixtures

## Purpose
Replace file-presence validation with behavioral checks that fail for each reproduced v5.4 defect.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `semantic-validation-engineer`
- Independent reviewer: `negative-regression-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `validation/validate_v5_4_acceptance.py`
- `validation/validate_hbm_units.py`
- `validation/validate_factory_scene_graph_contract.py`
- `validation/validate_fab_timeline_contract.py`
- `validation/validate_screenshot_visual_contract.py`
- `validation/validate_product_docs_contract.py`
- `validation/validate_ci_public_tool_evidence.py`
- `validation/validate_console_evidence_explorer.py`
- `validation/negative_fixtures/v5_4/`
- `tests/test_v5_4_negative_fixtures.py`
- `Makefile`

## Classes and functions to implement
- `run_validator_against_fixture(name)`
- `expect_failure_reason(result, code)`
- `validate_v5_4_acceptance(mode)`

## Input data
- good current-run artifact set
- isolated intentionally corrupted copies

## Output data and evidence
- semantic validation report
- negative fixture matrix with expected error codes
- focused Make targets

## Dashboard change
No visual changes; validators inspect the data and DOM/screenshot evidence that drive the product surface.

## Implementation tickets
1. Create fixtures for raw Gbps mislabeled GB/s, wrong /8 conversion, missing unit note, factory graph missing nodes/route/congestion, hard-coded route, blank USDA, one-LOT synthetic Fab timeline, generic screenshot manifest, missing Meta stage, duplicate tool cards, fake local CI URL, stale CI commit, shallow docs, runtime-written READY, cache files, and stale manifest.
2. Each fixture must fail for its intended semantic error code—not because JSON parsing or file lookup failed.
3. Add focused Make targets and include them in `make validate`/`validate-medium` without weakening existing checks.
4. Validate source and artifact freshness/order, not only final files.

## Required tests
- Every negative fixture is detected by exactly the intended validator family.
- Good artifacts pass all focused validators.
- Deleting a required source array while leaving screenshot PNG intact fails.
- Creating fake CI manifest locally fails.
- Legacy v5.3 state cannot satisfy v5.4 acceptance.

## Validation commands
```bash
pytest -q tests/test_v5_4_negative_fixtures.py
python validation/validate_v5_4_acceptance.py --local --strict
make validate
```

## Acceptance / Done criteria
- All five gap categories have positive and negative semantic proof.
- Legacy shallow validators cannot be the only acceptance path.
- Failure messages identify the violated product contract.

## Forbidden shortcuts
- Fixtures that fail only due to malformed syntax
- File-existence-only validators
- Skipping negative tests when tools unavailable
- Editing expected result to match broken implementation

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
