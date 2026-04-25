---
title: Set SQS - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/sqs/set-sqs
source: sitemap
fetched_at: 2026-04-12T18:48:05.710650093-03:00
rendered_js: false
word_count: 12
summary: This document provides an example cURL request demonstrating how to use the API endpoint to enable SQS and specify application startup events for a given instance.
tags:
    - curl
    - api-call
    - sqs-integration
    - endpoint-usage
    - application-config
category: reference
---

```
curl --request POST \
  --url https://evolution-example/sqs/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "sqs": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  }
}
'

This response has no body data.

curl --request POST \
  --url https://evolution-example/sqs/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "sqs": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  }
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Find Websocket](https://doc.evolution-api.com/v2/api-reference/integrations/websocket/find-websocket)[Find SQS](https://doc.evolution-api.com/v2/api-reference/integrations/sqs/find-sqs)