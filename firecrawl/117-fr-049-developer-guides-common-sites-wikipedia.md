---
title: Scraper Wikipédia - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/common-sites/wikipedia
source: sitemap
fetched_at: 2026-03-23T07:36:04.474405-03:00
rendered_js: false
word_count: 112
summary: This document provides a technical guide on using the Firecrawl SDK to scrape, map, and extract structured data from Wikipedia for research and AI application development.
tags:
    - web-scraping
    - wikipedia
    - data-extraction
    - firecrawl
    - node-js
    - structured-data
category: guide
---

Apprenez à scraper Wikipédia efficacement pour la recherche, l’extraction de connaissances et la création d’applications d’IA.

## Configuration

```
npm install @mendable/firecrawl-js zod
```

## Cas d’utilisation

- Automatisation de la recherche et vérification des informations
- Construction de graphes de connaissances
- Extraction multilingue de contenus
- Agrégation de contenus éducatifs
- Extraction d’informations sur les entités

## Scraper en mode JSON

Extrayez des données structurées à partir d’articles Wikipédia à l’aide de schémas Zod.

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

## Recherche

Recherchez des articles sur Wikipédia.

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

Récupérer un seul article Wikipédia.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    formats: ['markdown'], // par ex. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Découvrez toutes les URL disponibles dans un portail ou une catégorie Wikipédia. Remarque : Map retourne uniquement des URL, sans leur contenu.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://en.wikipedia.org/wiki/Portal:Computer_science');

console.log(mapResult.links);
// Renvoie un tableau d'URL sans contenu
```

## Crawl

Crawlez plusieurs pages de documentation ou de catégories Wikipédia.

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

Extraire plusieurs URL Wikipédia simultanément.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Attendre la fin
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