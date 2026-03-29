---
title: Index - OpenClaw
url: https://docs.openclaw.ai/channels
source: sitemap
fetched_at: 2026-01-30T20:36:58.401798521-03:00
rendered_js: false
word_count: 294
summary: This document provides an overview of the various chat channels supported by OpenClaw, explaining how each channel connects through the Gateway and detailing their specific features and setup requirements.
tags:
    - chat-channels
    - gateway
    - messaging-platforms
    - multi-channel-support
    - whatsapp
    - telegram
    - discord
category: reference
---

## Chat Channels

OpenClaw can talk to you on any chat app you already use. Each channel connects via the Gateway. Text is supported everywhere; media and reactions vary by channel.

## Supported channels

- [WhatsApp](https://docs.openclaw.ai/channels/whatsapp) — Most popular; uses Baileys and requires QR pairing.
- [Telegram](https://docs.openclaw.ai/channels/telegram) — Bot API via grammY; supports groups.
- [Discord](https://docs.openclaw.ai/channels/discord) — Discord Bot API + Gateway; supports servers, channels, and DMs.
- [Slack](https://docs.openclaw.ai/channels/slack) — Bolt SDK; workspace apps.
- [Google Chat](https://docs.openclaw.ai/channels/googlechat) — Google Chat API app via HTTP webhook.
- [Mattermost](https://docs.openclaw.ai/channels/mattermost) — Bot API + WebSocket; channels, groups, DMs (plugin, installed separately).
- [Signal](https://docs.openclaw.ai/channels/signal) — signal-cli; privacy-focused.
- [BlueBubbles](https://docs.openclaw.ai/channels/bluebubbles) — **Recommended for iMessage**; uses the BlueBubbles macOS server REST API with full feature support (edit, unsend, effects, reactions, group management — edit currently broken on macOS 26 Tahoe).
- [iMessage](https://docs.openclaw.ai/channels/imessage) — macOS only; native integration via imsg (legacy, consider BlueBubbles for new setups).
- [Microsoft Teams](https://docs.openclaw.ai/channels/msteams) — Bot Framework; enterprise support (plugin, installed separately).
- [LINE](https://docs.openclaw.ai/channels/line) — LINE Messaging API bot (plugin, installed separately).
- [Nextcloud Talk](https://docs.openclaw.ai/channels/nextcloud-talk) — Self-hosted chat via Nextcloud Talk (plugin, installed separately).
- [Matrix](https://docs.openclaw.ai/channels/matrix) — Matrix protocol (plugin, installed separately).
- [Nostr](https://docs.openclaw.ai/channels/nostr) — Decentralized DMs via NIP-04 (plugin, installed separately).
- [Tlon](https://docs.openclaw.ai/channels/tlon) — Urbit-based messenger (plugin, installed separately).
- [Twitch](https://docs.openclaw.ai/channels/twitch) — Twitch chat via IRC connection (plugin, installed separately).
- [Zalo](https://docs.openclaw.ai/channels/zalo) — Zalo Bot API; Vietnam’s popular messenger (plugin, installed separately).
- [Zalo Personal](https://docs.openclaw.ai/channels/zalouser) — Zalo personal account via QR login (plugin, installed separately).
- [WebChat](https://docs.openclaw.ai/web/webchat) — Gateway WebChat UI over WebSocket.

## Notes

- Channels can run simultaneously; configure multiple and OpenClaw will route per chat.
- Fastest setup is usually **Telegram** (simple bot token). WhatsApp requires QR pairing and stores more state on disk.
- Group behavior varies by channel; see [Groups](https://docs.openclaw.ai/concepts/groups).
- DM pairing and allowlists are enforced for safety; see [Security](https://docs.openclaw.ai/gateway/security).
- Telegram internals: [grammY notes](https://docs.openclaw.ai/channels/grammy).
- Troubleshooting: [Channel troubleshooting](https://docs.openclaw.ai/channels/troubleshooting).
- Model providers are documented separately; see [Model Providers](https://docs.openclaw.ai/providers/models).