---
title: Get Batch Scrape Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/batch-scrape-get
source: sitemap
fetched_at: 2026-03-23T07:18:40.409502-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema structure for a web scraping or content extraction API response, detailing the fields available for retrieved page content and associated metadata.
tags:
    - api-schema
    - data-extraction
    - json-response
    - web-scraping
    - metadata-fields
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