---
title: Migration guides | Mistral Docs
url: https://docs.mistral.ai/resources/migration-guides
source: sitemap
fetched_at: 2026-04-26T04:11:40.970877518-03:00
rendered_js: false
word_count: 307
summary: This document provides instructions for migrating existing applications to the Mistral API, including code adjustments, tokenizer updates, and SDK version upgrades.
tags:
    - mistral-api
    - api-migration
    - sdk-upgrade
    - tokenization
    - prompt-engineering
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral API follows the same Chat Completions structure as OpenAI. Most migrations require changing: client import, base URL, and model name.

## Client Update

**Before (OpenAI):**
```python
from openai import OpenAI
client = OpenAI(api_key="...")
```

**After (Mistral):**
```python
from mistralai import Mistral
client = Mistral(api_key="...")
```

## Key Differences

| Aspect | OpenAI | Mistral |
|--------|--------|---------|
| Base URL | `api.openai.com/v1` | `api.mistral.ai/v1` |
| Model name | `gpt-4` | `mistral-large-latest` |

## OpenAI-Compatible Clients

For LangChain, LlamaIndex, or third-party libraries, point at Mistral API by changing base URL and model name only. No library swap needed.

## Tokenizer

Mistral models use a different tokenizer than Llama. Install the official tokenizer:

```bash
pip install mistral-tokenizer
```

```python
from mistral_tokenizer import MistralTokenizer
tokenizer = MistralTokenizer.from_model("mistral-large-latest")
tokens = tokenizer.encode("Your text here")
```

HuggingFace models also work with `transformers` library — use `apply_chat_template` for automatic formatting.

## Prompt Format

> [!warning]
> Mistral models don't use `[INST]` / `[/INST]` from Llama 2. Passing Llama 2-formatted strings produces degraded output.

Use `apply_chat_template`:
```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
messages = [{"role": "user", "content": "Your query"}]
formatted = tokenizer.apply_chat_template(messages, tokenize=False)
```

## SDK V2 Migration

Version 2.0.0 introduces breaking changes. V1 = `mistralai<2`, V2 = `mistralai>=2`.

**Update package:**
```bash
pip install mistralai>=2.0.0
```

**Import path changes:**

| Platform | V1 | V2 |
|----------|----|----|
| Default | `from mistralai.client import MistralClient` | `from mistralai import Mistral` |
| Azure | `from mistralai.client.azure import MistralAzureClient` | `from mistralai import Mistral` |
| Google Cloud | `import vertexai` + `mistralchat` | `from mistralai import Mistral` |

All other APIs (chat, streaming, embeddings, agents, function calling, batch) are unchanged. #mistral-api #api-migration #sdk-upgrade