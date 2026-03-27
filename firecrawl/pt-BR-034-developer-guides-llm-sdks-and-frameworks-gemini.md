---
title: Gemini - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/gemini
source: sitemap
fetched_at: 2026-03-23T07:34:44.3608-03:00
rendered_js: false
word_count: 248
summary: This document provides a guide on integrating Firecrawl with Google Gemini to scrape web content and process it using generative AI models for summarization, analysis, and structured data extraction.
tags:
    - firecrawl
    - google-gemini
    - web-scraping
    - ai-integration
    - data-extraction
    - node-js
    - llm-workflows
category: tutorial
---

Integre o Firecrawl ao Gemini, da Google, para aplicativos de IA com dados da web.

## Configuração

```
npm install @mendable/firecrawl-js @google/genai
```

Crie o arquivo `.env`:

```
FIRECRAWL_API_KEY=sua_chave_firecrawl
GEMINI_API_KEY=sua_chave_gemini
```

> **Observação:** Se estiver usando Node &lt; 20, instale `dotenv` e adicione `import 'dotenv/config'` ao seu código.

## Scrape + Resumo

Este exemplo demonstra um fluxo de trabalho simples: fazer o scrape de um site e resumir o conteúdo com o Gemini.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Summarize: ${scrapeResult.markdown}`,
});

console.log('Summary:', response.text);
```

## Análise de Conteúdo

Este exemplo mostra como analisar o conteúdo de um site usando os recursos de conversa em múltiplas etapas do Gemini.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://news.ycombinator.com/', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const chat = ai.chats.create({
    model: 'gemini-2.5-flash'
});

// Ask for the top 3 stories on Hacker News
const result1 = await chat.sendMessage({
    message: `Based on this website content from Hacker News, what are the top 3 stories right now?\n\n${scrapeResult.markdown}`
});
console.log('Top 3 Stories:', result1.text);

// Solicita a 4ª e 5ª notícias do Hacker News
const result2 = await chat.sendMessage({
    message: `Now, what are the 4th and 5th top stories on Hacker News from the same content?`
});
console.log('4th and 5th Stories:', result2.text);
```

Este exemplo demonstra como extrair dados estruturados usando o modo JSON do Gemini a partir de conteúdo extraído de sites.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI, Type } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Comprimento do conteúdo extraído:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Extrair informações da empresa: ${scrapeResult.markdown}`,
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                name: { type: Type.STRING },
                industry: { type: Type.STRING },
                description: { type: Type.STRING },
                products: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING }
                }
            },
            propertyOrdering: ['name', 'industry', 'description', 'products']
        }
    }
});

console.log('Informações da empresa extraídas:', response?.text);
```

Para mais exemplos, consulte a [documentação do Gemini](https://ai.google.dev/docs).