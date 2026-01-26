---
title: "null"
url: https://docs.clawd.bot/cli/system.md
source: llms
fetched_at: 2026-01-26T09:51:03.375054839-03:00
rendered_js: false
word_count: 166
summary: This document provides a technical reference for the clawdbot system CLI commands used to manage system events, heartbeat controls, and presence monitoring within the Gateway.
tags:
    - cli-reference
    - system-events
    - heartbeat-control
    - presence-monitoring
    - gateway-management
    - clawdbot
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# `clawdbot system`

System-level helpers for the Gateway: enqueue system events, control heartbeats,
and view presence.

## Common commands

```bash  theme={null}
clawdbot system event --text "Check for urgent follow-ups" --mode now
clawdbot system heartbeat enable
clawdbot system heartbeat last
clawdbot system presence
```

## `system event`

Enqueue a system event on the **main** session. The next heartbeat will inject
it as a `System:` line in the prompt. Use `--mode now` to trigger the heartbeat
immediately; `next-heartbeat` waits for the next scheduled tick.

Flags:

* `--text <text>`: required system event text.
* `--mode <mode>`: `now` or `next-heartbeat` (default).
* `--json`: machine-readable output.

## `system heartbeat last|enable|disable`

Heartbeat controls:

* `last`: show the last heartbeat event.
* `enable`: turn heartbeats back on (use this if they were disabled).
* `disable`: pause heartbeats.

Flags:

* `--json`: machine-readable output.

## `system presence`

List the current system presence entries the Gateway knows about (nodes,
instances, and similar status lines).

Flags:

* `--json`: machine-readable output.

## Notes

* Requires a running Gateway reachable by your current config (local or remote).
* System events are ephemeral and not persisted across restarts.