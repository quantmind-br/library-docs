---
title: Building an LLM Agent to Find Relevant Research Papers from Arxiv - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-llamaindex-llamaindex_arxiv_agentic_rag
source: crawler
fetched_at: 2026-01-29T07:33:51.249644657-03:00
rendered_js: false
word_count: 584
summary: This tutorial explains how to build a ReAct-based LLM agent using LlamaIndex and MistralAI to search, summarize, and download research papers from ArXiv. It covers implementing tools for RAG, external paper fetching, and local file storage.
tags:
    - llamaindex
    - mistral-ai
    - llm-agent
    - arxiv-api
    - retrieval-augmented-generation
    - react-framework
    - python
category: tutorial
---

This notebook was created by Andrei Chernov ([Github](https://github.com/ChernovAndrey), [Linkedin](https://www.linkedin.com/in/andrei-chernov-58b157236/)) In this tutorial, we will create an LLM agent based on the **MistralAI** language model. The agent's primary purpose will be to find and summarize research papers from **Arxiv** that are relevant to the user's query. To build the agent, we will use the **LlamaIndex** framework.

## Tools Used by the Agent

The agent will utilize the following three tools:

1. **RAG Query Engine** This tool will store and retrieve recent papers from Arxiv, serving as a knowledge base for efficient and quick access to relevant information.
2. **Paper Fetch Tool** If the user specifies a topic that is not covered in the RAG Query Engine, this tool will fetch recent papers on the specified topic directly from Arxiv.
3. **PDF Download Tool** This tool allows the agent to download a research paper's PDF file locally using a link provided by Arxiv.

### First, let's install necessary libraries

### Additionally, You Need to Provide Your API Key to Access Mistral Models

You can obtain an API key [here](https://console.mistral.ai/api-keys/).

### To Build a RAG Query Engine, We Will Need an Embedding Model

For this tutorial, we will use the MistralAI embedding model.

### Now, We Will Download Recent Papers About Large Language Models from ArXiv

To keep this tutorial accessible with the free Mistral API version, we will download only the last 10 papers. Downloading more would exceed the limit later while building the RAG query engine. However, if you have a Mistral subscription, you can download additional papers.

### To Build a RAG Agent, We First Need to Index All Documents

This process creates a vector representation for each chunk of a document using the embedding model.

### Now, We Will Store the Index

Indexing a large number of texts can be time-consuming and costly since it requires making API calls to the embedding model. In real-world applications, it is better to store the index in a vector database to avoid reindexing. However, for simplicity, we will store the index locally in a directory in this tutorial, without using a vector database.

### We Are Ready to Build a RAG Query Engine for Our Agent

It is a good practice to provide a meaningful name and a clear description for each tool. This helps the agent select the most appropriate tool when needed.

### Let's Take a Look at the Prompts the RAG Tool Uses to Answer a Query Based on Context

Note that there are two prompts. By default, LlamaIndex uses a refine prompt before returning an answer. You can find more information about the response modes [here](https://docs.llamaindex.ai/en/v0.10.34/module_guides/deploying/query_engine/response_modes/).

### Building two other tools is straightforward because they are simply Python functions.

### Let's Chat with Our Agent

We built a ReAct agent, which operates in two main stages:

1. **Reasoning**: Upon receiving a query, the agent evaluates whether it has enough information to answer directly or if it needs to use a tool.
2. **Acting**: If the agent decides to use a tool, it executes the tool and then returns to the Reasoning stage to determine whether it can now answer the query or if further tool usage is necessary.

### The agent chose to use the RAG tool, found the relevant papers, and summarized them for us.

### Since the agent retains the chat history, we can request to download the papers without mentioning them explicitly.

### Let's see what happens if we ask about a topic that is not available in the RAG.

### As You Can See, the Agent Did Not Find the Papers in Storage and Fetched Them from ArXiv.