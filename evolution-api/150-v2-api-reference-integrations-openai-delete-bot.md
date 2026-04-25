---
title: Delete OpenIA Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/delete-bot
source: sitemap
fetched_at: 2026-04-12T18:48:29.630804495-03:00
rendered_js: false
word_count: 59
summary: This documentation provides the reference details and usage example for deleting an OpenAI Bot via a specific API endpoint. It outlines required headers, path parameters, and expected response information.
tags:
    - api-reference
    - delete-endpoint
    - openai-bot
    - authorization
    - curl-example
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Delete OpenAI Bot

```
curl --request DELETE \
  --url https://evolution-example/openai/delete/:openaiBotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

DELETE

/

openai

/

delete

/

:openaiBotId

/

{instance}

Delete OpenAI Bot

```
curl --request DELETE \
  --url https://evolution-example/openai/delete/:openaiBotId/{instance} \
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

[​](#parameter-openai-bot-id)

openaiBotId

string

required

ID of the bot

#### Response

200 - undefined

[Update Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/update-bot)[Find OpenIA Creds](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-creds-openai)