from __future__ import annotations
from pathlib import Path
from statistics import mean
from twin_core.evidence.run_receipts import internal_receipt

def run_circuit_physical(scenario: dict):
    x = scenario.get("inputs", {})
    cell = float(x.get("cell_cap_ff", 30)); bit = float(x.get("bitline_cap_ff", 260))
    vdd = float(x.get("vdd", 1.0)); leakage = float(x.get("leakage_na", 0.5))
    req = float(x.get("timing_required_ns", 0.9)); arr = float(x.get("timing_arrival_ns", 0.86))
    seed = int(scenario.get("seed", 0))
    delta = vdd * cell / (cell + bit) * 1000
    sense_margin = delta - 55 - (seed % 5) * 1.3
    retention = max(1.0, 128 * (cell/30) / max(0.1, leakage))
    if scenario.get("domain") == "memory_ppa":
        retention *= 0.72; sense_margin -= 8.0
    samples = [sense_margin + (((i*31+seed)%21)-10)*0.42 for i in range(96)]
    wns = req - arr
    proxy_execution_pass = True
    proxy_design_pass = bool(wns >= 0 and sorted(samples)[4] >= 0 and retention >= 64)
    parsed = {
        "domain": "circuit_physical", "charge_share_delta_v_mv": round(delta, 6),
        "sense_margin_mv": round(sense_margin, 6), "sense_margin_p05_mv": round(sorted(samples)[4], 6),
        "retention_ms": round(retention, 6), "wns_ns": round(wns, 6), "tns_ns": round(min(0, wns)*12, 6),
        "proxy_execution_pass": proxy_execution_pass, "proxy_design_pass": proxy_design_pass,
        "real_signoff_claim_allowed": False, "external_report_word": x.get("external_report_word", "PUBLIC_PROXY_REPORT"),
    }
    raw = {"mc_samples_mv": [round(s, 6) for s in samples], "sample_mean_mv": round(mean(samples), 6), "netlist_hint": "1T1C public read-path proxy"}
    lineage = {k: "computed by charge-sharing/timing proxy public model" for k in parsed if k != "domain"}
    return internal_receipt("circuit_physical_proxy_twin", scenario, Path(__file__), raw, parsed, lineage)
