---
title: Scraping na Amazon - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/common-sites/amazon
source: sitemap
fetched_at: 2026-03-23T07:35:00.199486-03:00
rendered_js: false
word_count: 110
summary: This document provides a guide on how to perform web scraping and data extraction from Amazon using the Firecrawl API and Zod for schema validation.
tags:
    - web-scraping
    - firecrawl
    - amazon-data
    - data-extraction
    - zod-validation
    - node-js
category: guide
---

## Configuração

```
npm install @mendable/firecrawl-js zod
```

## Visão geral

Ao fazer scraping na Amazon, você normalmente vai querer:

- Extrair informações de produtos (título, preço, disponibilidade)
- Obter avaliações e notas de clientes
- Monitorar variações de preço
- Pesquisar produtos de forma programática
- Acompanhar as listagens de concorrentes

Extraia dados estruturados de produtos usando esquemas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Definir schema Zod
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

// Fazer parse e validar com Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ Dados do produto validados:');
console.log(validated);
```

## Busca

Encontre produtos na Amazon.

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

## Scrape

Raspe uma única página de produto da Amazon.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // ex.: html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubra todas as URLs disponíveis em páginas de produtos ou categorias da Amazon. Observação: o Map retorna apenas URLs, sem conteúdo.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// Retorna um array de URLs sem conteúdo
```

## Crawl

Rastreie várias páginas de uma categoria ou de resultados de pesquisa da Amazon.

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

## Scraping em lote

Faça scraping de várias URLs de produtos da Amazon simultaneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Aguarda a conclusão
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