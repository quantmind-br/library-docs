---
title: Status da Fila - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/queue-status
source: sitemap
fetched_at: 2026-03-23T07:10:15.373186-03:00
rendered_js: false
word_count: 82
summary: This document provides the API specification for retrieving current scraping queue metrics and job status information.
tags:
    - api-reference
    - scraping-queue
    - job-monitoring
    - data-extraction
    - bearer-authentication
category: api
---

[Pular para o conteúdo principal](#content-area)

Métricas da fila de scraping da sua equipe

> Observação: uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/queue-status) agora está disponível com recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Resposta

Número de jobs atualmente na sua fila

Número de jobs ativos atualmente

Número de jobs aguardando no momento

Número máximo de jobs ativos em execução simultânea, de acordo com o seu plano

Timestamp do job mais recente bem-sucedido