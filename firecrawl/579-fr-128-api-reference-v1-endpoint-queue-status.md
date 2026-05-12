---
title: Statut de la file d’attente - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:14:06.002811-03:00
rendered_js: false
word_count: 89
summary: This document provides an overview of the scraping queue status API endpoint, detailing the authentication method and the specific metrics returned regarding task queues and processing limits.
tags:
    - api-documentation
    - scraping-service
    - queue-status
    - rate-limits
    - authentication
    - task-management
category: api
---

[Passer au contenu principal](#content-area)

Indicateurs sur la file d’attente de scraping de votre équipe

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/queue-status) est désormais disponible, avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Réponse

Nombre de tâches actuellement en file d'attente

Nombre de tâches en cours

Nombre de tâches actuellement en attente

Nombre maximal de tâches actives en parallèle en fonction de votre offre

Horodatage de la tâche la plus récente exécutée avec succès