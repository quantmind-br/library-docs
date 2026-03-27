---
title: Change Tracking | Firecrawl
url: https://docs.firecrawl.dev/fr/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:24:12.871105-03:00
rendered_js: false
word_count: 1110
summary: This document explains how to use the change tracking feature in Firecrawl to monitor web pages for content updates, providing mechanisms for both line-by-line git-style diffs and structured JSON data comparisons.
tags:
    - web-scraping
    - change-tracking
    - api-integration
    - data-monitoring
    - diffing
    - automation
category: guide
---

![Change Tracking](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) Le suivi des modifications compare le contenu actuel d’une page à celui de la dernière fois où vous l’avez extraite. Ajoutez `changeTracking` à votre tableau `formats` pour détecter si une page est nouvelle, inchangée ou modifiée et, si vous le souhaitez, obtenir un diff structuré de ce qui a changé.

- Fonctionne avec `/scrape`, `/crawl` et `/batch/scrape`
- Deux modes de diff : `git-diff` pour les changements au niveau des lignes, `json` pour la comparaison au niveau des champs
- Limité à votre équipe, et éventuellement limité à un tag que vous fournissez

Chaque scrape avec `changeTracking` activé stocke un instantané et le compare à l’instantané précédent pour cette URL. Les instantanés sont stockés de manière persistante et n’expirent pas, ce qui garantit que les comparaisons restent précises, quel que soit le temps écoulé entre les scrapes.

ScrapeRésultatPremière fois`changeStatus: "new"` (aucune version précédente n’existe)Contenu inchangé`changeStatus: "same"`Contenu modifié`changeStatus: "changed"` (données de diff disponibles)Page supprimée`changeStatus: "removed"`

La réponse inclut ces champs dans l’objet `changeTracking` :

ChampTypeDescription`previousScrapeAt``string | null`Horodatage du scrape précédent (`null` lors du premier scrape)`changeStatus``string``"new"`, `"same"`, `"changed"` ou `"removed"``visibility``string``"visible"` (accessible via des liens / le sitemap) ou `"hidden"` (l’URL fonctionne mais n’est plus référencée)`diff``object | undefined`Diff ligne par ligne (présent uniquement en mode `git-diff` lorsque le statut est `"changed"`)`json``object | undefined`Comparaison au niveau des champs (présente uniquement en mode `json` lorsque le statut est `"changed"`)

## Utilisation de base

Incluez à la fois `markdown` et `changeTracking` dans le tableau `formats`. Le format `markdown` est obligatoire, car la fonctionnalité de suivi des modifications compare les pages à partir de leur contenu Markdown.

### Réponse

Lors du premier scrape, `changeStatus` est `"new"` et `previousScrapeAt` est `null` :

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

Lors des extractions ultérieures, `changeStatus` indique si le contenu a été modifié :

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Mode git-diff

Le mode `git-diff` retourne les modifications ligne par ligne dans un format similaire à celui de `git diff`. Indiquez un objet dans le tableau `formats` avec `modes: ["git-diff"]` :

### Réponse

L’objet `diff` contient à la fois un diff en texte brut et une représentation JSON structurée :

```
{
  "suiviDesModifications": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

L’objet structuré `diff.json` contient :

- `files` : tableau des fichiers modifiés (généralement un seul par page web)
- `chunks` : sections de modifications au sein d’un fichier
- `changes` : modifications de lignes individuelles avec un `type` (`"add"`, `"del"` ou `"normal"`), un numéro de ligne (`ln`) et un `content`

## mode JSON

Le mode `json` extrait des champs spécifiques à partir de la version actuelle et de la version précédente de la page à l’aide d’un schéma que vous définissez. C’est utile pour suivre les changements dans des données structurées comme les prix, les niveaux de stock ou les métadonnées, sans analyser un diff complet. Passez `modes: ["json"]` avec un `schema` définissant les champs à extraire :

### Réponse

Chaque champ du schéma est renvoyé avec les valeurs `previous` et `current` :

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "In Stock",
        "current": "In Stock"
      }
    }
  }
}
```

Vous pouvez également transmettre un `prompt` facultatif pour guider l’extraction par le LLM en complément du schéma.

Par défaut, le suivi des modifications compare les résultats au scrape le plus récent de la même URL effectué par votre équipe. Les tags vous permettent de maintenir **des historiques de suivi distincts** pour une même URL, ce qui est utile lorsque vous surveillez la même page à des intervalles ou dans des contextes différents.

## Crawl avec suivi des modifications

Ajoutez le suivi des modifications aux opérations de crawl pour surveiller l’ensemble d’un site et détecter les changements. Indiquez le format `changeTracking` dans `scrapeOptions` :

## Scrape par lot avec suivi des modifications

Utilisez le [scrape par lot](https://docs.firecrawl.dev/fr/features/batch-scrape) pour surveiller un ensemble précis d’URL :

## Planification du suivi des modifications

Le suivi des modifications est particulièrement utile lorsque vous effectuez du scraping à intervalles réguliers. Vous pouvez l’automatiser à l’aide de cron, d’ordonnanceurs cloud ou d’outils de workflow.

### Tâche cron

Créez un script qui surveille une URL et envoie une alerte en cas de changement :

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # Envoyer une alerte par e-mail, Slack, etc.
fi
```

Programmez-le avec `crontab -e` :

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

PlanificationExpressionToutes les heures`0 * * * *`Toutes les 6 heures`0 */6 * * *`Tous les jours à 9 h`0 9 * * *`Chaque lundi à 8 h`0 8 * * 1`

### Planificateurs cloud et serverless

- **AWS** : règle EventBridge qui déclenche une fonction Lambda
- **GCP** : Cloud Scheduler qui déclenche une Cloud Function
- **Vercel / Netlify** : fonctions serverless déclenchées par des tâches cron
- **GitHub Actions** : workflows planifiés avec les déclencheurs `schedule` et `cron`

### Automatisation des workflows

Des plateformes no-code comme **n8n**, **Zapier** et **Make** peuvent appeler l’API Firecrawl à intervalles réguliers et envoyer les résultats vers Slack, l’email ou des bases de données. Consultez les [guides d’automatisation de workflows](https://docs.firecrawl.dev/fr/developer-guides/workflow-automation/n8n).

## Webhooks

Pour les opérations asynchrones comme `crawl` et `batch scrape`, utilisez des [webhooks](https://docs.firecrawl.dev/fr/webhooks/overview) pour recevoir les résultats de suivi des modifications dès qu’ils sont disponibles, au lieu d’effectuer du polling.

Le payload de l’événement `crawl.page` inclut l’objet `changeTracking` pour chaque page :

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# Pricing\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

Pour plus de détails sur la configuration des webhooks (en-têtes, métadonnées, événements, réessais, vérification de la signature), consultez la [documentation sur les webhooks](https://docs.firecrawl.dev/fr/webhooks/overview).

## Référence de configuration

Ensemble complet des options disponibles lorsque vous passez un objet de format `changeTracking` :

ParamètreTypeValeur par défautDescription`type``string`(requis)Doit être `"changeTracking"``modes``string[]``[]`Modes de comparaison (diff) à activer : `"git-diff"`, `"json"`, ou les deux`schema``object`(aucune)JSON Schema pour la comparaison au niveau des champs (requis pour le mode `json`)`prompt``string`(aucun)Prompt personnalisé pour guider l’extraction par le LLM (utilisé avec le mode `json`)`tag``string``null`Identifiant distinct pour l’historique de suivi des modifications

### Modèles de données

## Détails importants

- **Conservation des snapshots** : Les snapshots sont stockés de manière persistante et n’expirent jamais. Un scrape effectué des mois après le précédent sera toujours correctement comparé au snapshot antérieur.
- **Portée** : Les comparaisons sont limitées à votre équipe. Votre premier scrape de n’importe quelle URL renvoie `"new"`, même si d’autres utilisateurs l’ont déjà scrappée.
- **Correspondance d’URL** : Les scrapes précédents sont associés à l’URL source exacte, à l’ID d’équipe, au format `markdown` et au `tag`. Gardez les URL cohérentes entre les scrapes.
- **Cohérence des paramètres** : Utiliser des paramètres `includeTags`, `excludeTags` ou `onlyMainContent` différents entre les scrapes de la même URL produit des comparaisons peu fiables.
- **Algorithme de comparaison** : L’algorithme est résistant aux variations d’espacement et aux changements dans l’ordre du contenu. Les URL sources d’iframe sont ignorées pour gérer la variation aléatoire introduite par les systèmes captcha/antibot.
- **Mise en cache** : Les requêtes avec `changeTracking` contournent le cache d’index. Le paramètre `maxAge` est ignoré.
- **Gestion des erreurs** : Surveillez le champ `warning` dans les réponses et gérez le cas où l’objet `changeTracking` pourrait être absent (cela peut se produire si la recherche en base de données pour le scrape précédent dépasse le délai imparti).

## Facturation

ModeCoûtsuivi des modifications de baseAucun coût supplémentaire (crédits de scraping standard)mode `git-diff`Aucun coût supplémentairemode `json`5 crédits par page

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’onboarding automatisé.