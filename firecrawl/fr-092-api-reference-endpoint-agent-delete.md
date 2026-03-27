---
title: Annuler l’agent - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:15:52.966973-03:00
rendered_js: false
word_count: 61
summary: This document provides the API endpoint and authorization requirements to cancel a running agent task via a DELETE request.
tags:
    - api-reference
    - firecrawl
    - agent-task
    - data-cancellation
    - rest-api
    - authentication
category: api
---

Annuler une tâche d’agent

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

Annuler une tâche d’agent

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

> Vous êtes un agent d’IA et vous avez besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’onboarding automatisé.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de l’agent

#### Réponse

Tâche de l’agent annulée avec succès