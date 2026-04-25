---
title: Update Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/update-bot
source: sitemap
fetched_at: 2026-04-12T18:48:13.499445883-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to update an OpenAI bot configuration via a PUT request using the cURL command-line tool. It shows the structure and required headers for updating various settings of an existing bot instance.
tags:
    - curl
    - put-request
    - openai-bot
    - api-update
    - http-headers
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/openai/update/:openaiBotId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "openaiCredsId": "<string>",
  "botType": "assistant",
  "model": "<string>",
  "assistantId": "<string>",
  "functionUrl": "<string>",
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
  "triggerType": "all",
  "triggerOperator": "equals",
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