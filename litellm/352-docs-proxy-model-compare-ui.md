---
title: Model Compare Playground UI | liteLLM
url: https://docs.litellm.ai/docs/proxy/model_compare_ui
source: sitemap
fetched_at: 2026-01-21T19:53:01.145199516-03:00
rendered_js: false
word_count: 620
summary: This document explains how to use the Model Compare Playground UI to perform side-by-side evaluations of multiple LLM models based on response quality, performance metrics, and cost.
tags:
    - model-comparison
    - llm-playground
    - performance-metrics
    - litellm-proxy
    - model-evaluation
    - cost-analysis
    - benchmarking
category: guide
---

Compare multiple LLM models side-by-side in an interactive playground interface. Evaluate model responses, performance metrics, and costs to make informed decisions about which models work best for your use case.

This feature is **available in v1.80.0-stable and above**.

## Overview[​](#overview "Direct link to Overview")

The Model Compare Playground UI enables side-by-side comparison of up to 3 different LLM models simultaneously. Configure models, parameters, and test prompts to evaluate and compare model responses with detailed metrics including latency, token usage, and cost.

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Accessing the Model Compare UI[​](#accessing-the-model-compare-ui "Direct link to Accessing the Model Compare UI")

#### 1. Navigate to the Playground[​](#1-navigate-to-the-playground "Direct link to 1. Navigate to the Playground")

Go to the Playground page in the Admin UI (`PROXY_BASE_URL/ui/?login=success&page=llm-playground`)

#### 2. Switch to Compare Tab[​](#2-switch-to-compare-tab "Direct link to 2. Switch to Compare Tab")

Click on the **Compare** tab in the Playground interface.

## Configuration[​](#configuration "Direct link to Configuration")

### Setting Up Models[​](#setting-up-models "Direct link to Setting Up Models")

#### 1. Select Models to Compare[​](#1-select-models-to-compare "Direct link to 1. Select Models to Compare")

You can compare up to 3 models simultaneously. For each comparison panel:

- Click on the model dropdown to see available models
- Select a model from your configured endpoints
- Models are loaded from your LiteLLM proxy configuration

#### 2. Configure Model Parameters[​](#2-configure-model-parameters "Direct link to 2. Configure Model Parameters")

Each model panel supports individual parameter configuration:

**Basic Parameters:**

- **Temperature**: Controls randomness (0.0 to 2.0)
- **Max Tokens**: Maximum tokens in the response

**Advanced Parameters:**

- Enable "Use Advanced Params" to configure additional model-specific parameters
- Supports all parameters available for the selected model/provider

#### 3. Apply Parameters Across Models[​](#3-apply-parameters-across-models "Direct link to 3. Apply Parameters Across Models")

Use the "Sync Settings Across Models" toggle to synchronize parameters (tags, guardrails, temperature, max tokens, etc.) across all comparison panels for consistent testing.

### Guardrails[​](#guardrails "Direct link to Guardrails")

Configure and test guardrails directly in the playground:

1. Click on the guardrails selector in a model panel
2. Select one or more guardrails from your configured list
3. Test how different models respond to guardrail filtering
4. Compare guardrail behavior across models

### Tags[​](#tags "Direct link to Tags")

Apply tags to organize and filter your comparisons:

1. Select tags from the tag dropdown
2. Tags help categorize and track different test scenarios

### Vector Stores[​](#vector-stores "Direct link to Vector Stores")

Configure vector store retrieval for RAG (Retrieval Augmented Generation) comparisons:

1. Select vector stores from the dropdown
2. Compare how different models utilize retrieved context
3. Evaluate RAG performance across models

## Running Comparisons[​](#running-comparisons "Direct link to Running Comparisons")

### 1. Enter Your Prompt[​](#1-enter-your-prompt "Direct link to 1. Enter Your Prompt")

Type your test prompt in the message input area. You can:

- Enter a single message for all models
- Use suggested prompts for quick testing
- Build multi-turn conversations

### 2. Send Request[​](#2-send-request "Direct link to 2. Send Request")

Click the send button (or press Enter) to start the comparison. All selected models will process the request simultaneously.

### 3. View Responses[​](#3-view-responses "Direct link to 3. View Responses")

Responses appear side-by-side in each model panel, making it easy to compare:

- Response quality and content
- Response length and structure
- Model-specific formatting

## Comparison Metrics[​](#comparison-metrics "Direct link to Comparison Metrics")

Each comparison panel displays detailed metrics to help you evaluate model performance:

### Time To First Token (TTFT)[​](#time-to-first-token-ttft "Direct link to Time To First Token (TTFT)")

Measures the latency from request submission to the first token received. Lower values indicate faster initial response times.

### Token Usage[​](#token-usage "Direct link to Token Usage")

- **Input Tokens**: Number of tokens in the prompt/request
- **Output Tokens**: Number of tokens in the model's response
- **Reasoning Tokens**: Tokens used for reasoning (if applicable, e.g., o1 models)

### Total Latency[​](#total-latency "Direct link to Total Latency")

Complete time from request to final response, including streaming time.

### Cost[​](#cost "Direct link to Cost")

If cost tracking is enabled in your LiteLLM configuration, you'll see:

- Cost per request
- Cost breakdown by input/output tokens
- Comparison of costs across models

## Use Cases[​](#use-cases "Direct link to Use Cases")

### Model Selection[​](#model-selection "Direct link to Model Selection")

Compare multiple models on the same prompt to determine which performs best for your specific use case:

- Response quality
- Response time
- Cost efficiency
- Token usage

### Parameter Tuning[​](#parameter-tuning "Direct link to Parameter Tuning")

Test different parameter configurations across models to find optimal settings:

- Temperature variations
- Max token limits
- Advanced parameter combinations

### Guardrail Testing[​](#guardrail-testing "Direct link to Guardrail Testing")

Evaluate how different models respond to safety filters and guardrails:

- Filter effectiveness
- False positive rates
- Model-specific guardrail behavior

### A/B Testing[​](#ab-testing "Direct link to A/B Testing")

Use tags and multiple comparisons to run structured A/B tests:

- Compare model versions
- Test prompt variations
- Evaluate feature rollouts

* * *

- [Playground Chat UI](https://docs.litellm.ai/docs/proxy/playground.md) - Single model testing interface
- [Model Management](https://docs.litellm.ai/docs/proxy/model_management) - Configure and manage models
- [Guardrails](https://docs.litellm.ai/docs/proxy/guardrails.md) - Set up safety filters
- [AI Hub](https://docs.litellm.ai/docs/proxy/ai_hub) - Share models and agents with your organization