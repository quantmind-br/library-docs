---
title: 抽出 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/extract
source: sitemap
fetched_at: 2026-03-23T07:12:12.229204-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure for the Firecrawl extract endpoint, detailing the parameters available for web scraping, data extraction, and content parsing.
tags:
    - api-request
    - data-extraction
    - web-scraping
    - json-schema
    - firecrawl-api
    - scrape-options
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/extract \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "urls": [
    "<string>"
  ],
  "prompt": "<string>",
  "schema": {},
  "enableWebSearch": false,
  "ignoreSitemap": false,
  "includeSubdomains": true,
  "showSources": false,
  "scrapeOptions": {
    "onlyMainContent": true,
    "includeTags": [
      "<string>"
    ],
    "excludeTags": [
      "<string>"
    ],
    "maxAge": 0,
    "headers": {},
    "waitFor": 0,
    "mobile": false,
    "skipTlsVerification": false,
    "timeout": 30000,
    "parsePDF": true,
    "jsonOptions": {
      "schema": {},
      "systemPrompt": "<string>",
      "prompt": "<string>"
    },
    "actions": [
      {
        "type": "wait",
        "milliseconds": 2,
        "selector": "#my-element"
      }
    ],
    "location": {
      "country": "US",
      "languages": [
        "en-US"
      ]
    },
    "removeBase64Images": true,
    "blockAds": true,
    "proxy": "basic",
    "storeInCache": true,
    "formats": [
      "markdown"
    ],
    "changeTrackingOptions": {
      "modes": [
        "git-diff"
      ],
      "schema": {},
      "prompt": "<string>",
      "tag": null
    }
  },
  "ignoreInvalidURLs": false
}
'
```