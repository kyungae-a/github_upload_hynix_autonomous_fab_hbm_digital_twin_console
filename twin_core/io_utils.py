from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def stable(data) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
def sha_obj(data) -> str:
    return hashlib.sha256(stable(data)).hexdigest()
def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))
def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    tmp = path.with_name(f"{path.name}.tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)
def canonical_scenarios():
    items = []
    for p in sorted((ROOT / "scenarios" / "canonical").glob("S*.yaml")):
        item = read_json(p)
        item.setdefault("scenario_family", item["scenario_id"])
        item.setdefault("canonical_parent", item["scenario_id"])
        items.append(item)
    return items
def variant_scenarios():
    items = []
    for p in sorted((ROOT / "scenarios" / "variants" / "generated").glob("*.json")):
        item = read_json(p)
        parent = item.get("canonical_parent") or item.get("scenario_family")
        item.setdefault("scenario_family", parent)
        items.append(item)
    return items
def ensure_dirs():
    for d in ["run_receipts","engine_raw","engine_parsed","public_tool_receipts","evidence_packets","ai_judgments","red_team_challenges","meta_judge_outputs","supervisor_gate_logs","hidden_truth_reveals","metric_lineage","casebook","scenario_variant_results","factory_scene","dashboard","build_receipts"]:
        (ROOT / "outputs" / d).mkdir(parents=True, exist_ok=True)
