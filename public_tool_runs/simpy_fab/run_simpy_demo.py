from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from public_tool_runs.simpy.run_simpy_fab import run

if __name__ == "__main__":
    print(run()["status"])
