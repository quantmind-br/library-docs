---
title: Set n8n Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/set-settings-n8n
source: sitemap
fetched_at: 2026-04-12T18:48:33.596330517-03:00
rendered_js: false
word_count: 6
summary: This document provides a cURL example demonstrating how to update the configuration settings of an n8n bot via a POST request.
tags:
    - n8n
    - bot-settings
    - api-call
    - curl-example
    - configuration
category: reference
---

Atualiza as configurações do bot n8n

```
curl --request POST \
  --url https://evolution-example/n8n/settings/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "expire": 20,
  "keywordFinish": "#SAIR",
  "delayMessage": 1000,
  "unknownMessage": "Mensagem não reconhecida",
  "listeningFromMe": false,
  "stopBotFromMe": false,
  "keepOpen": false,
  "debounceTime": 0,
  "ignoreJids": [],
  "n8nIdFallback": "clyja4oys0a3uqpy7k3bd7swe"
}
'
```