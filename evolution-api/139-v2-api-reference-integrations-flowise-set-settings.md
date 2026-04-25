---
title: Set Settings Flowise Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/set-settings
source: sitemap
fetched_at: 2026-04-12T18:48:53.421389042-03:00
rendered_js: false
word_count: 5
summary: This document provides a cURL example demonstrating how to update the configuration settings for an instance of Flowise via a POST request.
tags:
    - flowise-settings
    - api-configuration
    - curl-example
    - post-request
    - instance-update
category: reference
---

Set as configurações do Flowise

```
curl --request POST \
  --url https://evolution-example/flowise/settings/{instance} \
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
  "flowiseIdFallback": "clyja4oys0a3uqpy7k3bd7swe"
}
'
```