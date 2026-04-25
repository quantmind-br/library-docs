---
title: Settings Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/settings-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:46.431379743-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to use an HTTP POST request to update the settings of a typebot instance via an API endpoint.
tags:
    - curl-command
    - api-settings
    - post-request
    - http-endpoint
    - typebot
category: reference
---

```
curl --request POST \
  --url https://evolution-example/typebot/settings/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "expire": "<string>",
  "keywordFinish": "<string>",
  "delayMessage": "<string>",
  "unknownMessage": "<string>",
  "listeningFromMe": "<string>",
  "stopBotFromMe": "<string>",
  "keepOpen": "<string>",
  "debounceTime": "<string>",
  "ignoreJids": "<string>",
  "typebotIdFallback": "<string>"
}
'
```