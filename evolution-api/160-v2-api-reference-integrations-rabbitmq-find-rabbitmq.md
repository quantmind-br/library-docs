---
title: Find RabbitMQ - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/rabbitmq/find-rabbitmq
source: sitemap
fetched_at: 2026-04-12T18:48:09.464942677-03:00
rendered_js: false
word_count: 37
summary: This document details how to use the GET endpoint to find a specific RabbitMQ instance using its identifier.
tags:
    - rabbitmq
    - find-instance
    - api-endpoint
    - rest-api
    - get-request
category: reference
---

Find RabbitMQ

```
curl --request GET \
  --url https://evolution-example/rabbitmq/find/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

rabbitmq

/

find

/

{instance}

Find RabbitMQ

```
curl --request GET \
  --url https://evolution-example/rabbitmq/find/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

#### Authorizations

[​](#authorization-apikey)

apikey

string

header

required

Your authorization key header

#### Path Parameters

[​](#parameter-instance)

instance

string

required

Name of the instance

#### Response

200 - undefined

[Set RabbitMQ](https://doc.evolution-api.com/v2/api-reference/integrations/rabbitmq/set-rabbitmq)