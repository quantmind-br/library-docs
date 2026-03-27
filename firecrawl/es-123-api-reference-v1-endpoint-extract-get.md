---
title: Obtener estado de extracción - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:16:10.574246-03:00
rendered_js: false
word_count: 74
summary: This document provides the API reference for retrieving the status and details of a specific data extraction task.
tags:
    - api-reference
    - data-extraction
    - status-check
    - firecrawl-api
    - rest-api
category: api
---

[Saltar al contenido principal](#content-area)

Consultar el estado de una tarea de extracción

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

Consultar el estado de una tarea de extracción

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/extract-get) con funciones y rendimiento mejorados.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID del trabajo de extracción

#### Respuesta

El estado actual del trabajo de extracción

Opciones disponibles:

`completed`,

`processing`,

`failed`,

`cancelled`