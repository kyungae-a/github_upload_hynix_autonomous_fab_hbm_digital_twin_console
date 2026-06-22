def compute_couplings(parsed):
    out = []
    mem = parsed.get("memory_system", {}); fab = parsed.get("fab_operation", {}); circ = parsed.get("circuit_physical", {}); scene = parsed.get("factory_scene", {})
    if mem and fab:
        out.append({"from": "memory.thermal_pressure", "to": "fab.tail_risk", "value": round(1+mem.get("thermal_pressure_index",0)*0.35,6)})
    if circ:
        out.append({"from": "circuit.proxy_design_pass", "to": "supervisor.signoff_boundary", "value": bool(circ.get("proxy_design_pass")) and bool(circ.get("real_signoff_claim_allowed"))})
    if scene and fab:
        out.append({"from": "factory.route_congestion", "to": "fab.qtime_risk", "value": scene.get("qtime_routing_multiplier",1)})
    return out
