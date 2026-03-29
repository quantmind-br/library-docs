---
title: Index - OpenClaw
url: https://docs.openclaw.ai
source: sitemap
fetched_at: 2026-01-30T20:38:52.167970724-03:00
rendered_js: false
word_count: 800
summary: OpenClaw is a platform that connects messaging platforms like WhatsApp, Telegram, Discord, and iMessage to AI coding agents such as Pi, enabling users to send messages and receive agent responses through various channels. It provides a gateway service for managing connections and integrates with web interfaces and mobile applications.
tags:
    - messaging-integration
    - ai-agents
    - whatsapp
    - telegram
    - discord
    - api-gateway
    - coding-tools
    - multi-platform-support
category: guide
---

> *“EXFOLIATE! EXFOLIATE!”* — A space lobster, probably

![OpenClaw](https://mintcdn.com/clawdhub/FaXdIfo7gPK_jSWb/assets/openclaw-logo-text.png?fit=max&auto=format&n=FaXdIfo7gPK_jSWb&q=85&s=d799bea41acb92d4c9fd1075c575879f)

![OpenClaw](https://mintcdn.com/clawdhub/FaXdIfo7gPK_jSWb/whatsapp-openclaw.jpg?fit=max&auto=format&n=FaXdIfo7gPK_jSWb&q=85&s=b74a3630b0e971f466eff15fbdc642cb)

**Any OS + WhatsApp/Telegram/Discord/iMessage gateway for AI agents (Pi).**  
Plugins add Mattermost and more. Send a message, get an agent response — from your pocket.

[GitHub](https://github.com/openclaw/openclaw) · [Releases](https://github.com/openclaw/openclaw/releases) · [Docs](https://docs.openclaw.ai/) · [OpenClaw assistant setup](https://docs.openclaw.ai/start/openclaw)

OpenClaw bridges WhatsApp (via WhatsApp Web / Baileys), Telegram (Bot API / grammY), Discord (Bot API / channels.discord.js), and iMessage (imsg CLI) to coding agents like [Pi](https://github.com/badlogic/pi-mono). Plugins add Mattermost (Bot API + WebSocket) and more. OpenClaw also powers the OpenClaw assistant.

## Start here

- **New install from zero:** [Getting Started](https://docs.openclaw.ai/start/getting-started)
- **Guided setup (recommended):** [Wizard](https://docs.openclaw.ai/start/wizard) (`openclaw onboard`)
- **Open the dashboard (local Gateway):** [http://127.0.0.1:18789/](http://127.0.0.1:18789/) (or [http://localhost:18789/](http://localhost:18789/))

If the Gateway is running on the same computer, that link opens the browser Control UI immediately. If it fails, start the Gateway first: `openclaw gateway`.

## Dashboard (browser Control UI)

The dashboard is the browser Control UI for chat, config, nodes, sessions, and more. Local default: [http://127.0.0.1:18789/](http://127.0.0.1:18789/) Remote access: [Web surfaces](https://docs.openclaw.ai/web) and [Tailscale](https://docs.openclaw.ai/gateway/tailscale)

## How it works

```
WhatsApp / Telegram / Discord / iMessage (+ plugins)
        │
        ▼
  ┌───────────────────────────┐
  │          Gateway          │  ws://127.0.0.1:18789 (loopback-only)
  │     (single source)       │
  │                           │  http://<gateway-host>:18793
  │                           │    /__openclaw__/canvas/ (Canvas host)
  └───────────┬───────────────┘
              │
              ├─ Pi agent (RPC)
              ├─ CLI (openclaw …)
              ├─ Chat UI (SwiftUI)
              ├─ macOS app (OpenClaw.app)
              ├─ iOS node via Gateway WS + pairing
              └─ Android node via Gateway WS + pairing
```

Most operations flow through the **Gateway** (`openclaw gateway`), a single long-running process that owns channel connections and the WebSocket control plane.

## Network model

- **One Gateway per host (recommended)**: it is the only process allowed to own the WhatsApp Web session. If you need a rescue bot or strict isolation, run multiple gateways with isolated profiles and ports; see [Multiple gateways](https://docs.openclaw.ai/gateway/multiple-gateways).
- **Loopback-first**: Gateway WS defaults to `ws://127.0.0.1:18789`.
  
  - The wizard now generates a gateway token by default (even for loopback).
  - For Tailnet access, run `openclaw gateway --bind tailnet --token ...` (token is required for non-loopback binds).
- **Nodes**: connect to the Gateway WebSocket (LAN/tailnet/SSH as needed); legacy TCP bridge is deprecated/removed.
- **Canvas host**: HTTP file server on `canvasHost.port` (default `18793`), serving `/__openclaw__/canvas/` for node WebViews; see [Gateway configuration](https://docs.openclaw.ai/gateway/configuration) (`canvasHost`).
- **Remote use**: SSH tunnel or tailnet/VPN; see [Remote access](https://docs.openclaw.ai/gateway/remote) and [Discovery](https://docs.openclaw.ai/gateway/discovery).

## Features (high level)

- 📱 **WhatsApp Integration** — Uses Baileys for WhatsApp Web protocol
- ✈️ **Telegram Bot** — DMs + groups via grammY
- 🎮 **Discord Bot** — DMs + guild channels via channels.discord.js
- 🧩 **Mattermost Bot (plugin)** — Bot token + WebSocket events
- 💬 **iMessage** — Local imsg CLI integration (macOS)
- 🤖 **Agent bridge** — Pi (RPC mode) with tool streaming
- ⏱️ **Streaming + chunking** — Block streaming + Telegram draft streaming details ([/concepts/streaming](https://docs.openclaw.ai/concepts/streaming))
- 🧠 **Multi-agent routing** — Route provider accounts/peers to isolated agents (workspace + per-agent sessions)
- 🔐 **Subscription auth** — Anthropic (Claude Pro/Max) + OpenAI (ChatGPT/Codex) via OAuth
- 💬 **Sessions** — Direct chats collapse into shared `main` (default); groups are isolated
- 👥 **Group Chat Support** — Mention-based by default; owner can toggle `/activation always|mention`
- 📎 **Media Support** — Send and receive images, audio, documents
- 🎤 **Voice notes** — Optional transcription hook
- 🖥️ **WebChat + macOS app** — Local UI + menu bar companion for ops and voice wake
- 📱 **iOS node** — Pairs as a node and exposes a Canvas surface
- 📱 **Android node** — Pairs as a node and exposes Canvas + Chat + Camera

Note: legacy Claude/Codex/Gemini/Opencode paths have been removed; Pi is the only coding-agent path.

## Quick start

Runtime requirement: **Node ≥ 22**.

```
# Recommended: global install (npm/pnpm)
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

# Onboard + install the service (launchd/systemd user service)
openclaw onboard --install-daemon

# Pair WhatsApp Web (shows QR)
openclaw channels login

# Gateway runs via the service after onboarding; manual run is still possible:
openclaw gateway --port 18789
```

Switching between npm and git installs later is easy: install the other flavor and run `openclaw doctor` to update the gateway service entrypoint. From source (development):

```
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build
openclaw onboard --install-daemon
```

If you don’t have a global install yet, run the onboarding step via `pnpm openclaw ...` from the repo. Multi-instance quickstart (optional):

```
OPENCLAW_CONFIG_PATH=~/.openclaw/a.json \
OPENCLAW_STATE_DIR=~/.openclaw-a \
openclaw gateway --port 19001
```

Send a test message (requires a running Gateway):

```
openclaw message send --target +15555550123 --message "Hello from OpenClaw"
```

## Configuration (optional)

Config lives at `~/.openclaw/openclaw.json`.

- If you **do nothing**, OpenClaw uses the bundled Pi binary in RPC mode with per-sender sessions.
- If you want to lock it down, start with `channels.whatsapp.allowFrom` and (for groups) mention rules.

Example:

```
{
  channels: {
    whatsapp: {
      allowFrom: ["+15555550123"],
      groups: { "*": { requireMention: true } }
    }
  },
  messages: { groupChat: { mentionPatterns: ["@openclaw"] } }
}
```

## Docs

- Start here:
  
  - [Docs hubs (all pages linked)](https://docs.openclaw.ai/start/hubs)
  - [Help](https://docs.openclaw.ai/help) ← *common fixes + troubleshooting*
  - [Configuration](https://docs.openclaw.ai/gateway/configuration)
  - [Configuration examples](https://docs.openclaw.ai/gateway/configuration-examples)
  - [Slash commands](https://docs.openclaw.ai/tools/slash-commands)
  - [Multi-agent routing](https://docs.openclaw.ai/concepts/multi-agent)
  - [Updating / rollback](https://docs.openclaw.ai/install/updating)
  - [Pairing (DM + nodes)](https://docs.openclaw.ai/start/pairing)
  - [Nix mode](https://docs.openclaw.ai/install/nix)
  - [OpenClaw assistant setup](https://docs.openclaw.ai/start/openclaw)
  - [Skills](https://docs.openclaw.ai/tools/skills)
  - [Skills config](https://docs.openclaw.ai/tools/skills-config)
  - [Workspace templates](https://docs.openclaw.ai/reference/templates/AGENTS)
  - [RPC adapters](https://docs.openclaw.ai/reference/rpc)
  - [Gateway runbook](https://docs.openclaw.ai/gateway)
  - [Nodes (iOS/Android)](https://docs.openclaw.ai/nodes)
  - [Web surfaces (Control UI)](https://docs.openclaw.ai/web)
  - [Discovery + transports](https://docs.openclaw.ai/gateway/discovery)
  - [Remote access](https://docs.openclaw.ai/gateway/remote)
- Providers and UX:
  
  - [WebChat](https://docs.openclaw.ai/web/webchat)
  - [Control UI (browser)](https://docs.openclaw.ai/web/control-ui)
  - [Telegram](https://docs.openclaw.ai/channels/telegram)
  - [Discord](https://docs.openclaw.ai/channels/discord)
  - [Mattermost (plugin)](https://docs.openclaw.ai/channels/mattermost)
  - [iMessage](https://docs.openclaw.ai/channels/imessage)
  - [Groups](https://docs.openclaw.ai/concepts/groups)
  - [WhatsApp group messages](https://docs.openclaw.ai/concepts/group-messages)
  - [Media: images](https://docs.openclaw.ai/nodes/images)
  - [Media: audio](https://docs.openclaw.ai/nodes/audio)
- Companion apps:
  
  - [macOS app](https://docs.openclaw.ai/platforms/macos)
  - [iOS app](https://docs.openclaw.ai/platforms/ios)
  - [Android app](https://docs.openclaw.ai/platforms/android)
  - [Windows (WSL2)](https://docs.openclaw.ai/platforms/windows)
  - [Linux app](https://docs.openclaw.ai/platforms/linux)
- Ops and safety:
  
  - [Sessions](https://docs.openclaw.ai/concepts/session)
  - [Cron jobs](https://docs.openclaw.ai/automation/cron-jobs)
  - [Webhooks](https://docs.openclaw.ai/automation/webhook)
  - [Gmail hooks (Pub/Sub)](https://docs.openclaw.ai/automation/gmail-pubsub)
  - [Security](https://docs.openclaw.ai/gateway/security)
  - [Troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)

## The name

**OpenClaw = CLAW + TARDIS** — because every space lobster needs a time-and-space machine.

* * *

*“We’re all just playing with our own prompts.”* — an AI, probably high on tokens

## Credits

- **Peter Steinberger** ([@steipete](https://twitter.com/steipete)) — Creator, lobster whisperer
- **Mario Zechner** ([@badlogicc](https://twitter.com/badlogicgames)) — Pi creator, security pen-tester
- **Clawd** — The space lobster who demanded a better name

## Core Contributors

- **Maxim Vovshin** (@Hyaxia, [36747317+Hyaxia@users.noreply.github.com](mailto:36747317+Hyaxia@users.noreply.github.com)) — Blogwatcher skill
- **Nacho Iacovino** (@nachoiacovino, [nacho.iacovino@gmail.com](mailto:nacho.iacovino@gmail.com)) — Location parsing (Telegram + WhatsApp)

## License

MIT — Free as a lobster in the ocean 🦞

* * *

*“We’re all just playing with our own prompts.”* — An AI, probably high on tokens