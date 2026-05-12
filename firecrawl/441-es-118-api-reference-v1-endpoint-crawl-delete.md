---
title: Cancelar rastreo - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:16:29.774129-03:00
rendered_js: false
word_count: 59
summary: This document provides the API endpoint reference for cancelling an active web crawling job using an authentication token and job identifier.
tags:
    - api-endpoint
    - web-crawling
    - job-management
    - rest-api
    - authentication
    - firecrawl
category: api
---

[Saltar al contenido principal](#content-area)

Cancelar un trabajo de rastreo

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

Cancelar un trabajo de rastreo

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-delete) con funcionalidades y rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea de rastreo

#### Respuesta

Opciones disponibles:

`cancelled`