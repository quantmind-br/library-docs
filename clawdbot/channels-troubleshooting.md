---
title: "null"
url: https://docs.clawd.bot/channels/troubleshooting.md
source: llms
fetched_at: 2026-01-26T10:11:55.282991598-03:00
rendered_js: false
word_count: 108
summary: This document provides diagnostic commands and troubleshooting steps for resolving connectivity and configuration issues across Discord, Telegram, and WhatsApp channels.
tags:
    - troubleshooting
    - diagnostics
    - clawdbot-cli
    - channel-configuration
    - network-connectivity
    - telegram-errors
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Channel troubleshooting

Start with:

```bash  theme={null}
clawdbot doctor
clawdbot channels status --probe
```

`channels status --probe` prints warnings when it can detect common channel misconfigurations, and includes small live checks (credentials, some permissions/membership).

## Channels

* Discord: [/channels/discord#troubleshooting](/channels/discord#troubleshooting)
* Telegram: [/channels/telegram#troubleshooting](/channels/telegram#troubleshooting)
* WhatsApp: [/channels/whatsapp#troubleshooting-quick](/channels/whatsapp#troubleshooting-quick)

## Telegram quick fixes

* Logs show `HttpError: Network request for 'sendMessage' failed` or `sendChatAction` → check IPv6 DNS. If `api.telegram.org` resolves to IPv6 first and the host lacks IPv6 egress, force IPv4 or enable IPv6. See [/channels/telegram#troubleshooting](/channels/telegram#troubleshooting).
* Logs show `setMyCommands failed` → check outbound HTTPS and DNS reachability to `api.telegram.org` (common on locked-down VPS or proxies).