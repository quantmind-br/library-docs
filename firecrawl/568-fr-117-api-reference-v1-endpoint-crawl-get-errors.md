---
title: Récupérer les erreurs de crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:14:45.005848-03:00
rendered_js: false
word_count: 80
summary: This document provides the API endpoint reference for retrieving error logs and blocked URLs associated with a specific web crawling task.
tags:
    - api-reference
    - crawl-errors
    - web-scraping
    - error-handling
    - robots-txt
category: api
---

Récupérer les erreurs d’une tâche de crawl

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

Récupérer les erreurs d’une tâche de crawl

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-get-errors) est maintenant disponible avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de crawl

#### Réponse

Tâches d’extraction en échec et détails des erreurs

Liste des URL pour lesquelles le scraping a été tenté mais bloqué par robots.txt