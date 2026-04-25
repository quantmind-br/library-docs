---
title: Speculative Decoding
url: https://lmstudio.ai/docs/typescript/llm-prediction/speculative-decoding
source: sitemap
fetched_at: 2026-04-07T21:31:51.187074551-03:00
rendered_js: false
word_count: 106
summary: This document explains how to implement speculative decoding within the `lmstudio-js` library to boost LLM generation speed while maintaining response quality.
tags:
    - speculative-decoding
    - llms
    - javascript
    - prediction
    - generation-speed
    - client
category: tutorial
---

Speculative decoding is a technique that can substantially increase the generation speed of large language models (LLMs) without reducing response quality. See [Speculative Decoding](https://lmstudio.ai/docs/app/advanced/speculative-decoding) for more info.

To use speculative decoding in `lmstudio-js`, simply provide a `draftModel` parameter when performing the prediction. You do not need to load the draft model separately.

```
import { LMStudioClient } from "@lmstudio/sdk";

const client = new LMStudioClient();

const mainModelKey = "qwen2.5-7b-instruct";
const draftModelKey = "qwen2.5-0.5b-instruct";

const model = await client.llm.model(mainModelKey);
const result = await model.respond("What are the prime numbers between 0 and 100?", {
  draftModel: draftModelKey,
});

const { content, stats } = result;
console.info(content);
console.info(`Accepted ${stats.acceptedDraftTokensCount}/${stats.predictedTokensCount} tokens`);
```