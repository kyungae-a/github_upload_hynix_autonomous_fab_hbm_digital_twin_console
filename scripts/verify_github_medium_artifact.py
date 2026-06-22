from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path

REAL = {"REAL_EXTERNAL_RUN", "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN"}
TOOLS = ["ngspice", "yosys", "verilator", "simpy"]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL GitHub medium artifact: {message}")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(root: Path, rel: str) -> dict:
    path = root / rel
    if not path.exists():
        fail(f"missing {rel}")
    return json.loads(path.read_text(encoding="utf-8"))


def verify_root(root: Path) -> None:
    ci = read_json(root, "outputs/public_tool_evidence/ci_run_manifest.json")
    if ci.get("schema_version") != "hynix-v5.4-ci-run-manifest-1":
        fail("bad CI manifest schema")
    if ci.get("status") != "PASS" or not ci.get("github_run_url") or not ci.get("commit_sha"):
        fail("CI identity missing")
    tools = ci.get("tools", {})
    if set(tools) != set(TOOLS) or any(tools[tool] not in REAL for tool in TOOLS):
        fail(f"non-real tool status {tools}")

    state = read_json(root, "docs/v5_4_build_state.json")
    if state.get("schema_version") != "hynix-v5.4-build-state-1":
        fail("bad state schema")
    if state.get("status") != "READY_FOR_GITHUB_REVIEW":
        fail(f"state is not READY_FOR_GITHUB_REVIEW: {state.get('status')}")
    if state.get("phases", {}).get("P11", {}).get("status") != "PASS":
        fail("P11 did not pass")
    if state.get("ci_medium_evidence", {}).get("github_run_url") != ci.get("github_run_url"):
        fail("state CI URL does not match manifest")

    side = read_json(root, "release/hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json")
    archive = root / "release" / "hynix-autonomous-fab-hbm-digital-twin-console.zip"
    if not archive.exists():
        fail("missing release archive")
    if side.get("schema_version") != "hynix-v5.4-release-manifest-1":
        fail("bad release manifest schema")
    if side.get("archive_sha256") != sha(archive):
        fail("release archive hash mismatch")
    if side.get("status") != "READY_FOR_GITHUB_REVIEW":
        fail(f"release sidecar is not READY: {side.get('status')}")
    required_flags = [
        "hbm_unit_normalized",
        "factory_route_map_ready",
        "screenshot_visual_contract_passed",
        "product_docs_contract_passed",
        "github_actions_medium_ready",
    ]
    for flag in required_flags:
        if side.get(flag) is not True:
            fail(f"release sidecar flag not true: {flag}")

    with zipfile.ZipFile(archive) as zf:
        for name in zf.namelist():
            if "\\" in name or name.startswith("/") or ".." in Path(name).parts:
                fail(f"unsafe zip entry {name}")
            if name.startswith(("private_inputs/", "private_work/", "reference/")) or "__pycache__" in name or name.endswith(".pyc"):
                fail(f"forbidden zip entry {name}")
    print("PASS GitHub medium artifact")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True, help="GitHub artifact directory or downloaded artifact zip")
    args = parser.parse_args()
    target = Path(args.artifact)
    if target.is_file():
        with tempfile.TemporaryDirectory(prefix="hynix_v54_artifact_") as tmp:
            with zipfile.ZipFile(target) as zf:
                for name in zf.namelist():
                    if "\\" in name or name.startswith("/") or ".." in Path(name).parts:
                        fail(f"unsafe artifact entry {name}")
                zf.extractall(tmp)
            verify_root(Path(tmp))
    else:
        verify_root(target)


if __name__ == "__main__":
    main()
