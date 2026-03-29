---
title: Router Query Engine with Mistral AI and LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-routerqueryengine
source: crawler
fetched_at: 2026-01-29T07:34:09.93336455-03:00
rendered_js: false
word_count: 144
---

A `VectorStoreIndex` is designed to handle queries related to specific contexts, while a `SummaryIndex` is optimized for answering summarization queries. However, in real-world scenarios, user queries may require either context-specific responses or summarizations. To address this, the system must effectively route user queries to the appropriate index to provide relevant answers.

In this notebook, we will utilize the `RouterQueryEngine` to direct user queries to the appropriate index based on the query type.

### Installation

### Setup API Key

### Set LLM and Embedding Model

### Download Data

We will use `Uber 10K SEC Filings`.

### Load Data

### Index and Query Engine creation

1. VectorStoreIndex -&gt; Specific context queries
2. SummaryIndex -&gt; Summarization queries

### Create Tools

### Create Router Query Engine

### Querying

#### Summarization Query

You can see that it uses `SummaryIndex` to provide answer to the summarization query.

#### Specific Context Query

You can see it uses `VectorStoreIndex` to answer specific context type query.