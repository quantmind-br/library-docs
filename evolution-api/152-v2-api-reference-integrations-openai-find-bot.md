---
title: Find OpenIA Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-bot
source: sitemap
fetched_at: 2026-04-12T18:48:16.639081441-03:00
rendered_js: false
word_count: 60
summary: This page serves as the main documentation hub for the Evolution API, providing access to guides, references, and specific endpoint details like finding an OpenAI Bot.
tags:
    - evolution-api
    - documentation
    - openai-integration
    - api-reference
    - getting-started
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find OpenAI Bot

```
curl --request GET \
  --url https://evolution-example/openai/find/:openaiBotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

openai

/

find

/

:openaiBotId

/

{instance}

Find OpenAI Bot

```
curl --request GET \
  --url https://evolution-example/openai/find/:openaiBotId/{instance} \
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

[Create OpenIA Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/create-bot)[Find OpenIA Bots](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-bots)