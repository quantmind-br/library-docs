---
title: Cancel Crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:19:44.986237-03:00
rendered_js: false
word_count: 38
summary: This document provides the API endpoint and authentication details for cancelling a specific crawl job using the Firecrawl service.
tags:
    - api-endpoint
    - firecrawl
    - data-scraping
    - http-delete
    - bearer-authentication
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Available options:

`cancelled`