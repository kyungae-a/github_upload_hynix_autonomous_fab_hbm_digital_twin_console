# 07 Fab Operation Twin

## Purpose

The Fab Operation Twin models dispatch pressure, q-time risk, metrology delay, observability, and yield-tail proxy behavior for a public autonomous-fab portfolio scenario. It demonstrates how a semiconductor workflow can connect local tool decisions to downstream evidence quality and risk, without claiming access to a real fab control system.

## Inputs

Scenarios provide process time, transport time, LOT priority, q-time limits, metrology delay, tool windows, sensor drift, evidence age, sample power, and public-model defect/throughput deltas. Seeds make the run deterministic.

## Engine Structure

`twin_core/fab_operation/discrete_event_engine.py` uses a small deterministic event model with two tools, repeated LOT arrivals, start/end events, q-time records, and metrology delay markers.

The parsed output exposes:

- `lot_qtime_trajectories`: at least `LOT_A` and `LOT_B`, each with time and q-time remaining points.
- `q_over_threshold`: records that exceed the q-time limit.
- `dispatch_markers`: tool assignment events used by the dashboard.
- `metrology_delay_markers`: delayed observability events.
- `events`: current-run event log for timeline rendering.
- Scalar metrics such as `qtime_risk_index`, `local_dispatch_score`, `metrology_delay_min`, and `tail_risk_index`.

## Dashboard Mapping

The Fab page uses only `dashboard_data.json -> fab_operation`. The JavaScript does not synthesize LOT curves or fake event logs. The screenshot must show both LOT_A and LOT_B curves, q-time threshold evidence, dispatch markers, metrology delay markers, and a source-linked event log.

## Evidence Paths

- Engine raw output: `outputs/engine_raw/*fab_operation_twin*.json`
- Engine parsed output: `outputs/engine_parsed/*fab_operation_twin*.json`
- Metric lineage: `outputs/metric_lineage/*fab_operation_twin*.json`
- Dashboard contract: `outputs/dashboard_data.json`
- Screenshot: `screenshots/02_fab_qtime_timeline.png`

## Claim Boundary

This is an executable public-model fab operations proxy. It supports portfolio claims about system thinking, deterministic evidence, q-time reasoning, and model-to-dashboard traceability. It does not represent an actual SK hynix fab scheduler, production optimization, or yield prediction system.
