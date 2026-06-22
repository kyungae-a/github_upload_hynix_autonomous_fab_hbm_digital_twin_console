from twin_core.io_utils import ROOT, read_json, write_json
def run_meta():
    for p in sorted((ROOT/"outputs"/"red_team_challenges").glob("S*.json")):
        red=read_json(p); status="VISIBLE_LOGIC_INCOMPLETE" if red["challenge_emitted"] else "VISIBLE_LOGIC_PLAUSIBLE_BUT_UNCHALLENGED"
        action="REQUIRES_REAL_DOMAIN_SIGNOFF" if red["challenge_emitted"] else "APPROVE_FOR_SIMULATION_REVIEW"
        write_json(ROOT/"outputs"/"meta_judge_outputs"/f"{red['scenario_id']}.json", {"schema_version":"hynix-v5-meta-judge-1","scenario_id":red["scenario_id"],"scenario_family":red.get("scenario_family"),"canonical_parent":red.get("canonical_parent"),"visible_logic_status":status,"recommended_supervisor_action":action,"visible_only":True})
