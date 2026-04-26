---
title: Your First Workflow | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/getting-started/your_first_workflow
source: sitemap
fetched_at: 2026-04-26T04:14:13.149068465-03:00
rendered_js: false
word_count: 355
summary: This document provides a step-by-step guide for setting up, configuring, and executing a basic workflow using the Mistral Workflows SDK.
tags:
    - mistral-workflows
    - python-sdk
    - workflow-automation
    - getting-started
    - api-integration
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Walk through creating a simple workflow that executes a single activity.

## Prerequisites

1. [Mistral account](https://console.mistral.ai/)
2. [Python](https://www.python.org/downloads/) 3.12 installed
3. [uvx](https://github.com/astral-sh/uvx) installed

## Step 1: Scaffold Project

```bash
uvx mistral-workflows scaffold my-workflow
```

This scaffolds a ready-to-run Python project with:
- Workflows SDK configured
- Minimal example workflow
- Helper commands to run your worker and trigger executions

The command prompts you to [generate a Mistral API key in the Mistral Console](https://console.mistral.ai/home?profile_dialog=api-keys). Note: API keys are only accessible once.

## Step 2: Explore the Project

Open `my-workflow` in your IDE.

**`src/workflows/hello.py`** — example workflow:

```python
from mistral_workflows import workflow

@workflow
def hello(input: dict):
    return f"Hello, {input['name']}!"
```

This defines a workflow that takes a `name` as input and returns a greeting.

**`src/discover.py`** — auto-discovers workflows:

```python
from mistral_workflows import run_worker

run_worker([hello])
```

This auto-discovers all workflows in `src/workflows` and auto-watches them using `run_worker`.

## Step 3: Run the Worker

```bash
make run-worker
```

This starts the worker, connects to the Mistral API, and registers your workflow to wait for tasks.

## Step 4: Trigger Execution

Trigger via Mistral Console, Python SDK, or API. The `my-workflow` project also includes a `Makefile` command:

1. Go to [https://console.mistral.ai/](https://console.mistral.ai/) → navigate to your workspace.
2. Click **Workflows** in the sidebar.
3. Select **hello-world**.
4. Click **Start Workflow** → input `{"name": <your_name>}`.
5. Find your execution in the **Executions** tab.
6. Verify the output.

## Stop Worker

Press `Ctrl+C` to stop the worker.

## Next Steps

- Learn more about [Core Concepts - Workflows](https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/workflows)
- See [Core Concepts - Scaling with Multiple Workers](https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/deployments#scaling) for scaling patterns

#mistral-workflows #python-sdk #workflow-automation