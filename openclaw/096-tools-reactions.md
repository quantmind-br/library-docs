---
title: Reactions - OpenClaw
url: https://docs.openclaw.ai/tools/reactions
source: sitemap
fetched_at: 2026-01-30T20:21:57.088757615-03:00
rendered_js: false
word_count: 116
summary: Explains the standardized semantics and channel-specific behavior for adding and removing reactions across different messaging platforms.
tags:
    - reaction-tooling
    - cross-platform
    - discord
    - slack
    - telegram
    - whatsapp
    - signal
category: reference
---

## Reaction tooling

Shared reaction semantics across channels:

- `emoji` is required when adding a reaction.
- `emoji=""` removes the bot’s reaction(s) when supported.
- `remove: true` removes the specified emoji when supported (requires `emoji`).

Channel notes:

- **Discord/Slack**: empty `emoji` removes all of the bot’s reactions on the message; `remove: true` removes just that emoji.
- **Google Chat**: empty `emoji` removes the app’s reactions on the message; `remove: true` removes just that emoji.
- **Telegram**: empty `emoji` removes the bot’s reactions; `remove: true` also removes reactions but still requires a non-empty `emoji` for tool validation.
- **WhatsApp**: empty `emoji` removes the bot reaction; `remove: true` maps to empty emoji (still requires `emoji`).
- **Signal**: inbound reaction notifications emit system events when `channels.signal.reactionNotifications` is enabled.