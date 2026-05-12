---
title: Cancelar scraping em lote - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:10:27.12155-03:00
rendered_js: false
word_count: 70
summary: This document provides the API endpoint and authorization requirements for canceling an active batch scraping job.
tags:
    - api-endpoint
    - batch-scraping
    - task-cancellation
    - web-scraping
    - rest-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Cancelar uma tarefa de raspagem em lote

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

Cancelar uma tarefa de raspagem em lote

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Observação: uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/batch-scrape-delete) está disponível com recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de raspagem em lote

#### Resposta

Cancelamento concluído com sucesso

Exemplo:

`"Batch scrape job successfully cancelled."`