---
title: RAG with Mistral AI and Pinecone - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/third_party-pinecone-pinecone_rag
source: crawler
fetched_at: 2026-01-29T07:34:06.643116664-03:00
rendered_js: false
word_count: 369
summary: This document provides a step-by-step guide on building a Retrieval-Augmented Generation (RAG) system using Mistral AI for embeddings and text generation integrated with a Pinecone vector database.
tags:
    - mistral-ai
    - pinecone
    - rag
    - vector-database
    - embeddings
    - semantic-search
    - llm
category: tutorial
---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/third_party/Pinecone/pinecone_rag.ipynb) [![Open nbviewer](https://raw.githubusercontent.com/pinecone-io/examples/master/assets/nbviewer-shield.svg)](https://nbviewer.org/github/mistralai/cookbook/blob/main/third_party/Pinecone/pinecone_rag.ipynb)

To begin, we setup our prerequisite libraries.

## Data Preparation

We start by downloading a dataset that we will encode and store. The dataset [`jamescalam/ai-arxiv2-semantic-chunks`](https://huggingface.co/datasets/jamescalam/ai-arxiv2-semantic-chunks) contains scraped data from many popular ArXiv papers centred around LLMs and GenAI.

We have 200K chunks, where each chunk is roughly the length of 1-2 paragraphs in length. Here is an example of a single record:

Format the data into the format we need, this will contain `id`, `text` (which we will embed), and `metadata`.

We need to define an embedding model to create our embedding vectors for retrieval, for that we will be using Mistral AI's `mistral-embed`. There is some cost associated with this model, so be aware of that (costs for running this notebook are &lt;$1).

We can create embeddings now like so:

We can view the dimensionality of our returned embeddings, which we'll need soon when initializing our vector index:

Now we create our vector DB to store our vectors. For this we need to get a [free Pinecone API key](https://app.pinecone.io) — the API key can be found in the "API Keys" button found in the left navbar of the Pinecone dashboard.

Now we setup our index specification, this allows us to define the cloud provider and region where we want to deploy our index. You can find a list of all [available providers and regions here](https://docs.pinecone.io/docs/projects).

Creating an index, we set `dimension` equal to the dimensionality of `mistral-embed` (`1024`), and use a `metric` also compatible with `mistral-embed` (this can be either `cosine` or `dotproduct`). We also pass our `spec` to index initialization.

We will define an embedding function that will allow us to avoid throwing too many tokens into a single embedding batch (as of 21 May 2024 the limit is `16384` tokens).

We can see the index is currently empty with a `total_vector_count` of `0`. We can begin populating it with `mistral-embed` built embeddings like so:

**⚠️ WARNING: Embedding costs for the full dataset as of 3 Jan 2024 is ~$5.70**

Now let's test retrieval!

Our retrieval component works, now let's try feeding this into Mistral Large LLM to produce an answer.

Don't forget to delete your index when you're done to save resources!