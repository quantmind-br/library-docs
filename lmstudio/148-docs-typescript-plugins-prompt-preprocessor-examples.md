---
title: Examples
url: https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessor/examples
source: sitemap
fetched_at: 2026-04-07T21:32:18.623824725-03:00
rendered_js: false
word_count: 88
summary: This document provides an example of a prompt preprocessor designed to manipulate incoming chat messages by replacing specific trigger words with custom instructional text.
tags:
    - prompt-preprocessor
    - message-manipulation
    - sdk-example
    - text-replacement
category: tutorial
---

The following is an example preprocessor that injects the current time before each user message.

Another example you can do it with simple text only processing is by replacing certain trigger words. For example, you can replace a `@init` trigger with a special initialization message.

src/promptPreprocessor.ts

```
import { type PromptPreprocessorController, type ChatMessage, text } from "@lmstudio/sdk";

const mySpecialInstructions = text`
  Here are some special instructions...
`;

export async function preprocess(ctl: PromptPreprocessorController, userMessage: ChatMessage) {
  const textContent = userMessage.getText();
  const transformed = textContent.replaceAll("@init", mySpecialInstructions);
  return transformed;
}
```