---
title: Mode JSON | Firecrawl
url: https://docs.firecrawl.dev/fr/features/llm-extract
source: sitemap
fetched_at: 2026-03-23T07:23:50.921623-03:00
rendered_js: false
word_count: 501
summary: This document explains how to use Firecrawl's JSON mode to extract structured data from websites using AI-powered scraping with or without predefined schemas.
tags:
    - web-scraping
    - ai-extraction
    - structured-data
    - json-mode
    - api-integration
    - data-parsing
category: guide
---

Firecrawl utilise l’IA pour obtenir des données structurées à partir de pages web en 3 étapes :

1. **Définir le schéma (optionnel) :** Définissez un schéma JSON (au format OpenAI) pour préciser les données souhaitées, ou fournissez simplement un `prompt` si vous n’avez pas besoin d’un schéma strict, ainsi que l’URL de la page web.
2. **Envoyer la requête :** Envoyez votre URL et votre schéma au point de terminaison /scrape en utilisant le mode JSON. Découvrez comment ici : [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)
3. **Récupérer vos données :** Recevez des données propres et structurées correspondant à votre schéma, prêtes à l’emploi.

Cela rend l’obtention de données web, au format dont vous avez besoin, rapide et simple.

### Mode JSON via /scrape

Permet d’extraire des données structurées à partir de pages explorées.

Résultat :

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Scraping et extraction de données web propulsés par l’IA",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Scraping et extraction de données web propulsés par l’IA",
        "robots": "suivre, indexer",
        "ogTitle": "Firecrawl",
        "ogDescription": "Scraping et extraction de données web propulsés par l’IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl"
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Données structurées sans schéma

Vous pouvez aussi extraire sans schéma en passant simplement un `prompt` au point de terminaison. Le LLM détermine la structure des données.

Résultat :

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "Collecte et extraction de données web propulsées par l’IA",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "Collecte et extraction de données web propulsées par l’IA",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "Collecte et extraction de données web propulsées par l’IA",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

Voici un exemple complet montrant comment extraire des informations structurées sur une entreprise à partir d’un site web :

Résultat :

```
{
  "success": true,
  "data": {
    "json": {
      "company_mission": "Transformer les sites web en données prêtes pour les LLM",
      "supports_sso": true,
      "is_open_source": true,
      "is_in_yc": true
    }
  }
}
```

### Options du format JSON

Lorsque vous utilisez le mode JSON dans la v2, incluez un objet dans `formats` avec le schéma directement intégré : `formats: [{ type: 'json', schema: { ... }, prompt: '...' }]` Paramètres :

- `schema` : schéma JSON décrivant la sortie structurée souhaitée (obligatoire pour l’extraction basée sur un schéma).
- `prompt` : invite facultative pour guider l’extraction (également utilisée pour l’extraction sans schéma).

**Important :** Contrairement à la v1, il n’existe pas de paramètre distinct `jsonOptions` dans la v2. Le schéma doit être inclus directement dans l’objet de format du tableau `formats`.

Si vous observez des résultats incohérents ou incomplets lors de l’extraction JSON, ces pratiques peuvent aider :

- **Gardez les prompts courts et ciblés.** Des prompts longs avec de nombreuses règles augmentent la variabilité. Placez plutôt les contraintes spécifiques (comme les valeurs autorisées) dans le schéma.
- **Utilisez des noms de propriétés concis.** Évitez d’inclure des instructions ou des listes d’énumération dans les noms de propriétés. Utilisez une clé courte comme `"installation_type"` et placez les valeurs autorisées dans un tableau `enum`.
- **Ajoutez des tableaux `enum` pour les champs contraints.** Lorsqu’un champ possède un ensemble fixe de valeurs, listez-les dans `enum` et assurez-vous qu’elles correspondent exactement au texte affiché sur la page.
- **Incluez la gestion de `null` dans les descriptions de champs.** Ajoutez `"Return null if not found on the page."` à la `description` de chaque champ afin que le modèle ne devine pas les valeurs manquantes.
- **Ajoutez des indications de localisation.** Indiquez au modèle où trouver les données sur la page, par exemple : `"Flow rate in GPM from the Specifications table."`.
- **Divisez les grands schémas en requêtes plus petites.** Les schémas avec de nombreux champs (par exemple 30+) produisent des résultats moins cohérents. Divisez-les en 2–3 requêtes de 10–15 champs chacune.

**Exemple de schéma bien structuré :**

```
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": ["string", "null"],
      "description": "Full descriptive product name as shown on the page. Return null if not found."
    },
    "installation_type": {
      "type": ["string", "null"],
      "description": "Installation type from the Specifications section. Return null if not found.",
      "enum": ["Deck-mount", "Wall-mount", "Countertop", "Drop-in", "Undermount"]
    },
    "flow_rate_gpm": {
      "type": ["string", "null"],
      "description": "Flow rate in GPM from the Specifications section. Return null if not found."
    }
  }
}
```

> Vous êtes un agent IA et vous avez besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.