---
title: Tipos de eventos de webhook | Firecrawl
url: https://docs.firecrawl.dev/es/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:10.270516-03:00
rendered_js: false
word_count: 403
summary: This document provides a technical reference for webhook event types and their payload structures, covering scraping, batch operations, data extraction, and agent activity.
tags:
    - webhooks
    - api-reference
    - data-scraping
    - event-driven
    - webhook-payloads
category: reference
---

## Referencia rápida

EventoActivador`crawl.started`El trabajo de rastreo comienza a procesarse`crawl.page`Se extrae una página durante un rastreo`crawl.completed`El trabajo de rastreo finaliza y todas las páginas se han procesado`batch_scrape.started`El trabajo de extracción por lotes comienza a procesarse`batch_scrape.page`Se extrae una URL durante una extracción por lotes`batch_scrape.completed`Todas las URL del lote se han procesado`extract.started`El trabajo de extracción comienza a procesarse`extract.completed`La extracción finaliza correctamente`extract.failed`La extracción falla`agent.started`El trabajo de agente comienza a procesarse`agent.action`El agente ejecuta una herramienta (scrape, search, etc.)`agent.completed`El agente finaliza correctamente`agent.failed`El agente se encuentra con un error`agent.cancelled`El trabajo de agente es cancelado por el usuario

## Estructura del payload

Todos los eventos de webhook comparten esta estructura:

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

FieldTypeDescription`success`booleanIndica si la operación se completó correctamente`type`stringTipo de evento (por ejemplo, `crawl.page`)`id`stringID del trabajo`data`arrayDatos específicos del evento (consulta los ejemplos más abajo)`metadata`objectMetadatos personalizados de tu configuración de webhook`error`stringMensaje de error (cuando `success` es `false`)

## Eventos de rastreo

### `crawl.started`

Se envía cuando la tarea de rastreo comienza a procesarse.

```
{
  "success": true,
  "type": "rastreo.iniciado",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

Se envía por cada página que se extrae. El arreglo `data` contiene el contenido de la página y sus metadatos.

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
        "description": "Descripción de la página",
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

Se envía cuando el trabajo de rastreo finaliza y todas las páginas han sido procesadas.

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## Eventos de scraping por lotes

### `batch_scrape.started`

Se envía cuando comienza una operación de scraping por lotes.

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

Se envía por cada URL individual que se extrae. El arreglo `data` contiene el contenido de la página y sus metadatos.

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
        "description": "Descripción de la página",
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

Se envía cuando se han procesado todas las URL del lote.

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Se envía cuando el trabajo de extracción comienza a ejecutarse.

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

Se envía cuando una operación de extracción se completa correctamente. El array `data` contiene los datos extraídos y la información de uso.

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Sitio de ejemplo", "category": "Tecnología" },
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

Se envía cuando falla la extracción. El campo `error` contiene el motivo del error.

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "No se pudieron extraer los datos: se superó el tiempo de espera",
  "metadata": {}
}
```

## Eventos del agente

### `agent.started`

Se envía cuando el trabajo del agente comienza su procesamiento.

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

Se envía tras cada ejecución de una herramienta (`scrape`, `search`, etc.).

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

Se envía cuando el agente finaliza correctamente. El array `data` contiene los datos extraídos y el total de créditos utilizados.

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

Se envía cuando el agente se encuentra con un error. El campo `error` contiene el motivo del fallo.

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
  "error": "Créditos máximos excedidos",
  "metadata": {}
}
```

### `agent.cancelled`

Se envía cuando el usuario cancela la tarea del agente.

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

## Filtrado de eventos

De forma predeterminada, recibes todos los eventos. Para suscribirte solo a eventos específicos, usa el array `events` en la configuración de tu webhook:

```
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```

Esto es útil si solo te interesa que el trabajo se complete y no necesitas actualizaciones por página.