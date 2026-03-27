---
title: Recherche | Firecrawl
url: https://docs.firecrawl.dev/fr/features/search
source: sitemap
fetched_at: 2026-03-23T07:24:02.637324-03:00
rendered_js: false
word_count: 1007
summary: This document explains the Firecrawl search API, which allows users to perform web searches, filter by source or category, and optionally scrape result content in various formats.
tags:
    - web-scraping
    - search-api
    - ai-data-extraction
    - api-documentation
    - data-processing
    - crawling
category: api
---

L’API de recherche de Firecrawl vous permet d’effectuer des recherches sur le web et, si vous le souhaitez, de scraper les résultats en une seule opération.

- Choisissez des formats de sortie spécifiques (markdown, HTML, liens, captures d’écran)
- Recherchez sur le web avec des paramètres personnalisables (localisation, etc.)
- Récupérez, en option, le contenu des résultats dans divers formats
- Contrôlez le nombre de résultats et définissez des délais d’attente

Pour plus de détails, consultez la [référence de l’API du point de terminaison /search](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Effectuer une recherche avec Firecrawl

### point de terminaison /search

Permet d’effectuer des recherches sur le web et, en option, de récupérer le contenu des résultats.

### Installation

### Utilisation de base

### Réponse

Les SDK renvoient directement l’objet de données. cURL renvoie la charge utile complète.

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

## Types de résultats de recherche

En plus des résultats web classiques, Search prend en charge des types de résultats spécialisés via le paramètre `sources` :

- `web` : résultats web standard (par défaut)
- `news` : résultats axés sur l’actualité
- `images` : résultats de recherche d’images

Vous pouvez demander plusieurs sources dans un seul appel (par exemple, `sources: ["web", "news"]`). Dans ce cas, le paramètre `limit` s’applique **par type de source** — ainsi, `limit: 5` avec `sources: ["web", "news"]` renvoie jusqu’à 5 résultats web et jusqu’à 5 résultats d’actualité (10 au total). Si vous avez besoin de paramètres différents par source (par exemple, des valeurs `limit` différentes ou des `scrapeOptions` différentes), effectuez plutôt des appels séparés.

## Catégories de recherche

Filtrez les résultats de recherche par catégorie à l’aide du paramètre `categories` :

- `github` : Rechercher dans les dépôts GitHub, le code, les tickets et la documentation
- `research` : Rechercher sur des sites académiques et de recherche (arXiv, Nature, IEEE, PubMed, etc.)
- `pdf` : Rechercher des fichiers PDF

### Recherche par catégorie sur GitHub

Recherchez spécifiquement dans les dépôts GitHub :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-VOTRE_CLÉ_API" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Recherche par catégorie

Recherchez sur des sites académiques et de recherche :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-VOTRE_CLÉ_API" \
  -d '{
    "query": "transformers en apprentissage automatique",
    "categories": ["recherche"],
    "limit": 10
  }'
```

### Recherche multi-catégories

Combinez plusieurs catégories dans une seule recherche :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-VOTRE_CLE_API" \
  -d '{
    "query": "réseaux de neurones",
    "categories": ["github", "recherche"],
    "limit": 15
  }'
```

### Format de réponse par catégorie

Chaque résultat de recherche comporte un champ `category` indiquant sa source :

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Implémentation de réseau de neurones"
        "description": "Une implémentation PyTorch de réseaux de neurones"
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Avancées dans l’architecture des réseaux de neurones"
        "description": "Article de recherche sur les améliorations des réseaux de neurones"
        "category": "research"
      }
    ]
  }
}
```

Exemples :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-VOTRE_CLÉ_API" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### Recherche d’images HD avec filtre de taille

Utilisez les opérateurs de recherche d’images pour trouver des images en haute résolution :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "coucher de soleil imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "fond d'écran montagne larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Résolutions HD courantes :**

- `imagesize:1920x1080` - Full HD (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - HD et supérieur
- `larger:2560x1440` - QHD et supérieur

Recherchez et récupérez le contenu des résultats de recherche en une seule opération.

Toutes les options du point de terminaison /scrape sont prises en charge par ce point de terminaison de recherche via le paramètre `scrapeOptions`.

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - L’API ultime de web scraping",
      "description": "Firecrawl est une API de web scraping puissante qui convertit n’importe quel site web en données propres et structurées, prêtes pour l’IA et l’analyse.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nL’API ultime de web scraping\n\n## Convertissez n’importe quel site web en données propres et structurées\n\nFirecrawl simplifie l’extraction de données depuis des sites web pour des applications d’IA, des études de marché, l’agrégation de contenu, et plus encore...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - L’API ultime de web scraping",
        "description": "Firecrawl est une API de web scraping puissante qui convertit n’importe quel site web en données propres et structurées, prêtes pour l’IA et l’analyse.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Options de recherche avancées

L’API de recherche de Firecrawl prend en charge plusieurs paramètres pour personnaliser votre recherche :

### Personnalisation de la localisation

### Recherche par plage temporelle

Utilisez le paramètre `tbs` pour filtrer les résultats par période. Notez que `tbs` s’applique uniquement aux résultats de la source `web` — il ne filtre pas les résultats `news` ou `images`. Si vous avez besoin d’actualités filtrées par période, envisagez d’utiliser une source `web` avec l’opérateur `site:` pour cibler des domaines d’actualités spécifiques.

Valeurs `tbs` courantes :

- `qdr:h` - Dernière heure
- `qdr:d` - Dernières 24 heures
- `qdr:w` - Dernière semaine
- `qdr:m` - Dernier mois
- `qdr:y` - Dernière année
- `sbd:1` - Trier par date (des plus récents aux plus anciens)

Pour un filtrage plus précis, vous pouvez spécifier des plages de dates exactes avec le format de plage de dates personnalisé :

Vous pouvez combiner `sbd:1` avec des filtres temporels pour obtenir des résultats triés par date dans une plage temporelle donnée. Par exemple, `sbd:1,qdr:w` renvoie les résultats de la dernière semaine, triés du plus récent au plus ancien, et `sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` renvoie les résultats de décembre 2024 triés par date.

### Délai d’attente personnalisé

Définissez un délai d’attente personnalisé pour les opérations de recherche :

## Zero Data Retention (ZDR)

Pour les équipes ayant des exigences strictes en matière de traitement des données, Firecrawl propose des options Zero Data Retention (ZDR) pour le point de terminaison `/search` via le paramètre `enterprise`. La recherche ZDR est disponible avec les offres Enterprise — rendez-vous sur [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) pour démarrer.

### ZDR de bout en bout

Avec le ZDR de bout en bout, Firecrawl et notre fournisseur de recherche en amont appliquent tous deux une politique de rétention zéro des données. Aucune donnée de requête ni de résultat n’est stockée à aucun moment du pipeline.

- **Coût :** 10 crédits pour 10 résultats
- **Paramètre :** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer VOTRE_CLÉ_API" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### ZDR anonymisé

Avec le ZDR anonymisé, Firecrawl applique une politique complète de rétention zéro des données de notre côté. Notre fournisseur de recherche peut mettre la requête en cache, mais elle est entièrement anonymisée — aucune information permettant de vous identifier n’y est associée.

- **Coût :** 2 crédits pour 10 résultats
- **Paramètre :** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer VOTRE_CLÉ_API" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### Combiner la recherche ZDR avec Scrape ZDR

Si vous utilisez la recherche avec du scraping de contenu (`scrapeOptions`), le paramètre `enterprise` couvre la partie recherche, tandis que `zeroDataRetention` dans `scrapeOptions` couvre la partie scraping. Pour bénéficier d’un ZDR complet sur les deux, définissez les deux :

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer VOTRE_CLÉ_API" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## Impact sur les coûts

Le coût d’une recherche est de 2 crédits pour 10 résultats de recherche. Si les options de scraping sont activées, les coûts de scraping standard s’appliquent à chaque résultat de recherche :

- **Basic scrape** : 1 crédit par page web
- **PDF parsing** : 1 crédit par page PDF
- **mode proxy amélioré** : 4 crédits supplémentaires par page web
- **mode JSON** : 4 crédits supplémentaires par page web

Pour aider à contrôler les coûts :

- Définissez `parsers: []` si l’analyse de PDF n’est pas nécessaire
- Utilisez `proxy: "basic"` plutôt que `"enhanced"` lorsque possible, ou réglez-le sur `"auto"`
- Limitez le nombre de résultats de recherche avec le paramètre `limit`

## Options de scraping avancées

Pour plus de détails sur les options de scraping, consultez la [documentation de la fonctionnalité Scrape](https://docs.firecrawl.dev/features/scrape). Toutes les fonctionnalités, à l’exception de l’agent FIRE-1 et du suivi des modifications, sont prises en charge par ce point de terminaison de recherche.

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.