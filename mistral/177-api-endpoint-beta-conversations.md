---
title: Beta Conversations
url: https://docs.mistral.ai/api/endpoint/beta/conversations
source: sitemap
fetched_at: 2026-04-26T04:01:28.915530046-03:00
rendered_js: false
word_count: 320
summary: API endpoints for managing conversational state, history, and message lifecycles.
tags:
    - rest-api
    - conversational-ai
    - message-history
    - endpoint-reference
    - conversation-management
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Conversations

API for managing conversation entities and entries.

---

## List Conversations

`GET /v1/conversations`

Retrieve conversation entities sorted by creation time.

---

## Create Conversation

`POST /v1/conversations`

Create a new conversation using a base model or agent, append entries, run completion, and return `conversation_id` for continuation.

---

## Get Conversation

`GET /v1/conversations/{conversation_id}`

Retrieve conversation entity by `conversation_id`.

---

## Append Entries

`POST /v1/conversations/{conversation_id}`

Run completion on conversation history and user entries. Returns newly created entries.

---

## Delete Conversation

`DELETE /v1/conversations/{conversation_id}`

Delete a conversation.

---

## Get History

`GET /v1/conversations/{conversation_id}/history`

Retrieve all entries (messages, connectors, function_calls) in order.

---

## Get Messages

`GET /v1/conversations/{conversation_id}/messages`

Retrieve all messages only (excludes other entry types).

---

## Restart Conversation

`POST /v1/conversations/{conversation_id}/restart`

Recreate conversation from a given entry point, run completion, return new conversation with new entries.

---

## Stream Endpoints

- `POST /v1/conversations#stream` — Create and stream
- `POST /v1/conversations/{conversation_id}#stream` — Append and stream
- `POST /v1/conversations/{conversation_id}/restart#stream` — Restart and stream

#conversation-management #message-history #rest-api
