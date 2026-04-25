---
title: Delete OpenIA Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/delete-creds
source: sitemap
fetched_at: 2026-04-12T18:48:23.556135017-03:00
rendered_js: false
word_count: 60
summary: This page serves as documentation for the Evolution API, specifically detailing how to delete stored OpenAI credentials using a DELETE request.
tags:
    - api
    - delete
    - openai-creds
    - curl
    - authorization
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Delete OpenAI Creds

```
curl --request DELETE \
  --url https://evolution-example/openai/creds/:openaiCredsId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

DELETE

/

openai

/

creds

/

:openaiCredsId

/

{instance}

Delete OpenAI Creds

```
curl --request DELETE \
  --url https://evolution-example/openai/creds/:openaiCredsId/{instance} \
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

[​](#parameter-openai-creds-id)

openaiCredsId

string

required

ID of the creds

#### Response

200 - undefined

[Creds config OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/set-creds)[Settigns config OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/settings-openai)