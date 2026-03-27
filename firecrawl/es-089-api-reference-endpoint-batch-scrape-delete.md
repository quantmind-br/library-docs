---
title: Cancelar extracción en lote - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:18:03.2313-03:00
rendered_js: false
word_count: 71
summary: This document provides the API endpoint and authentication requirements for cancelling a pending or active batch web scraping job in Firecrawl.
tags:
    - api-reference
    - batch-scraping
    - job-cancellation
    - firecrawl-api
    - web-scraping
category: api
---

[Saltar al contenido principal](#content-area)

Cancelar un trabajo de rastreo por lotes

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancelar un trabajo de rastreo por lotes

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> ¿Eres un agente de IA que necesita una API key de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El identificador del trabajo de scraping por lotes

#### Respuesta

Ejemplo:

`"Batch scrape job successfully cancelled."`