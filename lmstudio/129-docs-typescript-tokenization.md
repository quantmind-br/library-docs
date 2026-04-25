---
title: Tokenization
url: https://lmstudio.ai/docs/typescript/tokenization
source: sitemap
fetched_at: 2026-04-07T21:28:58.003740605-03:00
rendered_js: false
word_count: 123
summary: This document explains how to use an SDK to interact with a loaded LLM or embedding model for tokenization tasks. It provides methods for both getting the full list of tokens and simply counting the total number of tokens, including checking if a conversation fits within the model's context.
tags:
    - tokenization
    - llm-interaction
    - sdk-utility
    - context-length
    - token-counting
category: guide
---

Models use a tokenizer to internally convert text into "tokens" they can deal with more easily. LM Studio exposes this tokenizer for utility.

## Tokenize[](#tokenize "Link to 'Tokenize'")

You can tokenize a string with a loaded LLM or embedding model using the SDK. In the below examples, `llm` can be replaced with an embedding model `emb`.

```
import { LMStudioClient } from "@lmstudio/sdk";

const client = new LMStudioClient();
const model = await client.llm.model();

const tokens = await model.tokenize("Hello, world!");

console.info(tokens); // Array of token IDs.
```

## Count tokens[](#count-tokens "Link to 'Count tokens'")

If you only care about the number of tokens, you can use the `.countTokens` method instead.

```
const tokenCount = await model.countTokens("Hello, world!");
console.info("Token count:", tokenCount);
```

### Example: Count Context[](#example-count-context)

You can determine if a given conversation fits into a model's context by doing the following:

- Convert the conversation to a string using the prompt template.
- Count the number of tokens in the string.
- Compare the token count to the model's context length.

```
import { Chat, type LLM, LMStudioClient } from "@lmstudio/sdk";

async function doesChatFitInContext(model: LLM, chat: Chat) {
  // Convert the conversation to a string using the prompt template.
  const formatted = await model.applyPromptTemplate(chat);
  // Count the number of tokens in the string.
  const tokenCount = await model.countTokens(formatted);
  // Get the current loaded context length of the model
  const contextLength = await model.getContextLength();
  return tokenCount < contextLength;
}

const client = new LMStudioClient();
const model = await client.llm.model();

const chat = Chat.from([
  { role: "user", content: "What is the meaning of life." },
  { role: "assistant", content: "The meaning of life is..." },
  // ... More messages
]);

console.info("Fits in context:", await doesChatFitInContext(model, chat));
```