---
title: Búsqueda y scraping web con MCP en Windsurf - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/mcp-setup-guides/windsurf
source: sitemap
fetched_at: 2026-03-23T07:36:07.675077-03:00
rendered_js: false
word_count: 80
summary: This document provides instructions for integrating the Firecrawl MCP server into the Windsurf IDE to enable web searching and data scraping capabilities.
tags:
    - windsurf-ide
    - firecrawl
    - mcp-server
    - web-scraping
    - ai-agents
    - integration-guide
category: configuration
---

Añade capacidades de scraping y búsqueda web a Windsurf con Firecrawl MCP.

## Configuración rápida

### 1. Obtén tu clave de API

Regístrate en [firecrawl.dev/app](https://firecrawl.dev/app) y copia tu clave de API.

### 2. Añadir a Windsurf

Añade esto a `./codeium/windsurf/model_config.json`:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "TU_API_KEY"
      }
    }
  }
}
```

Reemplaza `YOUR_API_KEY` por tu clave real de la API de Firecrawl.

### 3. Reinicia Windsurf

¡Listo! Windsurf ahora puede buscar y hacer scraping en la web.

## Demostración rápida

Pruébalos en Windsurf: **Búsqueda:**

```
Busca las últimas funcionalidades de Tailwind CSS
```

**Extracción:**

```
Extrae datos de firecrawl.dev y explica qué hace
```

**Obtener docs:**

```
Busca y extrae la documentación de autenticación de Supabase
```

Los agentes de IA de Windsurf usarán automáticamente las herramientas de Firecrawl.