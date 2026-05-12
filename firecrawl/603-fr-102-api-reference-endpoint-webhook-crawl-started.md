---
title: Début de l’exploration - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:14:35.529714-03:00
rendered_js: false
word_count: 120
summary: This document describes the structure, authentication headers, and expected response format for the crawl-started webhook event.
tags:
    - webhooks
    - api-integration
    - hmac-security
    - event-notifications
    - data-delivery
category: reference
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Toujours `true` pour cet événement.

Le type d’événement.

Allowed value: `"crawl.started"`

L’ID de la tâche de crawl, correspondant à l’`id` renvoyé par `POST /crawl`.

Identifiant unique pour cette livraison de webhook. À utiliser pour la déduplication : la même valeur est envoyée lors des nouvelles tentatives.

Tableau vide pour cet événement.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour accuser réception.