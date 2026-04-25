---
title: Set Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/settings/set
source: sitemap
fetched_at: 2026-04-12T18:46:53.964053098-03:00
rendered_js: false
word_count: 35
summary: This document provides examples and structural guidance on how to use a POST request via cURL to set various user settings on an EvolutionAPI instance.
tags:
    - rest-api
    - http-request
    - set-settings
    - api-endpoint
    - json-payload
    - curl-example
category: reference
---

```
curl --request POST \
  --url https://evolution-example/settings/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "rejectCall": true,
  "msgCall": "<string>",
  "groupsIgnore": true,
  "alwaysOnline": true,
  "readMessages": true,
  "readStatus": true,
  "syncFullHistory": true
}
'

{
  "settings": {
    "instanceName": "teste-docs",
    "settings": {
      "reject_call": true,
      "groups_ignore": true,
      "always_online": true,
      "read_messages": true,
      "read_status": true,
      "sync_full_history": false
    }
  }
}

curl --request POST \
  --url https://evolution-example/settings/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "rejectCall": true,
  "msgCall": "<string>",
  "groupsIgnore": true,
  "alwaysOnline": true,
  "readMessages": true,
  "readStatus": true,
  "syncFullHistory": true
}
'

{
  "settings": {
    "instanceName": "teste-docs",
    "settings": {
      "reject_call": true,
      "groups_ignore": true,
      "always_online": true,
      "read_messages": true,
      "read_status": true,
      "sync_full_history": false
    }
  }
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Reject calls automatically

Message to be sent when a call is rejected automatically

Always show WhatsApp online

Syncronize full WhatsApp history with EvolutionAPI

#### Response

[Find Webhook](https://doc.evolution-api.com/v2/api-reference/webhook/get)[Find Settings](https://doc.evolution-api.com/v2/api-reference/settings/get)