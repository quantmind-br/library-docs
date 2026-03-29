---
title: Webchat - OpenClaw
url: https://docs.openclaw.ai/platforms/mac/webchat
source: sitemap
fetched_at: 2026-01-30T20:26:26.015701927-03:00
rendered_js: false
word_count: 158
summary: This document describes the WebChat macOS application, detailing its functionality as a native SwiftUI view that connects to a Gateway, including launch methods, debugging procedures, data plane integration, security considerations, and known limitations.
tags:
    - webchat
    - macos
    - gateway
    - websocket
    - swiftui
    - debugging
    - security
category: reference
---

## WebChat (macOS app)

The macOS menu bar app embeds the WebChat UI as a native SwiftUI view. It connects to the Gateway and defaults to the **main session** for the selected agent (with a session switcher for other sessions).

- **Local mode**: connects directly to the local Gateway WebSocket.
- **Remote mode**: forwards the Gateway control port over SSH and uses that tunnel as the data plane.

## Launch & debugging

- Manual: Lobster menu → “Open Chat”.
- Auto‑open for testing:
  
  ```
  dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
  ```
- Logs: `./scripts/clawlog.sh` (subsystem `bot.molt`, category `WebChatSwiftUI`).

## How it’s wired

- Data plane: Gateway WS methods `chat.history`, `chat.send`, `chat.abort`, `chat.inject` and events `chat`, `agent`, `presence`, `tick`, `health`.
- Session: defaults to the primary session (`main`, or `global` when scope is global). The UI can switch between sessions.
- Onboarding uses a dedicated session to keep first‑run setup separate.

## Security surface

- Remote mode forwards only the Gateway WebSocket control port over SSH.

## Known limitations

- The UI is optimized for chat sessions (not a full browser sandbox).