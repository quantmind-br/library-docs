---
title: Get Model Info
url: https://lmstudio.ai/docs/typescript/model-info/get-model-info
source: sitemap
fetched_at: 2026-04-07T21:28:43.267019851-03:00
rendered_js: false
word_count: 12
summary: This document demonstrates how to retrieve detailed information about a loaded local language model using the getInfo method from the LMStudio SDK.
tags:
    - lmstudio-sdk
    - model-info
    - api-usage
    - language-models
    - client-methods
category: reference
---

You can access information about a loaded model using the `getInfo` method.

```
import { LMStudioClient } from "@lmstudio/sdk";

const client = new LMStudioClient();
const model = await client.llm.model();

const modelInfo = await model.getInfo();

console.info("Model Key", modelInfo.modelKey);
console.info("Current Context Length", model.contextLength);
console.info("Model Trained for Tool Use", modelInfo.trainedForToolUse);
// etc.
```