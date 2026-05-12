---
title: Obtener errores de Batch Scrape - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:16:26.230677-03:00
rendered_js: false
word_count: 81
summary: This document provides the technical requirements and response structure for retrieving error details from a batch scraping job via the API.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - web-crawling
    - http-authentication
category: api
---

[Saltar al contenido principal](#content-area)

Obtener los errores de un trabajo de rastreo por lotes

> Nota: Ya está disponible una nueva [versión v2 de esta API](https://docs.firecrawl.dev/es/api-reference/endpoint/batch-scrape-get-errors) con informes de errores y funciones de depuración mejoradas.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID del trabajo de scraping por lotes

#### Respuesta

Tareas de scraping con errores y detalles asociados

Lista de URLs que se intentaron rastrear pero fueron bloqueadas por robots.txt