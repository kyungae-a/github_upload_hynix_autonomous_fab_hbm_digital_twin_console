# P06 — Nine-Page Evidence Explorer Integration and Local/CI Evidence Separation

## Purpose
Integrate P02–P05 into a coherent console whose main surfaces are charts, timelines, maps, tables, and decision flows.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `frontend-evidence-engineer`
- Independent reviewer: `frontend-evidence-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `frontend/index.html`
- `frontend/app.js`
- `frontend/styles.css`
- `twin_core/evidence/dashboard_builder.py`
- `scripts/generate_dashboard_data.py`
- `tests/frontend/test_console_pages.mjs`
- `tests/frontend/test_dashboard_data_binding.mjs`
- `validation/validate_console_evidence_explorer.py`

## Classes and functions to implement
- `MetricCard`
- `StatusBadge`
- `LineChart`
- `BarChart`
- `Timeline`
- `RouteMap`
- `EvidenceTable`
- `DecisionFlow`
- `ReceiptPanel`
- `ScenarioSelector`
- `VariantMatrix`
- `renderOverview()`
- `renderHbmPage()`
- `renderCircuitPage()`
- `renderFabPage()`
- `renderFactoryPage()`
- `renderAuditPage()`
- `renderPublicToolsPage()`
- `renderVariantsPage()`
- `renderHynixAlignmentPage()`

## Input data
- validated v5.4 dashboard bundle
- route/query selection
- source evidence links

## Output data and evidence
- nine functional routes
- data-testid visual elements
- evidence drill-down links
- explicit error states

## Dashboard change
Overview shows five layers and chain; HBM uses correct units; Circuit separates execution/design/signoff; Fab uses real traces; Factory uses raw graph; Audit has six stages including Meta; Tools split local/CI; Variants show 60+; Hynix page preserves public-model boundary.

## Implementation tickets
1. Treat JSON inspector as optional evidence drill-down only.
2. Add stable data-testid selectors for every screenshot-required chart/marker/map/flow/panel.
3. Render explicit ERROR panels for missing mandatory data; never invoke sample/fallback model builders in production frontend.
4. Make source artifact links and run IDs visible on each page.
5. Ensure responsive 1440x1000 capture layout without clipping core evidence.

## Required tests
- All nine routes render from one data bundle.
- Required selectors and source links exist.
- Missing domain object renders ERROR, not invented metrics.
- Public tools show exactly four unique tools in each relevant section.
- AI flow order contains Meta Judge.

## Validation commands
```bash
node --test tests/frontend/test_console_pages.mjs tests/frontend/test_dashboard_data_binding.mjs
python validation/validate_console_evidence_explorer.py --strict
make dashboard
```

## Acceptance / Done criteria
- Reviewer can understand product behavior without opening raw JSON.
- All five v5.4 gaps are visibly addressed in the console.
- Page data and evidence paths are current-run linked.

## Forbidden shortcuts
- Card-only final pages
- Main JSON dump
- Blank route map
- Repeated tool records
- Hidden hard-coded READY or metrics

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
