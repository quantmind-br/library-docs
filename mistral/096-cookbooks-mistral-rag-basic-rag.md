---
title: RAG Basics with Mistral AI - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-rag-basic_rag
source: crawler
fetched_at: 2026-01-29T07:34:01.190262877-03:00
rendered_js: false
word_count: 1195
summary: This document provides a detailed walkthrough of implementing Retrieval-augmented generation (RAG) using Mistral AI, covering document processing, embedding creation, and retrieval strategies.
tags:
    - rag
    - mistral-ai
    - embeddings
    - vector-search
    - document-chunking
    - llm-integration
category: guide
---

![](https://docs.mistral.ai/cookbooks/images/rag.png)

Retrieval-augmented generation (RAG) is an AI framework that synergizes the capabilities of LLMs and information retrieval systems. It’s useful to answer questions or generate content leveraging external knowledge. There are two main steps in RAG: 1) retrieval: retrieve relevant information from a knowledge base with text embeddings stored in a vector store; 2) generation: insert the relevant information to the prompt for the LLM to generate information. In this guide, we will walk through a very basic example of RAG with four implementations:

- RAG from scratch with Mistral
- RAG with Mistral and LangChain
- RAG with Mistral and LlamaIndex
- RAG with Mistral and Haystack

## RAG from scratch

This section aims to guide you through the process of building a basic RAG from scratch. We have two goals: firstly, to offer users a comprehensive understanding of the internal workings of RAG and demystify the underlying mechanisms; secondly, to empower you with the essential foundations needed to build an RAG using the minimum required dependencies.

### Import needed packages

The first step is to install the needed packages `mistralai` and `faiss-cpu` and import the needed packages:

### Get data

In this very simple example, we are getting data from an essay written by Paul Graham:

We can also save the essay in a local file:

## Split document into chunks

In a RAG system, it is crucial to split the document into smaller chunks so that it’s more effective to identify and retrieve the most relevant information in the retrieval process later. In this example, we simply split our text by character, combine 2048 characters into each chunk, and we get 37 chunks.

#### Considerations:

- **Chunk size**: Depending on your specific use case, it may be necessary to customize or experiment with different chunk sizes and chunk overlap to achieve optimal performance in RAG. For example, smaller chunks can be more beneficial in retrieval processes, as larger text chunks often contain filler text that can obscure the semantic representation. As such, using smaller text chunks in the retrieval process can enable the RAG system to identify and extract relevant information more effectively and accurately. However, it’s worth considering the trade-offs that come with using smaller chunks, such as increasing processing time and computational resources.
- **How to split**: While the simplest method is to split the text by character, there are other options depending on the use case and document structure. For example, to avoid exceeding token limits in API calls, it may be necessary to split the text by tokens. To maintain the cohesiveness of the chunks, it can be useful to split the text by sentences, paragraphs, or HTML headers. If working with code, it’s often recommended to split by meaningful code chunks for example using an Abstract Syntax Tree (AST) parser.

### Create embeddings for each text chunk

For each text chunk, we then need to create text embeddings, which are numeric representations of the text in the vector space. Words with similar meanings are expected to be in closer proximity or have a shorter distance in the vector space. To create an embedding, use Mistral’s embeddings API endpoint and the embedding model `mistral-embed`. We create a `get_text_embedding` to get the embedding from a single text chunk and then we use list comprehension to get text embeddings for all text chunks.

### Load into a vector database

Once we get the text embeddings, a common practice is to store them in a vector database for efficient processing and retrieval. There are several vector database to choose from. In our simple example, we are using an open-source vector database Faiss, which allows for efficient similarity search.

With Faiss, we instantiate an instance of the Index class, which defines the indexing structure of the vector database. We then add the text embeddings to this indexing structure.

#### Considerations:

- **Vector database**: When selecting a vector database, there are several factors to consider including speed, scalability, cloud management, advanced filtering, and open-source vs. closed-source.

### Create embeddings for a question

Whenever users ask a question, we also need to create embeddings for this question using the same embedding models as before.

#### Considerations:

- Hypothetical Document Embeddings (HyDE): In some cases, the user’s question might not be the most relevant query to use for identifying the relevant context. Instead, it maybe more effective to generate a hypothetical answer or a hypothetical document based on the user’s query and use the embeddings of the generated text to retrieve similar text chunks.

### Retrieve similar chunks from the vector database

We can perform a search on the vector database with `index.search`, which takes two arguments: the first is the vector of the question embeddings, and the second is the number of similar vectors to retrieve. This function returns the distances and the indices of the most similar vectors to the question vector in the vector database. Then based on the returned indices, we can retrieve the actual relevant text chunks that correspond to those indices.

#### Considerations:

- **Retrieval methods**: There are a lot different retrieval strategies. In our example, we are showing a simple similarity search with embeddings. Sometimes when there is metadata available for the data, it’s better to filter the data based on the metadata first before performing similarity search. There are also other statistical retrieval methods like TF-IDF and BM25 that use frequency and distribution of terms in the document to identify relevant text chunks.
- **Retrieved document**: Do we always retrieve individual text chunk as it is? Not always.
  
  - Sometimes, we would like to include more context around the actual retrieved text chunk. We call the actual retrieve text chunk “child chunk” and our goal is to retrieve a larger “parent chunk” that the “child chunk” belongs to.
  - On occasion, we might also want to provide weights to our retrieve documents. For example, a time-weighted approach would help us retrieve the most recent document.
  - One common issue in the retrieval process is the “lost in the middle” problem where the information in the middle of a long context gets lost. Our models have tried to mitigate this issue. For example, in the passkey task, our models have demonstrated the ability to find a "needle in a haystack" by retrieving a randomly inserted passkey within a long prompt, up to 32k context length. However, it is worth considering experimenting with reordering the document to determine if placing the most relevant chunks at the beginning and end leads to improved results.

### Combine context and question in a prompt and generate response

Finally, we can offer the retrieved text chunks as the context information within the prompt. Here is a prompt template where we can include both the retrieved text and user question in the prompt.

#### Considerations:

- Prompting techniques: Most of the prompting techniques can be used in developing a RAG system as well. For example, we can use few-shot learning to guide the model’s answers by providing a few examples. Additionally, we can explicitly instruct the model to format answers in a certain way.

In the next sections, we are going to show you how to do a similar basic RAG with some of the popular RAG frameworks. We will start with LlamaIndex and add other frameworks in the future.

## LangChain

## LlamaIndex

## Haystack