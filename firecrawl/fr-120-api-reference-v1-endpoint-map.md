---
title: Map - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:14:05.047395-03:00
rendered_js: false
word_count: 183
summary: This document provides the technical specifications and request parameters for an API endpoint designed to map multiple URLs from a base source.
tags:
    - url-mapping
    - web-scraping
    - api-documentation
    - crawler-configuration
    - network-parameters
category: api
---

[Passer au contenu principal](#content-area)

Cartographier plusieurs URL selon les options

> Remarque : une nouvelle [version v2 de cette API](https://docs.firecrawl.dev/fr/api-reference/endpoint/map) est désormais disponible, avec des fonctionnalités et des performances améliorées.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

L’URL de base à partir de laquelle démarrer l’exploration

Requête de recherche à utiliser pour la cartographie. Pendant la phase Alpha, la partie « intelligente » de la fonction de recherche est limitée à 500 résultats. En revanche, si « map » renvoie davantage de résultats, aucune limite n’est appliquée.

Ignorer le sitemap du site lors de l’exploration.

Ne renvoyer que les liens présents dans le sitemap du site web

Inclure les sous-domaines du site

Nombre maximal de liens renvoyés

Plage requise: `x <= 30000`

Délai d’expiration en millisecondes. Aucun délai d’expiration n’est défini par défaut.

Paramètres de localisation pour la requête. Lorsqu’ils sont spécifiés, un proxy approprié sera utilisé si disponible et les paramètres de langue et de fuseau horaire correspondants seront émulés. La valeur par défaut est « US » si aucun paramètre n’est indiqué.

#### Réponse