---
title: Uso histórico de créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/es/api-reference/endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:17:43.469504-03:00
rendered_js: false
word_count: 89
summary: This document describes an API endpoint for retrieving monthly credit usage history for the authenticated team, with an optional breakdown by API key.
tags:
    - api-documentation
    - credit-usage
    - billing-history
    - authentication
    - api-keys
category: api
---

Obtén el historial de uso de créditos del equipo autenticado

Devuelve el uso histórico de créditos mes a mes. El punto de conexión también puede desglosar el uso por clave de API, de forma opcional.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.

#### Autorizaciones

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parámetros de consulta

byApiKey

boolean

predeterminado:false

Obtener el historial de uso de créditos por clave de API

#### Respuesta