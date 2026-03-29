---
title: RAG with Mistral AI, Azure AI Search and Azure AI Studio - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-azure_ai_search-azure_ai_search_rag
source: crawler
fetched_at: 2026-01-29T07:34:04.262769287-03:00
rendered_js: false
word_count: 449
summary: A tutorial guide on implementing Retrieval-Augmented Generation (RAG) using Mistral AI models integrated with Azure AI Search and Azure AI Studio.
tags:
    - RAG
    - Mistral AI
    - Azure AI Search
    - Azure AI Studio
    - LLM
category: guide
---

## Overview

This notebook demonstrates how to integrate Mistral Embeddings with Azure AI Search as a vector store, and use the results to ground responses in the Mistral Chat Completion Model.

## Prerequisites

- Mistral AI API Key OR Azure AI Studio Deployed Mistral Chat Completion Model and Azure AI Studio API Key
- Azure AI Search service
- Python 3.x environment with necessary libraries installed

## Steps

1. Install required packages
2. Load data and generate Mistral embeddings
3. Index embeddings in Azure AI Search
4. Perform search using Azure AI Search
5. Ground search results in Mistral Chat Completion Model

## Install Required Packages

## Load Data and Generate Mistral Embeddings

We have 10K chunks, where each chunk is roughly the length of 1-2 paragraphs in length. Here is an example of a single record:

Format the data into the format we need, this will contain `id`, `title`, `content` (which we will embed), and `arxiv_id`.

We need to define an embedding model to create our embedding vectors for retrieval, for that we will be using Mistral AI's `mistral-embed`. There is some cost associated with this model, so be aware of that (costs for running this notebook are &lt;$1).

We can view the dimensionality of our returned embeddings, which we'll need soon when initializing our vector index:

## Index Embeddings into Azure AI Search

Now we create our vector DB to store our vectors. For this, we need to set up an [Azure AI Search service](https://portal.azure.com/#create/Microsoft.Search).

There are two ways to authenticate to Azure AI Search:

1. **Service Key**: The service key can be found in the "Settings -&gt; Keys" section in the left navbar of the Azure portal dashboard. Make sure to select the ADMIN key.
2. **Managed Identity**: Using Microsoft Entra ID (f.k.a. Azure Active Directory) is a more secure and recommended way to authenticate. You can follow the instructions in the [official Microsoft documentation](https://learn.microsoft.com/azure/search/search-security-rbac) to set up Managed Identity.

For more detailed instructions on creating an Azure AI Search service, please refer to the [official Microsoft documentation](https://learn.microsoft.com/azure/search/search-create-service-portal).

### Authenticate into Azure AI Search

### Create a vector index

### Estimate Cost for Embedding Generation

As per the information from [Lunary.ai's Mistral Tokenizer](https://lunary.ai/mistral-tokenizer), one token is approximately equivalent to five characters of text.

According to [Mistral's Pricing](https://mistral.ai/technology/#pricing), the cost for using `mistral-embed` is $0.1 per 1M tokens for both inputs and outputs.

In the following code block, we will calculate the estimated cost for generating embeddings based on the size of our dataset and these pricing details.

### Transform Dataset for Azure AI Search Upload

### Generate Embeddings

Azure AI Search doesn't allow certain unsafe keys so we'll base64 encode `id` here

### Upload Documents

## Perform a Vector Search

## Ground retrieved results from Azure AI Search to Mistral-Large LLM

## Ground Results to Mistral-Large hosted in Azure AI Studio