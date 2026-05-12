---
title: Historical Credit Usage - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:18:25.934449-03:00
rendered_js: false
word_count: 59
summary: This endpoint retrieves the historical credit consumption data for an authenticated team, providing a month-by-month breakdown of usage.
tags:
    - credit-usage
    - api-endpoint
    - billing-data
    - historical-metrics
    - auth-token
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
  --url https://api.firecrawl.dev/v1/team/credit-usage/historical \
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

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Query Parameters

Get historical credit usage by API key

#### Response