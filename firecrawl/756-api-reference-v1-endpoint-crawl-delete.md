---
title: Cancel Crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:18:48.155549-03:00
rendered_js: false
word_count: 37
summary: This document provides the API endpoint and authentication requirements for cancelling an active crawl job using a DELETE request.
tags:
    - api-reference
    - crawl-service
    - bearer-authentication
    - delete-endpoint
    - job-management
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/crawl-delete) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

#### Response

Available options:

`cancelled`