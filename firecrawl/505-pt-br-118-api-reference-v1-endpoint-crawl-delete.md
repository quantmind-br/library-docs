---
title: Cancelar Crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:10:34.428029-03:00
rendered_js: false
word_count: 62
summary: This document provides instructions on how to cancel a specific web scraping or crawling task using the Firecrawl API.
tags:
    - api-reference
    - crawl-task
    - data-scraping
    - http-delete
    - authorization
category: api
---

[Pular para o conteúdo principal](#content-area)

Cancelar uma tarefa de rastreamento

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

Cancelar uma tarefa de rastreamento

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Nota: Uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-delete) já está disponível, com recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de rastreamento

#### Resposta

Cancelamento concluído com sucesso

Opções disponíveis:

`cancelled`