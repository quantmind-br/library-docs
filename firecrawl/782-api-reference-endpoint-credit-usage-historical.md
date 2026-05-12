---
title: Historical Credit Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:19:26.085201-03:00
rendered_js: false
word_count: 76
summary: This endpoint retrieves historical credit usage data for an authenticated team, providing a breakdown of consumption periods and optional analysis by API key.
tags:
    - api-reference
    - credit-usage
    - billing-analytics
    - authentication
    - historical-data
    - team-management
category: api
---

GET

/

team

/

credit-usage

/

historical

Get historical credit usage for the authenticated team

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalCredits": 1000
    }
  ]
}
```

Returns historical credit usage on a month-by-month basis. The endpoint can also breaks usage down by API key optionally.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

Get historical credit usage by API key

#### Response