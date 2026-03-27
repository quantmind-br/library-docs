---
title: Listar sessões de navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:22:08.790102-03:00
rendered_js: false
word_count: 149
summary: This document provides the API specification for retrieving a list of browser sessions, including filter parameters and response object details.
tags:
    - api-reference
    - browser-sessions
    - web-scraping
    - cdp-integration
    - firecrawl
category: api
---

[Pular para o conteúdo principal](#content-area)

Listar sessões de navegador

CabeçalhoValor`Authorization``Bearer <API_KEY>`

## Parâmetros de query

ParâmetroTipoObrigatórioDescrição`status`stringNãoFiltra pelo status da sessão: `"active"` ou `"destroyed"`

## Resposta

CampoTipoDescrição`success`booleanIndica se a requisição foi bem-sucedida`sessions`arrayLista de objetos de sessão

### Objeto de sessão

CampoTipoDescrição`id`stringIdentificador único da sessão`status`stringStatus atual da sessão (`"active"` ou `"destroyed"`)`cdpUrl`stringURL de WebSocket para conexões CDP`liveViewUrl`stringURL para assistir à sessão em tempo real`interactiveLiveViewUrl`stringURL para interagir com a sessão em tempo real (clicar, digitar, rolar)`createdAt`stringCarimbo de data e hora ISO 8601 da criação da sessão`lastActivity`stringCarimbo de data e hora ISO 8601 da última atividade

### Exemplo de requisição

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### Exemplo de resposta

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver instruções de integração automatizada.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Parâmetros de consulta

Filtrar sessões por status

Opções disponíveis:

`active`,

`destroyed`

#### Resposta

Lista de sessões do navegador