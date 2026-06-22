# P11 — Genuine GitHub Medium Evidence Finalization and Independent Product Red Team

## Purpose
Use an actual GitHub Actions medium run to attach real public-tool evidence, rebuild the evidence surfaces, and perform final independent visual/semantic/reproducibility review.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `github-medium-finalizer`
- Independent reviewer: `final-product-redteam`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `.github/workflows/medium.yml`
- `outputs/public_tool_evidence/ci_run_manifest.json`
- `outputs/public_tool_runs/`
- `frontend/dashboard_data.json`
- `screenshots/`
- `release/`
- `docs/v5_4_build_state.json`
- `docs/v5_4_final_acceptance.md`

## Classes and functions to implement
- `finalize_from_github_medium_run()`
- `verify_ci_identity_against_repository()`
- `rerun_final_redteam()`
- `mark_ready_after_all_evidence()`

## Input data
- actual GitHub medium workflow environment
- four current-run tool receipts
- CI artifact bundle
- commit/run identity
- P10 release candidate

## Output data and evidence
- trusted CI manifest
- CI-aware dashboard/screenshots/docs
- final v5.4 release/sidecar
- final red-team reports
- READY_FOR_GITHUB_REVIEW state

## Dashboard change
Public Tool Evidence shows actual run URL and current tool receipts; screenshot 05 captures both Local and CI sections. Other pages remain bound to same commit/run evidence bundle.

## Implementation tickets
1. Execute medium workflow on the exact commit under review and generate CI manifest from environment variables.
2. Verify ngspice, Yosys, Verilator, and SimPy receipts semantically. Any unavailable/failed mandatory CI tool blocks final READY.
3. Rebuild dashboard and screenshots from the CI evidence bundle, rerun all validation, package, and clean-unzip in CI.
4. Spawn independent product-visual, semiconductor-semantic, CI-integrity, and release-reproducibility reviewers. Parent fixes every P0/P1 and reruns.
5. Set READY only when state, manifest, archive hash, CI identity, screenshot source hash, and reviewers all agree.

## Required tests
- CI manifest URL/commit/run ID match GitHub environment.
- Four mandatory tools have valid REAL statuses and current receipt hashes.
- Screenshot 05 contains CI evidence and run link.
- Release manifest has all v5.4 booleans true and archive hash matches.
- Fresh-unzip verification passes on GitHub runner.

## Validation commands
```bash
python scripts/write_ci_run_manifest.py --strict
make dashboard
make screenshots
make validate-medium
make package-release
make verify-clean-unzip
python scripts/validate_v5_4_state.py
```

## Acceptance / Done criteria
- Final state is READY_FOR_GITHUB_REVIEW.
- GitHub link, screenshots, and release all refer to one verified commit/run evidence set.
- No P0/P1 reviewer finding remains.

## Forbidden shortcuts
- Manually creating CI manifest
- Using a different commit/run artifact
- Treating workflow configuration as execution
- Approving real product/Fab signoff
- Final READY from local environment

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
