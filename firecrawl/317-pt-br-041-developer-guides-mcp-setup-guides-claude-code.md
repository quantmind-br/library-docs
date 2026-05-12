---
title: Pesquisa e scraping na web com MCP no Claude Code - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:13.035064-03:00
rendered_js: false
word_count: 105
summary: This document provides instructions on how to integrate web scraping and search capabilities into Claude Code using the Firecrawl MCP server.
tags:
    - claude-code
    - mcp-server
    - firecrawl
    - web-scraping
    - web-search
    - configuration
category: configuration
---

Adicione recursos de scraping e busca na web ao Claude Code com o Firecrawl MCP.

## Configuração rápida

### 1. Obtenha sua chave de API

Inscreva-se em [firecrawl.dev/app](https://firecrawl.dev/app) e copie sua chave de API.

### 2. Adicione o Firecrawl MCP Server

**Opção A: URL hospedada remotamente (recomendada)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**Opção B: Local (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

Substitua `your-api-key` pela sua chave de API real do Firecrawl. Pronto! Agora você pode fazer busca e scraping na web pelo Claude Code.

## Demonstração rápida

Experimente isto no Claude Code: **Faça uma busca na web:**

```
Search for the latest Next.js 15 features
```

**Faça o scraping de uma página:**

```
Scrape firecrawl.dev and tell me what it does
```

**Obtenha a documentação:**

```
Find and scrape the Stripe API docs for payment intents
```

Claude usará automaticamente as ferramentas de busca e scraping do Firecrawl para obter as informações.