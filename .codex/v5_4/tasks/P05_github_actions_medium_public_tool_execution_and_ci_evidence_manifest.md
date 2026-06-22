# P05 — GitHub Actions Medium Public-Tool Execution and CI Evidence Manifest

## Purpose
Create a genuine CI evidence path for ngspice, Yosys, Verilator, and SimPy while keeping local unavailable status honest and separate.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `ci-public-tool-engineer`
- Independent reviewer: `ci-public-tool-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `.github/workflows/medium.yml`
- `scripts/write_ci_run_manifest.py`
- `scripts/merge_public_tool_evidence.py`
- `outputs/public_tool_evidence/README.md`
- `public_tool_runs/tool_receipts.py`
- `schemas/public_tool_ci_manifest.schema.json`
- `tests/test_ci_manifest_guard.py`
- `tests/test_public_tool_receipt_semantics.py`
- `validation/validate_ci_public_tool_evidence.py`
- `validation/validate_github_medium_workflow.py`
- `docs/11_IMPLEMENTATION_EVIDENCE.md`

## Classes and functions to implement
- `is_github_actions_environment()`
- `require_github_environment()`
- `build_github_run_url(env)`
- `verify_tool_receipt(tool, receipt, run_identity)`
- `write_ci_run_manifest(output_path)`
- `merge_local_and_ci_status(local, ci)`

## Input data
- GitHub environment variables
- current-run tool receipts/raw logs/parsed outputs
- commit SHA
- workflow/run identity

## Output data and evidence
- local_status.json
- trusted ci_run_manifest.json
- tool receipt hashes
- uploaded artifact bundle
- local/CI dashboard objects

## Dashboard change
Public Tool Evidence page has two independent sections: Local Release Status and CI Evidence Status. Each tool shows status, version, exact command, return code, receipt link, run URL where trusted, unavailable explanation, and no-signoff boundary.

## Implementation tickets
1. Install ngspice/yosys/verilator with apt and SimPy with pip in medium workflow.
2. Run setup-medium, demo-medium, validate-medium, dashboard, screenshots, and CI manifest generation in explicit steps with retained logs.
3. Generate CI run URL only from `GITHUB_SERVER_URL`, `GITHUB_REPOSITORY`, and `GITHUB_RUN_ID` when `GITHUB_ACTIONS=true`.
4. Require current commit/run identity and receipt hashes before classifying tool evidence as REAL.
5. Upload `outputs/public_tool_evidence/**`, `outputs/public_tool_runs/**`, screenshots, dashboard data, validation/test logs, and release candidate.
6. Local code may show CI as pending/absent but may not manufacture a URL or REAL status.

## Required tests
- Local environment cannot write a trusted CI manifest.
- Missing GitHub variable, stale commit, nonzero tool return code, or missing raw hash fails.
- Four tool records are unique and classified correctly.
- Workflow contains install/run/validate/dashboard/screenshots/upload steps.
- Dashboard displays local and CI evidence separately.

## Validation commands
```bash
pytest -q tests/test_ci_manifest_guard.py tests/test_public_tool_receipt_semantics.py
python validation/validate_github_medium_workflow.py --strict
python validation/validate_ci_public_tool_evidence.py --allow-missing-ci-locally
make validate-medium
```

## Acceptance / Done criteria
- Repository is ready to produce real medium evidence in GitHub Actions.
- No local fake CI evidence is possible.
- CI artifacts are inspectable and bound to commit/run identity.

## Forbidden shortcuts
- Hard-coded GitHub URL
- REAL status from tool presence alone
- Workflow YAML as execution proof
- Merging local unavailable and CI real status into one ambiguous card

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
