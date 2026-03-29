---
title: Error Handling | goose
url: https://block.github.io/goose/docs/goose-architecture/error-handling
source: github_pages
fetched_at: 2026-01-22T22:13:28.363310145-03:00
rendered_js: true
word_count: 271
summary: This document explains the two primary types of error handling in the Goose framework, focusing on how system failures and agent-specific tool errors are processed and surfaced for model recovery.
tags:
    - error-handling
    - llm-agents
    - goose-framework
    - tool-use
    - rust-development
category: concept
---

Error handling is a key performance-driving part of goose. There are many ways that the non-determinism in the LLM can introduce an error that it can in turn recover from. In a typical goose session, it's expected for there to be several agent errors that the model can see directly and correct, perhaps entirely behind the scenes.

## Traditional Errors[​](#traditional-errors "Direct link to Traditional Errors")

While the agent is operating, there can be intermittent issues in the network, availability of the foundational model, etc. These are raised as errors in the agent API to the caller, who can decide how to handle that. We generally handle these with [anyhow::Error](https://docs.rs/anyhow/latest/anyhow/).

## Agent Errors[​](#agent-errors "Direct link to Agent Errors")

There are several types of errors where everything is working correctly, but the model generations themselves are somehow causing errors. Things like generating an unknown tool name, incorrect parameters, or a well formed tool call that results in an error in the tool itself. All of these can be surfaced to the LLM to have it attempt to recover.

The error messages are in some ways prompting - they give instructions to the LLM on how it might go about recovering. We handle these with [thiserror::Error](https://docs.rs/thiserror/latest/thiserror/) and carefully maintain a collection.

To cover all these cases, both `ToolUse` and `ToolResult` are typically passed through the API as part of a `Result<T, AgentError>`. An error in a `ToolUse` will immediately become an error in a `ToolResult` and passed back to the LLM. A valid `ToolUse` might still end up in an error `ToolResult`, which is also passed back to the LLM.

The providers then handle translating the agent errors into the various API specs as valid messages.