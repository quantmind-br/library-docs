---
title: Cancelar agente - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/agent-delete
source: sitemap
fetched_at: 2026-03-23T07:11:54.77604-03:00
rendered_js: false
word_count: 61
summary: This document provides the API endpoint and authorization requirements for canceling an active agent job in the Firecrawl system.
tags:
    - api-endpoint
    - agent-management
    - cancellation
    - firecrawl-api
    - rest-api
    - job-control
category: api
---

[Pular para o conteúdo principal](#content-area)

Cancelar uma tarefa de agente

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

Cancelar uma tarefa de agente

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/agent/{jobId} \
  --header 'Authorization: Bearer <token>'
```

> Você é um agente de IA que precisa de uma API key do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções automatizadas de onboarding.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

#### Resposta

Job do agente cancelado com sucesso