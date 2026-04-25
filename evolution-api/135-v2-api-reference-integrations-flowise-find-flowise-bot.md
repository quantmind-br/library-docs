---
title: Find Flowise Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-flowise-bot
source: sitemap
fetched_at: 2026-04-12T18:49:03.714308663-03:00
rendered_js: false
word_count: 40
summary: This document provides the API endpoint and method for retrieving active sessions associated with a Flowise bot instance.
tags:
    - api
    - flowise
    - sessions
    - get
    - endpoint
    - rest
category: reference
---

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/find/:flowiseId/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

flowise

/

find

/

:flowiseId

/

{instance}

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/find/:flowiseId/{instance} \
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

[Find Flowise Bots](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-flowise-bots)[Update Flowise Bot](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/update-flowise-bot)