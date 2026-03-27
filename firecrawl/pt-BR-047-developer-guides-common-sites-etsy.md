---
title: Scrapear o Etsy - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/common-sites/etsy
source: sitemap
fetched_at: 2026-03-23T07:34:55.451355-03:00
rendered_js: false
word_count: 114
summary: This document provides a guide on using the Firecrawl SDK to scrape, map, and crawl data from Etsy listings and shops using Node.js.
tags:
    - firecrawl
    - web-scraping
    - etsy-api
    - data-extraction
    - javascript
    - zod-validation
category: guide
---

## Configuração

```
npm install @mendable/firecrawl-js zod
```

## Visão geral

Ao fazer scraping no Etsy, você normalmente vai querer:

- Extrair anúncios de produtos e variações
- Obter informações e avaliações da loja
- Monitorar itens e categorias em alta
- Acompanhar dados de preços e vendas
- Extrair avaliações de clientes

## Raspagem no modo JSON

Extraia dados estruturados de listagens usando esquemas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Definir esquema Zod
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

// Analisar e validar com Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ Dados da listagem validados:');
console.log(validated);
```

## Busca

Encontre produtos na Etsy.

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

Extraia os dados de um único anúncio de produto no Etsy.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // ex.: html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubra todas as URLs disponíveis em uma loja ou categoria no Etsy. Observação: o Map retorna apenas URLs, sem conteúdo.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// Retorna um array de URLs sem conteúdo
```

## Crawl

Rastreie várias páginas de uma loja ou categoria no Etsy.

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

## Coleta em Lote

Extraia dados de várias URLs de anúncios do Etsy simultaneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Aguardar conclusão
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