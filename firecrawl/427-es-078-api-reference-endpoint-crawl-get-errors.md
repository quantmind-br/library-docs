---
title: Obtener errores del rastreo - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:17:44.148113-03:00
rendered_js: false
word_count: 80
summary: This document provides the API specification for retrieving error logs and failed URL attempts associated with a specific crawl job.
tags:
    - api-reference
    - crawl-job
    - error-handling
    - web-scraping
    - api-authentication
category: api
---

[Saltar al contenido principal](#content-area)

Obtener los errores de una tarea de rastreo

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

ID del trabajo de rastreo

#### Respuesta

Tareas de scraping con errores y detalles de los errores

Lista de URL que se intentó scrapear pero fueron bloqueadas por robots.txt