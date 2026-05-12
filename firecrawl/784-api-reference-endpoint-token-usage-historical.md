---
title: Historical Token Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:19:42.930281-03:00
rendered_js: false
word_count: 109
summary: This endpoint retrieves historical token consumption data for an authenticated team, organized by time periods and optionally broken down by API key.
tags:
    - api-endpoint
    - token-usage
    - billing-metrics
    - historical-data
    - firecrawl-api
category: api
---

GET

/

team

/

token-usage

/

historical

Get historical token usage for the authenticated team (Extract only)

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalTokens": 1000
    }
  ]
}
```

Returns historical token usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.

We’ve simplified billing so that Extract now uses credits, just like all of the other endpoints. Each credit is worth 15 tokens. Reported token usage now includes usage from all endpoints.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

Get historical token usage by API key

#### Response