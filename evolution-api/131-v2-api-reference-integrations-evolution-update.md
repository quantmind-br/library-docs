---
title: Update Evolution Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/update
source: sitemap
fetched_at: 2026-04-12T18:48:57.736963292-03:00
rendered_js: false
word_count: 0
summary: This document provides a command-line example using cURL to demonstrate how to send a PUT request to an endpoint for updating the configuration of an evolution bot.
tags:
    - curl
    - put-request
    - api-call
    - bot-update
    - json-data
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/evolutionBot/update/:evolutionBotId/{instance} \
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