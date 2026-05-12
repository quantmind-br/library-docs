---
title: Uso histórico de tokens - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:17:35.493156-03:00
rendered_js: false
word_count: 90
summary: This document describes the API endpoint used to retrieve historical token usage data for an authenticated team, with an optional breakdown by API key.
tags:
    - api-documentation
    - token-usage
    - billing-history
    - analytics
    - api-key-management
category: api
---

Obtén el historial de uso de tokens para el equipo autenticado (solo Extract)

Devuelve el uso histórico de tokens por mes. Este endpoint también puede desglosar el uso por clave de API de forma opcional.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de consulta

byApiKey

boolean

predeterminado:false

Obtener el historial de uso de tokens por clave de API

#### Respuesta