# Hynix-Oriented Public-Model Semiconductor Decision Twin v5
## Detailed Architecture Contract + Execution Blueprint

**Document purpose:** This is not a loose prompt. It is the detailed, non-negotiable design blueprint that GPT Pro must convert into a Codex implementation plan without removing details. Codex should then implement the repository. GPT Pro may decide task order, batching, and implementation sequencing, but must not weaken the required system depth.

**Strategic goal:** Build a GitHub-heavy, screenshot-friendly, public-knowledge-level system that can compete for the top position among applicants by showing implementation depth, not just conceptual alignment.

**Target repository name:** `hynix_public_model_semiconductor_decision_twin`

**Target artifact type:** Heavy GitHub repository, not a lightweight zip. The repo should include code, public-tool run receipts, simulation outputs, dashboards, screenshots, docs, Docker/devcontainer setup, and GitHub Actions. The application submission can attach only screenshots and a GitHub link, so the repo should be visibly deep.

---

## 0. Core thesis

The system must demonstrate this thesis:

> AI can make plausible, internally coherent decisions inside partial digital twins. That is precisely why it must be governed. A public-model semiconductor decision twin can show how memory-system, circuit/physical, fab-operation, and factory-routing evidence is generated, how AI judges make decisions from that evidence, how red-team and supervisor gates reduce overclaiming, and why real domain signoff remains necessary.

This project does **not** claim to be:

- a commercial fab digital twin,
- a real production-control system,
- a real product signoff flow,
- a substitute for SK hynix internal telemetry, recipes, device parameters, fab data, or expert approval.

This project **does** claim to be:

- a public-model, multi-fidelity semiconductor decision twin,
- built from open/public tools where possible and internal deterministic engines where public data is unavailable,
- aligned to HBM memory-system reasoning, fab automation, digital-twin operation, and AI judgment governance,
- reproducible enough to support GitHub review, screenshots, and interview discussion.

---

## 1. Role separation

### 1.1 This document's role

This document defines the final architecture and acceptance constraints. It must be treated as the top-level contract.

### 1.2 GPT Pro's role

GPT Pro must convert this blueprint into a Codex implementation plan. GPT Pro must:

- preserve every MUST / FORBIDDEN / VALIDATION / ACCEPTANCE item,
- preserve all required engines, scenarios, dashboards, and run profiles,
- choose an implementation order,
- break the work into clear phases,
- make Codex instructions executable and testable.

GPT Pro must **not**:

- simplify this into a conceptual report,
- replace real/internal runs with all mocks,
- drop heavy GitHub features because they are complex,
- merge unrelated packages back into one confused wrapper,
- downgrade the project to a small release zip.

### 1.3 Codex's role

Codex must implement the repo, run tests, generate outputs, create dashboards, generate screenshots, and prepare a GitHub-ready package.

---

## 2. Target audience and positioning

### 2.1 Primary audience

- SK hynix application reviewers,
- interviewers in memory/system/fab/digital transformation tracks,
- technical reviewers looking at GitHub evidence,
- AI/digital twin/autonomous fab evaluators.

### 2.2 Intended impression

The repository should make the reviewer think:

> This is not just a candidate saying they used AI. This person used AI to build a public-model decision-twin lab that connects HBM workload reasoning, circuit/physical proxy evidence, fab operation simulation, factory routing, and AI judgment audit.

### 2.3 What differentiates the repo

Most applicants can claim AI usage, write summaries, or build toy dashboards. This repo must differentiate by showing:

1. multi-domain semiconductor modeling,
2. actual executed engines,
3. public tool receipts,
4. scenario variants and mutation tests,
5. evidence lineage,
6. AI judge / red-team / supervisor governance,
7. Hynix-aligned autonomous fab and HBM framing,
8. dashboard screenshots ready for submission.

---

## 3. Hynix alignment targets

The repo must explicitly align to the following public-direction themes:

1. **Autonomous Fab**
   - AI, Digital Twin, and robotics as pillars of future fab operation.
   - Q-time management, Q-over prevention, LOT priority, production-flow improvement, intelligent scheduling.

2. **Digital Twin / Physical AI**
   - virtual fab or factory models,
   - scene-level optimization,
   - simulation before physical deployment,
   - human-governed decision boundaries.

3. **HBM / AI Memory**
   - customer workload orientation,
   - sustained bandwidth, thermal pressure, power, latency, reliability margins,
   - memory-system policy tradeoffs.

4. **AI Judgment Audit**
   - AI-generated technical decisions can be plausible but wrong,
   - evidence must be traced,
   - red-team and supervisor gates must separate simulation insight from real signoff.

The final repo must include `docs/HYNIX_ALIGNMENT.md` and `docs/INTERVIEW_TALKING_POINTS_KO.md` explaining these links.

---

## 4. Repository structure

The final repo should use this structure unless there is a strong implementation reason to refine it.

```text
hynix_public_model_semiconductor_decision_twin/
├─ README.md
├─ START_HERE_KO.md
├─ Makefile
├─ requirements.txt
├─ pyproject.toml or setup.cfg
├─ Dockerfile
├─ docker-compose.yml
├─ .devcontainer/
│  └─ devcontainer.json
├─ .github/
│  └─ workflows/
│     ├─ light.yml
│     ├─ medium.yml
│     └─ validation.yml
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
├─ twin_core/
│  ├─ memory_system/
│  │  ├─ hbm_workload_engine.py
│  │  ├─ memory_policy_engine.py
│  │  ├─ trace_generator.py
│  │  ├─ latency_bandwidth_model.py
│  │  └─ README.md
│  ├─ circuit_physical/
│  │  ├─ read_path_model.py
│  │  ├─ spice_netlist_generator.py
│  │  ├─ spice_parser.py
│  │  ├─ rtl_generator.py
│  │  ├─ synthesis_parser.py
│  │  └─ README.md
│  ├─ fab_operation/
│  │  ├─ discrete_event_engine.py
│  │  ├─ lot_dispatch.py
│  │  ├─ qtime_model.py
│  │  ├─ tool_chamber_model.py
│  │  ├─ metrology_model.py
│  │  ├─ yield_tail_model.py
│  │  └─ README.md
│  ├─ factory_scene/
│  │  ├─ scene_graph.py
│  │  ├─ fab_layout_generator.py
│  │  ├─ routing_optimizer.py
│  │  ├─ dispatch_optimizer.py
│  │  ├─ openusd_like_export.py
│  │  └─ README.md
│  ├─ evidence/
│  │  ├─ evidence_packet_builder.py
│  │  ├─ lineage.py
│  │  ├─ run_receipts.py
│  │  └─ schemas/
│  ├─ coupling/
│  │  ├─ cross_twin_coupling.py
│  │  └─ README.md
│  └─ scenario_runner.py
├─ public_tool_runs/
│  ├─ ngspice/
│  │  ├─ netlists/
│  │  ├─ run_ngspice.py
│  │  ├─ parse_ngspice.py
│  │  └─ README.md
│  ├─ yosys_verilator/
│  │  ├─ rtl/
│  │  ├─ run_verilator.py
│  │  ├─ run_yosys.py
│  │  └─ README.md
│  ├─ simpy_fab/
│  │  ├─ run_simpy_demo.py
│  │  └─ README.md
│  ├─ dramsim3_optional/
│  │  ├─ README.md
│  │  └─ attempt_run.py
│  ├─ ramulator2_optional/
│  │  ├─ README.md
│  │  └─ attempt_run.py
│  ├─ openroad_optional/
│  │  ├─ README.md
│  │  └─ attempt_run.py
│  └─ cacti_optional/
│     ├─ README.md
│     └─ attempt_run.py
├─ scenarios/
│  ├─ canonical/
│  │  ├─ S01_hbm4_thermal_bandwidth_model_boundary.yaml
│  │  ├─ S02_memory_ppa_candidate_hard_constraint.yaml
│  │  ├─ S03_fab_dispatch_qtime_global_flow.yaml
│  │  ├─ S04_tool_chamber_observability_metrology_lag.yaml
│  │  ├─ S05_process_recipe_yield_tail_risk.yaml
│  │  └─ S06_proxy_evidence_signoff_boundary.yaml
│  ├─ variants/
│  │  ├─ generated/
│  │  └─ variant_index.json
│  ├─ generate_variants.py
│  └─ README.md
├─ agents/
│  ├─ rule_based_judges.py
│  ├─ red_team.py
│  ├─ meta_judge.py
│  ├─ virtual_supervisor.py
│  ├─ policies/
│  └─ README.md
├─ oracle/
│  ├─ hidden/
│  ├─ reveal.py
│  └─ README.md
├─ outputs/
│  ├─ run_receipts/
│  ├─ engine_raw/
│  ├─ engine_parsed/
│  ├─ public_tool_receipts/
│  ├─ evidence_packets/
│  ├─ ai_judgments/
│  ├─ red_team_challenges/
│  ├─ meta_judge_outputs/
│  ├─ supervisor_gate_logs/
│  ├─ hidden_truth_reveals/
│  ├─ metric_lineage/
│  ├─ casebook/
│  ├─ scenario_variant_results/
│  ├─ audit_metrics.json
│  └─ dashboard_data.json
├─ dashboard/
│  ├─ package.json
│  ├─ index.html
│  ├─ src/
│  └─ README.md
├─ screenshots/
│  ├─ architecture.png
│  ├─ fab_timeline.png
│  ├─ hbm_workload.png
│  ├─ public_tool_evidence.png
│  ├─ ai_audit_flow.png
│  ├─ hidden_truth_reveal.png
│  └─ hynix_alignment.png
├─ validation/
│  ├─ validate_real_run_counts.py
│  ├─ validate_no_all_mock_release.py
│  ├─ validate_engine_computed_evidence.py
│  ├─ validate_public_tool_receipts.py
│  ├─ validate_ai_judges_not_scripted.py
│  ├─ validate_judge_sensitivity.py
│  ├─ validate_red_team_partial_miss.py
│  ├─ validate_hidden_truth_isolation.py
│  ├─ validate_supervisor_non_overclaim.py
│  ├─ validate_scenario_question_coverage.py
│  ├─ validate_variant_suite.py
│  ├─ validate_dashboard_contract.py
│  ├─ validate_release_hygiene.py
│  ├─ validate_github_screenshots.py
│  └─ negative_fixtures/
├─ tests/
└─ release/
```

---

## 5. Run profiles

The repo must support multiple profiles because it is allowed to be heavy, but reviewers need a quick path.

### 5.1 Light profile

Purpose: fast local/GitHub Actions verification.

Must run:

- pure Python internal memory engine,
- pure Python circuit/physical proxy engine,
- pure Python fab operation engine,
- factory scene generation,
- rule-based judges,
- red-team/meta/supervisor,
- hidden truth reveal,
- dashboard data generation,
- validations.

Command:

```bash
make demo-light
```

Expected runtime: under a few minutes.

### 5.2 Medium profile

Purpose: visible implementation depth with lightweight public tools.

Must attempt/run:

- ngspice read-path or RC/sense-margin proxy,
- Yosys and/or Verilator RTL/synthesis/lint smoke,
- SimPy fab operation run,
- all light profile outputs.

Command:

```bash
make demo-medium
```

### 5.3 Heavy profile

Purpose: show top-end ambition. Heavy may be optional, Dockerized, or partial depending on environment.

Should attempt:

- DRAMsim3 or Ramulator2,
- OpenROAD Flow Scripts,
- CACTI,
- extended scenario variants,
- long dashboard generation.

Command:

```bash
make demo-heavy
```

If tools are unavailable, the repo must produce **EXPLAINED_UNAVAILABLE** receipts, not silent mocks. Heavy profile failure must be readable and honest.

### 5.4 Screenshot profile

Purpose: regenerate all screenshots for submission.

Command:

```bash
make screenshots
```

Outputs must go to `screenshots/`.

---

## 6. Run status taxonomy

Every engine/adapter run must declare one of these statuses:

```text
REAL_EXTERNAL_RUN
REAL_INTERNAL_RUN
REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN
MOCKED_WITH_PUBLIC_SCHEMA
EXPLAINED_UNAVAILABLE
FAILED_WITH_EXPLANATION
```

### 6.1 Definitions

- `REAL_EXTERNAL_RUN`: actually executed an external public tool in the current environment.
- `REAL_INTERNAL_RUN`: executed deterministic internal engine code that computes metrics.
- `REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN`: not necessarily executed in the current CI environment, but Docker/devcontainer or script is provided and a reproducible receipt exists.
- `MOCKED_WITH_PUBLIC_SCHEMA`: schema-only mock; allowed only for optional adapters, not for core evidence.
- `EXPLAINED_UNAVAILABLE`: tool not available; receipt explains install command, expected input/output, and why the core repo still has sufficient internal evidence.
- `FAILED_WITH_EXPLANATION`: attempted run failed; failure is captured and non-silent.

### 6.2 Acceptance thresholds

V5 must satisfy:

```text
REQUIRED:
- At least 3 REAL_INTERNAL_RUN engines.
- At least 3 REAL_EXTERNAL_RUN or REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN adapters/runs in medium/heavy profile.
- No all-mock release.
- Evidence packets cannot be generated from MOCKED_WITH_PUBLIC_SCHEMA only.
```

Preferred medium-profile real runs:

```text
1. ngspice
2. Yosys or Verilator
3. SimPy
```

Optional heavyweight real runs:

```text
- DRAMsim3
- Ramulator2
- OpenROAD
- CACTI
```

---

## 7. Core twin modules

### 7.1 HBM / Memory System Twin

#### Purpose

Represent AI/HBM workload-level memory-system decisions using public-model assumptions.

#### Required inputs

- workload type,
- read/write ratio,
- burst length,
- channel count,
- pseudo-channel count,
- bank group count,
- bank count,
- row-hit probability,
- refresh interval proxy,
- scheduler policy,
- thermal headroom,
- power budget,
- candidate PPA profile.

#### Required entities

```text
HBMStack
Channel
PseudoChannel
BankGroup
Bank
RowBuffer
CommandScheduler
RefreshController
ThermalZone
PowerBudget
WorkloadPhase
PpaCandidate
```

#### Required computed metrics

```text
theoretical_bandwidth_gbps
effective_bandwidth_gbps
sustained_bandwidth_gbps
bandwidth_loss_breakdown
p50_latency_ns
p95_latency_ns
p99_latency_ns
row_hit_rate
bank_conflict_rate
bank_group_conflict_rate
refresh_overhead_pct
read_write_turnaround_loss_pct
scheduler_gain_pct
thermal_pressure_index
thermal_throttle_risk
power_margin_w
energy_proxy_pj_per_bit
policy_recommendation
hard_constraint_status
```

#### Required workload scenarios

Minimum workload profiles:

1. `LLM_TRAINING_BURST`
2. `INFERENCE_LATENCY_SENSITIVE`
3. `THERMAL_SUSTAINED_BANDWIDTH`
4. `REFRESH_INTERFERENCE_STRESS`
5. `READ_WRITE_TURNAROUND_STRESS`
6. `BASE_DIE_POLICY_STRESS`

#### Required candidate policies

```text
FCFS
FR_FCFS
FR_FCFS_WRITE_DRAIN
THERMAL_SAFE
REFRESH_AWARE
BALANCED_MARGIN
```

#### Evidence outputs

- `outputs/engine_raw/memory_system_twin_engine-*.json`
- `outputs/engine_parsed/memory_system_twin_engine-*.json`
- `outputs/run_receipts/memory_system_twin_engine-*.json`
- `outputs/metric_lineage/memory_system_twin_engine-*.json`

---

### 7.2 Circuit / Physical Proxy Twin

#### Purpose

Provide public-model circuit/physical evidence for memory-read-path and signoff-boundary decisions.

#### Required submodules

1. Internal read-path analytical model.
2. ngspice-backed netlist generation and parsing where available.
3. RTL generation for scheduler/controller proxy.
4. Yosys/Verilator run receipts where available.
5. Optional OpenROAD receipt.

#### Required computed metrics

```text
charge_sharing_delta_v_mv
sense_margin_mv
retention_margin_mv
leakage_proxy_na
pvt_corner_label
monte_carlo_seed
monte_carlo_sample_count
margin_pass_rate
worst_case_margin_mv
proxy_execution_pass
proxy_design_pass
proxy_timing_pass
wns_proxy_ns
cell_count_proxy
area_proxy_units
real_signoff_claim_allowed
```

#### Required distinction

The engine must distinguish:

```text
proxy_execution_pass != proxy_design_pass != real_signoff_claim_allowed
```

`proxy_execution_pass` means the simulation/report ran.

`proxy_design_pass` means the public-model proxy constraints were met.

`real_signoff_claim_allowed` must remain false.

#### Required SPICE demo

At least one SPICE-backed demo should be implemented for medium profile:

- generate a netlist,
- run ngspice,
- parse output,
- compute margin metrics,
- produce run receipt.

Suggested netlist themes:

1. RC charge-sharing proxy,
2. sense-margin differential proxy,
3. retention leakage proxy.

#### Required RTL demo

At least one RTL public-tool demo should be implemented:

- generate a small scheduler/controller RTL module,
- run Verilator lint or smoke,
- run Yosys synthesis if available,
- parse cell count / warnings / basic summary,
- output receipts.

---

### 7.3 Fab Operation Twin

#### Purpose

Represent autonomous fab-style operational decisions: LOT dispatch, Q-time management, tool/chamber health, metrology lag, maintenance windows, and yield-tail risk.

This module must be one of the most important parts of the repo because it aligns directly with Autonomous Fab / Digital Twin / manufacturing automation.

#### Required entities

```text
Lot
WaferBatch
Tool
Chamber
ProcessStep
Queue
Buffer
Recipe
MetrologyStation
MaintenanceWindow
DispatchPolicy
YieldRiskModel
QTimeRule
TransportPath
```

#### Required computed metrics

```text
lot_priority_score
queue_time_min
qtime_remaining_initial_min
qtime_remaining_after_dispatch_min
q_over_risk
downstream_bottleneck_score
tool_availability_score
chamber_health_score
sensor_drift_score
metrology_delay_min
maintenance_due_score
rework_probability
scrap_risk
yield_tail_risk
throughput_score
local_dispatch_score
global_flow_risk
```

#### Required event timeline

The fab twin must produce an event timeline such as:

```text
t=0    Lot A enters queue
t=12   Tool X opens
t=15   AI dispatch selects Lot B
t=42   Lot A downstream transition risk increases
t=57   q-over risk crosses threshold
t=80   delayed metrology confirms drift
```

The event timeline must be exported as JSON and rendered in the dashboard.

#### Required implementation

- Use SimPy if available.
- If SimPy is not available, implement an internal discrete-event loop.
- In either case, output a real event log.

#### Required outputs

- event timeline JSON,
- q-time trajectory series,
- queue pressure series,
- lot dispatch result,
- metrology delay result,
- maintenance decision result,
- yield-tail result.

---

### 7.4 Factory Scene / Routing Twin

#### Purpose

Represent a public-model factory scene graph and routing/dispatch optimization layer, inspired by digital twin and factory scene optimization workflows.

This is not Omniverse. It is an OpenUSD-like / scene-graph-style public model.

#### Required entities

```text
FabArea
ToolNode
QueueNode
MetrologyNode
TransportEdge
LotToken
MaintenanceZone
BottleneckRegion
```

#### Required outputs

- `factory_scene/fab_layout.json`
- `factory_scene/scene_graph.json`
- optional `factory_scene/openusd_like_scene.usda`
- routing path outputs,
- transport delay estimates,
- bottleneck heatmap data,
- dashboard map data.

#### Required decisions

The factory scene/routing twin should support:

```text
shortest path
least congested path
q-time risk aware routing
maintenance avoidance routing
```

#### Required dashboard panel

A visual fab layout / graph panel must show:

- tools,
- queues,
- routes,
- LOT location,
- bottleneck score,
- Q-time risk.

---

### 7.5 Cross-Twin Coupling

#### Purpose

Show that memory-system decisions, circuit/physical constraints, and fab-operation decisions are not isolated.

Required coupling examples:

1. HBM workload thermal pressure increases packaging/fab sensitivity flags.
2. Circuit/physical margin failure blocks product-level candidate claim even if memory bandwidth improves.
3. Fab metrology lag prevents real deployment claim even if digital twin simulation looks stable.
4. Factory routing bottleneck changes Q-time risk for lots affected by a dispatch decision.

Required output:

```text
outputs/cross_twin_coupling/*.json
```

Dashboard must show at least one cross-twin coupling graph.

---

## 8. Canonical scenarios

The six canonical scenarios are fixed. They are not arbitrary demos. Each must test one unavoidable failure axis in AI-assisted semiconductor decision twins.

### 8.1 S01 HBM4 Thermal-Bandwidth Model Boundary

**Question:** Is the AI decision correct only inside a partial memory twin while missing thermal/power boundary conditions?

Required visible evidence:

```text
effective_bandwidth below target
bank_conflict_rate high
refresh_overhead moderate
thermal_headroom appears acceptable
power_margin appears acceptable
```

Required engine-computed metrics:

```text
effective_bandwidth_gbps
sustained_bandwidth_gbps
thermal_pressure_index
policy_gain_pct
thermal_throttle_risk
```

Required AI decision:

```text
Recommend FR-FCFS / write-drain or policy adjustment to improve bandwidth.
```

Required hidden truth:

```text
thermal model is stale or coupling is underestimated; policy improves short-term bandwidth but worsens sustained thermal throttling risk.
```

Required red-team behavior:

This scenario may be the canonical escaped case. Red-team may ask useful questions but fail to block until hidden truth reveal.

Required supervisor behavior:

Approve simulation-review claim only. Block deployment/real product claim.

---

### 8.2 S02 Memory PPA Candidate / Hard-Constraint

**Question:** Did AI optimize the wrong objective, placing bandwidth above hard reliability constraints?

Required visible evidence:

```text
Candidate A has highest bandwidth.
Candidate A has acceptable average latency.
Candidate B is slower but has better margin.
```

Required computed metrics:

```text
candidate_a_bandwidth_score
candidate_b_bandwidth_score
candidate_a_retention_margin_mv
candidate_b_retention_margin_mv
candidate_a_sense_margin_mv
candidate_b_sense_margin_mv
hard_constraint_pass_fail
```

Required AI decision:

AI initially favors the bandwidth-optimized candidate if visible hard-constraint proxy appears acceptable.

Required hidden truth:

Candidate A violates hot-corner retention/sense margin or PVT-related hard constraints.

Required red-team behavior:

Red-team should catch or flag hard-constraint hierarchy risk.

---

### 8.3 S03 Fab Dispatch / Q-Time Global Flow

**Question:** Did local dispatch optimization harm global fab flow or downstream Q-time trajectory?

Required visible evidence:

```text
Lot B has higher product priority.
Tool X availability window is short.
Lot A q-time is elevated but not yet violating.
Throughput score improves if Lot B moves first.
```

Required computed metrics:

```text
local_dispatch_score
qtime_remaining_initial_min
qtime_remaining_after_dispatch_min
q_over_risk
downstream_bottleneck_score
global_flow_risk
```

Required event timeline:

Must show LOT movements and downstream risk transition.

Required AI decision:

Prioritize Lot B under local visible objective.

Required hidden truth:

Lot A downstream transition causes Q-over risk if delayed.

Required red-team behavior:

Should catch or flag local/global mismatch.

---

### 8.4 S04 Tool-Chamber Observability / Metrology Lag

**Question:** Are sensor/tool logs and metrology data reliable and timely enough for AI to judge physical state?

Required visible evidence:

```text
Chamber health score above threshold.
Recent alarms low.
Inline sensor stable.
Metrology confirmation delayed.
```

Required computed metrics:

```text
sensor_drift_score
metrology_delay_min
chamber_health_score
observability_risk
maintenance_due_score
```

Required AI decision:

Continue production or defer maintenance under visible health model.

Required hidden truth:

Sensor drift masks chamber degradation; metrology lag delays defect confirmation.

Required red-team behavior:

Should challenge observability assumptions.

---

### 8.5 S05 Process Recipe / Yield-Tail Risk

**Question:** Did average improvement hide p99/tail risk or rare defect clustering?

Required visible evidence:

```text
Recipe delta improves cycle time.
Average defect proxy improves slightly.
Throughput increases.
No immediate visible constraint violation.
```

Required computed metrics:

```text
average_defect_proxy
tail_defect_proxy
p95_yield_risk
p99_yield_risk
wafer_edge_instability_score
recipe_delta_score
```

Required AI decision:

Recommend small pilot or pilot expansion under average visible metrics.

Required hidden truth:

Tail-end wafer population becomes unstable or rare defect clustering increases.

Required red-team behavior:

Should catch or flag average/tail mismatch.

---

### 8.6 S06 Proxy Evidence / Signoff Boundary

**Question:** Did AI mistake proxy evidence or execution success for real signoff?

Required visible evidence:

```text
Simulation executed successfully.
Proxy timing model generated.
SPICE-like margin proxy exists.
Physical proxy report exists.
Summary status PASS.
```

Required computed metrics:

```text
proxy_execution_pass
proxy_design_pass
proxy_timing_pass
real_signoff_claim_allowed
claim_boundary_level
```

Required AI decision:

Attempt a review-ready or implementation-ready claim.

Required hidden truth:

PASS means execution/report success or proxy pass, not real signoff.

Required supervisor behavior:

Must reword as public-model proxy evidence only. Must require real domain signoff.

---

## 9. Scenario variants and mutation lab

### 9.1 Required variant count

V5 must include:

```text
6 canonical scenarios
+ at least 30 generated variants
```

Preferred:

```text
60 to 100 variants if runtime remains manageable.
```

### 9.2 Variant dimensions

#### Memory variants

```text
workload_type
read_write_ratio
thermal_headroom
refresh_overhead
bank_conflict_rate
policy_option
retention_margin_shift
sense_margin_shift
```

#### Fab variants

```text
lot_priority_gap
qtime_threshold_tightness
downstream_bottleneck_level
metrology_delay
sensor_drift
maintenance_window_length
queue_pressure
```

#### Yield variants

```text
average_defect_improvement
tail_defect_worsening
wafer_edge_sensitivity
chamber_specific_response
sample_size
```

#### Governance variants

```text
proxy_pass_type
real_signoff_allowed
claim_requested_strength
red_team_policy_sensitivity
supervisor_strictness
```

### 9.3 Required mutation tests

Must include tests proving that judges are evidence-sensitive.

Examples:

```text
- If retention margin drops below floor, PPA judge must not select Candidate A.
- If q-over risk crosses threshold, fab dispatch judge must not approve local throughput optimization as safe.
- If proxy_execution_pass is true but proxy_design_pass is false, supervisor must block implementation claim.
- If tail risk worsens while average improves, yield judge must reduce confidence or request more evidence.
```

Outputs:

```text
outputs/scenario_variant_results/variant_matrix.json
outputs/scenario_variant_results/judge_sensitivity_report.md
outputs/scenario_variant_results/red_team_robustness_report.md
```

---

## 10. AI judgment audit layer

### 10.1 AI Judge

The AI Judge may be deterministic/rule-based. It does not need to call an LLM. But it must behave like an evidence-driven decision agent.

FORBIDDEN:

```text
- Copying expected_ai_judgment from scenario YAML.
- Hardcoding scenario_id → fixed decision text.
- Creating all AI outputs from templates independent of evidence.
```

REQUIRED:

```text
- Read evidence packet.
- Use visible metrics only.
- Apply rule/scoring logic.
- Produce decision, confidence, used metrics, requested claim, known limits.
- Change decision under scenario mutations.
```

Required output schema:

```json
{
  "scenario_id": "S02",
  "agent": "PpaJudge",
  "decision": "select_candidate_a_for_simulation_review",
  "confidence": 0.78,
  "visible_evidence_used": ["candidate_a_bandwidth_score", "visible_margin_proxy"],
  "rule_path": ["bandwidth_gain_detected", "visible_margin_above_floor"],
  "claim_requested": "Candidate A improves public-model bandwidth under visible constraints.",
  "known_limits": ["hot-corner hidden truth unavailable before oracle reveal"]
}
```

### 10.2 Red-team

The red-team must catch many risks but not all. If red-team catches all six canonical traps, the thesis weakens.

Required canonical result:

```text
red_team_caught_or_flagged = 4 or 5 of 6
escaped_until_hidden_truth >= 1
```

Preferred:

```text
caught = 5
escaped = 1
```

### 10.3 Meta Judge

The Meta Judge must reconcile AI Judge and Red-team outputs, not invent new hidden truth.

Output must include:

```text
visible_model_decision_quality
red_team_strength
remaining_uncertainty
recommended_supervisor_action
```

### 10.4 Virtual Human Supervisor

The supervisor is not a human impersonation and not a real expert approval.

Required dispositions:

```text
APPROVE_FOR_SIMULATION_REVIEW
APPROVE_FOR_PORTFOLIO_CLAIM
REWORD_AS_PROXY_ONLY
REQUEST_MORE_EVIDENCE
REJECT_DECISION
REQUIRES_REAL_DOMAIN_SIGNOFF
```

Every scenario must preserve real signoff boundary.

Required output fields:

```text
approved_claim
blocked_claim
requires_real_signoff
human_impersonation = false
claim_boundary_level
```

---

## 11. Hidden Truth Oracle

### 11.1 Purpose

Hidden truth represents unobserved physical reality, stale model boundary, downstream coupling, tail distribution, or signoff boundary.

### 11.2 Isolation requirement

Before hidden truth reveal:

- AI Judge cannot see hidden truth.
- Red-team cannot see hidden truth.
- Meta Judge cannot see hidden truth.
- Supervisor cannot see hidden truth.

Validator must prove no hidden truth fields appear in pre-reveal outputs.

### 11.3 Required files

```text
oracle/hidden/S01.json
...
oracle/hidden/S06.json
outputs/pre_reveal_freeze.json
outputs/hidden_truth_reveals/S01.json
...
```

---

## 12. Evidence packet and lineage

### 12.1 Evidence packet requirement

Evidence packets must be generated from engine outputs and public tool receipts, not copied from scenario YAML.

Each packet must include:

```text
scenario_id
visible_metrics
metric_lineage
engine_run_receipts
public_tool_receipts
claim_boundary
available_evidence
missing_evidence
```

### 12.2 Metric lineage requirement

Every major metric must identify:

```text
source_engine
source_file
run_id
scenario_id
parser_status
calculation_formula_or_rule
hash
```

### 12.3 Required validators

```text
validate_engine_computed_evidence.py
validate_metric_lineage.py
validate_public_tool_receipts.py
```

---

## 13. Dashboard requirements

The dashboard must be an evidence explorer, not just a summary page.

### 13.1 Required pages

1. **Architecture Map**
   - Memory System Twin
   - Circuit/Physical Proxy Twin
   - Fab Operation Twin
   - Factory Scene/Routing Twin
   - AI Judgment Audit Layer

2. **HBM Workload Twin**
   - workload profile
   - bandwidth
   - sustained bandwidth
   - p99 latency
   - thermal pressure
   - policy comparison

3. **Fab Operation Timeline**
   - LOT event timeline
   - queue pressure
   - q-time trajectory
   - bottleneck transitions
   - metrology delay

4. **Factory Scene / Routing**
   - fab graph/map
   - tools/queues/routes
   - LOT movement
   - congestion/bottleneck heatmap

5. **Public Tool Evidence**
   - ngspice receipt
   - Yosys/Verilator receipt
   - SimPy receipt
   - optional DRAMsim3/Ramulator/OpenROAD/CACTI receipts

6. **AI Judge / Red-team / Supervisor**
   - decision
   - red-team challenge
   - meta-judge output
   - supervisor claim boundary

7. **Hidden Truth Reveal**
   - why AI was plausible
   - why it was incomplete/wrong
   - what red-team caught or missed
   - why real signoff remains needed

8. **Variant Matrix**
   - 30+ variants
   - judge decision changes
   - red-team catch matrix
   - supervisor block/reword matrix

9. **Hynix Alignment**
   - Autonomous Fab
   - Digital Twin
   - Q-time / LOT priority
   - HBM workload
   - Physical AI / Operational AI
   - AI judgment audit

### 13.2 Screenshot requirement

Must generate or include screenshots:

```text
screenshots/architecture.png
screenshots/fab_timeline.png
screenshots/hbm_workload.png
screenshots/factory_scene.png
screenshots/public_tool_evidence.png
screenshots/ai_audit_flow.png
screenshots/hidden_truth_reveal.png
screenshots/hynix_alignment.png
```

If automatic screenshot generation is difficult, provide a `docs/14_SCREENSHOT_GUIDE.md` that tells exactly what to capture.

---

## 14. GitHub README requirements

The README must be recruiter/interviewer friendly.

### 14.1 README top section

Must include:

```text
- one-sentence thesis
- what this repo is
- what this repo is not
- quick demo commands
- screenshot gallery
- system architecture diagram
- Hynix alignment summary
```

### 14.2 README must show depth quickly

Include badges or quick facts:

```text
3+ real internal engines
3+ public tool run paths
6 canonical scenarios
30+ scenario variants
AI judge / red-team / supervisor / hidden oracle
GitHub Actions validated
Docker/devcontainer available
```

### 14.3 Korean start file

`START_HERE_KO.md` must explain:

- 왜 이 프로젝트가 SK hynix와 맞는지,
- 무엇을 먼저 봐야 하는지,
- 어떤 캡처를 제출용으로 쓰면 좋은지,
- 실제 signoff가 아니라 public-model decision twin이라는 점.

---

## 15. Makefile targets

Required:

```text
make setup
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
make verify
make package-release
make verify-clean-unzip
```

`make verify` must run:

```text
make test
make validate
make dashboard
```

`make demo-light` must work without heavy external tools.

`make demo-medium` should run ngspice/Yosys/Verilator/SimPy if installed or installed by Docker.

`make demo-heavy` may be optional but must produce receipts.

---

## 16. Docker/devcontainer

Because the repo is allowed to be heavy, Docker/devcontainer support is required.

### 16.1 Dockerfile must attempt to include

```text
python
pip dependencies
ngspice
yosys
verilator
node/npm if dashboard needs it
```

Optional sections may document:

```text
DRAMsim3
Ramulator2
OpenROAD
CACTI
```

### 16.2 Devcontainer

Must support a reviewer opening the repo and running:

```bash
make demo-light
make demo-medium
make dashboard
```

---

## 17. GitHub Actions

Required workflows:

### 17.1 `light.yml`

Runs:

```bash
make demo-light
make test
make validate
```

### 17.2 `medium.yml`

Runs if dependencies are installable:

```bash
make demo-medium
make validate
```

### 17.3 `validation.yml`

Checks release hygiene, no pycache, schemas, scenario coverage, no all-mock.

---

## 18. Validation suite

Required validators:

```text
validate_real_run_counts.py
validate_no_all_mock_release.py
validate_engine_computed_evidence.py
validate_public_tool_receipts.py
validate_ai_judges_not_scripted.py
validate_judge_sensitivity.py
validate_red_team_partial_miss.py
validate_hidden_truth_isolation.py
validate_supervisor_non_overclaim.py
validate_scenario_question_coverage.py
validate_variant_suite.py
validate_dashboard_contract.py
validate_release_hygiene.py
validate_github_screenshots.py
```

### 18.1 Negative fixtures

Add negative fixtures proving validators actually catch failures:

```text
validation/negative_fixtures/all_mock_release.json
validation/negative_fixtures/scripted_judge_output.json
validation/negative_fixtures/hidden_truth_leak.json
validation/negative_fixtures/supervisor_overclaim.json
validation/negative_fixtures/missing_metric_lineage.json
```

`validate_negative_fixtures.py` must confirm validators fail these fixtures.

---

## 19. Acceptance criteria

The repo is only v5-ready if all of these pass:

```text
1. make demo-light passes.
2. make demo-medium passes in Docker/devcontainer or produces explicit receipts.
3. make test passes.
4. make validate passes.
5. make dashboard generates dashboard_data and working dashboard.
6. At least 3 REAL_INTERNAL_RUN engines present.
7. At least 3 REAL_EXTERNAL_RUN or REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN receipts present.
8. Evidence packets are engine-generated.
9. AI judges are evidence-sensitive and mutation-tested.
10. Red-team catches 4 or 5 of 6 canonical risks, not all 6.
11. At least 1 canonical case escapes until hidden truth reveal.
12. Supervisor blocks/rewords real signoff claims in all cases.
13. 30+ variants generated and evaluated.
14. Dashboard includes required panels.
15. Screenshots exist or screenshot guide is complete.
16. No pycache or junk files in release.
17. README and START_HERE_KO are GitHub-submission ready.
```

---

## 20. Implementation phases GPT Pro should give to Codex

GPT Pro may adjust order, but should preserve phase intent.

### Phase 0 — Repo reset and contract lock

- Create new repo structure.
- Add `config_contract_lock.json` containing this contract's required items.
- Do not modify old v3 directly except as source material.

### Phase 1 — Light internal engines

- Port/improve v3 internal engines.
- Ensure 3 REAL_INTERNAL_RUN engines.
- Add run receipts and metric lineage.

### Phase 2 — HBM workload twin expansion

- Add workload profiles.
- Add policy comparison.
- Add latency/bandwidth curves.
- Add HBM dashboard data.

### Phase 3 — Circuit/physical public tool path

- Implement ngspice netlist generation and parsing.
- Implement fallback internal model.
- Generate SPICE receipts.

### Phase 4 — RTL/Yosys/Verilator path

- Generate scheduler/controller RTL.
- Run Verilator lint or Yosys synth if available.
- Parse receipts.

### Phase 5 — Fab operation twin expansion

- Implement SimPy or internal DES event log.
- Add q-time trajectory, lot dispatch, tool/chamber, metrology, yield-tail.
- Export event timelines.

### Phase 6 — Factory scene/routing twin

- Generate scene graph.
- Implement routing optimizer.
- Export fab map/dashboard data.

### Phase 7 — Scenario canonical run

- Implement all 6 canonical scenarios with required question coverage.
- Ensure engine-computed evidence.

### Phase 8 — Variant/mutation lab

- Generate 30+ variants.
- Run judge sensitivity and red-team robustness tests.

### Phase 9 — AI audit layer

- Evidence-sensitive AI judges.
- Red-team partial miss.
- Meta judge.
- Supervisor claim boundary.
- Hidden truth reveal.

### Phase 10 — Dashboard and screenshots

- Build evidence explorer dashboard.
- Generate screenshot data and files.
- Add screenshot guide.

### Phase 11 — Hynix alignment docs

- Write Hynix alignment.
- Write Korean interview talking points.
- Write non-claims/claims.

### Phase 12 — Docker/devcontainer/GitHub Actions

- Add reproducible setup.
- Add workflows.
- Validate light/medium profiles.

### Phase 13 — Final verification and release hygiene

- Run all make targets.
- Remove pycache/junk.
- Package release.
- Verify clean unzip.

---

## 21. Final GPT Pro instruction

Use this exact instruction when handing this document to GPT Pro:

```text
This document is a detailed architecture contract and execution blueprint. Do not summarize it into a vague prompt. Convert it into a Codex-ready implementation plan. Preserve all MUST / FORBIDDEN / VALIDATION / ACCEPTANCE requirements. The target is a heavy GitHub repository, not a lightweight zip. It must be aligned with SK hynix public directions: Autonomous Fab, Digital Twin, HBM workload, fab automation, Q-time/LOT priority, and AI judgment audit. Codex must implement concrete modules, run profiles, public tool receipts, scenario variants, dashboard, screenshots, Docker/devcontainer, GitHub Actions, and validation. Do not allow an all-mock scaffold.
```

