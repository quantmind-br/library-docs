---
title: Agent terminé - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-agent-completed
source: sitemap
fetched_at: 2026-03-23T07:14:56.149652-03:00
rendered_js: false
word_count: 85
summary: This document describes the structure and security requirements for webhooks, including the HMAC-SHA256 signature verification and the expected response format for successful receipt.
tags:
    - webhooks
    - hmac-sha256
    - api-security
    - data-payload
    - event-notification
category: reference
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Allowed value: `"agent.completed"`

ID de la tâche de l’agent

Identifiant unique de cet envoi de webhook.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour accuser réception.