---
title: Delete Browser Session - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:26:12.111518-03:00
rendered_js: false
word_count: 71
summary: This document provides the API specification for terminating an active browser session using a unique session identifier.
tags:
    - api-reference
    - session-management
    - firecrawl
    - delete-request
    - authentication
category: api
---

HeaderValue`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Request Body

ParameterTypeRequiredDescription`id`stringYesThe session ID to destroy

## Response

FieldTypeDescription`success`booleanWhether the session was successfully destroyed

### Example Request

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### Example Response

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Browser session deleted successfully

Total session duration in milliseconds

Number of credits billed for the session