---
title: Find Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-status
source: sitemap
fetched_at: 2026-04-12T18:49:44.218642879-03:00
rendered_js: false
word_count: 40
summary: This document details the API endpoint used to retrieve active sessions for a Dify bot.
tags:
    - dify
    - bot-sessions
    - api-endpoint
    - rest-api
    - get-request
category: reference
---

Recupera as sessões ativas do bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/fetchSessions/:difyId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

dify

/

fetchSessions

/

:difyId

/

{instance}

Recupera as sessões ativas do bot Dify

```
curl --request GET \
  --url https://evolution-example/dify/fetchSessions/:difyId/{instance} \
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

[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/change-status)[Create n8n Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/create-n8n)