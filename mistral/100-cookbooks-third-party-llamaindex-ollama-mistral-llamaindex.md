---
title: RAG Pipeline with Ollama, Mistral and LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-ollama_mistral_llamaindex
source: crawler
fetched_at: 2026-01-29T07:34:05.918280891-03:00
rendered_js: false
word_count: 143
summary: A technical guide for building a Retrieval-Augmented Generation (RAG) pipeline using Ollama, Mistral models, and the LlamaIndex framework.
tags:
    - RAG
    - Ollama
    - Mistral
    - LlamaIndex
    - LLM
category: guide
---

In this notebook, we will demonstrate how to build a RAG pipeline using Ollama, Mistral models, and LlamaIndex. The following topics will be covered:

1. Integrating Mistral with Ollama and LlamaIndex.
2. Implementing RAG with Ollama and LlamaIndex using the Mistral model.
3. Routing queries with RouterQueryEngine.
4. Handling complex queries with SubQuestionQueryEngine.

Before running this notebook, you need to set up Ollama. Please follow the instructions [here](https://ollama.com/library/mistral:instruct).

## Setup LLM

### Querying

## Setup Embedding Model

## Download Data

We will use Uber and Lyft 10K SEC filings for the demostration.

## Load Data

## Create Index and Query Engines

### Querying

## RouterQueryEngine

We will utilize the `RouterQueryEngine` to direct user queries to the appropriate index based on the query related to either Uber/ Lyft.

### Create QueryEngine tools

### Create `RouterQueryEnine`

### Querying

## SubQuestionQueryEngine

We will explore how the `SubQuestionQueryEngine` can be leveraged to tackle complex queries by generating and addressing sub-queries.

### Create `SubQuestionQueryEngine`

### Querying