---
title: Gemini File Search | liteLLM
url: https://docs.litellm.ai/docs/providers/gemini_file_search
source: sitemap
fetched_at: 2026-01-21T19:49:10.07154157-03:00
rendered_js: false
word_count: 73
summary: This document explains how to use LiteLLM to interface with Google Gemini's File Search for document ingestion, indexing, and Retrieval Augmented Generation (RAG).
tags:
    - litellm
    - google-gemini
    - rag
    - vector-store
    - file-search
    - document-indexing
    - python
category: tutorial
---

Use Google Gemini's File Search for Retrieval Augmented Generation (RAG) with LiteLLM.

Gemini File Search imports, chunks, and indexes your data to enable fast retrieval of relevant information based on user prompts. This information is then provided as context to the model for more accurate and relevant answers.

```
import litellm

response =await litellm.aingest(
    ingest_options={
"name":"custom-chunking-store",
"vector_store":{
"custom_llm_provider":"gemini"
},
"chunking_strategy":{
"white_space_config":{
"max_tokens_per_chunk":200,
"max_overlap_tokens":20
}
}
},
    file_data=("document.txt", document_content,"text/plain")
)
```

```
import litellm

response =await litellm.aingest(
    ingest_options={
"name":"metadata-store",
"vector_store":{
"custom_llm_provider":"gemini",
"custom_metadata":[
{"key":"author","string_value":"John Doe"},
{"key":"year","numeric_value":2024},
{"key":"category","string_value":"documentation"}
]
}
},
    file_data=("document.txt", document_content,"text/plain")
)
```

```
import litellm

response =await litellm.vector_stores.asearch(
    vector_store_id="fileSearchStores/your-store-id",
    query="What is LiteLLM?",
    custom_llm_provider="gemini",
    filters={"author":"John Doe","category":"documentation"}
)
```

```
import litellm

# First, create a store
create_response =await litellm.vector_stores.acreate(
    name="My Persistent Store",
    custom_llm_provider="gemini"
)
store_id = create_response["id"]

# Then ingest multiple documents into it
for doc in documents:
await litellm.aingest(
        ingest_options={
"vector_store":{
"custom_llm_provider":"gemini",
"vector_store_id": store_id  # Reuse existing store
}
},
        file_data=(doc["name"], doc["content"], doc["type"])
)
```

```
import litellm

response =await litellm.vector_stores.asearch(
    vector_store_id="fileSearchStores/your-store-id",
    query="Explain the concept",
    custom_llm_provider="gemini"
)

for result in response["data"]:
# Access citation information
if"attributes"in result:
print(f"URI: {result['attributes'].get('uri')}")
print(f"Title: {result['attributes'].get('title')}")

# Content with relevance score
print(f"Score: {result.get('score')}")
print(f"Text: {result['content'][0]['text']}")
```

```
import litellm

# 1. Create a File Search store
store_response =await litellm.vector_stores.acreate(
    name="Knowledge Base",
    custom_llm_provider="gemini"
)
store_id = store_response["id"]
print(f"Created store: {store_id}")

# 2. Ingest documents with custom chunking and metadata
documents =[
{
"name":"intro.txt",
"content":b"Introduction to LiteLLM...",
"metadata":[
{"key":"section","string_value":"intro"},
{"key":"priority","numeric_value":1}
]
},
{
"name":"advanced.txt",
"content":b"Advanced features...",
"metadata":[
{"key":"section","string_value":"advanced"},
{"key":"priority","numeric_value":2}
]
}
]

for doc in documents:
    ingest_response =await litellm.aingest(
        ingest_options={
"name":f"ingest-{doc['name']}",
"vector_store":{
"custom_llm_provider":"gemini",
"vector_store_id": store_id,
"custom_metadata": doc["metadata"]
},
"chunking_strategy":{
"white_space_config":{
"max_tokens_per_chunk":300,
"max_overlap_tokens":50
}
}
},
        file_data=(doc["name"], doc["content"],"text/plain")
)
print(f"Ingested: {doc['name']}")

# 3. Search with filters
search_response =await litellm.vector_stores.asearch(
    vector_store_id=store_id,
    query="How do I get started?",
    custom_llm_provider="gemini",
    filters={"section":"intro"},
    max_num_results=3
)

# 4. Process results
for i, result inenumerate(search_response["data"]):
print(f"\nResult {i+1}:")
print(f"  Score: {result.get('score')}")
print(f"  File: {result.get('filename')}")
print(f"  Content: {result['content'][0]['text'][:100]}...")
```

```
# Ensure API key is set
import os
os.environ["GEMINI_API_KEY"]="your-api-key"

# Or pass explicitly
response =await litellm.aingest(
    ingest_options={
"vector_store":{
"custom_llm_provider":"gemini",
"api_key":"your-api-key"
}
},
    file_data=(...)
)
```

For files &gt;100MB, split them into smaller chunks before ingestion.

After ingestion, Gemini may need time to index documents. Wait a few seconds before searching: