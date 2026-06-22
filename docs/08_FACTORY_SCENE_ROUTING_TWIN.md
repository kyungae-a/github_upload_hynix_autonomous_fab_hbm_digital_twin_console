# 08 Factory Scene Routing Twin

## Purpose

The Factory Scene Routing Twin converts a small fab floor graph into a visible route map with congestion zones, selected path, route cost, delay, and OpenUSD-like public-model export. Its goal is to make factory-scene evidence inspectable from a reviewer screenshot, not merely to report node and edge counts.

## Inputs

Scenarios provide route congestion and deterministic seeds. The engine owns the graph: stockers, tools, metrology nodes, transport edges, congestion severity, and output paths.

## Engine Structure

`twin_core/factory_scene/scene_graph.py` creates a five-node coordinate plane and at least five transport edges. It computes the selected route with a Dijkstra-style shortest path over congestion-weighted edge costs. The selected route is then expanded into `route_segments` with source/destination coordinates and delay estimates.

The parsed factory object includes:

- `nodes`
- `edges`
- `selected_route`
- `route_segments`
- `congestion_zones`
- `route_cost`
- `route_delay_min`
- `openusd_like_export_path`

These fields are also written to `outputs/factory_scene/scene_graph.json` and summarized in `openusd_like_scene.usda`.

## Dashboard Mapping

The Factory page sends the exact dashboard factory object into `RouteMap`. If the graph is missing, the UI renders an error instead of a fallback sample map. The selected route is highlighted, congestion zones are drawn over the coordinate plane, and the route cost/delay panel is shown next to the map.

## Evidence Paths

- Layout: `outputs/factory_scene/fab_layout.json`
- Scene graph: `outputs/factory_scene/scene_graph.json`
- OpenUSD-like export: `outputs/factory_scene/openusd_like_scene.usda`
- Dashboard contract: `outputs/dashboard_data.json`
- Screenshot: `screenshots/04_factory_scene_routing.png`

## Claim Boundary

This twin demonstrates public-model spatial reasoning and evidence traceability. It is not an SK hynix factory digital twin, production route optimizer, or validated AMHS model.
