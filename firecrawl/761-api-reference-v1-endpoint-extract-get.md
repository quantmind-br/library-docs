---
title: Get Extract Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:18:33.00943-03:00
rendered_js: false
word_count: 67
summary: This document describes the API endpoint used to retrieve the current processing status and details of a specific data extraction job.
tags:
    - api-endpoint
    - job-status
    - data-extraction
    - firecrawl-api
    - http-get
category: api
---

Get the status of an extract job

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

Get the status of an extract job

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/extract-get) is now available with improved features and performance.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

The ID of the extract job

#### Response

The current status of the extract job

Available options:

`completed`,

`processing`,

`failed`,

`cancelled`