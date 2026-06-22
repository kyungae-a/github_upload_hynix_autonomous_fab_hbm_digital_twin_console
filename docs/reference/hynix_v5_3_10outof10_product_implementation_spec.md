# Hynix Autonomous Fab × HBM Digital Twin Console v5.3
## 10/10 Product Implementation Spec — No More Name-Tag Modules

> This document is not a validator checklist. It is the concrete product design for the next implementation pass.
>
> The goal is to make a GitHub-heavy, screenshot-ready, interview-grade public-model semiconductor digital twin console. GPT Pro should only convert this into Codex task tickets. Codex should implement the product behavior described here.

---

## 0. Why v5.2 Still Had Gaps

v5.2 improved the project substantially: the manifest identifies the release as `Hynix Autonomous Fab x HBM Digital Twin Console`, sets `public_model_only: true`, and makes no real signoff claim. It also contains the core repo structure, workflows, Docker/devcontainer, dashboard data, screenshots, validation files, and the v5.2 reference blueprint.

However, it still fell short of a 10/10 GitHub submission for one reason:

> We described module names and acceptance criteria, but not enough **product behavior**.

That caused predictable gaps:

1. **Dashboard gap** — the system produced dashboard data and screenshots, but the user-facing console was still closer to a data summary than an interactive decision-twin product.
2. **Screenshot gap** — screenshots became data-based, but not yet strong visual evidence: they need charts, timelines, route maps, tool receipts, and audit flows that look like actual product pages.
3. **Public tool gap** — external tool runners were honest about unavailable tools, but the final GitHub target must be designed around GitHub Actions / Docker medium profile where `ngspice`, `yosys`, `verilator`, and `simpy` can actually run.
4. **Narrative gap** — README and START_HERE must guide a reviewer through the product, not explain a Codex package.
5. **Product-flow gap** — engines, evidence packets, AI judges, red-team, supervisor, oracle, and dashboard need to form explicit user flows, not just outputs in folders.

The fix is not “more constraints.” The fix is to define the exact product: screens, controls, engine calls, outputs, evidence, screenshots, and the user journey.

---

## 1. Final Product Definition

### Product Name

**Hynix Autonomous Fab × HBM Digital Twin Console**

### Product One-Liner

A public-model, multi-fidelity semiconductor digital twin console that connects HBM workload simulation, circuit/physical proxy analysis, fab operation dispatch, factory scene routing, and AI judgment audit into one reproducible GitHub portfolio.

### What the Reviewer Should Experience

A reviewer should open the GitHub repo and immediately understand:

1. This is not a toy dashboard.
2. This is not a real SK hynix internal model.
3. This is a public-model console that reconstructs the kind of decision chain relevant to HBM and Autonomous Fab work.
4. The user can run or inspect:
   - HBM workload policy comparison.
   - Circuit/physical margin proxy.
   - Fab dispatch/Q-time simulation.
   - Factory scene routing and congestion.
   - AI judge → red-team → virtual supervisor → hidden truth audit.
5. Screenshots and dashboard pages show actual data, not placeholder images.

### Non-Claims

The project must state clearly:

- It is not a commercial Fab digital twin.
- It is not a product signoff tool.
- It uses public-model assumptions and synthetic data.
- It is designed to demonstrate system-building, evidence tracing, and AI judgment governance for semiconductor physical systems.

---

## 2. Required Reviewer Journey

The repo must support this exact review path:

### Step 1 — README overview

Reviewer sees:

- Product screenshot grid.
- 5 core modules.
- Run commands.
- What to click first.
- Claim boundary.

### Step 2 — Open dashboard

Reviewer opens `frontend/index.html` or `dashboard/index.html` and sees a navigation sidebar:

1. Overview
2. HBM Workload Twin
3. Circuit / Physical Proxy Twin
4. Fab Operation Twin
5. Factory Scene / Routing Twin
6. AI Judgment Audit
7. Public Tool Evidence
8. Scenario Variant Lab
9. Hynix Alignment

### Step 3 — Inspect one end-to-end scenario

Reviewer selects `S03 Fab Dispatch / Q-Time Global Flow`.

The page shows:

- Scenario description.
- Fab event timeline.
- LOT A and LOT B Q-time curves.
- Factory route map.
- Evidence packet.
- AI judge decision.
- Red-team challenge.
- Supervisor claim boundary.
- Hidden truth reveal.

### Step 4 — Check public tool evidence

Reviewer opens Public Tool Evidence page.

The page shows:

- Tool availability status.
- Exact command attempted.
- Return code.
- stdout/stderr/log links.
- Parsed metrics.
- Claim boundary for each receipt.

If local environment lacks a tool, this is shown as `EXPLAINED_UNAVAILABLE`, not fake success. If GitHub Actions / Docker medium runs the tool, it is shown as `REAL_EXTERNAL_RUN`.

### Step 5 — Open screenshots

Screenshots must visually show the product pages:

- Architecture page.
- HBM policy comparison chart.
- Fab Q-time timeline.
- Factory scene map.
- Public tool evidence page.
- AI audit flow page.
- Hynix alignment page.

---

## 3. Repo Layout to Implement

```text
hynix_autonomous_fab_hbm_digital_twin_console/
├─ README.md
├─ START_HERE_KO.md
├─ Makefile
├─ Dockerfile
├─ docker-compose.yml
├─ pyproject.toml
├─ requirements.txt
├─ .devcontainer/devcontainer.json
├─ .github/workflows/
│  ├─ light.yml
│  ├─ medium.yml
│  └─ validation.yml
│
├─ docs/
│  ├─ 00_READ_ME_FIRST.md
│  ├─ 01_SYSTEM_THESIS.md
│  ├─ 02_PUBLIC_MODEL_LIMITS.md
│  ├─ 03_HYNIX_ALIGNMENT.md
│  ├─ 04_DIGITAL_TWIN_ARCHITECTURE.md
│  ├─ 05_HBM_WORKLOAD_TWIN.md
│  ├─ 06_CIRCUIT_PHYSICAL_PROXY_TWIN.md
│  ├─ 07_FAB_OPERATION_TWIN.md
│  ├─ 08_FACTORY_SCENE_ROUTING_TWIN.md
│  ├─ 09_AI_JUDGMENT_AUDIT_LAYER.md
│  ├─ 10_SCENARIO_CASEBOOK.md
│  ├─ 11_IMPLEMENTATION_EVIDENCE.md
│  ├─ 12_NON_CLAIMS_AND_CLAIMS.md
│  ├─ 13_INTERVIEW_TALKING_POINTS_KO.md
│  ├─ 14_SCREENSHOT_GUIDE.md
│  └─ reference/
│
├─ twin_core/
│  ├─ hbm_memory/
│  ├─ circuit_physical/
│  ├─ fab_operation/
│  ├─ factory_scene/
│  ├─ evidence/
│  └─ scenario_runner.py
│
├─ public_tool_runs/
│  ├─ ngspice/
│  ├─ yosys_verilator/
│  ├─ simpy_fab/
│  ├─ dramsim3_optional/
│  ├─ ramulator2_optional/
│  ├─ openroad_optional/
│  └─ cacti_optional/
│
├─ agents/
│  ├─ rule_based_judges.py
│  ├─ red_team.py
│  ├─ meta_judge.py
│  ├─ virtual_supervisor.py
│  └─ audit_pipeline.py
│
├─ oracle/
│  ├─ hidden/
│  └─ reveal.py
│
├─ scenarios/
│  ├─ canonical/
│  ├─ variants/
│  └─ generate_variants.py
│
├─ outputs/
│  ├─ engine_raw/
│  ├─ engine_parsed/
│  ├─ evidence_packets/
│  ├─ ai_judgments/
│  ├─ red_team_challenges/
│  ├─ meta_judge_outputs/
│  ├─ supervisor_gate_logs/
│  ├─ hidden_truth_reveals/
│  ├─ public_tool_receipts/
│  ├─ scenario_variant_results/
│  ├─ dashboard_data.json
│  └─ audit_metrics.json
│
├─ frontend/
│  ├─ index.html
│  ├─ styles.css
│  ├─ app.js
│  └─ dashboard_data.json
│
├─ screenshots/
│  ├─ 01_architecture.png
│  ├─ 02_fab_qtime_timeline.png
│  ├─ 03_hbm_workload_policy_compare.png
│  ├─ 04_factory_scene_routing.png
│  ├─ 05_public_tool_evidence.png
│  ├─ 06_ai_judgment_audit_flow.png
│  ├─ 07_hynix_alignment.png
│  └─ screenshot_manifest.json
│
├─ scripts/
│  ├─ generate_dashboard_data.py
│  ├─ render_dashboard_screenshots.py
│  ├─ package_release.py
│  └─ setup_repo.py
│
├─ tests/
└─ validation/
```

---

## 4. Product Module 1 — HBM / Memory System Twin

### Purpose

Show how different HBM workload and scheduling policies create different bandwidth, latency, thermal, refresh, and conflict behavior.

### Files

```text
twin_core/hbm_memory/workloads.py
twin_core/hbm_memory/hbm_stack.py
twin_core/hbm_memory/scheduler.py
twin_core/hbm_memory/refresh_model.py
twin_core/hbm_memory/thermal_model.py
twin_core/hbm_memory/policy_compare.py
twin_core/hbm_memory/run_hbm_twin.py
```

### Data Classes

```python
@dataclass
class WorkloadEvent:
    t: int
    kind: str  # READ / WRITE / REFRESH_PRESSURE / IDLE
    address: int
    bytes: int
    stream_id: str

@dataclass
class HbmWorkloadConfig:
    workload_id: str
    duration_cycles: int
    read_ratio: float
    burstiness: float
    locality: float
    write_burst_period: int
    thermal_intensity: float

@dataclass
class HbmPolicyConfig:
    policy_id: str  # FCFS / FR_FCFS / WRITE_DRAIN / THERMAL_SAFE / REFRESH_AWARE / BALANCED
    write_drain_threshold: int
    thermal_throttle_threshold: float
    refresh_guardband: float
    row_hit_bonus: float

@dataclass
class HbmTwinMetrics:
    theoretical_bandwidth_gbps: float
    effective_bandwidth_gbps: float
    sustained_bandwidth_gbps: float
    p50_latency_ns: float
    p99_latency_ns: float
    row_hit_rate: float
    bank_conflict_rate: float
    bank_group_conflict_rate: float
    refresh_overhead_pct: float
    read_write_turnaround_loss_pct: float
    thermal_pressure_index: float
    power_pressure_index: float
    policy_score: float
    hard_constraint_status: str  # PASS / REVIEW_ONLY / FAIL
```

### Required Workloads

Implement these workload generators:

1. `LLM_TRAINING_BURST`
2. `LLM_INFERENCE_LATENCY`
3. `SUSTAINED_BANDWIDTH_THERMAL`
4. `REFRESH_STRESS`
5. `READ_WRITE_TURNAROUND_STRESS`
6. `BANK_GROUP_CONFLICT_STRESS`

### Simulation Algorithm

Minimum implementation:

```python
for cycle in range(duration_cycles):
    events = workload.generate(cycle)
    for event in events:
        bank_group, bank, row = address_map(event.address)
        scheduler.enqueue(event)

    if refresh_model.should_refresh(cycle):
        scheduler.insert_refresh_penalty()

    command = scheduler.issue(policy, bank_state, thermal_state)
    latency = estimate_latency(command, row_buffer_state, conflict_state, refresh_state)

    update_row_buffer_state(command)
    update_conflict_counters(command)
    update_thermal_state(command, policy)
    update_power_state(command)
    record_latency(latency)
    record_bytes_served(command)
```

### Policy Comparison

For each scenario, compare at least 4 policies:

- FCFS
- FR_FCFS
- WRITE_DRAIN
- THERMAL_SAFE
- BALANCED

Output:

```json
{
  "workload_id": "SUSTAINED_BANDWIDTH_THERMAL",
  "policies": {
    "FCFS": {...metrics...},
    "FR_FCFS": {...metrics...},
    "WRITE_DRAIN": {...metrics...},
    "THERMAL_SAFE": {...metrics...},
    "BALANCED": {...metrics...}
  },
  "recommended_policy": "BALANCED",
  "why": "best sustained bandwidth under thermal threshold"
}
```

### Dashboard Requirements

HBM page must show:

- Workload selector.
- Policy comparison table.
- Bar chart: effective vs sustained bandwidth.
- Line/bar chart: p50/p99 latency.
- Thermal pressure chart.
- Refresh overhead chart.
- Recommended policy.
- AI judge decision for S01/S02/S06.

---

## 5. Product Module 2 — Circuit / Physical Proxy Twin

### Purpose

Show how circuit-level proxy evidence creates margin and signoff-boundary risks.

### Files

```text
twin_core/circuit_physical/read_path_model.py
twin_core/circuit_physical/retention_model.py
twin_core/circuit_physical/pvt_corner_sweep.py
twin_core/circuit_physical/proxy_signoff.py
twin_core/circuit_physical/netlist_generator.py
twin_core/circuit_physical/run_circuit_proxy.py
public_tool_runs/ngspice/netlists/read_path_charge_sharing.sp
public_tool_runs/ngspice/netlists/retention_leakage_proxy.sp
public_tool_runs/ngspice/run_ngspice.py
public_tool_runs/ngspice/parse_ngspice.py
```

### Core Formulas

Implement charge sharing:

```text
V_final = (C_cell * V_cell + C_bitline * V_precharge) / (C_cell + C_bitline)
delta_v_bitline = abs(V_final - V_precharge)
```

Sense margin:

```text
sense_margin_mv = delta_v_bitline_mv - sense_amp_offset_mv - noise_sigma_mv * noise_guardband
```

Retention margin:

```text
retention_margin_mv = stored_charge_margin_mv - leakage_loss_mv - temperature_penalty_mv
```

Proxy pass logic:

```python
proxy_execution_pass = run_completed
proxy_design_pass = sense_margin_mv >= floor and retention_margin_mv >= floor and wns_proxy_ns >= 0
real_signoff_allowed = False
```

### Required Outputs

```json
{
  "cell_cap_fF": 24.0,
  "bitline_cap_fF": 280.0,
  "charge_share_delta_mv": 18.7,
  "sense_margin_mv": 11.2,
  "retention_margin_mv": -3.4,
  "pvt_corner": "HOT_SLOW",
  "wns_proxy_ns": -0.12,
  "proxy_execution_pass": true,
  "proxy_design_pass": false,
  "real_signoff_allowed": false
}
```

### Ngspice Integration

`run_ngspice.py` must:

- Check whether `ngspice` binary exists.
- If present, run subprocess command.
- Save stdout/stderr/log.
- Parse metrics.
- Mark receipt as `REAL_EXTERNAL_RUN`.
- If absent, mark `EXPLAINED_UNAVAILABLE` and keep internal proxy results.

Do not fake `REAL_EXTERNAL_RUN`.

### Dashboard Requirements

Circuit page must show:

- Charge-sharing visual summary.
- PVT/corner sweep table.
- Sense margin chart.
- Retention margin chart.
- Proxy execution vs proxy design vs real signoff status.
- Ngspice receipt/log link.

---

## 6. Product Module 3 — Fab Operation Twin

### Purpose

Show Q-time, LOT priority, tool availability, chamber health, metrology delay, and dispatch decisions in a public-model Autonomous Fab simulation.

### Files

```text
twin_core/fab_operation/simpy_environment.py
twin_core/fab_operation/lot.py
twin_core/fab_operation/tool.py
twin_core/fab_operation/chamber.py
twin_core/fab_operation/process_step.py
twin_core/fab_operation/qtime.py
twin_core/fab_operation/dispatch_policy.py
twin_core/fab_operation/maintenance.py
twin_core/fab_operation/metrology.py
twin_core/fab_operation/yield_risk.py
twin_core/fab_operation/run_fab_twin.py
public_tool_runs/simpy_fab/run_simpy_demo.py
```

### Entities

Implement classes:

```python
@dataclass
class Lot:
    lot_id: str
    product_priority: float
    qtime_deadline_min: float
    arrival_time: float
    route: list[str]
    current_step: str

@dataclass
class Tool:
    tool_id: str
    tool_type: str
    chamber_ids: list[str]
    availability: float
    maintenance_due_score: float

@dataclass
class Chamber:
    chamber_id: str
    health_score: float
    sensor_drift_score: float
    degradation_rate: float

@dataclass
class MetrologyStation:
    station_id: str
    delay_min: float
    sample_rate: float
```

### Required Event Types

```text
LOT_ARRIVAL
QUEUE_ENTER
TOOL_AVAILABLE
DISPATCH_DECISION
PROCESS_START
PROCESS_END
METROLOGY_SAMPLE
METROLOGY_DELAY
SENSOR_DRIFT_UPDATE
MAINTENANCE_DECISION
DOWNSTREAM_QUEUE_UPDATE
QTIME_RISK_THRESHOLD_CROSSED
YIELD_TAIL_RISK_ESCALATED
```

### Simulation Algorithm

Use SimPy when available:

```python
env = simpy.Environment()
tool_resource = simpy.Resource(env, capacity=1)
env.process(lot_process(env, lot, tool_resource, policy, event_log))
env.process(sensor_drift_process(env, chamber, event_log))
env.process(metrology_process(env, station, event_log))
env.run(until=simulation_horizon)
```

Fallback internal event loop is allowed only if SimPy is unavailable, but must be labeled accordingly.

### Required Metrics

```text
qtime_remaining_min
qtime_trajectory
q_over_risk
lot_priority_score
tool_availability
chamber_health_score
sensor_drift_score
metrology_delay_min
downstream_bottleneck_score
maintenance_due_score
expected_throughput
rework_probability
scrap_risk
yield_tail_risk
```

### Dashboard Requirements

Fab page must show:

- Event timeline with timestamps.
- LOT A / LOT B Q-time curves.
- Dispatch decision markers.
- Tool utilization.
- Queue depth over time.
- Metrology delay markers.
- Q-over risk marker.
- AI judge + red-team + supervisor summary.

---

## 7. Product Module 4 — Factory Scene / Routing Twin

### Purpose

Create an OpenUSD-like public-model fab scene and routing layer aligned with digital twin / factory scene concepts.

### Files

```text
twin_core/factory_scene/layout.py
twin_core/factory_scene/scene_graph.py
twin_core/factory_scene/routing_graph.py
twin_core/factory_scene/congestion.py
twin_core/factory_scene/openusd_like_export.py
twin_core/factory_scene/route_optimizer.py
twin_core/factory_scene/run_factory_scene.py
```

### Entities

```python
@dataclass
class FabNode:
    node_id: str
    kind: str  # TOOL / BUFFER / METROLOGY / STOCKER
    x: float
    y: float
    capacity: int

@dataclass
class TransportEdge:
    source: str
    target: str
    distance: float
    congestion_penalty: float

@dataclass
class RouteResult:
    lot_id: str
    path: list[str]
    total_distance: float
    total_delay: float
    congestion_score: float
```

### Routing Algorithm

Implement Dijkstra or A*:

```python
cost(edge) = edge.distance + edge.congestion_penalty * congestion_weight + qtime_pressure_penalty
```

### Required Exports

```text
outputs/factory_scene/fab_layout.json
outputs/factory_scene/scene_graph.json
outputs/factory_scene/routing_graph.json
outputs/factory_scene/routing_result.json
outputs/factory_scene/openusd_like_scene.usda
```

### Dashboard Requirements

Factory page must show:

- 2D fab floor map.
- Tool/buffer/metrology nodes.
- Transport edges.
- Selected LOT route.
- Congestion zones.
- Route distance/delay.
- OpenUSD-like export link.

---

## 8. Product Module 5 — AI Judgment Audit Layer

### Purpose

Demonstrate that AI judgment can be plausible inside a digital twin but still wrong or incomplete due to hidden truth, model boundary, stale evidence, or proxy/signoff confusion.

### Files

```text
agents/rule_based_judges.py
agents/red_team.py
agents/meta_judge.py
agents/virtual_supervisor.py
agents/audit_pipeline.py
oracle/reveal.py
oracle/hidden/S01.json ... S06.json
```

### Required Pipeline

```text
engine outputs
→ evidence packet
→ AI judge
→ red-team
→ meta judge
→ virtual supervisor
→ hidden truth reveal
→ audit metrics
```

### Judge Behavior

Judges must use evidence metrics, not hardcoded scenario IDs.

Example:

```python
if family == "S02":
    if retention_margin_mv < retention_floor_mv or sense_margin_mv < sense_floor_mv:
        decision = "reject_bandwidth_optimized_candidate"
    elif bandwidth_gain > threshold:
        decision = "select_bandwidth_candidate_for_review"
```

### Red-team Behavior

Red-team must catch 4–5 of 6 canonical issues. At least one issue must escape until hidden truth reveal.

### Supervisor Behavior

Supervisor must output:

```json
{
  "approved_claim": "...public-model review claim...",
  "blocked_claim": "...real deployment or signoff claim...",
  "requires_real_signoff": true,
  "claim_boundary": "..."
}
```

### Dashboard Requirements

AI Audit page must show:

- AI decision.
- Evidence metrics used.
- Confidence.
- Red-team challenge.
- Meta-judge assessment.
- Supervisor approved/blocked claim.
- Hidden truth reveal.
- Caught vs escaped status.

---

## 9. Evidence Packet Contract

Every scenario must produce:

```json
{
  "scenario_id": "S03",
  "scenario_family": "S03",
  "canonical_parent": "S03",
  "run_id": "...",
  "engines_used": ["fab_operation_twin", "factory_scene_routing_twin"],
  "visible_metrics": {...},
  "metric_lineage": [
    {
      "metric": "q_over_risk",
      "source_engine": "fab_operation_twin",
      "raw_output_path": "outputs/engine_raw/...json",
      "parsed_output_path": "outputs/engine_parsed/...json"
    }
  ],
  "public_tool_receipts": [...],
  "claim_boundary": "public_model_only"
}
```

---

## 10. Canonical Scenario Product Cards

### S01 — HBM Thermal-Bandwidth Boundary

Required pages/data:

- HBM policy comparison.
- Thermal pressure chart.
- AI recommendation.
- Hidden truth: stale thermal model or missing sustained thermal boundary.

### S02 — Memory PPA Hard Constraint

Required pages/data:

- Candidate A/B/C table.
- Bandwidth vs retention/sense margin.
- Circuit proxy margin results.
- AI decision changes when margin threshold changes.

### S03 — Fab Dispatch / Q-Time Global Flow

Required pages/data:

- LOT A/B event timeline.
- Q-time trajectory.
- Factory route map.
- Downstream bottleneck.

### S04 — Tool-Chamber Observability / Metrology Lag

Required pages/data:

- Chamber health score.
- Sensor drift.
- Metrology delay.
- Maintenance decision.

### S05 — Process Recipe / Yield-Tail Risk

Required pages/data:

- Average defect proxy.
- P95/P99 tail risk.
- Wafer edge/yield-tail risk.
- Pilot expansion blocked by supervisor.

### S06 — Proxy Evidence / Signoff Boundary

Required pages/data:

- Public tool receipts.
- Proxy execution pass.
- Proxy design pass.
- Real signoff false.
- AI overclaim blocked.

---

## 11. Variant / Mutation Lab

### Requirements

Generate at least 60 variants.

Each variant must contain:

```json
{
  "scenario_id": "V001_S01",
  "scenario_family": "S01",
  "canonical_parent": "S01",
  "mutation_type": "thermal_freshness",
  "mutation_parameters": {...}
}
```

### Required Variant Reports

```text
outputs/scenario_variant_results/variant_matrix.json
outputs/scenario_variant_results/judge_sensitivity_report.md
outputs/scenario_variant_results/red_team_robustness_report.md
outputs/scenario_variant_results/variant_heatmap_data.json
```

### Dashboard

Variant Lab page must show:

- Variant matrix by canonical parent.
- Judge decision heatmap.
- Red-team caught/escaped matrix.
- Supervisor blocked/reworded counts.

---

## 12. Frontend Console Requirements

Static frontend is acceptable, but it must look like a product console, not a JSON viewer.

### Required Pages

1. Overview
2. HBM Workload Twin
3. Circuit / Physical Proxy Twin
4. Fab Operation Twin
5. Factory Scene / Routing Twin
6. AI Judgment Audit
7. Public Tool Evidence
8. Scenario Variant Lab
9. Hynix Alignment

### Required Components

```text
MetricCard
StatusBadge
LineChart
BarChart
Timeline
RouteMap
EvidenceTable
DecisionFlow
ReceiptPanel
ScenarioSelector
VariantMatrix
```

If using pure HTML/JS, implement components as functions that render DOM blocks.

### No More JSON Dump UI

JSON preview can be included, but it cannot be the main UI.

---

## 13. Screenshot Requirements

Screenshots must correspond to actual console pages.

Required files:

```text
screenshots/01_architecture.png
screenshots/02_fab_qtime_timeline.png
screenshots/03_hbm_workload_policy_compare.png
screenshots/04_factory_scene_routing.png
screenshots/05_public_tool_evidence.png
screenshots/06_ai_judgment_audit_flow.png
screenshots/07_hynix_alignment.png
screenshots/screenshot_manifest.json
```

Each screenshot must show actual data:

- Charts.
- Timelines.
- Route maps.
- Tables.
- Receipts.
- Decision flow.

---

## 14. Public Tool Evidence Requirements

### Medium Profile Tools

- ngspice
- yosys
- verilator
- simpy

### Behavior

If installed:

- Run actual command.
- Save logs.
- Save receipt as `REAL_EXTERNAL_RUN` or `REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN`.

If not installed:

- Save receipt as `EXPLAINED_UNAVAILABLE`.
- Do not pretend success.
- README must explain GitHub Actions/Docker medium path.

---

## 15. Make Targets

Required:

```text
make setup-light
make setup-medium
make demo-light
make demo-medium
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

---

## 16. What GPT Pro Must Do

GPT Pro should not redesign this product.

It should convert this spec into Codex tasks:

- Phase 0: inspect current v5.2.
- Phase 1: fix START_HERE / README.
- Phase 2: implement full console pages.
- Phase 3: strengthen HBM page and charts.
- Phase 4: strengthen Fab timeline and SimPy evidence.
- Phase 5: strengthen Factory Scene map.
- Phase 6: strengthen Circuit/Physical proxy page.
- Phase 7: implement Public Tool Evidence page.
- Phase 8: implement AI Audit flow page.
- Phase 9: implement Variant Matrix page.
- Phase 10: regenerate screenshots from actual pages/data.
- Phase 11: run validation and package release.

---

## 17. Final Success Definition

The project is 10/10 only if a reviewer can open GitHub and see:

1. A real product-like console.
2. HBM workload policy comparison with charts.
3. Fab Q-time event timeline with curves.
4. Factory scene route map.
5. Circuit/physical margin and signoff boundary.
6. AI audit decision flow.
7. Public tool receipts.
8. Variant/mutation lab.
9. Hynix alignment page.
10. Honest public-model/non-signoff limits.

If the reviewer only sees file lists, JSON dumps, or validator outputs, it is not 10/10.

