---
title: Exploration | Firecrawl
url: https://docs.firecrawl.dev/fr/features/crawl
source: sitemap
fetched_at: 2026-03-23T07:24:02.952976-03:00
rendered_js: false
word_count: 1134
summary: This document explains how to use Firecrawl to perform recursive web crawling, including configuration options, job status management, and integration via webhooks or WebSockets.
tags:
    - web-crawling
    - api-documentation
    - data-extraction
    - webhooks
    - automation
    - recursive-scraping
category: api
---

L’exploration soumet une URL à Firecrawl, découvre récursivement chaque sous-page accessible et en extrait le contenu. Elle gère automatiquement les sitemaps, le rendu JavaScript et les limites de taux, en renvoyant du Markdown propre ou des données structurées pour chaque page.

- Découvre les pages via le sitemap et le parcours récursif des liens
- Prend en charge le filtrage des chemins, les limites de profondeur et le contrôle des sous-domaines et des liens externes
- Renvoie les résultats via polling, WebSocket ou webhook

## Installation

## Utilisation de base

Soumettez une tâche d’exploration en appelant `POST /v2/crawl` avec une URL de départ. Le point de terminaison renvoie un ID de tâche que vous utilisez pour interroger les résultats.

### Options de scrape

Toutes les options de l’[endpoint Scrape](https://docs.firecrawl.dev/fr/api-reference/endpoint/scrape) sont disponibles dans crawl via `scrapeOptions` (JS) / `scrape_options` (Python). Elles s’appliquent à chaque page que le crawler extrait, y compris les formats, le proxy, la mise en cache, les actions, la localisation et les tags.

## Vérification du statut du crawl

Utilisez l’ID du job pour interroger l’état du crawl et récupérer les résultats.

### Gestion des réponses

La réponse varie selon l’état du crawl. Pour les crawls non terminés ou les réponses volumineuses dépassant 10 Mo, un paramètre d’URL `next` est fourni. Vous devez appeler cette URL pour récupérer les 10 Mo de données suivants. Si le paramètre `next` est absent, cela indique la fin des données du crawl.

## Méthodes du SDK

Deux approches sont possibles pour utiliser crawl avec le SDK.

### Crawler puis attendre

La méthode `crawl` attend la fin du crawl et renvoie la réponse complète. Elle gère automatiquement la pagination. Cela est recommandé pour la plupart des cas d’usage.

La réponse inclut l’état du crawl et toutes les données extraites :

### Démarrer et vérifier plus tard

La méthode `startCrawl` / `start_crawl` renvoie immédiatement un ID de crawl. Vous pouvez ensuite vérifier manuellement l’état. Utile pour les crawls de longue durée ou une logique de polling personnalisée.

La réponse initiale renvoie l’ID du job :

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

## Résultats en temps réel avec WebSocket

La méthode watcher fournit des mises à jour en temps réel à mesure que les pages sont crawlées. Lancez un crawl, puis abonnez-vous aux événements pour traiter immédiatement les données.

## Webhooks

Vous pouvez configurer des webhooks pour recevoir des notifications en temps réel à mesure que votre crawl progresse. Cela vous permet de traiter les pages dès leur extraction, au lieu d’attendre la fin du crawl.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Types d’événements

ÉvénementDescription`crawl.started`Se déclenche au démarrage du crawl`crawl.page`Se déclenche pour chaque page extraite avec succès`crawl.completed`Se déclenche à la fin du crawl`crawl.failed`Se déclenche si le crawl rencontre une erreur

### Charge utile

```
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // Données de page pour les événements 'page'
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Vérification des signatures de webhook

Chaque requête de webhook provenant de Firecrawl inclut un en-tête `X-Firecrawl-Signature` contenant une signature HMAC-SHA256. Vérifiez toujours cette signature pour vous assurer que le webhook est authentique et n’a pas été altéré.

1. Récupérez votre secret de webhook dans l’[onglet Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) des paramètres de votre compte
2. Extrayez la signature de l’en-tête `X-Firecrawl-Signature`
3. Calculez le HMAC-SHA256 du corps brut de la requête à l’aide de votre secret
4. Comparez-le avec l’en-tête de signature en utilisant une fonction sécurisée contre les attaques par temporisation

Pour des exemples d’implémentation complets en JavaScript et Python, consultez la [documentation sur la sécurité des webhooks](https://docs.firecrawl.dev/fr/webhooks/security). Pour une documentation complète sur les webhooks, y compris les charges utiles d’événements détaillées, la structure des charges utiles, la configuration avancée et le dépannage, consultez la [documentation sur les webhooks](https://docs.firecrawl.dev/fr/webhooks/overview).

## Référence de configuration

Ensemble complet des paramètres disponibles lors de l’envoi d’une tâche de crawl :

ParamètreTypePar défautDescription`url``string`(obligatoire)URL de départ du crawl`limit``integer``10000`Nombre maximal de pages à crawler`maxDiscoveryDepth``integer`(aucun)Profondeur maximale depuis l’URL racine en fonction des sauts de découverte de liens, et non du nombre de segments `/` dans l’URL. Chaque fois qu’une nouvelle URL est trouvée sur une page, une profondeur supérieure de 1 à celle de la page sur laquelle elle a été découverte lui est attribuée. Le site racine et les pages du sitemap ont une profondeur de découverte égale à 0. Les pages à la profondeur maximale sont tout de même scrapées, mais les liens qu’elles contiennent ne sont pas suivis.`includePaths``string[]`(aucun)Expressions régulières sur le chemin de l’URL à inclure. Seuls les chemins correspondants sont crawlés.`excludePaths``string[]`(aucun)Expressions régulières sur le chemin de l’URL à exclure du crawl`regexOnFullURL``boolean``false`Applique `includePaths`/`excludePaths` à l’URL complète (y compris les paramètres de requête), et pas seulement au chemin`crawlEntireDomain``boolean``false`Suit les liens internes vers des URL sœurs ou parentes, et pas uniquement vers des chemins enfants`allowSubdomains``boolean``false`Suit les liens vers les sous-domaines du domaine principal`allowExternalLinks``boolean``false`Suit les liens vers des sites web externes`sitemap``string``"include"`Gestion du sitemap : `"include"` (par défaut), `"skip"` ou `"only"``ignoreQueryParameters``boolean``false`Évite de scraper plusieurs fois le même chemin avec des paramètres de requête différents`delay``number`(aucun)Délai, en secondes, entre les scrapes afin de respecter les limites de débit`maxConcurrency``integer`(aucun)Nombre maximal de scrapes simultanés. Utilise par défaut la limite de simultanéité de votre équipe.`scrapeOptions``object`(aucun)Options appliquées à chaque page lors du scrape (formats, proxy, mise en cache, actions, etc.)`webhook``object`(aucun)Configuration du webhook pour les notifications en temps réel`prompt``string`(aucun)Prompt en langage naturel permettant de générer les options de crawl. Les paramètres explicitement définis remplacent les équivalents générés.

## Détails importants

- **Découverte du sitemap** : Par défaut, le crawler inclut le sitemap du site pour découvrir les URL (`sitemap: "include"`). Si vous définissez `sitemap: "skip"`, seules les pages accessibles via des liens HTML depuis l’URL racine seront trouvées. Les ressources comme les PDF ou les pages profondément imbriquées listées dans le sitemap mais non directement liées en HTML ne seront pas découvertes. Pour une couverture maximale, conservez le paramètre par défaut.
- **Utilisation des crédits** : Chaque page crawlée coûte 1 crédit. Le mode JSON ajoute 4 crédits par page, le proxy avancé ajoute 4 crédits par page, et l’analyse des PDF coûte 1 crédit par page de PDF.
- **Expiration des résultats** : Les résultats des jobs restent disponibles via l’API pendant 24 heures après leur exécution. Passé ce délai, vous pouvez consulter les résultats dans les [journaux d’activité](https://www.firecrawl.dev/app/logs).
- **Erreurs de crawl** : Le tableau `data` contient les pages que Firecrawl a réussi à extraire. Utilisez le point de terminaison [Get Crawl Errors](https://docs.firecrawl.dev/fr/api-reference/endpoint/crawl-get-errors) pour récupérer les pages ayant échoué en raison d’erreurs réseau, de délais d’attente ou de blocages par robots.txt.
- **Résultats non déterministes** : Les résultats du crawl peuvent varier d’une exécution à l’autre avec la même configuration. Les pages sont extraites de manière concurrente, donc l’ordre dans lequel les liens sont découverts dépend du timing réseau et des pages qui finissent de se charger en premier. Cela signifie que différentes branches d’un site peuvent être explorées à des degrés divers à l’approche de la limite de profondeur, en particulier avec des valeurs élevées de `maxDiscoveryDepth`. Pour obtenir des résultats plus déterministes, définissez `maxConcurrency` sur `1` ou utilisez `sitemap: "only"` si le site dispose d’un sitemap complet.

> Êtes-vous un agent IA qui a besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.