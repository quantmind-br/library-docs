---
title: Sub-Question Query Engine with Mistral AI and LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-subquestionqueryengine
source: crawler
fetched_at: 2026-01-29T07:34:11.610484243-03:00
rendered_js: false
word_count: 193
---

A `VectorStoreIndex` is adept at addressing queries that pertain to specific contexts within a single document or a collection of documents. However, user queries in real-world scenarios can be intricate, often requiring the retrieval of context from multiple documents to provide an answer. In such situations, a straightforward VectorStoreIndex might not suffice. Instead, breaking down the complex user queries into sub-queries can yield more accurate responses.

In this notebook, we will explore how the `SubQuestionQueryEngine` can be leveraged to tackle complex queries by generating and addressing sub-queries.

### Installation

### Setup API Key

### Set LLM and Embedding Model

### Logging

### Download Data

We will use `Uber, Lyft 10K SEC Filings` and `Paul Graham Essay Document`.

### Load Data

### Index and Query Engine creation

### Create Tools

### Create SubQuestion Query Engine

### Querying

Here you can see the sub-queries created to answer complex user-query which has multiple questions.

#### Query related to Uber and Lyft docs.

Creates two sub-queries related to Uber and Lyft.

#### Query related to Uber and Paul Graham Essay

Creates two sub-queries related to Uber and Paul Graham Essay.

#### Query Related to Uber, Lyft and Paul Graham Essay.

Creates sub-queries related to Uber, Lyft and Paul Graham Essay.