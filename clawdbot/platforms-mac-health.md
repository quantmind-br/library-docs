---
title: "null"
url: https://docs.clawd.bot/platforms/mac/health.md
source: llms
fetched_at: 2026-01-26T10:14:28.614291368-03:00
rendered_js: false
word_count: 213
summary: This document explains how to monitor the connection health of linked communication channels using the macOS menu bar application and its settings interface.
tags:
    - macos
    - health-check
    - status-monitoring
    - clawdbot
    - connectivity
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Health Checks on macOS

How to see whether the linked channel is healthy from the menu bar app.

## Menu bar

* Status dot now reflects Baileys health:
  * Green: linked + socket opened recently.
  * Orange: connecting/retrying.
  * Red: logged out or probe failed.
* Secondary line reads "linked · auth 12m" or shows the failure reason.
* "Run Health Check" menu item triggers an on-demand probe.

## Settings

* General tab gains a Health card showing: linked auth age, session-store path/count, last check time, last error/status code, and buttons for Run Health Check / Reveal Logs.
* Uses a cached snapshot so the UI loads instantly and falls back gracefully when offline.
* **Channels tab** surfaces channel status + controls for WhatsApp/Telegram (login QR, logout, probe, last disconnect/error).

## How the probe works

* App runs `clawdbot health --json` via `ShellExecutor` every \~60s and on demand. The probe loads creds and reports status without sending messages.
* Cache the last good snapshot and the last error separately to avoid flicker; show the timestamp of each.

## When in doubt

* You can still use the CLI flow in [Gateway health](/gateway/health) (`clawdbot status`, `clawdbot status --deep`, `clawdbot health --json`) and tail `/tmp/clawdbot/clawdbot-*.log` for `web-heartbeat` / `web-reconnect`.