---
title: Create Dify Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/create-dify
source: sitemap
fetched_at: 2026-04-12T18:49:57.637454165-03:00
rendered_js: false
word_count: 0
summary: This document provides a command-line example using cURL to make a POST request to create an instance via an API endpoint.
tags:
    - curl
    - post-request
    - api-call
    - json-data
    - dify
category: reference
---

```
curl --request POST \
  --url https://evolution-example/dify/create/{instance} \
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