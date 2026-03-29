---
title: RAG Pipeline with LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-rag
source: crawler
fetched_at: 2026-01-29T07:34:11.373137088-03:00
rendered_js: false
word_count: 143
---

In this notebook we will look into building RAG with LlamaIndex using `MistralAI LLM and Embedding Model`. Additionally, we will look into using Index as Retreiver.

1. Basic RAG pipeline.
2. Index as Retriever.

## Setup API Keys

## Basic RAG pipeline

Following are the steps involved in Builiding a basic RAG pipeline.

1. Setup LLM and Embedding Model
2. Download Data
3. Load Data
4. Create Nodes
5. Create Index
6. Create Query Engine
7. Querying

Query Engine combines `Retrieval` and `Response Synthesis` modules to generate response for the given query.

### Setup LLM and Embedding Model

### Download Data

We will use `Uber 2021 10K SEC Filings` for the demonstration.

### Load Data

### Create Nodes

### Create Index

### Create Query Engine

### Querying

## Index as Retriever

We can make use of created index as a `Retriever`. Retriever helps you to retrieve relevant chunks/ nodes for the given user query.

### Create Retriever

### Retrieve relevant nodes for a Query