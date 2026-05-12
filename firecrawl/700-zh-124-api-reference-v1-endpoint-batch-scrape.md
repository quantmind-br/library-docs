---
title: 批量抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:08:39.477005-03:00
rendered_js: false
word_count: 0
summary: This document provides the API request structure for initiating a batch web scraping operation using the Firecrawl v1 endpoint.
tags:
    - web-scraping
    - batch-processing
    - api-request
    - data-extraction
    - firecrawl-api
category: api
---

```
curl --request POST \
  --url https://api.firecrawl.dev/v1/batch/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "urls": [
    "<string>"
  ],
  "webhook": {
    "url": "<string>",
    "headers": {},
    "metadata": {},
    "events": [
      "completed"
    ]
  },
  "maxConcurrency": 123,
  "ignoreInvalidURLs": false,
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
  },
  "zeroDataRetention": false
}
'
```