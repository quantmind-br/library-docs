---
title: Cancelar crawl - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:11:35.993547-03:00
rendered_js: false
word_count: 70
summary: This document provides the API endpoint and authentication requirements for cancelling an active web crawling task via the Firecrawl service.
tags:
    - api-endpoint
    - web-crawling
    - task-management
    - rest-api
    - authentication
category: api
---

[Pular para o conteúdo principal](#content-area)

Cancelar uma tarefa de rastreamento

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

Cancelar uma tarefa de rastreamento

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

O ID da tarefa de rastreamento

#### Resposta

Cancelamento realizado com sucesso

Opções disponíveis:

`cancelled`