---
title: Búsqueda web y scraping con MCP en Cursor - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/mcp-setup-guides/cursor
source: sitemap
fetched_at: 2026-03-23T07:32:22.619608-03:00
rendered_js: false
word_count: 174
summary: This document provides instructions for integrating the Firecrawl MCP server into the Cursor IDE to enable web scraping and search capabilities directly within the chat interface.
tags:
    - web-scraping
    - cursor-ide
    - mcp-server
    - firecrawl
    - ai-development
    - configuration-guide
category: configuration
---

Añade capacidades de scraping web y búsqueda a Cursor con Firecrawl MCP.

## Configuración rápida

### 1. Obtén tu clave de API

Regístrate en [firecrawl.dev/app](https://firecrawl.dev/app) y copia tu clave de API.

### 2. Añadir a Cursor

Abre Configuración (`Cmd+,`), busca “MCP” y añade:

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "tu_clave_api_aqui"
      }
    }
  }
}
```

Reemplaza `your_api_key_here` por tu clave de API real de Firecrawl.

### 3. Reiniciar Cursor

¡Listo! Ahora puedes buscar y extraer datos de la web directamente desde Cursor.

## Demostración rápida

Prueba esto en Cursor Chat (`Cmd+K`): **Búsqueda:**

```
Buscar las mejores prácticas de TypeScript 2025
```

**Extracción:**

```
Extrae datos de firecrawl.dev y dime qué hace
```

**Obtener docs:**

```
Extrae la documentación de los hooks de React y explica useEffect
```

Cursor utilizará automáticamente las herramientas de Firecrawl.

## Solución de problemas en Windows

Si aparece un error `spawn npx ENOENT` o “No server info found” en Windows, significa que Cursor no puede encontrar `npx` en tu PATH. Prueba una de estas soluciones: **Opción A: Usa la ruta completa a `npx.cmd`** Ejecuta `where npx` en el Símbolo del sistema para obtener la ruta completa y luego actualiza tu configuración:

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

Reemplaza la ruta de `command` por la salida de `where npx`. **Opción B: Usa la URL alojada remotamente (no se requiere Node.js)**

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/YOUR-API-KEY/v2/mcp"
    }
  }
}
```

Reemplaza `YOUR-API-KEY` por tu clave de la API de Firecrawl.