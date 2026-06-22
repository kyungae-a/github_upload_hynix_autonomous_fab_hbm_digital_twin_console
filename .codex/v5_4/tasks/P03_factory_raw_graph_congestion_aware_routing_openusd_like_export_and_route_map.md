# P03 — Factory Raw Graph, Congestion-Aware Routing, OpenUSD-Like Export, and Route Map

## Purpose
Replace summary/alias routing with a computed graph and a visibly inspectable 2D fab-floor route map.

## Preconditions
- All earlier phases are PASS in `docs/v5_4_build_state.json`.
- `python scripts/validate_v5_4_state.py` passes before edits.
- Read `AGENTS.md`, `CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md`, the source directive, contract lock, baseline audit, and this ticket completely.
- Modify the current product in place. Do not create a nested clone.

## Assigned agents
- Writer: `factory-route-product-engineer`
- Independent reviewer: `factory-route-reviewer`
- Writer cannot approve the phase or edit authoritative state to PASS. Parent closes P0/P1 findings and updates state.

## Files to create or modify
- `twin_core/factory_scene/layout.py`
- `twin_core/factory_scene/scene_graph.py`
- `twin_core/factory_scene/routing_graph.py`
- `twin_core/factory_scene/route_optimizer.py`
- `twin_core/factory_scene/openusd_like_export.py`
- `twin_core/factory_scene/run_factory_scene.py`
- `frontend/app.js`
- `frontend/styles.css`
- `tests/test_factory_scene_graph.py`
- `tests/test_factory_route_map_dashboard.py`
- `validation/validate_factory_scene_graph_contract.py`
- `docs/08_FACTORY_SCENE_ROUTING_TWIN.md`

## Classes and functions to implement
- `SceneNode`
- `TransportEdge`
- `CongestionZone`
- `RouteResult`
- `build_layout(config)`
- `build_graph(nodes, edges)`
- `edge_cost(edge, congestion_weight, qtime_pressure)`
- `dijkstra_route(graph, source, target, congestion_weight=1.0)`
- `astar_route(graph, source, target, heuristic, congestion_weight=1.0)`
- `build_route_segments(route)`
- `export_openusd_like_scene(scene, path)`
- `renderRouteMap(model)`

## Input data
- 2D node coordinates/types/labels
- transport edge distance/capacity/congestion
- source/target
- Q-time pressure
- maintenance constraints

## Output data and evidence
- nodes
- edges
- selected_route
- route_segments
- congestion_zones
- route_cost
- route_delay_min
- alternative routes
- meaningful `.usda`

## Dashboard change
Draw coordinate plane, node glyphs/labels, all edges, emphasized selected route, congestion circles/heat, and route cost/delay panel. Provide the USDA-like export link. Missing graph displays an ERROR panel; no sample fallback.

## Implementation tickets
1. Replace alias-only routing modules with actual implementations and unit-testable dataclasses/functions.
2. Replace congestion `if/else` route selection with Dijkstra and A* over the same adjacency model.
3. Use cost = distance + congestion penalty + Q-time pressure; preserve weights and per-edge cost lineage.
4. Promote the same raw graph object into parsed state, evidence packet, and dashboard bundle.
5. Write USDA-like `def Xform` primitives for FAB and each node plus route metadata—not only comments.
6. Feed route delay back to Fab S03 Q-time calculation through an explicit coupling record.

## Required tests
- At least five valid labeled nodes and five valid edges.
- Zero-congestion shortest path is selected.
- Congestion mutation causes a legal reroute.
- Every route segment references existing nodes/edges.
- USDA contains FAB and all node Xforms.
- Dashboard selected route equals engine route and no fallback branch exists.

## Validation commands
```bash
pytest -q tests/test_factory_scene_graph.py tests/test_factory_route_map_dashboard.py
python -m twin_core.factory_scene.run_factory_scene --seed 42 --export
python validation/validate_factory_scene_graph_contract.py --strict
make dashboard
```

## Acceptance / Done criteria
- Factory page visibly shows the computed route and congestion.
- Route algorithm is graph-based and perturbation-sensitive.
- Route delay has evidence lineage into Fab Q-time.

## Forbidden shortcuts
- Node-count-only dashboard
- Fixed route name lookup
- Frontend-defined graph
- Blank map
- Header-only USDA
- Fallback sample map

## Handoff evidence
Writer returns JSON conforming to `.codex/v5_4/schemas/phase_handoff.schema.json`: changed files, implemented symbols, exact commands and return codes, current-run artifact paths/hashes/run IDs, dashboard impact, open risks, and reviewer request. Reviewer returns severity-ranked findings and explicit PASS/FAIL. Parent fixes every P0/P1, reruns the commands and reviewer, then updates authoritative state.
