---
title: Flash Answers | Mistral Docs
url: https://docs.mistral.ai/le-chat/conversation/flash-answers
source: sitemap
fetched_at: 2026-04-26T04:07:43.796716626-03:00
rendered_js: false
word_count: 327
summary: This document explains the Flash Answers feature in Le Chat, which prioritizes response speed over reasoning depth for quick tasks and drafts.
tags:
    - flash-answers
    - le-chat
    - model-settings
    - low-latency
    - conversational-ai
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Flash Answers delivers answers at up to 10x usual speed, generating 1,000+ tokens per second. It prioritizes speed over chain-of-thought reasoning, providing direct answers instead of step-by-step explanations.

> [!info]
> [Deep Research](https://docs.mistral.ai/le-chat/research-analysis/deep-research) uses Flash Answers to generate full reports at speed once research phase completes.

## Activating Flash Answers

1. Click the `Flash` button at the bottom of the chat window
2. Type and send your message
3. Flash mode stays active until you click `Flash` again to revert

## Best Use Cases

- **Quick factual questions**: definitions, dates, concise explanations
- **Short-form content**: email drafts, social posts, talking points
- **Iterative brainstorming**: rapid idea generation without waiting
- **First drafts**: rough version fast, then polish with standard model or [[128-le-chat-conversation-flash-answers|Canvas]]

## When to Use Instead

> [!warning]
> Flash Answers trades reasoning depth for speed. Not suitable for multi-step logic, nuanced analysis, or careful trade-off evaluation.

Use **[Think mode](https://docs.mistral.ai/le-chat/conversation/think-mode)** for complex problems requiring chain-of-thought reasoning.

| Mode | Use When |
|------|----------|
| **Flash Answers** | Straightforward answer needed |
| **Think mode** | Model's reasoning wanted before trusting answer |
| **Deep Research** | Automated multi-source web research |
| **Chat** | Standard conversational mode |

#flash-answers #low-latency #le-chat