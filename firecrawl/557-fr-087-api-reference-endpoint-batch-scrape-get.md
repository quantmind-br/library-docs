---
title: Obtenir l’état d’une extraction par lot - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:16:01.597592-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure and schema for a data retrieval response, including usage metrics, status information, and extracted webpage content.
tags:
    - json-schema
    - data-structure
    - api-response
    - metadata-extraction
    - web-scraping
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