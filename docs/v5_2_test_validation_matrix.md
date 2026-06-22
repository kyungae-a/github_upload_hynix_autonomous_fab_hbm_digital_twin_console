# v5.2 Test and Validation Matrix

| Risk | Positive proof | Negative fixture / validator |
|---|---|---|
| Label-only twin | Engine trace, sensitivity tests | pass-only/stub module → `validate_product_modules.py` |
| Static HBM metrics | Workload/policy mutations change outputs | scenario-copied metrics → `validate_hbm_engine_behavior.py` |
| Shallow circuit proxy | Equation/PVT/MC tests | nominal-only/fake signoff → `validate_circuit_proxy_behavior.py` |
| Fake SimPy | causal 50+ event log | static event list → `validate_fab_simpy_behavior.py` |
| Static scene | Dijkstra/A* route changes | hard-coded route → `validate_factory_scene_routing.py` |
| Fake public tool | current subprocess receipt | hand-written REAL → `validate_public_tool_real_runs.py` |
| Variant routing bug | non-prefix IDs route by family | prefix router → `validate_variant_family_routing.py` |
| Scripted Judge | threshold perturbation changes decision | scenario lookup → `validate_judge_metric_sensitivity.py` |
| Omniscient red-team | 4–5 caught, >=1 escape | 6/6 catch → governance validator |
| Hidden leak | separate staging/freeze | canary leak/post-freeze mutation |
| Supervisor overclaim | requires real signoff | product approval fixture |
| Hard-coded dashboard | artifact lineage per value | stale/missing source |
| Placeholder screenshot | source-hash sidecar and data labels | gradient/blank fixture |
| Dirty release | path/cache scan | `__pycache__`, `.pyc`, absolute paths |
