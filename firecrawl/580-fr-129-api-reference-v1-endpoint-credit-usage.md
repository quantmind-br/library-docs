---
title: Utilisation des crédits - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/credit-usage
source: sitemap
fetched_at: 2026-03-23T07:14:23.733858-03:00
rendered_js: false
word_count: 50
summary: This document describes the endpoint used to retrieve current credit usage information for an authenticated team.
tags:
    - api-reference
    - credit-usage
    - account-billing
    - authentication
    - firecrawl
category: api
---

Récupérer les crédits restants de l’équipe authentifiée

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

Récupérer les crédits restants de l’équipe authentifiée

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

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/credit-usage) est désormais disponible, avec des fonctionnalités enrichies et de meilleures performances.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Réponse