---
title: スクレイプ - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/scrape
source: sitemap
fetched_at: 2026-03-23T07:12:54.553508-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for a standardized web scraping and data extraction API response, including metadata, branding details, and change tracking information.
tags:
    - api-schema
    - web-scraping
    - data-extraction
    - json-structure
    - metadata-format
category: api
---

```
{
  "success": true,
  "data": {
    "markdown": "<string>",
    "summary": "<string>",
    "html": "<string>",
    "rawHtml": "<string>",
    "screenshot": "<string>",
    "links": [
      "<string>"
    ],
    "actions": {
      "screenshots": [
        "<string>"
      ],
      "scrapes": [
        {
          "url": "<string>",
          "html": "<string>"
        }
      ],
      "javascriptReturns": [
        {
          "type": "<string>",
          "value": "<unknown>"
        }
      ],
      "pdfs": [
        "<string>"
      ]
    },
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
    },
    "warning": "<string>",
    "changeTracking": {
      "previousScrapeAt": "2023-11-07T05:31:56Z",
      "changeStatus": "new",
      "visibility": "visible",
      "diff": "<string>",
      "json": {}
    },
    "branding": {
      "colorScheme": "light",
      "logo": "<string>",
      "colors": {
        "primary": "<string>",
        "secondary": "<string>",
        "accent": "<string>",
        "background": "<string>",
        "textPrimary": "<string>",
        "textSecondary": "<string>",
        "link": "<string>",
        "success": "<string>",
        "warning": "<string>",
        "error": "<string>"
      },
      "fonts": [
        {
          "family": "<string>"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "<string>",
          "heading": "<string>",
          "code": "<string>"
        },
        "fontSizes": {
          "h1": "<string>",
          "h2": "<string>",
          "h3": "<string>",
          "body": "<string>"
        },
        "fontWeights": {
          "light": 123,
          "regular": 123,
          "medium": 123,
          "bold": 123
        },
        "lineHeights": {
          "heading": "<string>",
          "body": "<string>"
        }
      },
      "spacing": {
        "baseUnit": 123,
        "borderRadius": "<string>",
        "padding": {},
        "margins": {}
      },
      "components": {
        "buttonPrimary": {
          "background": "<string>",
          "textColor": "<string>",
          "borderRadius": "<string>"
        },
        "buttonSecondary": {
          "background": "<string>",
          "textColor": "<string>",
          "borderColor": "<string>",
          "borderRadius": "<string>"
        },
        "input": {}
      },
      "icons": {},
      "images": {
        "logo": "<string>",
        "favicon": "<string>",
        "ogImage": "<string>"
      },
      "animations": {},
      "layout": {},
      "personality": {}
    }
  }
}
```