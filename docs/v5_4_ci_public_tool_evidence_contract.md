# v5.4 GitHub Actions Public-Tool Evidence Contract

## Local versus CI

Local runs may report `EXPLAINED_UNAVAILABLE`. They write `outputs/public_tool_evidence/local_status.json`. They may not write a GitHub URL or claim CI execution.

A trusted `outputs/public_tool_evidence/ci_run_manifest.json` is created only when `GITHUB_ACTIONS=true` and the required GitHub environment variables are present. It records workflow, run URL, repository, run ID/attempt, commit SHA, OS/image, Python version, per-tool receipt path/hash/status/version/command/return code, and artifact bundle hash.

## Medium workflow

Install `ngspice`, `yosys`, and `verilator`; install Python requirements plus SimPy; run setup, medium demo, medium validation, dashboard, screenshot capture, and CI-manifest generation. Upload public-tool evidence, raw tool runs, screenshots, dashboard data, test/validation logs, and release candidate.

## Semantic trust

A CI tool can be `REAL_EXTERNAL_RUN` or `REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN` only when the current command returned zero, executable/version evidence exists, raw output and parsed result hashes match, and the receipt commit/run identity equals the manifest. The dashboard shows local and CI status in separate sections and never merges them into one badge.
