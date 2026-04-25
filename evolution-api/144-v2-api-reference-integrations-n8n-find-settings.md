---
title: Find n8n Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/find-settings
source: sitemap
fetched_at: 2026-04-12T18:48:34.067370674-03:00
rendered_js: false
word_count: 35
summary: This document details the API endpoint used to fetch n8n bot settings, including the necessary GET request structure and required authorization header.
tags:
    - n8n
    - settings
    - api-endpoint
    - get-request
    - authorization
    - fetch
category: reference
---

```
curl --request GET \
  --url https://evolution-example/n8n/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot n8n atualizadas com sucesso"
}
```

GET

/

n8n

/

fetchSettings

/

{instance}

```
curl --request GET \
  --url https://evolution-example/n8n/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot n8n atualizadas com sucesso"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Configurações do bot n8n atualizadas com sucesso.

Example:

`"Configurações do bot n8n atualizadas com sucesso"`

[Set n8n Settings](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/set-settings-n8n)[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/change-status)