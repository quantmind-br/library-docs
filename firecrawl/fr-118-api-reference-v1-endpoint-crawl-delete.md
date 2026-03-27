---
title: Annuler un crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:14:28.220609-03:00
rendered_js: false
word_count: 51
summary: This document provides the API specification for cancelling a specific web crawling task using a DELETE request.
tags:
    - api-reference
    - web-scraping
    - task-management
    - firecrawl-api
    - rest-api
category: api
---

[Passer au contenu principal](#content-area)

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Remarque : Une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-delete) est disponible, avec des fonctionnalités enrichies et de meilleures performances.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’identifiant de la tâche de crawl

#### Réponse

Options disponibles:

`cancelled`