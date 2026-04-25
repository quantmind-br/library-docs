---
title: Set Settings Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/set-settings
source: sitemap
fetched_at: 2026-04-12T18:49:09.593365388-03:00
rendered_js: false
word_count: 4
summary: This document provides a cURL example demonstrating how to programmatically set the configuration options for an Evolution Bot instance via a POST request.
tags:
    - evolution-bot
    - settings
    - api-call
    - webhook-configuration
    - curl-example
category: api
---

Create Evolution Bot Settings

```
curl --request POST \
  --url https://evolution-example/evolutionBot/settings/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "expire": 123,
  "keywordFinish": "<string>",
  "delayMessage": 123,
  "unknownMessage": "<string>",
  "listeningFromMe": true,
  "stopBotFromMe": true,
  "keepOpen": true,
  "debounceTime": 123,
  "botIdFallback": "<string>",
  "ignoreJids": [
    "<string>"
  ]
}
'
```