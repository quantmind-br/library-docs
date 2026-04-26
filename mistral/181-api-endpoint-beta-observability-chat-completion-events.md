---
title: Beta Observability Chat Completion Events
url: https://docs.mistral.ai/api/endpoint/beta/observability/chat_completion_events
source: sitemap
fetched_at: 2026-04-26T04:01:37.457105573-03:00
rendered_js: false
word_count: 49
summary: API endpoints for interacting with and retrieving chat completion observability data.
tags:
    - chat-completion
    - observability
    - api-endpoints
    - event-search
    - live-judging
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Observability Chat Completion Events

API for chat completion observability data.

---

## Search Events

`POST /v1/observability/chat-completion-events/search`

Search and return chat completion events.

---

## Search Event IDs

`POST /v1/observability/chat-completion-events/search-ids`

Alternative to `/search` returning only IDs (can return many at once).

---

## Get Event

`GET /v1/observability/chat-completion-events/{event_id}`

Get a single chat completion event.

---

## Get Similar Events

`GET /v1/observability/chat-completion-events/{event_id}/similar-events`

Get similar chat completion events.

---

## Run Live Judging

`POST /v1/observability/chat-completion-events/{event_id}/live-judging`

Run Judge on an event based on given options.

#observability #event-search #live-judging
