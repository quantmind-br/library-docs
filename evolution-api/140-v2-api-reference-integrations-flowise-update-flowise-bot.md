---
title: Update Flowise Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/update-flowise-bot
source: sitemap
fetched_at: 2026-04-12T18:49:07.65458479-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to send a POST request to update the configuration of a Flowise instance via an API endpoint.
tags:
    - api-call
    - http-request
    - flowise-update
    - json-data
    - rest-api
category: reference
---

```
curl --request POST \
  --url https://evolution-example/flowise/update/:flowiseId/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "apiUrl": "http://dify.site.com/v1",
  "triggerType": "keyword",
  "triggerOperator": "equals",
  "triggerValue": "teste",
  "apiKey": "app-123456",
  "expire": 0,
  "keywordFinish": "#SAIR",
  "delayMessage": 1000,
  "unknownMessage": "Mensagem não reconhecida",
  "listeningFromMe": false,
  "stopBotFromMe": false,
  "keepOpen": false,
  "debounceTime": 0,
  "ignoreJids": [
    "1234567890@s.whatsapp.net"
  ]
}
'
```