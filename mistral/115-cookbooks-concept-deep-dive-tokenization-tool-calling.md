---
title: Tokenization - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/concept-deep-dive-tokenization-tool_calling
source: crawler
fetched_at: 2026-01-29T07:34:53.640210433-03:00
rendered_js: false
word_count: 836
summary: This document explains the mechanism of tool calling in large language models and details how different tokenizer versions use control tokens to manage tool interactions and results.
tags:
    - tool-calling
    - tokenization
    - control-tokens
    - llm-features
    - tokenizer-v3
    - tekken
category: guide
---

## Tool Calling

Tool calling is a feature that allows the model to interact with external tools or APIs. The model is provided a list of tools it can pick from, the tool restul is then provided to the model. This can be useful for tasks that require information retrieval, computation, or other functionalities that the model cannot perform on its own. The tool calling feature is implemented using control tokens to ensure efficiency, security, and proper boundary handling.

### Tokenization - Recap

Tokenization is the process of converting a string into a sequence of token IDs. Tokens can be characters, subwords, or symbols. The tokenizer breaks the string into tokens and converts them into IDs (encoding) and vice versa (decoding). The model then predicts the next token based on the sequence. For example, the sentence "Hello, how are" might be tokenized as: `Hello,` -&gt; `432`, `how` -&gt; `523`, `are` -&gt; `87`. The model predicts the next token, such as `75` (decoded as `you`), allowing it to generate coherent text.

### Control Tokens - Recap

Control tokens tackle efficiency, security, and boundary issues. They introduce new tokens that the model never saw previously and that the user will never inject. These tokens replace special strings, making the encoding process more efficient and secure. For example, instead of encapsulating user instructions with special strings, we use control token IDs directly.

### Overall Concept

The idea is as follows:

- The user provides a set of tools and makes a request to the model.
- The Assistant decides what to do. If it does not need a tool, it will answer (it is possible to force the model to pick a tool). If not:
  
  - The Assistant replies with a tool call, mentioning the tool it wants to use and the arguments.
  - The User runs the tool and provides the result.
  - The Assistant replies, knowing the result.

### Tokenizer V2

The tokenizer V2 introduces control tokens for tool calling. These tokens include:

- `BEGIN_AVAILABLE_TOOLS` and `END_AVAILABLE_TOOLS`: Control tokens for the beginning and end of available tools.
- `BEGIN_TOOL_RESULTS` and `END_TOOL_RESULTS`: Control tokens for the beginning and end of tool results.
- `TOOL_CALLS`: Control token for tool calls.

#### Scenario: User Asks for a Calculation

Let's consider a scenario where a user asks the model to perform a calculation using an external tool.  
**User Message:**

We provide the model with a set of tools, for this example we will provide it a single tool.  
**Tools:**

**String Representation:**

Notice the whitespace after some of the control tokens.

Now that the model has the tool, it decides to use it.  
**Assistant Tool Call:**

**Tool Call String Representation:**

Notice the whitespace after some of the control tokens.

The next step, is to run the tool with the provided information. Once we have the result, we provide it to the model.  
**Tool Result:**

**Tool Result String Representation:**

Notice the whitespace after some of the control tokens.

Perfect, the model can now answer!  
**Final Assistant Response:**

**Final String Representation:**

Notice the whitespace after some of the control tokens.

In this scenario, the control tokens `TOOL_CALLS`, `BEGIN_TOOL_RESULTS`, and `END_TOOL_RESULTS` are used to encode the tool call and the tool result. The model can then generate a coherent response based on the tool result!

For better visualization, here is the string broken into different sections:

There is no line breaker in the real version.

### Tokenizer V3

The tokenizer V3 is overall similar to V2, but introduces a slightly different way of encoding tool messages. The main differences are:

1. **Tool Results Encoding:** In V3, tool results are not wrapped in a list, and the history of tool calls is tokenized as well.
2. **Tool Call Encoding:** In V3, tool calls include `id` field, which can be used to track the history of tool calls.

#### Scenario: User Asks for a Calculation

Let's consider the same scenario where a user asks the model to perform a calculation using an external tool.  
**User Message:**

We provide the model with a set of tools, for this example we will provide it a single tool.  
**Tools:**

**String Representation:**

Notice the whitespace after some of the control tokens.

Now that the model has the tool, it decides to use it.  
**Assistant Tool Call:**

**Tool Call String Representation:**

Notice the whitespace after some of the control tokens.

The next step, is to run the tool with the provided information. Once we have the result, we provide it to the model.  
**Tool Result:**

**Tool Result String Representation:**

Notice the whitespace after some of the control tokens.

The model can now answer!  
**Final Assistant Response:**

**Final String Representation:**

Notice the whitespace after some of the control tokens.

String broken into different sections:

There is no line breaker in the real version.

### Tokenizer V3 - Tekken

The main difference with tekken is once more whitespace, its overall the same tokenization, the only difference being that its not based on `sentencepiece`, the final string representation of the previous scenario would look like so:

No whitespace this time.

String broken into different sections:

There is no line breaker in the real version.