---
title: Fetch Evolution Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/fetch-bots
source: sitemap
fetched_at: 2026-04-12T18:49:14.122646118-03:00
rendered_js: false
word_count: 69
summary: This page serves as documentation for the Evolution API, providing endpoints and details on how to fetch information for a specific bot instance using cURL examples.
tags:
    - api-documentation
    - rest-api
    - curl-example
    - bot-management
    - authorization
    - get-information
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Bot Evo

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetch/:evolutionBotId/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "OK"
}
```

GET

/

evolutionBot

/

fetch

/

:evolutionBotId

/

{instance}

Find Bot Evo

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetch/:evolutionBotId/{instance} \
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

[​](#parameter-evolution-bot-id)

evolutionBotId

string

required

ID of the evo bot

#### Response

200 - application/json

Successfully fetched sessions

[​](#response-message)

message

string

Example:

`"OK"`

[Find Evolution Bots](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/find-bot)[Update Evolution Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/update)