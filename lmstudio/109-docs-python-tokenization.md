---
title: Tokenization
url: https://lmstudio.ai/docs/python/tokenization
source: sitemap
fetched_at: 2026-04-07T21:27:37.521440704-03:00
rendered_js: false
word_count: 131
summary: This document details how to use the LM Studio SDK's tokenizer functionality to convert text into token IDs and demonstrates methods for counting tokens or checking if a conversation fits within a model's context window.
tags:
    - tokenizer
    - tokenization
    - llm-sdk
    - counting-tokens
    - context-length
category: tutorial
---

Models use a tokenizer to internally convert text into "tokens" they can deal with more easily. LM Studio exposes this tokenizer for utility.

## Tokenize[](#tokenize "Link to 'Tokenize'")

You can tokenize a string with a loaded LLM or embedding model using the SDK. In the below examples, the LLM reference can be replaced with an embedding model reference without requiring any other changes.

```
import lmstudio as lms

model = lms.llm()

tokens = model.tokenize("Hello, world!")

print(tokens) # Array of token IDs.
```

## Count tokens[](#count-tokens "Link to 'Count tokens'")

If you only care about the number of tokens, simply check the length of the resulting array.

```
token_count = len(model.tokenize("Hello, world!"))
print("Token count:", token_count)
```

### Example: count context[](#example-count-context)

You can determine if a given conversation fits into a model's context by doing the following:

- Convert the conversation to a string using the prompt template.
- Count the number of tokens in the string.
- Compare the token count to the model's context length.

```
import lmstudio as lms

def does_chat_fit_in_context(model: lms.LLM, chat: lms.Chat) → bool:
    # Convert the conversation to a string using the prompt template.
    formatted = model.apply_prompt_template(chat)
    # Count the number of tokens in the string.
    token_count = len(model.tokenize(formatted))
    # Get the current loaded context length of the model
    context_length = model.get_context_length()
    return token_count < context_length

model = lms.llm()

chat = lms.Chat.from_history({
    "messages": [
        { "role": "user", "content": "What is the meaning of life." },
        { "role": "assistant", "content": "The meaning of life is..." },
        # ... More messages
    ]
})

print("Fits in context:", does_chat_fit_in_context(model, chat))
```