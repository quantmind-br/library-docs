---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:07:58.266813-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure for the Firecrawl map endpoint, detailing the required headers and configurable parameters for crawling web resources.
tags:
    - api-reference
    - web-scraping
    - http-post
    - data-crawling
    - firecrawl-api
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/map \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "url": "<string>",
  "search": "<string>",
  "ignoreSitemap": true,
  "sitemapOnly": false,
  "includeSubdomains": true,
  "limit": 5000,
  "timeout": 123,
  "location": {
    "country": "US",
    "languages": [
      "en-US"
    ]
  }
}
'
```