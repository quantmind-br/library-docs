---
title: クロールステータスを取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:12:25.808214-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a JSON response containing processed web content, including extracted text, HTML, and site metadata.
tags:
    - api-schema
    - data-extraction
    - json-response
    - web-scraping
    - metadata-structure
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