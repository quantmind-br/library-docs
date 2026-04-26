---
title: RAG Quickstart | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/rag_quickstart
source: sitemap
fetched_at: 2026-04-26T04:13:11.609396285-03:00
rendered_js: false
word_count: 1291
summary: This document provides a foundational guide on building a retrieval-augmented generation (RAG) system, covering key stages including document chunking, embedding generation, vector storage, and query-based context retrieval for LLM generation.
tags:
    - rag
    - llm
    - vector-database
    - embeddings
    - information-retrieval
    - artificial-intelligence
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Retrieval-augmented generation (RAG) synergizes LLM capabilities with information retrieval. It's useful for answering questions or generating content leveraging external knowledge.

**Two main steps:**
1. **Retrieval**: retrieve relevant information from a knowledge base using text embeddings stored in a vector store
2. **Generation**: insert retrieved information into the prompt for the LLM to generate a response

## Build a RAG from Scratch

[Open in Colab](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/rag/basic_RAG.ipynb)

### 1. Install Dependencies

```bash
pip install mistralai faiss-cpu
```

### 2. Get Data

This example uses an essay written by Paul Graham. Save it locally:

```python
import requests

url = "https://raw.githubusercontent.com/ignorept/Mistral/main/README.md"
response = requests.get(url)
with open("data.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
```

### 3. Chunk the Document

Split documents into smaller chunks for effective retrieval. This example splits by character with 2048 characters per chunk (yields 37 chunks).

**Chunk size considerations:**
- Smaller chunks can be more effective for retrieval — larger chunks often contain filler text obscuring semantic representation
- Trade-offs: smaller chunks increase processing time and computational resources

**How to split:**
- **By character**: simplest method
- **By tokens**: avoid exceeding API token limits
- **By sentences/paragraphs/HTML headers**: maintain cohesiveness
- **By AST parsing**: for code (recommended)

### 4. Create Embeddings

Text embeddings are numeric representations in vector space — words with similar meanings are closer together.

Use the Mistral AI embeddings API endpoint with model `mistral-embed`:

```python
from mistralai import Mistral

client = Mistral(api_key="your-api-key")

def get_text_embedding(text, client):
    response = client.embeddings.create(
        model="mistral-embed",
        inputs=[text]
    )
    return response.data[0].embedding

embeddings = [get_text_embedding(chunk, client) for chunk in chunks]
```

### 5. Store in Vector Database

Store embeddings in a vector database for efficient retrieval. This example uses Faiss (open-source):

```python
import faiss

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype('float32'))
```

**Vector database selection factors:** speed, scalability, cloud management, advanced filtering, open-source vs. closed-source.

### 6. Retrieve

Create embeddings for the user's question using the same model, then search:

```python
query_embedding = get_text_embedding(question, client)
distances, indices = index.search(
    np.array([query_embedding]).astype('float32'),
    k=3
)
retrieved_chunks = [chunks[i] for i in indices[0]]
```

**Retrieval methods:**
- **Similarity search** with embeddings (shown above)
- **Metadata filtering** before similarity search
- **TF-IDF and BM25**: frequency and distribution-based methods
- **Hypothetical Document Embeddings (HyDE)**: generate a hypothetical answer and use its embeddings for retrieval

**Retrieved document considerations:**
- "Child chunk" vs "parent chunk": include more context around the actual retrieved chunk
- **Time-weighted retrieval**: retrieve more recent documents
- **"Lost in the middle" problem**: place most relevant chunks at the beginning and end; our models can find a "needle in a haystack" up to 32k context length

### 7. Generate Response

Combine retrieved context with the question in a prompt:

```python
context = "\n".join(retrieved_chunks)
prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"

response = client.chat.complete(
    model="mistral-medium-latest",
    messages=[{"role": "user", "content": prompt}]
)
```

**Prompting techniques:** Few-shot learning, explicit formatting instructions.

## RAG Cookbooks

Visit the [cookbook](https://github.com/mistralai/cookbook) for more examples:
- [**RAG with LangChain**](https://docs.mistral.ai/resources/cookbooks/third_party-langchain-adaptive_rag_mistral): Adaptive RAG with LangChain's LangGraph
- [**RAG with LlamaIndex**](https://docs.mistral.ai/resources/cookbooks/third_party-llamaindex-llamaindex_agentic_rag): Complex queries over multiple documents using a ReAct agent
- [**RAG with Haystack**](https://docs.mistral.ai/resources/cookbooks/third_party-haystack-haystack_chat_with_docs): Chat with documents using Haystack

#rag #llm #vector-database