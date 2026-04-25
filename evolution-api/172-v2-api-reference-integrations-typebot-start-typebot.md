---
title: Start Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/start-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:33.61382472-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to initiate an interaction with the Typebot service via a POST request.
tags:
    - curl
    - api-call
    - http-request
    - typebot
    - post
    - json
category: reference
---

```
curl --request POST \
  --url https://evolution-example/typebot/start/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "url": "<string>",
  "typebot": "<string>",
  "remoteJid": "<string>",
  "startSession": true,
  "variables": [
    {
      "name": "<string>",
      "value": "<string>"
    }
  ]
}
'
```