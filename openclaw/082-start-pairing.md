---
title: Pairing - OpenClaw
url: https://docs.openclaw.ai/start/pairing
source: sitemap
fetched_at: 2026-01-30T20:23:24.59430373-03:00
rendered_js: false
word_count: 259
summary: This document explains OpenClaw's pairing mechanism for managing secure access to the gateway, covering both direct message sender approval and device/node authorization processes.
tags:
    - pairing
    - security
    - access-control
    - device-management
    - gateway-network
category: guide
---

“Pairing” is OpenClaw’s explicit **owner approval** step. It is used in two places:

1. **DM pairing** (who is allowed to talk to the bot)
2. **Node pairing** (which devices/nodes are allowed to join the gateway network)

Security context: [Security](https://docs.openclaw.ai/gateway/security)

## 1) DM pairing (inbound chat access)

When a channel is configured with DM policy `pairing`, unknown senders get a short code and their message is **not processed** until you approve. Default DM policies are documented in: [Security](https://docs.openclaw.ai/gateway/security) Pairing codes:

- 8 characters, uppercase, no ambiguous chars (`0O1I`).
- **Expire after 1 hour**. The bot only sends the pairing message when a new request is created (roughly once per hour per sender).
- Pending DM pairing requests are capped at **3 per channel** by default; additional requests are ignored until one expires or is approved.

### Approve a sender

```
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

Supported channels: `telegram`, `whatsapp`, `signal`, `imessage`, `discord`, `slack`.

### Where the state lives

Stored under `~/.openclaw/credentials/`:

- Pending requests: `<channel>-pairing.json`
- Approved allowlist store: `<channel>-allowFrom.json`

Treat these as sensitive (they gate access to your assistant).

## 2) Node device pairing (iOS/Android/macOS/headless nodes)

Nodes connect to the Gateway as **devices** with `role: node`. The Gateway creates a device pairing request that must be approved.

### Approve a node device

```
openclaw devices list
openclaw devices approve <requestId>
openclaw devices reject <requestId>
```

### Where the state lives

Stored under `~/.openclaw/devices/`:

- `pending.json` (short-lived; pending requests expire)
- `paired.json` (paired devices + tokens)

### Notes

- The legacy `node.pair.*` API (CLI: `openclaw nodes pending/approve`) is a separate gateway-owned pairing store. WS nodes still require device pairing.

<!--THE END-->

- Security model + prompt injection: [Security](https://docs.openclaw.ai/gateway/security)
- Updating safely (run doctor): [Updating](https://docs.openclaw.ai/install/updating)
- Channel configs:
  
  - Telegram: [Telegram](https://docs.openclaw.ai/channels/telegram)
  - WhatsApp: [WhatsApp](https://docs.openclaw.ai/channels/whatsapp)
  - Signal: [Signal](https://docs.openclaw.ai/channels/signal)
  - iMessage: [iMessage](https://docs.openclaw.ai/channels/imessage)
  - Discord: [Discord](https://docs.openclaw.ai/channels/discord)
  - Slack: [Slack](https://docs.openclaw.ai/channels/slack)