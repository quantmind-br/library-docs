---
title: Enhanced Code Editing with AI Models | goose
url: https://block.github.io/goose/docs/guides/enhanced-code-editing
source: github_pages
fetched_at: 2026-01-22T22:13:47.210450505-03:00
rendered_js: true
word_count: 266
summary: This document explains how to enable and configure AI-powered code editing in the Goose Developer extension using environment variables and OpenAI-compatible APIs to enhance the str_replace tool.
tags:
    - goose-extension
    - ai-code-editing
    - str-replace
    - environment-variables
    - llm-integration
    - developer-tools
category: configuration
---

The [Developer extension](https://block.github.io/goose/docs/mcp/developer-mcp) supports using AI models for enhanced code editing through the `str_replace` command. When configured, it intelligently applies code changes using an AI model instead of simple string replacement.

The use of models specializing in code editing can reduce the load on the main LLM providers while increasing accuracy, quality, and speed and lowering cost. This enhanced approach provides:

- **Context-aware editing**: The AI understands code structure and can make more intelligent changes
- **Better formatting**: Maintains consistent code style and formatting
- **Error prevention**: Can catch and fix potential issues during the edit
- **Flexible model support**: Works with any OpenAI-compatible API
- **Clean implementation**: Uses proper control flow instead of exception handling for configuration checks

## Configuration[​](#configuration "Direct link to Configuration")

Set these [environment variables](https://block.github.io/goose/docs/guides/environment-variables#enhanced-code-editing) to enable AI-powered code editing:

```
export GOOSE_EDITOR_API_KEY="your-api-key-here"
export GOOSE_EDITOR_HOST="https://api.openai.com/v1"
export GOOSE_EDITOR_MODEL="gpt-4o"
```

**All three environment variables must be set and non-empty for the feature to activate.**

This optional feature is completely backwards compatible - if not configured, the extension works exactly as before with simple string replacement.

### Supported Providers[​](#supported-providers "Direct link to Supported Providers")

Any OpenAI-compatible API endpoint should work. Examples:

**OpenAI:**

```
export GOOSE_EDITOR_API_KEY="sk-..."
export GOOSE_EDITOR_HOST="https://api.openai.com/v1"
export GOOSE_EDITOR_MODEL="gpt-4o"
```

**Anthropic (via OpenAI-compatible proxy):**

```
export GOOSE_EDITOR_API_KEY="sk-ant-..."
export GOOSE_EDITOR_HOST="https://api.anthropic.com/v1"
export GOOSE_EDITOR_MODEL="claude-3-5-sonnet-20241022"
```

**Morph:**

```
export GOOSE_EDITOR_API_KEY="sk-..."
export GOOSE_EDITOR_HOST="https://api.morphllm.com/v1"
export GOOSE_EDITOR_MODEL="morph-v0"
```

**Relace:**

```
export GOOSE_EDITOR_API_KEY="rlc-..."
export GOOSE_EDITOR_HOST="https://instantapply.endpoint.relace.run/v1/apply"
export GOOSE_EDITOR_MODEL="auto"
```

**Local/Custom endpoints:**

```
export GOOSE_EDITOR_API_KEY="your-key"
export GOOSE_EDITOR_HOST="http://localhost:8000/v1"
export GOOSE_EDITOR_MODEL="your-model"
```

## How It Works[​](#how-it-works "Direct link to How It Works")

When the `str_replace` tool is used to edit code:

1. **Configuration Check**: goose checks if all three environment variables are properly set and non-empty.
2. **With AI Enabled**: If configured, goose sends the original code and your requested change to the configured AI model for processing.
3. **Fallback**: If the AI API is not configured or the API call fails, it falls back to simple string replacement.
4. **User Feedback**: The first time you use `str_replace` without AI configuration, you'll see a helpful message explaining how to enable the feature.