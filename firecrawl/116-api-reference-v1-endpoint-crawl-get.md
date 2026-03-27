---
title: Get Crawl Status - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:18:56.09771-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a JSON response containing processed web content, including markdown, HTML, and extracted page metadata.
tags:
    - json-schema
    - data-structure
    - web-scraping
    - api-response
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