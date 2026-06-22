from twin_core.io_utils import ROOT, read_json, write_json
def reveal():
    for h in sorted((ROOT/"oracle"/"hidden").glob("S*.json")):
        data=read_json(h); sid=data["scenario_id"]
        label = data.pop("label")
        write_json(ROOT/"outputs"/"hidden_truth_reveals"/f"{sid}.json", {"schema_version":"hynix-v5-hidden-truth-reveal-1", **data, "post_reveal_label": label, "append_only": True})
if __name__ == "__main__":
    reveal()
