---
title: Mixed Models - Factory Documentation
url: https://docs.factory.ai/cli/configuration/mixed-models
source: sitemap
fetched_at: 2026-01-13T19:03:57.694748627-03:00
rendered_js: false
word_count: 561
summary: This guide explains how to configure and manage mixed models in the Droid CLI, allowing users to assign separate AI models for Specification Mode planning and standard coding sessions.
tags:
    - ai-configuration
    - model-selection
    - specification-mode
    - cli-setup
    - reasoning-effort
category: configuration
---

## What are mixed models?

Mixed models allow you to use a different AI model specifically for Specification Mode planning while keeping a separate default model for regular coding sessions. This gives you the flexibility to optimize both planning and implementation phases independently. For example, you might want to use a more powerful model for comprehensive specification planning, while using a faster model for day-to-day implementation work.

* * *

## Why use mixed models?

Different models excel at different tasks. Separating your spec mode model from your default model lets you:

* * *

## How to configure mixed models

### Accessing the Configuration

1. Run `droid` to start the CLI
2. Enter `/model` to open the model selector
3. Navigate to **“Configure Spec Mode Model”** (first option in the list)
4. Press **Enter** to begin configuration

### Configuration Options

When you open the configurator, you’ll see three options:

- **Yes, configure spec mode model** - Select a different model for Specification Mode
- **No, keep using \[current configuration/main model]** - Exit without making changes
- **Clear spec mode model (use main model)** - Remove the spec mode model and use your default model for everything *(only shown if you already have a spec mode model configured)*

### Selecting a Model

1. Choose **“Yes, configure spec mode model”**
2. Browse the list of available models
3. Select your preferred model for Specification Mode
4. If the model supports reasoning, choose your reasoning effort level
5. The configuration is saved automatically

* * *

## Model Compatibility

Not all model combinations work together due to how different AI providers handle reasoning traces and context. Here are the compatibility rules:

### Compatibility Rules

* * *

## Reasoning Effort Configuration

If you select an Anthropic model that supports reasoning (like Sonnet 4.5), you’ll be prompted to choose a reasoning effort level:

- **Off** - No extended thinking, faster responses
- **Low** - Brief consideration, balanced speed and depth
- **Medium** - Moderate thinking time for complex decisions
- **High** - Deep analysis for critical architectural choices

The reasoning effort for your spec mode model is independent of your default model’s reasoning setting, giving you complete control over each phase.

* * *

## Common Configurations

Here are some effective model combinations for different scenarios:

### Anthropic Models

**Best for:** Most development workflows, flexible reasoning control

- **Default model:** Haiku 4.5 or Sonnet 4.5 (select reasoning of your choice if supported)
- **Spec mode model:** Sonnet 4.5 (reasoning: high)
- **Benefits:** Fast implementation with deep planning analysis

### OpenAI Models

**Best for:** Teams using OpenAI models exclusively, cost-conscious projects

- **Default model:** GPT-5-Codex
- **Spec mode model:** GPT-5 (high reasoning)
- **Benefits:** Consistent reasoning format, specialized coding model for specs

* * *

## How It Works

Once configured, Droid automatically uses your spec mode model whenever you enter Specification Mode:

1. **Activate Specification Mode** with **Shift+Tab**
2. **Provide your feature description**
3. **Droid uses your spec mode model** to analyze, plan, and generate the specification
4. **Review and approve** the generated spec
5. **Implementation uses your default model** to write the actual code

* * *

## Checking Your Configuration

To see which models you’re currently using:

1. Enter `/model` in the CLI
2. Your current default model is highlighted
3. If you have a spec mode model configured, it’s displayed at the top of the selector

* * *

## Clearing your mixed models configuration

If you want to go back to using a single model for everything:

1. Enter `/model` in the CLI
2. Navigate to **“Configure Spec Mode Model”**
3. Press **Enter**
4. Select **“Clear spec mode model (use main model)”**
5. Confirm by pressing **Enter**

Your default model will now be used for both regular coding and Specification Mode.

* * *

## Best Practices

* * *

## Troubleshooting

* * *

* * *