---
title: Set Websocket - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/websocket/set-websocket
source: sitemap
fetched_at: 2026-04-12T18:47:39.609646828-03:00
rendered_js: false
word_count: 19
summary: This document demonstrates how to use a cURL command to make a POST request to set websocket configurations for a specified instance.
tags:
    - curl
    - websocket
    - post
    - api-call
    - websockets
    - configuration
category: reference
---

```
curl --request POST \
  --url https://evolution-example/websocket/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "websocket": {
    "enabled": true,
    "events": [
      "APPLICATION_STARTUP"
    ]
  }
}
'

This response has no body data.
```

POST

/

websocket

/

set

/

{instance}

```
curl --request POST \
  --url https://evolution-example/websocket/set/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "websocket": {
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

[Find Chatwoot](https://doc.evolution-api.com/v2/api-reference/integrations/chatwoot/find-chatwoot)[Find Websocket](https://doc.evolution-api.com/v2/api-reference/integrations/websocket/find-websocket)