---
title: Utilisation historique des jetons - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:15:21.720601-03:00
rendered_js: false
word_count: 74
summary: This document describes an API endpoint used to retrieve historical token usage data for an authenticated team, with an optional breakdown by API key.
tags:
    - api-documentation
    - token-usage
    - usage-metrics
    - authentication
    - historical-data
category: api
---

Obtenir l’historique d’utilisation des jetons de l’équipe authentifiée (Extract uniquement)

Renvoie l’utilisation historique des jetons, mois par mois. L’endpoint peut également, en option, ventiler l’utilisation par clé d’API.

> Êtes-vous un agent IA ayant besoin d’une clé d’API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’onboarding automatisé.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Paramètres de requête

Récupérer l’historique d’utilisation des jetons par clé API

#### Réponse