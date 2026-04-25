---
title: Create Evolution Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/create-bot
source: sitemap
fetched_at: 2026-04-12T18:49:21.502542467-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to make a POST request to create an instance of an evolution bot.
tags:
    - curl
    - post-request
    - api-call
    - bot-creation
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/evolutionBot/create/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "apiUrl": "<string>",
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
  "apiKey": "<string>",
  "ignoreJids": [
    "<string>"
  ]
}
'
```