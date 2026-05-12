---
title: Démarrage rapide | Firecrawl
url: https://docs.firecrawl.dev/fr/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:26.746207-03:00
rendered_js: false
word_count: 438
summary: This document provides an introduction to Firecrawl, an API service designed to scrape and crawl web content, converting it into structured data or markdown specifically formatted for LLM and AI agent integration.
tags:
    - web-scraping
    - llm-data
    - ai-agents
    - data-extraction
    - api-integration
    - browser-automation
category: guide
---

## Scrapez votre premier site web

Transformez n’importe quel site web en données propres, prêtes pour les LLM, avec un seul appel d’API.

### Utiliser Firecrawl avec des agents d’IA (recommandé)

Le skill Firecrawl est le moyen le plus rapide pour les agents de découvrir et d’utiliser Firecrawl. Sans lui, votre agent ne saura pas que Firecrawl est disponible.

```
npx -y firecrawl-cli@latest init --all --browser
```

Ou utilisez le [MCP Server](https://docs.firecrawl.dev/fr/mcp-server) pour connecter Firecrawl directement à Claude, Cursor, Windsurf, VS Code et à d’autres outils d’IA.

### Effectuez votre première requête

Copiez le code ci-dessous, remplacez `fc-YOUR-API-KEY` par votre clé d’API, puis exécutez-le :

Exemple de réponse

```
{
  "success": true,
  "data": {
    "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples...",
    "metadata": {
      "title": "Example Domain",
      "sourceURL": "https://example.com"
    }
  }
}
```

* * *

## Que peut faire Firecrawl ?

### Pourquoi Firecrawl ?

- **Sorties prêtes pour les LLM** : obtenez un markdown propre, du JSON structuré, des captures d’écran, et bien plus
- **Gère les aspects complexes** : proxies, anti-bot, rendu JavaScript et contenu dynamique
- **Fiable** : conçu pour la production avec une haute disponibilité et des résultats constants
- **Rapide** : obtenez des résultats en quelques secondes, optimisé pour un haut débit
- **Bac à sable de navigateur** : environnements de navigateur entièrement gérés pour les agents, sans configuration, qui passent à l’échelle quelle que soit la charge
- **Serveur MCP** : connectez Firecrawl à n’importe quel outil d’IA via le [Model Context Protocol](https://docs.firecrawl.dev/fr/mcp-server)

* * *

Extrayez n’importe quelle URL et obtenez son contenu en Markdown, HTML ou d’autres formats. Consultez la [documentation de la fonctionnalité Scrape](https://docs.firecrawl.dev/fr/features/scrape) pour toutes les options.

Réponse

Les SDK renvoient directement l’objet de données. cURL renvoie la charge utile exactement comme indiqué ci-dessous.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I est là ! [Découvrez notre sortie du Jour 2 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 2 mois offerts...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Accueil - Firecrawl",
      "description": "Firecrawl explore et convertit n’importe quel site web en markdown propre.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Données,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Transformez n’importe quel site web en données prêtes pour les LLM.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl"
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Recherche

L’API de recherche de Firecrawl vous permet d’effectuer des recherches sur le web et, en option, de scraper les résultats en une seule opération.

- Choisissez des formats de sortie spécifiques (Markdown, HTML, liens, captures d’écran)
- Choisissez des sources spécifiques (web, actualités, images)
- Recherchez sur le web avec des paramètres personnalisables (localisation, etc.)

Pour plus de détails, consultez la [référence de l’API du point de terminaison /search](https://docs.firecrawl.dev/fr/api-reference/endpoint/search).

Réponse

Les SDK renverront directement l’objet `data`. cURL renverra la charge utile complète.

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - L'API de données web pour l'IA",
        "description": "L'API d'exploration, de scraping et de recherche pour l'IA. Conçue pour passer à l'échelle. Firecrawl met l'ensemble du web à la portée des agents et développeurs d'IA.",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl : Transformez des sites entiers en contenus prêts pour les LLM… - GitHub",
        "description": "Firecrawl est un service d'API qui prend une URL, l'explore et la convertit en Markdown propre ou en données structurées.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Guide de démarrage rapide | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "La startup de Y Combinator Firecrawl est prête à payer 1 M$ pour embaucher trois agents IA comme employés",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "Elle a désormais publié trois nouvelles annonces sur le job board de YC pour « agents IA uniquement » et a réservé un budget total de 1 million de dollars pour y parvenir.",
        "date": "il y a 3 mois",
        "position": 1
      },
      ...
    ]
  }
}
```

## Agent

L’agent Firecrawl est un outil autonome de collecte de données sur le web. Décrivez simplement les données dont vous avez besoin, et il se chargera de les rechercher, d’y naviguer et de les extraire depuis n’importe où sur le web. Consultez la [documentation de la fonctionnalité Agent](https://docs.firecrawl.dev/fr/features/agent) pour toutes les options.

Exemple de réponse

```
{
  "success": true,
  "data": {
    "result": "Notion propose les formules tarifaires suivantes :\n\n1. **Free** - 0 $/mois - Pour les particuliers...\n2. **Plus** - 10 $/utilisateur/mois - Pour les petites équipes...\n3. **Business** - 18 $/utilisateur/mois - Pour les entreprises...\n4. **Enterprise** - Tarification personnalisée - Pour les grandes organisations...",
    "sources": [
      "https://www.notion.so/pricing"
    ]
  }
}
```

## Browser

Le bac à sable de navigateur de Firecrawl offre à vos agents un environnement de navigateur sécurisé pour interagir avec le web. Remplissez des formulaires, cliquez sur des boutons, authentifiez-vous, et plus encore. Aucune configuration locale ni installation de Chromium n’est nécessaire. Consultez la [documentation de la fonctionnalité Browser](https://docs.firecrawl.dev/fr/features/browser) pour une documentation complète.

Exemple de réponse

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-...",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-...?interactive=true"
}
```

* * *

## Ressources