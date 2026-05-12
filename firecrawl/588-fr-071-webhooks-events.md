---
title: Types d’événements de webhook | Firecrawl
url: https://docs.firecrawl.dev/fr/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:14.046776-03:00
rendered_js: false
word_count: 382
summary: This document provides a technical reference for webhook event types, payload structures, and event filtering mechanisms for crawling, batch scraping, and agent-based tasks.
tags:
    - webhooks
    - api-reference
    - data-scraping
    - event-notifications
    - crawling
    - web-automation
category: reference
---

## Référence rapide

ÉvénementDéclencheur`crawl.started`La tâche de crawl commence son traitement`crawl.page`Une page est extraite pendant un crawl`crawl.completed`La tâche de crawl se termine et toutes les pages ont été traitées`batch_scrape.started`La tâche d’extraction par lot commence son traitement`batch_scrape.page`Une URL est extraite pendant une extraction par lot`batch_scrape.completed`Toutes les URL du lot ont été traitées`extract.started`La tâche d’extraction commence son traitement`extract.completed`L’extraction se termine avec succès`extract.failed`L’extraction échoue`agent.started`La tâche de l’agent commence son traitement`agent.action`L’agent exécute un outil (scrape, search, etc.)`agent.completed`L’agent se termine avec succès`agent.failed`L’agent rencontre une erreur`agent.cancelled`La tâche de l’agent est annulée par l’utilisateur

## Structure du payload

Tous les événements webhook ont la même structure :

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

ChampTypeDescription`success`booleanIndique si l’opération a réussi`type`stringType d’événement (par exemple `crawl.page`)`id`stringID de la tâche`data`arrayDonnées spécifiques à l’événement (voir exemples ci-dessous)`metadata`objectMétadonnées personnalisées de la configuration de votre webhook`error`stringMessage d’erreur (lorsque `success` est `false`)

## Événements de crawl

### `crawl.started`

Envoyé lorsque la tâche de crawl commence son traitement.

```
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Envoyé pour chaque page extraite. Le tableau `data` contient le contenu de la page et ses métadonnées.

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "Description de la page",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `crawl.completed`

Envoyé lorsque la tâche de crawl est terminée et que toutes les pages ont été traitées.

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Événements de scraping par lot

### `batch_scrape.started`

Envoyé lorsque la tâche d’extraction par lots commence son traitement.

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

Envoyé pour chaque URL individuelle extraite. Le tableau `data` contient le contenu de la page et ses métadonnées.

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "Page description",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `batch_scrape.completed`

Envoyé lorsque toutes les URL du lot ont été traitées.

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Envoyé lorsque la tâche d’extraction commence à être traitée.

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Envoyé lorsqu’une opération d’extraction s’achève avec succès. Le tableau `data` contient les données extraites et les informations d’utilisation.

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Site exemple", "category": "Technologie" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

Envoyé lorsqu’une extraction échoue. Le champ `error` contient la raison de l’échec.

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "Échec de l'extraction des données : délai d'attente dépassé",
  "metadata": {}
}
```

## Événements de l’agent

### `agent.started`

Envoyé lorsque la tâche de l’agent commence à être traitée.

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `agent.action`

Envoyé après chaque exécution d’un outil (scrape, search, etc.).

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "mcp__tools__scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```

### `agent.completed`

Envoyé lorsque l’agent a terminé avec succès. Le tableau `data` contient les données extraites et le total des crédits consommés.

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "Example Corp",
        "industry": "Technology",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```

### `agent.failed`

Envoyé lorsque l’agent rencontre une erreur. Le champ `error` contient le motif de l’échec.

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "Crédits maximum dépassés",
  "metadata": {}
}
```

### `agent.cancelled`

Envoyé lorsque la tâche de l’agent est annulée par l’utilisateur.

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

## Filtrage des événements

Par défaut, vous recevez tous les événements. Pour vous abonner uniquement à certains événements, indiquez un tableau `events` dans la configuration de votre webhook :

```
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```

C’est utile si vous vous intéressez uniquement à l’achèvement de la tâche et n’avez pas besoin de mises à jour pour chaque page.