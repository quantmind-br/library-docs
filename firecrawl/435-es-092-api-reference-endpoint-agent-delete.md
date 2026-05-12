---
title: Cancelar agente - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:17:58.661536-03:00
rendered_js: false
word_count: 66
summary: This document provides the API endpoint and authentication requirements for cancelling an active agent task in Firecrawl.
tags:
    - api-reference
    - agent-task
    - cancellation
    - rest-api
    - firecrawl
category: api
---

[Saltar al contenido principal](#content-area)

Cancelar una tarea del agente

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

Cancelar una tarea del agente

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea del agente

#### Respuesta

Tarea del agente cancelada correctamente