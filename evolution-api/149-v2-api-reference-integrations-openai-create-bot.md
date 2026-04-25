---
title: Create OpenIA Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/create-bot
source: sitemap
fetched_at: 2026-04-12T18:48:47.736991638-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to make a POST request to create an instance via an API endpoint.
tags:
    - api-call
    - openai-integration
    - post-request
    - json-data
    - endpoint-example
category: api
---

```
curl --request POST \
  --url https://evolution-example/openai/create/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "openaiCredsId": "<string>",
  "botType": "<string>",
  "assistantId": "<string>",
  "functionUrl": "<string>",
  "model": "<string>",
  "systemMessages": [
    "<string>"
  ],
  "assistantMessages": [
    "<string>"
  ],
  "userMessages": [
    "<string>"
  ],
  "maxTokens": 123,
  "triggerType": "<string>",
  "triggerOperator": "<string>",
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