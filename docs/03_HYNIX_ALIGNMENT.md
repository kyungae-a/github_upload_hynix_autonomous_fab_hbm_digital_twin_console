# 03 Hynix Alignment

## Purpose

This repository is framed as a public-model portfolio aligned with SK hynix-facing themes: HBM workload pressure, Digital Twin thinking, Autonomous Fab operation, Q-time and LOT priority tradeoffs, and AI judgment governance. The alignment is directional and implementation-based. It does not claim access to proprietary SK hynix data, internal process recipes, product signoff, or commercial Fab control.

## Autonomous Fab Interpretation

PROJECT_INTERPRETATION: The Fab operation twin models LOT arrivals, queue decisions, tool availability, metrology delay, sensor drift, downstream bottleneck risk, and Q-time trajectories. This maps to the type of reasoning an Autonomous Fab system must support: local dispatch can look optimal while global flow or Q-time risk worsens.

The model is intentionally public and synthetic. The point is not to replicate a real Fab. The point is to show that a candidate can reason across event traces, constraints, and claim boundaries rather than treating throughput as the only objective.

## Digital Twin Interpretation

PROJECT_INTERPRETATION: The product joins four executable twins: HBM memory behavior, circuit/physical proxy margins, Fab operation, and factory routing. The dashboard exposes these as linked evidence rather than separate labels. A reviewer can follow a scenario from the visible configuration to engine output, evidence packet, AI judge, red-team challenge, supervisor boundary, and hidden-truth reveal.

## Q-Time / LOT Priority Implementation

The Fab scenario S03 asks whether a local priority decision can violate downstream Q-time. The generated event log and metrics expose `qtime_risk_index`, `local_dispatch_score`, metrology delay, and route congestion. The AI judge can initially prefer a local LOT priority when visible risk is low, while red-team and hidden-truth reveal show why global flow review is needed.

## HBM Workload Implementation

PROJECT_INTERPRETATION: The HBM twin models peak bandwidth, row locality, conflict pressure, refresh loss, read/write turnaround loss, latency, and thermal pressure. This connects to AI-memory workload reasoning because high short-term bandwidth is not enough when sustained bandwidth, thermal pressure, and hard constraints are visible.

## Factory Scene / Routing Implementation

The factory scene twin generates a 2D layout, transport edges, congestion index, selected route, route cost, and an OpenUSD-like public-model export. This gives Digital Twin visibility without claiming Omniverse deployment or internal factory layout access.

## AI Judgment Audit Implementation

USER_POSITIONING: The AI audit layer is the differentiating layer. It shows that AI-supported decisions can be useful but bounded. Judges read visible metrics, red-team catches four or five canonical cases, one scenario escapes until hidden truth reveal, and the virtual supervisor blocks real signoff claims.

## Evidence Map

- HBM evidence: `outputs/evidence_packets/`, `outputs/run_receipts/`, `outputs/metric_lineage/`
- Fab/Q-time evidence: `outputs/engine_raw/*fab_operation*`, `outputs/engine_parsed/*fab_operation*`
- Factory scene evidence: `outputs/factory_scene/`
- Public-tool evidence: `outputs/public_tool_receipts/`
- Dashboard and screenshots: `frontend/dashboard_data.json`, `screenshots/`

## Non-Claims

PUBLIC_SOURCE_SUPPORTED / PROJECT_INTERPRETATION / USER_POSITIONING labels are used to keep the framing honest. The repo does not imply endorsement, internal equivalence, proprietary access, real signoff, or finished-practitioner authority.
