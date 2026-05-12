---
title: Cancel Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:18:46.073084-03:00
rendered_js: false
word_count: 57
summary: This document provides the API endpoint and authentication requirements for cancelling a pending or active batch scrape job.
tags:
    - api-reference
    - batch-scraping
    - job-cancellation
    - rest-api
    - web-scraping
category: api
---

Cancel a batch scrape job

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancel a batch scrape job

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/batch-scrape-delete) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the batch scrape job

#### Response

Example:

`"Batch scrape job successfully cancelled."`