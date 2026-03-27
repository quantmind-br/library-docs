---
title: Obtener errores de rastreo - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:16:38.140461-03:00
rendered_js: false
word_count: 78
summary: This document describes the API endpoint used to retrieve specific error logs and robots.txt block information for a completed web crawling job.
tags:
    - firecrawl
    - api-reference
    - web-scraping
    - error-logs
    - crawl-job
    - data-retrieval
category: api
---

Obtener los errores de un trabajo de rastreo

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

Obtener los errores de un trabajo de rastreo

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-get-errors), con funcionalidades y rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea de rastreo

#### Respuesta

Tareas de scraping con errores y detalles asociados

Lista de URLs que se intentaron rastrear pero fueron bloqueadas por robots.txt