---
title: '`LLMPredictionConfigInput`'
url: https://lmstudio.ai/docs/typescript/api-reference/llm-prediction-config-input
source: sitemap
fetched_at: 2026-04-07T21:28:47.987332708-03:00
rendered_js: false
word_count: 848
summary: This document provides a detailed reference of various optional parameters used for controlling and tuning large language model generation, covering aspects like token limits, sampling diversity, context management, and structured output.
tags:
    - llm-parameters
    - generation-control
    - sampling-techniques
    - api-reference
    - model-tuning
category: reference
---

maxTokens (optional) : number | false

Number of tokens to predict at most. If set to false, the model will predict as many tokens as it wants.

When the prediction is stopped because of this limit, the `stopReason` in the prediction stats will be set to `maxPredictedTokensReached`.

temperature (optional) : number

The temperature parameter for the prediction model. A higher value makes the predictions more random, while a lower value makes the predictions more deterministic. The value should be between 0 and 1.

stopStrings (optional) : Array&lt;string&gt;

An array of strings. If the model generates one of these strings, the prediction will stop.

When the prediction is stopped because of this limit, the `stopReason` in the prediction stats will be set to `stopStringFound`.

toolCallStopStrings (optional) : Array&lt;string&gt;

An array of strings. If the model generates one of these strings, the prediction will stop with the `stopReason` `toolCalls`.

contextOverflowPolicy (optional) : LLMContextOverflowPolicy

The behavior for when the generated tokens length exceeds the context window size. The allowed values are:

- `stopAtLimit`: Stop the prediction when the generated tokens length exceeds the context window size. If the generation is stopped because of this limit, the `stopReason` in the prediction stats will be set to `contextLengthReached`
- `truncateMiddle`: Keep the system prompt and the first user message, truncate middle.
- `rollingWindow`: Maintain a rolling window and truncate past messages.

structured (optional) : ZodType&lt;TStructuredOutputType&gt; | LLMStructuredPredictionSetting

Configures the model to output structured JSON data that follows a specific schema defined using Zod.

When you provide a Zod schema, the model will be instructed to generate JSON that conforms to that schema rather than free-form text.

This is particularly useful for extracting specific data points from model responses or when you need the output in a format that can be directly used by your application.

topKSampling (optional) : number

Controls token sampling diversity by limiting consideration to the K most likely next tokens.

For example, if set to 40, only the 40 tokens with the highest probabilities will be considered for the next token selection. A lower value (e.g., 20) will make the output more focused and conservative, while a higher value (e.g., 100) allows for more creative and diverse outputs.

Typical values range from 20 to 100.

repeatPenalty (optional) : number | false

Applies a penalty to repeated tokens to prevent the model from getting stuck in repetitive patterns.

A value of 1.0 means no penalty. Values greater than 1.0 increase the penalty. For example, 1.2 would reduce the probability of previously used tokens by 20%. This is particularly useful for preventing the model from repeating phrases or getting stuck in loops.

Set to false to disable the penalty completely.

minPSampling (optional) : number | false

Sets a minimum probability threshold that a token must meet to be considered for generation.

For example, if set to 0.05, any token with less than 5% probability will be excluded from consideration. This helps filter out unlikely or irrelevant tokens, potentially improving output quality.

Value should be between 0 and 1. Set to false to disable this filter.

topPSampling (optional) : number | false

Implements nucleus sampling by only considering tokens whose cumulative probabilities reach a specified threshold.

For example, if set to 0.9, the model will consider only the most likely tokens that together add up to 90% of the probability mass. This helps balance between diversity and quality by dynamically adjusting the number of tokens considered based on their probability distribution.

Value should be between 0 and 1. Set to false to disable nucleus sampling.

xtcProbability (optional) : number | false

Controls how often the XTC (Exclude Top Choices) sampling technique is applied during generation.

XTC sampling can boost creativity and reduce clichés by occasionally filtering out common tokens. For example, if set to 0.3, there's a 30% chance that XTC sampling will be applied when generating each token.

Value should be between 0 and 1. Set to false to disable XTC completely.

xtcThreshold (optional) : number | false

Defines the lower probability threshold for the XTC (Exclude Top Choices) sampling technique.

When XTC sampling is activated (based on xtcProbability), the algorithm identifies tokens with probabilities between this threshold and 0.5, then removes all such tokens except the least probable one. This helps introduce more diverse and unexpected tokens into the generation.

Only takes effect when xtcProbability is enabled.

cpuThreads (optional) : number

Specifies the number of CPU threads to allocate for model inference.

Higher values can improve performance on multi-core systems but may compete with other processes. For example, on an 8-core system, a value of 4-6 might provide good performance while leaving resources for other tasks.

If not specified, the system will use a default value based on available hardware.

draftModel (optional) : string

The draft model to use for speculative decoding. Speculative decoding is a technique that can drastically increase the generation speed (up to 3x for larger models) by paring a main model with a smaller draft model.

See here for more information: [https://lmstudio.ai/docs/advanced/speculative-decoding](https://lmstudio.ai/docs/advanced/speculative-decoding)

You do not need to load the draft model yourself. Simply specifying its model key here is enough.