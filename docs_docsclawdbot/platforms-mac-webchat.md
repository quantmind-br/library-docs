---
title: "null"
url: https://docs.clawd.bot/platforms/mac/webchat.md
source: llms
fetched_at: 2026-01-26T09:53:11.140476228-03:00
rendered_js: false
word_count: 180
summary: This document provides a technical overview of the WebChat macOS menu bar application, detailing its connection modes, debugging procedures, and underlying WebSocket communication architecture.
tags:
    - macos-app
    - webchat
    - swiftui
    - websocket-api
    - ssh-tunneling
    - clawdbot
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# WebChat (macOS app)

The macOS menu bar app embeds the WebChat UI as a native SwiftUI view. It
connects to the Gateway and defaults to the **main session** for the selected
agent (with a session switcher for other sessions).

* **Local mode**: connects directly to the local Gateway WebSocket.
* **Remote mode**: forwards the Gateway control port over SSH and uses that
  tunnel as the data plane.

## Launch & debugging

* Manual: Lobster menu → “Open Chat”.
* Auto‑open for testing:
  ```bash  theme={null}
  dist/Clawdbot.app/Contents/MacOS/Clawdbot --webchat
  ```
* Logs: `./scripts/clawlog.sh` (subsystem `com.clawdbot`, category `WebChatSwiftUI`).

## How it’s wired

* Data plane: Gateway WS methods `chat.history`, `chat.send`, `chat.abort`,
  `chat.inject` and events `chat`, `agent`, `presence`, `tick`, `health`.
* Session: defaults to the primary session (`main`, or `global` when scope is
  global). The UI can switch between sessions.
* Onboarding uses a dedicated session to keep first‑run setup separate.

## Security surface

* Remote mode forwards only the Gateway WebSocket control port over SSH.

## Known limitations

* The UI is optimized for chat sessions (not a full browser sandbox).