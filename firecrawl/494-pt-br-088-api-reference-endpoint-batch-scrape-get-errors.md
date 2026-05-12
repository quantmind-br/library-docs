---
title: Obter erros de scraping em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:12:02.622222-03:00
rendered_js: false
word_count: 84
summary: This document provides the API specification for retrieving error information and blocked URL details from a batch scraping job.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - web-scraping
    - firecrawl-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter os erros de uma tarefa de raspagem em lote

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de integração automatizada.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de raspagem em lote

#### Resposta

Jobs de scraping com falha e detalhes do erro

Lista de URLs cuja raspagem foi tentada, mas bloqueada pelo robots.txt