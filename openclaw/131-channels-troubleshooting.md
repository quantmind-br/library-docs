---
title: Troubleshooting - OpenClaw
url: https://docs.openclaw.ai/channels/troubleshooting
source: sitemap
fetched_at: 2026-01-30T20:36:45.158004553-03:00
rendered_js: false
word_count: 86
summary: This document provides guidance on troubleshooting common issues with various communication channels including Discord, Telegram, and WhatsApp, with specific commands and error resolution steps.
tags:
    - channel-troubleshooting
    - discord
    - telegram
    - whatsapp
    - network-issues
    - error-resolution
category: guide
---

## Channel troubleshooting

Start with:

```
openclaw doctor
openclaw channels status --probe
```

`channels status --probe` prints warnings when it can detect common channel misconfigurations, and includes small live checks (credentials, some permissions/membership).

## Channels

- Discord: [/channels/discord#troubleshooting](https://docs.openclaw.ai/channels/discord#troubleshooting)
- Telegram: [/channels/telegram#troubleshooting](https://docs.openclaw.ai/channels/telegram#troubleshooting)
- WhatsApp: [/channels/whatsapp#troubleshooting-quick](https://docs.openclaw.ai/channels/whatsapp#troubleshooting-quick)

## Telegram quick fixes

- Logs show `HttpError: Network request for 'sendMessage' failed` or `sendChatAction` → check IPv6 DNS. If `api.telegram.org` resolves to IPv6 first and the host lacks IPv6 egress, force IPv4 or enable IPv6. See [/channels/telegram#troubleshooting](https://docs.openclaw.ai/channels/telegram#troubleshooting).
- Logs show `setMyCommands failed` → check outbound HTTPS and DNS reachability to `api.telegram.org` (common on locked-down VPS or proxies).