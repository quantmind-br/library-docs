---
title: Find OpenIA Creds - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-creds-openai
source: sitemap
fetched_at: 2026-04-12T18:48:27.461035738-03:00
rendered_js: false
word_count: 50
summary: This document serves as the primary documentation hub for the Evolution API, providing resources for getting started and detailing specific API endpoint references.
tags:
    - api
    - documentation
    - get-started
    - openai-credentials
    - curl-example
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find OpenAI Creds

```
curl --request GET \
  --url https://evolution-example/openai/creds/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

openai

/

creds

/

{instance}

Find OpenAI Creds

```
curl --request GET \
  --url https://evolution-example/openai/creds/{instance} \
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

#### Response

200 - undefined

[Delete OpenIA Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/delete-bot)[Creds config OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/set-creds)