---
title: Tokenization - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-templates
source: crawler
fetched_at: 2026-01-29T07:34:52.608002589-03:00
rendered_js: false
word_count: 82
summary: This document outlines the different versions of tokenizers used by Mistral AI models, specifying their underlying libraries and formatting structures for instructions.
tags:
    - mistral-ai
    - tokenization
    - sentencepiece
    - tiktoken
    - model-compatibility
    - llm-infrastructure
category: reference
---

Tokenizer V1`sentencepiece`Mistral-7B-v0.1, Mistral-7B-Instruct-v0.1, Mistral-7B-v0.2, Mistral-7B-Instruct-v0.2, Mixtral-8x7B-v0.1, Mixtral-8x7B-Instruct-v0.1, Mixtral-8x22B-v0.1`<s> [INST] Hello, how are you? [/INST] Fine, and you?</s> [INST] I'm doing great! [/INST] Glad to hear!</s>`Tokenizer V2`sentencepiece`*No models with weights available released*`<s>[INST] Hello, how are you?[/INST] Fine, and you?</s>[INST] I'm doing great![/INST] Glad to hear!</s>`Tokenizer V3`sentencepiece`Mixtral-8x22B-Instruct-v0.1, Mistral-7B-v0.3, Mistral-7B-Instruct-v0.3, Codestral-22B-v0.1, Mathstral-7B-v0.3, Mamba-Codestral-7B-v0.1, Mistral-Large-123B-Instruct-2407, Mistral Small 22B Instruct 2407`<s>[INST] Hello, how are you?[/INST] Fine, and you?</s>[INST] I'm doing great![/INST] Glad to hear!</s>`Tokenizer V3-Tekken`tiktoken`Mistral-Nemo-12B-2407, Mistral-Nemo-12B-Instruct-2407, Pixtral-12B-2409, Ministral-8B-Instruct-2410`<s>[INST]Hello, how are you?[/INST]Fine, and you?</s>[INST]I'm doing great![/INST]Glad to hear!</s>`