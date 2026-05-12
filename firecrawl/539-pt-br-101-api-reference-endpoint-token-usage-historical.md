---
title: Uso Histórico de Tokens - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:11:25.75465-03:00
rendered_js: false
word_count: 84
summary: This document describes an API endpoint for retrieving historical monthly token usage for an authenticated team, with the option to filter by specific API keys.
tags:
    - api-endpoint
    - token-usage
    - historical-data
    - authentication
    - billing-metrics
    - analytics
category: api
---

Obter o uso histórico de tokens da equipe autenticada (somente Extract)

Retorna o uso histórico de tokens mês a mês. O endpoint também pode, opcionalmente, detalhar o uso por chave de API.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de consulta

Obtenha o histórico de uso de tokens por chave de API

#### Resposta