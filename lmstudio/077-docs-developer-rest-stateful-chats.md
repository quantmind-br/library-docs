---
title: Stateful Chats
url: https://lmstudio.ai/docs/developer/rest/stateful-chats
source: sitemap
fetched_at: 2026-04-07T21:30:14.904733269-03:00
rendered_js: false
word_count: 192
summary: This document explains how the stateful nature of the /api/v1/chat endpoint works, detailing methods for continuing conversations using response IDs or disabling state storage entirely.
tags:
    - api-endpoint
    - chat-context
    - stateful-storage
    - response-id
    - conversation-management
category: guide
---

The `/api/v1/chat` endpoint is stateful by default. This means you don't need to pass the full conversation history in every request — LM Studio automatically stores and manages the context for you.

## How it works[](#how-it-works "Link to 'How it works'")

When you send a chat request, LM Studio stores the conversation in a chat thread and returns a `response_id` in the response. Use this `response_id` in subsequent requests to continue the conversation.

The response includes a `response_id`:

Every response includes an unique `response_id` that you can use to reference that specific point in the conversation for future requests. This allows you to branch conversations.

## Continue a conversation[](#continue-a-conversation "Link to 'Continue a conversation'")

Pass the `previous_response_id` in your next request to continue the conversation. The model will remember the previous context.

The model can reference the previous message without you needing to resend it and will return a new `response_id` for further continuation.

## Disable stateful storage[](#disable-stateful-storage "Link to 'Disable stateful storage'")

If you don't want to store the conversation, set `store` to `false`. The response will not include a `response_id`.

This is useful for one-off requests where you don't need to maintain context.