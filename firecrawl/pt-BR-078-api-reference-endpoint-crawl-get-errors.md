---
title: Obter erros do crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:11:38.58968-03:00
rendered_js: false
word_count: 81
summary: This document provides the API specification for retrieving error information and blocked URL details from a specific Firecrawl scraping job.
tags:
    - api-reference
    - firecrawl
    - scraping
    - error-handling
    - robots-txt
    - web-crawling
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter erros de um job de rastreamento

> Você é um agente de IA que precisa de uma chave de API da Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver as instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de rastreamento

#### Resposta

Jobs de scraping com falha e detalhes do erro

Lista de URLs cuja raspagem foi tentada, mas bloqueada pelo robots.txt