---
title: LangChain - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/langchain
source: sitemap
fetched_at: 2026-03-23T07:34:29.107345-03:00
rendered_js: false
word_count: 321
summary: This document provides a guide on integrating Firecrawl with LangChain to enable web scraping and data processing within AI applications.
tags:
    - web-scraping
    - langchain
    - data-extraction
    - ai-integration
    - node-js
    - structured-output
category: guide
---

Integre o Firecrawl ao LangChain para criar aplicativos de IA alimentados por dados da web.

## Configuração

```
npm install @langchain/openai @mendable/firecrawl-js
```

Crie o arquivo `.env`:

```
FIRECRAWL_API_KEY=sua_chave_firecrawl
OPENAI_API_KEY=sua_chave_openai
```

> **Observação:** Se estiver usando Node &lt; 20, instale `dotenv` e adicione `import 'dotenv/config'` ao seu código.

## Scrape + Chat

Este exemplo demonstra um fluxo de trabalho simples: fazer scraping de um site e processar o conteúdo com o LangChain.

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

## Chains

Este exemplo mostra como criar uma chain no LangChain para processar e analisar o conteúdo extraído.

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

// Criar cadeia de processamento
const prompt = ChatPromptTemplate.fromMessages([
    ['system', 'Você é um especialista em análise de sites de empresas.'],
    ['user', 'Extraia o nome da empresa e os principais produtos de: {content}']
]);

const chain = prompt.pipe(model).pipe(new StringOutputParser());

// Executar a cadeia
const result = await chain.invoke({
    content: scrapeResult.markdown
});

console.log('Chain result:', result);
```

Este exemplo demonstra como usar o recurso de chamada de ferramentas do LangChain para permitir que o modelo decida quando fazer scraping de sites.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { DynamicStructuredTool } from '@langchain/core/tools';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Cria a ferramenta de scraping
const scrapeWebsiteTool = new DynamicStructuredTool({
    name: 'scrape_website',
    description: 'Extrai conteúdo de qualquer URL de site',
    schema: z.object({
        url: z.string().url().describe('A URL para extrair')
    }),
    func: async ({ url }) => {
        console.log('Extraindo:', url);
        const result = await firecrawl.scrape(url, {
            formats: ['markdown']
        });
        console.log('Prévia do conteúdo extraído:', result.markdown?.substring(0, 200) + '...');
        return result.markdown || 'Nenhum conteúdo extraído';
    }
});

const model = new ChatOpenAI({
    model: 'gpt-5-nano',
    apiKey: process.env.OPENAI_API_KEY
}).bindTools([scrapeWebsiteTool]);

const response = await model.invoke('O que é o Firecrawl? Visite firecrawl.dev e me conte sobre ele.');

console.log('Resposta:', response.content);
console.log('Chamadas de ferramenta:', response.tool_calls);
```

Este exemplo mostra como extrair dados estruturados usando a funcionalidade de saída estruturada do LangChain.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Tamanho do conteúdo extraído:', scrapeResult.markdown?.length);

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
        content: 'Extraia informações da empresa do conteúdo do site.'
    },
    {
        role: 'user',
        content: `Extraia os dados: ${scrapeResult.markdown}`
    }
]);

console.log('Informações da empresa extraídas:', companyInfo);
```

Para mais exemplos, consulte a [documentação do LangChain](https://js.langchain.com/docs).