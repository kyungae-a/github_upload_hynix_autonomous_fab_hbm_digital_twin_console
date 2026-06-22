from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from twin_core.io_utils import write_json
from public_tool_runs.tool_receipts import write_python_public_run, write_unavailable_public_package

def run():
    raw_rel = "outputs/public_tool_receipts/simpy_raw.json"
    parsed_rel = "outputs/public_tool_receipts/simpy_parsed.json"
    command = ["python", "-B", "public_tool_runs/simpy/run_simpy_fab.py"]
    try:
        import simpy  # type: ignore
    except Exception as exc:
        return write_unavailable_public_package(
            "simpy",
            command,
            raw_rel,
            parsed_rel,
            f"simpy import failed: {type(exc).__name__}: {exc}",
        )

    events: list[dict] = []
    env = simpy.Environment()
    etch = simpy.Resource(env, capacity=2)
    metro = simpy.Resource(env, capacity=1)

    def lot_process(lot_id: str, arrival: int, priority: float):
        yield env.timeout(arrival)
        events.append({"t": env.now, "event": "LOT_ARRIVAL", "lot_id": lot_id})
        with etch.request() as req:
            events.append({"t": env.now, "event": "QUEUE_ENTER", "lot_id": lot_id, "tool_id": "ETCH"})
            yield req
            events.append({"t": env.now, "event": "PROCESS_START", "lot_id": lot_id, "tool_id": "ETCH"})
            yield env.timeout(7 + int(priority * 3))
            events.append({"t": env.now, "event": "PROCESS_END", "lot_id": lot_id, "tool_id": "ETCH"})
        with metro.request() as req:
            events.append({"t": env.now, "event": "METROLOGY_SAMPLE", "lot_id": lot_id, "tool_id": "METRO"})
            yield req
            yield env.timeout(3 + (arrival % 5))
            events.append({"t": env.now, "event": "METROLOGY_DELAY", "lot_id": lot_id, "delay_min": 3 + (arrival % 5)})
        qtime_remaining = 80 - env.now + arrival * 0.25
        if qtime_remaining < 18:
            events.append({"t": env.now, "event": "QTIME_RISK_THRESHOLD_CROSSED", "lot_id": lot_id, "qtime_remaining_min": qtime_remaining})

    for i in range(24):
        env.process(lot_process(f"LOT_{i:02d}", i * 2, 0.2 + (i % 5) * 0.16))
    env.run(until=180)

    qtime_events = [e for e in events if e["event"] == "QTIME_RISK_THRESHOLD_CROSSED"]
    metrics = {
        "environment_created": True,
        "event_count": len(events),
        "qtime_threshold_crossings": len(qtime_events),
        "simpy_version": getattr(simpy, "__version__", "unknown"),
    }
    write_json(ROOT / raw_rel, {"tool": "simpy", "events": events})
    write_json(ROOT / parsed_rel, {"tool": "simpy", "status": "REAL_REPRODUCIBLE_PUBLIC_TOOL_RUN", **metrics})
    return write_python_public_run("simpy", command, raw_rel, parsed_rel, metrics)

if __name__ == "__main__":
    print(run()["status"])
