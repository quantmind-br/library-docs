---
title: Obter status do crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:11:46.086662-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure and schema for a data retrieval response, including request status, usage credits, and parsed web content metadata.
tags:
    - api-schema
    - json-structure
    - data-response
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