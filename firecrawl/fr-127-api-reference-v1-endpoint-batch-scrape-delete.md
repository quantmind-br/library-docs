---
title: Annuler un Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:14:33.482199-03:00
rendered_js: false
word_count: 70
summary: This document provides the API endpoint and authentication details required to cancel a pending batch scraping job.
tags:
    - api-reference
    - batch-scraping
    - web-scraping
    - task-management
    - firecrawl
category: api
---

[Passer au contenu principal](#content-area)

Annuler une tâche de scraping par lots

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Annuler une tâche de scraping par lots

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape-delete) est désormais disponible avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de scraping en lot

#### Réponse

Exemple:

`"Batch scrape job successfully cancelled."`