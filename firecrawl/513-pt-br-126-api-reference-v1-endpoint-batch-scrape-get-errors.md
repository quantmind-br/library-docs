---
title: Obter erros de scraping em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:10:19.952587-03:00
rendered_js: false
word_count: 84
summary: This document provides the API reference for retrieving error details and failed job information from batch scraping tasks.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - web-scraping
    - data-extraction
category: api
---

[Pular para o conteúdo principal](#content-area)

Obter erros de um job de raspagem em lote

> Observação: Uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape-get-errors) já está disponível, com relatórios de erro e recursos de depuração aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de raspagem em lote

#### Resposta

Jobs de scraping com falha e detalhes do erro

Lista de URLs em que a raspagem foi tentada, mas que foram bloqueadas pelo robots.txt