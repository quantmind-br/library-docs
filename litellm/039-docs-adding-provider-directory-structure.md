---
title: Directory Structure | liteLLM
url: https://docs.litellm.ai/docs/adding_provider/directory_structure
source: sitemap
fetched_at: 2026-01-21T19:43:55.165318551-03:00
rendered_js: false
word_count: 24
summary: This document outlines the required directory structure and file organization for integrating a new model provider into the LiteLLM library.
tags:
    - litellm
    - provider-integration
    - directory-structure
    - llm-backend
    - api-integration
category: guide
---

When adding a new provider, you need to create a directory for the provider that follows the following structure:

```
litellm/llms/
└── provider_name/
    ├── completion/ # use when endpoint is equivalent to openai's `/v1/completions`
    │   ├── handler.py
    │   └── transformation.py
    ├── chat/ # use when endpoint is equivalent to openai's `/v1/chat/completions`
    │   ├── handler.py
    │   └── transformation.py
    ├── embed/ # use when endpoint is equivalent to openai's `/v1/embeddings`
    │   ├── handler.py
    │   └── transformation.py
    ├── audio_transcription/ # use when endpoint is equivalent to openai's `/v1/audio/transcriptions`
    │   ├── handler.py
    │   └── transformation.py
    └── rerank/ # use when endpoint is equivalent to cohere's `/rerank` endpoint.
        ├── handler.py
        └── transformation.py
```