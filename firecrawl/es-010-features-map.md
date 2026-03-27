---
title: Mapa | Firecrawl
url: https://docs.firecrawl.dev/es/features/map
source: sitemap
fetched_at: 2026-03-23T07:25:13.480707-03:00
rendered_js: false
word_count: 416
summary: This document describes the /map endpoint, which enables users to discover and extract website URLs for scraping or indexing purposes using sitemaps and search results.
tags:
    - api-documentation
    - web-scraping
    - url-discovery
    - sitemap-crawling
    - search-integration
    - data-extraction
category: api
---

## Presentamos /map

La forma más fácil de pasar de una sola URL a un mapa de todo el sitio web. Esto es especialmente útil para:

- Cuando necesitas pedir al usuario final que elija qué enlaces extraer
- Necesitas conocer rápidamente los enlaces de un sitio web
- Necesitas extraer páginas de un sitio web relacionadas con un tema específico (usa el parámetro `search`)
- Solo necesitas extraer páginas específicas de un sitio web

## Mapeo

### punto de conexión /map

Se usa para mapear una URL y obtener las URL del sitio web. Devuelve la mayoría de los enlaces presentes en el sitio. Las URL se descubren principalmente desde el sitemap del sitio web, complementadas con resultados de motores de búsqueda (SERP) y páginas rastreadas previamente para mejorar la cobertura. Puedes controlar el comportamiento del sitemap con el parámetro `sitemap`.

### Instalación

### Uso

### Respuesta

Los SDK devolverán el objeto de datos directamente. cURL devolverá el payload exactamente como se muestra a continuación.

```
{
  "success": true,
  "links": [
    {
      "url": "https://docs.firecrawl.dev/features/scrape",
      "title": "Scrape | Firecrawl",
      "description": "Convierte cualquier URL en datos limpios"
    },
    {
      "url": "https://www.firecrawl.dev/blog/5_easy_ways_to_access_glm_4_5",
      "title": "5 maneras sencillas de acceder a GLM-4.5",
      "description": "Descubre cómo acceder a los modelos GLM-4.5 localmente, mediante aplicaciones de chat, a través de la API oficial y usando la API de los marketplaces de LLM para una integración sin fricciones..."
    },
    {
      "url": "https://www.firecrawl.dev/playground",
      "title": "Playground - Firecrawl",
      "description": "Previsualiza la respuesta de la API y obtén fragmentos de código para la API"
    },
    {
      "url": "https://www.firecrawl.dev/?testId=2a7e0542-077b-4eff-bec7-0130395570d6",
      "title": "Firecrawl - La API de datos web para IA",
      "description": "La API de rastreo, scraping y búsqueda web para IA. Diseñada para escalar. Firecrawl pone todo internet al alcance de agentes y desarrolladores de IA. Limpio, estructurado y ..."
    },
    {
      "url": "https://www.firecrawl.dev/?testId=af391f07-ca0e-40d3-8ff2-b1ecf2e3fcde",
      "title": "Firecrawl - La API de datos web para IA",
      "description": "La API de rastreo, scraping y búsqueda web para IA. Diseñada para escalar. Firecrawl pone todo internet al alcance de agentes y desarrolladores de IA. Limpio, estructurado y ..."
    },
    ...
  ]
}
```

#### Map con búsqueda

Map con el parámetro `search` te permite buscar URLs específicas dentro de un sitio web.

```
curl -X POST https://api.firecrawl.dev/v2/map \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer TU_API_KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "search": "docs"
  }'
```

La respuesta será una lista ordenada, de la más relevante a la menos relevante.

```
{
  "status": "success",
  "links": [
    {
      "url": "https://docs.firecrawl.dev",
      "title": "Firecrawl Docs",
      "description": "Documentación de Firecrawl",
    },
    {
      "url": "https://docs.firecrawl.dev/sdks/python",
      "title": "SDK de Firecrawl para Python",
      "description": "Documentación del SDK de Firecrawl para Python"
    },
    ...
  ]
}
```

## Ubicación e idioma

Especifica el país y los idiomas preferidos para obtener contenido relevante según tu ubicación y preferencias de idioma, de forma similar al punto de conexión /scrape.

### Cómo funciona

Cuando especificas la configuración de ubicación, Firecrawl usará, si está disponible, un proxy adecuado y emulará la configuración de idioma y zona horaria correspondientes. De forma predeterminada, la ubicación se establece en “US” si no se especifica.

### Uso

Para usar la configuración de ubicación e idioma, incluye el objeto `location` en el cuerpo de la solicitud con las siguientes propiedades:

- `country`: código de país ISO 3166-1 alfa-2 (p. ej., ‘US’, ‘AU’, ‘DE’, ‘JP’). Valor predeterminado: ‘US’.
- `languages`: un arreglo de idiomas y configuraciones regionales preferidos para la solicitud, en orden de prioridad. Por defecto, el idioma de la ubicación especificada.

Para más detalles sobre las ubicaciones compatibles, consulta la [documentación de proxies](https://docs.firecrawl.dev/es/features/proxies).

## Consideraciones

Este punto de conexión prioriza la velocidad, por lo que es posible que no capture todos los enlaces del sitio web. Se basa principalmente en el sitemap del sitio web, complementado con datos de rastreo en caché y resultados de motores de búsqueda. Para obtener una lista de URL más completa y actualizada, considera usar el punto de conexión [/crawl](https://docs.firecrawl.dev/es/features/crawl) en su lugar.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.