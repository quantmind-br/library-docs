---
title: Action de l’agent - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-agent-action
source: sitemap
fetched_at: 2026-03-23T07:14:54.084488-03:00
rendered_js: false
word_count: 92
summary: This document provides the technical specifications for webhook request headers, payload structure, and expected response codes for handling agent action events.
tags:
    - webhooks
    - api-integration
    - hmac-security
    - payload-structure
    - event-notifications
category: reference
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Allowed value: `"agent.action"`

L’ID de la tâche d’agent.

Identifiant unique de cet envoi de webhook.

Tableau contenant un seul objet décrivant l’action effectuée.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour accuser réception.