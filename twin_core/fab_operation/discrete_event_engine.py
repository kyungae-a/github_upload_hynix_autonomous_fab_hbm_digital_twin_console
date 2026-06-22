from __future__ import annotations
import heapq
from pathlib import Path
from statistics import mean
from twin_core.evidence.run_receipts import internal_receipt

def run_fab_operation(scenario: dict):
    x = scenario.get("inputs", {}); seed = int(scenario.get("seed", 0))
    tools = [(0.0, i) for i in range(2)]; heapq.heapify(tools)
    process = float(x.get("process_min", 50)); transport = float(x.get("transport_min", 14))
    events=[]; lots=[]
    for i in range(16):
        lot = "A" if i % 4 == 0 else "B"; arrival = i * 17.0
        avail, tool = heapq.heappop(tools); start = max(arrival, avail)
        if lot == "B": start = max(arrival, start - float(x.get("lot_b_priority", 0.5))*3)
        end = start + process + ((seed+i*5)%9)
        heapq.heappush(tools, (end, tool))
        q = float(x.get("lot_a_qtime_min", 90)) + start + transport if lot == "A" else start*0.35
        lots.append({"lot": lot, "arrival": round(arrival,3), "start": round(start,3), "end": round(end,3), "tool": tool, "qtime_downstream_min": round(q,3)})
        events += [{"time": round(arrival,3), "event": "ARRIVE", "lot": lot}, {"time": round(start,3), "event": "START", "lot": lot, "tool": tool}, {"time": round(end,3), "event": "END", "lot": lot, "tool": tool}]
    qmax = max(r["qtime_downstream_min"] for r in lots if r["lot"] == "A")
    qlimit = float(scenario.get("constraints", {}).get("qtime_limit_min", 240))
    met_delay = float(x.get("metrology_delay_min", 90))
    lot_qtime_trajectories = []
    for lot_name in ["A", "B"]:
        points = [
            {
                "lot_id": f"LOT_{lot_name}",
                "time_min": row["start"],
                "qtime_remaining_min": round(max(0.0, qlimit - row["qtime_downstream_min"]), 6),
                "qtime_used_min": row["qtime_downstream_min"],
                "tool_id": f"TOOL_{row['tool']}",
            }
            for row in lots if row["lot"] == lot_name
        ]
        lot_qtime_trajectories.append({"lot_id": f"LOT_{lot_name}", "points": points})
    dispatch_markers = [
        {"time_min": row["start"], "lot_id": f"LOT_{row['lot']}", "tool_id": f"TOOL_{row['tool']}", "event": "dispatch"}
        for row in lots[:8]
    ]
    metrology_delay_markers = [
        {"time_min": row["end"] + met_delay, "lot_id": f"LOT_{row['lot']}", "delay_min": round(met_delay, 6)}
        for row in lots if row["lot"] == "A"
    ]
    q_over_threshold = [
        {"lot_id": f"LOT_{row['lot']}", "time_min": row["start"], "qtime_min": row["qtime_downstream_min"], "limit_min": qlimit}
        for row in lots if row["qtime_downstream_min"] > qlimit
    ]
    tail = max(0, 0.72-float(x.get("p99_sample_power", 0.8)))*0.35 + max(0, float(x.get("p99_evidence_age_h", 8))-12)/96 + float(x.get("edge_cluster_signal", 0.02))*0.55
    obs = max(0, met_delay-90)/160 + max(0, float(x.get("sensor_drift_ppm", 0))-10)/80
    parsed = {
        "domain": "fab_operation", "lots_processed": len(lots), "tool_utilization": round(mean(r["end"]-r["start"] for r in lots)/max(1, max(r["end"] for r in lots)/2), 6),
        "lot_a_max_qtime_min": round(qmax, 6), "qtime_risk_index": round(max(0, qmax-qlimit+32)/100, 6),
        "local_dispatch_score": round(float(x.get("lot_b_priority", 0.5))*0.62 + max(0, 60-float(x.get("tool_window_min", 45)))/60*0.38, 6),
        "metrology_delay_min": round(met_delay, 6), "observability_risk_index": round(obs, 6),
        "tail_risk_index": round(tail, 6), "avg_defect_delta_pct": float(x.get("avg_defect_delta_pct", 0)),
        "throughput_delta_pct": float(x.get("throughput_delta_pct", 0)),
        "lot_qtime_trajectories": lot_qtime_trajectories,
        "q_over_threshold": q_over_threshold,
        "dispatch_markers": dispatch_markers,
        "metrology_delay_markers": metrology_delay_markers,
        "events": sorted(events, key=lambda e: (e["time"], e["event"])),
    }
    raw = {
        "event_timeline": sorted(events, key=lambda e: (e["time"], e["event"])),
        "lot_records": lots,
        "lot_qtime_trajectories": lot_qtime_trajectories,
        "q_over_threshold": q_over_threshold,
        "dispatch_markers": dispatch_markers,
        "metrology_delay_markers": metrology_delay_markers,
    }
    lineage = {k: "computed by deterministic fab event model" for k in parsed if k != "domain"}
    return internal_receipt("fab_operation_twin", scenario, Path(__file__), raw, parsed, lineage)
