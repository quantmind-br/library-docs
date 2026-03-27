---
title: LangChain - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/langchain
source: sitemap
fetched_at: 2026-03-23T07:36:01.832431-03:00
rendered_js: false
word_count: 324
summary: This document provides a guide on integrating the Firecrawl web scraping service with the LangChain framework to build data-driven AI applications. It demonstrates workflows for scraping, processing, tool calling, and structured data extraction.
tags:
    - firecrawl
    - langchain
    - web-scraping
    - ai-development
    - data-extraction
    - llm-integration
    - node-js
category: guide
---

Intégrez Firecrawl à LangChain pour créer des applications d’IA alimentées par des données web.

## Configuration

```
npm install @langchain/openai @mendable/firecrawl-js
```

Créez le fichier `.env` :

```
FIRECRAWL_API_KEY=votre_clé_firecrawl
OPENAI_API_KEY=votre_clé_openai
```

> **Remarque :** Si vous utilisez Node &lt; 20, installez `dotenv` et ajoutez `import 'dotenv/config'` à votre code.

## Scrape + Chat

Cet exemple illustre un workflow simple : extraire les données d’un site web, puis traiter le contenu avec LangChain.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { HumanMessage } from '@langchain/core/messages';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const chat = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await chat.invoke([
    new HumanMessage(`Summarize: ${scrapeResult.markdown}`)
]);

console.log('Summary:', response.content);
```

## Chaînes

Cet exemple illustre comment construire une chaîne LangChain pour traiter et analyser le contenu récupéré par scraping.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { StringOutputParser } from '@langchain/core/output_parsers';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

// Créer la chaîne de traitement
const prompt = ChatPromptTemplate.fromMessages([
    ['system', 'Vous êtes un expert en analyse de sites web d'entreprise.'],
    ['user', 'Extrayez le nom de l'entreprise et les principaux produits de : {content}']
]);

const chain = prompt.pipe(model).pipe(new StringOutputParser());

// Exécuter la chaîne
const result = await chain.invoke({
    content: scrapeResult.markdown
});

console.log('Chain result:', result);
```

Cet exemple montre comment utiliser la fonction de tool calling de LangChain pour laisser le modèle décider quand scraper des sites web.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Créer l'outil de scraping
const scrapeWebsiteTool = new DynamicStructuredTool({
    name: 'scrape_website',
    description: 'Scraper le contenu de n'importe quelle URL de site web',
    schema: z.object({
        url: z.string().url().describe('L'URL à scraper')
    }),
    func: async ({ url }) => {
        console.log('Scraping :', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('Aperçu du contenu scrapé :', result.markdown?.substring(0, 200) + '...');
        return result.markdown || 'Aucun contenu scrapé';
    }
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).bindTools([scrapeWebsiteTool]);

const response = await model.invoke('Qu'est-ce que Firecrawl ? Visite firecrawl.dev et dis-moi de quoi il s'agit.');

console.log('Réponse :', response.content);
console.log('Appels d'outils :', response.tool_calls);
```

Cet exemple illustre comment extraire des données structurées en utilisant la fonctionnalité de sortie structurée de LangChain.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Longueur du contenu extrait :', scrapeResult.markdown?.length);

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string(),
    description: z.string(),
    products: z.array(z.string())
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).withStructuredOutput(CompanyInfoSchema);

const companyInfo = await model.invoke([
    {
        role: 'system',
        content: 'Extraire les informations de l'entreprise à partir du contenu du site web.'
    },
    {
        role: 'user',
        content: `Extraire les données : ${scrapeResult.markdown}`
    }
]);

console.log('Informations de l'entreprise extraites :', companyInfo);
```

Pour d’autres exemples, consultez la [documentation de LangChain](https://js.langchain.com/docs).