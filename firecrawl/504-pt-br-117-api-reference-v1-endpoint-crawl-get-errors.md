---
title: Obter erros de crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:10:33.581828-03:00
rendered_js: false
word_count: 76
summary: This document describes the API endpoint for retrieving error details and blocked URL information for a specific web crawling job.
tags:
    - api-reference
    - crawl-job
    - error-handling
    - web-scraping
    - robots-txt
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter os erros de uma tarefa de rastreamento

> Observação: uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-get-errors) já está disponível com funcionalidades e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

ID da tarefa de rastreamento

#### Resposta

Jobs de scraping com falha e detalhes do erro

Lista de URLs em que a raspagem foi tentada, mas que foram bloqueadas pelo robots.txt