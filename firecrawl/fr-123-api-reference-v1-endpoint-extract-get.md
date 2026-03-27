---
title: Obtenir le statut d'extraction - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:14:18.780256-03:00
rendered_js: false
word_count: 67
summary: This document provides the API endpoint details and authentication requirements for retrieving the current status of an extraction task.
tags:
    - api-reference
    - extraction-task
    - status-check
    - data-scraping
    - bearer-authentication
category: api
---

Récupérer le statut d'une tâche d'extraction

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

Récupérer le statut d'une tâche d'extraction

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/extract-get) est désormais disponible avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’identifiant de la tâche d’extraction

#### Réponse

Le statut actuel du job d’extraction

Options disponibles:

`completed`,

`processing`,

`failed`,

`cancelled`