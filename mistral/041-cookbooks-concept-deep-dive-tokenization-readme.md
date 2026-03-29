---
title: 'Concept Deep Dive: Tokenization - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-readme
source: crawler
fetched_at: 2026-01-29T07:33:54.15996691-03:00
rendered_js: false
word_count: 121
---

Tokenization is a crucial concept around LLMs, and it can be more complex than one may think!

For our tokenization implementation, please refer to [mistral-common](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-readme).

In this deep dive, we will dig into 3 versions of our tokenizer:

- V1: The tokenizer behind our very first models.
- V2: Introducing control tokens and function calling!
- V3: Better function calling implementation.
  
  - V3-Tekken: Different version based on `tiktoken`, opposed to the other versions based on `sentencepiece`.

## Overview

SectionDescription[Basics](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-basics)Basics of tokenization.[Boundaries & Token Healing](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-boundaries)Main problems with tokenization and token healing.[Control Tokens](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-control_tokens)Introduction to Control Tokens and their advantages.[Templates](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-templates)A summarized list of our tokenizers with their chat templates.[Tokenizer](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-tokenizer)Make your own tokenizer with sentencepiece.[Tool Calling](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-tool_calling)Learn about how tokenization for our tool calling works.[Chat Templates](https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-chat_templates)Legacy documentation around our chat templates.