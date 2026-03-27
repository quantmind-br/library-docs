---
title: Recherche - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:15:27.073056-03:00
rendered_js: false
word_count: 738
summary: This document provides a technical reference for the Firecrawl search endpoint, detailing how to perform web searches, apply filters, and configure scraping options for retrieved results.
tags:
    - api-reference
    - web-scraping
    - search-engine
    - data-extraction
    - query-parameters
    - api-integration
category: api
---

Rechercher et éventuellement scraper les résultats de recherche

L’endpoint de recherche combine la recherche web avec les capacités de scraping de Firecrawl pour renvoyer le contenu complet des pages pour n’importe quelle requête. Incluez `scrapeOptions` avec `formats: [{"type": "markdown"}]` pour obtenir le contenu markdown complet pour chaque résultat de recherche ; sinon, vous recevrez par défaut les résultats (URL, title, description). Vous pouvez également utiliser d’autres formats comme `{"type": "summary"}` pour un contenu condensé.

## Opérateurs de requête pris en charge

Nous prenons en charge une variété d’opérateurs de requête qui vous permettent de mieux filtrer vos recherches.

OpérateurFonctionnalitéExemples`""`Correspondance exacte (non floue) d’une chaîne de texte`"Firecrawl"``-`Exclut certains mots-clés ou annule d’autres opérateurs`-bad`, `-site:firecrawl.dev``site:`Ne renvoie que les résultats d’un site web spécifié`site:firecrawl.dev``filetype:`Ne renvoie que les résultats avec une extension de fichier spécifique`filetype:pdf`, `-filetype:pdf``inurl:`Ne renvoie que les résultats qui incluent un mot dans l’URL`inurl:firecrawl``allinurl:`Ne renvoie que les résultats qui incluent plusieurs mots dans l’URL`allinurl:git firecrawl``intitle:`Ne renvoie que les résultats qui incluent un mot dans le titre de la page`intitle:Firecrawl``allintitle:`Ne renvoie que les résultats qui incluent plusieurs mots dans le titre de la page`allintitle:firecrawl playground``related:`Ne renvoie que les résultats liés à un domaine spécifique`related:firecrawl.dev``imagesize:`Ne renvoie que les images avec des dimensions exactes`imagesize:1920x1080``larger:`Ne renvoie que les images plus grandes que les dimensions spécifiées`larger:1920x1080`

## Paramètre location

Utilisez le paramètre `location` pour obtenir des résultats de recherche géociblés. Format : `"string"`. Exemples : `"Germany"`, `"San Francisco,California,United States"`. Consultez la [liste complète des emplacements pris en charge](https://firecrawl.dev/search_locations.json) pour tous les pays et langues disponibles.

## Paramètre country

Utilisez le paramètre `country` pour définir le pays des résultats de recherche à l’aide des codes de pays ISO. Valeur par défaut : `"US"`. Exemples : `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`.

```
{
  "query": "restaurants",
  "country": "DE"
}
```

## Paramètre `categories`

Filtrez les résultats de recherche par catégories spécifiques à l’aide du paramètre `categories` :

- **`github`** : Rechercher dans les dépôts GitHub, le code, les tickets et la documentation
- **`research`** : Rechercher sur des sites académiques et de recherche (arXiv, Nature, IEEE, PubMed, etc.)
- **`pdf`** : Rechercher des fichiers PDF

### Exemple d’utilisation

```
{
  "query": "apprentissage automatique",
  "categories": ["github", "recherche"],
  "limit": 10
}
```

### Catégories de la réponse

Chaque résultat inclut un champ `category` indiquant sa source :

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## Recherche basée sur le temps

Utilisez le paramètre `tbs` pour filtrer les résultats par périodes, y compris avec des intervalles de dates personnalisés. Consultez la [documentation de la fonctionnalité de recherche](https://docs.firecrawl.dev/features/search#time-based-search) pour des exemples détaillés et les formats pris en charge.

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.

#### Autorisations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corps

La requête de recherche

Maximum string length: `500`

Nombre maximal de résultats à renvoyer

Plage requise: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

Sources à interroger. Déterminera les tableaux disponibles dans la réponse. Valeur par défaut : \['web'].

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

Catégories utilisées pour filtrer les résultats. Par défaut, la valeur est \[], ce qui signifie qu’aucun filtre de catégorie ne sera appliqué aux résultats.

- GitHub
- Research
- PDF

Paramètre de recherche temporel. Accepte des intervalles prédéfinis (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`), des plages de dates personnalisées (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`) ainsi que le tri par date (`sbd:1`). Les valeurs peuvent être combinées, par exemple : `sbd:1,qdr:w`.

Paramètre de localisation pour les résultats de recherche (par ex. `San Francisco,California,United States`). Pour de meilleurs résultats, définissez ce paramètre ainsi que le paramètre `country`.

Code pays ISO pour le ciblage géographique des résultats de recherche (par exemple `US`). Pour de meilleurs résultats, définissez ce paramètre ainsi que le paramètre `location`.

Délai d'expiration en millisecondes

Exclut des résultats de recherche les URL qui ne sont pas valides pour d’autres endpoints Firecrawl. Cela permet de réduire les erreurs si vous transmettez les données issues de la recherche vers d’autres endpoints de l’API Firecrawl.

Options de search Enterprise pour la rétention zéro des données (ZDR). Utilisez `["zdr"]` pour un ZDR de bout en bout (10 credits / 10 résultats) ou `["anon"]` pour un ZDR anonymisé (2 credits / 10 résultats). Doit être activé pour votre équipe.

Options disponibles:

`anon`,

`zdr`

Options pour extraire les résultats de recherche

#### Réponse

Les résultats de la recherche. Les tableaux disponibles dépendront des sources que vous avez spécifiées dans la requête. Par défaut, le tableau `web` sera renvoyé.

Message d’avertissement si des problèmes surviennent

L’ID de la tâche de recherche

Nombre de crédits utilisés pour la recherche