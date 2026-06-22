
# Current v5.2 Product Baseline Audit for the v5.3 Pass

## Baseline integrity

- Attached archive SHA-256: `77c686267f70564585797e29a711162d7c47ae045343cc5f9ba6f3f071846e51`
- Attached sidecar manifest SHA-256: `4c2982fc0388f854ee2d59bce27fb10691cd3e8b8d6870a7b2668430cc6b463c`
- v5.3 implementation specification SHA-256: `28380c8d45aa8da6ff70f3230a94098c8ec806724e0269f6d92ddb041d4f9617`
- Existing `make test`: PASS during audit
- Existing `make validate`: PASS during audit

The current release is a useful and coherent baseline: it already has the product name, public-model boundary, core repository shape, four technical areas, AI audit artifacts, tests, validators, Docker/devcontainer, CI files, outputs, and release metadata. The v5.3 pass preserves those strengths.

## Why an in-place product pass is required

The v5.3 specification changes the acceptance center from “files and evidence exist” to “a reviewer can operate and inspect a real console.” Source inspection found the following concrete implementation boundaries:

1. `frontend/index.html` currently presents the dashboard bundle as preformatted JSON rather than nine product pages.
2. `scripts/generate_screenshots.py` synthesizes text-card images; it does not capture the browser console.
3. The HBM engine is an aggregate formula path rather than a workload/request/scheduler trace.
4. The Fab engine is a shallow event loop rather than the specified SimPy entity/resource model.
5. Factory routing contains fixed selection logic and the `.usda` output is not yet a meaningful scene graph.
6. Red-team caught/escaped behavior is directly tied to scenario family.
7. Product runtime emits phase PASS receipts, mixing implementation evidence with orchestration state.
8. The variant generator produces 60 entries but lacks the required semantic mutation contract.

These are not reasons to lower the portfolio position. They identify exactly where implementation behavior must catch up with the strong product framing.

## Upgrade rule

- Modify the current product repository in place.
- Do not create a second nested product root.
- Keep working engines/docs/tests that survive behavior review.
- Replace shallow or synthetic implementations with the P00–P19 contracts.
- Do not trust legacy READY/PASS state for v5.3.
