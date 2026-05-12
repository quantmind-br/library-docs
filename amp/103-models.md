---
title: Models
url: https://ampcode.com/models
source: crawler
fetched_at: 2026-02-06T02:07:30.626041363-03:00
rendered_js: false
word_count: 198
summary: This document details the various foundation and specialized AI models Amp utilizes across different agent modes and system features to optimize performance for tasks like reasoning, search, and code review.
tags:
    - ai-models
    - agent-modes
    - machine-learning
    - code-analysis
    - llm-integration
    - system-architecture
category: reference
---

Amp uses the best model for each task: leading generalist foundation models for complex reasoning and planning, and smaller specialized models for fast, accurate responses in specific domains.

## Agent Modes

### Combination of System Prompt + Tools + Model

[Smart  
\
Unconstrained state-of-the-art model use  
\
Claude Opus 4.6](https://ampcode.com/manual#agent-modes)

[Rush  
\
Faster and cheaper, for small, well-defined tasks  
\
Claude Haiku 4.5](https://ampcode.com/news/rush-mode)

[Deep  
\
Deep reasoning with extended thinking  
\
GPT-5.2 Codex](https://ampcode.com/manual#agent-modes)

## Feature Models

[Review  
\
Bug identification & code review assistance  
\
Gemini 3 Pro](https://ampcode.com/news/review)

## Specialized Subagents

[Search  
\
Fast, accurate codebase retrieval  
\
Gemini 3 Flash](https://ampcode.com/news/gemini-3-flash-search)

[![Oracle](https://ampcode.com/%28marketing%29/models/oracle.png)  
\
Oracle  
\
Complex reasoning & planning on code  
\
GPT-5.2](https://ampcode.com/manual#oracle)

[![Librarian](https://ampcode.com/%28marketing%29/models/librarian.png)  
\
Librarian  
\
Large-scale retrieval & research on external code  
\
Claude Sonnet 4.5](https://ampcode.com/manual#librarian)

## System Models

[Look At  
\
Image, PDF, and media file analysis  
\
Gemini 3 Flash]()

[Painter  
\
Image generation and editing  
\
Gemini 3 Pro Image](https://ampcode.com/manual#painter)

[Handoff  
\
Context analysis for task continuation  
\
Gemini 2.5 Flash](https://ampcode.com/manual#handoff)

[Topics  
\
Thread categorization for indexing & analytics  
\
Gemini 2.5 Flash-Lite]()

[Titling  
\
Fast title generation for threads  
\
Claude Haiku 4.5]()

See the [Amp Security Reference](https://ampcode.com/security) for more details on model use and inference providers.