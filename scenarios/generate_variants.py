from __future__ import annotations
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from twin_core.io_utils import read_json, write_json

def main():
    variants = []
    canonical = [read_json(p) for p in sorted((ROOT / "scenarios" / "canonical").glob("S*.yaml"))]
    for i in range(60):
        base = canonical[i % len(canonical)]
        scale = 0.82 + (i % 10) * 0.04
        v = json.loads(json.dumps(base))
        v["variant_id"] = f"V{i+1:03d}_{base['scenario_id']}"
        v["scenario_id"] = v["variant_id"]
        v["canonical_parent"] = base["scenario_id"]
        v["scenario_family"] = base["scenario_id"]
        v["variant_axis"] = ["thermal", "retention", "qtime", "metrology", "tail", "governance"][i % 6]
        v["seed"] = int(base["seed"]) + i + 1000
        for key, value in list(v["inputs"].items()):
            if isinstance(value, (int, float)) and "allowed" not in key:
                v["inputs"][key] = round(value * scale, 6)
        path = ROOT / "scenarios" / "variants" / "generated" / f"{v['variant_id']}.json"
        write_json(path, v)
        variants.append({"variant_id": v["variant_id"], "parent": base["scenario_id"], "scenario_family": base["scenario_id"], "axis": v["variant_axis"], "path": path.relative_to(ROOT).as_posix()})
    write_json(ROOT / "scenarios" / "variants" / "variant_index.json", {"variant_count": len(variants), "variants": variants})
    print(f"generated {len(variants)} variants")

if __name__ == "__main__":
    main()
