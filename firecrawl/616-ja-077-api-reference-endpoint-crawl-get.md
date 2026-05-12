---
title: クロールのステータスを取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-get
source: sitemap
fetched_at: 2026-03-23T07:13:26.831462-03:00
rendered_js: false
word_count: 0
summary: This document defines the JSON structure for an API response containing paginated web content, including parsed markdown, HTML, and site metadata.
tags:
    - api-response
    - json-schema
    - web-scraping
    - data-extraction
    - metadata-format
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