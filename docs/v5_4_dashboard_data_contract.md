# v5.4 Dashboard Data Contract

## Root

`outputs/dashboard_data.json` is the canonical generated data file. `frontend/dashboard_data.json` is a byte-identical publication copy created after generation. The frontend must never manufacture missing domain arrays or graphs.

```json
{
  "schema_version": "hynix-v5.4-dashboard-data-1",
  "run_id": "...",
  "generated_at_utc": "...",
  "source_artifacts": [{"path": "...", "sha256": "...", "run_id": "..."}],
  "hbm_memory": {},
  "circuit_physical": {},
  "fab_operation": {},
  "factory_scene": {},
  "ai_audit": {},
  "public_tool_evidence": {"local": {}, "ci": {}},
  "variant_matrix": {},
  "hynix_alignment": {}
}
```

## HBM

- `raw_metrics.*_gbps`: bit rate only.
- `display_metrics.*_GBps`: byte rate only, computed from raw values.
- `unit_notes.conversion`: `GB/s = Gbps / 8`.
- `policy_comparison[]`: policy ID, raw/display bandwidth, p99 latency, thermal pressure, refresh overhead, bank conflict, bank-group conflict, hard-constraint result, score, and recommendation reason.
- Every display metric carries `source_metric_path` and `derivation`.

## Factory scene

The root object contains `nodes`, `edges`, `selected_route`, `route_segments`, `congestion_zones`, `route_cost`, `route_delay_min`, and `openusd_like_export_path`. Frontend RouteMap receives this exact object. Missing graph data renders an explicit ERROR; no sample graph is legal.

## Fab operation

`lot_qtime_trajectories` contains at least LOT_A and LOT_B arrays. `q_over_threshold`, `dispatch_markers`, `metrology_delay_markers`, and `events` are copied from current-run engine artifacts with source hashes—not created in JavaScript.

## Public tools

`local` may contain `EXPLAINED_UNAVAILABLE`. `ci` is either an explicit `NOT_PRESENT_IN_LOCAL_ARTIFACT` object or a verified GitHub `ci_run_manifest.json`. Raw, parsed, and receipt files are grouped by one tool ID rather than rendered as duplicate cards.

## AI audit

The canonical stage sequence is `Evidence Packet → AI Judge → Red-team → Meta Judge → Virtual Supervisor → Hidden Truth`. Each stage links to a current-run artifact and exposes caught/escaped, approved claim, blocked claim, and real-signoff requirement.
