---
title: Agent annulé - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-agent-cancelled
source: sitemap
fetched_at: 2026-03-23T07:14:50.189135-03:00
rendered_js: false
word_count: 90
summary: This document describes the structure and authentication requirements for webhook events related to agent task cancellations.
tags:
    - webhook
    - hmac-sha256
    - event-notification
    - api-integration
    - security-verification
category: reference
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Toujours `false` pour cet événement.

Allowed value: `"agent.cancelled"`

L’ID de la tâche de l’agent.

Identifiant unique de cet envoi de webhook.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour accuser réception.