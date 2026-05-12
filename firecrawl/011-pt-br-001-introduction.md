---
title: Guia rápido | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:17.002493-03:00
rendered_js: false
word_count: 410
summary: This document provides an introduction to Firecrawl, an API service designed to scrape websites and convert content into LLM-ready formats, including structured data, markdown, and interactive browser environments.
tags:
    - web-scraping
    - api-integration
    - ai-agents
    - data-extraction
    - markdown-conversion
    - web-crawling
category: guide
---

## Faça scraping do seu primeiro site

Transforme qualquer site em dados limpos, prontos para LLM, com uma única chamada de API.

### Use o Firecrawl com agentes de IA (recomendado)

A skill do Firecrawl é a forma mais rápida de os agentes descobrirem e usarem o Firecrawl. Sem ela, seu agente não saberá que o Firecrawl está disponível.

```
npx -y firecrawl-cli@latest init --all --browser
```

Ou use o [MCP Server](https://docs.firecrawl.dev/pt-BR/mcp-server) para conectar o Firecrawl diretamente ao Claude, Cursor, Windsurf, VS Code e a outras ferramentas de IA.

### Faça sua primeira requisição

Copie o código abaixo, substitua `fc-YOUR-API-KEY` pela sua chave de API e execute o comando:

Exemplo de resposta

```
{
  "success": true,
  "data": {
    "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples...",
    "metadata": {
      "title": "Example Domain",
      "sourceURL": "https://example.com"
    }
  }
}
```

* * *

## O que o Firecrawl pode fazer?

### Por que Firecrawl?

- **Saída pronta para LLMs**: Obtenha markdown limpo, JSON estruturado, capturas de tela e muito mais
- **Lida com as partes difíceis**: Proxies, anti-bot, renderização de JavaScript e conteúdo dinâmico
- **Confiável**: Feito para produção, com alta disponibilidade e resultados consistentes
- **Rápido**: Obtenha resultados em segundos, otimizado para alto volume de requisições
- **Sandbox de navegador**: Ambientes de navegador totalmente gerenciados para agentes, zero configuração, escala para qualquer volume
- **MCP Server**: Conecte o Firecrawl a qualquer ferramenta de IA via o [Model Context Protocol](https://docs.firecrawl.dev/pt-BR/mcp-server)

* * *

Extraia qualquer URL e obtenha seu conteúdo em markdown, HTML ou outros formatos. Veja a [documentação do recurso de Extração](https://docs.firecrawl.dev/pt-BR/features/scrape) para todas as opções.

Resposta

Os SDKs retornarão o objeto de dados diretamente. O cURL retornará o payload exatamente como mostrado abaixo.

```
{
  "success": true,
  "data" : {
    "markdown": "A Launch Week I chegou! [Confira nosso lançamento do Dia 2 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Ganhe 2 meses grátis...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "O Firecrawl rastreia e converte qualquer site em markdown limpo.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Dados,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Transforme qualquer site em dados prontos para LLM.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## Busca

A API de busca do Firecrawl permite realizar pesquisas na web e, opcionalmente, extrair (scrape) os resultados em uma única operação.

- Escolha formatos de saída específicos (Markdown, HTML, links, capturas de tela)
- Escolha fontes específicas (web, notícias, imagens)
- Pesquise na web com parâmetros personalizáveis (localização, etc.)

Para mais detalhes, consulte a [referência da API do endpoint /search](https://docs.firecrawl.dev/pt-BR/api-reference/endpoint/search).

Resposta

Os SDKs retornarão diretamente o objeto de dados. O cURL retornará o payload completo.

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - The Web Data API for AI",
        "description": "The web crawling, scraping, and search API for AI. Built for scale. Firecrawl delivers the entire internet to AI agents and builders.",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## Agent

O Agent do Firecrawl é uma ferramenta autônoma de coleta de dados na web. Basta descrever quais dados você precisa e ele vai pesquisar, navegar e extrair esses dados de qualquer lugar na web. Veja a [documentação do recurso Agent](https://docs.firecrawl.dev/pt-BR/features/agent) para ver todas as opções.

Exemplo de resposta

```
{
  "success": true,
  "data": {
    "result": "O Notion oferece os seguintes planos de preços:\n\n1. **Free** - US$0/mês - Para indivíduos...\n2. **Plus** - US$10/usuário/mês - Para pequenas equipes...\n3. **Business** - US$18/usuário/mês - Para empresas...\n4. **Enterprise** - Preço personalizado - Para grandes organizações...",
    "sources": [
      "https://www.notion.so/pricing"
    ]
  }
}
```

## Browser

O sandbox de navegador do Firecrawl oferece aos seus agentes um ambiente de navegador seguro para interagir com a web. Preencha formulários, clique em botões, autentique-se e muito mais. Não é necessário fazer nenhuma configuração local nem instalar o Chromium. Consulte a [documentação do recurso Browser](https://docs.firecrawl.dev/pt-BR/features/browser) para ver a documentação completa.

Exemplo de resposta

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-...",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-...?interactive=true"
}
```

* * *

## Recursos