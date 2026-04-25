---
title: LM Link
url: https://lmstudio.ai/docs/lmlink
source: sitemap
fetched_at: 2026-04-07T21:27:43.706398746-03:00
rendered_js: false
word_count: 243
summary: This document introduces LM Link, a feature in LM Studio that establishes custom, end-to-end encrypted networks to allow users to access and serve local LLMs across multiple personal devices.
tags:
    - lm-link
    - local-models
    - device-sync
    - tailscale
    - llm-serving
    - encryption
category: guide
---

![undefined](https://lmstudio.ai/assets/docs/lmlink-animation.gif)

LM Link is a new feature in LM Studio that provides a way to access local models across devices, wherever you are. Links are custom made, end-to-end encrypted networks intended for loading and serving LLMs across devices you own, made possible in partnership with Tailscale.

## What can I do with LM Link?[](#what-can-i-do-with-lm-link "Link to 'What can I do with LM Link?'")

LM Link unlocks the full potential of your hardware by sharing compute across connected devices. For example, you might have a powerful desktop in your home office, and a lightweight laptop you carry on the go. With LM Link, you can run large open-weight models on a powerful machine, and use them seamlessly from your laptop as if they were local. All communication and data transfer between devices is always end-to-end encrypted, thanks to Tailscale.

## Use Cases[](#use-cases "Link to 'Use Cases'")

LM Link use cases span individuals as well as teams.

You can manage a private link to keep your prized gaming GPU busy even when you're on the go. Moreover, LM Link allows you to set up LLM serving in a server and start using it with just few clicks.

## Use LM Link with[](#use-lm-link-with "Link to 'Use LM Link with'")

- **CLI** — manage LM Link from the terminal with [`lms link`](https://lmstudio.ai/docs/cli/link/link-enable)
- **REST API** — use remote models via the REST API with [LM Link](https://lmstudio.ai/docs/developer/core/lmlink)
- **Integrations** — use remote models with coding tools like Claude Code and Codex via [LM Link](https://lmstudio.ai/docs/integrations/lmlink)