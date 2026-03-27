---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/fr/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:38:30.538539-03:00
rendered_js: false
word_count: 143
summary: Ce document explique comment configurer et utiliser des webhooks pour recevoir des notifications en temps réel lors de l'exécution d'opérations de scraping et d'exploration de données.
tags:
    - webhooks
    - api-integration
    - real-time-notifications
    - data-scraping
    - event-driven
    - webhook-configuration
category: guide
---

Les webhooks vous permettent de recevoir des notifications en temps réel au fur et à mesure de l’exécution de vos opérations, au lieu d’interroger périodiquement leur statut.

## Opérations prises en charge

OpérationÉvénementsCrawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## Configuration

Ajoutez un objet `webhook` à votre requête :

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["start", "page", "completed", "failed"]
  }
}
```

ChampTypeRequisDescription`url`stringOuiL’URL de votre endpoint (HTTPS)`headers`objectNonEn-têtes personnalisés à inclure dans les requêtes du webhook`metadata`objectNonDonnées personnalisées incluses dans toutes les charges utiles du webhook`events`arrayNonTypes d’événements à recevoir (par défaut : tous les événements)

## Utilisation

### Exploration avec webhook

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

### Scrape par lots avec webhook

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

## Expirations & Réessais

Votre endpoint doit répondre avec un statut `2xx` en **10 secondes** maximum. Si la livraison échoue (expiration, statut non-2xx ou erreur réseau), Firecrawl réessaie automatiquement :

RéessaiDélai après l’échec1er1 minute2e5 minutes3e15 minutes

Après 3 réessais infructueux, le webhook est marqué comme échoué et aucune autre tentative n’est effectuée.