from __future__ import annotations
import heapq
from pathlib import Path
from twin_core.evidence.run_receipts import internal_receipt
from twin_core.io_utils import ROOT, write_json

def shortest_route(nodes: list[dict], edges: list[dict], source: str, target: str) -> tuple[list[str], float]:
    graph: dict[str, list[tuple[float, str]]] = {node["id"]: [] for node in nodes}
    for edge in edges:
        graph[edge["from"]].append((float(edge["cost"]), edge["to"]))
        graph[edge["to"]].append((float(edge["cost"]), edge["from"]))
    queue: list[tuple[float, str, list[str]]] = [(0.0, source, [source])]
    seen: set[str] = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue
        seen.add(node)
        if node == target:
            return path, cost
        for step_cost, nxt in graph.get(node, []):
            if nxt not in seen:
                heapq.heappush(queue, (cost + step_cost, nxt, path + [nxt]))
    raise ValueError(f"no route from {source} to {target}")

def run_factory_scene(scenario: dict):
    x = scenario.get("inputs", {}); seed = int(scenario.get("seed", 0))
    nodes = [
        {"id": "STOCKER_A", "kind": "stocker", "xy": [0, 0]},
        {"id": "ETCH_1", "kind": "tool", "xy": [2, 1]},
        {"id": "METRO_1", "kind": "metrology", "xy": [4, 1]},
        {"id": "CVD_1", "kind": "tool", "xy": [2, 4]},
        {"id": "STOCKER_B", "kind": "stocker", "xy": [5, 5]},
    ]
    congestion = float(x.get("route_congestion", 0.28)) + (seed % 5)*0.015
    edges = [
        {"from": "STOCKER_A", "to": "ETCH_1", "cost": round(3.0 + congestion, 6)},
        {"from": "ETCH_1", "to": "METRO_1", "cost": round(2.0 + congestion*2, 6)},
        {"from": "ETCH_1", "to": "CVD_1", "cost": round(3.5 + congestion*1.4, 6)},
        {"from": "CVD_1", "to": "STOCKER_B", "cost": round(2.8 + congestion, 6)},
        {"from": "METRO_1", "to": "STOCKER_B", "cost": round(2.2 + congestion*1.7, 6)},
    ]
    selected_route, route_cost = shortest_route(nodes, edges, "STOCKER_A", "STOCKER_B")
    node_xy = {node["id"]: node["xy"] for node in nodes}
    edge_by_pair = {(edge["from"], edge["to"]): edge for edge in edges} | {(edge["to"], edge["from"]): edge for edge in edges}
    route_segments = []
    for idx, (src, dst) in enumerate(zip(selected_route, selected_route[1:]), start=1):
        edge = edge_by_pair[(src, dst)]
        route_segments.append({
            "segment_id": f"R{idx:02d}",
            "from": src,
            "to": dst,
            "cost": edge["cost"],
            "delay_min": round(float(edge["cost"]) * (1.8 + congestion * 0.7), 6),
            "from_xy": node_xy[src],
            "to_xy": node_xy[dst],
        })
    congestion_zones = [
        {"zone_id": "Z_METRO", "center_xy": [4, 1], "radius": 0.85, "severity": round(congestion * 1.15, 6), "reason": "metrology queue pressure"},
        {"zone_id": "Z_ETCH_BUFFER", "center_xy": [2, 1], "radius": 0.75, "severity": round(congestion * 0.84, 6), "reason": "shared stocker to etch transport edge"},
    ]
    route_delay = sum(segment["delay_min"] for segment in route_segments)
    openusd_path = "outputs/factory_scene/openusd_like_scene.usda"
    parsed = {
        "domain": "factory_scene",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "route_congestion_index": round(congestion, 6),
        "best_route": selected_route,
        "selected_route": selected_route,
        "route_segments": route_segments,
        "congestion_zones": congestion_zones,
        "route_cost": round(route_cost, 6),
        "route_delay_min": round(route_delay, 6),
        "qtime_routing_multiplier": round(1 + congestion*0.35, 6),
        "nodes": nodes,
        "edges": edges,
        "openusd_like_export_path": openusd_path,
    }
    raw = {
        "nodes": nodes,
        "edges": edges,
        "selected_route": selected_route,
        "route_segments": route_segments,
        "congestion_zones": congestion_zones,
        "heatmap": [[round((r+c+1)*congestion, 4) for c in range(5)] for r in range(5)],
    }
    lineage = {k: "computed by factory scene graph routing model" for k in parsed if k != "domain"}
    write_json(ROOT / "outputs" / "factory_scene" / "fab_layout.json", {"nodes": nodes, "coordinate_system": "public_model_xy"})
    write_json(ROOT / "outputs" / "factory_scene" / "scene_graph.json", raw | {"route_cost": parsed["route_cost"], "route_delay_min": parsed["route_delay_min"]})
    (ROOT / openusd_path).write_text(
        "#usda 1.0\n"
        "# public-model factory scene\n"
        f"# selected_route = {' -> '.join(selected_route)}\n"
        f"# route_cost = {parsed['route_cost']} route_delay_min = {parsed['route_delay_min']}\n",
        encoding="utf-8",
    )
    return internal_receipt("factory_scene_routing_twin", scenario, Path(__file__), raw, parsed, lineage)
