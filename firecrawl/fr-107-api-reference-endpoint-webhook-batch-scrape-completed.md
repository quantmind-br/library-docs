---
title: Extraction en lot terminée - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-batch-scrape-completed
source: sitemap
fetched_at: 2026-03-23T07:15:05.084675-03:00
rendered_js: false
word_count: 95
summary: This document describes the payload structure and security requirements for webhooks in the Firecrawl batch scraping process.
tags:
    - webhooks
    - api-integration
    - batch-scraping
    - hmac-security
    - data-extraction
category: reference
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Allowed value: `"batch_scrape.completed"`

L’ID de la tâche d’extraction par lot.

Identifiant unique de cet envoi de webhook.

Tableau vide. Récupérez les résultats via `GET /batch/scrape/{id}`.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour en accuser réception.