from __future__ import annotations
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

SCREENSHOTS = [
    ("01_architecture.png", "overview", "Architecture / overview console"),
    ("02_fab_qtime_timeline.png", "fab", "Fab Q-time timeline"),
    ("03_hbm_workload_policy_compare.png", "hbm", "HBM workload policy compare"),
    ("04_factory_scene_routing.png", "factory", "Factory scene routing"),
    ("05_public_tool_evidence.png", "public-tools", "Public tool evidence"),
    ("06_ai_judgment_audit_flow.png", "audit", "AI judgment audit flow"),
    ("07_hynix_alignment.png", "hynix-alignment", "Hynix alignment"),
]

COMPAT_ROUTES = [
    ("architecture.png", "overview", "Architecture compatibility"),
    ("fab_timeline.png", "fab", "Fab timeline compatibility"),
    ("hbm_workload.png", "hbm", "HBM workload compatibility"),
    ("factory_scene.png", "factory", "Factory scene compatibility"),
    ("public_tool_evidence.png", "public-tools", "Public tools compatibility"),
    ("ai_audit_flow.png", "audit", "AI audit compatibility"),
    ("hidden_truth_reveal.png", "audit", "Hidden truth compatibility"),
    ("hynix_alignment.png", "hynix-alignment", "Hynix alignment compatibility"),
]

def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def find_browser() -> str:
    candidates = [
        shutil.which("msedge"),
        shutil.which("chrome"),
        shutil.which("chromium"),
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    raise SystemExit("No Chrome/Edge/Chromium browser found for v5.4 browser screenshot capture")

def ensure_dashboard_copy() -> tuple[Path, str]:
    source = ROOT / "outputs" / "dashboard_data.json"
    if not source.exists():
        source = ROOT / "outputs" / "dashboard" / "dashboard_data.json"
    if not source.exists():
        source = ROOT / "frontend" / "dashboard_data.json"
    target = ROOT / "frontend" / "dashboard_data.json"
    if source.resolve() != target.resolve():
        target.write_bytes(source.read_bytes())
    return target, sha_file(target)

def browser_version(browser: str) -> str:
    try:
        profile = Path(tempfile.mkdtemp(prefix="hynix_v54_browser_version_"))
        result = subprocess.run([browser, "--version", f"--user-data-dir={profile}"], text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=20)
        return (result.stdout or result.stderr or "unknown").strip()
    except Exception as exc:
        return f"unknown: {exc}"

def capture(browser: str, route: str, out: Path) -> dict:
    html = (ROOT / "frontend" / "index.html").resolve().as_uri()
    url = f"{html}#{quote(route)}"
    node = shutil.which("node")
    helper = ROOT / "scripts" / "browser_capture.mjs"
    if node and helper.exists():
        cmd = [node, str(helper), browser, url, str(out), str(ROOT)]
        result = subprocess.run(cmd, cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=120)
        if result.returncode == 0 and out.exists() and out.stat().st_size >= 20000:
            return {
                "route": route,
                "url": url,
                "command": cmd,
                "returncode": result.returncode,
                "stdout_preview": result.stdout[:500],
                "stderr_preview": result.stderr[:500],
                "capture_backend": "playwright_core",
            }
    profile = Path(tempfile.mkdtemp(prefix="hynix_v54_browser_"))
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--disable-gpu-compositing",
        "--disable-gpu-rasterization",
        "--disable-gpu-sandbox",
        "--disable-software-rasterizer",
        "--disable-features=VizDisplayCompositor,DawnGraphite,UseSkiaRenderer",
        "--disable-accelerated-2d-canvas",
        "--run-all-compositor-stages-before-draw",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-dev-shm-usage",
        "--allow-file-access-from-files",
        "--hide-scrollbars",
        f"--user-data-dir={profile}",
        "--window-size=1440,1000",
        f"--screenshot={out}",
        url,
    ]
    result = subprocess.run(cmd, cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=90)
    if result.returncode != 0 or not out.exists() or out.stat().st_size < 20000:
        raise SystemExit(f"browser screenshot failed for {route}: rc={result.returncode}\n{result.stdout}\n{result.stderr}")
    return {
        "route": route,
        "url": url,
        "command": cmd,
        "returncode": result.returncode,
        "stdout_preview": result.stdout[:500],
        "stderr_preview": result.stderr[:500],
    }

def write_sidecar(path: Path, info: dict) -> None:
    sidecar = path.with_name(f"{path.name}.json")
    sidecar.write_text(json.dumps(info, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    out_dir = ROOT / "screenshots"
    out_dir.mkdir(exist_ok=True)
    browser = find_browser()
    version = browser_version(browser)
    data_path, data_hash = ensure_dashboard_copy()
    entries = []
    for name, route, label in SCREENSHOTS + COMPAT_ROUTES:
        out = out_dir / name
        result = capture(browser, route, out)
        entry = {
            "screenshot": f"screenshots/{name}",
            "route": route,
            "label": label,
            "viewport": "1440x1000",
            "browser": browser,
            "browser_version": version,
            "capture_kind": "headless_browser_file_route",
            "dashboard_data_path": data_path.relative_to(ROOT).as_posix(),
            "dashboard_sha256": data_hash,
            "png_sha256": sha_file(out),
            "visible_labels": ["MetricCard", "StatusBadge", "LineChart", "BarChart", "Timeline", "RouteMap", "EvidenceTable", "DecisionFlow", "ReceiptPanel", "VariantMatrix"],
            **result,
        }
        write_sidecar(out, entry)
        entries.append(entry)
    manifest = {
        "schema_version": "hynix-v5.4-browser-screenshot-manifest-1",
        "source": data_path.relative_to(ROOT).as_posix(),
        "source_sha256": data_hash,
        "browser": browser,
        "browser_version": version,
        "screenshots": entries,
    }
    (out_dir / "screenshot_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS browser screenshots")

if __name__ == "__main__":
    main()
