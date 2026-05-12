---
title: Scrape | Firecrawl
url: https://docs.firecrawl.dev/fr/features/scrape
source: sitemap
fetched_at: 2026-03-23T07:23:46.805171-03:00
rendered_js: false
word_count: 1498
summary: Firecrawl is an API service that converts websites into structured data and Markdown, specifically optimized for LLM applications. It supports diverse output formats, including raw HTML, screenshots, branding profiles, and custom JSON schema extraction.
tags:
    - web-scraping
    - llm
    - markdown-conversion
    - data-extraction
    - api-reference
    - branding-analysis
category: api
---

Firecrawl convertit les pages web en Markdown, idéal pour les applications LLM.

- Il gère les complexités : proxys, mise en cache, limites de débit, contenu bloqué par JavaScript
- Prend en charge le contenu dynamique : sites dynamiques, sites rendus par JavaScript, PDF, images
- Produit un Markdown propre, des données structurées, des captures d’écran ou du HTML.

Pour plus de détails, consultez la [référence de l’API Scrape Endpoint](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### point de terminaison /scrape

Utilisé pour scraper une URL et en récupérer le contenu.

### Installation

### Utilisation

Pour plus d’informations sur les paramètres, consultez la [référence de l’API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### Réponse

Les SDK renvoient directement l’objet de données. cURL renvoie la charge utile exactement comme ci-dessous.

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

## Formats de scraping

Vous pouvez désormais choisir les formats de votre sortie. Vous pouvez spécifier plusieurs formats de sortie. Les formats pris en charge sont :

- Markdown (`markdown`)
- Résumé (`summary`)
- HTML (`html`) - version nettoyée du HTML de la page
- HTML brut (`rawHtml`) - HTML non modifié tel que reçu depuis la page
- Capture d’écran (`screenshot`, avec des options comme `fullPage`, `quality`, `viewport`) — les URL de capture d’écran expirent après 24 heures
- Liens (`links`)
- JSON (`json`) - sortie structurée
- Images (`images`) - extrait toutes les URL d’images de la page
- Branding (`branding`) - extrait l’identité de marque et le design system

Les clés de sortie correspondront au format que vous choisissez.

### Point de terminaison /scrape (avec json)

Permet d’extraire des données structurées à partir de pages scrappées.

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

Vous pouvez désormais extraire sans schéma en passant simplement un `prompt` au point de terminaison. Le LLM choisit la structure des données.

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

### Options du format JSON

Lorsque vous utilisez le format `json`, passez un objet dans `formats` avec les paramètres suivants :

- `schema` : schéma JSON pour la sortie structurée.
- `prompt` : invite facultative pour orienter l’extraction lorsqu’un schéma est présent ou lorsque vous souhaitez un guidage léger.

### endpoint /scrape (avec branding)

Le format « branding » extrait des informations complètes sur l’identité de marque à partir d’une page web, notamment les couleurs, les polices, la typographie, les espacements, les composants d’interface, et bien plus encore. C’est utile pour l’analyse de design systems, la veille de marque, ou la création d’outils qui doivent comprendre l’identité visuelle d’un site web.

### Réponse

Le format d’habillage de marque retourne un objet `BrandingProfile` complet avec la structure suivante :

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Structure du profil de marque

L’objet `branding` contient les propriétés suivantes :

- `colorScheme` : Schéma de couleurs détecté (« light » ou « dark »)
- `logo` : URL du logo principal
- `colors` : Objet contenant les couleurs de la marque :
  
  - `primary`, `secondary`, `accent` : Couleurs principales de la marque
  - `background`, `textPrimary`, `textSecondary` : Couleurs de l’interface
  - `link`, `success`, `warning`, `error` : Couleurs sémantiques
- `fonts` : Tableau des familles de polices utilisées sur la page
- `typography` : Informations détaillées sur la typographie :
  
  - `fontFamilies` : Familles de polices principales, titres et code
  - `fontSizes` : Définitions des tailles pour les titres et le corps du texte
  - `fontWeights` : Définitions des graisses (light, regular, medium, bold)
  - `lineHeights` : Valeurs d’interlignage pour différents types de texte
- `spacing` : Informations sur les espacements et la mise en page :
  
  - `baseUnit` : Unité d’espacement de base en pixels
  - `borderRadius` : Rayon de bordure par défaut
  - `padding`, `margins` : Valeurs d’espacement
- `components` : Styles des composants d’interface :
  
  - `buttonPrimary`, `buttonSecondary` : Styles des boutons
  - `input` : Styles des champs de saisie
- `icons` : Informations sur le style des icônes
- `images` : Images de la marque (logo, favicon, og:image)
- `animations` : Paramètres d’animation et de transition
- `layout` : Configuration de la mise en page (grille, hauteurs d’en-tête/pied de page)
- `personality` : Traits de personnalité de la marque (ton, énergie, public cible)

### Combiner avec d’autres formats

Vous pouvez combiner le format « branding » avec d’autres formats pour obtenir des données de page complètes :

## Interagir avec la page à l’aide des actions

Firecrawl vous permet d’effectuer diverses actions sur une page web avant d’en extraire le contenu. C’est particulièrement utile pour interagir avec du contenu dynamique, naviguer entre les pages ou accéder à du contenu nécessitant une interaction de l’utilisateur. Voici un exemple d’utilisation des actions pour accéder à google.com, rechercher Firecrawl, cliquer sur le premier résultat et prendre une capture d’écran. Il est recommandé d’utiliser presque systématiquement l’action `wait` avant et après l’exécution d’autres actions afin de laisser suffisamment de temps au chargement de la page.

### Exemple

### Résultat

Pour en savoir plus sur les paramètres des actions, consultez la [référence de l’API](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Localisation et langue

Indiquez le pays et les langues souhaitées pour obtenir un contenu pertinent selon votre zone cible et vos préférences linguistiques.

### Fonctionnement

Lorsque vous renseignez les paramètres de localisation, Firecrawl utilisera, si possible, un proxy adapté et adoptera la langue et le fuseau horaire correspondants. Par défaut, la localisation est définie sur « US » si aucun paramètre n’est fourni.

### Utilisation

Pour utiliser les paramètres de localisation et de langue, incluez l’objet `location` dans le corps de votre requête avec les propriétés suivantes :

- `country` : code pays ISO 3166-1 alpha-2 (p. ex. « US », « AU », « DE », « JP »). Par défaut : « US ».
- `languages` : un tableau des langues et paramètres régionaux préférés pour la requête, par ordre de priorité. Par défaut : la langue de la localisation spécifiée.

Pour plus de détails sur les localisations prises en charge, consultez la [documentation sur les proxys](https://docs.firecrawl.dev/fr/features/proxies).

## Mise en cache et maxAge

Pour accélérer les requêtes, Firecrawl renvoie par défaut les résultats depuis le cache lorsqu’une copie récente est disponible.

- **Fenêtre de fraîcheur par défaut** : `maxAge = 172800000` ms (2 jours). Si une page en cache est plus récente que ce délai, elle est renvoyée instantanément ; sinon, la page est explorée puis mise en cache.
- **Performances** : cela peut accélérer les scrapes jusqu’à 5x lorsque les données n’ont pas besoin d’être ultra fraîches.
- **Toujours récupérer du contenu frais** : définissez `maxAge` à `0`. Cela contourne complètement le cache : chaque requête passe par l’intégralité du pipeline de scraping, ce qui allonge le temps de traitement et augmente le risque d’échec. Utilisez une valeur de `maxAge` non nulle si une fraîcheur maximale à chaque requête n’est pas critique.
- **Éviter le stockage** : définissez `storeInCache` sur `false` si vous ne voulez pas que Firecrawl mette en cache/stocke les résultats pour cette requête.
- **Consultation du cache uniquement** : définissez `minAge` pour effectuer une consultation du cache uniquement sans déclencher de nouveau scrape. La valeur est en millisecondes et spécifie l’ancienneté minimale que doivent avoir les données en cache. Si aucune donnée en cache n’est trouvée, une erreur `404` avec le code `SCRAPE_NO_CACHED_DATA` est renvoyée. Définissez `minAge` à `1` pour accepter toute donnée en cache, quel que soit son âge.
- **Suivi des modifications** : les requêtes qui incluent `changeTracking` contournent le cache, donc `maxAge` est ignoré.

Exemple (forcer du contenu frais) :

Exemple (utiliser une fenêtre de cache de 10 minutes) :

Vous pouvez désormais lancer l’extraction par lots de plusieurs URL simultanément. La fonction prend en arguments les URL de départ ainsi que des paramètres optionnels. L’argument params vous permet de définir des options supplémentaires pour la tâche d’extraction par lots, comme les formats de sortie.

### Fonctionnement

C’est très proche du fonctionnement du point de terminaison `/crawl`. Il lance un job de scraping par lot et renvoie un ID de job pour en vérifier l’état. Le SDK propose deux méthodes, synchrone et asynchrone. La méthode synchrone renvoie les résultats du job de scraping par lot, tandis que la méthode asynchrone renvoie un ID de job que vous pouvez utiliser pour en suivre l’état.

### Utilisation

### Réponse

Si vous utilisez les méthodes synchrones des SDK, elles renverront les résultats du travail de scraping par lot. Sinon, elles renverront un identifiant de travail que vous pourrez utiliser pour vérifier l’état du scraping par lot.

#### Synchrone

```
{
  "status": "terminée",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Page d’accueil de la documentation Firecrawl![logo clair](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Créer un « chat avec un site web » avec Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Apprenez à utiliser Firecrawl, Groq Llama 3 et LangChain pour créer un bot « discuter avec votre site web ».",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Asynchrone

Vous pouvez ensuite utiliser l’ID de la tâche pour vérifier l’état du batch scrape en appelant le point de terminaison `/batch/scrape/{id}`. Ce point de terminaison est destiné à être utilisé pendant l’exécution de la tâche ou juste après son achèvement, **car les tâches de batch scrape expirent après 24 heures**.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Mode amélioré

Pour les sites web complexes, Firecrawl propose un mode amélioré qui offre de meilleurs taux de réussite tout en préservant la confidentialité. En savoir plus sur le [Mode amélioré](https://docs.firecrawl.dev/fr/features/enhanced-mode).

## Rétention zéro des données (ZDR)

Firecrawl prend en charge la rétention zéro des données (ZDR) pour les équipes ayant des exigences strictes en matière de traitement des données. Lorsqu’elle est activée, Firecrawl ne conserve aucun contenu de page ni aucune donnée extraite au-delà de la durée de vie de la requête. Pour activer ZDR, définissez `zeroDataRetention: true` dans votre requête :

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

ZDR est disponible sur les offres Enterprise et doit être activé pour votre équipe. Rendez-vous sur [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) pour démarrer. ZDR ajoute **1 crédit supplémentaire par page** en plus du coût de base du scrape.

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir les instructions d’intégration automatisée.