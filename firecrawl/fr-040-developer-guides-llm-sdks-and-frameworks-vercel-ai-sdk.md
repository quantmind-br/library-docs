---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:15.296005-03:00
rendered_js: false
word_count: 205
summary: This document provides a technical guide on integrating Firecrawl tools with the Vercel AI SDK to perform web scraping, searching, browsing, and autonomous data collection for AI applications.
tags:
    - firecrawl
    - vercel-ai-sdk
    - web-scraping
    - llm-agents
    - browser-automation
    - data-extraction
    - typescript
category: guide
---

Outils Firecrawl pour Vercel AI SDK. Effectuez du web scraping, recherchez, naviguez et extrayez des données web dans vos applications d’IA.

## Installation

```
npm install firecrawl-aisdk ai
```

Configurez les variables d’environnement :

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## Démarrage rapide

La manière la plus simple de démarrer. `FirecrawlTools()` vous fournit des outils de recherche, de scraping et de navigation avec une invite système générée automatiquement qui guide le modèle dans le choix des outils.

```
import { generateText, stepCountIs } from 'ai';
import { FirecrawlTools } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and summarize what it does',
  tools: FirecrawlTools(),
  stopWhen: stepCountIs(5),
});
```

Avec des options personnalisées :

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // optionnel, utilise la variable d'environnement par défaut
  search: { limit: 3, country: 'US' },    // options de recherche par défaut
  scrape: { onlyMainContent: true },       // options de scraping par défaut
  browser: {},                             // activer l'outil navigateur
});
```

Désactivez un outil en passant `false`\\u00a0:

```
const tools = FirecrawlTools({
  browser: false,   // recherche + scraping uniquement
});
```

Chaque outil est **à double usage** : vous pouvez l’utiliser directement comme outil (il lit `FIRECRAWL_API_KEY` depuis les variables d’environnement) ou l’appeler comme factory pour une configuration personnalisée :

```
import { scrape, search } from 'firecrawl-aisdk';

// Utilisation directe - lit FIRECRAWL_API_KEY depuis l'environnement
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// Ou appeler comme factory pour une configuration personnalisée
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});
```

### Scraping

```
import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev et résume ce que ça fait',
  tools: { scrape },
});
```

### Recherche

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Recherchez Firecrawl et résumez ce que vous trouvez',
  tools: { search },
});

import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Recherche Firecrawl, scrape le premier résultat et explique ce qu'il fait',
  tools: { search, scrape },
});
```

### Cartographie

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Map https://docs.firecrawl.dev and list the main sections',
  tools: { map },
});
```

### Streaming

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and explain what it does',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Navigateur

L’outil de navigation crée automatiquement une session dans le cloud lors de sa première utilisation et la supprime à la fin du processus :

```
import { generateText, stepCountIs } from 'ai';
import { browser } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser() },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});
```

Pour obtenir une URL de vue en direct (pour suivre le navigateur en temps réel) ou contrôler manuellement le cycle de vie de la session :

```
const browserTool = browser();
console.log('Live view:', await browserTool.start());

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browserTool },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});

await browserTool.close();
```

### Navigateur + Recherche

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: 'Search for the top AI paper this week, browse it, and summarize the key findings.',
});
```

Crawl, batch scrape, extract et agent renvoient un identifiant de tâche. Associez-les à `poll` pour récupérer les résultats :

### Crawl

```
import { generateText } from 'ai';
import { crawl, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Crawl https://docs.firecrawl.dev (limit 3 pages) and summarize',
  tools: { crawl, poll },
});
```

### Scraping par lots

```
import { generateText } from 'ai';
import { batchScrape, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and https://docs.firecrawl.dev, then compare',
  tools: { batchScrape, poll },
});
```

### Agent

Collecte autonome de données sur le web – recherche, navigue et extrait des données en toute autonomie.

```
import { generateText, stepCountIs } from 'ai';
import { agent, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Trouve les fondateurs de Firecrawl, leurs rôles et leurs parcours',
  tools: { agent, poll },
  stopWhen: stepCountIs(10),
});
```

## Toutes les exportations

```
import {
  // Outils polyvalents (utilisation directe ou en tant que factory)
  scrape,             // Scraper une seule URL
  search,             // Rechercher sur le web
  map,                // Découvrir les URL d'un site
  crawl,              // Crawler plusieurs pages (async)
  batchScrape,        // Scraper plusieurs URL (async)
  agent,              // Agent web autonome (async)
  extract,            // Extraire des données structurées (async)

  // Gestion des jobs
  poll,               // Interroger les jobs async pour obtenir les résultats
  status,             // Vérifier le statut d'un job
  cancel,             // Annuler les jobs en cours

  // Navigateur (factory uniquement)
  browser,            // browser({ firecrawlApiKey: '...' })

  // Bundle tout-en-un
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // Utilitaires
  stepLogger,         // Statistiques de tokens par appel d'outil
  logStep,            // Journalisation simple en une ligne
} from 'firecrawl-aisdk';
```