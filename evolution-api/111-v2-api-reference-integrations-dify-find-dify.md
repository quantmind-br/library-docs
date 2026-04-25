---
title: Find Dify Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-dify
source: sitemap
fetched_at: 2026-04-12T18:49:51.533036628-03:00
rendered_js: false
word_count: 58
summary: This documentation provides reference material for using the Evolution API, specifically detailing how to find a Dify Bot instance via a GET request. It covers necessary components like authentication headers and path parameters.
tags:
    - evolution-api
    - dify-bot
    - get-request
    - api-reference
    - authorization
    - integration
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Fetch Bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/find/{instance} \
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

{instance}

Fetch Bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/find/{instance} \
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

#### Response

200 - application/json

Successfully fetched sessions

[​](#response-message)

message

string

Example:

`"OK"`

[Create Dify Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/create-dify)[Find Dify Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-bot-dify)