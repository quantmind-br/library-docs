---
title: Model capabilities maintenance
url: https://github.com/code-yeongyu/oh-my-openagent/blob/dev/docs/model-capabilities-maintenance.md
source: git
fetched_at: 2026-04-01T11:22:14.924303375-03:00
rendered_js: false
word_count: 222
summary: This document explains the layered system for model capability resolution and internal policies for maintaining model aliases and canonical IDs in the project.
tags:
    - model-capabilities
    - alias-management
    - canonical-ids
    - runtime-metadata
    - model-resolution
category: reference
---

# Model Capabilities Maintenance

This project treats model capability resolution as a layered system:

1. runtime metadata from connected providers
2. `models.dev` bundled/runtime snapshot data
3. explicit compatibility aliases
4. heuristic fallback as the last resort

## Internal policy

- Built-in OmO agent/category requirement models must use canonical model IDs.
- Aliases exist only to preserve compatibility with historical OmO names or provider-specific decorations.
- New decorated names like `-high`, `-low`, or `-thinking` should not be added to built-in requirements when a canonical model ID plus structured settings can express the same thing.
- If a provider or config input still uses an alias, normalize it at the edge and continue internally with the canonical ID.

## When adding an alias

- Add the alias rule to `src/shared/model-capability-aliases.ts`.
- Include a rationale for why the alias exists.
- Add or update tests so the alias is covered explicitly.
- Ensure the alias canonical target exists in the bundled `models.dev` snapshot.

## Guardrails

`bun run test:model-capabilities` enforces the following invariants:

- exact alias targets must exist in the bundled snapshot
- exact alias keys must not silently become canonical `models.dev` IDs
- pattern aliases must not rewrite canonical snapshot IDs
- built-in requirement models must stay canonical and snapshot-backed

The scheduled `refresh-model-capabilities` workflow runs these guardrails before opening an automated snapshot refresh PR.
