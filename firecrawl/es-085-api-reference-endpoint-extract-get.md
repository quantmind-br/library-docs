---
title: Obtener el estado de extracción - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:17:55.297989-03:00
rendered_js: false
word_count: 88
summary: This document provides the API specification for retrieving the status and usage metrics of an extraction job using a Bearer token for authentication.
tags:
    - api-reference
    - extraction-job
    - status-check
    - token-usage
    - authentication
category: api
---

[Saltar al contenido principal](#content-area)

Obtén el estado de un trabajo de extracción

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID del trabajo de extracción

#### Respuesta

Estado actual del trabajo de extracción

Opciones disponibles:

`completed`,

`processing`,

`failed`,

`cancelled`

Número de tokens usados por la tarea de extracción. Solo disponible si la tarea se ha completado.