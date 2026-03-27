---
title: Migración de v1 a v2 | Firecrawl
url: https://docs.firecrawl.dev/es/migrate-to-v2
source: sitemap
fetched_at: 2026-03-23T07:39:10.692351-03:00
rendered_js: false
word_count: 486
summary: This document provides a technical migration guide for upgrading from Firecrawl v1 to v2, outlining API changes, updated SDK method naming conventions, and new features.
tags:
    - api-migration
    - sdk-update
    - web-scraping
    - api-reference
    - firecrawl
category: guide
---

## Visión general

### Mejoras clave

- **Más rápido de forma predeterminada**: Las solicitudes se almacenan en caché con `maxAge` establecido por defecto en 2 días, y están habilitados valores predeterminados sensatos como `blockAds`, `skipTlsVerification` y `removeBase64Images`.
- **Nuevo formato de resumen**: Ahora puedes especificar `"summary"` como formato para recibir directamente un resumen conciso del contenido de la página.
- **Extracción JSON actualizada**: La extracción en JSON y el seguimiento de cambios ahora usan un formato de objeto: `{ type: "json", prompt, schema }`. El antiguo formato `"extract"` pasó a llamarse `"json"`.
- **Opciones de captura de pantalla mejoradas**: Usa el formato de objeto: `{ type: "screenshot", fullPage, quality, viewport }`.
- **Nuevas fuentes de búsqueda**: Busca en `"news"` e `"images"`, además de los resultados web, configurando el parámetro `sources`.
- **Rastreo inteligente con prompts**: Pasa un `prompt` en lenguaje natural para el rastreo y el sistema derivará rutas y límites automáticamente. Usa el nuevo punto de conexión /crawl/params-preview para inspeccionar las opciones derivadas antes de iniciar un trabajo.

## Lista rápida de verificación de migración

- Reemplaza el uso del cliente v1 por los clientes v2:
  
  - JS: `const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' })`
  - Python: `firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')`
  - API: usa los nuevos puntos de conexión `https://api.firecrawl.dev/v2/`.
- Actualiza los formatos:
  
  - Usa `"summary"` cuando sea necesario
  - modo JSON: usa `{ type: "json", prompt, schema }` para la extracción en modo JSON
  - Screenshot y Screenshot@fullPage: usa el formato de objeto de captura de pantalla al especificar opciones
- Adopta flujos asíncronos estandarizados en los SDK:
  
  - Crawls: `startCrawl` + `getCrawlStatus` (o el “waiter” `crawl`)
  - Batch: `startBatchScrape` + `getBatchScrapeStatus` (o el “waiter” `batchScrape`)
  - Extract: `startExtract` + `getExtractStatus` (o el “waiter” `extract`)
- Mapeo de opciones de crawl (ver abajo)
- Verifica el `prompt` de crawl con `/crawl/params-preview`

## Superficie del SDK (v2)

### JS/TS

#### Cambios en los nombres de métodos (migración v1 → v2)

**Scrape, Search y Map**

v1 (FirecrawlApp)v2 (Firecrawl)`scrapeUrl(url, ...)``scrape(url, options?)``search(query, ...)``search(query, options?)``mapUrl(url, ...)``map(url, options?)`

**Crawling**

v1v2`crawlUrl(url, ...)``crawl(url, options?)` (bloqueante)`asyncCrawlUrl(url, ...)``startCrawl(url, options?)``checkCrawlStatus(id, ...)``getCrawlStatus(id)``cancelCrawl(id)``cancelCrawl(id)``checkCrawlErrors(id)``getCrawlErrors(id)`

**Batch Scraping**

v1v2`batchScrapeUrls(urls, ...)``batchScrape(urls, opts?)` (bloqueante)`asyncBatchScrapeUrls(urls, ...)``startBatchScrape(urls, opts?)``checkBatchScrapeStatus(id, ...)``getBatchScrapeStatus(id)``checkBatchScrapeErrors(id)``getBatchScrapeErrors(id)`

**Extraction**

v1v2`extract(urls?, params?)``extract(args)``asyncExtract(urls, params?)``startExtract(args)``getExtractStatus(id)``getExtractStatus(id)`

**Otros / Eliminados**

v1v2`generateLLMsText(...)`(no incluido en el SDK v2)`checkGenerateLLMsTextStatus(id)`(no incluido en el SDK v2)`crawlUrlAndWatch(...)``watcher(jobId, ...)``batchScrapeUrlsAndWatch(...)``watcher(jobId, ...)`

* * *

### Python (sincrónico)

#### Cambios en los nombres de métodos (migración v1 → v2)

**Scrape, Search y Map**

v1v2`scrape_url(...)``scrape(...)``search(...)``search(...)``map_url(...)``map(...)`

**Crawling**

v1v2`crawl_url(...)``crawl(...)` (waiter)`async_crawl_url(...)``start_crawl(...)``check_crawl_status(...)``get_crawl_status(...)``cancel_crawl(...)``cancel_crawl(...)`

**Batch Scraping**

v1v2`batch_scrape_urls(...)``batch_scrape(...)` (waiter)`async_batch_scrape_urls(...)``start_batch_scrape(...)``get_batch_scrape_status(...)``get_batch_scrape_status(...)``get_batch_scrape_errors(...)``get_batch_scrape_errors(...)`

**Extraction**

v1v2`extract(...)``extract(...)``start_extract(...)``start_extract(...)``get_extract_status(...)``get_extract_status(...)`

**Otros / Eliminados**

v1v2`generate_llms_text(...)`(no está en el SDK v2)`get_generate_llms_text_status(...)`(no está en el SDK v2)`watch_crawl(...)``watcher(job_id, ...)`

* * *

### Python (async)

- `AsyncFirecrawl` ofrece los mismos métodos (todos awaitable).

## Formatos y opciones de scrape

- Usa formatos de texto para lo básico: `"markdown"`, `"html"`, `"rawHtml"`, `"links"`, `"summary"`, `"images"`.
- En lugar de `parsePDF`, usa `parsers: [ { "type": "pdf" } | "pdf" ]`.
- Usa formatos de objeto para JSON, seguimiento de cambios y capturas de pantalla:

### Formato JSON

### Formato de captura de pantalla

## Mapeo de opciones de rastreo (v1 → v2)

v1v2`allowBackwardCrawling`(eliminado) utiliza `crawlEntireDomain``maxDepth`(eliminado) utiliza `maxDiscoveryDepth``ignoreSitemap` (bool)`sitemap` (p. ej., “only”, “skip” o “include”)(ninguno)`prompt`

## Vista previa de prompt y parámetros de rastreo

Consulta ejemplos de la vista previa de parámetros de rastreo: