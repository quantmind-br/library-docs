---
title: Obter status da raspagem em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:10:24.989715-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a JSON response containing paginated data processing results, including scraped content, metadata, and usage statistics.
tags:
    - json-schema
    - data-structure
    - api-response
    - web-scraping
    - metadata-extraction
category: reference
---

```
{
  "status": "<string>",
  "total": 123,
  "completed": 123,
  "creditsUsed": 123,
  "expiresAt": "2023-11-07T05:31:56Z",
  "next": "<string>",
  "data": [
    {
      "markdown": "<string>",
      "html": "<string>",
      "rawHtml": "<string>",
      "links": [
        "<string>"
      ],
      "screenshot": "<string>",
      "metadata": {
        "title": "<string>",
        "description": "<string>",
        "language": "<string>",
        "sourceURL": "<string>",
        "keywords": "<string>",
        "ogLocaleAlternate": [
          "<string>"
        ],
        "<any other metadata> ": "<string>",
        "statusCode": 123,
        "error": "<string>"
      }
    }
  ]
}
```