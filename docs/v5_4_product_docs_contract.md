# v5.4 Product Documentation Contract

The required documents are product manuals, not presence markers. Each must contain the directive's numbered sections, at least one implementation diagram or execution chain, actual code paths, input schema, computed metrics, dashboard mapping, current-run evidence paths, representative scenario, validation command, and public-model/signoff boundary.

- `docs/05_HBM_WORKLOAD_TWIN.md`: workload generators, policies, refresh/turnaround/thermal model, raw/display unit semantics, S01, dashboard and evidence.
- `docs/07_FAB_OPERATION_TWIN.md`: SimPy/event architecture, Lot/Tool/Chamber/QTime, dispatch, drift, metrology, trajectories, S03, dashboard and boundary.
- `docs/08_FACTORY_SCENE_ROUTING_TWIN.md`: scene graph, graph data, congestion, Dijkstra/A*, USDA-like export, dashboard map, scenario, evidence and boundary.
- `docs/09_AI_JUDGMENT_AUDIT_LAYER.md`: evidence packet, rule-based Judge, Red-team, Meta, Supervisor, Oracle, caught/escaped, boundary.
- `docs/11_IMPLEMENTATION_EVIDENCE.md`: engine, public-tool, HBM, circuit, Fab, routing, audit, screenshot evidence, known limits.

The validator must resolve every referenced repo path and reject one-line repetitions, missing claim boundaries, or headings with no substantive body.
