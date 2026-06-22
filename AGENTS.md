# AGENTS.md — Hynix v5.4 Final Productization

## Governing documents

Read `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, `docs/reference/hynix_v5_4_final_productization_directive.md`, `config/v5_4_contract_lock.json`, `docs/current_v5_3_product_gap_audit.md`, and the current phase ticket before editing.

## Work boundary

Upgrade the current product in place. Preserve working v5.3 behavior unless the current ticket replaces it. Do not create a nested product tree, lower positioning, or turn the repository into a workflow wrapper.

## Evidence rules

- Implement behavior before validators.
- Never fabricate tool execution, GitHub run identity, screenshots, route data, timelines, or metrics.
- Product runtime cannot approve phases or write final state.
- Writer cannot approve its own phase.
- P0/P1 findings block progression.
- Every generated artifact used for a claim needs path, SHA-256, producer/run ID, and validator.
- Keep public-model/no-real-signoff boundaries explicit.

## Shared-file ownership

Parent orchestrator owns `Makefile`, shared schemas, authoritative state, final dashboard schema, and release manifests. Isolated phase writers request shared-contract changes through handoff rather than racing edits.

## Completion

Local work may stop only at `AWAITING_GITHUB_MEDIUM` when all local gates pass but genuine CI evidence is absent. Final `READY_FOR_GITHUB_REVIEW` requires P11 and all final gates/reviewers.
