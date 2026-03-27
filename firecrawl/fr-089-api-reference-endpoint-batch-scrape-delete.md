---
title: Annuler une extraction par lots - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:16:00.897319-03:00
rendered_js: false
word_count: 71
summary: This document provides the API endpoint and authentication requirements for cancelling an active batch scraping job.
tags:
    - api-reference
    - scraping
    - batch-processing
    - cancellation
    - firecrawl
category: api
---

[Passer au contenu principal](#content-area)

Annuler une tâche de scraping par lots

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Annuler une tâche de scraping par lots

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de scraping par lots

#### Réponse

Exemple:

`"Batch scrape job successfully cancelled."`