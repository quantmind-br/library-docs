---
title: Find SQS - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/sqs/find-sqs
source: sitemap
fetched_at: 2026-04-12T18:48:01.769284655-03:00
rendered_js: false
word_count: 38
summary: This document details the endpoint and method for finding an Amazon SQS instance using a GET request, specifying required authorization headers and path parameters.
tags:
    - sqs
    - aws-messaging
    - get-request
    - api-endpoint
    - instance
category: reference
---

Find SQS

```
curl --request GET \
  --url https://evolution-example/sqs/find/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

sqs

/

find

/

{instance}

Find SQS

```
curl --request GET \
  --url https://evolution-example/sqs/find/{instance} \
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

[Set SQS](https://doc.evolution-api.com/v2/api-reference/integrations/sqs/set-sqs)[Set RabbitMQ](https://doc.evolution-api.com/v2/api-reference/integrations/rabbitmq/set-rabbitmq)