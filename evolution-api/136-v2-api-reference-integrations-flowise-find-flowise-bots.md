---
title: Find Flowise Bots - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-flowise-bots
source: sitemap
fetched_at: 2026-04-12T18:48:54.175971286-03:00
rendered_js: false
word_count: 31
summary: This document provides the cURL command and expected response structure for retrieving active bot sessions from Flowise using a specific API endpoint.
tags:
    - flowise
    - api-call
    - get-sessions
    - endpoint-usage
    - authorization
category: reference
---

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/find/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

Recupera as sessões ativas do bot Flowise

```
curl --request GET \
  --url https://evolution-example/flowise/find/{instance} \
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

[Create Flowise Bot](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/create-bot)[Find Flowise Bot](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-flowise-bot)