---
title: List Loaded Models
url: https://lmstudio.ai/docs/typescript/manage-models/list-loaded
source: sitemap
fetched_at: 2026-04-07T21:28:53.672553956-03:00
rendered_js: false
word_count: 52
summary: This document demonstrates how to retrieve a list of models currently loaded in memory using the `listLoaded` method available within the `LMStudioClient` object for both LLM and embedding namespaces.
tags:
    - lmstudio-client
    - listloaded
    - llm-models
    - embedding-models
    - sdk-usage
category: guide
---

You can iterate through models loaded into memory using the `listLoaded` method. This method lives under the `llm` and `embedding` namespaces of the `LMStudioClient` object.

## List Models Currently Loaded in Memory[](#list-models-currently-loaded-in-memory "Link to 'List Models Currently Loaded in Memory'")

This will give you results equivalent to using [`lms ps`](https://lmstudio.ai/docs/cli/ps) in the CLI.

```
import { LMStudioClient } from "@lmstudio/sdk";

const client = new LMStudioClient();

const llmOnly = await client.llm.listLoaded();
const embeddingOnly = await client.embedding.listLoaded();
```