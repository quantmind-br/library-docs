---
title: ZeroClaw Operations Runbook
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/ops/operations-runbook.md
source: git
fetched_at: 2026-05-02T14:51:48.620502299-03:00
rendered_js: false
word_count: 330
summary: This document provides operational procedures for managing the ZeroClaw runtime, covering system health checks, incident triage, service management, and safe configuration deployment.
tags:
    - operations
    - runbook
    - incident-response
    - service-management
    - zeroclaw
    - health-monitoring
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# ZeroClaw Operations Runbook

For operators who maintain availability, security posture, and incident response.

Last verified: **February 18, 2026**

## Scope

Use for day-2 operations:
- Starting and supervising runtime
- Health checks and diagnostics
- Safe rollout and rollback
- Incident triage and recovery

For first-time installation, start from [[001-setup-guides-one-click-bootstrap|One-Click Bootstrap]].

## Runtime Modes

| Mode | Command | When to use |
|---|---|---|
| Foreground runtime | `zeroclaw daemon` | Local debugging, short-lived sessions |
| Foreground gateway only | `zeroclaw gateway` | Webhook endpoint testing |
| User service | `zeroclaw service install && zeroclaw service start` | Persistent operator-managed runtime |

## Baseline Operator Checklist

1. Validate configuration:

```bash
zeroclaw status
```

2. Verify diagnostics:

```bash
zeroclaw doctor
zeroclaw channel doctor
```

3. Start runtime:

```bash
zeroclaw daemon
```

4. For persistent user session service:

```bash
zeroclaw service install
zeroclaw service start
zeroclaw service status
```

## Health and State Signals

| Signal | Command / File | Expected |
|---|---|---|
| Config validity | `zeroclaw doctor` | No critical errors |
| Channel connectivity | `zeroclaw channel doctor` | Configured channels healthy |
| Runtime summary | `zeroclaw status` | Expected provider/model/channels |
| Daemon heartbeat/state | `~/.zeroclaw/daemon_state.json` | File updates periodically |

## Logs and Diagnostics

### macOS / Windows (service wrapper logs)

- `~/.zeroclaw/logs/daemon.stdout.log`
- `~/.zeroclaw/logs/daemon.stderr.log`

### Linux (systemd user service)

```bash
journalctl --user -u zeroclaw.service -f
```

## Incident Triage Flow (Fast Path)

1. Snapshot system state:

```bash
zeroclaw status
zeroclaw doctor
zeroclaw channel doctor
```

2. Check service state:

```bash
zeroclaw service status
```

3. If service unhealthy, restart cleanly:

```bash
zeroclaw service stop
zeroclaw service start
```

4. If channels still fail, verify allowlists and credentials in `~/.zeroclaw/config.toml`

5. If gateway involved, verify bind/auth settings (`[gateway]`) and local reachability

## Safe Change Procedure

Before applying config changes:

1. Backup `~/.zeroclaw/config.toml`
2. Apply one logical change at a time
3. Run `zeroclaw doctor`
4. Restart daemon/service
5. Verify with `status` + `channel doctor`

## Rollback Procedure

If rollout regresses behavior:

1. Restore previous `config.toml`
2. Restart runtime (`daemon` or `service`)
3. Confirm recovery via `doctor` and channel health checks
4. Document incident root cause and mitigation

## Related Docs

- [[001-setup-guides-one-click-bootstrap|One-Click Bootstrap]]
- [[070-ops-troubleshooting|Troubleshooting]]
- [[123-reference-config-reference|Config Reference]]
- [[120-reference-cli-commands-reference|Commands Reference]]

#operations #runbook #incident-response #service-management #zeroclaw #health-monitoring
