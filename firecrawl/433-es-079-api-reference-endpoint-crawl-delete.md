---
title: Cancelar rastreo - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:17:43.456219-03:00
rendered_js: false
word_count: 65
summary: This document provides the API endpoint and authorization requirements for canceling an active web crawling task in Firecrawl.
tags:
    - api-reference
    - firecrawl
    - web-scraping
    - task-management
    - rest-api
    - crawling
category: api
---

[Saltar al contenido principal](#content-area)

Cancelar un proceso de rastreo

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

Cancelar un proceso de rastreo

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea de rastreo

#### Respuesta

Opciones disponibles:

`cancelled`