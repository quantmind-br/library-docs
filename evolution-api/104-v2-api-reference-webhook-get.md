---
title: Find Webhook - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/webhook/get
source: sitemap
fetched_at: 2026-04-12T18:46:59.564366751-03:00
rendered_js: false
word_count: 25
summary: This document demonstrates how to retrieve webhook details by making a GET request to the specified endpoint, showing the necessary authorization header and expected JSON response.
tags:
    - webhook
    - get-request
    - api-call
    - authorization
    - endpoint-reference
category: reference
---

```
curl --request GET \
  --url https://evolution-example/webhook/find/{instance} \
  --header 'apikey: <api-key>'

{
  "enabled": true,
  "url": "https://example.com",
  "events": [
    "APPLICATION_STARTUP"
  ]
}

curl --request GET \
  --url https://evolution-example/webhook/find/{instance} \
  --header 'apikey: <api-key>'

{
  "enabled": true,
  "url": "https://example.com",
  "events": [
    "APPLICATION_STARTUP"
  ]
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Indicates whether the webhook is enabled.

List of events the webhook is subscribed to.

[Set Webhook](https://doc.evolution-api.com/v2/api-reference/webhook/set)[Set Settings](https://doc.evolution-api.com/v2/api-reference/settings/set)