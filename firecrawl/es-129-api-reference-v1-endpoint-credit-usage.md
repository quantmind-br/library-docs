---
title: Uso de créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:16:42.050885-03:00
rendered_js: false
word_count: 47
summary: This document provides the API endpoint details and authentication requirements for retrieving the current credit usage and billing information for an authenticated team.
tags:
    - api-endpoint
    - credit-usage
    - billing-information
    - firecrawl-api
    - authentication
category: api
---

Obtener los créditos restantes del equipo autenticado

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_credits": 1000,
    "plan_credits": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

Obtener los créditos restantes del equipo autenticado

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_credits": 1000,
    "plan_credits": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/credit-usage) con funciones mejoradas y mayor rendimiento.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Respuesta