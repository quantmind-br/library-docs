---
title: Create Instance - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/create-instance-basic
source: sitemap
fetched_at: 2026-04-12T18:46:50.380701173-03:00
rendered_js: false
word_count: 0
summary: This document provides a cURL example demonstrating how to use an HTTP POST request to create a new instance via an API endpoint.
tags:
    - api-call
    - post-request
    - instance-creation
    - curl-example
    - webhook-setup
category: reference
---

```
curl --request POST \
  --url https://evolution-example/instance/create \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "instanceName": "<string>",
  "integration": "WHATSAPP-BAILEYS",
  "token": "<string>",
  "qrcode": true,
  "number": "<string>",
  "rejectCall": true,
  "msgCall": "<string>",
  "groupsIgnore": true,
  "alwaysOnline": true,
  "readMessages": true,
  "readStatus": true,
  "syncFullHistory": true,
  "proxyHost": "<string>",
  "proxyPort": "<string>",
  "proxyProtocol": "<string>",
  "proxyUsername": "<string>",
  "proxyPassword": "<string>",
  "webhook": {
    "url": "<string>",
    "byEvents": true,
    "base64": true,
    "headers": {
      "authorization": "<string>",
      "Content-Type": "<string>"
    },
    "events": [
      "APPLICATION_STARTUP"
    ]
  },
  "rabbitmq": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  },
  "sqs": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  },
  "chatwootAccountId": 123,
  "chatwootToken": "<string>",
  "chatwootUrl": "<string>",
  "chatwootSignMsg": true,
  "chatwootReopenConversation": true,
  "chatwootConversationPending": true,
  "chatwootImportContacts": true,
  "chatwootNameInbox": "<string>",
  "chatwootMergeBrazilContacts": true,
  "chatwootImportMessages": true,
  "chatwootDaysLimitImportMessages": 123,
  "chatwootOrganization": "<string>",
  "chatwootLogo": "<string>"
}
'
```