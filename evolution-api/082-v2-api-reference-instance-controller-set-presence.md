---
title: Set Presence - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/set-presence
source: sitemap
fetched_at: 2026-04-12T18:50:04.356808228-03:00
rendered_js: false
word_count: 29
summary: This document provides details on how to use the API endpoint to set the presence status for a specific instance, including required headers and body parameters.
tags:
    - api-call
    - http-method
    - instance-management
    - presence-status
    - curl-example
category: reference
---

```
curl --request POST \
  --url https://evolution-example/instance/setPresence/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "presence": "available"
}
'

This response has no body data.
```

POST

/

instance

/

setPresence

/

{instance}

```
curl --request POST \
  --url https://evolution-example/instance/setPresence/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "presence": "available"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to connect

#### Body

Available options:

`available`,

`unavailable`

#### Response

[Delete Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/delete-instance)[Set Webhook](https://doc.evolution-api.com/v2/api-reference/webhook/set)