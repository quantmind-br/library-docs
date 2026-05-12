---
title: Obtener el estado del agente - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:18:03.751972-03:00
rendered_js: false
word_count: 100
summary: This document outlines the API endpoint and requirements for retrieving the current status and results of an AI agent task.
tags:
    - api-documentation
    - agent-tasks
    - status-retrieval
    - bearer-authentication
    - firecrawl
category: api
---

[Saltar al contenido principal](#content-area)

Obtener el estado de una tarea de agente

> ¿Eres un agente de IA que necesita una API key de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automática.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de ruta

El ID de la tarea del agente

#### Respuesta

Opciones disponibles:

`processing`,

`completed`,

`failed`

Los datos extraídos (solo disponibles cuando el estado es "completed")

model

enum&lt;string&gt;

predeterminado:spark-1-pro

Configuración predefinida del modelo utilizada en la ejecución del agente

Opciones disponibles:

`spark-1-pro`,

`spark-1-mini`

Mensaje de error (solo presente cuando el estado es `failed`)