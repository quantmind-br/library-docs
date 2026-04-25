---
title: Find settings OpenAI - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-settings
source: sitemap
fetched_at: 2026-04-12T18:48:19.776370678-03:00
rendered_js: false
word_count: 50
summary: This documentation serves as a central hub for the Evolution API, providing access points for getting started, general API references, and specific endpoints like fetching OpenAI settings.
tags:
    - api
    - openai
    - settings
    - documentation
    - integration
    - rest-api
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find OpenAI Settings

```
curl --request GET \
  --url https://evolution-example/openai/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

openai

/

fetchSettings

/

{instance}

Find OpenAI Settings

```
curl --request GET \
  --url https://evolution-example/openai/fetchSettings/{instance} \
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

[Settigns config OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/settings-openai)[Change status OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/change-status)