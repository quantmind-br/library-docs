---
title: Python SDK - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/python-sdk
source: sitemap
fetched_at: 2026-04-27T20:12:39.979009135-03:00
rendered_js: false
word_count: 108
summary: This document provides an overview of the official Python SDK for the Fireworks AI API, highlighting its advantages over the standard OpenAI SDK and outlining how to install and begin using it.
tags:
    - python-sdk
    - fireworks-ai
    - openai-compatibility
    - installation
    - api-client
    - concurrency
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
The official Python SDK for the Fireworks AI API is available on [GitHub](https://github.com/fw-ai-external/python-sdk) and [PyPI](https://pypi.org/project/fireworks-ai/).

## Fireworks vs. OpenAI SDK

Fireworks is [[093-tools-sdks-openai-compatibility|OpenAI-compatible]], so you can use the OpenAI SDK with Fireworks. The Fireworks SDK offers additional benefits:

- **Better concurrency defaults** — Optimized connection pooling for high-throughput workloads
- **Fireworks-exclusive features** — Access parameters and response fields not available in the OpenAI API
- **Platform automation** — Manage datasets, evals, fine-tuning, and deployments programmatically

## Installation

Requires Python 3.9+ and an API key. See [[001-api-reference-introduction|Getting your API key]] for instructions.

For detailed usage instructions, see the [README.md](https://github.com/fw-ai-external/python-sdk#readme). To quickly get started with serverless, see our [[009-getting-started-quickstart|Serverless Quickstart]].
