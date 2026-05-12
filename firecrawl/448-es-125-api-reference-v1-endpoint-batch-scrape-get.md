---
title: Obtener el estado de Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:16:38.94776-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for an API response containing web page content, usage statistics, and extracted document metadata.
tags:
    - api-response
    - json-schema
    - web-scraping
    - metadata-extraction
    - data-format
category: api
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