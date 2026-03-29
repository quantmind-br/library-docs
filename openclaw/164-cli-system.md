---
title: System - OpenClaw
url: https://docs.openclaw.ai/cli/system
source: sitemap
fetched_at: 2026-01-30T20:34:27.990669982-03:00
rendered_js: false
word_count: 142
summary: Provides instructions for using system-level commands in the Gateway to manage events, heartbeats, and system presence information.
tags:
    - system-events
    - heartbeat-control
    - presence-monitoring
    - gateway-management
category: reference
---

System-level helpers for the Gateway: enqueue system events, control heartbeats, and view presence.

## Common commands

```
openclaw system event --text "Check for urgent follow-ups" --mode now
openclaw system heartbeat enable
openclaw system heartbeat last
openclaw system presence
```

## `system event`

Enqueue a system event on the **main** session. The next heartbeat will inject it as a `System:` line in the prompt. Use `--mode now` to trigger the heartbeat immediately; `next-heartbeat` waits for the next scheduled tick. Flags:

- `--text <text>`: required system event text.
- `--mode <mode>`: `now` or `next-heartbeat` (default).
- `--json`: machine-readable output.

## `system heartbeat last|enable|disable`

Heartbeat controls:

- `last`: show the last heartbeat event.
- `enable`: turn heartbeats back on (use this if they were disabled).
- `disable`: pause heartbeats.

Flags:

- `--json`: machine-readable output.

## `system presence`

List the current system presence entries the Gateway knows about (nodes, instances, and similar status lines). Flags:

- `--json`: machine-readable output.

## Notes

- Requires a running Gateway reachable by your current config (local or remote).
- System events are ephemeral and not persisted across restarts.