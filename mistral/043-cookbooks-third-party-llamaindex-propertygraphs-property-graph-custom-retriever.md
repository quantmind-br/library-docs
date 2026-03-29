---
title: Custom Retriever in PropertyGraph - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-propertygraphs-property_graph_custom_retriever
source: crawler
fetched_at: 2026-01-29T07:33:56.879462269-03:00
rendered_js: false
word_count: 130
summary: This document provides a guide on building a custom retriever for property graphs by combining vector search and text-to-Cypher techniques followed by a reranking process. It explains how to implement advanced retrieval workflows using Neo4j and Cohere for precise control over graph data queries.
tags:
    - property-graph
    - neo4j
    - vector-search
    - text-to-cypher
    - reranking
    - custom-retriever
category: tutorial
---

In this notebook we demonstrate how to define a custom retriever for a property graph. Although this approach is more complex than using standard graph retrievers, it offers detailed control over the retrieval process, allowing for customization that aligns closely with your specific application needs.

Also, we will walk you through an advanced retrieval workflow using the property graph store directly. We’ll conduct both vector search and text-to-Cypher retrieval, and subsequently integrate the results using a reranking module.

We will be using cohere reranker, so we will need cohere-api-key

## Setup

## Download Data

## Load Data

## Docker Setup

You need to login and set password for the first time.

1. username: neo4j
2. password: neo4j

## Setup Neo4j GraphStore

## PropertyGraphIndex Construction

## CustomRetriever

Define a custom retriever that combines VectorContextRetriever, TextToCypherRetriever and Reranker.

## Setup CustomRetriever

## QueryEngine