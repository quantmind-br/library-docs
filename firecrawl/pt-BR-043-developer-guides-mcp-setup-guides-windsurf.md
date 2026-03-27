---
title: Busca e raspagem na web com MCP no Windsurf - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:34:25.478712-03:00
rendered_js: false
word_count: 87
summary: This document provides instructions on how to integrate the Firecrawl MCP server into the Windsurf IDE to enable automated web scraping and search capabilities for AI agents.
tags:
    - windsurf
    - firecrawl
    - mcp-server
    - web-scraping
    - ai-agents
    - configuration
category: configuration
---

Adicione recursos de raspagem e busca na web ao Windsurf com o Firecrawl MCP.

## Configuração rápida

### 1. Obtenha sua chave de API

Crie uma conta em [firecrawl.dev/app](https://firecrawl.dev/app) e copie sua chave de API.

### 2. Adicione ao Windsurf

Adicione o seguinte ao seu `./codeium/windsurf/model_config.json`:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "SUA_CHAVE_DE_API"
      }
    }
  }
}
```

Substitua `YOUR_API_KEY` pela sua chave de API real do Firecrawl.

### 3. Reinicie o Windsurf

Pronto! O Windsurf agora pode pesquisar e fazer scraping na web.

## Demonstração rápida

Experimente isto no Windsurf: **Pesquisa:**

```
Pesquise os recursos mais recentes do Tailwind CSS
```

**Scraping:**

```
Faça scraping do firecrawl.dev e explique o que ele faz
```

**Obter docs:**

```
Encontre e faça scraping da documentação de autenticação do Supabase
```

Os agentes de IA do Windsurf usarão automaticamente as ferramentas do Firecrawl.