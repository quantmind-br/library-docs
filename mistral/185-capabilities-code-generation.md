---
title: Coding | Mistral Docs
url: https://docs.mistral.ai/capabilities/code_generation
source: crawler
fetched_at: 2026-01-29T07:33:12.51536417-03:00
rendered_js: false
word_count: 648
summary: This document provides instructions and configuration details for integrating the Codestral model with several third-party development tools, IDE extensions, and AI frameworks.
tags:
    - codestral
    - mistral-ai
    - ide-integration
    - ai-coding-assistant
    - developer-tools
    - api-configuration
category: guide
---

**Integration with continue.dev**

Continue.dev supports both Codestral base for code generation and Codestral Instruct for chat.

#### How to set up Codestral with Continue

**Here is a step-by-step guide on how to set up Codestral with Continue using the Mistral AI API:**

1. Install the Continue VS Code or JetBrains extension following the instructions [here](https://docs.continue.dev/quickstart). Please make sure you install Continue version &gt;v0.8.33.
2. Automatic set up:

<!--THE END-->

- Click on the Continue extension iron on the left menu. Select `Mistral API` as a provider, select `Codestral` as a model.
- Click "Get API Key" to get Codestral API key.
- Click "Add model", which will automatically populate the config.json.

<!--THE END-->

![drawing](https://docs.mistral.ai/img/guides/codestral1.png)

2. (alternative) Manually edit config.json

<!--THE END-->

- Click on the gear icon in the bottom right corner of the Continue window to open `~/.continue/config.json` (MacOS) / `%userprofile%\.continue\config.json` (Windows)
- Log in and request a Codestral API key on Mistral AI's La Plateforme [here](https://console.mistral.ai/codestral)
- To use Codestral as your model for both `autocomplete` and `chat`, replace `[API_KEY]` with your Mistral API key below and add it to your `config.json` file:

If you run into any issues or have any questions, please join our Discord and post in `#help` channel [here](https://discord.gg/EfJEfdFnDQ)

**Integration with Tabnine**

Tabnine supports Codestral Instruct for chat.

#### How to set up Codestral with Tabnine

##### What is Tabnine Chat?

Tabnine Chat is a code-centric chat application that runs in the IDE and allows developers to interact with Tabnine’s AI models in a flexible, free-form way, using natural language. Tabnine Chat also supports dedicated quick actions that use predefined prompts optimized for specific use cases.

##### Getting started

To start using Tabnine Chat, first [launch](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/launch) it in your IDE (VSCode, JetBrains, or Eclipse). Then, learn how to [interact](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/interact) with Tabnine Chat, for example, how to ask questions or give instructions. Once you receive your response, you can [read, review, and apply](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/consume) it within your code.

##### Selecting Codestral as Tabnine Chat App model

In the Tabnine Chat App, use the [model selector](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/switching-between-chat-ai-models) to choose *Codestral*.

**Integration with LangChain**

LangChain provides support for Codestral Instruct. Here is how you can use it in LangChain:

For a more complex use case of self-corrective code generation using the instruct Codestral tool use, check out this [notebook](https://github.com/mistralai/cookbook/blob/main/third_party/langchain/langgraph_code_assistant_mistral.ipynb) and this video:

**Integration with LlamaIndex**

LlamaIndex provides support for Codestral Instruct and Fill In Middle (FIM) endpoints. Here is how you can use it in LlamaIndex:

Check out more details on using Instruct and Fill In Middle(FIM) with LlamaIndex in this [notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/codestral.ipynb).

**Integration with Jupyter AI**

Jupyter AI seamlessly integrates Codestral into JupyterLab, offering users a streamlined and enhanced AI-assisted coding experience within the Jupyter ecosystem. This integration boosts productivity and optimizes users' overall interaction with Jupyter.

To get started using Codestral and Jupyter AI in JupyterLab, first install needed packages in your Python environment:

Then launch Jupyter Lab:

Afterwards, you can select Codestral as your model of choice, input your Mistral API key, and start coding with Codestral!

**Integration with JupyterLite**

JupyterLite is a project that aims to bring the JupyterLab environment to the web browser, allowing users to run Jupyter directly in their browser without the need for a local installation.

You can try Codestral with JupyterLite in your browser: [![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyterlite.github.io/ai/lab/index.html)

**Integration with Tabby**

Tabby is an open-source AI coding assistant. You can use Codestral for both code completion and chat via Tabby.

To use Codestral in Tabby, configure your model configuration in `~/.tabby/config.toml` as follows.

You can check out [Tabby's documentation](https://tabby.tabbyml.com/docs/administration/model/#mistral--codestral) to learn more.

**Integration with E2B**

E2B provides open-source secure sandboxes for AI-generated code execution. With E2B, it is easy for developers to add code interpreting capabilities to AI apps using Codestral.

In the following examples, the AI agent performs a data analysis task on an uploaded CSV file, executes the AI-generated code by Codestral in the sandboxed environment by E2B, and returns a chart, saving it as a PNG file.

Python implementation ([cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-python)):

JS implementation ([cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/E2B_Code_Interpreting/codestral-code-interpreter-js)):