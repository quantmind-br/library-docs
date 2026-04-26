---
title: Coding | Mistral Docs
url: https://docs.mistral.ai/mistral-vibe/using-fim-api
source: sitemap
fetched_at: 2026-04-26T04:08:37.203930465-03:00
rendered_js: false
word_count: 645
summary: Instructions for integrating Codestral AI models into development tools, IDE extensions, and frameworks including Continue, Tabnine, LangChain, and Jupyter.
tags:
    - codestral
    - ide-integration
    - ai-development
    - model-configuration
    - coding-assistant
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Coding

Integrate Codestral into your development workflow through various IDEs and frameworks.

## Continue.dev

Continue.dev supports Codestral base for code generation and Codestral Instruct for chat.

### Setup Codestral with Continue

1. Install the Continue VS Code or JetBrains extension (version >v0.8.33) from [their docs](https://docs.continue.dev/quickstart).
2. **Automatic setup:**
   - Click the Continue extension icon, select `Mistral API` as provider and `Codestral` as model.
   - Click "Get API Key" to obtain a Codestral API key.
   - Click "Add model" to auto-populate `config.json`.
3. **Manual setup:**
   - Open `~/.continue/config.json` (MacOS) or `%userprofile%\.continue\config.json` (Windows).
   - Request a Codestral API key in [Studio›Codestral](https://console.mistral.ai/codestral).
   - Replace `[API_KEY]` with your Mistral API key in the config.

![Setup screenshot](https://docs.mistral.ai/img/guides/codestral1.png)

For issues, join the Discord `#help` channel [here](https://discord.gg/EfJEfdFnDQ).

## Tabnine

Tabnine supports Codestral Instruct for chat.

### Getting Started

1. [Launch](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/launch) Tabnine Chat in your IDE (VSCode, JetBrains, or Eclipse).
2. Learn how to [interact](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/interact) with Tabnine Chat.
3. Use the [model selector](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/switching-between-chat-ai-models) to choose *Codestral*.

## LangChain

LangChain provides support for Codestral Instruct. For self-corrective code generation examples, see:
- [Notebook](https://github.com/mistralai/cookbook/blob/main/third_party/langchain/langgraph_code_assistant_mistral.ipynb)
- [Video walkthrough](https://www.youtube.com/watch?v=example)

## LlamaIndex

LlamaIndex supports Codestral Instruct and Fill In Middle (FIM) endpoints. See the [notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/codestral.ipynb) for details.

## Jupyter AI

Jupyter AI integrates Codestral into JupyterLab for AI-assisted coding.

### Setup

```bash
pip install jupyterlab jupyter_ai codestral
jupyter lab
```

After launching, select Codestral as your model and enter your Mistral API key.

## JupyterLite

JupyterLite runs JupyterLab in the browser without local installation. Try Codestral with JupyterLite:

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyterlite.github.io/ai/lab/index.html)

## Tabby

Tabby is an open-source AI coding assistant supporting Codestral for code completion and chat.

Configure Codestral in `~/.tabby/config.toml`:

```toml
[model]
provider = "mistral"
model = "codestral"
api_key = "your-api-key"
```

See Tabby's [documentation](https://tabby.tabbyml.com/docs/administration/model/#mistral--codestral) for details.

## E2B

E2B provides secure sandboxes for AI-generated code execution. Codestral can execute code in E2B sandboxes for tasks like data analysis on CSV files.

- [Python cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-python)
- [JS cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-js)

#codestral #ide-integration #ai-development #model-configuration #coding-assistant
