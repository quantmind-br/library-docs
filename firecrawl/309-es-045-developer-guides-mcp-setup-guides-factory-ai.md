---
title: Búsqueda web y scraping con MCP en Factory AI - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/mcp-setup-guides/factory-ai
source: sitemap
fetched_at: 2026-03-23T07:36:15.176867-03:00
rendered_js: false
word_count: 121
summary: This document provides instructions on how to integrate web scraping and search capabilities into Factory AI using the Firecrawl MCP server.
tags:
    - factory-ai
    - firecrawl
    - mcp-server
    - web-scraping
    - web-search
    - api-integration
category: configuration
---

Añade capacidades de scraping y búsqueda web a Factory AI con Firecrawl MCP.

## Configuración rápida

### 1. Obtén tu clave de API

Regístrate en [firecrawl.dev/app](https://firecrawl.dev/app) y copia tu clave de API.

### 2. Instalar Factory AI CLI

Instala la [Factory AI CLI](https://docs.factory.ai/cli/getting-started/quickstart) si aún no lo has hecho: **macOS/Linux:**

```
curl -fsSL https://app.factory.ai/cli | sh
```

**Windows:**

```
iwr https://app.factory.ai/cli/install.ps1 -useb | iex
```

### 3. Añade el servidor MCP de Firecrawl

En la CLI de Factory droid, añade Firecrawl con el comando `/mcp add`:

```
/mcp add firecrawl "npx -y firecrawl-mcp" -e FIRECRAWL_API_KEY=your-api-key-here
```

Reemplaza `your-api-key-here` por tu clave de API real de Firecrawl.

### 4. ¡Listo!

¡Las herramientas de Firecrawl ya están disponibles en tu sesión de Factory AI!

## Demostración rápida

Prueba esto en Factory AI: **Buscar en la web:**

```
Busca las últimas funciones de Next.js 15
```

**Extraer una página:**

```
Extrae datos de firecrawl.dev y dime qué hace
```

**Obtener la documentación:**

```
Encuentra y extrae la documentación de la API de Stripe sobre intenciones de pago
```

Factory utilizará automáticamente las herramientas de búsqueda y extracción de Firecrawl para obtener la información.