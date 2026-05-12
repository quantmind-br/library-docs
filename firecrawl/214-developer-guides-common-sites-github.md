---
title: Scraping GitHub - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/common-sites/github
source: sitemap
fetched_at: 2026-03-23T07:33:33.299853-03:00
rendered_js: false
word_count: 93
summary: This document provides a comprehensive guide on utilizing Firecrawl to scrape, map, crawl, and extract structured data from GitHub repositories and documentation sites.
tags:
    - web-scraping
    - github-integration
    - data-extraction
    - structured-data
    - api-tutorial
    - crawl-automation
category: tutorial
---

Learn how to use Firecrawl’s core features to scrape GitHub repositories, issues, and documentation.

## Setup

```
npm install @mendable/firecrawl-js zod
```

## Scrape with JSON Mode

Extract structured data from repositories using Zod schemas.

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

Find repositories, issues, or documentation on GitHub.

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

Scrape a single GitHub page - repository, issue, or file.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://github.com/firecrawl/firecrawl', {
    formats: ['markdown'] // i.e. html, links, etc.
});

console.log(result);
```

## Map

Discover all available URLs in a repository or documentation site. Note: Map returns URLs only, without content.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://github.com/vercel/next.js/tree/canary/docs');

console.log(mapResult.links);
// Returns array of URLs without content
```

## Crawl

Crawl multiple pages from a repository or documentation.

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

## Batch Scrape

Scrape multiple GitHub URLs simultaneously.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
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

## Batch Scrape with JSON Mode

Extract structured data from multiple repositories at once.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Wait for completion
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