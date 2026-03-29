---
title: Build a RAG application with Milvus Lite, Mistral and Llama-index - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-milvus-milvus_rag_french_parliament
source: crawler
fetched_at: 2026-01-29T07:34:09.342318072-03:00
rendered_js: false
word_count: 308
---

In this notebook, we are showing how you can build a Retrieval Augmented Generation (RAG) application to interact with data from the French Parliament. It uses Ollama with Mistral for LLM operations, Llama-index for orchestration, and [Milvus](https://milvus.io/) for vector storage.

## Install Ollama

Make sure to have Ollama installed and Running on your laptop --&gt; [https://ollama.com/](https://ollama.com/)

### Install the different dependencies

### Download data

Note: Run this cell only if you haven't cloned the repository.

### Use Mistral Embedding

Make sure to create an [API Key](https://console.mistral.ai/api-keys/) on Mistral's platform and load it as an environment variable.

On this tutorial, we are loading the environment variable stored in our `.env` file.

### Prepare out data to be stored in Milvus

This code makes it possible to process text embeddings using Mistral Embed & Mistral-7B and store those in Milvus.

**!!Make sure to have Ollama running on your laptop!!**

- Initialises Mistral-7B model using Ollama
- Service Context: Configures a service context with Mistral and the embedding model defined above
- Vector Store: Sets up a collection in Milvus to store text embeddings, specifying the database file, collection name, vector dimensions
- Storage Context: Configures a storage context with the Milvus vector store

This makes it possible to have efficient storage and retrieval of vector embeddings for text data.

### Using Mistral AI API

If you prefer not to run models locally or need more powerful models, you can use Mistral's API instead of Ollama. The API offers:

- Access to more powerful models like `mistral-large` and `mistral-small`
- No local GPU/CPU requirements
- Consistent performance and reliability
- Production-ready deployment

Make sure to create an [API Key](https://console.mistral.ai/api-keys/) on Mistral's platform first.

The rest of the setup using Milvus would stay the same.

### Process and load the Data

### Finally, ask questions to our RAG system

* * *

#### If you like this tutorial, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/stephen-batifol/), check out [Milvus](https://github.com/milvus-io/milvus) and join our [Discord](https://discord.gg/FG6hMJStWu).