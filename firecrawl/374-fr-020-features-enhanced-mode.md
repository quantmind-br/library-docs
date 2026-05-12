---
title: Mode avancé | Firecrawl
url: https://docs.firecrawl.dev/fr/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:24:08.754578-03:00
rendered_js: false
word_count: 143
summary: This document describes the proxy configuration options available in Firecrawl for web scraping, outlining the different proxy types and their cost and performance characteristics.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl-api
    - network-requests
    - scraping-strategy
category: configuration
---

Firecrawl propose différents types de proxy pour vous aider à effectuer du scraping sur des sites web de complexité variable. Définissez le paramètre `proxy` pour choisir la stratégie de proxy utilisée pour une requête.

## Types de proxy

Firecrawl prend en charge trois types de proxy :

TypeDescriptionVitesseCoût`basic`Proxies standard adaptés à la plupart des sitesRapide1 crédit`enhanced`Proxies avancés pour les sites complexesPlus lent5 crédits par requête`auto`Essaie d’abord `basic`, puis réessaie avec `enhanced` en cas d’échecVariable1 crédit si `basic` réussit, 5 crédits si `enhanced` est nécessaire

Si vous ne spécifiez pas de proxy, Firecrawl utilise `auto` par défaut.

## Utilisation de base

Définissez le paramètre `proxy` pour choisir une stratégie de proxy. L’exemple suivant utilise `auto`, ce qui permet à Firecrawl de décider quand passer à des proxies avancés.

> Êtes-vous un agent d’IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour les instructions d’intégration automatisée.