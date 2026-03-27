---
title: Extraer - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/extract
source: sitemap
fetched_at: 2026-03-23T07:17:22.889056-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure and parameters for the Firecrawl extraction endpoint, used to scrape and process web content based on specific schemas.
tags:
    - web-scraping
    - data-extraction
    - api-endpoint
    - json-schema
    - firecrawl-api
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v2/extract \
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
    "formats": [
      "markdown"
    ],
    "onlyMainContent": true,
    "includeTags": [
      "<string>"
    ],
    "excludeTags": [
      "<string>"
    ],
    "maxAge": 172800000,
    "minAge": 123,
    "headers": {},
    "waitFor": 0,
    "mobile": false,
    "skipTlsVerification": true,
    "timeout": 30000,
    "parsers": [
      "pdf"
    ],
    "actions": [
      {
        "type": "wait",
        "milliseconds": 2
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
    "proxy": "auto",
    "storeInCache": true
  },
  "ignoreInvalidURLs": true
}
'
```