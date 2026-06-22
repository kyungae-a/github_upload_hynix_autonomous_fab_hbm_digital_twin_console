from twin_core.io_utils import ROOT, read_json, write_json
def challenge(packet, judgment):
    sid = packet["scenario_id"]
    family = packet.get("scenario_family") or packet.get("canonical_parent") or sid
    if family == "S01":
        emitted=False; typ="thermal_boundary_not_visible"; msg="No reliable model-age signal is visible; this escapes until reveal."
    elif family == "S02":
        emitted=True; typ="hard_constraint_gap"; msg="Reliability hard constraints must precede PPA score."
    elif family == "S03":
        emitted=True; typ="local_global_flow_gap"; msg="Local dispatch may harm downstream q-time."
    elif family == "S04":
        emitted=True; typ="observability_gap"; msg="Metrology lag and drift weaken stable-sensor inference."
    elif family == "S05":
        emitted=True; typ="tail_risk_gap"; msg="Average improvement may hide p99 tail risk."
    else:
        emitted=True; typ="proxy_signoff_boundary"; msg="Execution pass is not product signoff."
    return {"schema_version":"hynix-v5-red-team-1","scenario_id":sid,"scenario_family":family,"canonical_parent":packet.get("canonical_parent"),"target_decision":judgment["decision_id"],"challenge_emitted":emitted,"challenge_type":typ,"challenge":msg,"visible_only":True}
def run_red_team():
    for path in sorted((ROOT/"outputs"/"evidence_packets").glob("S*.json")):
        packet=read_json(path); judgment=read_json(ROOT/"outputs"/"ai_judgments"/f"{packet['scenario_id']}.json")
        write_json(ROOT/"outputs"/"red_team_challenges"/f"{packet['scenario_id']}.json", challenge(packet, judgment))
