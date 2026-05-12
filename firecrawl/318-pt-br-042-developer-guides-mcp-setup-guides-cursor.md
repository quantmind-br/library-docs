---
title: Pesquisa e raspagem na web com MCP no Cursor - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/mcp-setup-guides/cursor
source: sitemap
fetched_at: 2026-03-23T07:32:09.180698-03:00
rendered_js: false
word_count: 175
summary: This document provides instructions on how to integrate Firecrawl's web scraping and search capabilities into the Cursor code editor using the Model Context Protocol (MCP).
tags:
    - cursor-editor
    - firecrawl
    - mcp-server
    - web-scraping
    - ai-integration
    - development-tools
category: configuration
---

Adicione recursos de raspagem e pesquisa na web ao Cursor com o Firecrawl MCP.

## Configuração rápida

### 1. Obtenha sua chave de API

Crie uma conta em [firecrawl.dev/app](https://firecrawl.dev/app) e copie sua chave de API.

### 2. Adicionar ao Cursor

Abra as configurações (`Cmd+,`), pesquise por “MCP” e adicione:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "sua_chave_de_api_aqui"
      }
    }
  }
}
```

Substitua `your_api_key_here` pela sua chave de API do Firecrawl.

### 3. Reinicie o Cursor

Pronto! Agora você pode pesquisar e raspar a web diretamente no Cursor.

## Demo Rápido

Experimente isto no Cursor Chat (`Cmd+K`): **Pesquisar:**

```
Buscar melhores práticas de TypeScript 2025
```

**Raspagem:**

```
Faça scraping do firecrawl.dev e me diga o que ele faz
```

**Obter documentação:**

```
Faça scraping da documentação de hooks do React e explique o useEffect
```

O Cursor usará automaticamente as ferramentas do Firecrawl.

## Solução de problemas no Windows

Se você encontrar um erro `spawn npx ENOENT` ou “No server info found” no Windows, o Cursor não está encontrando `npx` no seu PATH. Tente uma destas soluções: **Opção A: Use o caminho completo para `npx.cmd`** Execute `where npx` no Prompt de Comando para obter o caminho completo e, em seguida, atualize sua configuração:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Substitua o caminho do `command` pela saída de `where npx`. **Opção B: Use a URL hospedada remotamente (sem Node.js)**

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/YOUR-API-KEY/v2/mcp"
    }
  }
}
```

Substitua `YOUR-API-KEY` pela sua chave de API do Firecrawl.