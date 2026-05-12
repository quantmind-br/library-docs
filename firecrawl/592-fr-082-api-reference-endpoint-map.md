---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:15:39.659151-03:00
rendered_js: false
word_count: 262
summary: This document provides technical documentation for configuring and executing web URL mapping using the Firecrawl API, including parameters for sitemap handling, search filtering, and proxy localization.
tags:
    - web-scraping
    - url-mapping
    - api-documentation
    - sitemap-configuration
    - data-crawling
category: api
---

[Passer au contenu principal](#content-area)

Mapper plusieurs URL en fonction des options

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

L’URL de base à partir de laquelle démarrer le crawl

Spécifiez une requête de recherche pour classer les résultats par pertinence. Exemple : « blog » renverra les URL qui contiennent le mot « blog » dans leur adresse, classées par pertinence.

sitemap

enum&lt;string&gt;

défaut:include

Mode sitemap lors du mapping. Si vous le réglez sur `skip`, le sitemap ne sera pas utilisé pour trouver des URL. Si vous le réglez sur `only`, seules les URL présentes dans le sitemap seront renvoyées. Par défaut (`include`), le sitemap et d’autres méthodes sont utilisés conjointement pour trouver des URL.

Options disponibles:

`skip`,

`include`,

`only`

Inclure les sous-domaines du site

Ne renvoyez pas d’URL contenant des paramètres de requête

Ignorez le cache du sitemap pour récupérer les URL les plus récentes. Les données du sitemap sont mises en cache pendant 7 jours ; utilisez ce paramètre lorsque votre sitemap a été mis à jour récemment.

Nombre maximal de liens à retourner

Plage requise: `x <= 100000`

Délai d’attente en millisecondes. Aucun délai d’attente n’est appliqué par défaut.

Paramètres de localisation de la requête. Lorsqu’ils sont spécifiés, un proxy approprié est utilisé, si disponible, et les paramètres de langue et de fuseau horaire correspondants sont émulés. La valeur par défaut est « US » si aucun paramètre n’est spécifié.

#### Réponse