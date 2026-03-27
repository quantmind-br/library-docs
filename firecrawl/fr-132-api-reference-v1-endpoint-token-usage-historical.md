---
title: Historique d’utilisation des jetons - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:13:58.015385-03:00
rendered_js: false
word_count: 64
summary: This endpoint retrieves the historical token usage data for an authenticated team, providing a monthly breakdown of consumption optionally segmented by API key.
tags:
    - token-usage
    - api-documentation
    - historical-data
    - billing-metrics
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

Récupérer l’historique d’utilisation des tokens de l’équipe authentifiée (Extract uniquement)

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

Retourne l’utilisation des jetons, mois par mois. Ce point de terminaison peut également ventiler l’usage par clé d’API, en option.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de requête

Récupérer l’historique d’utilisation des jetons par clé API

#### Réponse