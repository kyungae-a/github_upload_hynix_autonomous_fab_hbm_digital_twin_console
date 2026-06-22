# Codex Master Directive — Hynix v5.4 Final Productization

## 1. Mission

Upgrade the current v5.3 repository **in place** into the final GitHub-link and screenshot submission build of **Hynix Autonomous Fab × HBM Digital Twin Console**. This is not a new scaffold and not a validator exercise. Preserve working twins, scenarios, variants, governance, and release machinery; directly close the five product gaps proven in the source directive and baseline audit.

The reviewer must see a coherent evidence explorer: correct HBM units and policy charts, real Fab trajectories, a computed factory route map, circuit/signoff boundaries, local and GitHub CI tool evidence, the full AI audit flow, variants, and Hynix alignment.

## 2. Non-negotiable locks

- Source directive SHA-256: `eceb397237971df0faa33d6edf3b3211ed9700317d18a209b20a6d415fcd2e89`
- Baseline archive SHA-256: `0979456db809d195bcf4f66739c973ff7f47ee4374f71d0c6b533647ca1c177c`
- Baseline sidecar manifest SHA-256: `6df0c52d9f9291c107634ab06f361e1949a5dc58bd07fbac9e3e6566206a33ce`
- Contract: `config/v5_4_contract_lock.json`
- Authoritative state: `docs/v5_4_build_state.json`
- Upgrade mode: current repository root; no nested product clone
- Final product boundary: public model only; no commercial Fab twin, proprietary SK hynix access, production control, or real product signoff

The existing v5.3 release is strong and byte-integrity checked, but its historical READY state is not v5.4 acceptance.

## 3. Phase orchestration

| Phase | Work | Writer | Independent reviewer |
|---|---|---|---|
| P00 | Baseline integrity, in-place upgrade boundary, and authority reset | `baseline-auditor` | `baseline-integrity-reviewer` |
| P01 | v5.4 product data contract, dashboard lifecycle, and current-run provenance | `product-contract-engineer` | `product-contract-reviewer` |
| P02 | HBM bandwidth unit normalization and policy-comparison product page | `hbm-unit-product-engineer` | `hbm-unit-reviewer` |
| P03 | Factory raw graph, congestion-aware routing, OpenUSD-like export, and route map | `factory-route-product-engineer` | `factory-route-reviewer` |
| P04 | Fab Q-time timeline fidelity, dual-LOT trajectories, and event markers | `fab-timeline-product-engineer` | `fab-timeline-reviewer` |
| P05 | GitHub Actions medium public-tool execution and CI evidence manifest | `ci-public-tool-engineer` | `ci-public-tool-reviewer` |
| P06 | Nine-page evidence explorer integration and local/CI evidence separation | `frontend-evidence-engineer` | `frontend-evidence-reviewer` |
| P07 | Browser screenshot visual contract and source-linked capture evidence | `screenshot-contract-engineer` | `screenshot-contract-reviewer` |
| P08 | Reviewer-grade product documentation and claim-to-evidence mapping | `product-docs-engineer` | `product-docs-reviewer` |
| P09 | Semantic validators and deliberate negative regression fixtures | `semantic-validation-engineer` | `negative-regression-reviewer` |
| P10 | Local final transaction, deterministic release candidate, and clean-unzip verification | `release-productization-engineer` | `cleanroom-release-reviewer` |
| P11 | Genuine GitHub medium evidence finalization and independent product red team | `github-medium-finalizer` | `final-product-redteam` |

Explicitly spawn each writer and reviewer. Writer cannot approve itself. Parent alone edits shared contracts, `Makefile`, authoritative state, and final manifests after closing all P0/P1 findings.

## 4. Dependency and batching

- Serial: P00 → P01.
- P02, P03, P04, and P05 may proceed in isolated worktrees after P01 freezes schemas.
- Integration serial: P06 → P07; P08 may overlap P07 only after dashboard paths are stable.
- Hardening serial: P09 → P10 → P11.
- Hidden/final state, dashboard schema, Makefile, and manifests are parent-owned shared files.

## 5. Product-wide invariants

1. **No unit ambiguity:** `_gbps` is Gbps; `_GBps` is GB/s and equals raw/8. UI labels bind only to display fields.
2. **No fallback evidence:** frontend does not synthesize HBM, Fab, route, audit, or tool data.
3. **Computed route graph:** route and congestion are engine outputs, not UI illustration or if/else lookup.
4. **One evidence chain:** current input → engine/tool → raw → parsed → metric lineage → dashboard → DOM → screenshot → manifest.
5. **Honest CI:** local unavailable is allowed; final CI evidence comes only from genuine GitHub Actions environment and current tool receipts.
6. **Claim boundary:** proxy execution/design evidence never becomes real signoff; Virtual Supervisor is a claim-boundary manager.
7. **Visual product acceptance:** charts, timelines, maps, tables, and decision flow are the primary UI. JSON is secondary drill-down only.
8. **No self-certification:** product runtime and frontend cannot write phase PASS/READY.
9. **Producers before validators:** freeze after all producers; manifest last; package without regeneration; clean-unzip from fresh directory.

## 6. Per-phase execution loop

1. Read the current ticket under `.codex/v5_4/tasks/` completely.
2. Spawn the named writer and demand schema-valid handoff.
3. Run every listed test/command and retain logs/hashes/run IDs.
4. Spawn the independent reviewer with task, diff, logs, dashboard, screenshots, and evidence.
5. Parent fixes all P0/P1 and reruns tests/reviewer.
6. Only parent marks the phase PASS in `docs/v5_4_build_state.json`.
7. Continue without routine milestone approval.

## 7. Local versus GitHub final state

A fully valid local build without genuine GitHub medium evidence ends at `AWAITING_GITHUB_MEDIUM`. P11 executes on the exact GitHub commit, generates trusted `ci_run_manifest.json`, rebuilds dashboard/screenshots/release, passes clean-unzip, and then may set `READY_FOR_GITHUB_REVIEW`. Never manufacture CI evidence to avoid this boundary.

## 8. Final transaction

```bash
make demo-light
make demo-medium || true
make demo-heavy
make run-canonical
make run-variants
make run-public-tools
make dashboard
make screenshots
make test
make validate
make validate-medium
make package-release
make verify-clean-unzip
```

Final release manifest must use `hynix-v5.4-release-manifest-1` and contain all required v5.4 semantic flags from the contract lock. P11 additionally requires genuine GitHub medium receipts for ngspice, Yosys, Verilator, and SimPy plus four independent final reviewer PASS results.
