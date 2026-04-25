---
title: Set RabbitMQ - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/rabbitmq/set-rabbitmq
source: sitemap
fetched_at: 2026-04-12T18:48:06.186797595-03:00
rendered_js: false
word_count: 12
summary: This document provides an example using curl to demonstrate how to programmatically enable RabbitMQ integration and specify application startup events via a POST request.
tags:
    - curl
    - rabbitmq
    - api-call
    - post-request
    - configuration
    - integration
category: reference
---

```
curl --request POST \
  --url https://evolution-example/rabbitmq/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "rabbitmq": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  }
}
'

This response has no body data.

curl --request POST \
  --url https://evolution-example/rabbitmq/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "rabbitmq": {
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

[Find SQS](https://doc.evolution-api.com/v2/api-reference/integrations/sqs/find-sqs)[Find RabbitMQ](https://doc.evolution-api.com/v2/api-reference/integrations/rabbitmq/find-rabbitmq)