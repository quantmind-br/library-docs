---
title: Scraping en Amazon - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/common-sites/amazon
source: sitemap
fetched_at: 2026-03-23T07:36:35.587569-03:00
rendered_js: false
word_count: 105
summary: This document provides a guide on using the Firecrawl SDK to scrape, search, and map Amazon product data using Zod schemas for structured extraction.
tags:
    - web-scraping
    - amazon-data
    - data-extraction
    - firecrawl-api
    - zod-validation
    - web-crawling
category: guide
---

## Configuración

```
npm install @mendable/firecrawl-js zod
```

## Descripción general

Al extraer datos de Amazon, normalmente querrás:

- Extraer información de productos (título, precio, disponibilidad)
- Obtener reseñas y valoraciones de clientes
- Supervisar cambios de precio
- Buscar productos de forma programática
- Rastrear listados de competidores

Extrae datos de productos estructurados usando esquemas de Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Definir esquema de Zod
const ProductSchema = z.object({
    title: z.string(),
    price: z.string(),
    rating: z.number(),
    availability: z.string(),
    features: z.array(z.string())
});

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/dp/B0DZZWMB2L', {
    formats: [{
        type: 'json',
        schema: z.toJSONSchema(ProductSchema)
    }],
});

// Parsear y validar con Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ Datos del producto validados:');
console.log(validated);
```

## Búsqueda

Busca productos en Amazon.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('gaming laptop site:amazon.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

Extrae datos de una única página de producto de Amazon.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // p. ej. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubre todas las URL disponibles en páginas de producto o de categoría de Amazon. Nota: Map solo devuelve las URL, sin contenido.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// Devuelve un array de URLs sin contenido
```

## Rastreo

Rastrea varias páginas de categorías o resultados de búsqueda de Amazon.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://www.amazon.com/s?k=mechanical+keyboards', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

Extrae varias URL de productos de Amazon a la vez.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Esperar finalización
const job = await firecrawl.batchScrape([
    'https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L',
    'https://www.amazon.com/Razer-Blade-Gaming-Laptop-Lightweight/dp/B0FP47DNFQ',
    'https://www.amazon.com/HP-2025-Omen-Gaming-Laptop/dp/B0FL4RMGSH'],
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