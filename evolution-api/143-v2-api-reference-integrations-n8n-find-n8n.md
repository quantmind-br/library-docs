---
title: Find n8n Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/find-n8n
source: sitemap
fetched_at: 2026-04-12T18:48:41.571903425-03:00
rendered_js: false
word_count: 58
summary: This page serves as the home documentation for the Evolution API, providing links to get started guides and specific API references for functionalities like fetching information about an n8n bot.
tags:
    - api
    - documentation
    - n8n-integration
    - get-started
    - rest-api
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Fetch n8n Bot

```
curl --request GET \
  --url https://evolution-example/n8n/find/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "OK"
}
```

GET

/

n8n

/

find

/

{instance}

Fetch n8n Bot

```
curl --request GET \
  --url https://evolution-example/n8n/find/{instance} \
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

[Create n8n Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/create-n8n)[Update n8n Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/update-n8n)