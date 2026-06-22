#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASES = [f"P{i:02d}" for i in range(12)]
REAL = {"REAL_EXTERNAL_RUN", "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN"}

def fail(msg: str) -> None:
    raise ValueError(msg)

def validate(state: dict) -> None:
    if state.get("schema_version") != "hynix-v5.4-build-state-1": fail("state schema")
    if list(state.get("phases", {})) != PHASES: fail("phase order")
    if state.get("legacy_v5_3_ready_trusted_for_v5_4") is not False: fail("legacy READY trusted")
    statuses=[state["phases"][p].get("status") for p in PHASES]
    allowed={"PENDING","IN_PROGRESS","PASS","BLOCKED"}
    if any(s not in allowed for s in statuses): fail("invalid phase status")
    passed_prefix=True
    for i,s in enumerate(statuses):
        if s=="PASS" and not passed_prefix: fail(f"phase {PHASES[i]} passed before predecessor")
        if s!="PASS": passed_prefix=False
        if s=="PASS":
            rec=state["phases"][PHASES[i]]
            if not rec.get("gate_receipts") or not rec.get("review_receipts"): fail(f"{PHASES[i]} missing receipts")
            if rec.get("open_p0_p1"): fail(f"{PHASES[i]} open P0/P1")
    status=state.get("status")
    if status not in {"REWORK_REQUIRED","IN_PROGRESS","AWAITING_GITHUB_MEDIUM","READY_FOR_GITHUB_REVIEW"}: fail("invalid build status")
    ci=state.get("ci_medium_evidence", {})
    if status=="AWAITING_GITHUB_MEDIUM":
        if any(state["phases"][p]["status"]!="PASS" for p in PHASES[:-1]): fail("awaiting CI before local phases complete")
        if state["phases"]["P11"]["status"]=="PASS": fail("awaiting CI with P11 pass")
    if status=="READY_FOR_GITHUB_REVIEW":
        if any(s!="PASS" for s in statuses): fail("READY with phase not pass")
        if ci.get("status")!="PASS" or not ci.get("github_run_url") or not ci.get("commit_sha"): fail("READY without trusted CI identity")
        if any(v not in REAL for v in ci.get("tools", {}).values()): fail("READY without four real tool statuses")
        if any(v!="PASS" for v in state.get("final_gates", {}).values()): fail("READY with final gate not pass")
        if any(v!="PASS" for v in state.get("final_reviewers", {}).values()): fail("READY with reviewer not pass")
        rel=state.get("release", {})
        if not rel.get("archive_sha256") or rel.get("manifest_schema_version")!="hynix-v5.4-release-manifest-1": fail("READY without v5.4 release")
        if any(x in str(rel.get("archive_path", "")) for x in ["..","\\"]): fail("unsafe release path")

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--state", default=str(ROOT/"docs/v5_4_build_state.json")); args=ap.parse_args()
    try:
        state=json.loads(Path(args.state).read_text(encoding="utf-8")); validate(state)
    except Exception as exc:
        raise SystemExit(f"FAIL v5.4 state: {exc}")
    print("PASS v5.4 state")
if __name__=="__main__": main()
