---
title: Navegador | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/features/browser
source: sitemap
fetched_at: 2026-03-23T07:21:58.008839-03:00
rendered_js: false
word_count: 1013
summary: The Firecrawl Browser Sandbox provides a secure, managed environment for AI agents to perform complex web interactions like form submission and authentication without local infrastructure.
tags:
    - browser-automation
    - firecrawl
    - ai-agents
    - headless-browser
    - playwright
    - web-scraping
    - sandbox
category: guide
---

O Firecrawl Browser Sandbox oferece aos seus agentes um ambiente de navegador seguro onde eles podem interagir com a web. Preencha formulários, clique em botões, autentique-se e muito mais. Sem configuração local, sem instalações do Chromium, sem problemas de compatibilidade de driver. Agent browser e playwright vêm pré-instalados. Disponível via [API](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-create), [CLI](https://docs.firecrawl.dev/pt-BR/sdks/cli#browser) (Bash / agent-browser, Python, Node), [Node SDK](https://docs.firecrawl.dev/pt-BR/sdks/node#browser), [Python SDK](https://docs.firecrawl.dev/pt-BR/sdks/python#browser), [Vercel AI SDK](https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk) e [MCP Server](https://docs.firecrawl.dev/pt-BR/mcp-server). Para adicionar suporte de navegador a um agente de codificação com IA (Claude Code, Codex, Open Code, Cursor etc.), instale a skill do Firecrawl:

```
npx -y firecrawl-cli@latest init --all --browser
```

Cada sessão é executada em um sandbox isolado, descartável ou persistente, que escala sem gerenciar infraestrutura.

## Início rápido

Crie uma sessão, execute código e feche-a:

- **Sem instalação de drivers** - Sem binário do Chromium, sem `playwright install`, sem problemas de compatibilidade de drivers
- **Python, JavaScript e Bash** - Envie código via API, CLI ou SDK e receba os resultados de volta. As três linguagens são executadas remotamente no sandbox
- **agent-browser** - CLI pré-instalada com mais de 60 comandos. Agentes de IA escrevem comandos Bash simples em vez de código Playwright
- **Playwright carregado** - Playwright vem pré-instalado no sandbox. Agentes podem escrever código Playwright se preferirem.
- **Acesso ao CDP** - Conecte sua própria instância do Playwright via WebSocket quando precisar de controle total
- **Visualização em tempo real** - Assista às sessões em tempo real por meio de uma URL de transmissão incorporável
- **Visualização em tempo real interativa** - Permita que os usuários interajam diretamente com o navegador por meio de uma transmissão interativa incorporável

## Iniciar uma sessão

Retorna um ID de sessão, uma URL do CDP e uma URL de visualização em tempo real.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## Executar código

Execute código Python, JavaScript ou bash na sua sessão. O resultado é retornado via `stdout`; no Node.js, o valor da última expressão também fica disponível em `result`.

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### Como lidar com downloads de arquivos

Arquivos baixados dentro de uma sessão podem ser capturados e retornados em base64. Use a API de download do Playwright por meio do endpoint `execute`:

## agent-browser (Modo Bash)

[agent-browser](https://github.com/vercel-labs/agent-browser) é uma CLI de navegador headless pré-instalada em cada sandbox. Em vez de escrever código em Playwright, os agentes enviam comandos bash simples. A CLI injeta automaticamente `--cdp` para que o agent-browser se conecte automaticamente à sua sessão ativa.

### Forma abreviada

A maneira mais rápida de usar o browser. Tanto a forma abreviada quanto `execute` enviam comandos para o agent-browser automaticamente. A forma abreviada apenas ignora o `execute` e inicia uma sessão automaticamente, se necessário:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

A forma explícita usa `execute`. Os comandos são enviados automaticamente ao agent-browser — você não precisa digitar `agent-browser` nem usar `--bash`:

### API & SDK

Use `language: "bash"` para executar comandos do agent-browser por meio da API ou dos SDKs:

## Gerenciamento de sessões

### Sessões persistentes

Por padrão, cada sessão do navegador começa em um estado limpo. Com `profile`, você pode salvar e reutilizar o estado do navegador entre sessões. Isso é útil para permanecer logado e preservar preferências. Para salvar ou selecionar um perfil, use o parâmetro `profile` ao criar uma sessão.

ParâmetroPadrãoDescrição`name`—Um nome para o perfil persistente. Sessões com o mesmo nome compartilham o armazenamento.`saveChanges``true`Quando `true`, o estado do navegador é salvo de volta no perfil ao encerrar. Defina como `false` para carregar dados existentes sem gravar — útil quando você precisa de vários leitores simultâneos.

O estado da sessão do navegador só é salvo quando a sessão é encerrada. Portanto, recomendamos encerrar a sessão do navegador quando terminar de usá-la, para que ela possa ser reutilizada. Depois que uma sessão é encerrada, seu ID de sessão não é mais válido — você não pode reutilizá-lo. Em vez disso, crie uma nova sessão com o mesmo nome de perfil e use o novo ID de sessão retornado na resposta. Para salvar e encerrar:

### Listar sessões

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### Configuração de TTL

As sessões têm dois controles de TTL:

ParâmetroPadrãoDescrição`ttl`600s (10 min)Tempo máximo de duração da sessão (30-3600s)`activityTtl`300s (5 min)Encerramento automático após inatividade (10-3600s)

### Encerrar a sessão

## Visualização em tempo real

Toda sessão retorna uma `liveViewUrl` na resposta que você pode incorporar para acompanhar o navegador em tempo real. Útil para depuração, demonstrações ou para criar interfaces baseadas em navegador.

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### Visualização Interativa Ao Vivo

A resposta também inclui um `interactiveLiveViewUrl`. Diferente da visualização ao vivo padrão, que é apenas para consulta, a visualização interativa ao vivo permite que os usuários cliquem, digitem e interajam com a sessão do navegador diretamente por meio do streaming incorporado. Isso é útil para construir interfaces de navegador voltadas para o usuário final, depuração colaborativa ou qualquer cenário em que quem estiver visualizando precise controlar o navegador.

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## Conectando-se ao CDP

Cada sessão expõe uma URL de WebSocket do CDP. A API `execute` e a opção `--bash` cobrem a maioria dos casos de uso, mas, se você precisar de controle local total, pode se conectar diretamente.

## Quando usar o navegador

Caso de usoFerramenta certaExtrair conteúdo de uma URL conhecida[Scrape](https://docs.firecrawl.dev/pt-BR/features/scrape)Pesquisar na web e obter resultados[Search](https://docs.firecrawl.dev/pt-BR/features/search)Navegar por paginação, preencher formulários, clicar em fluxos**Browser**Fluxos de trabalho com várias etapas e interação**Browser**Navegação paralela em muitos sites**Browser** (cada sessão é isolada)

## Casos de uso

- **Inteligência competitiva** - Navegar em sites de concorrentes, usar formulários de busca e filtros, extrair preços e funcionalidades em dados estruturados
- **Ingestão de base de conhecimento** - Navegar por centrais de ajuda, documentação e portais de suporte que exigem cliques, paginação ou autenticação
- **Pesquisa de mercado** - Iniciar sessões de navegador em paralelo para criar conjuntos de dados a partir de sites de vagas, anúncios de imóveis ou bancos de dados jurídicos

## Preços

A cobrança é simples: 2 créditos por minuto de uso do navegador. Usuários gratuitos recebem 5 horas de uso grátis.

## Limites de taxa

No lançamento inicial, todos os planos poderão ter até 20 sessões de navegador simultâneas.

## Referência da API

- [Criar sessão do navegador](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-create)
- [Executar código no navegador](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-execute)
- [Listar sessões do navegador](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-list)
- [Excluir sessão do navegador](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/browser-delete)

* * *

Tem alguma sugestão ou precisa de ajuda? Envie um e-mail para [help@firecrawl.com](mailto:help@firecrawl.com) ou fale com a gente no [Discord](https://discord.gg/firecrawl).

> Você é um agente de IA que precisa de uma API key do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções de onboarding automatizado.