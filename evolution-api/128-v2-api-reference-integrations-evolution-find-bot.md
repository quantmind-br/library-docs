---
title: Find Evolution Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/find-bot
source: sitemap
fetched_at: 2026-04-12T18:49:27.763995857-03:00
rendered_js: false
word_count: 58
summary: This document serves as the home page documentation for the Evolution API, providing access points to general guides and specific reference endpoints like finding a bot instance.
tags:
    - evolution-api
    - api-reference
    - documentation
    - get-started
    - bot-management
category: guide
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Bots Evo

```
curl --request GET \
  --url https://evolution-example/evolutionBot/find/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "OK"
}
```

GET

/

evolutionBot

/

find

/

{instance}

Find Bots Evo

```
curl --request GET \
  --url https://evolution-example/evolutionBot/find/{instance} \
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

[Create Evolution Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/create-bot)[Fetch Evolution Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/fetch-bots)