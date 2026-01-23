---
title: One post tagged with "azure_storage" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/azure-storage
source: sitemap
fetched_at: 2026-01-21T19:41:20.46696793-03:00
rendered_js: false
word_count: 65
summary: This document highlights key updates in the LiteLLM v1.55.8 stable release, including new features for remote prompt management via Langfuse and usage data logging to Azure Data Lake.
tags:
    - litellm
    - stable-release
    - azure-data-lake
    - prompt-management
    - logging
    - llm-proxy
category: reference
---

A new LiteLLM Stable release [just went out](https://github.com/BerriAI/litellm/releases/tag/v1.55.8-stable). Here are 5 updates since v1.52.2-stable.

This makes it easy to run experiments or change the specific models `gpt-4o` to `gpt-4o-mini` on Langfuse, instead of making changes in your applications. [Start here](https://docs.litellm.ai/docs/proxy/prompt_management)

Send LLM usage (spend, tokens) data to [Azure Data Lake](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction). This makes it easy to consume usage data on other services (eg. Databricks) [Start here](https://docs.litellm.ai/docs/proxy/logging#azure-blob-storage)

```
docker run \
-e STORE_MODEL_IN_DB=True \
-p 4000:4000 \
docker.litellm.ai/berriai/litellm:litellm_stable_release_branch-v1.55.8-stable
```