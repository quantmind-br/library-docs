---
title: Voyage AI | liteLLM
url: https://docs.litellm.ai/docs/providers/voyage
source: sitemap
fetched_at: 2026-01-21T19:50:55.66409915-03:00
rendered_js: false
word_count: 363
summary: This document provides technical specifications and implementation examples for using VoyageAI's embedding and reranking models via the LiteLLM library. It covers API configuration, supported model parameters, and specialized features like contextual embeddings for long documents.
tags:
    - voyage-ai
    - embeddings
    - reranking
    - litellm
    - api-reference
    - vector-search
    - python-sdk
category: reference
---

[https://docs.voyageai.com/embeddings/](https://docs.voyageai.com/embeddings/)

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['VOYAGE_API_KEY']
```

## Sample Usage - Embedding[​](#sample-usage---embedding "Direct link to Sample Usage - Embedding")

```
from litellm import embedding
import os

os.environ['VOYAGE_API_KEY']=""
response = embedding(
    model="voyage/voyage-3.5",
input=["good morning from litellm"],
)
print(response)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

VoyageAI embeddings support the following optional parameters:

- `input_type`: Specifies the type of input for retrieval optimization
  
  - `"query"`: Use for search queries
  - `"document"`: Use for documents being indexed
- `dimensions`: Output embedding dimensions (256, 512, 1024, or 2048)
- `encoding_format`: Output format (`"float"`, `"int8"`, `"uint8"`, `"binary"`, `"ubinary"`)
- `truncation`: Whether to truncate inputs exceeding max tokens (default: `True`)

### Example with Parameters[​](#example-with-parameters "Direct link to Example with Parameters")

```
from litellm import embedding
import os

os.environ['VOYAGE_API_KEY']="your-api-key"

# Embedding with custom dimensions and input type
response = embedding(
    model="voyage/voyage-3.5",
input=["Your text here"],
    dimensions=512,
    input_type="document"
)
print(f"Embedding dimensions: {len(response.data[0]['embedding'])}")
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

All models listed here [https://docs.voyageai.com/embeddings/#models-and-specifics](https://docs.voyageai.com/embeddings/#models-and-specifics) are supported

Model NameFunction Callvoyage-3.5`embedding(model="voyage/voyage-3.5", input)`voyage-3.5-lite`embedding(model="voyage/voyage-3.5-lite", input)`voyage-3-large`embedding(model="voyage/voyage-3-large", input)`voyage-3`embedding(model="voyage/voyage-3", input)`voyage-3-lite`embedding(model="voyage/voyage-3-lite", input)`voyage-code-3`embedding(model="voyage/voyage-code-3", input)`voyage-finance-2`embedding(model="voyage/voyage-finance-2", input)`voyage-law-2`embedding(model="voyage/voyage-law-2", input)`voyage-code-2`embedding(model="voyage/voyage-code-2", input)`voyage-multilingual-2`embedding(model="voyage/voyage-multilingual-2 ", input)`voyage-large-2-instruct`embedding(model="voyage/voyage-large-2-instruct", input)`voyage-large-2`embedding(model="voyage/voyage-large-2", input)`voyage-2`embedding(model="voyage/voyage-2", input)`voyage-lite-02-instruct`embedding(model="voyage/voyage-lite-02-instruct", input)`voyage-01`embedding(model="voyage/voyage-01", input)`voyage-lite-01`embedding(model="voyage/voyage-lite-01", input)`voyage-lite-01-instruct`embedding(model="voyage/voyage-lite-01-instruct", input)`

## Contextual Embeddings (voyage-context-3)[​](#contextual-embeddings-voyage-context-3 "Direct link to Contextual Embeddings (voyage-context-3)")

VoyageAI's `voyage-context-3` model provides contextualized chunk embeddings, where each chunk is embedded with awareness of its surrounding document context. This significantly improves retrieval quality compared to standard context-agnostic embeddings.

### Key Benefits[​](#key-benefits "Direct link to Key Benefits")

- Chunks understand their position and role within the full document
- Improved retrieval accuracy for long documents (outperforms competitors by 7-23%)
- Better handling of ambiguous references and cross-chunk dependencies
- Seamless drop-in replacement for standard embeddings in RAG pipelines

### Usage[​](#usage "Direct link to Usage")

Contextual embeddings require a **nested input format** where each inner list represents chunks from a single document:

```
from litellm import embedding
import os

os.environ['VOYAGE_API_KEY']="your-api-key"

# Single document with multiple chunks
response = embedding(
    model="voyage/voyage-context-3",
input=[
[
"Chapter 1: Introduction to AI",
"This chapter covers the basics of artificial intelligence.",
"We will explore machine learning and deep learning."
]
]
)
print(f"Number of chunk groups: {len(response.data)}")

# Multiple documents
response = embedding(
    model="voyage/voyage-context-3",
input=[
["Paris is the capital of France.","It is known for the Eiffel Tower."],
["Tokyo is the capital of Japan.","It is a major economic hub."]
]
)
print(f"Processed {len(response.data)} documents")
```

### Specifications[​](#specifications "Direct link to Specifications")

- Model: `voyage-context-3`
- Context length: 32,000 tokens per document
- Output dimensions: 256, 512, 1024 (default), or 2048
- Max inputs: 1,000 per request
- Max total tokens: 120,000
- Max chunks: 16,000
- Pricing: $0.18 per million tokens

### When to Use Contextual Embeddings[​](#when-to-use-contextual-embeddings "Direct link to When to Use Contextual Embeddings")

**Use `voyage-context-3` when:**

- Processing long documents split into chunks
- Document structure and flow are important
- References between sections matter
- You need to preserve document hierarchy

**Use standard models (voyage-3.5, voyage-3-large) when:**

- Embedding independent pieces of text
- Processing short queries
- Document context is not relevant
- You need faster/cheaper processing

## Model Selection Guide[​](#model-selection-guide "Direct link to Model Selection Guide")

ModelBest ForContext LengthPrice/M Tokensvoyage-3.5General-purpose, multilingual32K$0.06voyage-3.5-liteLatency-sensitive applications32K$0.02voyage-3-largeBest overall quality32K$0.18voyage-code-3Code retrieval and search32K$0.18voyage-finance-2Financial documents32K$0.12voyage-law-2Legal documents16K$0.12voyage-context-3Contextual document embeddings32K$0.18

## Rerank[​](#rerank "Direct link to Rerank")

Voyage AI provides reranking models to improve search relevance by reordering documents based on their relevance to a query.

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import rerank
import os

os.environ["VOYAGE_API_KEY"]="your-api-key"

response = rerank(
    model="voyage/rerank-2.5",
    query="What is the capital of France?",
    documents=[
"Paris is the capital of France.",
"London is the capital of England.",
"Berlin is the capital of Germany.",
],
    top_n=3,
)

print(response)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import arerank
import os
import asyncio

os.environ["VOYAGE_API_KEY"]="your-api-key"

asyncdefmain():
    response =await arerank(
        model="voyage/rerank-2.5-lite",
        query="Best programming language for beginners?",
        documents=[
"Python is great for beginners due to simple syntax.",
"JavaScript runs in browsers and is versatile.",
"Rust has a steep learning curve but is very safe.",
],
        top_n=2,
)
print(response)

asyncio.run(main())
```

### LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

Add to your `config.yaml`:

```
model_list:
-model_name: rerank-2.5
litellm_params:
model: voyage/rerank-2.5
api_key: os.environ/VOYAGE_API_KEY
-model_name: rerank-2.5-lite
litellm_params:
model: voyage/rerank-2.5-lite
api_key: os.environ/VOYAGE_API_KEY
```

Test with curl:

```
curl http://localhost:4000/rerank \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "rerank-2.5",
    "query": "What is the capital of France?",
    "documents": [
        "Paris is the capital of France.",
        "London is the capital of England.",
        "Berlin is the capital of Germany."
    ],
    "top_n": 3
  }'
```

### Supported Rerank Models[​](#supported-rerank-models "Direct link to Supported Rerank Models")

ModelContext LengthDescriptionPrice/M Tokensrerank-2.532KBest quality, multilingual, instruction-following$0.05rerank-2.5-lite32KOptimized for latency and cost$0.02rerank-216KLegacy model$0.05rerank-2-lite8KLegacy model, faster$0.02

### Supported Parameters[​](#supported-parameters-1 "Direct link to Supported Parameters")

ParameterTypeDescription`model`stringModel name (e.g., `voyage/rerank-2.5`)`query`stringThe search query`documents`listList of documents to rerank`top_n`intNumber of top results to return`return_documents`boolWhether to include document text in response