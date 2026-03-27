---
title: Búsqueda y scraping web con MCP en Claude Code - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/mcp-setup-guides/claude-code
source: sitemap
fetched_at: 2026-03-23T07:29:24.803565-03:00
rendered_js: false
word_count: 107
summary: This document provides instructions on how to integrate the Firecrawl MCP server with Claude Code to enable web scraping and search capabilities.
tags:
    - firecrawl
    - claude-code
    - mcp-server
    - web-scraping
    - web-search
    - automation
    - integration
category: configuration
---

Añade funciones de scraping y búsqueda web a Claude Code con Firecrawl MCP.

## Configuración rápida

### 1. Obtén tu clave de API

Crea una cuenta en [firecrawl.dev/app](https://firecrawl.dev/app) y copia tu clave de API.

### 2. Añade el servidor MCP de Firecrawl

**Opción A: URL alojada en remoto (recomendada)**

```
claude mcp add firecrawl --url https://mcp.firecrawl.dev/your-api-key/v2/mcp
```

**Opción B: Local (npx)**

```
claude mcp add firecrawl -e FIRECRAWL_API_KEY=your-api-key -- npx -y firecrawl-mcp
```

Reemplaza `your-api-key` por tu clave real de la API de Firecrawl. ¡Listo! Ahora puedes buscar y extraer datos de la web desde Claude Code.

## Demostración rápida

Prueba lo siguiente en Claude Code: **Buscar en la web:**

```
Search for the latest Next.js 15 features
```

**Extrae datos de una página:**

```
Scrape firecrawl.dev and tell me what it does
```

**Consulta la documentación:**

```
Find and scrape the Stripe API docs for payment intents
```

Claude usará automáticamente las herramientas de búsqueda y scraping de Firecrawl para obtener la información.