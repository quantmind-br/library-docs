---
title: Obtener el estado de la captura por lotes - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:18:12.757988-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure and schema for a data retrieval response, including usage metrics, status information, and structured metadata for individual records.
tags:
    - api-schema
    - json-response
    - data-structure
    - metadata-format
    - web-scraping
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
        "url": "<string>",
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