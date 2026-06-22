# P04 — Fab Q-Time Timeline Fidelity, Dual-LOT Trajectories, and Event Markers

## Purpose
Make the Fab screenshot and page reflect actual current-run event simulation rather than JavaScript-generated lines and fallback events.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `fab-timeline-product-engineer`
- Independent reviewer: `fab-timeline-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `twin_core/fab_operation/discrete_event_engine.py`
- `twin_core/fab_operation/timeline_builder.py`
- `twin_core/fab_operation/run_fab_twin.py`
- `twin_core/evidence/dashboard_builder.py`
- `frontend/app.js`
- `frontend/styles.css`
- `tests/test_fab_qtime_timeline.py`
- `tests/test_fab_dashboard_no_fallback.py`
- `validation/validate_fab_timeline_contract.py`
- `docs/07_FAB_OPERATION_TWIN.md`

## Classes and functions to implement
- `LotTrajectoryPoint`
- `FabTimelineMarker`
- `build_lot_qtime_trajectories(events, rules)`
- `build_dispatch_markers(events)`
- `build_metrology_delay_markers(events)`
- `build_event_mini_log(events, limit)`
- `renderFabPage(model)`

## Input data
- actual Fab engine event log
- LOT IDs
- QTimeRule thresholds
- dispatch decisions
- tool/chamber allocation
- metrology sample/result times

## Output data and evidence
- LOT_A/LOT_B q-time arrays
- Q-over threshold
- dispatch markers
- metrology delay markers
- event log
- tool/chamber labels
- source hashes

## Dashboard change
Render two distinguishable Q-time curves, threshold, event markers, event/Gantt mini-log, queue/tool/chamber context, metrology lag, and dispatch rationale from the generated bundle.

## Implementation tickets
1. Remove `fallbackEvents`, `Array.from` event fabrication, and synthetic point generation from frontend production code.
2. Build trajectories from event timestamps and q-time rules in Python; preserve raw event IDs in points/markers.
3. Require two canonical lots with different priorities/paths for screenshot scenario S03.
4. Expose timeline data through the normalized dashboard contract with provenance.
5. Keep deterministic seed while preserving event sensitivity to dispatch/metrology mutations.

## Required tests
- LOT_A and LOT_B each have at least five monotonic time points.
- At least one dispatch marker and one metrology-delay marker references a real event ID.
- Q-over threshold line matches the QTimeRule.
- Changing dispatch priority or metrology delay changes trajectories.
- Frontend contains no production fallback event arrays.

## Validation commands
```bash
pytest -q tests/test_fab_qtime_timeline.py tests/test_fab_dashboard_no_fallback.py
python -m twin_core.fab_operation.run_fab_twin --scenario S03 --seed 42
python validation/validate_fab_timeline_contract.py --strict
make dashboard
```

## Acceptance / Done criteria
- Fab page and screenshot are trace-backed.
- Both LOTs, threshold, dispatch, metrology, and tool/chamber context are visible.
- No synthetic frontend evidence remains.

## Forbidden shortcuts
- Generated JavaScript timeline
- One-curve screenshot
- Markers without event IDs
- Static image unrelated to current run

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
