---
title: Memory - OpenClaw
url: https://docs.openclaw.ai/cli/memory
source: sitemap
fetched_at: 2026-01-30T20:34:48.68549388-03:00
rendered_js: false
word_count: 89
summary: Provides instructions for managing semantic memory indexing and search operations through command-line interface commands.
tags:
    - semantic-memory
    - indexing
    - search
    - command-line
    - memory-management
category: reference
---

Manage semantic memory indexing and search. Provided by the active memory plugin (default: `memory-core`; set `plugins.slots.memory = "none"` to disable). Related:

- Memory concept: [Memory](https://docs.openclaw.ai/concepts/memory)
- Plugins: [Plugins](https://docs.openclaw.ai/plugins)

## Examples

```
openclaw memory status
openclaw memory status --deep
openclaw memory status --deep --index
openclaw memory status --deep --index --verbose
openclaw memory index
openclaw memory index --verbose
openclaw memory search "release checklist"
openclaw memory status --agent main
openclaw memory index --agent main --verbose
```

## Options

Common:

- `--agent <id>`: scope to a single agent (default: all configured agents).
- `--verbose`: emit detailed logs during probes and indexing.

Notes:

- `memory status --deep` probes vector + embedding availability.
- `memory status --deep --index` runs a reindex if the store is dirty.
- `memory index --verbose` prints per-phase details (provider, model, sources, batch activity).
- `memory status` includes any extra paths configured via `memorySearch.extraPaths`.