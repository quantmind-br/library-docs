---
title: Utilisation des jetons - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:14:12.371793-03:00
rendered_js: false
word_count: 57
summary: This document describes the API endpoint for retrieving the remaining token usage balance for an authenticated team.
tags:
    - api-endpoint
    - token-usage
    - authentication
    - billing
    - firecrawl-api
category: api
---

Récupérer le nombre de jetons restants pour l’équipe authentifiée (extraction uniquement)

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

Récupérer le nombre de jetons restants pour l’équipe authentifiée (extraction uniquement)

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

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/token-usage) est désormais disponible avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Réponse