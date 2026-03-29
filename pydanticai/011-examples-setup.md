---
title: Setup - Pydantic AI
url: https://ai.pydantic.dev/examples/setup/
source: sitemap
fetched_at: 2026-01-22T22:25:46.208293633-03:00
rendered_js: false
word_count: 219
summary: This document provides instructions for installing dependencies, configuring environment variables, and running the provided example code for the Pydantic AI library.
tags:
    - pydantic-ai
    - example-usage
    - environment-setup
    - installation-guide
    - llm-configuration
    - python-development
category: guide
---

## Examples

Here we include some examples of how to use Pydantic AI and what it can do.

## Usage

These examples are distributed with `pydantic-ai` so you can run them either by cloning the [pydantic-ai repo](https://github.com/pydantic/pydantic-ai) or by simply installing `pydantic-ai` from PyPI with `pip` or `uv`.

### Installing required dependencies

Either way you'll need to install extra dependencies to run some examples, you just need to install the `examples` optional dependency group.

If you've installed `pydantic-ai` via pip/uv, you can install the extra dependencies with:

pipuv

```
pipinstall"pydantic-ai[examples]"
```

```
uvadd"pydantic-ai[examples]"
```

If you clone the repo, you should instead use `uv sync --extra examples` to install extra dependencies.

### Setting model environment variables

These examples will need you to set up authentication with one or more of the LLMs, see the [model configuration](https://ai.pydantic.dev/models/overview/) docs for details on how to do this.

TL;DR: in most cases you'll need to set one of the following environment variables:

OpenAIGoogle Gemini

```
exportOPENAI_API_KEY=your-api-key
```

```
exportGEMINI_API_KEY=your-api-key
```

### Running Examples

To run the examples (this will work whether you installed `pydantic_ai`, or cloned the repo), run:

pipuv

```
python-mpydantic_ai_examples.<example_module_name>
```

```
uvrun-mpydantic_ai_examples.<example_module_name>
```

For example, to run the very simple [`pydantic_model`](https://ai.pydantic.dev/examples/pydantic-model/) example:

pipuv

```
python-mpydantic_ai_examples.pydantic_model
```

```
uvrun-mpydantic_ai_examples.pydantic_model
```

If you like one-liners and you're using uv, you can run a pydantic-ai example with zero setup:

```
OPENAI_API_KEY='your-api-key'\
uvrun--with"pydantic-ai[examples]"\
-mpydantic_ai_examples.pydantic_model
```

* * *

You'll probably want to edit examples in addition to just running them. You can copy the examples to a new directory with:

pipuv

```
python-mpydantic_ai_examples--copy-toexamples/
```

```
uvrun-mpydantic_ai_examples--copy-toexamples/
```