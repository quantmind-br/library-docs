---
title: Búsqueda | Firecrawl
url: https://docs.firecrawl.dev/es/features/search
source: sitemap
fetched_at: 2026-03-23T07:25:30.618196-03:00
rendered_js: false
word_count: 932
summary: This document describes the Firecrawl search API, which allows users to perform web searches and optionally scrape content from results using customizable sources, categories, and advanced filtering options.
tags:
    - web-scraping
    - api-documentation
    - search-api
    - data-extraction
    - ai-agents
    - firecrawl
category: api
---

La API de búsqueda de Firecrawl te permite realizar búsquedas en la web y, opcionalmente, extraer los resultados en una sola operación.

- Elige formatos de salida específicos (markdown, HTML, links, capturas de pantalla)
- Busca en la web con parámetros personalizables (ubicación, etc.)
- Recupera opcionalmente contenido de los resultados de búsqueda en varios formatos
- Controla la cantidad de resultados y establece tiempos de espera

Para más detalles, consulta la [referencia del punto de conexión /search](https://docs.firecrawl.dev/api-reference/endpoint/search).

## Buscar con Firecrawl

### punto de conexión /search

Se usa para realizar búsquedas en la web y, opcionalmente, obtener contenido de los resultados.

### Instalación

### Uso básico

### Respuesta

Los SDK devolverán directamente el objeto de datos. cURL devolverá el payload completo.

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

## Tipos de resultados de búsqueda

Además de los resultados web habituales, Search admite tipos de resultados especializados mediante el parámetro `sources`:

- `web`: resultados web estándar (predeterminado)
- `news`: resultados enfocados en noticias
- `images`: resultados de búsqueda de imágenes

Puedes solicitar varias fuentes en una sola llamada (por ejemplo, `sources: ["web", "news"]`). Cuando lo haces, el parámetro `limit` se aplica **por tipo de fuente**; así, `limit: 5` con `sources: ["web", "news"]` devuelve hasta 5 resultados web y hasta 5 resultados de noticias (10 en total). Si necesitas parámetros diferentes por fuente (por ejemplo, valores `limit` distintos o diferentes `scrapeOptions`), haz llamadas separadas en su lugar.

## Categorías de búsqueda

Filtra los resultados por categorías específicas usando el parámetro `categories`:

- `github`: Busca en repositorios, código, issues y documentación de GitHub
- `research`: Busca en sitios académicos y de investigación (arXiv, Nature, IEEE, PubMed, etc.)
- `pdf`: Busca archivos PDF

### Búsqueda de categorías en GitHub

Busca específicamente dentro de los repositorios de GitHub:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-TU_API_KEY" \
  -d '{
    "query": "web scraping en Python",
    "categories": ["github"],
    "limit": 10
  }'
```

### Búsqueda por categoría de investigación

Busca en sitios web académicos y de investigación:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-TU_API_KEY" \
  -d '{
    "query": "transformers de aprendizaje automático",
    "categories": ["investigación"],
    "limit": 10
  }'
```

### Búsqueda de categorías mixtas

Combina varias categorías en una sola búsqueda:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "redes neuronales",
    "categories": ["github", "investigación"],
    "limit": 15
  }'
```

### Formato de respuesta de categorías

Cada resultado de búsqueda incluye un campo `category` que indica su fuente:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "Implementación de redes neuronales",
        "description": "Implementación de redes neuronales en PyTorch",
        "category": "github"
        "category": "github",
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "Avances en la arquitectura de redes neuronales",
        "description": "Artículo de investigación sobre mejoras en redes neuronales",
        "category": "research"
      }
    ]
  }
}
```

Ejemplos:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-TU_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### Búsqueda de imágenes en HD con filtro de tamaño

Usa los operadores de imágenes para encontrar imágenes de alta resolución:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "atardecer imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "fondo de pantalla de montaña larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**Resoluciones HD habituales:**

- `imagesize:1920x1080` - Full HD (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - HD o superior
- `larger:2560x1440` - QHD o superior

Busca y recupera contenido de los resultados de búsqueda en una sola operación.

Todas las opciones del punto de conexión /scrape son compatibles con este punto de conexión de búsqueda mediante el parámetro `scrapeOptions`.

### Respuesta con contenido rastreado

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - La API definitiva de web scraping",
      "description": "Firecrawl es una potente API de web scraping que convierte cualquier sitio web en datos limpios y estructurados para IA y análisis.",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\nLa API definitiva de web scraping\n\n## Convierte cualquier sitio web en datos limpios y estructurados\n\nFirecrawl facilita la extracción de datos de sitios web para aplicaciones de IA, investigación de mercados, agregación de contenido y más...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - La API definitiva de web scraping",
        "description": "Firecrawl es una potente API de web scraping que convierte cualquier sitio web en datos limpios y estructurados para IA y análisis.",
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## Opciones de búsqueda avanzadas

La API de búsqueda de Firecrawl admite varios parámetros para personalizar la búsqueda:

### Personalización de la ubicación

### Búsqueda por tiempo

Usa el parámetro `tbs` para filtrar resultados por periodo. Ten en cuenta que `tbs` solo se aplica a resultados de `web` — no filtra resultados de `news` ni de `images`. Si necesitas noticias filtradas por tiempo, considera usar `web` como origen con el operador `site:` para restringir la búsqueda a dominios de noticias específicos.

Valores comunes de `tbs`:

- `qdr:h` - Última hora
- `qdr:d` - Últimas 24 horas
- `qdr:w` - Última semana
- `qdr:m` - Último mes
- `qdr:y` - Último año
- `sbd:1` - Ordenar por fecha (las más recientes primero)

Para un filtrado temporal más preciso, puedes especificar rangos exactos usando el formato de rango de fechas personalizado:

Puedes combinar `sbd:1` con filtros de tiempo para obtener resultados ordenados por fecha dentro de un rango temporal. Por ejemplo, `sbd:1,qdr:w` devuelve resultados de la última semana ordenados de más recientes a más antiguos, y `sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` devuelve resultados de diciembre de 2024 ordenados por fecha.

### Tiempo de espera personalizado

Configura un tiempo de espera personalizado para las operaciones de búsqueda:

## Retención de datos cero (ZDR)

Para equipos con requisitos estrictos de tratamiento de datos, Firecrawl ofrece opciones de Retención de datos cero (ZDR) para el punto de conexión `/search` mediante el parámetro `enterprise`. La búsqueda con ZDR está disponible en los planes Enterprise — visita [firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) para comenzar.

### ZDR de extremo a extremo

Con ZDR de extremo a extremo, tanto Firecrawl como nuestro proveedor de búsqueda upstream aplican retención de datos cero. No se almacenan datos de consultas ni de resultados en ningún punto del pipeline.

- **Costo:** 10 créditos por 10 resultados
- **Parámetro:** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### ZDR anonimizado

Con ZDR anonimizado, Firecrawl aplica retención de datos cero completa por nuestra parte. Nuestro proveedor de búsqueda puede almacenar en caché la consulta, pero está completamente anonimizada — no se adjunta ninguna información identificativa.

- **Costo:** 2 créditos por 10 resultados
- **Parámetro:** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### Combinar Search ZDR con Scrape ZDR

Si estás usando search con scraping de contenido (`scrapeOptions`), el parámetro `enterprise` cubre la parte de búsqueda, mientras que `zeroDataRetention` en `scrapeOptions` cubre la parte de scraping. Para obtener ZDR completo en ambos, configura ambos:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## Implicaciones de costos

El costo de una búsqueda es de 2 créditos por cada 10 resultados de búsqueda. Si las opciones de scraping están habilitadas, se aplican los costos estándar de scraping a cada resultado de búsqueda:

- **Basic scrape**: 1 crédito por página web
- **PDF parsing**: 1 crédito por página de PDF
- **Enhanced proxy mode**: 4 créditos adicionales por página web
- **JSON mode**: 4 créditos adicionales por página web

Para ayudar a controlar los costos:

- Establece `parsers: []` si no se requiere el análisis de PDF
- Usa `proxy: "basic"` en lugar de `"enhanced"` cuando sea posible, o configúralo en `"auto"`
- Limita la cantidad de resultados de búsqueda con el parámetro `limit`

## Opciones avanzadas de scraping

Para más detalles sobre las opciones de scraping, consulta la [documentación de la función Scrape](https://docs.firecrawl.dev/features/scrape). Todo, excepto FIRE-1 (Agente) y seguimientoDeCambios, es compatible con este punto de conexión de búsqueda.

> ¿Eres un agente de IA que necesita una API key de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automatizada.