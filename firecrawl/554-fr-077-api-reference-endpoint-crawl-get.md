---
title: Obtenir l’état d’un crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:15:33.555334-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for an API response, detailing the fields for request status, usage credits, and a collection of processed webpage data including content formats and metadata.
tags:
    - api-schema
    - json-structure
    - web-scraping
    - response-format
    - data-extraction
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