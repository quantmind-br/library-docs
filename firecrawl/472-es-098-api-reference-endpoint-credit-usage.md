---
title: Uso de créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:17:47.137025-03:00
rendered_js: false
word_count: 54
summary: This document outlines the API endpoint for retrieving current credit usage and billing information for an authenticated Firecrawl team account.
tags:
    - api-reference
    - credit-usage
    - billing-information
    - firecrawl-api
    - authentication
    - account-management
category: api
---

Obtener los créditos restantes para el equipo autenticado

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingCredits": 1000,
    "planCredits": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

Obtener los créditos restantes para el equipo autenticado

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/credit-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingCredits": 1000,
    "planCredits": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Respuesta