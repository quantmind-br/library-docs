---
title: Migração da v1 para a v2 | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/migrate-to-v2
source: sitemap
fetched_at: 2026-03-23T07:37:35.003493-03:00
rendered_js: false
word_count: 462
summary: This document provides migration instructions and a reference for updating from version 1 to version 2 of the Firecrawl API and SDK, detailing changes to endpoints, method names, and configuration formats.
tags:
    - api-migration
    - sdk-update
    - web-scraping
    - api-reference
    - data-extraction
    - crawling
category: guide
---

## Visão geral

### Melhorias principais

- **Mais rápido por padrão**: As requisições são armazenadas em cache com `maxAge` definido para 2 dias, e padrões sensatos como `blockAds`, `skipTlsVerification` e `removeBase64Images` vêm habilitados.
- **Novo formato de resumo**: Agora você pode especificar `"summary"` como um formato para receber diretamente um resumo conciso do conteúdo da página.
- **Extração JSON atualizada**: A extração JSON e o rastreamento de alterações agora usam um formato de objeto: `{ type: "json", prompt, schema }`. O antigo formato `"extract"` foi renomeado para `"json"`.
- **Opções de captura de tela aprimoradas**: Use o formato de objeto: `{ type: "screenshot", fullPage, quality, viewport }`.
- **Novas fontes de pesquisa**: Pesquise em `"news"` e `"images"`, além dos resultados da web, definindo o parâmetro `sources`.
- **Rastreamento inteligente com prompts**: Forneça um `prompt` em linguagem natural para o crawl e o sistema derivará caminhos/limites automaticamente. Use o novo endpoint /crawl/params-preview para inspecionar as opções derivadas antes de iniciar um job.

## Lista de verificação rápida de migração

- Substitua o uso do cliente v1 pelos clientes v2:
  
  - JS: `const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' })`
  - Python: `firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')`
  - API: use os novos endpoints em `https://api.firecrawl.dev/v2/`.
- Atualize os formatos:
  
  - Use “summary” quando necessário
  - modo JSON: use `{ type: "json", prompt, schema }` para extração em JSON
  - Screenshot e Screenshot@fullPage: use o formato de objeto de screenshot ao especificar opções
- Adote fluxos assíncronos padronizados nos SDKs:
  
  - Crawls: `startCrawl` + `getCrawlStatus` (ou o waiter `crawl`)
  - Batch: `startBatchScrape` + `getBatchScrapeStatus` (ou o waiter `batchScrape`)
  - Extract: `startExtract` + `getExtractStatus` (ou o waiter `extract`)
- Mapeamento de opções de crawl (veja abaixo)
- Verifique o `prompt` do crawl com `/crawl/params-preview`

## Interface do SDK (v2)

### JS/TS

#### Mudanças nos nomes dos métodos (migração v1 → v2)

**Scrape, Search e Map**

v1 (FirecrawlApp)v2 (Firecrawl)`scrapeUrl(url, ...)``scrape(url, options?)``search(query, ...)``search(query, options?)``mapUrl(url, ...)``map(url, options?)`

**Crawling**

v1v2`crawlUrl(url, ...)``crawl(url, options?)` (waiter)`asyncCrawlUrl(url, ...)``startCrawl(url, options?)``checkCrawlStatus(id, ...)``getCrawlStatus(id)``cancelCrawl(id)``cancelCrawl(id)``checkCrawlErrors(id)``getCrawlErrors(id)`

**Batch Scraping**

v1v2`batchScrapeUrls(urls, ...)``batchScrape(urls, opts?)` (waiter)`asyncBatchScrapeUrls(urls, ...)``startBatchScrape(urls, opts?)``checkBatchScrapeStatus(id, ...)``getBatchScrapeStatus(id)``checkBatchScrapeErrors(id)``getBatchScrapeErrors(id)`

**Extração**

v1v2`extract(urls?, params?)``extract(args)``asyncExtract(urls, params?)``startExtract(args)``getExtractStatus(id)``getExtractStatus(id)`

**Outros / Removidos**

v1v2`generateLLMsText(...)`(não está no SDK v2)`checkGenerateLLMsTextStatus(id)`(não está no SDK v2)`crawlUrlAndWatch(...)``watcher(jobId, ...)``batchScrapeUrlsAndWatch(...)``watcher(jobId, ...)`

* * *

### Python (sincrono)

#### Mudanças nos nomes dos métodos (migração v1 → v2)

**Scrape, Search e Map**

v1v2`scrape_url(...)``scrape(...)``search(...)``search(...)``map_url(...)``map(...)`

**Crawling**

v1v2`crawl_url(...)``crawl(...)` (waiter)`async_crawl_url(...)``start_crawl(...)``check_crawl_status(...)``get_crawl_status(...)``cancel_crawl(...)``cancel_crawl(...)`

**Scraping em lote**

v1v2`batch_scrape_urls(...)``batch_scrape(...)` (waiter)`async_batch_scrape_urls(...)``start_batch_scrape(...)``get_batch_scrape_status(...)``get_batch_scrape_status(...)``get_batch_scrape_errors(...)``get_batch_scrape_errors(...)`

**Extração**

v1v2`extract(...)``extract(...)``start_extract(...)``start_extract(...)``get_extract_status(...)``get_extract_status(...)`

**Outros / Removidos**

v1v2`generate_llms_text(...)`(não disponível no SDK v2)`get_generate_llms_text_status(...)`(não disponível no SDK v2)`watch_crawl(...)``watcher(job_id, ...)`

* * *

### Python (assíncrono)

- `AsyncFirecrawl` oferece os mesmos métodos (todos aguardáveis).

## Formatos e opções de scraping

- Use formatos de string para o básico: `"markdown"`, `"html"`, `"rawHtml"`, `"links"`, `"summary"`, `"images"`.
- Em vez de `parsePDF`, use `parsers: [ { "type": "pdf" } | "pdf" ]`.
- Use formatos de objeto para JSON, controle de alterações e capturas de tela:

### Formato JSON

### Formato de captura de tela

## Mapeamento de opções de rastreamento (v1 → v2)

v1v2`allowBackwardCrawling`(removido) use `crawlEntireDomain``maxDepth`(removido) use `maxDiscoveryDepth``ignoreSitemap` (bool)`sitemap` (por exemplo, “only”, “skip” ou “include”)(nenhum)`prompt`

## Visualização de prompt de crawl + parâmetros

Veja exemplos de visualização de parâmetros de crawl: