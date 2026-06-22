from __future__ import annotations
from pathlib import Path
from statistics import mean
from twin_core.evidence.run_receipts import internal_receipt

def gbps_to_GBps(value: float) -> float:
    return round(value / 8.0, 6)

def run_memory_system(scenario: dict):
    x = scenario.get("inputs", {})
    peak = float(x.get("peak_gbps", 24000))
    locality = float(x.get("row_locality", 0.5))
    traffic = float(x.get("traffic_gib", 4))
    thermal = float(x.get("thermal_headroom_c", 6))
    power = float(x.get("power_margin_w", 0.8))
    seed = int(scenario.get("seed", 0))
    conflicts = max(0.02, min(0.62, (1-locality)*0.54 + (seed % 7)*0.01))
    refresh_loss = 0.018 + traffic / 2048.0
    turnaround_loss = 0.024 + conflicts * 0.08
    fcfs = peak * (0.70 + locality*0.12) * (1 - conflicts*0.26 - refresh_loss - turnaround_loss)
    frfcfs = fcfs * (1.04 + conflicts*0.16)
    thermal_pressure = max(0, frfcfs/peak - 0.62) * max(0, 8-thermal)/8 + max(0, 0.75-power)*0.17
    sustained = frfcfs * (1 - min(0.23, thermal_pressure))
    lat = [44 + conflicts*37 + ((i*13+seed)%17) + refresh_loss*70 for i in range(80)]
    fcfs_score = fcfs * (1 - conflicts * 0.08)
    frfcfs_score = sustained * (1 - thermal_pressure * 0.12)
    thermal_aware = sustained * (1 - max(0, thermal_pressure - 0.08) * 0.22)
    raw_metrics = {
        "theoretical_bandwidth_gbps": round(peak, 6),
        "fcfs_bandwidth_gbps": round(fcfs, 6),
        "frfcfs_bandwidth_gbps": round(frfcfs, 6),
        "sustained_bandwidth_gbps": round(sustained, 6),
    }
    display_metrics = {
        "theoretical_bandwidth_GBps": gbps_to_GBps(peak),
        "fcfs_bandwidth_GBps": gbps_to_GBps(fcfs),
        "frfcfs_bandwidth_GBps": gbps_to_GBps(frfcfs),
        "sustained_bandwidth_GBps": gbps_to_GBps(sustained),
    }
    policy_comparison = [
        {
            "policy_id": "FCFS",
            "raw_bandwidth_gbps": raw_metrics["fcfs_bandwidth_gbps"],
            "display_bandwidth_GBps": display_metrics["fcfs_bandwidth_GBps"],
            "p99_latency_ns": round(sorted(lat)[-1] + conflicts * 8, 6),
            "thermal_pressure": round(max(0.0, thermal_pressure * 0.72), 6),
            "refresh_overhead_pct": round(refresh_loss * 100, 6),
            "bank_conflict_rate": round(conflicts, 6),
            "bank_group_conflict_rate": round(conflicts * 0.42, 6),
            "hard_constraint_result": "PASS",
            "score": round(fcfs_score, 6),
            "recommendation_reason": "baseline fairness, lower scheduler complexity",
        },
        {
            "policy_id": "FR-FCFS",
            "raw_bandwidth_gbps": raw_metrics["frfcfs_bandwidth_gbps"],
            "display_bandwidth_GBps": display_metrics["frfcfs_bandwidth_GBps"],
            "p99_latency_ns": round(sorted(lat)[-1] + conflicts * 13, 6),
            "thermal_pressure": round(thermal_pressure, 6),
            "refresh_overhead_pct": round(refresh_loss * 100, 6),
            "bank_conflict_rate": round(conflicts * 0.86, 6),
            "bank_group_conflict_rate": round(conflicts * 0.36, 6),
            "hard_constraint_result": "PASS" if thermal_pressure < 0.22 else "REVIEW",
            "score": round(frfcfs_score, 6),
            "recommendation_reason": "higher effective bandwidth with bounded thermal pressure",
        },
        {
            "policy_id": "THERMAL_AWARE_FRFCFS",
            "raw_bandwidth_gbps": round(thermal_aware, 6),
            "display_bandwidth_GBps": gbps_to_GBps(thermal_aware),
            "p99_latency_ns": round(sorted(lat)[-1] + conflicts * 10, 6),
            "thermal_pressure": round(max(0.0, thermal_pressure - 0.04), 6),
            "refresh_overhead_pct": round((refresh_loss + 0.004) * 100, 6),
            "bank_conflict_rate": round(conflicts * 0.9, 6),
            "bank_group_conflict_rate": round(conflicts * 0.34, 6),
            "hard_constraint_result": "PASS",
            "score": round(thermal_aware * (1 - max(0.0, thermal_pressure - 0.04)), 6),
            "recommendation_reason": "recommended when reviewer prioritizes sustained bandwidth and margin",
        },
    ]
    parsed = {
        "domain": "memory_system", **raw_metrics,
        "row_hit_rate": round(locality, 6),
        "bank_conflict_rate": round(conflicts, 6), "refresh_loss_pct": round(refresh_loss*100, 6),
        "turnaround_loss_pct": round(turnaround_loss*100, 6), "latency_mean_ns": round(mean(lat), 6),
        "latency_p95_ns": round(sorted(lat)[75], 6), "thermal_pressure_index": round(thermal_pressure, 6),
        "ppa_candidate_a_score": round(frfcfs*1.08, 6), "ppa_candidate_b_score": round(frfcfs*0.98, 6),
        "raw_metrics": raw_metrics,
        "display_metrics": {
            key: {"value": value, "source_metric_path": f"raw_metrics.{key.replace('_GBps', '_gbps')}", "derivation": "GB/s = Gbps / 8"}
            for key, value in display_metrics.items()
        },
        "unit_notes": {"conversion": "GB/s = Gbps / 8", "raw_suffix": "_gbps", "display_suffix": "_GBps"},
        "policy_comparison": policy_comparison,
        "recommended_policy": max(policy_comparison, key=lambda item: item["score"])["policy_id"],
    }
    raw = {"trace": [{"cycle": i, "op": "READ" if i % 10 < 7 else "WRITE", "bank": (i*7+seed)%128} for i in range(96)]}
    lineage = {k: "computed by HBM workload public model" for k in parsed if k != "domain"}
    return internal_receipt("hbm_memory_system_twin", scenario, Path(__file__), raw, parsed, lineage)
