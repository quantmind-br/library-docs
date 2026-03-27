---
title: Échec de l’agent - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/webhook-agent-failed
source: sitemap
fetched_at: 2026-03-23T07:14:55.788173-03:00
rendered_js: false
word_count: 99
summary: This document describes the structure and expected response format for agent failure webhooks, including HMAC signature verification and payload fields.
tags:
    - webhook
    - api-integration
    - security-hmac
    - agent-failed
    - event-payload
category: api
---

[Passer au contenu principal](#content-area)

#### En-têtes

Signature HMAC-SHA256 du corps brut de la requête, au format `sha256=<hex>`. Présente lorsqu’un secret HMAC est configuré dans les [paramètres de votre compte](https://www.firecrawl.dev/app/settings?tab=advanced). Consultez [Sécurité des webhooks](https://docs.firecrawl.dev/webhooks/security) pour savoir comment la vérifier.

Exemple:

`"sha256=abc123def456789..."`

#### Corps

Toujours `false` pour cet événement.

Allowed value: `"agent.failed"`

L’ID de la tâche de l’agent.

Identifiant unique de cet envoi de webhook.

Message d’erreur lisible par un humain décrivant l’échec.

L’objet de métadonnées personnalisé que vous avez fourni dans la configuration du webhook. Renvoyé dans chaque envoi de webhook.

#### Réponse

Renvoyez n’importe quel code d’état `2xx` pour en accuser réception.