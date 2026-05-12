---
title: Obter status do scrape em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:11:50.869601-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for an API response containing paginated web content, including processed markup, extracted metadata, and usage statistics.
tags:
    - api-response
    - json-schema
    - web-scraping
    - data-model
    - metadata-extraction
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