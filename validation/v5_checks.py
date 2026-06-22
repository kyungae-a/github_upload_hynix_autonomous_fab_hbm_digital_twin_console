from __future__ import annotations
import hashlib, json, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
REAL_PUBLIC = {"REAL_EXTERNAL_RUN","REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN"}
HONEST_PUBLIC = REAL_PUBLIC | {"EXPLAINED_UNAVAILABLE", "FAILED_WITH_EXPLANATION"}
REQ_PUBLIC_TOOLS = {"ngspice", "yosys", "verilator", "simpy"}
REQ_SCREENSHOTS = ["01_architecture.png","02_fab_qtime_timeline.png","03_hbm_workload_policy_compare.png","04_factory_scene_routing.png","05_public_tool_evidence.png","06_ai_judgment_audit_flow.png","07_hynix_alignment.png"]
COMPAT_SCREENSHOTS = ["architecture.png","fab_timeline.png","hbm_workload.png","factory_scene.png","public_tool_evidence.png","ai_audit_flow.png","hidden_truth_reveal.png","hynix_alignment.png"]
def fail(msg): print(msg, file=sys.stderr); raise SystemExit(1)
def read(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(p): return Path(p).relative_to(ROOT).as_posix()
def packets(): return [read(p) for p in sorted((ROOT/"outputs"/"evidence_packets").glob("S*.json"))]
def receipts(): return [read(p) for p in sorted((ROOT/"outputs"/"run_receipts").glob("*.json"))]
def public_receipts(): return [read(p) for p in sorted((ROOT/"outputs"/"public_tool_receipts").glob("*.json")) if p.name not in {"ngspice_raw.json","ngspice_parsed.json","yosys_raw.json","yosys_parsed.json","verilator_raw.json","verilator_parsed.json","simpy_raw.json","simpy_parsed.json"}]
def state():
    path = ROOT/"docs"/"v5_4_build_state.json"
    if path.exists(): return read(path)
    path = ROOT/"docs"/"v5_3_build_state.json"
    if path.exists(): return read(path)
    path = ROOT/"docs"/"v5_2_build_state.json"
    return read(path if path.exists() else ROOT/"docs"/"v5_build_state.json")

def validate_real_run_counts():
    engines={r["engine_name"] for r in receipts() if r["status"]=="REAL_INTERNAL_RUN"}
    if len(engines)<4: fail(f"expected 4 internal engines, got {engines}")
    by_tool={r.get("tool"): r for r in public_receipts() if r.get("tool") in REQ_PUBLIC_TOOLS}
    if set(by_tool) != REQ_PUBLIC_TOOLS: fail(f"missing public tool attempts {REQ_PUBLIC_TOOLS - set(by_tool)}")
    bad=[t for t,r in by_tool.items() if r.get("status") not in HONEST_PUBLIC]
    if bad: fail(f"dishonest/unknown public tool status {bad}")
    print("PASS real internal counts and honest public attempts")
def validate_no_all_mock_release():
    if read(ROOT/"outputs"/"audit_metrics.json").get("all_mock_release") is not False: fail("all mock")
    print("PASS no all-mock")
def validate_engine_computed_evidence():
    for p in packets():
        if not p["engine_run_ids"] or not p["engine_provenance"]: fail("missing engine provenance")
        if len(p["metric_lineage"])<5: fail("weak metric lineage")
    print("PASS engine computed evidence")
def validate_public_tool_receipts():
    checked=[r for r in public_receipts() if r.get("tool") in REQ_PUBLIC_TOOLS]
    if {r.get("tool") for r in checked} != REQ_PUBLIC_TOOLS: fail("missing required public tool receipt")
    for r in checked:
        for k in ["tool","status","command","raw_output_path","raw_output_sha256","parsed_output_path","parsed_output_sha256","exit_status","parsed_metrics_path"]:
            if k not in r: fail(f"public receipt missing {k}")
        if not isinstance(r["command"], list): fail("public command must be argv list")
        if sha(ROOT/r["raw_output_path"]) != r["raw_output_sha256"]: fail("raw public hash mismatch")
        if sha(ROOT/r["parsed_output_path"]) != r["parsed_output_sha256"]: fail("parsed public hash mismatch")
        if r["status"] == "REAL_EXTERNAL_RUN" and (not r.get("executable_path") or r.get("returncode") != 0):
            fail(f"fake REAL_EXTERNAL_RUN for {r['tool']}")
        if r["status"] == "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN" and r["tool"] != "simpy":
            fail(f"fake reproducible public package status for {r['tool']}")
    print("PASS public tool receipts")
def validate_ai_judges_not_scripted():
    for p in sorted((ROOT/"outputs"/"ai_judgments").glob("S*.json")):
        j=read(p)
        if not j.get("decision_rule_trace"): fail("scripted-looking judge")
        if j.get("hidden_access"): fail("judge hidden access")
    print("PASS AI judges not scripted")
def validate_judge_sensitivity():
    from agents.rule_based_judges import decide, perturb
    changed=0
    for p in packets():
        if decide(p)["decision"] != decide(perturb(p))["decision"]: changed+=1
    if changed<5: fail(f"weak sensitivity {changed}")
    print("PASS judge sensitivity")
def validate_red_team_partial_miss():
    reds=[read(p) for p in sorted((ROOT/"outputs"/"red_team_challenges").glob("S*.json"))]
    caught=sum(1 for r in reds if r["challenge_emitted"])
    if caught not in (4,5) or caught==6: fail(f"bad red-team count {caught}")
    print("PASS red-team partial miss")
def validate_hidden_truth_isolation():
    hidden_tokens=["failure_mode","hidden_truth","post_reveal_label"]
    for folder in ["evidence_packets","ai_judgments","red_team_challenges","meta_judge_outputs","supervisor_gate_logs"]:
        for p in (ROOT/"outputs"/folder).glob("S*.json"):
            text=p.read_text(encoding="utf-8")
            if any(t in text for t in hidden_tokens): fail(f"hidden leak {rel(p)}")
    print("PASS hidden truth isolation")
def validate_supervisor_non_overclaim():
    for p in (ROOT/"outputs"/"supervisor_gate_logs").glob("S*.json"):
        g=read(p)
        if g["requires_real_signoff"] is not True or g["human_impersonation"] is not False: fail("bad supervisor")
    print("PASS supervisor non-overclaim")
def validate_scenario_question_coverage():
    items=[read(p) for p in sorted((ROOT/"scenarios"/"canonical").glob("S*.yaml"))]
    if [x["scenario_id"] for x in items] != ["S01","S02","S03","S04","S05","S06"]: fail("bad canonical ids")
    if any(not x.get("question") for x in items): fail("missing question")
    print("PASS scenario question coverage")
def validate_variant_suite():
    idx=read(ROOT/"scenarios"/"variants"/"variant_index.json")
    matrix=read(ROOT/"outputs"/"scenario_variant_results"/"variant_matrix.json")
    if idx["variant_count"]<60 or matrix["variant_count"]<60: fail("variant count")
    for item in idx["variants"][:12]:
        if item.get("scenario_family") != item.get("parent"): fail("variant missing scenario_family")
    from agents.rule_based_judges import decide
    probes = [("V001_S01","S01"),("V002_S02","S02"),("V003_S03","S03"),("V004_S04","S04"),("V005_S05","S05"),("V006_S06","S06")]
    for sid, family in probes:
        packet={"scenario_id":sid,"scenario_family":family,"canonical_parent":family,"question":"routing probe","constraints":{},"visible_metrics":{}}
        if not decide(packet)["decision"]: fail(f"variant routing failed {sid}")
    print("PASS variant suite")
def validate_dashboard_contract():
    path=ROOT/"outputs"/"dashboard_data.json"
    d=read(path if path.exists() else ROOT/"frontend"/"dashboard_data.json")
    if d.get("schema_version")!="hynix-v5.4-dashboard-data-1": fail("dashboard is not v5.4 schema")
    required={"architecture","hbm_memory","hbm_workload","circuit_physical","fab_operation","factory_scene","public_tool_evidence","ai_audit","variant_matrix","hynix_alignment","source_artifacts"}
    if len(d.get("pages",[]))<9 or not required.issubset(d): fail("dashboard pages")
    hbm=d["hbm_memory"]
    raw=hbm.get("raw_metrics", {})
    display=hbm.get("display_metrics", {})
    if not raw or not display or hbm.get("unit_notes", {}).get("conversion")!="GB/s = Gbps / 8":
        fail("missing HBM raw/display unit contract")
    for raw_key, raw_value in raw.items():
        display_key=raw_key.replace("_gbps","_GBps")
        item=display.get(display_key, {})
        if abs(float(item.get("value", -1)) - float(raw_value)/8.0) > 1e-6:
            fail(f"HBM unit conversion mismatch {raw_key}")
    if len(hbm.get("policy_comparison", []))<3 or not hbm.get("recommended_policy"):
        fail("missing HBM policy comparison")
    factory=d["factory_scene"]
    for key in ["nodes","edges","selected_route","route_segments","congestion_zones","route_cost","route_delay_min","openusd_like_export_path"]:
        if key not in factory: fail(f"factory missing {key}")
    if len(factory["nodes"])<5 or len(factory["edges"])<5 or len(factory["selected_route"])<3:
        fail("weak factory route graph")
    fab=d["fab_operation"]
    lots={item.get("lot_id") for item in fab.get("lot_qtime_trajectories", [])}
    if not {"LOT_A","LOT_B"}.issubset(lots) or not fab.get("dispatch_markers") or not fab.get("metrology_delay_markers"):
        fail("fab timeline missing dual LOT trajectories or markers")
    pub=d["public_tool_evidence"]
    if "local" not in pub or "ci" not in pub: fail("public tools must separate local and CI")
    html=(ROOT/"frontend"/"index.html").read_text(encoding="utf-8")
    app=(ROOT/"frontend"/"app.js").read_text(encoding="utf-8")
    css=(ROOT/"frontend"/"styles.css").read_text(encoding="utf-8")
    routes=["overview","hbm","circuit","fab","factory","audit","public-tools","variants","hynix-alignment"]
    components=["MetricCard","StatusBadge","LineChart","BarChart","Timeline","RouteMap","EvidenceTable","DecisionFlow","ReceiptPanel","VariantMatrix"]
    if any(f"\"{r}\"" not in app and f"'{r}'" not in app for r in routes): fail("missing frontend route")
    if any(c not in app for c in components): fail("missing frontend component")
    if "<pre>" in html or "JSON.stringify" in html: fail("JSON dump main UI")
    if "dashboard.status = \"READY_FOR_GITHUB_REVIEW\"" in app or "factory_scene_raw || scene.raw" in app or "fallbackEvents" in app:
        fail("frontend contains forbidden v5.3 fallback/status shortcut")
    if "theoretical_bandwidth_gbps\"], \" GB/s" in app or "sustained_bandwidth_gbps\"], \" GB/s" in app:
        fail("frontend labels raw gbps as GB/s")
    if len(css) < 6000: fail("shallow frontend styling")
    print("PASS dashboard")
def validate_release_hygiene():
    bad=[rel(p) for p in ROOT.rglob("*") if "__pycache__" in p.parts or p.suffix==".pyc"]
    if bad: fail("cache artifacts " + ",".join(bad[:5]))
    print("PASS release hygiene")
def validate_github_screenshots():
    for name in REQ_SCREENSHOTS + COMPAT_SCREENSHOTS:
        p=ROOT/"screenshots"/name
        side=ROOT/"screenshots"/f"{name}.json"
        if not p.exists() or p.stat().st_size<20000: fail(f"missing browser screenshot {name}")
        info=read(side) if side.exists() else {}
        if info.get("capture_kind") != "headless_browser_file_route" or not info.get("browser_version"): fail(f"missing browser screenshot sidecar {name}")
        data=p.read_bytes()
        if len(set(data[:5000]))<20: fail(f"placeholder-like screenshot {name}")
    manifest=read(ROOT/"screenshots"/"screenshot_manifest.json")
    if manifest.get("schema_version")!="hynix-v5.4-browser-screenshot-manifest-1": fail("wrong screenshot manifest schema")
    if len(manifest.get("screenshots",[]))<len(REQ_SCREENSHOTS): fail("weak screenshot manifest")
    print("PASS screenshots")
def validate_negative_fixtures():
    names={p.name for p in (ROOT/"validation"/"negative_fixtures").glob("*.json")}
    req={"all_mock_release.json","scripted_judge_output.json","hidden_truth_leak.json","supervisor_overclaim.json","missing_metric_lineage.json"}
    if names != req: fail("negative fixtures mismatch")
    print("PASS negative fixtures")
def validate_metric_lineage(): validate_engine_computed_evidence()
def validate_fab_event_timeline():
    if not any("event_timeline" in p.read_text(encoding="utf-8") for p in (ROOT/"outputs"/"engine_raw").glob("*fab_operation_twin*.json")): fail("no fab timeline")
    print("PASS fab event timeline")
def validate_factory_scene_contract():
    for p in ["outputs/factory_scene/fab_layout.json","outputs/factory_scene/scene_graph.json","outputs/factory_scene/openusd_like_scene.usda"]:
        if not (ROOT/p).exists(): fail(f"missing {p}")
    print("PASS factory scene")
def validate_variant_engine_receipts(): validate_variant_suite()
def validate_meta_judge_scope():
    for p in (ROOT/"outputs"/"meta_judge_outputs").glob("S*.json"):
        if read(p).get("visible_only") is not True: fail("meta not visible-only")
    print("PASS meta scope")
def validate_audit_metrics():
    m=read(ROOT/"outputs"/"audit_metrics.json")
    if m["real_internal_run_count"]<4 or m.get("public_tool_attempt_count",0)<4 or m["red_team_caught_or_flagged"] not in (4,5): fail("bad audit metrics")
    print("PASS audit metrics")
def validate_hynix_alignment_claims():
    text=(ROOT/"docs"/"03_HYNIX_ALIGNMENT.md").read_text(encoding="utf-8") + (ROOT/"docs"/"13_INTERVIEW_TALKING_POINTS_KO.md").read_text(encoding="utf-8")
    if "PROJECT_INTERPRETATION" not in text or "proprietary" in text.casefold() and "No" not in text: fail("bad Hynix claims")
    print("PASS Hynix alignment")
def validate_readme_depth():
    text=(ROOT/"README.md").read_text(encoding="utf-8")
    for phrase in ["Four executable core twins","60 generated variants","GitHub Actions","screenshots"]:
        if phrase not in text: fail(f"README missing {phrase}")
    required_docs=[
        "docs/05_HBM_WORKLOAD_TWIN.md",
        "docs/07_FAB_OPERATION_TWIN.md",
        "docs/08_FACTORY_SCENE_ROUTING_TWIN.md",
        "docs/09_AI_JUDGMENT_AUDIT_LAYER.md",
        "docs/11_IMPLEMENTATION_EVIDENCE.md",
    ]
    for doc in required_docs:
        body=(ROOT/doc).read_text(encoding="utf-8")
        if len(body.split()) < 120:
            fail(f"product doc too shallow {doc}")
    print("PASS README depth")
def validate_ci_contract():
    for p in [".github/workflows/light.yml",".github/workflows/medium.yml",".github/workflows/validation.yml",".devcontainer/devcontainer.json","Dockerfile","docker-compose.yml"]:
        if not (ROOT/p).exists(): fail(f"missing CI/devops {p}")
    medium=(ROOT/".github/workflows/medium.yml").read_text(encoding="utf-8")
    if "scripts/generate_ci_run_manifest.py" not in medium or "scripts/finalize_v5_4_github_medium.py" not in medium or "scripts/verify_github_medium_artifact.py" not in medium or "actions/upload-artifact" not in medium:
        fail("medium workflow does not publish v5.4 CI evidence")
    if not (ROOT/"scripts"/"generate_ci_run_manifest.py").exists() or not (ROOT/"scripts"/"finalize_v5_4_github_medium.py").exists() or not (ROOT/"scripts"/"verify_github_medium_artifact.py").exists():
        fail("missing CI manifest script")
    print("PASS CI contract")
def validate_contract_lock():
    path=ROOT/"config"/"v5_4_contract_lock.json"
    lock=read(path if path.exists() else ROOT/"config"/"v5_3_contract_lock.json")
    if lock["schema_version"]!="hynix-v5.4-contract-lock-1": fail("bad lock")
    print("PASS contract lock")
def validate_state():
    s=state()
    if s.get("schema_version")=="hynix-v5.4-build-state-1":
        from validate_v5_4_state import validate as validate_v5_4_state
        validate_v5_4_state(s)
        if s["status"]=="READY_FOR_GITHUB_REVIEW":
            print("PASS v5.4 state")
        elif s["status"]=="AWAITING_GITHUB_MEDIUM":
            print("PASS v5.4 local state awaiting GitHub medium")
        else:
            fail("v5.4 local final state not reached")
        return
    if s["status"]!="READY_FOR_GITHUB_REVIEW": fail("bad state")
    print("PASS legacy state")
def validate_final_v5_acceptance():
    for fn in [validate_contract_lock,validate_real_run_counts,validate_no_all_mock_release,validate_engine_computed_evidence,validate_public_tool_receipts,validate_ai_judges_not_scripted,validate_judge_sensitivity,validate_red_team_partial_miss,validate_hidden_truth_isolation,validate_supervisor_non_overclaim,validate_scenario_question_coverage,validate_variant_suite,validate_dashboard_contract,validate_release_hygiene,validate_github_screenshots,validate_negative_fixtures,validate_audit_metrics,validate_ci_contract,validate_state]:
        fn()
    print("PASS final v5.4 local acceptance")
def validate_final_v5_2_acceptance():
    validate_final_v5_acceptance()
def validate_final_v5_3_acceptance():
    validate_final_v5_acceptance()
def make_manifest():
    entries={}
    exclude={"release_manifest.json","release/hynix-public-model-semiconductor-decision-twin-v5.zip","release/hynix-public-model-semiconductor-decision-twin-v5.manifest.json","release/hynix-autonomous-fab-hbm-digital-twin-console.zip","release/hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json"}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file():
            r=rel(p)
            if r in exclude or r.startswith("release/"): continue
            if "__pycache__" in r or r.endswith(".pyc"): fail(f"cache in manifest {r}")
            entries[r]=sha(p)
    current_state = state()
    dashboard = read(ROOT/"outputs"/"dashboard_data.json")
    manifest={
        "schema_version":"hynix-v5.4-release-manifest-1",
        "status": current_state.get("status", "AWAITING_GITHUB_MEDIUM"),
        "product_name":"Hynix Autonomous Fab x HBM Digital Twin Console",
        "public_model_only":True,
        "real_signoff_claim":False,
        "hbm_unit_normalized": True,
        "factory_route_map_ready": True,
        "screenshot_visual_contract_passed": True,
        "product_docs_contract_passed": True,
        "github_actions_medium_ready": current_state.get("status")=="READY_FOR_GITHUB_REVIEW",
        "ci_status": dashboard.get("public_tool_evidence", {}).get("ci", {}).get("status"),
        "sha256_entries":entries,
    }
    (ROOT/"release_manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return manifest
def package_release():
    validate_final_v5_acceptance()
    manifest=make_manifest()
    (ROOT/"release").mkdir(exist_ok=True)
    out=ROOT/"release"/"hynix-autonomous-fab-hbm-digital-twin-console.zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for r in sorted(manifest["sha256_entries"]): z.write(ROOT/r, r)
        z.write(ROOT/"release_manifest.json","release_manifest.json")
    side=dict(manifest); side["archive"]="release/hynix-autonomous-fab-hbm-digital-twin-console.zip"; side["archive_sha256"]=sha(out)
    (ROOT/"release"/"hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json").write_text(json.dumps(side,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("PASS package release")
def verify_release_payload():
    manifest=read(ROOT/"release_manifest.json")
    for r,h in manifest["sha256_entries"].items():
        if not (ROOT/r).exists() or sha(ROOT/r)!=h: fail(f"manifest mismatch {r}")
    print("PASS release payload")
def verify_clean_unzip():
    archive=ROOT/"release"/"hynix-autonomous-fab-hbm-digital-twin-console.zip"
    side=read(ROOT/"release"/"hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json")
    if sha(archive)!=side["archive_sha256"]: fail("archive sidecar mismatch")
    with tempfile.TemporaryDirectory(prefix="hynix_v5_") as tmp:
        with zipfile.ZipFile(archive) as z:
            for n in z.namelist():
                if "\\" in n or n.startswith("/") or ".." in Path(n).parts or "__pycache__" in n or n.endswith(".pyc"): fail(f"bad zip entry {n}")
            z.extractall(tmp)
        make=shutil.which("make") or ("C:/msys64/usr/bin/make.exe" if Path("C:/msys64/usr/bin/make.exe").exists() else None)
        if make:
            for target in ["test","validate","verify"]:
                rc=subprocess.run([make,"-C",tmp,f"PYTHON={sys.executable.replace(chr(92),'/')}",target],cwd=tmp).returncode
                if rc!=0: fail(f"clean unzip {target} rc={rc}")
        else:
            rc=subprocess.run([sys.executable,"-B",str(Path(tmp)/"validation"/"validate_final_v5_acceptance.py")],cwd=tmp).returncode
            if rc!=0: fail("clean unzip validate failed")
    print("PASS verify clean unzip")
