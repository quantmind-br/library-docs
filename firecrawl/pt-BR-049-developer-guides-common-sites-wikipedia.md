---
title: Raspando a Wikipédia - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/common-sites/wikipedia
source: sitemap
fetched_at: 2026-03-23T07:34:49.103115-03:00
rendered_js: false
word_count: 118
summary: This document provides a guide on how to use the Firecrawl SDK to extract, scrape, and crawl structured and unstructured data from Wikipedia for research and AI applications.
tags:
    - web-scraping
    - data-extraction
    - firecrawl
    - wikipedia
    - automation
    - structured-data
    - node-js
category: tutorial
---

Aprenda a raspar a Wikipédia de forma eficaz para pesquisa, extração de conhecimento e criação de aplicações de IA.

## Configuração

```
npm install @mendable/firecrawl-js zod
```

## Casos de uso

- Automação de pesquisas e verificação de fatos
- Construção de grafos de conhecimento
- Extração de conteúdo multilíngue
- Agregação de conteúdo educacional
- Extração de informações sobre entidades

## Fazer scraping no modo JSON

Extraia dados estruturados de artigos da Wikipédia usando schemas do Zod.

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

## Busca

Encontre artigos na Wikipédia.

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

Faça o scraping de um único artigo da Wikipedia.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // ex.: html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Descubra todas as URLs disponíveis em um portal ou categoria da Wikipédia. Observação: Map retorna apenas URLs, sem conteúdo.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// Retorna array de URLs sem conteúdo
```

## Crawl

Rastreie várias páginas de documentação ou categorias na Wikipédia.

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

## Coleta em Lote

Raspe várias URLs da Wikipédia simultaneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Aguarda a conclusão
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