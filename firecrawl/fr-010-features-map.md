---
title: Cartographier | Firecrawl
url: https://docs.firecrawl.dev/fr/features/map
source: sitemap
fetched_at: 2026-03-23T07:23:56.776681-03:00
rendered_js: false
word_count: 445
summary: This document explains how to use the /map endpoint to generate a list of links for a given website, including filtering options via search parameters and localization settings.
tags:
    - web-scraping
    - site-mapping
    - url-discovery
    - api-documentation
    - data-extraction
    - firecrawl
category: api
---

## Présentation de /map

La façon la plus simple de passer d’une seule URL à une cartographie de l’ensemble du site. C’est extrêmement utile pour :

- Lorsque vous devez demander à l’utilisateur final de choisir quels liens scraper
- Lorsque vous devez connaître rapidement les liens d’un site
- Lorsque vous devez scraper des pages d’un site liées à un sujet spécifique (utilisez le paramètre `search`)
- Lorsque vous ne souhaitez scraper que certaines pages d’un site

## Mapping

### point de terminaison /map

Permet de cartographier une URL et d’obtenir les URL du site web. Renvoie la plupart des liens présents sur le site. Les URL sont principalement découvertes à partir du sitemap du site web, complété par les résultats des moteurs de recherche (SERP) et les pages précédemment explorées afin d’améliorer la couverture. Vous pouvez contrôler le comportement du sitemap avec le paramètre `sitemap`.

### Installation

### Utilisation

### Réponse

Les SDK renvoient directement l’objet de données. cURL renvoie la charge utile exactement comme indiqué ci-dessous.

```
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "Transformez n’importe quelle URL en données propres",
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "5 moyens simples d’accéder à GLM-4.5",
      "description": "Découvrez comment accéder aux modèles GLM-4.5 en local, via des applications de chat, via l’API officielle, et grâce à l’API des marketplaces LLM pour une intégration fluide…",
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "Prévisualisez la réponse de l’API et obtenez les extraits de code pour l’API",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - L’API de données web pour l’IA",
      "description": "L’API d’exploration, de scraping et de recherche pour l’IA. Conçue pour passer à l’échelle. Firecrawl fournit l’ensemble du web aux agents et aux développeurs d’IA. Propre, structuré et …",
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - L’API de données web pour l’IA",
      "description": "L’API d’exploration, de scraping et de recherche pour l’IA. Conçue pour passer à l’échelle. Firecrawl fournit l’ensemble du web aux agents et aux développeurs d’IA. Propre, structuré et …"
    },
    ...
  ]
}
```

#### Cartographie avec recherche

La cartographie avec le paramètre `search` vous permet de rechercher des URL spécifiques au sein d’un site web.

```
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer VOTRE_CLÉ_API' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

La réponse sera une liste classée de la plus pertinente à la moins pertinente.

```
{
  "status": "succès",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Docs Firecrawl",
      "description": "Documentation Firecrawl",
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "SDK Firecrawl pour Python",
      "description": "Documentation du SDK Firecrawl pour Python"
    },
    ...
  ]
}
```

## Localisation et langue

Indiquez le pays et les langues préférées pour obtenir un contenu pertinent en fonction de la zone ciblée et de vos préférences linguistiques, comme avec le point de terminaison /scrape.

### Fonctionnement

Lorsque vous définissez les paramètres de localisation, Firecrawl utilise, si disponible, un proxy approprié et émule les paramètres de langue et de fuseau horaire correspondants. Par défaut, la localisation est définie sur « US » si aucun paramètre n’est spécifié.

### Utilisation

Pour utiliser les paramètres de lieu et de langue, incluez l’objet `location` dans le corps de votre requête avec les propriétés suivantes :

- `country` : code pays ISO 3166-1 alpha-2 (p. ex. « US », « AU », « DE », « JP »). Valeur par défaut : « US ».
- `languages` : tableau des langues et paramètres régionaux préférés pour la requête, par ordre de priorité. Par défaut : la langue du lieu spécifié.

Pour plus de détails sur les lieux pris en charge, consultez la [documentation des proxies](https://docs.firecrawl.dev/fr/features/proxies).

## Considérations

Ce point de terminaison privilégie la rapidité ; il se peut donc qu’il ne récupère pas tous les liens d’un site web. Il s’appuie principalement sur le sitemap du site, complété par des données de crawl mises en cache et par les résultats des moteurs de recherche. Pour obtenir une liste d’URL plus exhaustive et à jour, envisagez plutôt d’utiliser le point de terminaison [/crawl](https://docs.firecrawl.dev/fr/features/crawl).

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.