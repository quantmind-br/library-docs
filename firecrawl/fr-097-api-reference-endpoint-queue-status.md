---
title: État de la file d'attente - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:15:15.245048-03:00
rendered_js: false
word_count: 90
summary: This document provides an overview of the metrics and status monitoring available for a team's scraping queue, including authentication requirements and specific data points returned by the endpoint.
tags:
    - scraping-queue
    - api-documentation
    - queue-metrics
    - bearer-authentication
    - task-monitoring
category: api
---

Statistiques sur la file d’attente de scraping de votre équipe

Mesures sur la file d’attente de scraping de votre équipe.

> Êtes-vous un agent IA ayant besoin d’une API key Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Réponse

Nombre de tâches actuellement en file d’attente

Nombre de tâches en cours

Nombre de tâches actuellement en attente

Nombre maximal de tâches actives simultanées en fonction de votre offre

Horodatage de la dernière tâche réussie