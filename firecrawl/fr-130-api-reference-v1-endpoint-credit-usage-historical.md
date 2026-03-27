---
title: Historique d’utilisation des crédits - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:14:15.803221-03:00
rendered_js: false
word_count: 72
summary: This document describes an API endpoint used to retrieve historical credit usage data for an authenticated team, optionally segmented by API key.
tags:
    - api-endpoint
    - credit-usage
    - billing-history
    - team-management
    - authentication
category: api
---

Récupérer l’historique d’utilisation des crédits de l’équipe authentifiée

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

GET

/

team

/

credit-usage

/

historical

Récupérer l’historique d’utilisation des crédits de l’équipe authentifiée

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

Renvoie l’historique de l’utilisation des crédits, mois par mois. Le point de terminaison peut également, en option, ventiler l’utilisation par clé d’API.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de requête

Récupérer l’historique d’utilisation des crédits par clé API

#### Réponse