from __future__ import annotations
from pathlib import Path
from twin_core.io_utils import ROOT, sha_file, sha_obj, write_json
EPOCH = "2026-06-22T00:00:00Z"

def internal_receipt(engine_name: str, scenario: dict, code_path: Path, raw: dict, parsed: dict, lineage: dict):
    input_hash = sha_obj({"scenario": scenario, "engine": engine_name})
    run_id = f"{engine_name}-{scenario['scenario_id']}-{input_hash[:10]}"
    raw_rel = f"outputs/engine_raw/{run_id}.json"
    parsed_rel = f"outputs/engine_parsed/{run_id}.json"
    lineage_rel = f"outputs/metric_lineage/{run_id}.json"
    write_json(ROOT / raw_rel, raw)
    write_json(ROOT / parsed_rel, parsed)
    write_json(ROOT / lineage_rel, lineage)
    receipt = {
        "run_id": run_id, "engine_name": engine_name, "status": "REAL_INTERNAL_RUN",
        "scenario_id": scenario["scenario_id"],
        "scenario_family": scenario.get("scenario_family", scenario.get("canonical_parent", scenario["scenario_id"])),
        "canonical_parent": scenario.get("canonical_parent", scenario.get("scenario_family", scenario["scenario_id"])),
        "engine_version": "v5.2-public-model",
        "command": f"python -B -m twin_core.scenario_runner --engine {engine_name}",
        "relative_cwd": ".", "environment": "local-stdlib", "seed": scenario.get("seed", 0),
        "code_sha256": sha_file(code_path), "input_sha256": input_hash, "exit_status": 0,
        "deterministic_start": EPOCH, "deterministic_end": EPOCH,
        "raw_output_path": raw_rel, "raw_output_sha256": sha_file(ROOT / raw_rel),
        "parsed_output_path": parsed_rel, "parsed_output_sha256": sha_file(ROOT / parsed_rel),
        "metric_lineage_path": lineage_rel, "metric_lineage_sha256": sha_file(ROOT / lineage_rel),
    }
    write_json(ROOT / "outputs" / "run_receipts" / f"{run_id}.json", receipt)
    return {"run_id": run_id, "receipt": receipt, "raw": raw, "parsed": parsed, "lineage": lineage}
