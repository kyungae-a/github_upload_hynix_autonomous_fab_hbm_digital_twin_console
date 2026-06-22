
# v5.3 Frontend Console Contract

## Reviewer journey

1. README screenshot grid and five-module map.
2. Nine-route console.
3. S03 end-to-end drill-down: timeline → Q-time → route → evidence → judgment → red-team → supervisor → reveal.
4. Current public-tool receipts with commands/logs/hashes.
5. Real browser screenshots.

## Routes

`overview`, `hbm`, `circuit`, `fab`, `factory`, `audit`, `public-tools`, `variants`, `hynix-alignment`.

## Required components

`MetricCard`, `StatusBadge`, `LineChart`, `BarChart`, `Timeline`, `RouteMap`, `EvidenceTable`, `DecisionFlow`, `ReceiptPanel`, `ScenarioSelector`, `VariantMatrix`.

## Evidence rule

The browser never owns domain calculations. Every technical value carries a run ID, unit, source artifact path/hash, and validation status. Missing or stale evidence is rendered as an error, never as zero or a plausible placeholder.

## Screenshot rule

Final images are Playwright/equivalent browser captures of the actual routes. The capture manifest records route/query, viewport, browser version, current run ID, dashboard hash, visible labels/values, and PNG hash. Synthetic text-card generation is forbidden for final files.
