---
title: Set Dify Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/set-settings-dify
source: sitemap
fetched_at: 2026-04-12T18:49:33.632729903-03:00
rendered_js: false
word_count: 6
summary: This document provides a cURL command example demonstrating how to programmatically update the settings for a Dify bot instance via an API endpoint.
tags:
    - dify-settings
    - api-update
    - bot-configuration
    - curl-example
category: guide
---

Atualiza as configurações do bot Dify

```
curl --request POST \
  --url https://evolution-example/dify/settings/{instance} \
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
  "difyIdFallback": "clyja4oys0a3uqpy7k3bd7swe"
}
'
```