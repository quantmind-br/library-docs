---
title: List Browser Sessions - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:26:08.487621-03:00
rendered_js: false
word_count: 108
summary: This document provides the API specification for retrieving browser session details, including connection URLs and status information, using bearer token authentication.
tags:
    - api-reference
    - browser-sessions
    - rest-api
    - authentication
    - web-scraping
category: api
---

HeaderValue`Authorization``Bearer <API_KEY>`

## Query Parameters

ParameterTypeRequiredDescription`status`stringNoFilter by session status: `"active"` or `"destroyed"`

## Response

FieldTypeDescription`success`booleanWhether the request succeeded`sessions`arrayList of session objects

### Session Object

FieldTypeDescription`id`stringUnique session identifier`status`stringCurrent session status (`"active"` or `"destroyed"`)`cdpUrl`stringWebSocket URL for CDP connections`liveViewUrl`stringURL to watch the session in real time`interactiveLiveViewUrl`stringURL to interact with the session in real time (click, type, scroll)`createdAt`stringISO 8601 timestamp of session creation`lastActivity`stringISO 8601 timestamp of last activity

### Example Request

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### Example Response

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

Filter sessions by status

Available options:

`active`,

`destroyed`

#### Response