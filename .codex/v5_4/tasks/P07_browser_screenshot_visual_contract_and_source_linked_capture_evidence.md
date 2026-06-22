# P07 — Browser Screenshot Visual Contract and Source-Linked Capture Evidence

## Purpose
Produce seven submission-grade captures from the actual console and prove their required visual semantics against dashboard data.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `screenshot-contract-engineer`
- Independent reviewer: `screenshot-contract-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `scripts/render_dashboard_screenshots.py`
- `scripts/inspect_screenshot_dom.py`
- `screenshots/01_architecture.png`
- `screenshots/02_fab_qtime_timeline.png`
- `screenshots/03_hbm_workload_policy_compare.png`
- `screenshots/04_factory_scene_routing.png`
- `screenshots/05_public_tool_evidence.png`
- `screenshots/06_ai_judgment_audit_flow.png`
- `screenshots/07_hynix_alignment.png`
- `screenshots/screenshot_manifest.json`
- `validation/validate_screenshot_visual_contract.py`
- `tests/test_screenshot_manifest.py`
- `docs/14_SCREENSHOT_GUIDE.md`

## Classes and functions to implement
- `ScreenshotSpec`
- `start_dashboard_server()`
- `capture_route(page, spec)`
- `collect_dom_evidence(page, selectors)`
- `hash_dashboard_bundle()`
- `write_screenshot_manifest(records)`
- `validate_visual_record(record, dashboard)`

## Input data
- served frontend
- validated dashboard data
- per-image route/query/selector contract

## Output data and evidence
- seven PNGs
- per-image browser/DOM sidecars
- source-linked screenshot manifest
- capture log

## Dashboard change
P07 does not add synthetic visuals. It captures P06 routes and fails if required selectors/series/map nodes are missing or clipped.

## Implementation tickets
1. Use Playwright/Chromium browser capture, not Pillow/pixel-font composition.
2. Capture only after page readiness marker and all required selector counts are satisfied.
3. Record visible text/numeric values and compare them with dashboard source fields.
4. Record selector bounding boxes to prove evidence is on-screen, not hidden/off-canvas.
5. Reject generic manifest labels reused for every screenshot.

## Required tests
- Architecture has five named layers and arrows.
- Fab image has two SVG/canvas series plus threshold and two marker classes.
- HBM image uses `_GBps` values and visible conversion note.
- Factory image has ≥5 nodes, ≥5 edges, selected-route and congestion selectors.
- Public tools has Local and CI headings plus four tools.
- Audit image has six ordered stages including Meta Judge.
- PNG and dashboard hashes match manifest.

## Validation commands
```bash
pytest -q tests/test_screenshot_manifest.py
make dashboard
make screenshots
python validation/validate_screenshot_visual_contract.py --strict
```

## Acceptance / Done criteria
- Seven captures are actual product pages with required visual evidence.
- Manifest proves exact data source and DOM presence.
- No placeholder/card/JSON-dump image passes.

## Forbidden shortcuts
- Static image generation disconnected from browser UI
- Screenshots before dashboard freeze
- Low-information size-only validation
- Generic repeated screenshot metadata

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
