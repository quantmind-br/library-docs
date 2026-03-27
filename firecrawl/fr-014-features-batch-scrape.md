---
title: Scrape par lots | Firecrawl
url: https://docs.firecrawl.dev/fr/features/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:24:13.714009-03:00
rendered_js: false
word_count: 544
summary: This document explains how to perform batch scraping tasks in Firecrawl, covering both synchronous and asynchronous operations, concurrency control, structured data extraction, and webhook integration.
tags:
    - batch-scraping
    - web-scraping
    - api-integration
    - concurrency
    - webhooks
    - data-extraction
category: guide
---

Le scrape par lots vous permet de scraper plusieurs URL en une seule tâche. Transmettez une liste d’URL et des paramètres facultatifs, et Firecrawl les traite en parallèle avant de renvoyer tous les résultats ensemble.

- Fonctionne comme `/crawl`, mais pour une liste explicite d’URL
- Modes synchrone et asynchrone
- Prend en charge toutes les options de scrape, y compris l’extraction structurée
- Concurrence configurable par tâche

## Fonctionnement

Vous pouvez exécuter un scraping par lot de deux façons :

ModeMéthode SDK (JS / Python)ComportementSynchrone`batchScrape` / `batch_scrape`Démarre le lot et attend la fin de l’opération, en renvoyant tous les résultatsAsynchrone`startBatchScrape` / `start_batch_scrape`Démarre le lot et renvoie un identifiant de tâche pour le polling ou les webhooks

## Utilisation de base

### Réponse

Appeler `batchScrape` / `batch_scrape` renvoie les résultats complets une fois le lot terminé.

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

Appeler `startBatchScrape` / `start_batch_scrape` renvoie un ID de tâche que vous pouvez suivre via `getBatchScrapeStatus` / `get_batch_scrape_status`, le point de terminaison API `/batch/scrape/{id}` ou des webhooks. Les résultats de la tâche sont accessibles via l’API pendant 24 heures après son achèvement. Passé ce délai, vous pouvez toujours consulter l’historique et les résultats de vos batch scrapes dans les [journaux d’activité](https://www.firecrawl.dev/app/logs).

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Concurrence

Par défaut, un job de scraping par lot utilise l’intégralité de la limite de navigateurs concurrents de votre équipe (voir [Rate Limits](https://docs.firecrawl.dev/fr/rate-limits)). Vous pouvez la réduire pour chaque job avec le paramètre `maxConcurrency`. Par exemple, `maxConcurrency: 50` limite ce job à 50 opérations de scraping simultanées. Fixer une valeur trop basse pour de gros lots ralentira significativement le traitement, donc ne la réduisez que si vous devez conserver de la capacité pour d’autres jobs concurrents.

Vous pouvez utiliser le grattage en lot pour extraire des données structurées depuis chaque page du lot. C’est utile si vous voulez appliquer le même schéma à une liste d’URL.

### Réponse

`batchScrape` / `batch_scrape` retourne les résultats complets :

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "json": {
        "title": "Créer un « chat avec un site web » avec Groq Llama 3 | Firecrawl",
        "description": "Découvrez comment utiliser Firecrawl, Groq Llama 3 et LangChain pour créer un bot de « chat avec votre site web »."
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` retourne un ID de tâche :

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Webhooks

Vous pouvez configurer des webhooks pour recevoir des notifications en temps réel à mesure que chaque URL de votre lot est récupérée. Cela vous permet de traiter les résultats immédiatement, sans attendre la fin de l’ensemble du lot.

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer VOTRE_CLÉ_API' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "n_importe_quelle_valeur"
        },
        "events": ["démarrage", "page", "terminé"]
      }
    }'
```

### Types d’événements

ÉvénementDescription`batch_scrape.started`La tâche de scraping par lot a démarré`batch_scrape.page`Une URL a été scrapée avec succès`batch_scrape.completed`Toutes les URL ont été traitées`batch_scrape.failed`La tâche de scraping par lot a rencontré une erreur

### Charge utile

Chaque livraison de webhook inclut un corps JSON avec la structure suivante :

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "batch-job-id",
  "data": [...],
  "metadata": {},
  "error": null
}
```

### Vérification des signatures de webhook

Chaque requête de webhook provenant de Firecrawl inclut un en-tête `X-Firecrawl-Signature` contenant une signature HMAC-SHA256. Vérifiez toujours cette signature pour vous assurer que le webhook est authentique et n’a pas été altéré.

1. Récupérez votre secret de webhook dans l’[onglet Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) des paramètres de votre compte
2. Extrayez la signature depuis l’en-tête `X-Firecrawl-Signature`
3. Calculez le HMAC-SHA256 du corps brut de la requête en utilisant votre secret
4. Comparez-la à l’en-tête de signature à l’aide d’une fonction sécurisée vis-à-vis du temps d’exécution (timing-safe)

Pour des exemples d’implémentation complets en JavaScript et Python, consultez la [documentation sur la sécurité des webhooks](https://docs.firecrawl.dev/fr/webhooks/security). Pour une documentation complète sur les webhooks, incluant des payloads d’événement détaillés, une configuration avancée et des conseils de dépannage, consultez la [documentation sur les webhooks](https://docs.firecrawl.dev/fr/webhooks/overview).

> Êtes-vous un agent IA qui a besoin d’une API key Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.