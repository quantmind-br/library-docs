---
title: Obtenir l'état de l'extraction - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:15:24.915665-03:00
rendered_js: false
word_count: 80
summary: This document describes the API endpoint and requirements for retrieving the current status and token usage of a specific data extraction task.
tags:
    - api-reference
    - extraction-task
    - status-retrieval
    - authentication
    - token-usage
category: api
---

[Passer au contenu principal](#content-area)

Récupérer le statut d’une tâche d’extraction

> Êtes-vous un agent IA ayant besoin d’une API key Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’identifiant de la tâche d’extraction

#### Réponse

L’état actuel de la tâche d’extraction

Options disponibles:

`completed`,

`processing`,

`failed`,

`cancelled`

Nombre de tokens utilisés pour la tâche d’extraction. Uniquement disponible lorsque la tâche est terminée.