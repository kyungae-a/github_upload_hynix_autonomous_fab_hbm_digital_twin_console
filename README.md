# Hynix Autonomous Fab x HBM Digital Twin Console

This repository is a public-model semiconductor decision-twin portfolio. It connects HBM workload behavior, circuit/physical proxy margins, Fab LOT and Q-time flow, factory routing, public-tool execution attempts, evidence lineage, and an AI judgment audit chain inside a nine-page product console.

It is designed for GitHub review: run the commands, inspect the generated evidence, open the dashboard, and compare the screenshots to the current output JSON.

## What Is Implemented

- Four executable core twins: HBM Memory System, Circuit/Physical Proxy, Fab Operation, and Factory Scene/Routing.
- `REAL_INTERNAL_RUN` receipts for all four core twins.
- Honest public-tool receipts for ngspice, Yosys, Verilator, and SimPy. Installed tools are executed through subprocesses; missing tools are recorded as `EXPLAINED_UNAVAILABLE` and are never promoted to fake real runs.
- Exactly six canonical scenarios plus 60 generated variants routed by `scenario_family` / `canonical_parent`, not by fragile scenario-id prefix checks.
- Evidence packets with engine provenance, public-tool receipts, metric lineage, input/output hashes, and claim limits.
- Deterministic evidence-sensitive AI judges, red-team partial miss, meta judge, virtual supervisor, and hidden-truth reveal.
- Evidence explorer dashboard, data-backed screenshots, Docker/devcontainer, GitHub Actions, negative fixtures, and manifest-last release packaging.
- Browser-captured screenshots of the actual console routes, not synthetic text cards.

## Console Pages

Open `frontend/index.html` after running the demo. The console contains:

1. Overview
2. HBM Workload Twin
3. Circuit / Physical Proxy Twin
4. Fab Operation Twin
5. Factory Scene / Routing Twin
6. AI Judgment Audit
7. Public Tool Evidence
8. Scenario Variant Lab
9. Hynix Alignment

The recommended reviewer path is to start on Overview, open the Fab Operation page for S03 Q-time flow, inspect the Factory route map, check Public Tool Evidence, then follow the AI Judgment Audit flow into the supervisor claim boundary.

## Quick Start

```bash
make setup-light
make demo-light
make validate
make dashboard
make screenshots
```

## Full Review Path

```bash
make setup-light
make demo-light
make setup-medium
make demo-medium
make demo-heavy
make run-canonical
make run-variants
make run-public-tools
make dashboard
make screenshots
make validate
make validate-medium
make package-release
make verify-clean-unzip
```

## Evidence Map

- Engine receipts: `outputs/run_receipts/`
- Public-tool receipts: `outputs/public_tool_receipts/`
- Evidence packets: `outputs/evidence_packets/`
- Metric lineage: `outputs/metric_lineage/`
- Dashboard data: `frontend/dashboard_data.json` and `outputs/dashboard_data.json`
- Screenshots: `screenshots/`
- Release archive: `release/hynix-autonomous-fab-hbm-digital-twin-console.zip`
- Release manifest: `release/hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json`
- GitHub submission steps: `GITHUB_SUBMISSION_STEPS_KO.md`

## Screenshot Set

- `screenshots/01_architecture.png`
- `screenshots/02_fab_qtime_timeline.png`
- `screenshots/03_hbm_workload_policy_compare.png`
- `screenshots/04_factory_scene_routing.png`
- `screenshots/05_public_tool_evidence.png`
- `screenshots/06_ai_judgment_audit_flow.png`
- `screenshots/07_hynix_alignment.png`

## Claim Boundary

This is not commercial Fab control, proprietary SK hynix modeling, real HBM vendor signoff, real recipe approval, or human expert approval. It is public-model portfolio evidence showing how semiconductor design/manufacturing decisions can be represented, tested, challenged, and bounded.

The virtual supervisor is a claim-boundary manager. It does not impersonate a real supervisor, and it always blocks product-level or signoff-level claims.
