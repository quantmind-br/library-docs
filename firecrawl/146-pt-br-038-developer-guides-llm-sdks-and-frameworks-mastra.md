---
title: Mastra - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/mastra
source: sitemap
fetched_at: 2026-03-23T07:34:33.401313-03:00
rendered_js: false
word_count: 284
summary: This document provides a guide on how to integrate the Firecrawl web scraping tool into the Mastra TypeScript framework to build automated AI agent workflows.
tags:
    - mastra
    - firecrawl
    - ai-agents
    - typescript
    - web-scraping
    - workflow-automation
    - integration
category: guide
---

Integre o Firecrawl ao Mastra, o framework TypeScript para criar agentes e workflows de IA.

## Configuração

```
npm install @mastra/core @mendable/firecrawl-js zod
```

Crie o arquivo `.env`:

```
FIRECRAWL_API_KEY=sua_chave_firecrawl
OPENAI_API_KEY=sua_chave_openai
```

> **Observação:** Se estiver usando Node &lt; 20, instale `dotenv` e adicione `import 'dotenv/config'` ao seu código.

## Fluxo em múltiplas etapas

Este exemplo demonstra um fluxo completo que pesquisa, executa scraping e resume a documentação usando Firecrawl e Mastra.

```
import { createWorkflow, createStep } from "@mastra/core/workflows";
import { z } from "zod";
import Firecrawl from "@mendable/firecrawl-js";
import { Agent } from "@mastra/core/agent";

const firecrawl = new Firecrawl({
  apiKey: process.env.FIRECRAWL_API_KEY || "fc-YOUR_API_KEY"
});

const agent = new Agent({
  name: "summarizer",
  instructions: "You are a helpful assistant that creates concise summaries of documentation.",
  model: "openai/gpt-5-nano",
});

// Step 1: Search with Firecrawl SDK
const searchStep = createStep({
  id: "search",
  inputSchema: z.object({
    query: z.string(),
  }),
  outputSchema: z.object({
    url: z.string(),
    title: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { query: string } }) => {
    console.log(`Searching: ${inputData.query}`);
    const searchResults = await firecrawl.search(inputData.query, { limit: 1 });
    const webResults = (searchResults as any)?.web;

    if (!webResults || !Array.isArray(webResults) || webResults.length === 0) {
      throw new Error("No search results found");
    }

    const firstResult = webResults[0];
    console.log(`Found: ${firstResult.title}`);
    return {
      url: firstResult.url,
      title: firstResult.title,
    };
  },
});

// Step 2: Scrape the URL with Firecrawl SDK
const scrapeStep = createStep({
  id: "scrape",
  inputSchema: z.object({
    url: z.string(),
    title: z.string(),
  }),
  outputSchema: z.object({
    markdown: z.string(),
    title: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { url: string; title: string } }) => {
    console.log(`Scraping: ${inputData.url}`);
    const scrapeResult = await firecrawl.scrape(inputData.url, {
      formats: ["markdown"],
    });

    console.log(`Scraped: ${scrapeResult.markdown?.length || 0} characters`);
    return {
      markdown: scrapeResult.markdown || "",
      title: inputData.title,
    };
  },
});

// Step 3: Summarize with Claude
const summarizeStep = createStep({
  id: "summarize",
  inputSchema: z.object({
    markdown: z.string(),
    title: z.string(),
  }),
  outputSchema: z.object({
    summary: z.string(),
  }),
  execute: async ({ inputData }: { inputData: { markdown: string; title: string } }) => {
    console.log(`Summarizing: ${inputData.title}`);

    const prompt = `Resuma a seguinte documentação em 2-3 frases:\n\nTítulo: ${inputData.title}\n\n${inputData.markdown}`;
    const result = await agent.generate(prompt);

    console.log(`Summary generated`);
    return { summary: result.text };
  },
});

// Create workflow
export const workflow = createWorkflow({
  id: "firecrawl-workflow",
  inputSchema: z.object({
    query: z.string(),
  }),
  outputSchema: z.object({
    summary: z.string(),
  }),
  steps: [searchStep, scrapeStep, summarizeStep],
})
  .then(searchStep)
  .then(scrapeStep)
  .then(summarizeStep)
  .commit();

async function testWorkflow() {
  const run = await workflow.createRunAsync();
  const result = await run.start({
    inputData: { query: "Firecrawl documentation" }
  });

  if (result.status === "success") {
    const { summarize } = result.steps;

    if (summarize.status === "success") {
      console.log(`\n${summarize.output.summary}`);
    }
  } else {
    console.error("Workflow failed:", result.status);
  }
}

testWorkflow().catch(console.error);
```

Para mais exemplos, veja a [documentação do Mastra](https://mastra.ai/docs).