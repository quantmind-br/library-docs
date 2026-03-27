---
title: Scraping de Etsy - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/common-sites/etsy
source: sitemap
fetched_at: 2026-03-23T07:36:39.58174-03:00
rendered_js: false
word_count: 104
summary: This document provides a guide on using the Firecrawl SDK to extract, crawl, and map structured data from Etsy product listings and storefronts.
tags:
    - web-scraping
    - etsy-api
    - data-extraction
    - firecrawl-js
    - zod-validation
    - web-crawling
category: guide
---

## Configuración

```
npm install @mendable/firecrawl-js zod
```

## Descripción general

Al hacer scraping en Etsy, normalmente querrás:

- Extraer listados de productos y sus variaciones
- Obtener información de la tienda y valoraciones
- Monitorizar productos y categorías en tendencia
- Rastrear datos de precios y ventas
- Extraer opiniones de clientes

Extrae datos estructurados de listados usando esquemas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Definir esquema de Zod
const ListingSchema = z.object({
    title: z.string(),
    price: z.string(),
    shopName: z.string(),
    rating: z.number()
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ListingSchema)
    }],
});

// Parsear y validar con Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ Datos del listado validados:');
console.log(validated);
```

## Búsqueda

Busca productos en el mercado de Etsy.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('handmade jewelry site:etsy.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Extrae un único anuncio de producto de Etsy.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // p. ej. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubre todas las URL disponibles de una tienda o categoría de Etsy. Nota: Map solo devuelve URL, sin contenido.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// Devuelve un array de URLs sin contenido
```

## Crawl

Rastrea varias páginas de una tienda o categoría de Etsy.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.etsy.com/c/jewelry', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

Extrae varias URL de listados de Etsy simultáneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Esperar finalización
const job = await firecrawl.batchScrape([
    'https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set',
    'https://www.etsy.com/market/handmade_jewelry',
    'https://www.etsy.com/market/jewelry_handmade'],
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