from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from public_tool_runs.tool_receipts import write_external_attempt

def run():
    net = ROOT / "public_tool_runs" / "ngspice" / "netlists" / "read_path_charge_sharing.sp"
    net.parent.mkdir(parents=True, exist_ok=True)
    net.write_text(
        "* public-model DRAM read path charge-sharing proxy\n"
        "Vpre bl 0 0.5\n"
        "Ccell cell 0 30f\n"
        "Cbl bl 0 260f\n"
        "Raccess cell bl 2k\n"
        ".tran 1p 2n\n"
        ".print tran v(bl) v(cell)\n"
        ".end\n",
        encoding="utf-8",
    )
    log = ROOT / "outputs" / "public_tool_receipts" / "ngspice_native.log"
    return write_external_attempt(
        "ngspice",
        "ngspice",
        ["-b", net.relative_to(ROOT).as_posix(), "-o", log.relative_to(ROOT).as_posix()],
        "outputs/public_tool_receipts/ngspice_raw.json",
        "outputs/public_tool_receipts/ngspice_parsed.json",
        [net],
    )

if __name__ == "__main__":
    print(run()["status"])
