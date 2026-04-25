---
title: Set EvoAI Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/set-settings-evoai
source: sitemap
fetched_at: 2026-04-12T18:49:24.343746223-03:00
rendered_js: false
word_count: 6
summary: This document provides a cURL example demonstrating how to update the settings for an EvoAI bot instance via a POST request.
tags:
    - api-settings
    - bot-configuration
    - curl-example
    - webhook-update
category: guide
---

Atualiza as configurações do bot EvoAI

```
curl --request POST \
  --url https://evolution-example/evoai/settings/{instance} \
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
  "evoaiIdFallback": "clyja4oys0a3uqpy7k3bd7swe"
}
'
```