---
title: Anthropic - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/anthropic
source: sitemap
fetched_at: 2026-03-23T07:35:44.610908-03:00
rendered_js: false
word_count: 299
summary: This document demonstrates how to integrate Firecrawl with the Anthropic Claude API to scrape website content for summarization, tool-based retrieval, and structured data extraction.
tags:
    - web-scraping
    - ai-integration
    - node-js
    - claude-api
    - data-extraction
    - firecrawl
category: tutorial
---

Intégrez Firecrawl à Claude pour créer des applications d’IA alimentées par des données web.

## Configuration

```
npm install @mendable/firecrawl-js @anthropic-ai/sdk zod zod-to-json-schema
```

Créez un fichier `.env` :

```
FIRECRAWL_API_KEY=votre_clé_firecrawl
ANTHROPIC_API_KEY=votre_clé_anthropic
```

> **Remarque :** Si vous utilisez Node &lt; 20, installez `dotenv` et ajoutez `import 'dotenv/config'` à votre code.

Cet exemple illustre un flux de travail simple : extraire un site web et en résumer le contenu à l’aide de Claude.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: `Summarize in 100 words: ${scrapeResult.markdown}` }
    ]
});

console.log('Response:', message);
```

Cet exemple montre comment utiliser la fonctionnalité d’outils de Claude pour laisser le modèle décider quand scraper des sites web en fonction des requêtes des utilisateurs.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { Anthropic } from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const firecrawl = new FirecrawlApp({
    apiKey: process.env.FIRECRAWL_API_KEY
});

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
});

const ScrapeArgsSchema = z.object({
    url: z.string()
});

console.log("Envoi du message utilisateur à Claude et demande d'utilisation d'outil si nécessaire...");
const response = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    tools: [{
        name: 'scrape_website',
        description: 'Scraper et extraire le contenu markdown d'une URL de site web',
        input_schema: zodToJsonSchema(ScrapeArgsSchema, 'ScrapeArgsSchema') as any
    }],
    messages: [{
        role: 'user',
        content: 'Qu'est-ce que Firecrawl ? Vérifiez firecrawl.dev'
    }]
});

const toolUse = response.content.find(block => block.type === 'tool_use');

if (toolUse && toolUse.type === 'tool_use') {
    const input = toolUse.input as { url: string };
    console.log(`Appel de l'outil : ${toolUse.name} | URL : ${input.url}`);

    const result = await firecrawl.scrape(input.url, {
        formats: ['markdown']
    });

    console.log(`Aperçu du contenu scrapé : ${result.markdown?.substring(0, 300)}...`);
    // Continuer la conversation ou traiter le contenu scrapé selon les besoins
}
```

Cet exemple montre comment utiliser Claude pour extraire des données structurées à partir de contenu de sites web exploré.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string().optional(),
    description: z.string().optional()
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown'],
    onlyMainContent: true
});

const prompt = `Extrayez les informations de l'entreprise à partir du contenu de ce site web.

Sortie UNIQUEMENT en JSON valide dans ce format exact (pas de markdown, pas d'explication) :

{
  "name": "Nom de l'entreprise",
  "industry": "Secteur",
  "description": "Description en une phrase"
}

Contenu du site web :
${scrapeResult.markdown}`;

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: prompt },
        { role: 'assistant', content: '{' }
    ]
});

const textBlock = message.content.find(block => block.type === 'text');

if (textBlock && textBlock.type === 'text') {
    const jsonText = '{' + textBlock.text;
    const companyInfo = CompanyInfoSchema.parse(JSON.parse(jsonText));

    console.log(companyInfo);
}
```

Pour plus d’exemples, consultez la [documentation de Claude](https://docs.anthropic.com/claude/docs).