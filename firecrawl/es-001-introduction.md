---
title: Guía rápida | Firecrawl
url: https://docs.firecrawl.dev/es/introduction
source: sitemap
fetched_at: 2026-03-23T07:30:21.088255-03:00
rendered_js: false
word_count: 405
summary: This document provides an introduction to Firecrawl, an API service designed to convert websites into clean, LLM-ready data formats through scraping, searching, and browser automation.
tags:
    - web-scraping
    - llm-data
    - data-extraction
    - ai-agents
    - browser-automation
    - api-integration
category: guide
---

## Haz scraping de tu primer sitio web

Convierte cualquier sitio web en datos limpios y listos para usar con LLM mediante una única llamada a la API.

### Utiliza Firecrawl con agentes de IA (recomendado)

La skill de Firecrawl es la forma más rápida para que los agentes descubran y utilicen Firecrawl. Sin ella, tu agente no sabrá que Firecrawl está disponible.

```
npx -y firecrawl-cli@latest init --all --browser
```

O bien usa el [MCP Server](https://docs.firecrawl.dev/es/mcp-server) para conectar Firecrawl directamente con Claude, Cursor, Windsurf, VS Code y otras herramientas de IA.

### Haz tu primera solicitud

Copia el siguiente código, reemplaza `fc-YOUR-API-KEY` por tu clave de API y ejecútalo:

Respuesta de ejemplo

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

## ¿Qué puede hacer Firecrawl?

### ¿Por qué Firecrawl?

- **Resultados listos para LLM**: Obtén markdown limpio, JSON estructurado, capturas de pantalla y más
- **Se encarga de lo difícil**: Proxies, anti-bot, renderizado de JavaScript y contenido dinámico
- **Confiable**: Construido para producción con alta disponibilidad y resultados consistentes
- **Rápido**: Obtén resultados en segundos, optimizado para alto rendimiento
- **Sandbox de navegador**: Entornos de navegador totalmente gestionados para agentes, sin configuración y que escalan a cualquier tamaño
- **Servidor MCP**: Conecta Firecrawl a cualquier herramienta de IA a través del [Model Context Protocol](https://docs.firecrawl.dev/es/mcp-server)

* * *

## Scraping

Extrae el contenido de cualquier URL y obténlo en markdown, HTML u otros formatos. Consulta la [documentación de la funcionalidad Scrape](https://docs.firecrawl.dev/es/features/scrape) para ver todas las opciones.

Respuesta

Los SDK devolverán el objeto de datos directamente. cURL devolverá la carga útil exactamente como se muestra a continuación.

```
{
  "success": true,
  "data" : {
    "markdown": "¡Launch Week I ya está aquí! [Consulta nuestro lanzamiento del Día 2 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Obtén 2 meses gratis...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Inicio - Firecrawl",
      "description": "Firecrawl rastrea y convierte cualquier sitio web en Markdown limpio.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "seguir, indexar",
      "ogTitle": "Firecrawl",
      "ogDescription": "Convierte cualquier sitio web en datos listos para LLM.",
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

## Búsqueda

La API de búsqueda de Firecrawl te permite realizar búsquedas en la web y, opcionalmente, extraer (scrape) los resultados en una sola operación.

- Elige formatos de salida específicos (Markdown, HTML, enlaces, capturas de pantalla)
- Elige fuentes específicas (web, noticias, imágenes)
- Busca en la web con parámetros personalizables (ubicación, etc.)

Para más detalles, consulta la [Referencia del endpoint /search](https://docs.firecrawl.dev/es/api-reference/endpoint/search).

Respuesta

Los SDK devolverán el objeto de datos directamente. cURL devolverá el payload completo.

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

## Agente

El Agent de Firecrawl es una herramienta autónoma de recopilación de datos web. Solo tienes que describir qué datos necesitas, y buscará, navegará y los extraerá desde cualquier lugar de la web. Consulta la [documentación de la funcionalidad Agent](https://docs.firecrawl.dev/es/features/agent) para ver todas las opciones.

respuesta de ejemplo

```
{
  "success": true,
  "data": {
    "result": "Notion offers the following pricing plans:\n\n1. **Free** - $0/month - For individuals...\n2. **Plus** - $10/seat/month - For small teams...\n3. **Business** - $18/seat/month - For companies...\n4. **Enterprise** - Custom pricing - For large organizations...",
    "sources": [
      "https://www.notion.so/pricing"
    ]
  }
}
```

## Browser

Firecrawl Browser Sandbox ofrece a tus agentes un entorno de navegador seguro para interactuar con la web. Completa formularios, haz clic en botones, autentícate y mucho más. No necesitas configuración local ni instalar Chromium. Consulta la [documentación de Browser](https://docs.firecrawl.dev/es/features/browser) para obtener toda la información.

Respuesta de ejemplo

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