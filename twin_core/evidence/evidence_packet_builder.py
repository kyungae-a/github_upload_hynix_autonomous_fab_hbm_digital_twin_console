from __future__ import annotations
from twin_core.memory_system.hbm_workload_engine import run_memory_system
from twin_core.circuit_physical.read_path_model import run_circuit_physical
from twin_core.fab_operation.discrete_event_engine import run_fab_operation
from twin_core.factory_scene.scene_graph import run_factory_scene
from twin_core.coupling.cross_twin_coupling import compute_couplings
from twin_core.io_utils import ROOT, sha_obj, write_json

def build_packet(scenario: dict, public_receipts: list[dict] | None = None):
    results = []
    if "memory_system" in scenario["twin_scope"]: results.append(run_memory_system(scenario))
    if "circuit_physical" in scenario["twin_scope"]: results.append(run_circuit_physical(scenario))
    if "fab_operation" in scenario["twin_scope"]: results.append(run_fab_operation(scenario))
    if "factory_scene" in scenario["twin_scope"]: results.append(run_factory_scene(scenario))
    parsed = {r["parsed"]["domain"]: r["parsed"] for r in results}
    metrics = {}
    lineage = {}
    for r in results:
        dom = r["parsed"]["domain"]
        for k, v in r["parsed"].items():
            if k == "domain": continue
            if isinstance(v, (int, float, bool, str)):
                metrics[f"{dom}.{k}"] = v
                lineage[f"{dom}.{k}"] = {"run_id": r["run_id"], "formula": r["lineage"].get(k, "engine-derived")}
    packet = {
        "schema_version": "hynix-v5-evidence-packet-1", "scenario_id": scenario["scenario_id"],
        "scenario_family": scenario.get("scenario_family", scenario.get("canonical_parent", scenario["scenario_id"])),
        "canonical_parent": scenario.get("canonical_parent", scenario.get("scenario_family", scenario["scenario_id"])),
        "variant_id": scenario.get("variant_id"),
        "title": scenario["title"], "question": scenario["question"], "twin_scope": scenario["twin_scope"],
        "engine_run_ids": [r["run_id"] for r in results], "engine_provenance": [r["receipt"] for r in results],
        "public_tool_receipts": public_receipts or [], "computed_state": parsed, "visible_metrics": metrics,
        "metric_lineage": lineage, "cross_twin_coupling": compute_couplings(parsed),
        "input_hash": sha_obj(scenario), "claim_limits": ["public_model_only", "requires_real_domain_signoff"],
        "constraints": scenario.get("constraints", {}), "packet_sha256": None,
    }
    packet["packet_sha256"] = sha_obj({k:v for k,v in packet.items() if k != "packet_sha256"})
    write_json(ROOT / "outputs" / "evidence_packets" / f"{scenario['scenario_id']}.json", packet)
    return packet
