---
title: Estado de la cola - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:17:22.208383-03:00
rendered_js: false
word_count: 88
summary: This document outlines the API endpoints and authentication requirements for retrieving real-time metrics regarding an organization's web scraping queue.
tags:
    - api-reference
    - scraping-metrics
    - queue-status
    - bearer-authentication
    - job-monitoring
category: api
---

Métricas de la cola de rastreo de tu equipo

Métricas sobre la cola de scraping del equipo.

> ¿Eres un agente de IA que necesita una API key de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Respuesta

Número de trabajos en tu cola actualmente

Número de trabajos activos actualmente

Número de trabajos en espera

Número máximo de trabajos activos simultáneos según tu plan

Marca de tiempo del trabajo exitoso más reciente