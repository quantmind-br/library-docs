---
title: Find Dify Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-bot-dify
source: sitemap
fetched_at: 2026-04-12T18:49:47.543538616-03:00
rendered_js: false
word_count: 69
summary: This document provides the technical reference for interacting with the Evolution API to specifically find a Dify bot using a GET request, detailing required parameters and expected responses.
tags:
    - api-reference
    - dify-bot
    - get-request
    - authorization
    - parameters
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/find/:difyId/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "OK"
}
```

GET

/

dify

/

find

/

:difyId

/

{instance}

Find Bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/find/:difyId/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "OK"
}
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

[​](#parameter-dify-id)

difyId

string

required

ID of the dify bot

#### Response

200 - application/json

Successfully fetched sessions

[​](#response-message)

message

string

Example:

`"OK"`

[Find Dify Bots](https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-dify)[Update Dify Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/update-dify)