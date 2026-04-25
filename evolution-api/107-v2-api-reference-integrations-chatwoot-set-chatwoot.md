---
title: Set Chatwoot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/chatwoot/set-chatwoot
source: sitemap
fetched_at: 2026-04-12T18:49:49.679771802-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL command example demonstrating how to make a POST request to an endpoint for configuring settings within the Chatwoot platform.
tags:
    - curl
    - api-request
    - post-method
    - configuration
    - chatwoot-api
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chatwoot/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "enabled": true,
  "accountId": "<string>",
  "token": "<string>",
  "url": "<string>",
  "signMsg": true,
  "reopenConversation": true,
  "conversationPending": true,
  "nameInbox": "<string>",
  "mergeBrazilContacts": true,
  "importContacts": true,
  "importMessages": true,
  "daysLimitImportMessages": 123,
  "signDelimiter": "<string>",
  "autoCreate": true,
  "organization": "<string>",
  "logo": "<string>",
  "ignoreJids": [
    "<string>"
  ]
}
'
```