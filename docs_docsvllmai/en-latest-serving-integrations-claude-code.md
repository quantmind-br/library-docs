---
title: Claude Code - vLLM
url: https://docs.vllm.ai/en/latest/serving/integrations/claude_code/
source: sitemap
fetched_at: 2026-05-07T21:15:15.952036922-03:00
rendered_js: false
word_count: 523
summary: This document provides instructions on configuring the Claude Code agentic tool to use a local vLLM server as a backend instead of the Anthropic API. It explains the requirements for tool-calling models and the environment variables needed to establish a successful connection.
tags:
    - claude-code
    - vllm-server
    - tool-calling
    - agentic-coding
    - anthropic-api
    - model-deployment
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/serving/integrations/claude_code.md "Edit this page")

[Claude Code](https://code.claude.com/docs/en/quickstart) is Anthropic's official agentic coding tool that lives in your terminal. It can understand your codebase, edit files, run commands, and help you write code more efficiently.

By pointing Claude Code at a vLLM server, you can use your own models as the backend instead of the Anthropic API. This is useful for:

- Running fully local/private coding assistance
- Using open-weight models with tool calling capabilities
- Testing and developing with custom models

## How It Works[¶](#how-it-works "Permanent link")

vLLM implements the Anthropic Messages API, which is the same API that Claude Code uses to communicate with Anthropic's servers. By setting `ANTHROPIC_BASE_URL` to point at your vLLM server, Claude Code sends its requests to vLLM instead of Anthropic. vLLM then translates these requests to work with your local model and returns responses in the format Claude Code expects.

This means any model served by vLLM with proper tool calling support can act as a drop-in replacement for Claude models in Claude Code.

## Requirements[¶](#requirements "Permanent link")

Claude Code requires a model with strong tool calling capabilities. The model must support the OpenAI-compatible tool calling API. See [Tool Calling](https://docs.vllm.ai/en/latest/features/tool_calling/) for details on enabling tool calling for your model.

## Installation[¶](#installation "Permanent link")

First, install Claude Code by following the [official installation guide](https://docs.anthropic.com/en/docs/claude-code/getting-started).

## Starting the vLLM Server[¶](#starting-the-vllm-server "Permanent link")

Start vLLM with a tool-calling capable model - here's an example using `openai/gpt-oss-120b`:

```
vllmserveopenai/gpt-oss-120b--served-model-namemy-model--enable-auto-tool-choice--tool-call-parseropenai
```

For other models, you'll need to enable tool calling explicitly with `--enable-auto-tool-choice` and the right `--tool-call-parser`. Refer to the [Tool Calling documentation](https://docs.vllm.ai/en/latest/features/tool_calling/) for the correct flags for your model.

## Configuring Claude Code[¶](#configuring-claude-code "Permanent link")

Launch Claude Code with environment variables pointing to your vLLM server:

```
ANTHROPIC_BASE_URL=http://localhost:8000\
ANTHROPIC_API_KEY=dummy\
ANTHROPIC_AUTH_TOKEN=dummy\
ANTHROPIC_DEFAULT_OPUS_MODEL=my-model\
ANTHROPIC_DEFAULT_SONNET_MODEL=my-model\
ANTHROPIC_DEFAULT_HAIKU_MODEL=my-model\
claude
```

The environment variables:

Variable Description `ANTHROPIC_BASE_URL` Points to your vLLM server (default port is 8000) `ANTHROPIC_API_KEY` Can be any value since vLLM doesn't require authentication by default `ANTHROPIC_AUTH_TOKEN` Is required. Can be any value. `ANTHROPIC_DEFAULT_OPUS_MODEL` Model name for Opus-tier requests `ANTHROPIC_DEFAULT_SONNET_MODEL` Model name for Sonnet-tier requests `ANTHROPIC_DEFAULT_HAIKU_MODEL` Model name for Haiku-tier requests

Tip

You can add these environment variables to your shell profile (e.g., `.bashrc`, `.zshrc`), Claude Code configuration file (`~/.claude/settings.json`), or create a wrapper script for convenience.

Warning

Claude Code recently started injecting a per-request hash in the system prompt, which can defeat [prefix caching](https://docs.vllm.ai/en/latest/design/prefix_caching/) because the prompt changes on every request, causing greatly reduced performance. This is addressed automatically in vLLM versions &gt; 0.17.1 but for older versions `"CLAUDE_CODE_ATTRIBUTION_HEADER": "0"` should be added to the `"env"` section of `~/.claude/settings.json` (see this [blog post](https://unsloth.ai/docs/basics/claude-code#fixing-90-slower-inference-in-claude-code) from Unsloth).

## Testing the Setup[¶](#testing-the-setup "Permanent link")

Once Claude Code launches, try a simple prompt to verify the connection:

[![Claude Code example chat](https://docs.vllm.ai/en/latest/assets/deployment/claude-code-example.png)](https://docs.vllm.ai/en/latest/assets/deployment/claude-code-example.png)

If the model responds correctly, your setup is working. You can now use Claude Code with your vLLM-served model for coding tasks.

## Troubleshooting[¶](#troubleshooting "Permanent link")

**Connection refused**: Ensure vLLM is running and accessible at the specified URL. Check that the port matches.

**Tool calls not working**: Verify that your model supports tool calling and that you've enabled it with the correct `--tool-call-parser` flag. See [Tool Calling](https://docs.vllm.ai/en/latest/features/tool_calling/).

**Model not found**: Ensure the `--served-model-name` matches the model names in your environment variables. You cannot use model names with `/` in them, such as `openai/gpt-oss-120b` directly from Huggingface, so beware of that limitation with Claude Code.