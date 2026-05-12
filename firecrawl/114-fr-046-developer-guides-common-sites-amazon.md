---
title: Scraper Amazon - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/common-sites/amazon
source: sitemap
fetched_at: 2026-03-23T07:36:03.885505-03:00
rendered_js: false
word_count: 117
summary: This document provides a technical guide on using the Firecrawl SDK to scrape, map, and crawl Amazon product data, including methods for structured data extraction using Zod schemas.
tags:
    - web-scraping
    - firecrawl
    - data-extraction
    - amazon-scraping
    - zod-validation
    - node-js
category: guide
---

## Configuration

```
npm install @mendable/firecrawl-js zod
```

## Aperçu

Lors du scraping d’Amazon, vous chercherez généralement à :

- Extraire les informations sur le produit (titre, prix, disponibilité)
- Récupérer les avis et notes des clients
- Surveiller les variations de prix
- Rechercher des produits de manière programmatique
- Suivre les fiches produits des concurrents

Extrayez des données produit structurées à l’aide de schémas Zod.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { z } from 'zod';

// Définir le schéma Zod
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

// Parser et valider avec Zod
const jsonData = typeof result.json === 'string' ? JSON.parse(result.json) : result.json;
const validated = ProductSchema.parse(jsonData);

console.log('✅ Données produit validées :');
console.log(validated);
```

## Recherche

Rechercher des produits sur Amazon.

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

Récupérer les données d’une seule page produit Amazon.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await firecrawl.scrape('https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L', {
    formats: ['markdown'], // par ex. html, links, etc.
    onlyMainContent: true
});

console.log(result);
```

## Map

Découvrez toutes les URL disponibles sur les pages de produit ou de catégorie Amazon. Remarque : Map retourne uniquement des URL, sans contenu.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const mapResult = await firecrawl.map('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics');

console.log(mapResult.links);
// Renvoie un tableau d'URL sans contenu
```

## Crawl

Explorer plusieurs pages issues d’une catégorie Amazon ou de résultats de recherche Amazon.

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

## Scraping par lots

Scraper plusieurs URL de produits Amazon simultanément.

```
import FirecrawlApp from '@mendable/firecrawl-js';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Attendre la fin
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