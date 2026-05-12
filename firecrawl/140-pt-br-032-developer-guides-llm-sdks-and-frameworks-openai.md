---
title: OpenAI - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/openai
source: sitemap
fetched_at: 2026-03-23T07:34:49.07292-03:00
rendered_js: false
word_count: 340
summary: This document provides a set of integration tutorials for combining Firecrawl with OpenAI to perform web scraping, data extraction, and information analysis using AI models.
tags:
    - web-scraping
    - ai-integration
    - data-extraction
    - openai-api
    - firecrawl
    - function-calling
    - mcp-server
category: tutorial
---

Integre o Firecrawl ao OpenAI para criar aplicativos de IA alimentados por dados da Web.

## Configuração

```
npm install @mendable/firecrawl-js openai zod
```

Crie um arquivo `.env`:

```
FIRECRAWL_API_KEY=sua_chave_firecrawl
OPENAI_API_KEY=sua_chave_openai
```

> **Nota:** Se estiver usando Node &lt; 20, instale `dotenv` e adicione `import 'dotenv/config'` ao seu código.

## Scrape + Resumo

Este exemplo demonstra um fluxo de trabalho simples: fazer scraping de um site e resumir o conteúdo usando um modelo da OpenAI.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Faz scrape do conteúdo do site
const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

// Resumir com o modelo OpenAI
const completion = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [
        { role: 'user', content: `Summarize: ${scrapeResult.markdown}` }
    ]
});

console.log('Summary:', completion.choices[0]?.message.content);
```

## Chamadas de função

Este exemplo mostra como usar o recurso de chamadas de função da OpenAI para permitir que o modelo decida quando realizar scraping de sites com base nas solicitações do usuário.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const ScrapeArgsSchema = z.object({
    url: z.string().describe('The URL of the website to scrape')
});

const tools = [{
    type: 'function' as const,
    function: {
        name: 'scrape_website',
        description: 'Faz scrape de conteúdo de qualquer URL de site',
        parameters: z.toJSONSchema(ScrapeArgsSchema)
    }
}];

const response = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [{
        role: 'user',
        content: 'What is Firecrawl? Visit firecrawl.dev and tell me about it.'
    }],
    tools
});

const message = response.choices[0]?.message;

if (message?.tool_calls && message.tool_calls.length > 0) {
    for (const toolCall of message.tool_calls) {
        if (toolCall.type === 'function') {
            console.log('Tool called:', toolCall.function.name);

            const args = ScrapeArgsSchema.parse(JSON.parse(toolCall.function.arguments));
            const result = await firecrawl.scrape(args.url, {
                formats: ['markdown'] // Other formats: html, links, etc.
            });
            console.log('Scraped content:', result.markdown?.substring(0, 200) + '...');

            // Send the scraped content back to the model for final response
            const finalResponse = await openai.chat.completions.create({
                model: 'gpt-5-nano',
                messages: [
                    {
                        role: 'user',
                        content: 'What is Firecrawl? Visit firecrawl.dev and tell me about it.'
                    },
                    message,
                    {
                        role: 'tool',
                        tool_call_id: toolCall.id,
                        content: result.markdown || 'No content scraped'
                    }
                ],
                tools
            });

            console.log('Final response:', finalResponse.choices[0]?.message?.content);
        }
    }
} else {
    console.log('Direct response:', message?.content);
}
```

Este exemplo mostra como usar modelos da OpenAI com saídas estruturadas para extrair dados específicos de conteúdo extraído por scraping.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

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

const response = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [
        {
            role: 'system',
            content: 'Extraia informações da empresa do conteúdo do site.'
        },
        {
            role: 'user',
            content: `Extrair dados: ${scrapeResult.markdown}`
        }
    ],
    response_format: {
        type: 'json_schema',
        json_schema: {
            name: 'company_info',
            schema: z.toJSONSchema(CompanyInfoSchema),
            strict: true
        }
    }
});

const content = response.choices[0]?.message?.content;
const companyInfo = content ? CompanyInfoSchema.parse(JSON.parse(content)) : null;
console.log('Informações da empresa validadas:', companyInfo);
```

## Buscar + Analisar

Este exemplo combina as funcionalidades de busca do Firecrawl com a análise de modelo da OpenAI para localizar e resumir informações a partir de múltiplas fontes.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import OpenAI from 'openai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Busca por informações relevantes
const searchResult = await firecrawl.search('Next.js 16 new features', {
    limit: 3,
    sources: [{ type: 'web' }], // Outras fontes: { type: 'news' }, { type: 'images' }
    scrapeOptions: { formats: ['markdown'] }
});

console.log('Resultados da busca:', searchResult.web?.length, 'páginas encontradas');

// Analisa e resume os principais recursos
const analysis = await openai.chat.completions.create({
    model: 'gpt-5-nano',
    messages: [{
        role: 'user',
        content: `Resuma os principais recursos: ${JSON.stringify(searchResult)}`
    }]
});

console.log('Análise:', analysis.choices[0]?.message?.content);
```

Este exemplo mostra como usar a Responses API da OpenAI com o Firecrawl configurado como servidor MCP (Model Context Protocol).

```
import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await openai.responses.create({
    model: 'gpt-5-nano',
    tools: [
        {
            type: 'mcp',
            server_label: 'firecrawl',
            server_description: 'A web search and scraping MCP server to scrape and extract content from websites.',
            server_url: `https://mcp.firecrawl.dev/${process.env.FIRECRAWL_API_KEY}/v2/mcp`,
            require_approval: 'never'
        }
    ],
    input: 'Find out what the top stories on Hacker News are and the latest blog post on OpenAI and summarize them in a bullet point format'
});

console.log('Response:', JSON.stringify(response.output, null, 2));
```

Para mais exemplos, consulte a [documentação da OpenAI](https://platform.openai.com/docs).