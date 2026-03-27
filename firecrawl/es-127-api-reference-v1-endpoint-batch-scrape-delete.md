---
title: Cancelar Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:17:07.719775-03:00
rendered_js: false
word_count: 68
summary: This document provides the API endpoint and authentication requirements for cancelling a pending or active batch scrape job.
tags:
    - api-reference
    - batch-scraping
    - job-cancellation
    - rest-api
category: api
---

[Saltar al contenido principal](#content-area)

Cancelar una tarea de extracción por lotes

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancelar una tarea de extracción por lotes

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-delete), con más funciones y mejor rendimiento.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID del trabajo de scraping por lotes

#### Respuesta

Ejemplo:

`"Batch scrape job successfully cancelled."`