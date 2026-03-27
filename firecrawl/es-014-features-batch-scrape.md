---
title: Raspado en lote | Firecrawl
url: https://docs.firecrawl.dev/es/features/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:25:36.740868-03:00
rendered_js: false
word_count: 532
summary: This document explains how to perform batch scraping in Firecrawl, allowing for the concurrent processing of multiple URLs using either synchronous or asynchronous methods with support for webhooks and structured data extraction.
tags:
    - batch-scraping
    - webhooks
    - concurrent-processing
    - api-integration
    - data-extraction
    - firecrawl
category: guide
---

El raspado en lote permite raspar múltiples URL en un solo trabajo. Pasa una lista de URL y parámetros opcionales, y Firecrawl las procesa de forma concurrente y devuelve todos los resultados de una sola vez.

- Funciona como `/crawl` pero para una lista explícita de URL
- Modos síncrono y asíncrono
- Compatible con todas las opciones de raspado, incluida la extracción estructurada
- Concurrencia configurable por trabajo

## Cómo funciona

Puedes ejecutar un scrape por lotes de dos maneras:

ModoMétodo del SDK (JS / Python)ComportamientoSíncrono`batchScrape` / `batch_scrape`Inicia el lote y espera a que finalice, devolviendo todos los resultadosAsíncrono`startBatchScrape` / `start_batch_scrape`Inicia el lote y devuelve un ID de trabajo para polling o webhooks

## Uso básico

### Respuesta

Invocar `batchScrape` / `batch_scrape` devuelve los resultados completos cuando el lote finaliza.

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
      "markdown": "[Página principal de la documentación de Firecrawl![logotipo claro](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Crea un «chat con el sitio web» usando Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Aprende a usar Firecrawl, Groq Llama 3 y LangChain para crear un bot de «chat con tu sitio web»."
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

Invocar `startBatchScrape` / `start_batch_scrape` devuelve un ID de tarea que puedes monitorear mediante `getBatchScrapeStatus` / `get_batch_scrape_status`, el endpoint de la API `/batch/scrape/{id}` o webhooks. Los resultados de la tarea están disponibles a través de la API durante 24 horas después de su finalización. Después de este período, aún puedes ver el historial y los resultados de tus ejecuciones de batch scrape en los [activity logs](https://www.firecrawl.dev/app/logs).

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Concurrencia

De forma predeterminada, un trabajo de extracción por lotes usa todo el límite de navegadores concurrentes de tu equipo (consulta [Rate Limits](https://docs.firecrawl.dev/es/rate-limits)). Puedes reducir este valor por trabajo con el parámetro `maxConcurrency`. Por ejemplo, `maxConcurrency: 50` limita ese trabajo a 50 extracciones simultáneas. Establecer este valor demasiado bajo en lotes grandes ralentizará significativamente el procesamiento, así que solo redúcelo si necesitas dejar capacidad para otros trabajos concurrentes.

Puedes usar el raspado por lotes para extraer datos estructurados de cada página del lote. Esto es útil si quieres aplicar el mismo esquema a una lista de URL.

### Respuesta

`batchScrape` / `batch_scrape` devuelve resultados completos:

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
        "title": "Crea un ‘chat con el sitio web’ usando Groq Llama 3 | Firecrawl",
        "description": "Aprende a usar Firecrawl, Groq Llama 3 y LangChain para crear un bot de ‘chat con tu sitio web’."
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` devuelve un ID de tarea:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Webhooks

Puedes configurar webhooks para recibir notificaciones en tiempo real a medida que se rastrea cada URL de tu lote. Esto te permite procesar los resultados de inmediato en lugar de esperar a que finalice todo el lote.

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

### Tipos de eventos

EventoDescripción`batch_scrape.started`El proceso de scraping por lotes ha comenzado`batch_scrape.page`Se ha hecho scraping correctamente de una sola URL`batch_scrape.completed`Se han procesado todas las URL`batch_scrape.failed`Se produjo un error durante el scraping por lotes

### Carga útil

Cada entrega de webhook incluye un cuerpo JSON con la siguiente estructura:

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

### Verificación de firmas de webhooks

Cada solicitud de webhook de Firecrawl incluye un encabezado `X-Firecrawl-Signature` que contiene una firma HMAC-SHA256. Verifica siempre esta firma para asegurarte de que el webhook sea auténtico y no haya sido manipulado.

1. Obtén tu secreto de webhook en la [pestaña Advanced](https://www.firecrawl.dev/app/settings?tab=advanced) de la configuración de tu cuenta
2. Extrae la firma del encabezado `X-Firecrawl-Signature`
3. Calcula el HMAC-SHA256 del cuerpo sin procesar de la solicitud usando tu secreto
4. Compáralo con el encabezado de firma utilizando una función segura frente a ataques de temporización

Para ejemplos completos de implementación en JavaScript y Python, consulta la [documentación de seguridad de webhooks](https://docs.firecrawl.dev/es/webhooks/security). Para obtener una documentación completa sobre webhooks, incluidas cargas útiles de eventos detalladas, configuración avanzada y solución de problemas, consulta la [documentación de webhooks](https://docs.firecrawl.dev/es/webhooks/overview).

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.