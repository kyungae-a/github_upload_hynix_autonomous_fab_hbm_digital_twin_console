# 14 Screenshot Guide

## Purpose

The screenshot folder is generated from `frontend/dashboard_data.json`. Each PNG has a JSON sidecar that records the dashboard data hash used to render it. This is meant to prevent placeholder or manually edited screenshots from being treated as evidence.

## Required v5.2 Screenshots

- `screenshots/01_architecture.png`
- `screenshots/02_fab_qtime_timeline.png`
- `screenshots/03_hbm_workload_policy_compare.png`
- `screenshots/04_factory_scene_routing.png`
- `screenshots/05_public_tool_evidence.png`
- `screenshots/06_ai_judgment_audit_flow.png`

## Compatibility Screenshots

The generator also emits legacy v5 names for older review prompts:

- `screenshots/architecture.png`
- `screenshots/fab_timeline.png`
- `screenshots/hbm_workload.png`
- `screenshots/factory_scene.png`
- `screenshots/public_tool_evidence.png`
- `screenshots/ai_audit_flow.png`
- `screenshots/hidden_truth_reveal.png`
- `screenshots/hynix_alignment.png`

## How To Regenerate

Run:

```bash
make dashboard
make screenshots
```

Then inspect `screenshots/screenshot_manifest.json`. The manifest lists the data source, source SHA-256, and screenshot entries.

## Claim Boundary

These screenshots are dashboard evidence views, not product signoff evidence. They show public-model computation, public-tool attempt status, AI audit flow, and portfolio traceability.
