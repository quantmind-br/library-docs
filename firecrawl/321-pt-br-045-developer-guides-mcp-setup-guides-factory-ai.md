---
title: Pesquisa e raspagem na web com MCP no Factory AI - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:34:27.973633-03:00
rendered_js: false
word_count: 119
summary: Este documento fornece instruções de configuração para integrar o Firecrawl MCP ao Factory AI, permitindo recursos de raspagem e pesquisa na web através do CLI.
tags:
    - factory-ai
    - firecrawl
    - mcp
    - web-scraping
    - web-search
    - api-integration
    - cli-setup
category: configuration
---

Adicione recursos de raspagem e pesquisa ao Factory AI com o Firecrawl MCP.

## Configuração rápida

### 1. Obtenha sua chave de API

Cadastre-se em [firecrawl.dev/app](https://firecrawl.dev/app) e copie sua chave de API.

### 2. Instalar o Factory AI CLI

Instale o [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) se ainda não o fez: **macOS/Linux:**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows:**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Adicionar o servidor MCP do Firecrawl

No CLI do Factory Droid, adicione o Firecrawl usando o comando `/mcp add`:

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

Substitua `your-api-key-here` pela sua chave de API do Firecrawl.

### 4. Pronto!

As ferramentas do Firecrawl agora estão disponíveis na sessão do Factory AI!

## Demonstração rápida

Experimente isto no Factory AI: **Pesquisar na web:**

```
Busque os recursos mais recentes do Next.js 15
```

**Raspar uma página:**

```
Faça scraping do firecrawl.dev e me diga o que ele faz
```

**Acessar a documentação:**

```
Encontre e extraia a documentação da API do Stripe sobre intenções de pagamento
```

A Factory utilizará automaticamente as ferramentas de busca e extração do Firecrawl para obter as informações.