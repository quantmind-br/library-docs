---
title: Chroma — Open-source embedding database for AI applications | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma
source: crawler
fetched_at: 2026-04-24T17:01:22.827830759-03:00
rendered_js: false
word_count: 52
summary: This document serves as a comprehensive guide and reference for using ChromaDB, an open-source vector database designed for AI applications. It details core functionalities such as creating collections, adding data with various methods, performing sophisticated queries (including filtering), updating records, persisting data to disk, and integrating with external embedding models or frameworks like LangChain and LlamaIndex.
tags:
    - vector-database
    - ai-application
    - chroma-db
    - embedding-search
    - llm-memory
    - data-retrieval
category: guide
---

Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from notebooks to production clusters. Use for semantic search, RAG applications, or document retrieval. Best for local development and open-source projects.

The AI-native database for building LLM applications with memory.

```python
import chromadb

# Create client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="my_collection")

# Add documents
collection.add(
    documents=["This is document 1","This is document 2"],
    metadatas=[{"source":"doc1"},{"source":"doc2"}],
    ids=["id1","id2"]
)

# Query
results = collection.query(
    query_texts=["document about topic"],
    n_results=2
)

print(results)
```

```python
# Simple collection
collection = client.create_collection("my_docs")

# With custom embedding function
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="my_docs",
    embedding_function=openai_ef
)

# Get existing collection
collection = client.get_collection("my_docs")

# Delete collection
client.delete_collection("my_docs")
```

```python
# Add with auto-generated IDs
collection.add(
    documents=["Doc 1","Doc 2","Doc 3"],
    metadatas=[
{"source":"web","category":"tutorial"},
{"source":"pdf","page":5},
{"source":"api","timestamp":"2025-01-01"}
],
    ids=["id1","id2","id3"]
)

# Add with custom embeddings
collection.add(
    embeddings=[[0.1,0.2,...],[0.3,0.4,...]],
    documents=["Doc 1","Doc 2"],
    ids=["id1","id2"]
)
```

```python
# Basic query
results = collection.query(
    query_texts=["machine learning tutorial"],
    n_results=5
)

# Query with filters
results = collection.query(
    query_texts=["Python programming"],
    n_results=3,
    where={"source":"web"}
)

# Query with metadata filters
results = collection.query(
    query_texts=["advanced topics"],
    where={
"$and":[
{"category":"tutorial"},
{"difficulty":{"$gte":3}}
]
}
)

# Access results
print(results["documents"])# List of matching documents
print(results["metadatas"])# Metadata for each doc
print(results["distances"])# Similarity scores
print(results["ids"])# Document IDs
```

```python
# Get by IDs
docs = collection.get(
    ids=["id1","id2"]
)

# Get with filters
docs = collection.get(
    where={"category":"tutorial"},
    limit=10
)

# Get all documents
docs = collection.get()
```

```python
# Update document content
collection.update(
    ids=["id1"],
    documents=["Updated content"],
    metadatas=[{"source":"updated"}]
)
```

```python
# Persist to disk
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection("my_docs")
collection.add(documents=["Doc 1"], ids=["id1"])

# Data persisted automatically
# Reload later with same path
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("my_docs")
```

```python
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="openai_docs",
    embedding_function=openai_ef
)
```

```python
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="your-key",
    model_name="sentence-transformers/all-mpnet-base-v2"
)

collection = client.create_collection(
    name="hf_docs",
    embedding_function=huggingface_ef
)
```

```python
from chromadb import Documents, EmbeddingFunction, Embeddings

classMyEmbeddingFunction(EmbeddingFunction):
def__call__(self,input: Documents)-> Embeddings:
# Your embedding logic
return embeddings

my_ef = MyEmbeddingFunction()
collection = client.create_collection(
    name="custom_docs",
    embedding_function=my_ef
)
```

```python
# Exact match
results = collection.query(
    query_texts=["query"],
    where={"category":"tutorial"}
)

# Comparison operators
results = collection.query(
    query_texts=["query"],
    where={"page":{"$gt":10}}# $gt, $gte, $lt, $lte, $ne
)

# Logical operators
results = collection.query(
    query_texts=["query"],
    where={
"$and":[
{"category":"tutorial"},
{"difficulty":{"$lte":3}}
]
}# Also: $or
)

# Contains
results = collection.query(
    query_texts=["query"],
    where={"tags":{"$in":["python","ml"]}}
)
```

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(documents)

# Create Chroma vector store
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)

# Query
results = vectorstore.similarity_search("machine learning", k=3)

# As retriever
retriever = vectorstore.as_retriever(search_kwargs={"k":5})
```

```python
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, StorageContext
import chromadb

# Initialize Chroma
db = chromadb.PersistentClient(path="./chroma_db")
collection = db.get_or_create_collection("my_collection")

# Create vector store
vector_store = ChromaVectorStore(chroma_collection=collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context
)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("What is machine learning?")
```

```python
# Run Chroma server
# Terminal: chroma run --path ./chroma_db --port 8000

# Connect to server
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    settings=Settings(anonymized_telemetry=False)
)

# Use as normal
collection = client.get_or_create_collection("my_docs")
```