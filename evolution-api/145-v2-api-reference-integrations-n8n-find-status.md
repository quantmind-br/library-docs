---
title: Find Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/find-status
source: sitemap
fetched_at: 2026-04-12T18:48:31.418656937-03:00
rendered_js: false
word_count: 40
summary: This document provides an API endpoint and the corresponding cURL request to retrieve active sessions for an n8n bot using a specified instance ID and an API key.
tags:
    - api-reference
    - n8n
    - fetch-sessions
    - bot-management
    - rest-api
category: reference
---

Recupera as sessões ativas do bot n8n

```
curl --request GET \
  --url https://evolution-example/n8n/fetchSessions/:n8nId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

n8n

/

fetchSessions

/

:n8nId

/

{instance}

Recupera as sessões ativas do bot n8n

```
curl --request GET \
  --url https://evolution-example/n8n/fetchSessions/:n8nId/{instance} \
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

[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/change-status)[Create EvoAI Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/create-evoai)