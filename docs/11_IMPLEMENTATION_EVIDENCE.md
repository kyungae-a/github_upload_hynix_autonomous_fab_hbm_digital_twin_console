# 11 Implementation Evidence

## Run Profile Summary

The repository supports light, medium, and heavy review profiles. The light profile runs the internal deterministic twins and builds evidence. The medium profile also attempts public tools and regenerates dashboard/screenshot evidence. The heavy profile runs the complete canonical and variant set before packaging.

## Internal Engine Summary

Four internal engines emit `REAL_INTERNAL_RUN` receipts:

- `hbm_memory_system_twin`
- `circuit_physical_proxy_twin`
- `fab_operation_twin`
- `factory_scene_routing_twin`

Each receipt includes the scenario ID, scenario family, input hash, code hash, raw output path, parsed output path, metric-lineage path, and deterministic environment metadata.

## Public Tool Run Summary

The public-tool layer covers ngspice, Yosys, Verilator, and SimPy. The runners now make current execution attempts. If a binary or package exists, it is executed and parsed. If unavailable, the receipt records `EXPLAINED_UNAVAILABLE`; this is intentionally not promoted to `REAL_EXTERNAL_RUN`.

This distinction matters because a portfolio should not pretend that an unavailable EDA tool was executed. The honest evidence is still useful: it proves the command, netlist/RTL artifact, expected path, and clean fallback boundary.

## Scenario Coverage

Six canonical scenarios are implemented:

- S01 HBM Thermal-Bandwidth Boundary
- S02 Memory PPA Hard Constraint
- S03 Fab Dispatch / Q-Time Global Flow
- S04 Tool-Chamber Observability / Metrology Lag
- S05 Process Recipe / Yield-Tail Risk
- S06 Proxy Evidence / Signoff Boundary

Each scenario creates evidence packets, AI judgments, red-team outputs, meta-judge outputs, supervisor logs, and hidden-truth reveal records.

## Variant / Mutation Coverage

The variant lab generates 60 variants, ten per canonical family. Each variant carries `scenario_family` and `canonical_parent`, so routing is stable even when the raw scenario ID begins with `V001_` rather than `S01`.

## Evidence Packet Lineage

Evidence packets live in `outputs/evidence_packets/`. Visible metrics map back to engine receipts and metric-lineage files. Hidden-truth data is intentionally excluded from packets, AI judgments, red-team challenges, meta-judge outputs, and supervisor logs until reveal.

## Dashboard / Screenshots

The dashboard data is generated into `frontend/dashboard_data.json` and `outputs/dashboard_data.json`. Screenshots are generated from that data and include sidecar JSON files containing the source hash. This prevents placeholder screenshot substitution.

## Validation Summary

Validation checks internal engine counts, public-tool receipt honesty, variant routing, metric sensitivity, hidden-truth isolation, red-team partial miss, supervisor non-overclaim, screenshot sidecars, dashboard sections, release hygiene, CI/devcontainer presence, and clean unzip reproducibility.

## Known Limitations

This is a public-model implementation. It is not a commercial Fab twin, not a proprietary HBM model, not real EDA signoff, and not real human approval. Its value is in showing connected reasoning and auditable claim boundaries.
