---
title: Recherche - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:14:02.998063-03:00
rendered_js: false
word_count: 375
summary: This document provides technical documentation for the Firecrawl search endpoint, detailing how to execute web searches, apply advanced query operators, and configure scraping options for search results.
tags:
    - web-scraping
    - search-api
    - data-extraction
    - query-operators
    - api-documentation
    - geo-targeting
    - temporal-search
category: api
---

Rechercher et éventuellement scraper les résultats de recherche

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/search) est désormais disponible avec des fonctionnalités et des performances améliorées.

Le point de terminaison /search combine la recherche web avec les capacités de scraping de Firecrawl pour renvoyer le contenu complet des pages pour n’importe quelle requête. Incluez `scrapeOptions` avec `formats: ["markdown"]` pour obtenir le contenu Markdown complet pour chaque résultat de recherche ; sinon, par défaut, vous recevrez uniquement les résultats (URL, title, description).

## Opérateurs de requête pris en charge

Nous prenons en charge divers opérateurs de requête pour affiner vos recherches.

OpérateurFonctionnalitéExemples`""`Correspondance exacte d’une chaîne de texte (non floue)`"Firecrawl"``-`Exclut certains mots‑clés ou inverse d’autres opérateurs`-bad`, `-site:firecrawl.dev``site:`Renvoie uniquement des résultats d’un site web spécifié`site:firecrawl.dev``inurl:`Renvoie uniquement des résultats qui incluent un mot dans l’URL`inurl:firecrawl``allinurl:`Renvoie uniquement des résultats qui incluent plusieurs mots dans l’URL`allinurl:git firecrawl``intitle:`Renvoie uniquement des résultats qui incluent un mot dans le titre de la page`intitle:Firecrawl``allintitle:`Renvoie uniquement des résultats qui incluent plusieurs mots dans le titre de la page`allintitle:firecrawl playground``related:`Renvoie uniquement des résultats liés à un domaine spécifique`related:firecrawl.dev`

## Paramètre location

Utilisez le paramètre `location` pour obtenir des résultats de recherche géociblés. Format : `"string"`. Exemples : `"Germany"`, `"San Francisco,California,United States"`. Consultez la [liste complète des lieux pris en charge](https://firecrawl.dev/search_locations.json) pour tous les pays et langues disponibles.

## Recherche par période

Utilisez le paramètre `tbs` pour filtrer les résultats par période, y compris selon des plages de dates personnalisées. Consultez la [documentation de la fonction de recherche](https://docs.firecrawl.dev/features/search#time-based-search) pour des exemples détaillés et les formats pris en charge.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

Nombre maximal de résultats à retourner

Plage requise: `1 <= x <= 100`

Paramètre de recherche temporel. Prend en charge les intervalles de temps prédéfinis (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`) et les plages de dates personnalisées (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`).

Paramètre de localisation des résultats de recherche

Délai d’expiration en millisecondes

Exclut des résultats de recherche les URL qui ne sont pas valides pour d’autres endpoints de Firecrawl. Cela permet de réduire les erreurs si vous transférez les données issues de la recherche vers d’autres endpoints de l’API Firecrawl.

Options de scraping des résultats de recherche

#### Réponse

Message d’avertissement en cas de problèmes

L’identifiant de la tâche de recherche