---
title: Uso histórico de créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:16:47.991549-03:00
rendered_js: false
word_count: 70
summary: This endpoint retrieves the historical credit usage for an authenticated team, providing a month-by-month breakdown with an optional filter to group data by API key.
tags:
    - credit-usage
    - billing-history
    - api-analytics
    - team-management
    - auth-token
category: api
---

GET

/

team

/

credit-usage

/

historical

Obtén el historial de uso de créditos del equipo autenticado

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/credit-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalCredits": 1000
    }
  ]
}
```

Devuelve el uso histórico de créditos mes a mes. El endpoint también puede, opcionalmente, desglosar el uso por clave de API.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de consulta

byApiKey

boolean

predeterminado:false

Obtener el uso histórico de créditos por clave de API

#### Respuesta