from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from public_tool_runs.tool_receipts import write_external_attempt
from public_tool_runs.yosys_verilator.run_yosys import write_rtl

def run():
    rtl = write_rtl()
    return write_external_attempt(
        "verilator",
        "verilator",
        ["--lint-only", rtl.relative_to(ROOT).as_posix()],
        "outputs/public_tool_receipts/verilator_raw.json",
        "outputs/public_tool_receipts/verilator_parsed.json",
        [rtl],
    )

if __name__ == "__main__":
    print(run()["status"])
