---
title: Create a Message - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/anthropic-messages
source: sitemap
fetched_at: 2026-04-27T20:19:21.687811797-03:00
rendered_js: false
word_count: 129
summary: This document explains the structure and components required when sending input messages to an AI model, detailing how roles like 'user' and 'assistant' function, how consecutive turns are combined, and the various formats content can take.
tags:
    - message-structure
    - conversational-flow
    - api-input
    - role-definition
    - content-format
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Models operate on alternating `user` and `assistant` conversational turns. Specify prior turns with the `messages` parameter; the model generates the next message. Consecutive `user` or `assistant` turns are combined into a single turn.

Each input message requires a `role` and `content`. If the final message uses the `assistant` role, the response continues from that content—constraining part of the model's output.

## Single Message

```json
[{"role": "user", "content": "Hello"}]
```

## Multiple Conversational Turns

```json
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm here to help. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"}
]
```

## Partial Assistant Response

```json
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

## Content Format

The `content` field can be a string (shorthand for one text block) or an array of content blocks:

```json
{"role": "user", "content": "Hello"}
{"role": "user", "content": [{"type": "text", "text": "Hello"}]}
```

Both formats are equivalent.

> [!info]
> Use the top-level `system` parameter for system prompts—there is no `"system"` role in the Messages API.

> [!note]
> Maximum 100,000 messages per request.

See [input examples](https://docs.claude.com/en/api/messages-examples) for more details.
