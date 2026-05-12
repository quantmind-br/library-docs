---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/es/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:38:56.734256-03:00
rendered_js: false
word_count: 150
summary: This document explains how to configure and use webhooks to receive real-time status notifications for scraping and extraction operations.
tags:
    - webhooks
    - api-integration
    - real-time-notifications
    - data-scraping
    - event-driven
    - web-automation
category: configuration
---

Los webhooks te permiten recibir notificaciones en tiempo real a medida que avanzan tus operaciones, en lugar de consultar periódicamente su estado.

## Operaciones admitidas

OperaciónEventosCrawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## Configuración

Añade un objeto `webhook` a tu solicitud:

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["iniciado", "página", "completado", "error"]
  }
}
```

CampoTipoRequeridoDescripción`url`stringSíLa URL de tu endpoint (HTTPS)`headers`objectNoEncabezados personalizados para incluir en las solicitudes del webhook`metadata`objectNoDatos personalizados incluidos en las cargas del webhook`events`arrayNoTipos de eventos a recibir (por defecto: todos los eventos)

## Uso

### Rastreo con webhook

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://tu-dominio.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Raspado en lote con webhook

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

## Tiempos de espera y reintentos

Tu endpoint debe responder con un estado `2xx` en un plazo de **10 segundos**. Si la entrega falla (se excede el tiempo de espera, el estado no es 2xx o hay un error de red), Firecrawl reintenta automáticamente:

ReintentoRetraso después del fallo1.º1 minuto2.º5 minutos3.º15 minutos

Después de 3 reintentos fallidos, el webhook se marca como fallido y no se realizan más intentos.