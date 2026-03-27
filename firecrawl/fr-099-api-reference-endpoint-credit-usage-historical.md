---
title: Historique d’utilisation des crédits - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:15:08.88357-03:00
rendered_js: false
word_count: 77
summary: This document describes an API endpoint used to retrieve the monthly credit usage history for an authenticated team, with an optional breakdown by API key.
tags:
    - api-endpoint
    - credit-usage
    - billing-history
    - authentication
    - api-key-tracking
category: api
---

Obtenir l’historique d’utilisation des crédits de l’équipe authentifiée

Renvoie l’historique de l’utilisation des crédits, mois par mois. Ce point de terminaison peut aussi, en option, ventiler l’utilisation par clé API.

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de requête

Récupérer l’historique d’utilisation des crédits par clé API

#### Réponse