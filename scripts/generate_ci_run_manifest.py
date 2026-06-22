from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from twin_core.io_utils import ROOT, sha_file, write_json

REAL = {"REAL_EXTERNAL_RUN", "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN"}
TOOLS = ["ngspice", "yosys", "verilator", "simpy"]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    commit = os.environ.get("GITHUB_SHA", "")
    if not run_id or not repo or not commit:
        raise SystemExit("FAIL CI manifest: GitHub Actions identity variables are missing")

    receipts = {}
    statuses = {}
    for tool in TOOLS:
        path = ROOT / "outputs" / "public_tool_receipts" / f"{tool}.json"
        if not path.exists():
            raise SystemExit(f"FAIL CI manifest: missing {tool} receipt")
        receipt = read_json(path)
        statuses[tool] = receipt.get("status")
        receipts[tool] = {
            "receipt_path": path.relative_to(ROOT).as_posix(),
            "receipt_sha256": sha_file(path),
            "status": receipt.get("status"),
            "command": receipt.get("command"),
        }
    if any(status not in REAL for status in statuses.values()):
        raise SystemExit(f"FAIL CI manifest: non-real tool status {statuses}")

    manifest = {
        "schema_version": "hynix-v5.4-ci-run-manifest-1",
        "status": "PASS",
        "workflow": os.environ.get("GITHUB_WORKFLOW", "medium"),
        "commit_sha": commit,
        "github_run_url": f"{server}/{repo}/actions/runs/{run_id}",
        "tools": statuses,
        "receipts": receipts,
        "public_model_only": True,
        "real_signoff_claim": False,
    }
    write_json(ROOT / "outputs" / "public_tool_evidence" / "ci_run_manifest.json", manifest)
    print("PASS CI run manifest")


if __name__ == "__main__":
    main()
