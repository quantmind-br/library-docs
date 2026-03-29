---
title: ForgeCode
url: https://forgecode.dev/docs/error-handling/
source: sitemap
fetched_at: 2026-03-29T16:30:38.427053-03:00
rendered_js: false
word_count: 344
summary: This document explains the automatic retry mechanism and exponential backoff configuration for handling tool call parsing errors in ForgeCode.
tags:
    - error-handling
    - automatic-retries
    - exponential-backoff
    - forgecode-configuration
    - tool-call-parsing
category: configuration
---

ForgeCode includes error handling capabilities, including limited automatic retry mechanisms with exponential backoff for specific types of errors. This documentation covers how to configure and optimize these features for improved system resilience.

ForgeCode currently implements automatic retries specifically for tool call parsing errors that occur during agent interactions. This ensures that temporary issues in parsing tool calls don't cause complete workflow failures.

### How It Works[​](#how-it-works "Direct link to How It Works")

When a tool call parsing error occurs:

1. ForgeCode detects the parsing failure
2. A retry is attempted after an initial delay
3. Each subsequent retry uses an exponentially increasing delay with jitter
4. After reaching the maximum retry count, the operation fails permanently
5. Success at any point in the retry sequence continues normal execution

This targeted approach helps maintain conversational flow by gracefully handling errors in the agent's tool usage expressions.

The retry mechanism can be configured in your `forge.yaml` file:

### Configuration Parameters[​](#configuration-parameters "Direct link to Configuration Parameters")

ParameterDefaultDescription`max_attempts`3Maximum number of attempts (including initial attempt)`initial_delay_ms`200Initial delay before first retry (milliseconds)`backoff_factor`2Exponential multiplier for delay between retries

### How Backoff Works[​](#how-backoff-works "Direct link to How Backoff Works")

With default settings, retry delays follow this pattern (with added jitter):

1. Initial attempt fails
2. Wait ~200ms (initial\_delay\_ms with jitter)
3. First retry fails
4. Wait ~400ms (initial\_delay\_ms × backoff\_factor with jitter)
5. Second retry fails
6. Wait ~800ms (previous delay × backoff\_factor with jitter)

The delay approximately doubles with each retry until reaching the maximum number of attempts.

Currently, ForgeCode implements retries only for specific error types:

### Tool Call Parsing Errors[​](#tool-call-parsing-errors "Direct link to Tool Call Parsing Errors")

The following parsing-related errors trigger automatic retries:

- `ToolCallParse`: Errors that occur when parsing a tool call expression
- `ToolCallArgument`: Errors related to invalid arguments in a tool call
- `ToolCallMissingName`: Errors when a tool call is missing a required name

These retries help handle cases where the AI model produces malformed tool call syntax but might output correct syntax on a retry.

### Adjusting Retry Parameters[​](#adjusting-retry-parameters "Direct link to Adjusting Retry Parameters")

Optimize retry settings based on your specific use case:

#### For High-Quality Models[​](#for-high-quality-models "Direct link to For High-Quality Models")

Models that rarely produce syntax errors may benefit from fewer retries:

#### For More Exploratory Workflows[​](#for-more-exploratory-workflows "Direct link to For More Exploratory Workflows")

Workflows that might push model boundaries could benefit from more patient retries:

Here's a comprehensive example combining retry configuration with error logging: