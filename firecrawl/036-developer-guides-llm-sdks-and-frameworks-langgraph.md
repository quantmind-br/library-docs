---
title: LangGraph - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/llm-sdks-and-frameworks/langgraph
source: sitemap
fetched_at: 2026-03-23T07:39:59.702378-03:00
rendered_js: false
word_count: 252
summary: This document provides instructions on integrating Firecrawl with LangGraph to automate web scraping and content analysis within AI agent workflows.
tags:
    - firecrawl
    - langgraph
    - web-scraping
    - ai-agents
    - workflow-automation
    - llm-integration
category: guide
---

This guide shows how to integrate Firecrawl with LangGraph to build AI agent workflows that can scrape and process web content.

## Setup

```
npm install @langchain/langgraph @langchain/openai @mendable/firecrawl-js
```

Create `.env` file:

```
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **Note:** If using Node &lt; 20, install `dotenv` and add `import 'dotenv/config'` to your code.

## Basic Workflow

This example demonstrates a basic LangGraph workflow that scrapes a website and analyzes the content.

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
    messages: [{ role: "user", content: "Summarize the website" }]
});

console.log(JSON.stringify(result, null, 2));
```

## Multi-Step Workflow

This example demonstrates a more complex workflow that scrapes multiple URLs and processes them.

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { ChatOpenAI } from '@langchain/openai';
import { StateGraph, Annotation, START, END } from '@langchain/langgraph';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const llm = new ChatOpenAI({ model: "gpt-5-nano", apiKey: process.env.OPENAI_API_KEY });

// Define custom state
const WorkflowState = Annotation.Root({
    urls: Annotation<string[]>(),
    scrapedData: Annotation<Array<{ url: string; content: string }>>(),
    summary: Annotation<string>()
});

// Scrape multiple URLs
async function scrapeMultiple(state: typeof WorkflowState.State) {
    const scrapedData = [];
    for (const url of state.urls) {
        const result = await firecrawl.scrape(url, { formats: ['markdown'] });
        scrapedData.push({ url, content: result.markdown || '' });
    }
    return { scrapedData };
}

// Summarize all scraped content
async function summarizeAll(state: typeof WorkflowState.State) {
    const combinedContent = state.scrapedData
        .map(item => `Content from ${item.url}:\n${item.content}`)
        .join('\n\n');

    const response = await llm.invoke([
        { role: "user", content: `Summarize these websites:\n${combinedContent}` }
    ]);

    return { summary: response.content as string };
}

// Build the workflow graph
const workflow = new StateGraph(WorkflowState)
    .addNode("scrape", scrapeMultiple)
    .addNode("summarize", summarizeAll)
    .addEdge(START, "scrape")
    .addEdge("scrape", "summarize")
    .addEdge("summarize", END);

const app = workflow.compile();

// Execute workflow
const result = await app.invoke({
    urls: ["https://firecrawl.dev", "https://firecrawl.dev/pricing"]
});

console.log(result.summary);
```

For more examples, check the [LangGraph documentation](https://langchain-ai.github.io/langgraphjs/).