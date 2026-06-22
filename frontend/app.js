const routes = [
  ["overview", "Overview"],
  ["hbm", "HBM Workload Twin"],
  ["circuit", "Circuit / Physical Proxy Twin"],
  ["fab", "Fab Operation Twin"],
  ["factory", "Factory Scene / Routing Twin"],
  ["audit", "AI Judgment Audit"],
  ["public-tools", "Public Tool Evidence"],
  ["variants", "Scenario Variant Lab"],
  ["hynix-alignment", "Hynix Alignment"],
];

let dashboard = null;

function fmt(value, unit = "") {
  if (value === undefined || value === null || value === "") return "NA";
  if (typeof value === "number") return `${Number.isInteger(value) ? value : value.toFixed(3)}${unit}`;
  return `${value}${unit}`;
}

function byFamily(packetFamily) {
  return (dashboard.packets || []).find((packet) => packet.scenario_family === packetFamily || packet.scenario_id === packetFamily) || {};
}

function metricsFor(family) {
  return byFamily(family).visible_metrics || {};
}

function MetricCard(label, value, sub = "") {
  return `<div class="metric-card"><div class="label">${label}</div><div class="value">${value}</div><div class="sub">${sub}</div></div>`;
}

function StatusBadge(status) {
  const s = String(status || "UNKNOWN");
  const cls = s.includes("PASS") || s.includes("REAL") || s.includes("READY") ? "good" : (s.includes("FAIL") ? "bad" : "warn");
  return `<span class="status ${cls}">${s}</span>`;
}

function BarChart(rows, opts = {}) {
  const width = 760, height = 280, left = 170, top = 28, rowH = 38;
  const max = Math.max(1, ...rows.map((r) => Number(r.value) || 0));
  const bars = rows.map((r, i) => {
    const y = top + i * rowH;
    const w = Math.max(3, (Number(r.value) || 0) / max * (width - left - 96));
    return `<text x="12" y="${y + 18}">${r.label}</text><rect x="${left}" y="${y}" width="${w}" height="22" rx="3" fill="${r.color || "#1d5d8f"}"></rect><text x="${left + w + 8}" y="${y + 17}">${fmt(r.value, opts.unit || "")}</text>`;
  }).join("");
  return `<svg class="chart" viewBox="0 0 ${width} ${height}" role="img">${bars}</svg>`;
}

function LineChart(points, color = "#1d5d8f", label = "trajectory") {
  const safe = points.length ? points : [{ x: 0, y: 0 }, { x: 1, y: 0 }];
  const width = 760, height = 260, left = 52, top = 30, plotW = 650, plotH = 178;
  const xs = safe.map((p) => Number(p.x));
  const ys = safe.map((p) => Number(p.y));
  const minX = Math.min(...xs, 0), maxX = Math.max(...xs, 1);
  const minY = Math.min(...ys, 0), maxY = Math.max(...ys, 1);
  const coords = safe.map((p) => {
    const x = left + ((p.x - minX) / Math.max(1, maxX - minX)) * plotW;
    const y = top + plotH - ((p.y - minY) / Math.max(1, maxY - minY)) * plotH;
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  }).join(" ");
  const dots = safe.map((p) => {
    const x = left + ((p.x - minX) / Math.max(1, maxX - minX)) * plotW;
    const y = top + plotH - ((p.y - minY) / Math.max(1, maxY - minY)) * plotH;
    return `<circle cx="${x}" cy="${y}" r="3" fill="${color}"></circle>`;
  }).join("");
  return `<svg class="chart" viewBox="0 0 ${width} ${height}" role="img"><text x="18" y="22">${label}</text><line x1="${left}" y1="${top + plotH}" x2="${left + plotW}" y2="${top + plotH}" stroke="#cfd9e3"></line><line x1="${left}" y1="${top}" x2="${left}" y2="${top + plotH}" stroke="#cfd9e3"></line><polyline points="${coords}" fill="none" stroke="${color}" stroke-width="3"></polyline>${dots}<text x="${left}" y="236">t ${fmt(minX)} to ${fmt(maxX)}</text><text x="600" y="236">value ${fmt(minY)} to ${fmt(maxY)}</text></svg>`;
}

function Timeline(events) {
  return `<div class="timeline">${events.slice(0, 16).map((e) => `<div class="timeline-row"><strong>${fmt(e.time ?? e.time_min ?? e.t, "m")}</strong><span>${e.event}</span><div>${e.lot || e.lot_id || ""} ${e.tool !== undefined ? "Tool " + e.tool : e.tool_id || ""}</div></div>`).join("")}</div>`;
}

function RouteMap(scene) {
  const nodes = scene.nodes || [];
  const edges = scene.edges || [];
  if (nodes.length < 5 || edges.length < 5) {
    return `<div class="error-box">ERROR: computed factory route graph is missing. Frontend fallback maps are forbidden.</div>`;
  }
  const selected = scene.selected_route || [];
  const selectedPairs = new Set(selected.slice(0, -1).map((node, i) => `${node}->${selected[i + 1]}`));
  const width = 760, height = 390;
  const nodeById = Object.fromEntries(nodes.map((n) => [n.id, n]));
  const zones = (scene.congestion_zones || []).map((z) => {
    const x = 80 + z.center_xy[0] * 115, y = 65 + z.center_xy[1] * 48;
    return `<circle cx="${x}" cy="${y}" r="${32 + Number(z.severity || 0) * 28}" fill="#d9770629" stroke="#d97706"></circle><text x="${x - 45}" y="${y - 36}">${z.zone_id}</text>`;
  }).join("");
  const lines = edges.map((e) => {
    const a = nodeById[e.from || e.source], b = nodeById[e.to || e.target];
    if (!a || !b) return "";
    const ax = 80 + (a.xy ? a.xy[0] : a.x) * 115, ay = 65 + (a.xy ? a.xy[1] : a.y) * 48;
    const bx = 80 + (b.xy ? b.xy[0] : b.x) * 115, by = 65 + (b.xy ? b.xy[1] : b.y) * 48;
    const active = selectedPairs.has(`${e.from}->${e.to}`) || selectedPairs.has(`${e.to}->${e.from}`);
    return `<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="${active ? "#b74b3f" : "#95a7b8"}" stroke-width="${active ? 6 : 3}"></line><text x="${(ax + bx) / 2}" y="${(ay + by) / 2 - 6}">${fmt(e.cost || e.distance)}</text>`;
  }).join("");
  const points = nodes.map((n) => {
    const x = 80 + (n.xy ? n.xy[0] : n.x) * 115, y = 65 + (n.xy ? n.xy[1] : n.y) * 48;
    const fill = (n.kind || n.type) === "metrology" ? "#6d5aa7" : ((n.kind || n.type) === "tool" ? "#1d5d8f" : "#0f766e");
    return `<circle cx="${x}" cy="${y}" r="16" fill="${fill}"></circle><text x="${x - 38}" y="${y + 38}">${n.id}</text>`;
  }).join("");
  return `<svg class="route-map" viewBox="0 0 ${width} ${height}" role="img"><rect x="20" y="20" width="720" height="330" rx="8" fill="#eef4f8" stroke="#d7e1ea"></rect>${zones}${lines}${points}<text x="32" y="374">selected route: ${selected.join(" -> ")} | cost ${fmt(scene.route_cost)} | delay ${fmt(scene.route_delay_min, " min")}</text></svg>`;
}

function EvidenceTable(rows) {
  return `<table><thead><tr><th>Metric / Tool</th><th>Status</th><th>Source artifact</th></tr></thead><tbody>${rows.map((r) => `<tr><td>${r.name}</td><td>${StatusBadge(r.status)}</td><td class="evidence-path">${r.path}</td></tr>`).join("")}</tbody></table>`;
}

function DecisionFlow(packet) {
  const sid = packet.scenario_id || "S03";
  const judgment = (dashboard.ai_audit?.judgments || []).find((j) => j.scenario_id === sid) || {};
  const red = (dashboard.ai_audit?.red_team || []).find((j) => j.scenario_id === sid) || {};
  const meta = (dashboard.ai_audit?.meta_judge || []).find((j) => j.scenario_id === sid) || {};
  const supervisor = (dashboard.ai_audit?.supervisor || []).find((j) => j.scenario_id === sid) || {};
  const hidden = (dashboard.ai_audit?.hidden_truth || []).find((j) => j.scenario_id === sid) || {};
  return `<div class="flow">
    <div class="flow-step"><small>Evidence Packet</small><strong>${sid}</strong><p>${Object.keys(packet.visible_metrics || {}).length} visible metrics</p></div>
    <div class="flow-step"><small>AI Judge</small><strong>${judgment.decision || "pending"}</strong><p>confidence ${fmt(judgment.confidence)}</p></div>
    <div class="flow-step"><small>Red-team</small><strong>${red.challenge_emitted ? "caught" : "escaped"}</strong><p>${red.challenge_type || "visible gap"}</p></div>
    <div class="flow-step"><small>Meta Judge</small><strong>${meta.disposition || meta.decision || "visible-only"}</strong><p>scope checked</p></div>
    <div class="flow-step"><small>Virtual Supervisor</small><strong>${supervisor.disposition || "bounded"}</strong><p>requires real signoff</p></div>
    <div class="flow-step"><small>Hidden Truth</small><strong>${hidden.post_reveal_label || "post-freeze"}</strong><p>caught or escaped boundary</p></div>
  </div>`;
}

function ReceiptPanel(receipts) {
  return `<div class="grid cols-2">${receipts.map((r) => `<div class="panel"><h3>${r.tool}</h3>${StatusBadge(r.status)}<p class="note">${r.reason || "current-run receipt"}</p><div class="evidence-path">${Array.isArray(r.command) ? r.command.join(" ") : r.command}</div><p class="evidence-path">${r.log_path || r.raw_output_path}</p></div>`).join("")}</div>`;
}

function VariantMatrix() {
  const results = dashboard.variant_matrix?.results || [];
  const families = ["S01", "S02", "S03", "S04", "S05", "S06"];
  return families.map((family) => {
    const cells = results.filter((r) => r.parent === family || r.canonical_parent === family).slice(0, 12).map((r, i) => {
      const color = r.decision?.includes("hold") || r.decision?.includes("request") ? "#b74b3f" : (r.decision?.includes("select") ? "#1d5d8f" : "#0f766e");
      return `<span class="variant-cell" style="background:${color}" title="${r.variant_id || r.scenario_id}">${i + 1}</span>`;
    }).join("");
    return `<div class="panel"><h3>${family}</h3>${cells || "<p class='note'>No variants</p>"}</div>`;
  }).join("");
}

function pageOverview() {
  const m = dashboard.audit_metrics || {};
  return `<div class="grid cols-4">
      ${MetricCard("Internal engines", fmt(m.real_internal_run_count), "REAL_INTERNAL_RUN receipts")}
      ${MetricCard("Public tool attempts", fmt(m.public_tool_attempt_count), "local evidence")}
      ${MetricCard("Canonical scenarios", fmt(m.scenario_count), "S01-S06 product cards")}
      ${MetricCard("Variants", fmt(dashboard.variant_matrix?.variant_count || 0), "family-routed mutations")}
    </div>
    <div class="grid cols-2">
      <div class="panel"><h2>Five-module product map</h2>${BarChart([
        { label: "HBM memory", value: 4, color: "#1d5d8f" },
        { label: "Circuit proxy", value: 4, color: "#6d5aa7" },
        { label: "Fab operation", value: 5, color: "#0f766e" },
        { label: "Factory routing", value: 4, color: "#287a4b" },
        { label: "AI audit", value: 5, color: "#b74b3f" },
      ])}</div>
      <div class="panel"><h2>S03 evidence chain</h2>${DecisionFlow(byFamily("S03"))}</div>
    </div>
    <div class="panel"><h2>Reviewer journey</h2><p class="note">current input -> engine/tool -> raw -> parsed -> metric lineage -> dashboard -> DOM -> screenshot -> manifest. Public-model only; real product signoff stays blocked.</p></div>`;
}

function pageHbm() {
  const hbm = dashboard.hbm_memory || dashboard.hbm_workload || {};
  const display = hbm.display_metrics || {};
  const recommended = String(hbm.recommended_policy || "NA").replaceAll("_", " ");
  const policyRows = (hbm.policy_comparison || []).map((p) => ({ label: p.policy_id, value: p.display_bandwidth_GBps, color: p.policy_id.includes("THERMAL") ? "#0f766e" : (p.policy_id === "FR-FCFS" ? "#1d5d8f" : "#95a7b8") }));
  return `<div class="grid cols-4">
    ${MetricCard("Theoretical bandwidth", fmt(display.theoretical_bandwidth_GBps?.value, " GB/s"), "derived from raw Gbps / 8")}
    ${MetricCard("Sustained bandwidth", fmt(display.sustained_bandwidth_GBps?.value, " GB/s"), "display suffix _GBps")}
    ${MetricCard("Recommended policy", recommended, "hard constraints before score")}
    ${MetricCard("Unit note", "GB/s = Gbps / 8", "raw _gbps is never labeled GB/s")}
  </div>
  <div class="grid cols-2"><div class="panel"><h2>Policy comparison in GB/s</h2>${BarChart(policyRows, { unit: " GB/s" })}</div><div class="panel"><h2>Policy evidence</h2>${EvidenceTable((hbm.policy_comparison || []).map((p) => ({ name: p.policy_id, status: p.hard_constraint_result, path: `${p.display_bandwidth_GBps} GB/s, p99 ${p.p99_latency_ns} ns, thermal ${p.thermal_pressure}` })))}</div></div>`;
}

function pageCircuit() {
  const m = metricsFor("S02");
  return `<div class="grid cols-4">
    ${MetricCard("Charge share", fmt(m["circuit_physical.charge_share_delta_v_mv"], " mV"), "1T1C proxy")}
    ${MetricCard("Sense margin", fmt(m["circuit_physical.sense_margin_mv"], " mV"), "offset/noise included")}
    ${MetricCard("Retention", fmt(m["circuit_physical.retention_ms"], " ms"), "public-model margin")}
    ${MetricCard("Real signoff", "False", "always blocked")}
  </div>
  <div class="grid cols-2"><div class="panel"><h2>Margin proxy</h2>${BarChart([
    { label: "Delta V mV", value: m["circuit_physical.charge_share_delta_v_mv"] || 0, color: "#1d5d8f" },
    { label: "Sense margin mV", value: m["circuit_physical.sense_margin_mv"] || 0, color: "#6d5aa7" },
    { label: "Retention ms", value: m["circuit_physical.retention_ms"] || 0, color: "#0f766e" },
    { label: "WNS proxy ns x100", value: (m["circuit_physical.wns_ns"] || 0) * 100, color: "#b74b3f" },
  ])}</div><div class="panel"><h2>Signoff semantics</h2>${EvidenceTable([
    { name: "Proxy execution", status: m["circuit_physical.proxy_execution_pass"] ? "PASS" : "FAIL", path: "outputs/engine_parsed/*circuit_physical*" },
    { name: "Proxy design", status: m["circuit_physical.proxy_design_pass"] ? "PASS" : "REVIEW", path: "outputs/metric_lineage/*circuit_physical*" },
    { name: "Real signoff", status: "BLOCKED", path: "docs/12_NON_CLAIMS_AND_CLAIMS.md" },
  ])}</div></div>`;
}

function pageFab() {
  const fab = dashboard.fab_operation || {};
  const trajectories = fab.lot_qtime_trajectories || [];
  const lotA = trajectories.find((t) => t.lot_id === "LOT_A")?.points || [];
  const lotB = trajectories.find((t) => t.lot_id === "LOT_B")?.points || [];
  const toPoints = (items) => items.map((p) => ({ x: p.time_min, y: p.qtime_remaining_min }));
  return `<div class="grid cols-4">
    ${MetricCard("Q-time risk", fmt(fab.qtime_risk_index), "S03 judge input")}
    ${MetricCard("Dispatch markers", fmt((fab.dispatch_markers || []).length), "current-run events")}
    ${MetricCard("Metrology delay", fmt(fab.metrology_delay_min, " min"), "delay markers")}
    ${MetricCard("Q over threshold", fmt((fab.q_over_threshold || []).length), "constraint evidence")}
  </div>
  <div class="grid cols-2"><div class="panel"><h2>LOT_A curve</h2>${LineChart(toPoints(lotA), "#b74b3f", "LOT_A q-time remaining")}</div><div class="panel"><h2>LOT_B curve</h2>${LineChart(toPoints(lotB), "#1d5d8f", "LOT_B q-time remaining")}</div></div>
  <div class="grid cols-2"><div class="panel"><h2>Event log with dispatch and metrology markers</h2>${Timeline(fab.events || [])}</div><div class="panel"><h2>Marker evidence</h2>${EvidenceTable([
    { name: "dispatch_marker", status: "PASS", path: `count ${(fab.dispatch_markers || []).length}` },
    { name: "metrology_delay_marker", status: "PASS", path: `count ${(fab.metrology_delay_markers || []).length}` },
    { name: "q_over_threshold", status: (fab.q_over_threshold || []).length ? "REVIEW" : "PASS", path: "outputs/engine_raw/*fab_operation*" },
  ])}</div></div>`;
}

function pageFactory() {
  const scene = dashboard.factory_scene || {};
  return `<div class="grid cols-4">
    ${MetricCard("Nodes", fmt((scene.nodes || []).length), "tool/buffer/metrology")}
    ${MetricCard("Edges", fmt((scene.edges || []).length), "transport links")}
    ${MetricCard("Selected route", (scene.selected_route || []).join(" -> "), "engine-selected")}
    ${MetricCard("Route delay", fmt(scene.route_delay_min, " min"), "congestion-aware")}
  </div>
  <div class="grid cols-2"><div class="panel"><h2>2D factory route map</h2>${RouteMap(scene)}</div><div class="panel"><h2>Route segments and congestion zones</h2>${EvidenceTable([
    { name: "selected_route", status: (scene.selected_route || []).length >= 3 ? "PASS" : "FAIL", path: (scene.selected_route || []).join(" -> ") },
    { name: "route_segments", status: (scene.route_segments || []).length >= 2 ? "PASS" : "FAIL", path: `segments ${(scene.route_segments || []).length}` },
    { name: "congestion_zone", status: (scene.congestion_zones || []).length ? "PASS" : "FAIL", path: `zones ${(scene.congestion_zones || []).length}` },
    { name: "OpenUSD-like export", status: "PUBLIC_MODEL", path: scene.openusd_like_export_path || "outputs/factory_scene/openusd_like_scene.usda" },
  ])}</div></div>`;
}

function pageAudit() {
  return `<div class="panel"><h2>AI judgment to claim boundary</h2>${DecisionFlow(byFamily("S03"))}</div>
  <div class="grid cols-2"><div class="panel"><h2>Canonical audit outcomes</h2>${EvidenceTable((dashboard.ai_audit?.red_team || []).map((r) => ({ name: r.scenario_id, status: r.challenge_emitted ? "CAUGHT" : "ESCAPED_UNTIL_REVEAL", path: `outputs/red_team_challenges/${r.scenario_id}.json` })))}</div><div class="panel"><h2>Supervisor boundary</h2>${EvidenceTable((dashboard.ai_audit?.supervisor || []).map((r) => ({ name: r.scenario_id, status: r.disposition, path: `outputs/supervisor_gate_logs/${r.scenario_id}.json` })))}</div></div>`;
}

function pagePublicTools() {
  const local = Object.values(dashboard.public_tool_evidence?.local?.tools || {});
  const ci = dashboard.public_tool_evidence?.ci || {};
  const ciTools = ci.tools || {};
  return `<div class="grid cols-4">${local.map((r) => MetricCard(r.tool, r.status, "local status")).join("")}</div>
  <div class="grid cols-2"><div class="panel"><h2>Local public-tool receipts</h2>${ReceiptPanel(local)}</div><div class="panel"><h2>GitHub Actions medium evidence</h2>${StatusBadge(ci.status)}<p class="note">${ci.explanation || ci.github_run_url || "CI manifest will be created by the medium workflow."}</p>${EvidenceTable(["ngspice","yosys","verilator","simpy"].map((tool) => ({ name: tool, status: ciTools[tool] || "NOT_PRESENT_IN_LOCAL_ARTIFACT", path: ci.manifest_path || "outputs/public_tool_evidence/ci_run_manifest.json" })))}</div></div>
  <div class="panel"><h2>Boundary</h2><p class="note">Local unavailable is recorded honestly. The final READY state requires a genuine GitHub Actions run URL, commit SHA, and four real tool statuses; this page does not fabricate CI identity.</p></div>`;
}

function pageVariants() {
  return `<div class="grid cols-3">${MetricCard("Variant count", fmt(dashboard.variant_matrix?.variant_count || 0), "minimum 60")}${MetricCard("Routing field", "scenario_family", "no prefix router")}${MetricCard("Sensitivity", "tested", "judge perturbation")}</div><div class="grid cols-3">${VariantMatrix()}</div>`;
}

function pageHynix() {
  return `<div class="grid cols-3">
    ${MetricCard("Autonomous Fab", "Q-time / LOT", "dispatch and downstream risk")}
    ${MetricCard("HBM workload", "GB/s normalized", "bandwidth, thermal, refresh")}
    ${MetricCard("Digital Twin", "route + evidence", "map and traceability")}
  </div><div class="panel"><h2>Alignment with boundaries</h2><p class="note">PUBLIC_SOURCE_SUPPORTED: HBM workload pressure and autonomous fab vocabulary are public industry themes. PROJECT_INTERPRETATION: this repo maps those themes into a reproducible public-model console. USER_POSITIONING: it demonstrates system-building and claim-boundary discipline without implying proprietary access or real product signoff.</p>${EvidenceTable([
    { name: "Hynix alignment doc", status: "PUBLIC_MODEL", path: "docs/03_HYNIX_ALIGNMENT.md" },
    { name: "Non-claims", status: "ENFORCED", path: "docs/12_NON_CLAIMS_AND_CLAIMS.md" },
    { name: "Interview talking points", status: "READY", path: "docs/13_INTERVIEW_TALKING_POINTS_KO.md" },
  ])}</div>`;
}

const renderers = {
  "overview": pageOverview,
  "hbm": pageHbm,
  "circuit": pageCircuit,
  "fab": pageFab,
  "factory": pageFactory,
  "audit": pageAudit,
  "public-tools": pagePublicTools,
  "variants": pageVariants,
  "hynix-alignment": pageHynix,
};

function render() {
  const route = location.hash.replace("#", "") || "overview";
  const selected = routes.find((r) => r[0] === route) ? route : "overview";
  document.querySelector("#page-title").textContent = routes.find((r) => r[0] === selected)[1];
  document.querySelector("#nav").innerHTML = routes.map(([id, title]) => `<button class="nav-link ${id === selected ? "active" : ""}" onclick="location.hash='${id}'">${title}</button>`).join("");
  const m = dashboard.audit_metrics || {};
  document.querySelector("#run-status").innerHTML = [StatusBadge(dashboard.status || "AWAITING_GITHUB_MEDIUM"), StatusBadge(`${m.red_team_caught_or_flagged || 0} caught`), StatusBadge(`${m.red_team_escaped_until_hidden_truth || 0} escaped`)].join("");
  document.querySelector("#app").innerHTML = renderers[selected]();
}

async function start() {
  const response = await fetch("dashboard_data.json", { cache: "no-store" });
  dashboard = await response.json();
  window.addEventListener("hashchange", render);
  render();
}

start().catch((error) => {
  document.querySelector("#app").innerHTML = `<div class="panel"><h2>Dashboard data unavailable</h2><p class="note">${error}</p></div>`;
});
