---
title: Nodes - OpenClaw
url: https://docs.openclaw.ai/cli/nodes
source: sitemap
fetched_at: 2026-01-30T20:34:40.133166948-03:00
rendered_js: false
word_count: 182
summary: This document explains how to manage paired devices using the OpenClaw CLI, including listing nodes, checking their status, and invoking commands on them.
tags:
    - node-management
    - device-control
    - cli-tool
    - command-invoke
    - node-status
    - openclaw-cli
category: reference
---

Manage paired nodes (devices) and invoke node capabilities. Related:

- Nodes overview: [Nodes](https://docs.openclaw.ai/nodes)
- Camera: [Camera nodes](https://docs.openclaw.ai/nodes/camera)
- Images: [Image nodes](https://docs.openclaw.ai/nodes/images)

Common options:

- `--url`, `--token`, `--timeout`, `--json`

## Common commands

```
openclaw nodes list
openclaw nodes list --connected
openclaw nodes list --last-connected 24h
openclaw nodes pending
openclaw nodes approve <requestId>
openclaw nodes status
openclaw nodes status --connected
openclaw nodes status --last-connected 24h
```

`nodes list` prints pending/paired tables. Paired rows include the most recent connect age (Last Connect). Use `--connected` to only show currently-connected nodes. Use `--last-connected <duration>` to filter to nodes that connected within a duration (e.g. `24h`, `7d`).

## Invoke / run

```
openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
openclaw nodes run --node <id|name|ip> <command...>
openclaw nodes run --raw "git status"
openclaw nodes run --agent main --node <id|name|ip> --raw "git status"
```

Invoke flags:

- `--params <json>`: JSON object string (default `{}`).
- `--invoke-timeout <ms>`: node invoke timeout (default `15000`).
- `--idempotency-key <key>`: optional idempotency key.

### Exec-style defaults

`nodes run` mirrors the model’s exec behavior (defaults + approvals):

- Reads `tools.exec.*` (plus `agents.list[].tools.exec.*` overrides).
- Uses exec approvals (`exec.approval.request`) before invoking `system.run`.
- `--node` can be omitted when `tools.exec.node` is set.
- Requires a node that advertises `system.run` (macOS companion app or headless node host).

Flags:

- `--cwd <path>`: working directory.
- `--env <key=val>`: env override (repeatable).
- `--command-timeout <ms>`: command timeout.
- `--invoke-timeout <ms>`: node invoke timeout (default `30000`).
- `--needs-screen-recording`: require screen recording permission.
- `--raw <command>`: run a shell string (`/bin/sh -lc` or `cmd.exe /c`).
- `--agent <id>`: agent-scoped approvals/allowlists (defaults to configured agent).
- `--ask <off|on-miss|always>`, `--security <deny|allowlist|full>`: overrides.