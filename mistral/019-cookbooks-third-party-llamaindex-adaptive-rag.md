---
title: Adaptive RAG with LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-adaptive_rag
source: crawler
fetched_at: 2026-01-29T07:34:11.53749373-03:00
rendered_js: false
word_count: 432
summary: This document provides a step-by-step guide to implementing an Adaptive RAG system that routes simple and complex user queries to specific indices or tools using MistralAI and LlamaIndex.
tags:
    - adaptive-rag
    - llamaindex
    - mistral-ai
    - router-query-engine
    - function-calling
    - query-routing
category: tutorial
---

User queries in general can be complex queries, simple queries. One don't always need complex RAG system even to handle simple queries. [Adaptive RAG](https://arxiv.org/abs/2403.14403) proposes an approach to handle complex queries and simple queries.

In this notebook, we will implement an approach similar to Adaptive RAG, which differentiates between handling complex and simple queries. We'll focus on Lyft's 10k SEC filings for the years 2020, 2021, and 2022.

Our approach will involve using `RouterQueryEngine` and `FunctionCalling` capabilities of `MistralAI` to call different tools or indices based on the query's complexity.

- **Complex Queries:** These will leverage multiple tools that require context from several documents.
- **Simple Queries:** These will utilize a single tool that requires context from a single document or directly use an LLM to provide an answer.

Following are the steps we follow here:

1. Download Data.
2. Load Data.
3. Create indices for 3 documents.
4. Create query engines with documents and LLM.
5. Initialize a `FunctionCallingAgentWorker` for complex queries.
6. Create tools.
7. Create `RouterQueryEngine` - To route queries based on its complexity.
8. Querying.

### Installation

### Setup API Key

### Setup LLM and Embedding Model

### Logging

### Download Data

We will download Lyft's 10k SEC filings for the years 2020, 2021, and 2022.

### Load Data

### Create Indicies

### Create Query Engines

Query Engine for LLM. With this we will use LLM to answer the query.

### Initialize a `FunctionCallingAgentWorker`

### Create Tools

We will create tools using the `QueryEngines`, and `FunctionCallingAgentWorker` created earlier.

### Create RouterQueryEngine

`RouterQueryEngine` will route user queries to select one of the tools based on the complexity of the query.

### Querying

#### Simple Queries:

##### Query: What is the capital of France?

You can see that it used LLM tool since it is a general query.

##### Query: What did Lyft do in R&D in 2022?

You can see that it used lyft\_2022 tool to answer the query.

##### Query: What did Lyft do in R&D in 2021?

You can see that it used lyft\_2021 tool to answer the query.

##### Query: What did Lyft do in R&D in 2020?

You can see that it used lyft\_2020 tool to answer the query.

#### Complex Queries

Let's test queries that requires multiple tools.

##### Query: What did Lyft do in R&D in 2022 vs 2020?

You can see that it used lyft\_2020 and lyft\_2022 tools with `FunctionCallingAgent` to answer the query.

##### Query: What did Lyft do in R&D in 2021 vs 2020?

You can see that it used lyft\_2020 and lyft\_2021 tools with `FunctionCallingAgent` to answer the query.

##### Query: What did Lyft do in R&D in 2022 vs 2021 vs 2020?

You can see that it used lyft\_2020, lyft\_2021 and lyft\_2022 tools with `FunctionCallingAgent` to answer the query.