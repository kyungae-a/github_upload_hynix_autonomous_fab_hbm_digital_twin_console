# v5.4 Batching and Dependency Graph

```text
P00 → P01
        ├─ P02 HBM units/page ─┐
        ├─ P03 Factory graph ──┤
        ├─ P04 Fab timeline ───┤→ P06 Console integration → P07 Screenshots
        └─ P05 CI evidence ────┘                      └────→ P08 Docs
                                                        P09 Validation
                                                        P10 Local release
                                                        P11 GitHub medium finalization
```

P02–P05 may use isolated worktrees after P01 freezes schemas. Only the parent orchestrator edits shared dashboard schema, `Makefile`, authoritative state, final manifest, or global frontend router. P06 integrates all branch outputs. P07 captures only after data/UI freeze. P10 may end at `AWAITING_GITHUB_MEDIUM`; P11 must execute in genuine GitHub Actions context before final READY.
