---
title: Property Graph with Pre-defined Schemas - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-propertygraphs-property_graph_predefined_schema
source: crawler
fetched_at: 2026-01-29T07:33:57.302243087-03:00
rendered_js: false
word_count: 103
---

In this notebook, we guide you through using Neo4j, Ollama, and Huggingface to build a property graph.

Specifically, we will utilize the SchemaLLMPathExtractor, which enables us to define a precise schema containing possible entity types, relation types, and how they can be interconnected.

## Setup

## Download Data

## Load Data

## Graph Construction

To build our graph, we will use the SchemaLLMPathExtractor.

This tool allows us to specify a schema for the graph, enabling us to extract entities and relations that adhere to this predefined schema, rather than allowing the LLM to randomly determine entities and relations.

## Neo4j setup

## PropertyGraphIndex construction

## Setup Retrievers

## Querying

### Retriever

### QueryEngine