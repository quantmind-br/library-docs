---
title: "null"
url: https://docs.clawd.bot/tools/reactions.md
source: llms
fetched_at: 2026-01-26T09:54:18.953137562-03:00
rendered_js: false
word_count: 138
summary: This document outlines the unified semantics and platform-specific behaviors for managing emoji reactions across various messaging channels.
tags:
    - messaging-channels
    - reactions
    - emoji-management
    - bot-tools
    - cross-platform
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Reaction tooling

Shared reaction semantics across channels:

* `emoji` is required when adding a reaction.
* `emoji=""` removes the bot's reaction(s) when supported.
* `remove: true` removes the specified emoji when supported (requires `emoji`).

Channel notes:

* **Discord/Slack**: empty `emoji` removes all of the bot's reactions on the message; `remove: true` removes just that emoji.
* **Google Chat**: empty `emoji` removes the app's reactions on the message; `remove: true` removes just that emoji.
* **Telegram**: empty `emoji` removes the bot's reactions; `remove: true` also removes reactions but still requires a non-empty `emoji` for tool validation.
* **WhatsApp**: empty `emoji` removes the bot reaction; `remove: true` maps to empty emoji (still requires `emoji`).
* **Signal**: inbound reaction notifications emit system events when `channels.signal.reactionNotifications` is enabled.