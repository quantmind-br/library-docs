---
title: Find EvoAI Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/find-settings
source: sitemap
fetched_at: 2026-04-12T18:49:41.394584247-03:00
rendered_js: false
word_count: 35
summary: This document provides the endpoint details and a cURL example for fetching EvoAI bot settings, outlining the required GET request structure including instance parameters and authorization headers.
tags:
    - api-endpoint
    - settings-fetch
    - evoai-integration
    - get-request
    - authorization
category: reference
---

```
curl --request GET \
  --url https://evolution-example/evoai/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot EvoAI atualizadas com sucesso"
}
```

GET

/

evoai

/

fetchSettings

/

{instance}

```
curl --request GET \
  --url https://evolution-example/evoai/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

{
  "message": "Configurações do bot EvoAI atualizadas com sucesso"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Configurações do bot EvoAI atualizadas com sucesso.

Example:

`"Configurações do bot EvoAI atualizadas com sucesso"`

[Set EvoAI Settings](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/set-settings-evoai)[Change Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/change-status)