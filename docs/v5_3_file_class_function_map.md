# v5.3 File / Class / Function Implementation Map

This map is generated from the phase tickets and is a navigation aid; the source specification remains authoritative.

## P00 — Current v5.2 Baseline Audit, In-Place Upgrade Boundary, and Anti-Scaffold Inventory

### Files
- `docs/v5_3_baseline_audit.md`
- `outputs/v5_3_baseline_receipts.json`
- `outputs/v5_3_baseline_file_inventory.json`
- `outputs/v5_3_baseline_dashboard_audit.json`
- `docs/v5_3_build_state.json`

### Required symbols
- `audit_archive_and_manifest(zip_path, manifest_path)`
- `run_baseline_command(command, cwd)`
- `classify_frontend_surface(frontend_root)`
- `classify_screenshot_provenance(screenshot_path, sidecar_path)`
- `detect_hardcoded_pass_and_scenario_lookup(repo_root)`
- `build_reuse_replace_map(repo_root)`

### Dashboard
No visual redesign yet. Record the current navigation, page count, chart/timeline/map availability, data bindings, and screenshot provenance as the baseline that P02/P13–P15 must replace.

## P01 — Shared Product Contracts, Schemas, Units, Hashing, Run Receipts, and Artifact Lifecycle

### Files
- `twin_core/common/schemas.py`
- `twin_core/common/units.py`
- `twin_core/common/hashing.py`
- `twin_core/common/run_receipt.py`
- `twin_core/common/artifact_store.py`
- `twin_core/common/evidence_packet.py`
- `schemas/*.schema.json`
- `tests/test_common_contracts.py`
- `validation/validate_run_lifecycle.py`

### Required symbols
- `RunContext`
- `RunReceipt`
- `ArtifactRef`
- `MetricLineage`
- `ConstraintResult`
- `ToolStatus`
- `ClaimBoundary`
- `EvidencePacket`
- `create_run_context(profile, seed)`
- `hash_artifact(path)`
- `write_atomic_json(path, payload)`
- `freeze_artifact_set(run_id, paths)`
- `validate_current_run_id(payload, run_id)`

### Dashboard
Define the dashboard-data schema and stable IDs for pages/components, but do not hard-code values. Every UI datum must carry `run_id`, source artifact, source hash, unit, and evidence status.

## P02 — Reviewer Journey, README/START_HERE Rewrite, and Real Frontend Application Shell

### Files
- `README.md`
- `START_HERE_KO.md`
- `frontend/index.html`
- `frontend/styles.css`
- `frontend/app.js`
- `frontend/router.js`
- `frontend/components/*.js`
- `frontend/pages/overview.js`
- `frontend/pages/*.js`
- `tests/frontend/test_navigation.mjs`

### Required symbols
- `createRouter(routeTable)`
- `navigate(routeId, params)`
- `loadDashboardIndex(url)`
- `renderAppShell(root, state)`
- `renderSidebar(routes, activeRoute)`
- `MetricCard(props)`
- `StatusBadge(props)`
- `EvidenceTable(props)`
- `ScenarioSelector(props)`
- `ErrorBoundary(renderFn)`

### Dashboard
Create routes: Overview, HBM Workload Twin, Circuit / Physical Proxy Twin, Fab Operation Twin, Factory Scene / Routing Twin, AI Judgment Audit, Public Tool Evidence, Scenario Variant Lab, Hynix Alignment. A raw JSON drawer may exist only as a secondary evidence inspector.

## P03 — HBM Workload Generator, Stack Topology, Address Mapping, and Deterministic Request Trace

### Files
- `twin_core/hbm_memory/workloads.py`
- `twin_core/hbm_memory/hbm_stack.py`
- `twin_core/hbm_memory/address_map.py`
- `twin_core/hbm_memory/request_trace.py`
- `twin_core/hbm_memory/run_workloads.py`
- `tests/test_hbm_workloads.py`

### Required symbols
- `WorkloadEvent`
- `HbmWorkloadConfig`
- `HbmTopology`
- `AddressTuple`
- `RequestTrace`
- `generate_llm_training_burst(config, rng)`
- `generate_llm_inference_latency(config, rng)`
- `generate_sustained_bandwidth_thermal(config, rng)`
- `generate_refresh_stress(config, rng)`
- `generate_read_write_turnaround_stress(config, rng)`
- `generate_bank_group_conflict_stress(config, rng)`
- `map_address(address, topology)`
- `generate_trace(config, topology, seed)`

### Dashboard
Expose workload selector metadata and trace preview data for the HBM page: request mix over time, address locality, bank-group occupancy, and burst windows.

## P04 — HBM Scheduler, Refresh, Turnaround, Thermal Model, Policy Comparison, Metrics, and Product Page

### Files
- `twin_core/hbm_memory/scheduler.py`
- `twin_core/hbm_memory/refresh_model.py`
- `twin_core/hbm_memory/thermal_model.py`
- `twin_core/hbm_memory/policy_compare.py`
- `twin_core/hbm_memory/run_hbm_twin.py`
- `frontend/pages/hbm.js`
- `frontend/components/charts.js`
- `tests/test_hbm_memory_twin.py`

### Required symbols
- `HbmPolicyConfig`
- `HbmTwinMetrics`
- `BankState`
- `SchedulerState`
- `RefreshState`
- `ThermalState`
- `schedule_fcfs(...)`
- `schedule_fr_fcfs(...)`
- `apply_write_drain(...)`
- `apply_thermal_safe(...)`
- `apply_refresh_aware(...)`
- `estimate_latency(...)`
- `update_thermal_state(...)`
- `compute_policy_score(...)`
- `compare_policies(...)`
- `renderHbmPage(model)`

### Dashboard
Implement workload selector, policy table, effective-vs-sustained bandwidth grouped bars, p50/p99 latency chart, thermal-pressure timeline, refresh/turnaround waterfall, conflict heatmap, recommendation rationale, and S01/S02/S06 judgment links.

## P05 — Circuit / Physical Proxy Twin: Charge Sharing, Sense/Retention Margin, PVT Sweep, and Signoff Semantics

### Files
- `twin_core/circuit_physical/read_path_model.py`
- `twin_core/circuit_physical/retention_model.py`
- `twin_core/circuit_physical/pvt_corner_sweep.py`
- `twin_core/circuit_physical/timing_proxy.py`
- `twin_core/circuit_physical/proxy_signoff.py`
- `twin_core/circuit_physical/netlist_generator.py`
- `twin_core/circuit_physical/run_circuit_proxy.py`
- `frontend/pages/circuit.js`
- `tests/test_circuit_proxy.py`

### Required symbols
- `ReadPathConfig`
- `PvtCorner`
- `ProxyMetrics`
- `compute_charge_share_voltage(...)`
- `compute_delta_v_bitline(...)`
- `compute_sense_margin(...)`
- `compute_leakage_loss(...)`
- `compute_retention_margin(...)`
- `run_pvt_sweep(...)`
- `run_seeded_monte_carlo(...)`
- `compute_wns_tns_proxy(...)`
- `evaluate_proxy_status(...)`
- `generate_ngspice_netlist(...)`
- `renderCircuitPage(model)`

### Dashboard
Implement charge-sharing visual, PVT/corner table, sense/retention margin charts with threshold lines, Monte Carlo distribution, timing proxy panel, and three-level execution/design/signoff status.

## P06 — Current-Run ngspice, Yosys, Verilator, and SimPy Public-Tool Evidence

### Files
- `public_tool_runs/ngspice/run_ngspice.py`
- `public_tool_runs/ngspice/parse_ngspice.py`
- `public_tool_runs/ngspice/netlists/*.sp`
- `public_tool_runs/yosys_verilator/generate_policy_rtl.py`
- `public_tool_runs/yosys_verilator/run_yosys.py`
- `public_tool_runs/yosys_verilator/run_verilator.py`
- `public_tool_runs/simpy_fab/run_simpy_demo.py`
- `public_tool_runs/common/tool_receipt.py`
- `frontend/pages/public_tools.js`
- `tests/test_public_tool_receipts.py`

### Required symbols
- `ToolReceipt`
- `detect_tool(binary)`
- `run_checked_subprocess(command, cwd, env)`
- `parse_ngspice_metrics(log)`
- `generate_policy_controller_rtl(config)`
- `parse_yosys_stats(log)`
- `parse_verilator_lint(log)`
- `run_simpy_receipt(config)`
- `renderPublicToolEvidencePage(model)`

### Dashboard
Implement receipt panels for ngspice, Yosys, Verilator, and SimPy showing status, version, exact command, return code, parsed metrics, log links, input/output hashes, run timestamp, and claim boundary.

## P07 — Fab Operation Twin Domain Model and SimPy Event Engine

### Files
- `twin_core/fab_operation/simpy_environment.py`
- `twin_core/fab_operation/lot.py`
- `twin_core/fab_operation/tool.py`
- `twin_core/fab_operation/chamber.py`
- `twin_core/fab_operation/process_step.py`
- `twin_core/fab_operation/queue.py`
- `twin_core/fab_operation/qtime.py`
- `twin_core/fab_operation/metrology.py`
- `twin_core/fab_operation/maintenance.py`
- `twin_core/fab_operation/event_log.py`
- `twin_core/fab_operation/run_fab_twin.py`
- `tests/test_fab_simpy_core.py`

### Required symbols
- `Lot`
- `Tool`
- `Chamber`
- `ProcessStep`
- `FabQueue`
- `QTimeRule`
- `MaintenanceWindow`
- `MetrologyStation`
- `Sensor`
- `FabEvent`
- `FabEnvironment`
- `lot_process(...)`
- `sensor_drift_process(...)`
- `metrology_process(...)`
- `maintenance_process(...)`
- `run_fab_environment(config, seed)`

### Dashboard
Define the Fab timeline data source: lanes for LOTs/tools/chambers, queue and process intervals, metrology/maintenance markers, and synchronized cursor timestamps.

## P08 — Fab Dispatch, Q-Time, Metrology Lag, Sensor Drift, Maintenance, Yield-Tail Risk, and Product Timeline

### Files
- `twin_core/fab_operation/dispatch_policy.py`
- `twin_core/fab_operation/qtime.py`
- `twin_core/fab_operation/maintenance.py`
- `twin_core/fab_operation/metrology.py`
- `twin_core/fab_operation/yield_risk.py`
- `twin_core/fab_operation/metrics.py`
- `frontend/pages/fab.js`
- `frontend/components/timeline.js`
- `tests/test_fab_decisions.py`

### Required symbols
- `DispatchPolicy`
- `DispatchDecision`
- `QTimeTrajectory`
- `YieldRiskModel`
- `score_lot_priority(...)`
- `estimate_q_over_risk(...)`
- `compute_downstream_bottleneck(...)`
- `update_chamber_health(...)`
- `apply_sensor_drift(...)`
- `schedule_maintenance(...)`
- `estimate_yield_tail(...)`
- `compare_dispatch_policies(...)`
- `renderFabPage(model)`

### Dashboard
Implement LOT A/B Q-time curves, Gantt/timeline lanes, dispatch markers, queue depth, tool utilization, chamber health, drift, metrology delay, Q-over threshold, yield-tail panels, and AI audit summary for S03–S05.

## P09 — Factory Scene / Routing Twin, 2D Layout, Congestion, Dijkstra/A*, OpenUSD-Like Export, and Map

### Files
- `twin_core/factory_scene/layout.py`
- `twin_core/factory_scene/scene_graph.py`
- `twin_core/factory_scene/routing_graph.py`
- `twin_core/factory_scene/congestion.py`
- `twin_core/factory_scene/route_optimizer.py`
- `twin_core/factory_scene/openusd_like_export.py`
- `twin_core/factory_scene/run_factory_scene.py`
- `frontend/pages/factory.js`
- `frontend/components/route_map.js`
- `tests/test_factory_routing.py`

### Required symbols
- `FabNode`
- `TransportEdge`
- `RoutingGraph`
- `RouteRequest`
- `RouteResult`
- `build_layout(config)`
- `build_adjacency(nodes, edges)`
- `edge_cost(edge, congestion_weight, qtime_pressure)`
- `dijkstra_route(graph, start, goal, cost_fn)`
- `astar_route(graph, start, goal, heuristic)`
- `update_congestion(events, graph)`
- `export_openusd_like_scene(...)`
- `renderFactoryPage(model)`

### Dashboard
Implement pan/zoom 2D fab floor map with node types, transport edges, selected and alternative routes, moving LOT marker, congestion heat, route metrics, and `.usda` download link.

## P10 — Six Canonical Scenarios, Cross-Twin Orchestration, Evidence Packets, and Metric Lineage

### Files
- `scenarios/canonical/S01.yaml`
- `scenarios/canonical/S02.yaml`
- `scenarios/canonical/S03.yaml`
- `scenarios/canonical/S04.yaml`
- `scenarios/canonical/S05.yaml`
- `scenarios/canonical/S06.yaml`
- `twin_core/scenario_runner.py`
- `twin_core/evidence/build_packet.py`
- `twin_core/evidence/lineage.py`
- `tests/test_canonical_scenarios.py`

### Required symbols
- `ScenarioConfig`
- `ScenarioExecutionPlan`
- `EngineDependency`
- `run_scenario(config, run_context)`
- `resolve_engine_plan(scenario_family)`
- `build_evidence_packet(...)`
- `build_metric_lineage(...)`
- `validate_visible_only(packet)`
- `link_public_tool_receipts(...)`

### Dashboard
Populate scenario selector and product cards. S03 must link the Fab timeline, Q-time curves, route map, evidence packet, judgment chain, and later truth reveal from one selection.

## P11 — Evidence-Sensitive AI Judge, Red-Team Partial Miss, Meta Judge, Claim-Boundary Supervisor, Freeze, and Hidden Truth Reveal

### Files
- `agents/rule_based_judges.py`
- `agents/red_team.py`
- `agents/meta_judge.py`
- `agents/virtual_supervisor.py`
- `agents/audit_pipeline.py`
- `oracle/hidden/S01.json`
- `oracle/hidden/S02.json`
- `oracle/hidden/S03.json`
- `oracle/hidden/S04.json`
- `oracle/hidden/S05.json`
- `oracle/hidden/S06.json`
- `oracle/reveal.py`
- `tests/test_ai_audit_pipeline.py`

### Required symbols
- `JudgeDecision`
- `RedTeamChallenge`
- `MetaAssessment`
- `SupervisorDisposition`
- `TruthReveal`
- `select_judge_profile(scenario_family)`
- `judge_evidence(packet, profile)`
- `challenge_visible_decision(packet, judgment)`
- `reconcile_visible_outputs(judgment, challenge)`
- `manage_claim_boundary(meta, packet)`
- `freeze_pre_reveal_outputs(...)`
- `reveal_hidden_truth(...)`
- `compute_audit_metrics(...)`

### Dashboard
Implement the data contract for DecisionFlow: evidence metrics → AI decision → red-team → meta judge → supervisor approved/blocked claim → hidden truth reveal. Show caught/escaped state and why real signoff remains required.

## P12 — 60+ Semantic Scenario Variants, Family-Based Routing, Judge Sensitivity, and Red-Team Robustness

### Files
- `scenarios/generate_variants.py`
- `scenarios/variant_catalog.py`
- `scenarios/variants/*.yaml`
- `twin_core/variant_runner.py`
- `outputs/scenario_variant_results/variant_matrix.json`
- `outputs/scenario_variant_results/variant_heatmap_data.json`
- `outputs/scenario_variant_results/judge_sensitivity_report.md`
- `outputs/scenario_variant_results/red_team_robustness_report.md`
- `tests/test_variant_lab.py`

### Required symbols
- `VariantSpec`
- `MutationCatalog`
- `generate_variants(canonical, catalog, seed)`
- `apply_mutation(config, mutation_type, parameters)`
- `route_variant_by_family(variant)`
- `run_variant_matrix(...)`
- `compute_decision_transition(...)`
- `compute_red_team_robustness(...)`
- `build_variant_heatmap(...)`

### Dashboard
Implement Variant Matrix data: filter by parent/family/mutation/status, heatmap of judge decisions, red-team caught/escaped cells, supervisor blocked/reworded counts, and drill-down to changed metrics/lineage.

## P13 — Dashboard Data Builder, Evidence Explorer API, Cross-Link Index, and Freshness Contract

### Files
- `scripts/generate_dashboard_data.py`
- `twin_core/evidence/dashboard_index.py`
- `frontend/dashboard_data.json`
- `outputs/dashboard_data.json`
- `outputs/evidence_index.json`
- `schemas/dashboard_data.schema.json`
- `tests/test_dashboard_data.py`

### Required symbols
- `DashboardBundle`
- `PageModel`
- `ChartSeries`
- `TimelineModel`
- `RouteMapModel`
- `DecisionFlowModel`
- `ReceiptView`
- `VariantMatrixModel`
- `build_dashboard_bundle(run_id, artifact_index)`
- `build_hbm_page_model(...)`
- `build_circuit_page_model(...)`
- `build_fab_page_model(...)`
- `build_factory_page_model(...)`
- `build_audit_page_model(...)`
- `validate_dashboard_sources(bundle)`

### Dashboard
Provide exact models for Overview, HBM, Circuit, Fab, Factory, AI Audit, Public Tool Evidence, Variant Lab, and Hynix Alignment. Every chart/table/timeline/map/flow has source IDs and units.

## P14 — Nine-Page Evidence Explorer Console with Charts, Timelines, Maps, Tables, and Decision Flow

### Files
- `frontend/index.html`
- `frontend/styles.css`
- `frontend/app.js`
- `frontend/router.js`
- `frontend/components/metric_card.js`
- `frontend/components/status_badge.js`
- `frontend/components/line_chart.js`
- `frontend/components/bar_chart.js`
- `frontend/components/timeline.js`
- `frontend/components/route_map.js`
- `frontend/components/evidence_table.js`
- `frontend/components/decision_flow.js`
- `frontend/components/receipt_panel.js`
- `frontend/components/scenario_selector.js`
- `frontend/components/variant_matrix.js`
- `frontend/pages/*.js`
- `tests/frontend/*.mjs`

### Required symbols
- `MetricCard`
- `StatusBadge`
- `LineChart`
- `BarChart`
- `Timeline`
- `RouteMap`
- `EvidenceTable`
- `DecisionFlow`
- `ReceiptPanel`
- `ScenarioSelector`
- `VariantMatrix`
- `renderOverviewPage`
- `renderHbmPage`
- `renderCircuitPage`
- `renderFabPage`
- `renderFactoryPage`
- `renderAuditPage`
- `renderPublicToolsPage`
- `renderVariantLabPage`
- `renderHynixAlignmentPage`

### Dashboard
Overview shows architecture/evidence chain and quick facts; HBM shows policy charts; Circuit shows margins/corners/status; Fab shows event timeline/Q-time; Factory shows map/routes; Audit shows decision flow/reveal; Tools show receipts; Variants show matrix/heatmap; Alignment maps public direction to project evidence.

## P15 — Real Browser Screenshot Capture, Visual Evidence Manifest, and Screenshot Quality Regression

### Files
- `scripts/render_dashboard_screenshots.py`
- `scripts/serve_dashboard.py`
- `screenshots/01_architecture.png`
- `screenshots/02_fab_qtime_timeline.png`
- `screenshots/03_hbm_workload_policy_compare.png`
- `screenshots/04_factory_scene_routing.png`
- `screenshots/05_public_tool_evidence.png`
- `screenshots/06_ai_judgment_audit_flow.png`
- `screenshots/07_hynix_alignment.png`
- `screenshots/screenshot_manifest.json`
- `tests/test_screenshot_manifest.py`

### Required symbols
- `ScreenshotSpec`
- `start_static_server(...)`
- `capture_route(page, spec)`
- `wait_for_component_ready(page, component_ids)`
- `collect_dom_evidence(page, selectors)`
- `compute_image_entropy(path)`
- `detect_blank_or_placeholder(path)`
- `build_screenshot_manifest(...)`

### Dashboard
Capture architecture, Fab Q-time timeline, HBM policy comparison, factory routing, public tool evidence, AI audit flow, and Hynix alignment at stable product states. Ensure charts, timelines, maps, tables/receipts, and decision flow are visibly present.

## P16 — Docker, Docker Compose, Devcontainer, GitHub Actions, and Reproducible Medium Profile

### Files
- `Dockerfile`
- `docker-compose.yml`
- `.devcontainer/devcontainer.json`
- `.github/workflows/light.yml`
- `.github/workflows/medium.yml`
- `.github/workflows/validation.yml`
- `requirements.txt`
- `pyproject.toml`
- `scripts/install_medium_tools.sh`
- `tests/test_ci_contract.py`

### Required symbols
- `No product Python symbols required; implement pinned build stages, health checks, artifact upload paths, cache keys, and commands that invoke Make targets exactly.`

### Dashboard
Public Tool Evidence page must show latest medium-profile receipts and distinguish local versus CI/container provenance.

## P17 — Semantic Validators, Behavioral Tests, and Deliberate Negative Regression Fixtures

### Files
- `validation/validate_no_name_tag_modules.py`
- `validation/validate_engine_computed_evidence.py`
- `validation/validate_ai_judges_not_scripted.py`
- `validation/validate_red_team_partial_miss.py`
- `validation/validate_hidden_truth_isolation.py`
- `validation/validate_supervisor_non_overclaim.py`
- `validation/validate_variant_routing.py`
- `validation/validate_frontend_console.py`
- `validation/validate_screenshot_data_sync.py`
- `validation/validate_public_tool_receipts.py`
- `validation/validate_release_hygiene.py`
- `tests/negative_fixtures/*`
- `tests/test_negative_regressions.py`

### Required symbols
- `ValidationFinding`
- `ValidationReport`
- `run_validator_suite(profile)`
- `assert_expected_failure(fixture, validator, reason_code)`
- `scan_ast_for_stubs(root)`
- `scan_for_scenario_lookup(root)`
- `scan_frontend_for_hardcoded_metrics(root)`
- `scan_release_hygiene(root)`

### Dashboard
Overview and Public Tool pages show validator status and evidence links, but validation badges may not replace actual charts or engine evidence.

## P18 — GitHub Product Documentation, Hynix Alignment, Public-Model Boundaries, and Reviewer/Interview Journey

### Files
- `README.md`
- `START_HERE_KO.md`
- `docs/00_READ_ME_FIRST.md`
- `docs/01_SYSTEM_THESIS.md`
- `docs/02_PUBLIC_MODEL_LIMITS.md`
- `docs/03_HYNIX_ALIGNMENT.md`
- `docs/04_DIGITAL_TWIN_ARCHITECTURE.md`
- `docs/05_HBM_WORKLOAD_TWIN.md`
- `docs/06_CIRCUIT_PHYSICAL_PROXY_TWIN.md`
- `docs/07_FAB_OPERATION_TWIN.md`
- `docs/08_FACTORY_SCENE_ROUTING_TWIN.md`
- `docs/09_AI_JUDGMENT_AUDIT_LAYER.md`
- `docs/10_SCENARIO_CASEBOOK.md`
- `docs/11_IMPLEMENTATION_EVIDENCE.md`
- `docs/12_NON_CLAIMS_AND_CLAIMS.md`
- `docs/13_INTERVIEW_TALKING_POINTS_KO.md`
- `docs/14_SCREENSHOT_GUIDE.md`

### Required symbols
- `scripts/generate_readme_quick_facts.py: build_quick_facts(run_index)`
- `scripts/generate_implementation_evidence.py: build_evidence_report(...)`
- `scripts/validate_doc_links.py: validate_links(root)`

### Dashboard
Hynix Alignment page reads structured alignment data and links each row to project artifacts, limits, and source category. Overview links to README deep dives and screenshots.

## P19 — Final Make Transaction, Deterministic Release, Clean-Unzip Verification, and Independent Red Team

### Files
- `Makefile`
- `scripts/package_release.py`
- `scripts/verify_clean_unzip.py`
- `release/release_manifest.json`
- `release/hynix-autonomous-fab-hbm-digital-twin-console-v5.3.zip`
- `release/hynix-autonomous-fab-hbm-digital-twin-console-v5.3.release_manifest.json`
- `docs/v5_3_build_state.json`
- `outputs/final_acceptance_receipts.json`

### Required symbols
- `build_release_file_list(root)`
- `assert_release_hygiene(paths)`
- `write_internal_content_manifest(paths)`
- `build_deterministic_zip(paths, output)`
- `write_external_archive_manifest(zip_path)`
- `verify_clean_unzip(zip_path)`
- `verify_final_state(state, receipts, manifest)`

### Dashboard
No new values. Rebuild bundle and screenshots before freeze, then verify packaged console opens and all relative evidence links work.
