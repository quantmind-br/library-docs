---
title: Uso de tokens - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:16:06.994411-03:00
rendered_js: false
word_count: 54
summary: This document describes the API endpoint for retrieving the remaining token usage balance for an authenticated team.
tags:
    - api-reference
    - token-usage
    - authentication
    - billing
    - firecrawl-api
category: api
---

Obtener los tokens restantes para el equipo autenticado (solo Extract)

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

Obtener los tokens restantes para el equipo autenticado (solo Extract)

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/token-usage), que ofrece funcionalidades y un rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Respuesta