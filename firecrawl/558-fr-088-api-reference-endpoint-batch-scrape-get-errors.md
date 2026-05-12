---
title: Récupérer les erreurs d'extraction par lot - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:15:56.309178-03:00
rendered_js: false
word_count: 82
summary: This document provides the API specifications for retrieving error details and blocked URL information from failed batch scraping jobs.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - web-scraping
    - authentication
    - firecrawl
category: api
---

[Passer au contenu principal](#content-area)

Obtenir les erreurs d’un job de scraping par lots

> Êtes-vous un agent d’IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID du job de scraping par lots

#### Réponse

Tâches de scraping en échec et détails des erreurs

Liste des URL qui ont été tentées lors du scraping mais bloquées par robots.txt