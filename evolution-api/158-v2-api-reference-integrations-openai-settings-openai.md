---
title: Settigns config OpenAI - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/settings-openai
source: sitemap
fetched_at: 2026-04-12T18:48:11.53409467-03:00
rendered_js: false
word_count: 0
summary: This document provides a command-line example demonstrating how to send a POST request to update settings for an OpenAI instance using cURL.
tags:
    - curl
    - post-request
    - api-call
    - openai-settings
    - http-headers
    - json-data
category: reference
---

```
curl --request POST \
  --url https://evolution-example/openai/settings/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "openaiCredsId": "<string>",
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
  ],
  "openaiIdFallback": "<string>"
}
'
```