---
title: Scraping de Wikipedia - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/common-sites/wikipedia
source: sitemap
fetched_at: 2026-03-23T07:36:38.065767-03:00
rendered_js: false
word_count: 118
summary: This document provides a guide on using the Firecrawl SDK to scrape, map, and crawl Wikipedia content for data extraction and research applications.
tags:
    - web-scraping
    - wikipedia
    - data-extraction
    - firecrawl
    - javascript
    - automation
    - api-integration
category: guide
---

Aprende a hacer scraping de Wikipedia de forma efectiva para investigación, extracción de conocimiento y creación de aplicaciones de IA.

## Configuración

```
npm install @mendable/firecrawl-js zod
```

## Casos de uso

- Automatización de la investigación y verificación de datos
- Creación de gráficos de conocimiento
- Extracción de contenido multilingüe
- Agregación de contenido educativo
- Extracción de información sobre entidades

## Rastrear con modo JSON

Extrae datos estructurados de artículos de Wikipedia usando esquemas de Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/JavaScript', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            creator: z.string(),
            firstAppeared: z.string(),
            typingDiscipline: z.string(),
            website: z.string()
        })
    }]
});

console.log(result.json);
```

## Buscar

Busca artículos en Wikipedia.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('quantum computing site:en.wikipedia.org', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Extrae datos de un único artículo de Wikipedia.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // p. ej. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubre todas las URLs disponibles en un portal o categoría de Wikipedia. Nota: Map solo devuelve URLs, sin contenido.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// Devuelve un array de URLs sin contenido
```

## Crawl

Rastrea varias páginas de la documentación de Wikipedia o de sus categorías.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://en.wikipedia.org/wiki/Portal:Artificial_intelligence', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

Extrae varias URL de Wikipedia simultáneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Esperar finalización
const job = await firecrawl.batchScrape([
    'https://en.wikipedia.org/wiki/Machine_learning',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://en.wikipedia.org/wiki/Deep_learning'],
    {
        options: {
            formats: ['markdown']
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```