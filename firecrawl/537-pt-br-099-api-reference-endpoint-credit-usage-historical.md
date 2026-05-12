---
title: Uso histórico de créditos - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/credit-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:11:33.214136-03:00
rendered_js: false
word_count: 83
summary: This document describes an API endpoint used to retrieve the monthly historical credit usage for an authenticated team, with an optional breakdown by API key.
tags:
    - credit-usage
    - api-documentation
    - billing-history
    - authentication
    - api-analytics
category: api
---

Obtém o histórico de uso de créditos da equipe autenticada

Retorna o uso histórico de créditos mês a mês. O endpoint também pode, opcionalmente, detalhar o uso por chave de API.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções automatizadas de onboarding.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de consulta

Obter histórico de uso de créditos por chave de API

#### Resposta