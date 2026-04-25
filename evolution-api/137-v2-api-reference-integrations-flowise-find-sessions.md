---
title: Find Sessions Flowise - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-sessions
source: sitemap
fetched_at: 2026-04-12T18:48:49.632676776-03:00
rendered_js: false
word_count: 39
summary: This document provides the method and endpoint for retrieving active sessions from a Flowise bot instance using a GET request.
tags:
    - flowise
    - sessions
    - api-endpoint
    - get-request
    - bot-management
category: reference
---

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/fetchSessions/:flowiseId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

flowise

/

fetchSessions

/

:flowiseId

/

{instance}

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/fetchSessions/:flowiseId/{instance} \
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

[Change Status Session](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/change-session-status)[Set Chatwoot](https://doc.evolution-api.com/v2/api-reference/integrations/chatwoot/set-chatwoot)