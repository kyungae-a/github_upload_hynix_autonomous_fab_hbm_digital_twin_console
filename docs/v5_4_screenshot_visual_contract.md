# v5.4 Screenshot Visual Contract

All seven images are Playwright/Chromium captures of actual routes loaded from the final dashboard bundle. The renderer records route, query parameters, viewport, browser version, dashboard SHA-256, PNG SHA-256, source sections, required selectors, selector counts, visible text values, and bounding boxes.

## Required images

1. `01_architecture.png`: five core layers and evidence-chain arrows.
2. `02_fab_qtime_timeline.png`: LOT_A and LOT_B curves, Q-over threshold, dispatch and metrology markers, event mini-log, tool/chamber labels.
3. `03_hbm_workload_policy_compare.png`: policy x-axis, effective and sustained GB/s bars, p99 panel, thermal indicator, recommendation, unit note.
4. `04_factory_scene_routing.png`: coordinate plane, five labeled nodes and edges, selected path, congestion zone, route cost and delay.
5. `05_public_tool_evidence.png`: four tools, separate local and CI panels, unavailable explanation, no-signoff boundary.
6. `06_ai_judgment_audit_flow.png`: six stages including Meta Judge, caught/escaped status, approved/blocked claim, signoff requirement.
7. `07_hynix_alignment.png`: Autonomous Fab, Digital Twin, HBM workload, Q-time/LOT priority, AI audit, public-model boundary.

A screenshot fails when required data-testid selectors are absent, source arrays are empty, visible values do not match the dashboard JSON, the image is a generic card/JSON dump, or manifest provenance is stale.
