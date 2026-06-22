# P02 — HBM Bandwidth Unit Normalization and Policy-Comparison Product Page

## Purpose
Correct the raw bit-rate/display byte-rate contract and turn the HBM page into a trustworthy policy comparison view.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `hbm-unit-product-engineer`
- Independent reviewer: `hbm-unit-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `twin_core/memory_system/metrics.py`
- `twin_core/memory_system/hbm_workload_engine.py`
- `twin_core/memory_system/policy_compare.py`
- `twin_core/memory_system/run_hbm_twin.py`
- `frontend/app.js`
- `frontend/styles.css`
- `tests/test_hbm_units.py`
- `tests/test_hbm_policy_dashboard.py`
- `validation/validate_hbm_units.py`
- `docs/05_HBM_WORKLOAD_TWIN.md`

## Classes and functions to implement
- `gbps_to_GBps(value_gbps: float) -> float`
- `build_bandwidth_metrics(raw_gbps: dict) -> dict`
- `PolicyComparisonRow`
- `simulate_policy(workload, policy, seed)`
- `compare_policies(workload, policies)`
- `select_recommended_policy(rows, hard_constraints)`
- `renderHbmPage(model)`

## Input data
- engine-computed theoretical/effective/sustained bandwidth in Gbps
- workload ID
- policy parameters
- p99 latency/conflict/refresh/thermal arrays

## Output data and evidence
- raw_metrics with `_gbps` keys
- display_metrics with `_GBps` keys
- unit_notes
- six-policy comparison rows
- recommendation and reason trace

## Dashboard change
Render workload selector, policy table, grouped effective/sustained GB/s bars, p99 latency chart, thermal pressure, refresh overhead, bank/bank-group conflict, recommendation badge, and `GB/s = Gbps / 8` note. GB/s labels bind only to `_GBps` paths.

## Implementation tickets
1. Use current canonical `twin_core/memory_system` path; do not create a second divergent HBM engine tree. Add a compatibility import only if an existing public API requires it.
2. Compute byte-rate fields once in Python and include derivation/source paths; do not divide ad hoc in multiple frontend components.
3. Generate policy rows from engine runs, not proportional scaling. At minimum compare FCFS, FR_FCFS, WRITE_DRAIN, THERMAL_SAFE, REFRESH_AWARE, and BALANCED.
4. Recommendation must obey hard constraints before score ranking.
5. Search all docs/frontend/screenshots for raw `_gbps` fields labeled GB/s and eliminate them.

## Required tests
- Each `_GBps` value equals corresponding `_gbps / 8` within tolerance.
- Negative, NaN, or nonnumeric rates are rejected.
- Frontend source does not bind a GB/s label to `_gbps` key.
- Policy perturbation changes computed bandwidth/latency/thermal metrics.
- Screenshot source manifest includes unit note selector and display metric paths.

## Validation commands
```bash
pytest -q tests/test_hbm_units.py tests/test_hbm_policy_dashboard.py
python -m twin_core.memory_system.run_hbm_twin --all-workloads --all-policies --seed 42
python validation/validate_hbm_units.py --strict
make dashboard
```

## Acceptance / Done criteria
- Raw and display units are unambiguous end to end.
- The HBM page is a policy-comparison product view, not two metric cards.
- No raw Gbps value is presented as GB/s.

## Forbidden shortcuts
- Renaming raw fields without conversion
- Dividing only in screenshot code
- Hard-coded policy chart values
- Unit note hidden in documentation only

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
