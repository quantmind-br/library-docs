---
title: Find Dify Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-settings
source: sitemap
fetched_at: 2026-04-12T18:49:39.663428972-03:00
rendered_js: false
word_count: 35
summary: This document details the endpoint for fetching Dify bot settings, providing a cURL example and describing its structure within an API context.
tags:
    - api-reference
    - dify
    - fetch-settings
    - curl
    - http-request
category: reference
---

```
curl --request GET \
  --url https://evolution-example/dify/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot Dify atualizadas com sucesso"
}
```

GET

/

dify

/

fetchSettings

/

{instance}

```
curl --request GET \
  --url https://evolution-example/dify/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot Dify atualizadas com sucesso"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Configurações do bot Dify atualizadas com sucesso.

Example:

`"Configurações do bot Dify atualizadas com sucesso"`

[Set Dify Settings](https://doc.evolution-api.com/v2/api-reference/integrations/dify/set-settings-dify)[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/change-status)