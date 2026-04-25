---
title: Find Websocket - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/websocket/find-websocket
source: sitemap
fetched_at: 2026-04-12T18:47:31.336200947-03:00
rendered_js: false
word_count: 38
summary: This document details the API endpoint used to find a specific Websocket instance, providing the necessary GET request structure and required parameters.
tags:
    - websocket
    - find
    - api-endpoint
    - get-request
    - instance
    - api-key
category: reference
---

Find Websocket

```
curl --request GET \
  --url https://evolution-example/websocket/find/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

websocket

/

find

/

{instance}

Find Websocket

```
curl --request GET \
  --url https://evolution-example/websocket/find/{instance} \
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

[Set Websocket](https://doc.evolution-api.com/v2/api-reference/integrations/websocket/set-websocket)[Set SQS](https://doc.evolution-api.com/v2/api-reference/integrations/sqs/set-sqs)