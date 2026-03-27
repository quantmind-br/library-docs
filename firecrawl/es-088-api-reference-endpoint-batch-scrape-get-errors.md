---
title: Obtener errores de raspado por lotes - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:18:06.395918-03:00
rendered_js: false
word_count: 86
summary: This document describes the API endpoint and authentication requirements for retrieving error logs and failed URL details from a batch scraping job.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - web-scraping
    - http-authentication
category: api
---

[Saltar al contenido principal](#content-area)

Obtener los errores de un trabajo de scraping por lotes

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea de scraping por lotes

#### Respuesta

Tareas de scraping con errores y detalles de los errores

Lista de URL que se intentó scrapear pero fueron bloqueadas por robots.txt