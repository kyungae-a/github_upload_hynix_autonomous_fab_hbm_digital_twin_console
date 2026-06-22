from __future__ import annotations
from copy import deepcopy
from twin_core.io_utils import ROOT, read_json, write_json

def decide(packet):
    m = packet["visible_metrics"]; q = packet["question"]
    family = packet.get("scenario_family") or packet.get("canonical_parent") or packet["scenario_id"]
    trace = []
    if family == "S01":
        bw = m.get("memory_system.sustained_bandwidth_gbps", 0); floor = packet["constraints"].get("min_sustained_gbps", 0); pressure = m.get("memory_system.thermal_pressure_index", 0)
        decision = "change_memory_policy_inside_visible_twin" if bw < floor and pressure < 0.2 else "request_thermal_boundary_evidence"
        conf = 0.72 if decision.startswith("change") else 0.54
        trace.append({"expr": f"sustained {bw} floor {floor} pressure {pressure}", "result": decision})
    elif family == "S02":
        a = m.get("memory_system.ppa_candidate_a_score", 0); b = m.get("memory_system.ppa_candidate_b_score", 0); ret = m.get("circuit_physical.retention_ms", 999)
        decision = "select_candidate_b_until_hard_constraints_pass" if ret < packet["constraints"].get("min_retention_ms", 64) else ("select_candidate_a" if a > b else "select_candidate_b")
        conf = 0.76
        trace.append({"expr": f"A {a} B {b} retention {ret}", "result": decision})
    elif family == "S03":
        qri = m.get("fab_operation.qtime_risk_index", 0); local = m.get("fab_operation.local_dispatch_score", 0)
        decision = "prioritize_lot_b_local_window" if local > 0.6 and qri < 0.45 else "protect_lot_a_qtime_or_request_global_flow"
        conf = 0.69
        trace.append({"expr": f"local {local} qtime {qri}", "result": decision})
    elif family == "S04":
        obs = m.get("fab_operation.observability_risk_index", 0)
        decision = "continue_with_monitoring" if obs < 0.85 else "stop_for_metrology_confirmation"
        conf = 0.63
        trace.append({"expr": f"observability {obs}", "result": decision})
    elif family == "S05":
        avg = m.get("fab_operation.avg_defect_delta_pct", 0); tail = m.get("fab_operation.tail_risk_index", 0)
        decision = "bounded_recipe_pilot" if avg < 0 and tail < 0.35 else "hold_for_tail_risk_evidence"
        conf = 0.66
        trace.append({"expr": f"avg {avg} tail {tail}", "result": decision})
    else:
        exec_pass = m.get("circuit_physical.proxy_execution_pass", False); design = m.get("circuit_physical.proxy_design_pass", False); signoff = m.get("circuit_physical.real_signoff_claim_allowed", False)
        decision = "claim_proxy_evidence_only" if exec_pass and not signoff else "request_more_evidence"
        conf = 0.61
        trace.append({"expr": f"exec {exec_pass} design {design} signoff {signoff}", "result": decision})
    return {"profile": "EvidenceSensitiveRuleJudge", "decision": decision, "confidence": conf, "decision_rule_trace": trace}

def perturb(packet):
    p = deepcopy(packet)
    family = packet.get("scenario_family") or packet.get("canonical_parent") or packet["scenario_id"]
    if family == "S01":
        p["visible_metrics"]["memory_system.sustained_bandwidth_gbps"] = p["constraints"].get("min_sustained_gbps", 0) - 1000
        p["visible_metrics"]["memory_system.thermal_pressure_index"] = 0.01
    elif family == "S02":
        p["visible_metrics"]["circuit_physical.retention_ms"] = 1
    elif family == "S03":
        p["visible_metrics"]["fab_operation.local_dispatch_score"] = 0.95
        p["visible_metrics"]["fab_operation.qtime_risk_index"] = 0.05
    elif family == "S04":
        p["visible_metrics"]["fab_operation.observability_risk_index"] = 0.95
    elif family == "S05":
        p["visible_metrics"]["fab_operation.tail_risk_index"] = 0.05
        p["visible_metrics"]["fab_operation.avg_defect_delta_pct"] = -8
    else:
        p["visible_metrics"]["circuit_physical.proxy_execution_pass"] = False
    return p

def run_judges(packet_only=None):
    if packet_only is not None:
        return decide(packet_only)
    for path in sorted((ROOT/"outputs"/"evidence_packets").glob("S*.json")):
        packet = read_json(path); result = decide(packet)
        out = {"schema_version":"hynix-v5-ai-judgment-1", "scenario_id": packet["scenario_id"], "scenario_family": packet.get("scenario_family"), "canonical_parent": packet.get("canonical_parent"), "decision_id": f"{packet['scenario_id']}-JDG-001", **result, "visible_evidence_used": sorted(packet["visible_metrics"].keys()), "hidden_access": False}
        write_json(ROOT/"outputs"/"ai_judgments"/f"{packet['scenario_id']}.json", out)
