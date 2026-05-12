---
title: Obtenir le statut d’un batch scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:14:31.802214-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a JSON response containing processed web content, including markdown, HTML, and extracted site metadata.
tags:
    - json-schema
    - web-scraping
    - api-response
    - data-extraction
    - content-metadata
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