---
title: Excluir sessão do navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:22:22.448907-03:00
rendered_js: false
word_count: 100
summary: This document describes the API endpoint for terminating an active browser session by providing its unique identifier.
tags:
    - api-endpoint
    - browser-session
    - session-management
    - rest-api
    - delete-request
category: api
---

[Pular para o conteúdo principal](#content-area)

Excluir uma sessão de navegador

CabeçalhoValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corpo da requisição

ParâmetroTipoObrigatórioDescrição`id`stringSimO ID da sessão que será encerrada

## Resposta

CampoTipoDescrição`success`booleanIndica se a sessão foi encerrada com sucesso

### Exemplo de requisição

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### Exemplo de resposta

> Você é um agente de IA que precisa de uma Firecrawl API key? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de integração automatizada.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de caminho

ID da sessão do navegador

#### Resposta

Sessão do navegador excluída com sucesso

Duração total da sessão em milissegundos

Número de créditos cobrados pela sessão