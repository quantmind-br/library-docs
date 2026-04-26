---
title: Installation | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/installation
source: sitemap
fetched_at: 2026-04-26T04:14:09.091942294-03:00
rendered_js: false
word_count: 103
summary: This guide provides instructions for installing the Workflows SDK using Python and uv, along with steps for verifying the installation and setting up the Mistral plugin.
tags:
    - workflows-sdk
    - python-installation
    - mistral-integration
    - environment-setup
    - package-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Guide to set up Workflows and verify your installation.

## Prerequisites

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Install Workflows

```bash
uv pip install mistral-workflows
```

This creates a virtual environment (if one doesn't exist) and installs Workflows along with its core dependencies.

## Install Mistral Plugin

The Mistral plugin provides native integration with Mistral's AI models and services, including durable agents, tool calling, and multi-agent handoffs:

```bash
uv pip install mistral-workflows[mistral]
```

## Verify Installation

```bash
mistral-workflows --version
```

> [!warning]
> If you encounter errors, check that your Python environment is properly configured.

#workflows-sdk #python-installation #mistral-integration