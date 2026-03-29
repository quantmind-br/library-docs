---
title: Rpc - OpenClaw
url: https://docs.openclaw.ai/reference/rpc
source: sitemap
fetched_at: 2026-01-30T20:24:43.966906408-03:00
rendered_js: false
word_count: 123
summary: 'This document explains how OpenClaw integrates external CLIs using JSON-RPC through two distinct adapter patterns: HTTP daemon and stdio child processes. It outlines the technical specifications and guidelines for implementing these RPC adapters.'
tags:
    - rpc-adapters
    - json-rpc
    - cli-integration
    - daemon-process
    - stdio-communication
    - adapter-patterns
category: reference
---

## RPC adapters

OpenClaw integrates external CLIs via JSON-RPC. Two patterns are used today.

## Pattern A: HTTP daemon (signal-cli)

- `signal-cli` runs as a daemon with JSON-RPC over HTTP.
- Event stream is SSE (`/api/v1/events`).
- Health probe: `/api/v1/check`.
- OpenClaw owns lifecycle when `channels.signal.autoStart=true`.

See [Signal](https://docs.openclaw.ai/channels/signal) for setup and endpoints.

## Pattern B: stdio child process (imsg)

- OpenClaw spawns `imsg rpc` as a child process.
- JSON-RPC is line-delimited over stdin/stdout (one JSON object per line).
- No TCP port, no daemon required.

Core methods used:

- `watch.subscribe` → notifications (`method: "message"`)
- `watch.unsubscribe`
- `send`
- `chats.list` (probe/diagnostics)

See [iMessage](https://docs.openclaw.ai/channels/imessage) for setup and addressing (`chat_id` preferred).

## Adapter guidelines

- Gateway owns the process (start/stop tied to provider lifecycle).
- Keep RPC clients resilient: timeouts, restart on exit.
- Prefer stable IDs (e.g., `chat_id`) over display strings.