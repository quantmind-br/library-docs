---
title: Scraper GitHub - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/common-sites/github
source: sitemap
fetched_at: 2026-03-23T07:33:06.066419-03:00
rendered_js: false
word_count: 121
summary: This document provides a technical guide on using the Firecrawl SDK to extract, crawl, and map data from GitHub repositories, issues, and documentation.
tags:
    - firecrawl
    - web-scraping
    - github-api
    - data-extraction
    - json-schema
    - node-js
category: guide
---

Découvrez comment utiliser les fonctionnalités clés de Firecrawl pour scraper des dépôts, des issues et la documentation de GitHub.

## Configuration

```
npm install @mendable/firecrawl-js zod
```

## Scrape en mode JSON

Extraire des données structurées à partir de dépôts en utilisant des schémas Zod.

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

Rechercher des dépôts, des tickets ou de la documentation sur GitHub.

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

Extraire une seule page GitHub – dépôt, ticket ou fichier.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: ['markdown'] // par ex. html, links, etc.
});

console.log(result);
```

## Map

Découvrez toutes les URL disponibles dans un dépôt ou un site de documentation. Remarque : Map ne renvoie que les URL, sans contenu.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// Retourne un tableau d'URL sans contenu
```

## Crawl

Explorer plusieurs pages d’un dépôt ou d’une documentation.

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

## Scrape par lots

Extraire plusieurs URL GitHub simultanément.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Attendre la fin
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

## Scraping par lots avec le mode JSON

Extrayez des données structurées à partir de plusieurs dépôts en une seule opération.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Attendre la fin
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