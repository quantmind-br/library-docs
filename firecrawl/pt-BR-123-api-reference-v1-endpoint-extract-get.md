---
title: Obter status da extração - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:10:13.100154-03:00
rendered_js: false
word_count: 68
summary: This document describes the API endpoint used to retrieve the current status and results of a specific data extraction task.
tags:
    - api-endpoint
    - data-extraction
    - task-status
    - authentication
    - firecrawl-api
category: api
---

Obter o status de uma tarefa de extração

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

Obter o status de uma tarefa de extração

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> Observação: Uma nova [versão v2 desta API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/extract-get) já está disponível, com recursos e desempenho aprimorados.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de extração

#### Resposta

Status atual do processo de extração

Opções disponíveis:

`completed`,

`processing`,

`failed`,

`cancelled`