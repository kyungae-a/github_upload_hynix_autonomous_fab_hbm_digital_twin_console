from __future__ import annotations
import shutil, subprocess
from pathlib import Path
from twin_core.io_utils import ROOT, sha_file, sha_obj, write_json

REAL_STATUSES = {"REAL_EXTERNAL_RUN", "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN"}

def _write_text(rel: str, text: str) -> str:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return rel

def write_external_attempt(
    tool: str,
    executable: str,
    args: list[str],
    raw_rel: str,
    parsed_rel: str,
    input_paths: list[Path] | None = None,
) -> dict:
    outputs = ROOT / "outputs" / "public_tool_receipts"
    outputs.mkdir(parents=True, exist_ok=True)
    exe_path = shutil.which(executable)
    command = [executable, *args]
    stdout_rel = f"outputs/public_tool_receipts/{tool}_stdout.txt"
    stderr_rel = f"outputs/public_tool_receipts/{tool}_stderr.txt"
    log_rel = f"outputs/public_tool_receipts/{tool}_attempt.log"

    if exe_path:
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        stdout = completed.stdout
        stderr = completed.stderr
        returncode = completed.returncode
        status = "REAL_EXTERNAL_RUN" if returncode == 0 else "FAILED_WITH_EXPLANATION"
        reason = "subprocess completed" if returncode == 0 else "subprocess returned non-zero"
    else:
        stdout = ""
        stderr = f"{executable} was not found on PATH; no proxy output was promoted to REAL_EXTERNAL_RUN.\n"
        returncode = None
        status = "EXPLAINED_UNAVAILABLE"
        reason = f"{executable} executable unavailable"

    _write_text(stdout_rel, stdout)
    _write_text(stderr_rel, stderr)
    _write_text(log_rel, f"tool={tool}\ncommand={' '.join(command)}\nstatus={status}\nreason={reason}\n")
    parsed = {
        "tool": tool,
        "status": status,
        "returncode": returncode,
        "reason": reason,
        "parser_status": "PASS" if status == "REAL_EXTERNAL_RUN" else "EXPLAINED",
        "stdout_preview": stdout[:400],
        "stderr_preview": stderr[:400],
    }
    raw = {
        "tool": tool,
        "attempted": True,
        "command": command,
        "executable_path": exe_path,
        "returncode": returncode,
        "status": status,
        "reason": reason,
        "stdout_path": stdout_rel,
        "stderr_path": stderr_rel,
        "log_path": log_rel,
        "claim_boundary": {"public_tool_proxy_only": True, "real_signoff_allowed": False},
    }
    write_json(ROOT / raw_rel, raw)
    write_json(ROOT / parsed_rel, parsed)
    input_hash = sha_obj({
        "tool": tool,
        "command": command,
        "inputs": [p.relative_to(ROOT).as_posix() for p in input_paths or []],
    })
    receipt = {
        "tool": tool,
        "status": status,
        "command": command,
        "relative_cwd": ".",
        "environment": "current-subprocess-attempt",
        "executable": executable,
        "executable_path": exe_path,
        "returncode": returncode,
        "exit_status": 0 if returncode is None else returncode,
        "reason": reason,
        "stdout_path": stdout_rel,
        "stdout_sha256": sha_file(ROOT / stdout_rel),
        "stderr_path": stderr_rel,
        "stderr_sha256": sha_file(ROOT / stderr_rel),
        "log_path": log_rel,
        "log_sha256": sha_file(ROOT / log_rel),
        "raw_output_path": raw_rel,
        "raw_output_sha256": sha_file(ROOT / raw_rel),
        "parsed_output_path": parsed_rel,
        "parsed_output_sha256": sha_file(ROOT / parsed_rel),
        "parsed_metrics_path": parsed_rel,
        "input_sha256": input_hash,
        "parser_status": parsed["parser_status"],
        "claim_boundary": {"public_tool_proxy_only": True, "real_signoff_allowed": False},
    }
    out = outputs / f"{tool}.json"
    write_json(out, receipt)
    return receipt

def write_python_public_run(tool: str, command: list[str], raw_rel: str, parsed_rel: str, metrics: dict) -> dict:
    receipt = {
        "tool": tool,
        "status": "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN",
        "command": command,
        "relative_cwd": ".",
        "environment": "python-public-package-current-run",
        "returncode": 0,
        "exit_status": 0,
        "raw_output_path": raw_rel,
        "raw_output_sha256": sha_file(ROOT / raw_rel),
        "parsed_output_path": parsed_rel,
        "parsed_output_sha256": sha_file(ROOT / parsed_rel),
        "parsed_metrics_path": parsed_rel,
        "input_sha256": sha_obj({"tool": tool, "command": command}),
        "parser_status": "PASS",
        "parsed_metrics": metrics,
        "claim_boundary": {"public_tool_proxy_only": True, "real_signoff_allowed": False},
    }
    write_json(ROOT / "outputs" / "public_tool_receipts" / f"{tool}.json", receipt)
    return receipt

def write_unavailable_public_package(tool: str, command: list[str], raw_rel: str, parsed_rel: str, reason: str) -> dict:
    write_json(ROOT / raw_rel, {"tool": tool, "attempted": True, "status": "EXPLAINED_UNAVAILABLE", "reason": reason})
    write_json(ROOT / parsed_rel, {"tool": tool, "status": "EXPLAINED_UNAVAILABLE", "reason": reason, "parser_status": "EXPLAINED"})
    receipt = {
        "tool": tool,
        "status": "EXPLAINED_UNAVAILABLE",
        "command": command,
        "relative_cwd": ".",
        "environment": "python-public-package-current-run",
        "returncode": None,
        "exit_status": 0,
        "reason": reason,
        "raw_output_path": raw_rel,
        "raw_output_sha256": sha_file(ROOT / raw_rel),
        "parsed_output_path": parsed_rel,
        "parsed_output_sha256": sha_file(ROOT / parsed_rel),
        "parsed_metrics_path": parsed_rel,
        "input_sha256": sha_obj({"tool": tool, "command": command}),
        "parser_status": "EXPLAINED",
        "claim_boundary": {"public_tool_proxy_only": True, "real_signoff_allowed": False},
    }
    write_json(ROOT / "outputs" / "public_tool_receipts" / f"{tool}.json", receipt)
    return receipt
