# Hynix v5.2 Concrete Product Implementation Blueprint

## 0. Purpose of this document

This is not a naming/spec checklist. This is the concrete product blueprint for the next implementation pass.

The target repository must implement a real, inspectable **Hynix-oriented Public-Model Semiconductor Digital Twin Console**, not a bundle of labels, placeholder screenshots, or status receipts.

The core product is:

> **Hynix Autonomous Fab × HBM Digital Twin Console**  
> A heavy GitHub repository where HBM workload behavior, circuit/physical proxy margins, Fab Q-time/LOT dispatch flow, factory routing/scene graph, and AI judgment audit are connected through executable engines, evidence packets, dashboard pages, screenshots, and validation.

GPT Pro should not reinterpret this document. GPT Pro should transform it into Codex implementation tickets. Codex should implement the modules described here.

---

## 1. Product definition

### 1.1 What the user should be able to do

A reviewer should be able to open the repo and run:

```bash
make demo-light
make demo-medium
make validate
make dashboard
```

Then open the dashboard and see:

1. an architecture page showing the four twins and the AI audit layer;
2. an HBM workload page where policies change bandwidth, latency, conflict, refresh, thermal pressure, and hard-constraint status;
3. a circuit/physical proxy page showing charge-sharing, sense margin, retention margin, PVT/corner sweep, ngspice/Yosys/Verilator receipts where available, and proxy-vs-signoff boundary;
4. a Fab operation page showing LOT movement, Q-time trajectory, tool/chamber state, metrology lag, sensor drift, maintenance decisions, and yield-tail risk;
5. a factory scene/routing page showing a 2D fab layout, tool nodes, transport edges, congestion, route choice, and dispatch delay;
6. an AI audit page showing AI Judge → Red-team → Meta Judge → Virtual Supervisor → Hidden Truth Reveal for each canonical scenario and variants;
7. a screenshot folder with images generated from the actual dashboard data, not placeholders.

### 1.2 What this repo is not

It is not a commercial Fab digital twin.  
It is not product signoff.  
It is not a claim of proprietary SK hynix data access.  
It is not a real Omniverse deployment.  
It is not a real DRAM/HBM vendor model.

It is a public-model, multi-fidelity, reproducible decision-twin console implemented with public knowledge, internal deterministic models, and optional real public tool runs.

---

## 2. Final product architecture

The repo must be built as a product with five internal subsystems.

```text
hynix_public_model_semiconductor_decision_twin/
├─ README.md
├─ START_HERE_KO.md
├─ Makefile
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .devcontainer/devcontainer.json
├─ .github/workflows/
│  ├─ light.yml
│  ├─ medium.yml
│  └─ validation.yml
│
├─ twin_core/
│  ├─ common/
│  │  ├─ schemas.py
│  │  ├─ units.py
│  │  ├─ hashing.py
│  │  ├─ run_receipt.py
│  │  └─ evidence_packet.py
│  │
│  ├─ hbm_memory/
│  │  ├─ hbm_stack.py
│  │  ├─ workloads.py
│  │  ├─ scheduler.py
│  │  ├─ refresh_model.py
│  │  ├─ thermal_model.py
│  │  ├─ policy_compare.py
│  │  ├─ trace_generator.py
│  │  └─ run_hbm_twin.py
│  │
│  ├─ circuit_physical/
│  │  ├─ read_path_model.py
│  │  ├─ retention_model.py
│  │  ├─ pvt_corner_sweep.py
│  │  ├─ proxy_signoff.py
│  │  ├─ rtl_proxy.py
│  │  ├─ netlist_generator.py
│  │  └─ run_circuit_proxy.py
│  │
│  ├─ fab_operation/
│  │  ├─ simpy_environment.py
│  │  ├─ lot.py
│  │  ├─ tool.py
│  │  ├─ chamber.py
│  │  ├─ process_step.py
│  │  ├─ qtime.py
│  │  ├─ dispatch_policy.py
│  │  ├─ maintenance.py
│  │  ├─ metrology.py
│  │  ├─ yield_risk.py
│  │  └─ run_fab_twin.py
│  │
│  ├─ factory_scene/
│  │  ├─ layout.py
│  │  ├─ scene_graph.py
│  │  ├─ routing_graph.py
│  │  ├─ congestion.py
│  │  ├─ route_optimizer.py
│  │  ├─ openusd_like_export.py
│  │  └─ run_factory_scene.py
│  │
│  └─ pipeline/
│     ├─ scenario_loader.py
│     ├─ run_scenario.py
│     ├─ run_variants.py
│     ├─ build_dashboard_data.py
│     └─ build_release.py
│
├─ public_tool_runs/
│  ├─ ngspice/
│  ├─ rtl/
│  ├─ simpy/
│  ├─ dramsim3_optional/
│  ├─ ramulator2_optional/
│  └─ openroad_optional/
│
├─ agents/
│  ├─ rule_based_judges.py
│  ├─ red_team.py
│  ├─ meta_judge.py
│  ├─ virtual_supervisor.py
│  └─ audit_pipeline.py
│
├─ scenarios/
│  ├─ canonical/
│  └─ variants/
│
├─ outputs/
│  ├─ engine_raw/
│  ├─ engine_parsed/
│  ├─ public_tool_runs/
│  ├─ evidence_packets/
│  ├─ ai_judgments/
│  ├─ red_team_challenges/
│  ├─ meta_judge_outputs/
│  ├─ supervisor_gate_logs/
│  ├─ hidden_truth_reveals/
│  ├─ factory_scene/
│  ├─ fab_event_logs/
│  ├─ hbm_traces/
│  ├─ metric_lineage/
│  ├─ audit_metrics.json
│  └─ dashboard_data.json
│
├─ dashboard/
│  ├─ index.html
│  ├─ app.js
│  ├─ style.css
│  └─ pages/
│     ├─ architecture.html
│     ├─ hbm_workload.html
│     ├─ circuit_physical.html
│     ├─ fab_operation.html
│     ├─ factory_scene.html
│     ├─ ai_audit.html
│     └─ evidence_lineage.html
│
├─ screenshots/
│  ├─ 01_architecture.png
│  ├─ 02_fab_qtime_timeline.png
│  ├─ 03_hbm_workload_policy_compare.png
│  ├─ 04_factory_scene_routing.png
│  ├─ 05_public_tool_evidence.png
│  ├─ 06_ai_judgment_audit_flow.png
│  └─ screenshot_manifest.json
│
├─ scripts/
│  ├─ render_dashboard_screenshots.py
│  ├─ generate_variants.py
│  └─ collect_github_submission_pack.py
│
├─ validation/
│  ├─ validate_product_modules.py
│  ├─ validate_hbm_engine_behavior.py
│  ├─ validate_circuit_proxy_behavior.py
│  ├─ validate_fab_simpy_behavior.py
│  ├─ validate_factory_scene_routing.py
│  ├─ validate_public_tool_real_runs.py
│  ├─ validate_variant_family_routing.py
│  ├─ validate_judge_metric_sensitivity.py
│  ├─ validate_dashboard_evidence_lineage.py
│  ├─ validate_screenshots_from_dashboard.py
│  ├─ validate_hynix_docs_depth.py
│  └─ validate_release_hygiene.py
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
│  └─ 14_SCREENSHOT_GUIDE.md
└─ release/
```

---

## 3. Data model: scenario, engine output, evidence packet

### 3.1 Scenario object

Every canonical and variant scenario must use this structure.

```json
{
  "scenario_id": "S03",
  "scenario_family": "S03",
  "canonical_parent": "S03",
  "title": "Fab Dispatch / Q-Time Global Flow",
  "core_question": "Can a local dispatch optimum violate downstream Q-time and global fab flow?",
  "twins_required": ["fab_operation", "factory_scene", "ai_audit"],
  "workload_profile": null,
  "fab_profile": "qtime_downstream_bottleneck",
  "mutation_type": null,
  "mutation_parameters": {},
  "visible_config": {
    "lot_a_qtime_remaining_min": 44,
    "lot_b_priority_score": 0.91,
    "tool_available_window_min": 18,
    "downstream_bottleneck_proxy": 0.42
  },
  "hidden_truth_ref": "oracle/hidden/S03.json"
}
```

Important: agents must route by `scenario_family`, not by `scenario_id` prefix.

### 3.2 Engine output object

Each twin must return an engine output.

```json
{
  "engine_name": "fab_operation_twin",
  "run_mode": "REAL_INTERNAL_RUN",
  "scenario_id": "S03",
  "scenario_family": "S03",
  "input_hash": "...",
  "engine_version": "v5.2",
  "raw_output_path": "outputs/engine_raw/fab_operation_twin-S03.json",
  "parsed_output_path": "outputs/engine_parsed/fab_operation_twin-S03.json",
  "metrics": {},
  "event_log": [],
  "claim_boundary": {
    "commercial_fab_control": false,
    "real_signoff_allowed": false,
    "public_model_only": true
  }
}
```

### 3.3 Evidence packet object

Evidence packet must be generated from engine outputs and public tool run receipts.

```json
{
  "scenario_id": "S03",
  "scenario_family": "S03",
  "evidence_packet_id": "S03-...",
  "visible_metrics": {},
  "engine_outputs": [
    {
      "engine_name": "fab_operation_twin",
      "run_mode": "REAL_INTERNAL_RUN",
      "parsed_output_path": "...",
      "metric_keys": ["qtime_trajectory", "q_over_risk", "event_log"]
    }
  ],
  "public_tool_receipts": [],
  "metric_lineage": {
    "q_over_risk": {
      "source_engine": "fab_operation_twin",
      "source_file": "outputs/engine_parsed/fab_operation_twin-S03.json",
      "formula_or_method": "qtime trajectory crossing threshold"
    }
  },
  "claim_boundary": {
    "approved_for_public_model_review": true,
    "real_signoff_allowed": false
  }
}
```

---

## 4. HBM / Memory System Twin internal implementation

### 4.1 Goal

This must not be a label or a static table. It must simulate HBM workload pressure under multiple scheduling policies and generate metrics used by AI Judges.

### 4.2 Core classes

```python
@dataclass
class HBMStackConfig:
    stack_name: str
    channels: int
    pseudo_channels_per_channel: int
    banks_per_pseudo_channel: int
    bank_groups: int
    io_width_bits: int
    data_rate_gbps_per_pin: float
    t_rcd_ns: float
    t_rp_ns: float
    t_cas_ns: float
    t_rfc_ns: float
    t_refi_ns: float
    read_write_turnaround_ns: float
    thermal_limit_c: float
    base_temperature_c: float
    power_limit_w: float

@dataclass
class WorkloadBurst:
    t_start_ns: int
    duration_ns: int
    read_ratio: float
    write_ratio: float
    locality: float
    burst_intensity: float
    row_reuse_probability: float

@dataclass
class HBMPolicy:
    name: str
    open_page: bool
    write_drain_threshold: float
    refresh_aware: bool
    thermal_throttle: bool
    bank_group_aware: bool
```

### 4.3 Required workloads

Implement `twin_core/hbm_memory/workloads.py` with:

```python
def llm_training_burst(seed: int) -> list[WorkloadBurst]
def llm_inference_latency(seed: int) -> list[WorkloadBurst]
def sustained_bandwidth_thermal(seed: int) -> list[WorkloadBurst]
def refresh_stress(seed: int) -> list[WorkloadBurst]
def read_write_turnaround_stress(seed: int) -> list[WorkloadBurst]
def bank_group_conflict_stress(seed: int) -> list[WorkloadBurst]
```

The generator must create at least 100 time windows per workload and must vary read/write ratio, locality, row reuse, and burst intensity.

### 4.4 Simulation algorithm

Implement `run_hbm_simulation(config, workload, policy)`.

For each time window:

1. create demand in bytes from burst intensity;
2. map memory requests to pseudo-channel, bank group, bank, row;
3. calculate row-buffer hit probability from locality and policy;
4. calculate bank conflict and bank-group conflict;
5. insert refresh penalty using `t_refi_ns` and `t_rfc_ns`;
6. calculate read/write turnaround loss from write ratio and policy;
7. calculate raw bandwidth and effective bandwidth;
8. update thermal pressure using bandwidth, write activity, and policy;
9. if thermal throttle is enabled, reduce sustained bandwidth after thermal pressure crosses threshold;
10. sample latency distribution and record p50/p95/p99.

### 4.5 Required output metrics

```json
{
  "theoretical_bandwidth_gbps": 3328.0,
  "effective_bandwidth_gbps": 2510.4,
  "sustained_bandwidth_gbps": 2198.7,
  "p50_latency_ns": 87.1,
  "p95_latency_ns": 155.2,
  "p99_latency_ns": 211.8,
  "row_hit_rate": 0.47,
  "bank_conflict_rate": 0.31,
  "bank_group_conflict_rate": 0.19,
  "refresh_overhead_pct": 6.8,
  "read_write_turnaround_loss_pct": 4.2,
  "thermal_pressure_index": 0.82,
  "power_pressure_index": 0.71,
  "hard_constraint_status": "REVIEW_ONLY",
  "policy_scores": {
    "FCFS": 0.51,
    "FR_FCFS": 0.69,
    "WRITE_DRAIN": 0.72,
    "THERMAL_SAFE": 0.78,
    "BALANCED": 0.81
  },
  "recommended_policy": "BALANCED"
}
```

### 4.6 Required tests

`tests/test_hbm_memory_twin.py`

Tests must verify:

1. thermal-safe policy lowers thermal pressure compared to bandwidth-only policy;
2. refresh-stress workload increases refresh overhead;
3. read/write turnaround stress increases turnaround loss;
4. bank-group conflict stress increases bank-group conflict rate;
5. policy recommendation changes when thermal pressure is weighted higher.

---

## 5. Circuit / Physical Proxy Twin implementation

### 5.1 Goal

This twin must produce margin evidence and clearly separate execution pass, proxy design pass, and real signoff.

### 5.2 Required calculations

Implement:

```python
def charge_share_delta_mv(cell_cap_fF, bitline_cap_fF, v_cell, v_precharge) -> float:
    # V_final = (C_cell*V_cell + C_bl*V_precharge) / (C_cell + C_bl)
    # delta = abs(V_final - V_precharge)


def sense_margin_mv(delta_v_mv, sense_amp_offset_mv, noise_sigma_mv, sigma_count=3) -> float:
    # margin = delta_v - offset - sigma_count*noise


def retention_margin_mv(initial_delta_mv, leakage_mv_per_ms, refresh_interval_ms, margin_floor_mv) -> float:
    # retained_delta = initial_delta - leakage*refresh_interval
    # margin = retained_delta - margin_floor
```

### 5.3 Required PVT/corner sweep

Implement `pvt_corner_sweep.py` with these corners:

```text
TT_25C
SS_85C
FF_0C
HOT_LEAKAGE_95C
LOW_VDD_85C
```

For each corner, vary:

```text
cell_cap_fF
bitline_cap_fF
vdd
sense_amp_offset_mv
noise_sigma_mv
leakage_mv_per_ms
refresh_interval_ms
```

### 5.4 Required ngspice integration

Files:

```text
public_tool_runs/ngspice/netlists/read_path_charge_sharing.sp
public_tool_runs/ngspice/netlists/retention_leakage_proxy.sp
public_tool_runs/ngspice/run_ngspice.py
public_tool_runs/ngspice/parse_ngspice.py
```

`run_ngspice.py` must attempt to execute:

```bash
ngspice -b <netlist> -o <log>
```

If ngspice is unavailable, the receipt must say `EXPLAINED_UNAVAILABLE`, not `REAL_EXTERNAL_RUN`.

### 5.5 Required output metrics

```json
{
  "charge_share_delta_mv": 18.7,
  "sense_margin_mv": 11.2,
  "retention_margin_mv": -3.4,
  "worst_corner": "HOT_LEAKAGE_95C",
  "proxy_execution_pass": true,
  "proxy_design_pass": false,
  "real_signoff_allowed": false,
  "ngspice_status": "REAL_EXTERNAL_RUN_OR_EXPLAINED_UNAVAILABLE",
  "corner_table": []
}
```

### 5.6 Required RTL/Yosys/Verilator proxy

Files:

```text
public_tool_runs/rtl/rtl/hbm_policy_controller.v
public_tool_runs/rtl/run_verilator_lint.py
public_tool_runs/rtl/run_yosys_synth.py
```

The RTL does not need to be product-grade. It should implement a small policy selector with:

```text
inputs: bandwidth_pressure, thermal_pressure, qtime_risk, margin_risk
outputs: selected_policy, requires_supervisor_gate
```

Yosys/Verilator runners must execute subprocess if tools exist.

---

## 6. Fab Operation Twin implementation

### 6.1 Goal

This is the core Hynix-aligned twin. It must be a real event simulation, not a list of made-up events.

### 6.2 Core classes

```python
@dataclass
class Lot:
    lot_id: str
    product_priority: float
    qtime_deadline_min: float
    current_step: str
    route: list[str]
    arrival_time: float
    qtime_start_time: float

@dataclass
class Tool:
    tool_id: str
    tool_type: str
    chamber_count: int
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
    delay_distribution_min: tuple[float, float]
    sample_rate: float
```

### 6.3 SimPy environment behavior

`twin_core/fab_operation/simpy_environment.py` must:

1. import `simpy`;
2. create `simpy.Environment()`;
3. create tool resources using `simpy.Resource`;
4. create lot processes with `env.process(lot_process(...))`;
5. run with `env.run(until=...)`;
6. emit structured event logs.

### 6.4 Required dispatch policies

Implement:

```python
class DispatchPolicy(Enum):
    PRIORITY_FIRST
    QTIME_FIRST
    BOTTLENECK_AWARE
    BALANCED
    MAINTENANCE_AWARE
```

### 6.5 Required event log

Each run must produce at least 50 events for canonical Fab scenarios.

Required event types:

```text
LOT_ARRIVAL
QUEUE_ENTER
QUEUE_EXIT
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
SUPERVISOR_REVIEW_REQUIRED
```

Each event:

```json
{
  "t": 42.0,
  "event": "DOWNSTREAM_QUEUE_UPDATE",
  "lot_id": "LOT_A",
  "tool_id": "ETCH_01",
  "details": {
    "qtime_remaining_min": 8.2,
    "downstream_bottleneck_score": 0.86
  }
}
```

### 6.6 Required metrics

```json
{
  "event_count": 84,
  "qtime_trajectory": [{"t": 0, "LOT_A": 44}, {"t": 57, "LOT_A": 6}],
  "q_over_risk": 0.78,
  "lot_priority_score": 0.91,
  "tool_utilization": 0.84,
  "queue_depth_max": 7,
  "chamber_health_score": 0.72,
  "sensor_drift_score": 0.36,
  "metrology_delay_min": 80,
  "downstream_bottleneck_score": 0.86,
  "maintenance_due_score": 0.73,
  "rework_probability": 0.18,
  "scrap_risk": 0.09,
  "yield_tail_risk": 0.66
}
```

---

## 7. Factory Scene / Routing Twin implementation

### 7.1 Goal

This twin gives visible digital-twin scene value. It should make the repo look like a factory digital twin, not just an algorithm report.

### 7.2 Layout model

`factory_scene/layout.py` must generate a 2D fab layout with coordinates.

```json
{
  "nodes": [
    {"id": "ETCH_01", "type": "tool", "x": 20, "y": 40},
    {"id": "MET_01", "type": "metrology", "x": 80, "y": 35},
    {"id": "BUF_01", "type": "buffer", "x": 50, "y": 55}
  ],
  "edges": [
    {"source": "ETCH_01", "target": "BUF_01", "distance": 30, "base_delay_min": 4.0}
  ]
}
```

### 7.3 Routing algorithm

Implement Dijkstra or A*.

Edge cost:

```text
cost = base_delay + distance_weight*distance + congestion_weight*congestion + qtime_weight*qtime_pressure
```

### 7.4 OpenUSD-like export

Generate a `.usda` file such as:

```text
#usda 1.0

def Xform "FAB" {
    def Xform "ETCH_01" {
        double3 xformOp:translate = (20, 40, 0)
    }
}
```

This is not a real Omniverse claim. It is an OpenUSD-like public-model scene export.

### 7.5 Dashboard requirements

Factory scene dashboard must show:

1. tool nodes;
2. transport edges;
3. selected route;
4. congestion zones;
5. route delay before/after dispatch;
6. link to scene graph JSON and `.usda` export.

---

## 8. Public tool run design

### 8.1 Required public tool runners

Implement these as actual attempts, not fake status.

```text
public_tool_runs/ngspice/run_ngspice.py
public_tool_runs/rtl/run_yosys_synth.py
public_tool_runs/rtl/run_verilator_lint.py
public_tool_runs/simpy/run_simpy_fab.py
```

### 8.2 Receipt schema

```json
{
  "tool": "ngspice",
  "status": "REAL_EXTERNAL_RUN | EXPLAINED_UNAVAILABLE",
  "command": [],
  "returncode": 0,
  "executable_path": "...",
  "version_stdout": "...",
  "stdout_path": "...",
  "stderr_path": "...",
  "log_path": "...",
  "parsed_metrics_path": "...",
  "input_sha256": "...",
  "log_sha256": "...",
  "claim_boundary": {
    "public_tool_proxy_only": true,
    "real_signoff_allowed": false
  }
}
```

---

## 9. AI Judgment Audit implementation

### 9.1 Evidence-sensitive judges

`agents/rule_based_judges.py` must implement:

```python
def judge_hbm_thermal(packet): ...
def judge_memory_ppa(packet): ...
def judge_fab_dispatch(packet): ...
def judge_observability(packet): ...
def judge_yield_tail(packet): ...
def judge_proxy_signoff(packet): ...
```

Each judge must read `packet["visible_metrics"]` and must change output when key metrics change.

### 9.2 Required judge outputs

```json
{
  "scenario_id": "S02",
  "scenario_family": "S02",
  "judge": "MemoryPPAJudge",
  "decision": "REJECT_BANDWIDTH_OPTIMIZED_CANDIDATE",
  "confidence": 0.78,
  "visible_evidence_used": ["retention_margin_mv", "sense_margin_mv", "effective_bandwidth_gbps"],
  "rule_trace": [
    "Candidate A bandwidth score highest",
    "Candidate A retention margin below floor",
    "Hard constraint dominates bandwidth objective"
  ],
  "claim_requested": "Candidate B is safer in the public-model proxy twin",
  "known_limits": ["not real product signoff"]
}
```

### 9.3 Red-team behavior

Red-team must flag 4 or 5 canonical scenarios, not all 6.

Use a deterministic miss policy, e.g.:

```python
if scenario_family == "S01" and evidence["thermal_model_freshness"] == "stale_but_not_visible":
    caught = False
```

### 9.4 Virtual supervisor

Always output:

```json
{
  "approved_claim": "... public-model only ...",
  "blocked_claim": "... real fab/product claim ...",
  "requires_real_signoff": true,
  "human_impersonation": false
}
```

---

## 10. Canonical scenarios as product cards

### S01 HBM Thermal-Bandwidth Boundary

Twins: HBM Memory, Circuit/Physical optional, AI Audit.

Must show:

1. short-term bandwidth improves under aggressive policy;
2. sustained bandwidth degrades under thermal pressure;
3. red-team misses or partially misses stale thermal boundary;
4. hidden truth reveal explains model-boundary failure.

### S02 Memory PPA Hard Constraint

Twins: HBM Memory, Circuit/Physical, AI Audit.

Must show:

1. bandwidth-optimized candidate looks attractive;
2. retention/sense margin violates floor under corner;
3. judge rejects or downgrades candidate after hard-constraint check;
4. supervisor blocks product-level claim.

### S03 Fab Dispatch / Q-Time Global Flow

Twins: Fab Operation, Factory Scene, AI Audit.

Must show:

1. LOT B local priority looks better;
2. LOT A downstream Q-time trajectory crosses risk threshold;
3. factory route delay contributes to risk;
4. supervisor requests fab engineer review.

### S04 Tool-Chamber Observability / Metrology Lag

Twins: Fab Operation, Factory Scene optional, AI Audit.

Must show:

1. chamber health score looks acceptable;
2. sensor drift and metrology lag hide degradation;
3. maintenance delay looks locally rational;
4. hidden truth reveal shows observability failure.

### S05 Process Recipe / Yield-Tail Risk

Twins: Fab Operation, Circuit/Physical optional, AI Audit.

Must show:

1. average defect proxy improves;
2. p99/tail risk worsens;
3. pilot expansion claim is blocked;
4. dashboard displays average vs tail divergence.

### S06 Proxy Evidence / Signoff Boundary

Twins: HBM Memory, Circuit/Physical, public tool runs, AI Audit.

Must show:

1. public tool/proxy execution passes;
2. proxy design may still fail or remain limited;
3. real signoff claim is blocked;
4. supervisor rewrites claim into public-model evidence only.

---

## 11. Variant and mutation lab

Generate at least 60 variants.

Variant fields:

```json
{
  "scenario_id": "V001_S01",
  "scenario_family": "S01",
  "canonical_parent": "S01",
  "mutation_type": "thermal_pressure_sweep",
  "mutation_parameters": {
    "thermal_limit_c": 82,
    "burst_intensity_scale": 1.25
  }
}
```

Required mutation families:

```text
S01: thermal limit, burst intensity, refresh overhead
S02: retention floor, sense amp offset, bandwidth gain
S03: qtime deadline, downstream bottleneck, route congestion
S04: sensor drift, metrology delay, maintenance window
S05: average defect improvement, p99 tail risk, wafer-edge risk
S06: proxy pass/fail, external tool availability, signoff boundary
```

Variant dashboard must show a heatmap by parent scenario.

---

## 12. Dashboard implementation

### 12.1 Dashboard data

`outputs/dashboard_data.json` must include:

```json
{
  "architecture": {},
  "hbm_workload": {},
  "circuit_physical": {},
  "fab_operation": {},
  "factory_scene": {},
  "ai_audit": {},
  "variant_matrix": {},
  "public_tool_evidence": {},
  "hynix_alignment": {}
}
```

### 12.2 Dashboard pages

Do not build one generic summary page only. Build specific sections:

1. Architecture
2. HBM Workload
3. Circuit/Physical Proxy
4. Fab Operation Timeline
5. Factory Scene/Routing
6. Public Tool Evidence
7. AI Audit Flow
8. Variant Matrix
9. Hynix Alignment

### 12.3 Screenshot rendering

`scripts/render_dashboard_screenshots.py` must read `outputs/dashboard_data.json` and generate data-backed images. It may use matplotlib/Pillow or browser automation. The screenshots must contain real metrics from dashboard data.

---

## 13. Documentation requirements

Docs must explain the implementation, not merely name modules.

### 13.1 `docs/03_HYNIX_ALIGNMENT.md`

Required sections:

1. Autonomous Fab interpretation
2. Digital Twin interpretation
3. Q-time / LOT priority implementation
4. HBM workload implementation
5. Factory scene/routing implementation
6. AI judgment audit implementation
7. Evidence map from repo files to Hynix relevance
8. Non-claims

### 13.2 `docs/11_IMPLEMENTATION_EVIDENCE.md`

Required sections:

1. Run profile summary
2. Internal engine summary
3. Public tool run summary
4. Scenario coverage
5. Variant/mutation coverage
6. Evidence packet lineage
7. Dashboard/screenshots
8. Validation summary
9. Known limitations

---

## 14. Make targets

Required Make targets:

```makefile
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
make validate
make validate-medium
make package-release
make verify-clean-unzip
```

`demo-medium` should run at least:

1. HBM internal engine
2. Circuit/physical internal engine
3. Fab SimPy engine
4. Factory scene engine
5. ngspice attempt
6. Yosys/Verilator attempt
7. dashboard build
8. screenshot generation
9. validation

---

## 15. Final GPT Pro handoff prompt

Use this prompt with GPT Pro.

```text
첨부한 문서는 조건 목록이 아니라, 최종 구현해야 하는 제품의 내부 설계도다.

이번 목표는 validator를 통과하는 패키지가 아니라, GitHub에서 실제로 보이는 `Hynix Autonomous Fab × HBM Digital Twin Console`을 구현하는 것이다.

GPT Pro의 역할은 이 설계도를 줄이거나 재해석하는 것이 아니라, Codex가 구현할 수 있는 작업 티켓으로 변환하는 것이다. 각 티켓은 반드시 다음을 포함해야 한다:

1. 구현할 파일 경로
2. 구현할 class/function
3. 입력 데이터 구조
4. 출력 데이터 구조
5. dashboard 연결 위치
6. 테스트/검증 방법
7. 완료 기준

특히 다음 5개 본체는 이름표만 붙이지 말고 실제 내부 로직을 구현해야 한다.

1. HBM / Memory System Twin
   - workload generator
   - scheduler/policy comparison
   - refresh/turnaround/thermal model
   - bandwidth/latency/conflict metrics

2. Circuit / Physical Proxy Twin
   - charge-sharing model
   - sense/retention margin model
   - PVT/corner sweep
   - ngspice netlist generator and runner
   - proxy execution vs proxy design vs real signoff boundary

3. Fab Operation Twin
   - SimPy environment
   - lots/tools/chambers/process steps
   - dispatch policy
   - Q-time trajectory
   - metrology lag
   - sensor drift
   - maintenance decision
   - yield-tail risk

4. Factory Scene / Routing Twin
   - 2D fab layout
   - routing graph
   - congestion penalty
   - Dijkstra/A* route optimization
   - OpenUSD-like scene export

5. AI Judgment Audit Layer
   - evidence-sensitive rule-based judges
   - red-team partial miss
   - meta judge
   - virtual supervisor claim boundary
   - hidden truth reveal

이 문서를 기준으로 Phase별 Codex 작업 지시서를 만들어라. 단순히 금지조건이나 validator를 추가하는 것이 아니라, 위 제품이 실제로 구현되도록 작업을 분해하라.
```

---

## 16. Final target sentence

The finished repo should be describable as:

> A heavy GitHub repository implementing a public-model HBM workload and Fab operation digital twin console aligned with SK hynix Autonomous Fab direction, with executable HBM, circuit/physical, fab operation, and factory routing twins, public-tool run receipts, evidence lineage, AI judgment audit, dashboard, and screenshots.

