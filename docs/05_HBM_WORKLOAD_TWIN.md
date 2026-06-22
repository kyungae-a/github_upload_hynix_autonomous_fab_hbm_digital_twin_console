# 05 HBM Workload Twin

## Purpose

This twin is a public-model workload and policy comparator for HBM-style memory pressure. It does not claim SK hynix proprietary controller behavior or silicon signoff. Its job is to show how a design candidate can be evaluated from request locality, bank pressure, refresh overhead, turnaround loss, latency tail, thermal headroom, and policy-level PPA tradeoffs.

## Inputs

Canonical and variant scenarios provide `peak_gbps`, `row_locality`, `traffic_gib`, `thermal_headroom_c`, `power_margin_w`, and deterministic seeds. These are public proxy inputs. They are designed to create repeatable stress cases rather than to reproduce confidential product telemetry.

## Engine Structure

`twin_core/memory_system/hbm_workload_engine.py` computes FCFS, FR-FCFS, and thermal-aware FR-FCFS candidates. Raw bandwidth fields always use the `_gbps` suffix. Display bandwidth fields always use the `_GBps` suffix and are derived by `GB/s = Gbps / 8`.

The engine emits:

- `raw_metrics.*_gbps`: bit-rate values for lineage and compatibility.
- `display_metrics.*_GBps`: byte-rate display values with source metric paths and derivations.
- `policy_comparison[]`: policy ID, raw/display bandwidth, p99 latency, thermal pressure, refresh overhead, bank conflict, bank-group conflict, hard-constraint result, score, and recommendation reason.
- `recommended_policy`: the highest scoring feasible policy under the public-model constraints.

## Dashboard Mapping

The HBM page reads `outputs/dashboard_data.json -> hbm_memory`. UI labels with `GB/s` bind only to `_GBps` display values. The page intentionally shows the unit note so a reviewer can see that raw Gbps values were not relabeled as byte bandwidth.

## Evidence Paths

- Engine raw output: `outputs/engine_raw/*hbm_memory_system_twin*.json`
- Engine parsed output: `outputs/engine_parsed/*hbm_memory_system_twin*.json`
- Metric lineage: `outputs/metric_lineage/*hbm_memory_system_twin*.json`
- Dashboard contract: `outputs/dashboard_data.json`
- Screenshot: `screenshots/03_hbm_workload_policy_compare.png`

## Claim Boundary

This is implementation evidence for public-model reasoning: unit discipline, policy comparison, deterministic metrics, and claim traceability. It is not a DRAM/HBM product signoff model, JEDEC compliance proof, or internal SK hynix design disclosure.
