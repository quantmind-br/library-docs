---
title: Find Flowise settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/flowise/find-settings
source: sitemap
fetched_at: 2026-04-12T18:48:51.534975321-03:00
rendered_js: false
word_count: 37
summary: This document provides the technical details and necessary cURL command to retrieve the settings configuration for a Flowise bot using an API endpoint.
tags:
    - flowise
    - api-settings
    - bot-management
    - rest-api
    - curl
category: reference
---

Recupera os configurações do bot flowise

```
curl --request GET \
  --url https://evolution-example/flowise/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "sessions": "<string>"
}
```

GET

/

flowise

/

fetchSettings

/

{instance}

Recupera os configurações do bot flowise

```
curl --request GET \
  --url https://evolution-example/flowise/fetchSettings/{instance} \
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

[Set Settings Flowise Bots](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/set-settings)[Change Status Session](https://doc.evolution-api.com/v2/api-reference/integrations/flowise/change-session-status)