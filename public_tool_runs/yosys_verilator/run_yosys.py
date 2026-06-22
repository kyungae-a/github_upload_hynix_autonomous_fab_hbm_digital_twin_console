from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from public_tool_runs.tool_receipts import write_external_attempt

def write_rtl() -> Path:
    rtl = ROOT / "public_tool_runs" / "rtl" / "rtl" / "hbm_policy_controller.v"
    rtl.parent.mkdir(parents=True, exist_ok=True)
    rtl.write_text(
        "module hbm_policy_controller(\n"
        "  input [7:0] bandwidth_pressure,\n"
        "  input [7:0] thermal_pressure,\n"
        "  input [7:0] qtime_risk,\n"
        "  input [7:0] margin_risk,\n"
        "  output reg [2:0] selected_policy,\n"
        "  output reg requires_supervisor_gate\n"
        ");\n"
        "always @* begin\n"
        "  requires_supervisor_gate = (margin_risk > 8'd160) || (qtime_risk > 8'd180);\n"
        "  if (thermal_pressure > 8'd170) selected_policy = 3'd3;\n"
        "  else if (margin_risk > 8'd140) selected_policy = 3'd5;\n"
        "  else if (bandwidth_pressure > 8'd150) selected_policy = 3'd1;\n"
        "  else selected_policy = 3'd0;\n"
        "end\n"
        "endmodule\n",
        encoding="utf-8",
    )
    return rtl

def run():
    rtl = write_rtl()
    return write_external_attempt(
        "yosys",
        "yosys",
        ["-p", f"read_verilog {rtl.relative_to(ROOT).as_posix()}; synth; stat"],
        "outputs/public_tool_receipts/yosys_raw.json",
        "outputs/public_tool_receipts/yosys_parsed.json",
        [rtl],
    )

if __name__ == "__main__":
    print(run()["status"])
