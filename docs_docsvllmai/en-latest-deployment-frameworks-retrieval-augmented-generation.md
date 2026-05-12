---
title: Retrieval-Augmented Generation - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/retrieval_augmented_generation/
source: sitemap
fetched_at: 2026-05-07T21:11:53.604340175-03:00
rendered_js: false
word_count: 180
summary: This document provides instructions for integrating vLLM with LangChain and LlamaIndex to implement retrieval-augmented generation pipelines using Milvus as a vector store.
tags:
    - vllm
    - retrieval-augmented-generation
    - langchain
    - llamaindex
    - milvus
    - llm-deployment
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/retrieval_augmented_generation.md "Edit this page")

[Retrieval-augmented generation (RAG)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) is a technique that enables generative artificial intelligence (Gen AI) models to retrieve and incorporate new information. It modifies interactions with a large language model (LLM) so that the model responds to user queries with reference to a specified set of documents, using this information to supplement information from its pre-existing training data. This allows LLMs to use domain-specific and/or updated information. Use cases include providing chatbot access to internal company data or generating responses based on authoritative sources.

Here are the integrations:

- vLLM + [langchain](https://github.com/langchain-ai/langchain) + [milvus](https://github.com/milvus-io/milvus)
- vLLM + [llamaindex](https://github.com/run-llama/llama_index) + [milvus](https://github.com/milvus-io/milvus)

## vLLM + langchain[¶](#vllm-langchain "Permanent link")

### Prerequisites[¶](#prerequisites "Permanent link")

Set up the vLLM and langchain environment:

```
pipinstall-Uvllm\
langchain_milvuslangchain_openai\
langchain_communitybeautifulsoup4\
langchain-text-splitters
```

### Deploy[¶](#deploy "Permanent link")

1. Start the vLLM server with the supported embedding model, e.g.
   
   ```
   # Start embedding service (port 8000)
   vllmservessmits/Qwen2-7B-Instruct-embed-base
   ```
2. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   # Start chat service (port 8001)
   vllmserveqwen/Qwen1.5-0.5B-Chat--port8001
   ```
3. Use the script: [examples/online\_serving/retrieval\_augmented\_generation\_with\_langchain.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/retrieval_augmented_generation_with_langchain.py)
4. Run the script
   
   ```
   pythonretrieval_augmented_generation_with_langchain.py
   ```

## vLLM + llamaindex[¶](#vllm-llamaindex "Permanent link")

### Prerequisites[¶](#prerequisites_1 "Permanent link")

Set up the vLLM and llamaindex environment:

```
pipinstallvllm\
llama-indexllama-index-readers-web\
llama-index-llms-openai-like\
llama-index-embeddings-openai-like\
llama-index-vector-stores-milvus\
```

### Deploy[¶](#deploy_1 "Permanent link")

1. Start the vLLM server with the supported embedding model, e.g.
   
   ```
   # Start embedding service (port 8000)
   vllmservessmits/Qwen2-7B-Instruct-embed-base
   ```
2. Start the vLLM server with the supported chat completion model, e.g.
   
   ```
   # Start chat service (port 8001)
   vllmserveqwen/Qwen1.5-0.5B-Chat--port8001
   ```
3. Use the script: [examples/online\_serving/retrieval\_augmented\_generation\_with\_llamaindex.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/retrieval_augmented_generation_with_llamaindex.py)
4. Run the script:
   
   ```
   pythonretrieval_augmented_generation_with_llamaindex.py
   ```