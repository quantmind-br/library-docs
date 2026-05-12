---
title: LangGraph - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/langgraph
source: sitemap
fetched_at: 2026-03-23T07:36:37.043128-03:00
rendered_js: false
word_count: 276
summary: This guide demonstrates how to integrate Firecrawl with LangGraph to build automated AI agent workflows for web scraping and content processing.
tags:
    - web-scraping
    - ai-agents
    - langgraph
    - firecrawl
    - workflow-automation
    - llm-integration
category: guide
---

Esta guía explica cómo integrar Firecrawl con LangGraph para crear flujos de trabajo de agentes de IA que puedan rastrear y procesar contenido web.

## Configuración

```
npm install @langchain/langgraph @langchain/openai @mendable/firecrawl-js
```

Crea un archivo `.env`:

```
FIRECRAWL_API_KEY=tu_clave_firecrawl
OPENAI_API_KEY=tu_clave_openai
```

> **Nota:** Si usas Node &lt; 20, instala `dotenv` y añade `import 'dotenv/config'` a tu código.

## Flujo de trabajo básico

Este ejemplo muestra un flujo de trabajo básico de LangGraph que realiza scraping de un sitio web y analiza el contenido.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, MessagesAnnotation, START, END } from '@langchain/langgraph';

// Inicializar Firecrawl
const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Inicializar LLM
const llm = new ChatOpenAI({
    model: "gpt-5-nano",
    apiKey: process.env.OPENAI_API_KEY
});

// Definir el nodo de scraping
async function scrapeNode(state: typeof MessagesAnnotation.State) {
    console.log('Scrapeando...');
    const result = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown'] });
    return {
        messages: [{
            role: "system",
            content: `Contenido extraído: ${result.markdown}`
        }]
    };
}

// Definir el nodo de análisis
async function analyzeNode(state: typeof MessagesAnnotation.State) {
    console.log('Analizando...');
    const response = await llm.invoke(state.messages);
    return { messages: [response] };
}

// Construir el grafo
const graph = new StateGraph(MessagesAnnotation)
    .addNode("scrape", scrapeNode)
    .addNode("analyze", analyzeNode)
    .addEdge(START, "scrape")
    .addEdge("scrape", "analyze")
    .addEdge("analyze", END);

// Compilar el grafo
const app = graph.compile();

// Ejecutar el flujo de trabajo
const result = await app.invoke({
    messages: [{ role: "user", content: "Resume el sitio web" }]
});

console.log(JSON.stringify(result, null, 2));
```

## Flujo de trabajo de varios pasos

Este ejemplo muestra un flujo de trabajo más complejo que extrae datos de varias URL y las procesa.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, Annotation, START, END } from '@langchain/langgraph';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const llm = new ChatOpenAI({ model: "gpt-5-nano", apiKey: process.env.OPENAI_API_KEY });

// Definir estado personalizado
const WorkflowState = Annotation.Root({
    urls: Annotation<string[]>(),
    scrapedData: Annotation<Array<{ url: string; content: string }>>(),
    summary: Annotation<string>()
});

// Scrapear múltiples URLs
async function scrapeMultiple(state: typeof WorkflowState.State) {
    const scrapedData = [];
    for (const url of state.urls) {
        const result = await firecrawl.scrape(url, { formats: ['markdown'] });
        scrapedData.push({ url, content: result.markdown || '' });
    }
    return { scrapedData };
}

// Resumir todo el contenido scrapeado
async function summarizeAll(state: typeof WorkflowState.State) {
    const combinedContent = state.scrapedData
        .map(item => `Content from ${item.url}:\n${item.content}`)
        .join('\n\n');

    const response = await llm.invoke([
        { role: "user", content: `Resumir estos sitios web:\n${combinedContent}` }
    ]);

    return { summary: response.content as string };
}

// Construir el grafo del flujo de trabajo
const workflow = new StateGraph(WorkflowState)
    .addNode("scrape", scrapeMultiple)
    .addNode("summarize", summarizeAll)
    .addEdge(START, "scrape")
    .addEdge("scrape", "summarize")
    .addEdge("summarize", END);

const app = workflow.compile();

// Ejecutar flujo de trabajo
const result = await app.invoke({
    urls: ["https://firecrawl.dev", "https://firecrawl.dev/pricing"]
});

console.log(result.summary);
```

Para ver más ejemplos, consulta la [documentación de LangGraph](https://langchain-ai.github.io/langgraphjs/).