---
title: Jina AI | liteLLM
url: https://docs.litellm.ai/docs/providers/jina_ai
source: sitemap
fetched_at: 2026-01-21T19:49:27.507868156-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for using the LiteLLM rerank function to order documents by relevance using the Jina AI reranker model.
tags:
    - litellm
    - rerank
    - jina-ai
    - python-sdk
    - search-optimization
category: tutorial
---

```
from litellm import rerank
import os

os.environ["JINA_AI_API_KEY"]="sk-..."

query ="What is the capital of the United States?"
documents =[
"Carson City is the capital city of the American state of Nevada.",
"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
"Washington, D.C. is the capital of the United States.",
"Capital punishment has existed in the United States since before it was a country.",
]

response = rerank(
    model="jina_ai/jina-reranker-v2-base-multilingual",
    query=query,
    documents=documents,
    top_n=3,
)
print(response)
```