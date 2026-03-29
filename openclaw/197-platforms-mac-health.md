---
title: Health - OpenClaw
url: https://docs.openclaw.ai/platforms/mac/health
source: sitemap
fetched_at: 2026-01-30T20:27:20.831823003-03:00
rendered_js: false
word_count: 189
summary: Explains how to monitor and check the health status of linked channels through a macOS menu bar application, including visual indicators and diagnostic functionality.
tags:
    - health-check
    - macos
    - status-monitoring
    - channel-health
    - ui-indicators
    - probe-system
category: guide
---

## Health Checks on macOS

How to see whether the linked channel is healthy from the menu bar app.

- Status dot now reflects Baileys health:
  
  - Green: linked + socket opened recently.
  - Orange: connecting/retrying.
  - Red: logged out or probe failed.
- Secondary line reads “linked · auth 12m” or shows the failure reason.
- “Run Health Check” menu item triggers an on-demand probe.

## Settings

- General tab gains a Health card showing: linked auth age, session-store path/count, last check time, last error/status code, and buttons for Run Health Check / Reveal Logs.
- Uses a cached snapshot so the UI loads instantly and falls back gracefully when offline.
- **Channels tab** surfaces channel status + controls for WhatsApp/Telegram (login QR, logout, probe, last disconnect/error).

## How the probe works

- App runs `openclaw health --json` via `ShellExecutor` every ~60s and on demand. The probe loads creds and reports status without sending messages.
- Cache the last good snapshot and the last error separately to avoid flicker; show the timestamp of each.

## When in doubt

- You can still use the CLI flow in [Gateway health](https://docs.openclaw.ai/gateway/health) (`openclaw status`, `openclaw status --deep`, `openclaw health --json`) and tail `/tmp/openclaw/openclaw-*.log` for `web-heartbeat` / `web-reconnect`.