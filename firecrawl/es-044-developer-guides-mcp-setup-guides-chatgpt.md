---
title: Búsqueda web y scraping con MCP en ChatGPT - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:39:09.948694-03:00
rendered_js: false
word_count: 309
summary: This document provides step-by-step instructions for integrating Firecrawl's web scraping and search capabilities into ChatGPT using the Model Context Protocol (MCP).
tags:
    - firecrawl
    - chatgpt
    - mcp-server
    - web-scraping
    - api-integration
    - developer-mode
category: configuration
---

Agrega capacidades de scraping web y búsqueda a ChatGPT con Firecrawl MCP.

## Configuración rápida

### 1. Obtén tu clave de API

Regístrate en [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) y copia tu clave de API.

### 2. Activa el modo desarrollador

Abre la configuración de ChatGPT haciendo clic en tu nombre de usuario en la esquina inferior izquierda, o ve directamente a [chatgpt.com/#settings](https://chatgpt.com/#settings). En la ventana de configuración, desplázate hasta la parte inferior y selecciona **Advanced Settings**. Activa **Developer mode**.

### 3. Crear el conector

Con el modo Developer habilitado, ve a la pestaña **Apps & Connectors** en el mismo modal de configuración. Haz clic en el botón **Create** en la esquina superior derecha.

Completa los detalles del conector:

- **Name:** `Firecrawl MCP`
- **Description:** `Web scraping, crawling, search, and content extraction` (opcional)
- **MCP Server URL:** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication:** `None`

Reemplaza `YOUR_API_KEY_HERE` en la URL con tu [clave de API de Firecrawl](https://www.firecrawl.dev/app/api-keys) real.

Marca la casilla **“I understand and want to continue”** y luego haz clic en **Create**.

### 4. Verificar la configuración

Vuelve a la interfaz principal de ChatGPT. Deberías ver **Developer mode** en pantalla, lo que indica que los conectores MCP están activos. Si no ves **Developer mode**, recarga la página. Si aún no aparece, abre la configuración de nuevo y verifica que **Developer mode** esté activado en la sección **Advanced Settings**.

Para usar Firecrawl en una conversación, haz clic en el botón **+** en el campo de entrada del chat, luego selecciona **More** y elige **Firecrawl MCP**.

## Demostración rápida

Con Firecrawl MCP seleccionado, prueba con estos prompts: **Búsqueda:**

```
Search for the latest React Server Components updates
```

**Scrape:**

```
Scrape firecrawl.dev and tell me what it does
```

**Obtener documentos:**

```
Extrae la documentación de Vercel sobre funciones edge y resúmela
```

Cuando ChatGPT use las herramientas MCP de Firecrawl, verás un mensaje de confirmación solicitando tu aprobación.

Puedes marcar **“Remember for this conversation”** para evitar confirmaciones repetidas durante la misma sesión de chat. Esta medida de seguridad la implementa OpenAI para garantizar que las herramientas MCP no realicen acciones no deseadas. Una vez confirmes, ChatGPT ejecutará la solicitud y devolverá los resultados.