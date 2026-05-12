---
title: Create Browser Session - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:26:17.815154-03:00
rendered_js: false
word_count: 247
summary: This document provides the API specifications for initiating a managed browser session, including parameter configurations for session duration, inactivity timeouts, and persistent storage settings.
tags:
    - api-reference
    - browser-automation
    - session-management
    - http-requests
    - cdp-integration
    - persistent-storage
category: api
---

HeaderValue`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Request Body

ParameterTypeRequiredDefaultDescription`ttl`numberNo600Total session lifetime in seconds (30-3600)`activityTtl`numberNo300Seconds of inactivity before session is destroyed (10-3600)`profile`objectNo—Enable persistent storage across sessions. See below.`profile.name`stringYes\*—Name for the profile (1-128 chars). Sessions with the same name share storage.`profile.saveChanges`booleanNo`true`When `true`, browser state is saved back to the profile on close. Set to `false` to load existing data without writing. Only one saver is allowed at a time.

## Response

FieldTypeDescription`success`booleanWhether the session was created`id`stringUnique session identifier`cdpUrl`stringWebSocket URL for CDP connections`liveViewUrl`stringURL to watch the session in real time`interactiveLiveViewUrl`stringURL to interact with the session in real time (click, type, scroll)`expiresAt`stringWhen the session will expire based on TTL

### Example Request

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### Example Response

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

Total time-to-live in seconds for the browser session

Required range: `30 <= x <= 3600`

Time in seconds before the session is destroyed due to inactivity

Required range: `10 <= x <= 3600`

Whether to stream a live view of the browser

Enable persistent storage across browser sessions. Data saved in one session can be loaded in a later session using the same name.

#### Response

Browser session created successfully

The unique session identifier

WebSocket URL for Chrome DevTools Protocol access

URL to view the browser session in real time

URL to interact with the browser session in real time (click, type, scroll)

When the session will expire based on TTL