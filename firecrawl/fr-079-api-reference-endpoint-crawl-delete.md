---
title: Annuler le crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:15:51.635953-03:00
rendered_js: false
word_count: 61
summary: This document provides the API endpoint and instructions for canceling an active web crawl task using a specific task ID.
tags:
    - web-crawling
    - api-documentation
    - task-management
    - rest-api
    - firecrawl
category: api
---

[Passer au contenu principal](#content-area)

Annuler une tâche de crawl

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

Annuler une tâche de crawl

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L'ID de la tâche de crawl

#### Réponse

Options disponibles:

`cancelled`