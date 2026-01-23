---
title: Smart Context Management | goose
url: https://block.github.io/goose/docs/guides/sessions/smart-context-management
source: github_pages
fetched_at: 2026-01-22T22:14:29.499655086-03:00
rendered_js: true
word_count: 1279
summary: This document explains how goose manages LLM context windows and conversation history through automatic compaction, manual strategies, and turn limits. It provides instructions for configuring these limits to maintain long-running sessions and prevent resource exhaustion.
tags:
    - context-management
    - llm-tokens
    - auto-compaction
    - session-limits
    - goose-configuration
    - conversation-history
category: guide
---

When working with [Large Language Models (LLMs)](https://block.github.io/goose/docs/getting-started/providers), there are limits to how much conversation history they can process at once. goose provides smart context management features to help handle context and conversation limits so you can maintain productive sessions. Here are some key concepts:

- **Context Length**: The amount of conversation history the LLM can consider, also referred to as the context window
- **Context Limit**: The maximum number of tokens the model can process
- **Context Management**: How goose handles conversations approaching these limits
- **Turn**: One complete prompt-response interaction between goose and the LLM

## How goose Manages Context[​](#how-goose-manages-context "Direct link to How goose Manages Context")

goose uses a two-tiered approach to context management:

1. **Auto-Compaction**: Proactively summarizes conversation when approaching token limits
2. **Context Strategies**: Backup strategy used if the context limit is still exceeded after auto-compaction

This layered approach lets goose handle token and context limits gracefully.

## Automatic Compaction[​](#automatic-compaction "Direct link to Automatic Compaction")

goose automatically compacts (summarizes) older parts of your conversation when approaching token limits, allowing you to maintain long-running sessions without manual intervention. Auto-compaction is triggered by default when you reach 80% of the token limit in goose Desktop and the goose CLI.

Control the auto-compaction behavior with the `GOOSE_AUTO_COMPACT_THRESHOLD` [environment variable](https://block.github.io/goose/docs/guides/environment-variables#session-management). Disable this feature by setting the value to `0.0`.

```
# Automatically compact sessions when 60% of available tokens are used
export GOOSE_AUTO_COMPACT_THRESHOLD=0.6
```

When you reach the auto-compaction threshold:

1. goose will automatically start compacting the conversation to make room.
2. Once complete, you'll see a confirmation message that the conversation was compacted and summarized.
3. Continue the session. Your previous conversation remains visible, but only the compacted conversion is included in the active context for goose.

### Manual Compaction[​](#manual-compaction "Direct link to Manual Compaction")

You can also trigger compaction manually before reaching context or token limits:

- goose Desktop
- goose CLI

<!--THE END-->

1. Point to the token usage indicator dot next to the model name at the bottom of the app
2. Click `Compact now` in the context window that appears
3. Once complete, you'll see a confirmation message that the conversation was compacted and summarized.
4. Continue the session. Your previous conversation remains visible, but only the compacted conversion is included in the active context for goose.

info

You must send at least one message in the chat before the `Compact now` button is enabled.

## Context Limit Strategies[​](#context-limit-strategies "Direct link to Context Limit Strategies")

When auto-compaction is disabled, or if a conversation still exceeds the context limit, goose offers different ways to handle it:

FeatureDescriptionBest ForAvailabilityImpact**Summarization**Condenses conversation while preserving key pointsLong, complex conversationsDesktop and CLIMaintains most context**Truncation**Removes oldest messages to make roomSimple, linear conversationsCLI onlyLoses old context**Clear**Starts fresh while keeping session activeNew direction in conversationCLI onlyLoses all context**Prompt**Asks user to choose from the above optionsControl over each decision in interactive sessionsCLI onlyDepends on choice made

- goose Desktop
- goose CLI

goose Desktop exclusively uses summarization by compacting the conversation to manage context, preserving key information while reducing size.

## Maximum Turns[​](#maximum-turns "Direct link to Maximum Turns")

The `Max Turns` limit is the maximum number of consecutive turns that goose can take without user input (default: 1000). When the limit is reached, goose stops and prompts: "I've reached the maximum number of actions I can do without user input. Would you like me to continue?" If the user answers in the affirmative, goose continues until the limit is reached and then prompts again.

This feature gives you control over agent autonomy and prevents infinite loops and runaway behavior, which could have significant cost consequences or damaging impact in production environments. Use it for:

- Preventing infinite loops and excessive API calls or resource consumption in automated tasks
- Enabling human supervision or interaction during autonomous operations
- Controlling loops while testing and debugging agent behavior

This setting is stored as the `GOOSE_MAX_TURNS` environment variable in your [config.yaml file](https://block.github.io/goose/docs/guides/config-files). You can configure it using the Desktop app or CLI.

- goose Desktop
- goose CLI

<!--THE END-->

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `Chat` tab
4. Scroll to `Conversation Limits` and enter a value for `Max Turns`

**Choosing the Right Value**

The appropriate max turns value depends on your use case and comfort level with automation:

- **5-10 turns**: Good for exploratory tasks, debugging, or when you want frequent check-ins. For example, "analyze this codebase and suggest improvements" where you want to review each step
- **25-50 turns**: Effective for well-defined tasks with moderate complexity, such as "refactor this module to use the new API" or "set up a basic CI/CD pipeline"
- **100+ turns**: More suitable for complex, multi-step automation where you trust goose to work independently, like "migrate this entire project from React 16 to React 18" or "implement comprehensive test coverage for this service"

Remember that even simple-seeming tasks often require multiple turns. For example, asking goose to "fix the failing tests" might involve analyzing test output (1 turn), identifying the root cause (1 turn), making code changes (1 turn), and verifying the fix (1 turn).

## Token Usage[​](#token-usage "Direct link to Token Usage")

After sending your first message, goose Desktop and goose CLI display token usage.

- goose Desktop
- goose CLI

The Desktop displays a colored circle next to the model name at the bottom of the session window. The color provides a visual indicator of your token usage for the session.

- **Green**: Normal usage - Plenty of context space available
- **Orange**: Warning state - Approaching limit (80% of capacity)
- **Red**: Error state - Context limit reached

Hover over this circle to display:

- The number of tokens used
- The percentage of available tokens used
- The total available tokens
- A progress bar showing your current token usage

## Model Context Limit Overrides[​](#model-context-limit-overrides "Direct link to Model Context Limit Overrides")

Context limits are automatically detected based on your model name, but goose provides settings to override the default limits:

ModelDescriptionBest ForSetting**Main**Set context limit for the main model (also serves as fallback for other models)LiteLLM proxies, custom models with non-standard names`GOOSE_CONTEXT_LIMIT`**Lead**Set larger context for planning in [lead/worker mode](https://block.github.io/goose/docs/tutorials/lead-worker)Complex planning tasks requiring more context`GOOSE_LEAD_CONTEXT_LIMIT`**Worker**Set smaller context for execution in lead/worker modeCost optimization during execution phase`GOOSE_WORKER_CONTEXT_LIMIT`**Planner**Set context for [planner models](https://block.github.io/goose/docs/guides/creating-plans)Large planning tasks requiring extensive context`GOOSE_PLANNER_CONTEXT_LIMIT`

info

This setting only affects the displayed token usage and progress indicators. Actual context management is handled by your LLM, so you may experience more or less usage than the limit you set, regardless of what the display shows.

This feature is particularly useful with:

- **LiteLLM Proxy Models**: When using LiteLLM with custom model names that don't match goose's patterns
- **Enterprise Deployments**: Custom model deployments with non-standard naming
- **Fine-tuned Models**: Custom models with different context limits than their base versions
- **Development/Testing**: Temporarily adjusting context limits for testing purposes

goose resolves context limits with the following precedence (highest to lowest):

1. Explicit context\_limit in model configuration (if set programmatically)
2. Specific environment variable (e.g., `GOOSE_LEAD_CONTEXT_LIMIT`)
3. Global environment variable (`GOOSE_CONTEXT_LIMIT`)
4. Model-specific default based on name pattern matching
5. Global default (128,000 tokens)

**Configuration**

- goose Desktop
- goose CLI

Model context limit overrides are not yet available in the goose Desktop app.

**Scenarios**

1. LiteLLM proxy with custom model name

```
# LiteLLM proxy with custom model name
export GOOSE_PROVIDER="openai"
export GOOSE_MODEL="my-custom-gpt4-proxy"
export GOOSE_CONTEXT_LIMIT=200000  # Override the 32k default
```

2. Lead/worker setup with different context limits

```
# Different context limits for planning vs execution
export GOOSE_LEAD_MODEL="claude-opus-custom"
export GOOSE_LEAD_CONTEXT_LIMIT=500000    # Large context for planning
export GOOSE_WORKER_CONTEXT_LIMIT=128000  # Smaller context for execution
```

3. Planner with large context

```
# Large context for complex planning
export GOOSE_PLANNER_MODEL="gpt-4-custom"
export GOOSE_PLANNER_CONTEXT_LIMIT=1000000
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

Display real-time estimated costs of your session.

- goose Desktop
- goose CLI

To manage live cost tracking:

1. Click the button in the top-left to open the sidebar
2. Click the `Settings` button on the sidebar
3. Click the `App` tab
4. Toggle `Cost Tracking` on/off

The session cost is shown at the bottom of the goose window and updates dynamically as tokens are consumed. Hover over the cost to see a detailed breakdown of token usage. If multiple models are used in the session, this includes a cost breakdown by model. Ollama and local deployments always show a cost of $0.00.

Pricing data is regularly fetched from the OpenRouter API and cached locally. The `Advanced settings` tab shows when the data was last updated and allows you to refresh.

These costs are estimates only, and not connected to your actual provider bill. The cost shown is an approximation based on token counts and public pricing data.