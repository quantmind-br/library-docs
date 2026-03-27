---
title: Scraper Etsy - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/common-sites/etsy
source: sitemap
fetched_at: 2026-03-23T07:35:59.770652-03:00
rendered_js: false
word_count: 115
summary: This document demonstrates how to use the Firecrawl SDK to extract, map, and crawl data from Etsy listings and shop pages using structured schemas.
tags:
    - web-scraping
    - etsy-api
    - data-extraction
    - firecrawl-sdk
    - zod-validation
    - web-crawling
category: guide
---

## Configuration

```
npm install @mendable/firecrawl-js zod
```

## Vue d’ensemble

Lorsque vous scrappez Etsy, vous chercherez généralement à :

- Extraire les fiches produit et leurs variantes
- Récupérer les informations sur les boutiques et leurs évaluations
- Suivre les articles et catégories tendance
- Suivre les prix et les données de vente
- Extraire les avis clients

Extrayez des données structurées de type listing à l’aide de schémas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Définir le schéma Zod
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

// Analyser et valider avec Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ListingSchema.parse(jsonData);

console.log('✅ Données de l'annonce validées :');
console.log(validated);
```

## Recherche

Trouvez des produits sur la marketplace Etsy.

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

Scraper une seule fiche produit Etsy.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.etsy.com/listing/1844315896/handmade-925-sterling-silver-jewelry-set', {
    formats: ['markdown'], // par ex. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Découvrez toutes les URL disponibles dans une boutique ou une catégorie Etsy. Remarque : Map renvoie uniquement les URL, sans leur contenu.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.etsy.com/shop/YourShopName');

console.log(mapResult.links);
// Renvoie un tableau d'URL sans contenu
```

## Crawl

Explorer plusieurs pages d’une boutique ou d’une catégorie Etsy.

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

## Scraping par lot

Extraire plusieurs URL d’annonces Etsy simultanément.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Attendre la fin
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