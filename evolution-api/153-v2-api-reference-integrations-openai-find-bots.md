---
title: Find OpenIA Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-bots
source: sitemap
fetched_at: 2026-04-12T18:48:21.560881331-03:00
rendered_js: false
word_count: 41
summary: This documentation explains how to use the GET endpoint to find OpenAI bots for a specified instance using an API key.
tags:
    - openai
    - find-bots
    - api-endpoint
    - get-request
    - authentication
    - path-parameter
category: reference
---

Find OpenAI Bots

```
curl --request GET \
  --url https://evolution-example/openai/find/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

openai

/

find

/

{instance}

Find OpenAI Bots

```
curl --request GET \
  --url https://evolution-example/openai/find/{instance} \
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

[Find OpenIA Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-bot)[Update Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/update-bot)