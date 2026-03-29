---
title: PropertyGraph Index with Mistral AI and LlamaIndex - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-propertygraphs-property_graph
source: crawler
fetched_at: 2026-01-29T07:33:57.5660527-03:00
rendered_js: false
word_count: 353
---

In this notebook, we demonstrate the basic usage of the PropertyGraphIndex in LlamaIndex.

The property graph index will process unstructured documents, extract a property graph from them, and offer various methods for querying this graph.

## Setup

## Download Data

## Load Data

## Create PropertyGraphIndex

The following steps occur during the creation of a PropertyGraph:

1. PropertyGraphIndex.from\_documents(): We load documents into an index.
2. Parsing Nodes: The index parses the documents into nodes.
3. Extracting Paths from Text: The nodes are passed to an LLM, which is prompted to generate knowledge graph triples (i.e., paths).
4. Extracting Implicit Paths: The node.relationships property is used to infer implicit paths.
5. Generating Embeddings: Embeddings are generated for each text node and graph node, occurring twice during the process.

For debugging purposes, the default SimplePropertyGraphStore includes a helper to save a networkx representation of the graph to an html file.

## Querying

Querying a property graph index typically involves using one or more sub-retrievers and combining their results. The process of graph retrieval includes:

1. Selecting Nodes: Identifying the initial nodes of interest within the graph.
2. Traversing: Moving from the selected nodes to explore connected elements.

By default, two primary types of retrieval are employed simultaneously:

• Synonym/Keyword Expansion: Utilizing an LLM to generate synonyms and keywords derived from the query.

• Vector Retrieval: Employing embeddings to locate nodes within your graph.

Once nodes are identified, you can choose to:

• Return Paths: Provide the paths adjacent to the selected nodes, typically in the form of triples.

• Return Paths and Source Text: Provide both the paths and the original source text of the chunk, if available.

### Retreival

### QueryEngine

## Storage

By default, storage is managed using our straightforward in-memory abstractions—SimpleVectorStore for embeddings and SimplePropertyGraphStore for the property graph.

We can save and load these structures to and from disk.

## Vector Stores

While some graph databases, such as Neo4j, support vectors, you can still specify which vector store to use with your graph in cases where vectors are not supported, or when you want to override the default settings.

Below, we will demonstrate how to combine ChromaVectorStore with the default SimplePropertyGraphStore.

### Build and Save Index

### Load Index