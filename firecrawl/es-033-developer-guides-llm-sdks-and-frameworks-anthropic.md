---
title: Anthropic - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/anthropic
source: sitemap
fetched_at: 2026-03-23T07:36:26.445068-03:00
rendered_js: false
word_count: 285
summary: This document provides a guide on integrating Firecrawl with the Anthropic Claude API to perform web scraping, summarize content, use autonomous tool-calling, and extract structured data from websites.
tags:
    - web-scraping
    - claude-api
    - data-extraction
    - ai-integration
    - firecrawl
    - node-js
    - structured-data
category: guide
---

Integra Firecrawl con Claude para crear aplicaciones de IA impulsadas por datos de la web.

## Configuración

```
npm install @mendable/firecrawl-js @anthropic-ai/sdk zod zod-to-json-schema
```

Crea un archivo `.env`:

```
FIRECRAWL_API_KEY=tu_clave_firecrawl
ANTHROPIC_API_KEY=tu_clave_anthropic
```

> **Nota:** Si usas Node &lt; 20, instala `dotenv` y añade `import 'dotenv/config'` a tu código.

## Scrapear + resumir

Este ejemplo muestra un flujo de trabajo sencillo: scrapear un sitio web y resumir su contenido con Claude.

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

Este ejemplo muestra cómo usar la funcionalidad de herramientas de Claude para permitir que el modelo decida cuándo hacer scraping de sitios web en función de las solicitudes del usuario.

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

console.log("Enviando mensaje de usuario a Claude y solicitando uso de herramienta si es necesario...");
const response = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    tools: [{
        name: 'scrape_website',
        description: 'Extrae contenido markdown de una URL de sitio web',
        input_schema: zodToJsonSchema(ScrapeArgsSchema, 'ScrapeArgsSchema') as any
    }],
    messages: [{
        role: 'user',
        content: '¿Qué es Firecrawl? Consulta firecrawl.dev'
    }]
});

const toolUse = response.content.find(block => block.type === 'tool_use');

if (toolUse && toolUse.type === 'tool_use') {
    const input = toolUse.input as { url: string };
    console.log(`Llamando herramienta: ${toolUse.name} | URL: ${input.url}`);

    const result = await firecrawl.scrape(input.url, {
        formats: ['markdown']
    });

    console.log(`Vista previa del contenido extraído: ${result.markdown?.substring(0, 300)}...`);
    // Continuar con la conversación o procesar el contenido extraído según sea necesario
}
```

Este ejemplo muestra cómo utilizar Claude para extraer datos estructurados a partir de contenido de sitios web obtenido mediante scraping.

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

const prompt = `Extract company information from this website content.

Output ONLY valid JSON in this exact format (no markdown, no explanation):

{
  "name": "Company Name",
  "industry": "Industry",
  "description": "One sentence description"
}

Website content:
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

Para ver más ejemplos, consulta la [documentación de Claude](https://docs.anthropic.com/claude/docs).