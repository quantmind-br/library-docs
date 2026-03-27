---
title: LangGraph - Firecrawl Docs
url: https://docs.firecrawl.dev/fr/developer-guides/llm-sdks-and-frameworks/langgraph
source: sitemap
fetched_at: 2026-03-23T07:35:48.186146-03:00
rendered_js: false
word_count: 272
summary: This document provides a guide on integrating Firecrawl with LangGraph to build automated AI agent workflows for web scraping and content analysis.
tags:
    - web-scraping
    - ai-agents
    - workflow-automation
    - langgraph
    - firecrawl
    - node-js
    - llm-integration
category: guide
---

Ce guide explique comment intégrer Firecrawl à LangGraph pour créer des workflows d’agents IA capables de crawler et de traiter du contenu web.

## Configuration

```
npm install @langchain/langgraph @langchain/openai @mendable/firecrawl-js
```

Créer un fichier `.env` :

```
FIRECRAWL_API_KEY=votre_clé_firecrawl
OPENAI_API_KEY=votre_clé_openai
```

> **Remarque :** Si vous utilisez Node &lt; 20, installez `dotenv` et ajoutez `import 'dotenv/config'` à votre code.

## Flux de travail de base

Cet exemple présente un flux de travail LangGraph de base qui récupère les données d’un site web et en analyse le contenu.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, MessagesAnnotation, START, END } from '@langchain/langgraph';

// Initialize Firecrawl
const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

// Initialize LLM
const llm = new ChatOpenAI({
    model: "gpt-5-nano",
    apiKey: process.env.OPENAI_API_KEY
});

// Define the scrape node
async function scrapeNode(state: typeof MessagesAnnotation.State) {
    console.log('Scraping...');
    const result = await firecrawl.scrape('https://firecrawl.dev', { formats: ['markdown'] });
    return {
        messages: [{
            role: "system",
            content: `Scraped content: ${result.markdown}`
        }]
    };
}

// Define the analyze node
async function analyzeNode(state: typeof MessagesAnnotation.State) {
    console.log('Analyzing...');
    const response = await llm.invoke(state.messages);
    return { messages: [response] };
}

// Build the graph
const graph = new StateGraph(MessagesAnnotation)
    .addNode("scrape", scrapeNode)
    .addNode("analyze", analyzeNode)
    .addEdge(START, "scrape")
    .addEdge("scrape", "analyze")
    .addEdge("analyze", END);

// Compile the graph
const app = graph.compile();

// Run the workflow
const result = await app.invoke({
    messages: [{ role: "user", content: "Résumer le site web" }]
});

console.log(JSON.stringify(result, null, 2));
```

## Flux de travail en plusieurs étapes

Cet exemple illustre un flux de travail plus complexe qui explore plusieurs URL et les traite.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, Annotation, START, END } from '@langchain/langgraph';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const llm = new ChatOpenAI({ model: "gpt-5-nano", apiKey: process.env.OPENAI_API_KEY });

// Définir l'état personnalisé
const WorkflowState = Annotation.Root({
    urls: Annotation<string[]>(),
    scrapedData: Annotation<Array<{ url: string; content: string }>>(),
    summary: Annotation<string>()
});

// Scraper plusieurs URL
async function scrapeMultiple(state: typeof WorkflowState.State) {
    const scrapedData = [];
    for (const url of state.urls) {
        const result = await firecrawl.scrape(url, { formats: ['markdown'] });
        scrapedData.push({ url, content: result.markdown || '' });
    }
    return { scrapedData };
}

// Résumer tout le contenu scrapé
async function summarizeAll(state: typeof WorkflowState.State) {
    const combinedContent = state.scrapedData
        .map(item => `Content from ${item.url}:\n${item.content}`)
        .join('\n\n');

    const response = await llm.invoke([
        { role: "user", content: `Résume ces sites web :\n${combinedContent}` }
    ]);

    return { summary: response.content as string };
}

// Construire le graphe du workflow
const workflow = new StateGraph(WorkflowState)
    .addNode("scrape", scrapeMultiple)
    .addNode("summarize", summarizeAll)
    .addEdge(START, "scrape")
    .addEdge("scrape", "summarize")
    .addEdge("summarize", END);

const app = workflow.compile();

// Exécuter le workflow
const result = await app.invoke({
    urls: ["https://firecrawl.dev", "https://firecrawl.dev/pricing"]
});

console.log(result.summary);
```

Pour plus d’exemples, consultez la [documentation de LangGraph](https://langchain-ai.github.io/langgraphjs/).