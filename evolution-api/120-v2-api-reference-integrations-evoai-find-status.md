---
title: Find Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/find-status
source: sitemap
fetched_at: 2026-04-12T18:49:34.686886389-03:00
rendered_js: false
word_count: 40
summary: This document provides instructions on how to use a GET request to fetch the active sessions for an EvoAI bot instance via an API endpoint.
tags:
    - evoai
    - api
    - sessions
    - fetch
    - get-request
    - bot-management
category: reference
---

Recupera as sessões ativas do bot EvoAI

```
curl --request GET \
  --url https://evolution-example/evoai/fetchSessions/:evoaiId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

evoai

/

fetchSessions

/

:evoaiId

/

{instance}

Recupera as sessões ativas do bot EvoAI

```
curl --request GET \
  --url https://evolution-example/evoai/fetchSessions/:evoaiId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Sessões recuperadas com sucesso.

[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/change-status)[Create Flowise Bot](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/create-bot)