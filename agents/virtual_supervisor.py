from twin_core.io_utils import ROOT, read_json, write_json
def run_supervisor():
    for p in sorted((ROOT/"outputs"/"meta_judge_outputs").glob("S*.json")):
        meta=read_json(p); sid=meta["scenario_id"]
        family = meta.get("scenario_family") or meta.get("canonical_parent") or sid
        disposition = "REQUIRES_REAL_DOMAIN_SIGNOFF" if family!="S06" else "REWORD_AS_PROXY_ONLY"
        write_json(ROOT/"outputs"/"supervisor_gate_logs"/f"{sid}.json", {"schema_version":"hynix-v5-supervisor-1","scenario_id":sid,"scenario_family":family,"canonical_parent":meta.get("canonical_parent"),"disposition":disposition,"approved_claim":"public-model portfolio evidence only","blocked_claim":"real fab/product/signoff approval","requires_real_signoff":True,"human_impersonation":False})
