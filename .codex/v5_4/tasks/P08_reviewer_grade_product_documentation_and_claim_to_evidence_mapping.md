# P08 — Reviewer-Grade Product Documentation and Claim-to-Evidence Mapping

## Purpose
Expand key documents into product manuals that explain implementation, inputs, metric calculations, dashboard mapping, evidence, and claim boundaries.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `product-docs-engineer`
- Independent reviewer: `product-docs-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `README.md`
- `START_HERE_KO.md`
- `docs/05_HBM_WORKLOAD_TWIN.md`
- `docs/07_FAB_OPERATION_TWIN.md`
- `docs/08_FACTORY_SCENE_ROUTING_TWIN.md`
- `docs/09_AI_JUDGMENT_AUDIT_LAYER.md`
- `docs/11_IMPLEMENTATION_EVIDENCE.md`
- `docs/03_HYNIX_ALIGNMENT.md`
- `docs/14_SCREENSHOT_GUIDE.md`
- `validation/validate_product_docs_contract.py`
- `tests/test_docs_references.py`

## Classes and functions to implement
- `collect_doc_evidence_links()`
- `validate_required_headings()`
- `resolve_referenced_paths()`
- `validate_claim_boundary_sections()`

## Input data
- final code structure
- current-run output/evidence paths
- dashboard route mapping
- screenshots and CI evidence contract

## Output data and evidence
- five implementation manuals
- reviewer-first README/START_HERE
- claim-to-artifact tables
- exact run/review path

## Dashboard change
Docs link directly to relevant console routes and evidence files; dashboard Evidence links return to exact docs sections.

## Implementation tickets
1. Implement every required heading from the source directive with substantive body and actual repo paths.
2. Explain algorithms/formulas and data lineage, not just module names.
3. Map each page chart/timeline/map/flow to its dashboard JSON section and producer.
4. Separate local public-tool state from CI evidence in README and implementation evidence.
5. Preserve strong positioning while stating public-model, synthetic-data, no proprietary access, and no real signoff boundaries.

## Required tests
- All required headings exist with nontrivial content.
- Every backticked repo path resolves or is explicitly marked generated-at-run.
- Each key doc contains Dashboard mapping, Evidence files, and Claim boundary.
- README guides reviewer through 7 screenshots and 9 pages.

## Validation commands
```bash
pytest -q tests/test_docs_references.py
python validation/validate_product_docs_contract.py --strict
```

## Acceptance / Done criteria
- Docs can stand alone as product explanations.
- No key doc remains a three-line label.
- Claims map to inspectable evidence and limits.

## Forbidden shortcuts
- One-line section bodies
- Copying the same generic paragraph into all docs
- Broken artifact paths
- Timid toy framing
- Real SK hynix internal equivalence claim

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
