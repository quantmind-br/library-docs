---
title: Uso histórico de tokens - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:16:13.705918-03:00
rendered_js: false
word_count: 74
summary: This endpoint retrieves the historical token usage of the authenticated team, providing monthly data with an optional breakdown by API key.
tags:
    - token-usage
    - api-documentation
    - historical-data
    - team-metrics
    - authentication
category: api
---

GET

/

team

/

token-usage

/

historical

Obtener el uso histórico de tokens del equipo autenticado (solo Extract)

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalTokens": 1000
    }
  ]
}
```

Devuelve el uso histórico de tokens mes a mes. El punto de conexión también puede, opcionalmente, desglosar el uso por clave de API.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de consulta

byApiKey

boolean

predeterminado:false

Obtener el historial de uso de tokens por clave de API

#### Respuesta