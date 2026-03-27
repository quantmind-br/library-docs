---
title: Criar sessão de navegador - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:22:21.537787-03:00
rendered_js: false
word_count: 291
summary: This document provides the API specifications for creating and managing browser sessions, including configuration parameters for session duration, inactivity timeouts, and persistent storage profiles.
tags:
    - api-reference
    - browser-session
    - web-automation
    - cdp-protocol
    - firecrawl-api
category: api
---

[Pular para o conteúdo principal](#content-area)

Criar uma sessão de navegador

CabeçalhoValor`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## Corpo da Requisição

ParâmetroTipoObrigatórioPadrãoDescrição`ttl`numberNão600Tempo de vida total da sessão, em segundos (30-3600)`activityTtl`numberNão300Número de segundos de inatividade antes que a sessão seja destruída (10-3600)`profile`objectNão—Habilita armazenamento persistente entre sessões. Veja abaixo.`profile.name`stringSim\*—Nome do perfil (1-128 caracteres). Sessões com o mesmo nome compartilham o armazenamento.`profile.saveChanges`booleanNão`true`Quando `true`, o estado do navegador é salvo de volta no perfil ao fechar. Defina como `false` para carregar dados existentes sem gravar. Apenas um salvamento é permitido por vez.

## Resposta

CampoTipoDescrição`success`booleanIndica se a sessão foi criada`id`stringIdentificador único da sessão`cdpUrl`stringURL WebSocket para conexões CDP`liveViewUrl`stringURL para assistir à sessão em tempo real`interactiveLiveViewUrl`stringURL para interagir com a sessão em tempo real (clicar, digitar, rolar)`expiresAt`stringQuando a sessão expira com base no TTL

### Exemplo de requisição

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### Resposta de exemplo

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de onboarding automatizado.

#### Autorizações

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Corpo

Tempo de vida máximo, em segundos, da sessão de navegador

Intervalo obrigatório: `30 <= x <= 3600`

Tempo, em segundos, antes de a sessão ser encerrada por inatividade

Intervalo obrigatório: `10 <= x <= 3600`

Indica se uma visualização ao vivo do navegador deve ser transmitida

Ativar o armazenamento persistente entre sessões do navegador. Dados salvos em uma sessão podem ser carregados em outra sessão posteriormente usando o mesmo nome.

#### Resposta

Sessão de navegador criada com sucesso

Identificador exclusivo da sessão

URL de WebSocket para acesso ao Chrome DevTools Protocol

URL para visualizar a sessão do navegador em tempo real

URL para interagir em tempo real com a sessão do navegador (clicar, digitar, rolar)

Momento em que a sessão irá expirar, com base no TTL