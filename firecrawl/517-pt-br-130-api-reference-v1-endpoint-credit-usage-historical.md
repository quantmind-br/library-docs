---
title: Uso Histórico de Créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:10:43.360623-03:00
rendered_js: false
word_count: 68
summary: This endpoint retrieves the monthly historical credit usage for the authenticated team, with an optional breakdown by API key.
tags:
    - credit-usage
    - billing-api
    - account-management
    - api-analytics
    - usage-tracking
category: api
---

GET

/

team

/

credit-usage

/

historical

Obtenha o histórico de uso de créditos da equipe autenticada

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

Retorna o uso histórico de créditos mês a mês. O endpoint também pode, opcionalmente, detalhar o uso por chave de API.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de consulta

Obtenha o histórico de uso de créditos por chave de API

#### Resposta