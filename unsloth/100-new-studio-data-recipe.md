---
title: Unsloth Data Recipes
url: https://unsloth.ai/docs/new/studio/data-recipe.md
source: llms
fetched_at: 2026-04-27T18:13:25.844199548-03:00
rendered_js: false
word_count: 1377
summary: This guide introduces Unsloth Data Recipes, explaining how users can transform raw documents (like PDFs or CSVs) into usable datasets using a visual graph-node workflow powered by NVIDIA Nemo. It details the process from creation to full dataset building and outlines the core components available in the editor.
tags:
    - data-recipes
    - unsloth-studio
    - dataset-workflow
    - graph-node
    - nemo-powered
    - synthetic-data
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Data Recipes

Visual graph-node editor for transforming raw documents (PDFs, CSVs) into training datasets. Powered by **NVIDIA Nemo Data Designer** ([GitHub](https://github.com/NVIDIA-NeMo/DataDesigner)).

## Workflow Overview

1. Open the recipes page.
2. Create a new recipe or open an existing one.
3. Add blocks to define the dataset workflow.
4. Click **Validate** to catch configuration issues.
5. Run a preview to inspect sample rows.
6. Run a full dataset build when ready.
7. Review progress live in graph or **Executions** view.
8. Select the resulting dataset in [[097-new-studio|Studio]] and fine-tune a model.

## Getting Started

Recipes are stored locally in the browser. You can create blank recipes or guided learning recipes.

> [!info] Sharing recipes
> Recipes can be exported/imported. Ask in Unsloth Discord if you need a specific dataset pattern -- someone may already have one.

| Goal | Start with |
|---|---|
| Build a custom workflow quickly | Start Empty |
| Learn from an example | Start from Learning Recipe |
| Continue previous work | Open a saved recipe |

## Editor Components

- **Recipe header** -- rename recipe, switch between Editor and Executions views
- **Canvas** -- recipe graph display
- **Block sheet** -- add new blocks
- **Configuration dialogs** -- prompts, references, model aliases, validators, seed settings
- **Floating controls** -- Run and Validate buttons

### Common Blocks

- **Seed** -- input data from Hugging Face, local structured files, or unstructured documents (chunked into rows)
- **LLM + Models** -- providers, model configs, LLM generation blocks, shared tool profiles
- **Expression** -- Jinja2-based transforms (no LLM call required)
- **Validators** -- filter bad generated code via built-in linters (Python, SQL, JS/TS)
- **Samplers** -- deterministic columns (categories, subcategories)

## References

Most blocks that produce data become a reference for later blocks. Create once, reuse in prompts, expressions, structured outputs, and validation steps.

> [!info] Jinja expressions
> Reference nested fields: `{{customer.first_name}}`. Join values: `{{customer.first_name}} {{customer.last_name}}`. Conditionals: `{% if condition %}...{% endif %}`

Examples:
- Category block named `domain` referenced as `{{ domain }}`
- Seed columns (HF dataset columns, CSV) used directly in LLM prompts
- Structured LLM output exposes fields for later prompts
- Expression blocks combine earlier values without another model call

## Output

- **Preview runs** -- sample rows and analysis for quick iteration
- **Full runs** -- persisted local dataset artifact, appears in Studio's local dataset picker for fine-tuning
- Optionally publish datasets to Hugging Face

## Model Setup

Two-layer configuration:

- **Model provider** -- endpoint and authentication
- **Model config** -- model name and inference settings

Works with hosted providers, self-hosted endpoints, vLLM, llama.cpp, or any OpenAI-compatible API.

> [!info] Multi-model recipes
> Add multiple model providers and configs. Use different models for different steps (e.g., one for coding, another for general text).

### LLM Block Types

| Block | Output | Best for |
|---|---|---|
| LLM Text | Free-form text | Instructions, explanations, conversations, descriptions |
| LLM Structured | JSON | Fixed fields, predictable structure |
| LLM Code | Code | Python, SQL, TypeScript, other code generation |
| LLM Judge | Scored evaluation | Grading outputs with user-defined scores |

### Tool Profiles

Shared MCP-based tool access for one or more LLM blocks. Use when a generation step needs tools (e.g., looking up code documentation through Context7).

## Validators

Target LLM code blocks by running generated code through linters and syntax validation. Filters bad/invalid code rows from the final dataset. Built-in support: Python, SQL, JavaScript/TypeScript.

## Validate, Preview, Run

Recommended execution order:

1. **Validate** -- catch configuration issues
2. **Preview** -- inspect sample rows and analysis
3. **Refine** -- adjust prompts, references, seed settings, or validators; iterate until satisfied
4. **Run full dataset build**

#unsloth-studio #data-recipes #synthetic-data
