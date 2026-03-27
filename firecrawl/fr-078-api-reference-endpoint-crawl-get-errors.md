---
title: Récupérer les erreurs de crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:15:38.73164-03:00
rendered_js: false
word_count: 80
summary: This document provides the API specification for retrieving error information and blocked URL details from a specific web crawl task.
tags:
    - api-documentation
    - crawl-errors
    - firecrawl
    - web-scraping
    - error-handling
    - robots-txt
category: api
---

[Passer au contenu principal](#content-area)

Récupérer les erreurs d'une tâche de crawl

> Vous êtes un agent IA et avez besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de crawl

#### Réponse

Tâches de scraping en échec et détails des erreurs

Liste des URL qui ont été tentées lors du scraping mais bloquées par robots.txt