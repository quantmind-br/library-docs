---
title: Historical Token Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:18:10.319464-03:00
rendered_js: false
word_count: 61
summary: This endpoint retrieves historical token consumption data for an authenticated team, providing usage metrics broken down by time period and optionally by individual API keys.
tags:
    - api-endpoint
    - token-usage
    - historical-data
    - team-analytics
    - authentication
    - usage-tracking
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
  --url https://api.firecrawl.dev/v1/team/token-usage/historical \
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

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

Get historical token usage by API key

#### Response