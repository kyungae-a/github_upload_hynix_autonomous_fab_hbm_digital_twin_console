# Current v5.3 Product Gap Audit for v5.4 Final Productization

## Audit boundary

The attached v5.3 release is treated as a strong product baseline and upgraded **in place**. Its archive SHA-256 is `0979456db809d195bcf4f66739c973ff7f47ee4374f71d0c6b533647ca1c177c` and all 1,060 sidecar-listed payload hashes match the 1,061-entry archive. The historical v5.3 `READY_FOR_GITHUB_REVIEW` state is not accepted as evidence that v5.4 is complete.

## What is preserved

- Five-subsystem product architecture and nine-page console shell.
- Canonical scenarios, 60+ variant framework, AI Judge / Red-team / Meta / Supervisor / Oracle pipeline.
- Public-model and non-signoff boundaries.
- Docker/devcontainer/GitHub workflow structure, deterministic release conventions, and current evidence directories.

## P0 semantic gaps reproduced from source

### 1. HBM unit mismatch

`twin_core/memory_system/hbm_workload_engine.py` emits `*_gbps`. `frontend/app.js` reads those raw fields and appends `GB/s`. The current screenshot consequently presents bit-rate values as byte-rate values. v5.4 must create raw and display metrics, make `GB/s = Gbps / 8` explicit, and reject any GB/s label backed by a `_gbps` field.

### 2. Factory map is not yet a computed route map

The current scene engine stores a five-node graph only in raw output, emits summary counts in parsed state, chooses a route with a congestion `if/else`, and writes a two-line `.usda`. Alias-only routing modules do not implement Dijkstra/A*. The dashboard selects the summary object, so the route panel can be blank. v5.4 must promote the graph, selected route, route segments, congestion zones, route cost, route delay, and export path into the canonical dashboard contract.

### 3. Screenshots pass weak checks without proving required visual semantics

The legacy validator checks dimensions, byte variety, and a generic browser sidecar. It does not prove that the HBM screenshot uses byte-rate units, the Factory page contains a route, the Fab page contains two real LOT trajectories, the AI flow contains Meta Judge, or Public Tool Evidence separates local and CI state.

### 4. Product docs are not implementation manuals

Four key twin/audit documents are three lines long. v5.4 requires inputs, engine structure, formula/metric derivation, dashboard mapping, evidence paths, representative scenarios, and claim boundaries.

### 5. GitHub medium path has no CI evidence product

The workflow installs tools and runs targets but does not create a trusted `ci_run_manifest.json` from GitHub environment variables and does not upload the required evidence artifacts. The current dashboard repeats receipt artifacts and has no independent Local / CI evidence contract.

## Additional P0 authority issue

Product runtime currently writes phase PASS receipts and a `READY_FOR_GITHUB_REVIEW` state, while the frontend also hard-codes READY. Product execution may generate engineering evidence, but it may not certify orchestration completion. P00 removes this authority leak before any v5.4 feature work.

## Baseline command truth

`make test` and `make validate` both return zero. That demonstrates regression compatibility, not v5.4 product acceptance. The new validators must reject the reproduced semantic defects above.
