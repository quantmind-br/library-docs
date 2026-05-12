---
title: Cancel Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:19:52.175461-03:00
rendered_js: false
word_count: 58
summary: This document provides instructions on how to cancel a previously initiated batch scraping job using the Firecrawl API.
tags:
    - api-reference
    - batch-scraping
    - job-cancellation
    - rest-api
category: api
---

Cancel a batch scrape job

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancel a batch scrape job

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the batch scrape job

#### Response

Example:

`"Batch scrape job successfully cancelled."`