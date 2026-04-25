---
title: Create Flowise Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/create-bot
source: sitemap
fetched_at: 2026-04-12T18:49:04.195468681-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to make a POST request to create an instance resource via the evolution-example API endpoint.
tags:
    - curl
    - post-request
    - api-call
    - json-data
    - instance-creation
category: reference
---

```
curl --request POST \
  --url https://evolution-example/flowise/create/{instance} \
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