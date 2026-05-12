---
title: Estado de la cola - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:16:27.996694-03:00
rendered_js: false
word_count: 84
summary: This document describes the API endpoint for retrieving real-time metrics regarding a team's scraping queue, including active, pending, and total job counts.
tags:
    - scraping-metrics
    - queue-status
    - api-documentation
    - bearer-authentication
    - job-monitoring
category: api
---

[Saltar al contenido principal](#content-area)

Métricas sobre la cola de scraping de tu equipo

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/queue-status) con nuevas funciones y mejor rendimiento.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Respuesta

Número de trabajos que hay actualmente en tu cola

Número de trabajos activos en este momento

Número de tareas en espera actualmente

Número máximo de tareas activas simultáneas según tu plan

Marca de tiempo del último trabajo exitoso