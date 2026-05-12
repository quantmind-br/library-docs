---
title: Récupérer les erreurs de Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:14:43.208561-03:00
rendered_js: false
word_count: 83
summary: This document describes the API endpoint used to retrieve error logs and failure details for batch scraping jobs.
tags:
    - batch-scraping
    - error-logs
    - api-endpoint
    - web-scraping
    - debugging
category: api
---

[Passer au contenu principal](#content-area)

Obtenir les erreurs d’un job de scraping par lot

> Remarque : Une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/batch-scrape-get-errors) est désormais disponible avec une journalisation et un débogage des erreurs améliorés.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de chemin

L’ID de la tâche de scraping par lot

#### Réponse

Tâches d’extraction en échec et détails des erreurs

Liste des URL pour lesquelles le scraping a été tenté mais bloqué par robots.txt