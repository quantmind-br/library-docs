---
title: LangChain - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/langchain
source: sitemap
fetched_at: 2026-03-23T07:36:16.082349-03:00
rendered_js: false
word_count: 320
summary: Este documento explica cómo integrar Firecrawl con LangChain para automatizar el scraping de contenido web y procesarlo mediante modelos de lenguaje para análisis y extracción de datos estructurados.
tags:
    - web-scraping
    - langchain
    - data-extraction
    - ai-integration
    - node-js
    - structured-output
category: tutorial
---

Integra Firecrawl con LangChain para crear aplicaciones de IA impulsadas por datos de la web.

## Configuración

```
npm install @langchain/openai @mendable/firecrawl-js
```

Crea un archivo `.env`:

```
FIRECRAWL_API_KEY=tu_clave_firecrawl
OPENAI_API_KEY=tu_clave_openai
```

> **Nota:** Si usas Node &lt; 20, instala `dotenv` y añade `import 'dotenv/config'` a tu código.

## Scrape + Chat

Este ejemplo muestra un flujo de trabajo sencillo: realizar scraping de un sitio web y procesar el contenido con LangChain.

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

## Cadenas

Este ejemplo muestra cómo construir una cadena de LangChain para procesar y analizar contenido obtenido mediante *scraping*.

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

// Crear cadena de procesamiento
const prompt = ChatPromptTemplate.fromMessages([
    ['system', 'Eres un experto en analizar sitios web de empresas.'],
    ['user', 'Extrae el nombre de la empresa y los productos principales de: {content}']
]);

const chain = prompt.pipe(model).pipe(new StringOutputParser());

// Ejecutar la cadena
const result = await chain.invoke({
    content: scrapeResult.markdown
});

console.log('Chain result:', result);
```

Este ejemplo muestra cómo usar la funcionalidad de invocación de herramientas de LangChain para permitir que el modelo decida cuándo extraer datos de sitios web.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Crear la herramienta de scraping
const scrapeWebsiteTool = new DynamicStructuredTool({
    name: 'scrape_website',
    description: 'Scrape content from any website URL',
    schema: z.object({
        url: z.string().url().describe('The URL to scrape')
    }),
    func: async ({ url }) => {
        console.log('Scraping:', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('Vista previa del contenido scrapeado:', result.markdown?.substring(0, 200) + '...');
        return result.markdown || 'No se scrapeó contenido';
    }
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).bindTools([scrapeWebsiteTool]);

const response = await model.invoke('What is Firecrawl? Visit firecrawl.dev and tell me about it.');

console.log('Respuesta:', response.content);
console.log('Llamadas a herramientas:', response.tool_calls);
```

Este ejemplo muestra cómo extraer datos estructurados usando la funcionalidad de salida estructurada de LangChain.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Longitud del contenido scrapeado:', scrapeResult.markdown?.length);

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
        content: 'Extrae la información de la empresa del contenido del sitio web.'
    },
    {
        role: 'user',
        content: `Extrae los datos: ${scrapeResult.markdown}`
    }
]);

console.log('Información de la empresa extraída:', companyInfo);
```

Para ver más ejemplos, consulta la [documentación de LangChain](https://js.langchain.com/docs).