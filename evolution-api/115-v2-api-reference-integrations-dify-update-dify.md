---
title: Update Dify Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/update-dify
source: sitemap
fetched_at: 2026-04-12T18:49:37.786223967-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to use an HTTP PUT request to update a specific instance within the Dify API.
tags:
    - curl
    - http-put
    - api-update
    - dify
    - rest-api
    - webhook
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/dify/update/:difyId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "botType": "chatBot",
  "apiUrl": "<string>",
  "apiKey": "<string>",
  "triggerType": "all",
  "triggerOperator": "contains",
  "triggerValue": "<string>",
  "expire": 123,
  "keywordFinish": "<string>",
  "delayMessage": 123,
  "unknownMessage": "<string>",
  "listeningFromMe": true,
  "stopBotFromMe": true,
  "keepOpen": true,
  "debounceTime": 123,
  "ignoreJids": [
    "<string>"
  ]
}
'
```