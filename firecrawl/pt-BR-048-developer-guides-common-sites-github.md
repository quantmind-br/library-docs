---
title: Scrapear o GitHub - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/common-sites/github
source: sitemap
fetched_at: 2026-03-23T07:32:39.532601-03:00
rendered_js: false
word_count: 106
summary: This guide provides instructions on using the Firecrawl SDK to perform web scraping, crawling, and structured data extraction from GitHub repositories, issues, and documentation.
tags:
    - firecrawl
    - web-scraping
    - github-api
    - data-extraction
    - typescript
    - zod
    - automation
category: guide
---

Aprenda a usar os recursos principais do Firecrawl para scrapear repositórios, issues e documentação do GitHub.

## Configuração

```
npm install @mendable/firecrawl-js zod
```

Extraia dados estruturados de repositórios usando esquemas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: [{
        type: 'json',
        schema: z.object({
            name: z.string(),
            description: z.string(),
            stars: z.number(),
            forks: z.number(),
            language: z.string(),
            topics: z.array(z.string())
        })
    }]
});

console.log(result.json);
```

## Search

Pesquise repositórios, issues ou documentação no GitHub.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const searchResult = await firecrawl.search('machine learning site:github.com', {
    limit: 10,
    sources: [{ type: 'web' }], // { type: 'news' }, { type: 'images' }
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(searchResult);
```

## Scrape

Fazer scraping de uma única página do GitHub — repositório, issue ou arquivo.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: ['markdown'] // ex.: html, links, etc.
});

console.log(result);
```

## Map

Descubra todas as URLs disponíveis em um repositório ou site de documentação. Nota: Map retorna somente URLs, sem conteúdo.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// Retorna array de URLs sem conteúdo
```

## Crawl

Fazer crawling de várias páginas de um repositório ou documentação.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const crawlResult = await firecrawl.crawl('https://github.com/facebook/react/wiki', {
    limit: 10,
    scrapeOptions: {
        formats: ['markdown']
    }
});

console.log(crawlResult.data);
```

## Scrape em lote

Fazer scraping de várias URLs do GitHub simultaneamente.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Aguardar a conclusão
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react',
    'https://github.com/microsoft/typescript'],
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

## Raspagem em lote com o modo JSON

Extraia dados estruturados de vários repositórios de uma só vez.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Aguardar conclusão
const job = await firecrawl.batchScrape([
    'https://github.com/vercel/next.js',
    'https://github.com/facebook/react'],
    {
        options: {
            formats: [{
                type: 'json',
                schema: z.object({
                    name: z.string(),
                    description: z.string(),
                    stars: z.number(),
                    language: z.string()
                })
            }]
        },
        pollInterval: 2,
        timeout: 120
    }
);


console.log(job.status, job.completed, job.total);

console.log(job);
```