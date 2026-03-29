---
title: Environment Variables | goose
url: https://block.github.io/goose/docs/guides/environment-variables
source: github_pages
fetched_at: 2026-01-22T22:13:49.003573938-03:00
rendered_js: true
word_count: 1585
summary: This document provides a comprehensive reference for environment variables used to configure goose, including model providers, lead-worker patterns, and session management settings.
tags:
    - environment-variables
    - configuration
    - goose
    - llm-providers
    - session-management
    - retry-logic
category: reference
---

goose supports various environment variables that allow you to customize its behavior. This guide provides a comprehensive list of available environment variables grouped by their functionality.

## Model Configuration[​](#model-configuration "Direct link to Model Configuration")

These variables control the [language models](https://block.github.io/goose/docs/getting-started/providers) and their behavior.

### Basic Provider Configuration[​](#basic-provider-configuration "Direct link to Basic Provider Configuration")

These are the minimum required variables to get started with goose.

VariablePurposeValuesDefault`GOOSE_PROVIDER`Specifies the LLM provider to use[See available providers](https://block.github.io/goose/docs/getting-started/providers#available-providers)None (must be [configured](https://block.github.io/goose/docs/getting-started/providers#configure-provider-and-model))`GOOSE_MODEL`Specifies which model to use from the providerModel name (e.g., "gpt-4", "claude-sonnet-4-20250514")None (must be [configured](https://block.github.io/goose/docs/getting-started/providers#configure-provider-and-model))`GOOSE_TEMPERATURE`Sets the [temperature](https://medium.com/@kelseyywang/a-comprehensive-guide-to-llm-temperature-%EF%B8%8F-363a40bbc91f) for model responsesFloat between 0.0 and 1.0Model-specific default`GOOSE_MAX_TOKENS`Sets the maximum number of tokens for each model response (truncates longer responses)Positive integer (e.g., 4096, 8192)Model-specific default

**Examples**

```
# Basic model configuration
export GOOSE_PROVIDER="anthropic"
export GOOSE_MODEL="claude-sonnet-4-5-20250929"
export GOOSE_TEMPERATURE=0.7

# Set a lower limit for shorter interactions
export GOOSE_MAX_TOKENS=4096

# Set a higher limit for tasks requiring longer output (e.g. code generation)
export GOOSE_MAX_TOKENS=16000
```

### Advanced Provider Configuration[​](#advanced-provider-configuration "Direct link to Advanced Provider Configuration")

These variables are needed when using custom endpoints, enterprise deployments, or specific provider implementations.

VariablePurposeValuesDefault`GOOSE_PROVIDER__TYPE`The specific type/implementation of the provider[See available providers](https://block.github.io/goose/docs/getting-started/providers#available-providers)Derived from GOOSE\_PROVIDER`GOOSE_PROVIDER__HOST`Custom API endpoint for the providerURL (e.g., "[https://api.openai.com](https://api.openai.com)")Provider-specific default`GOOSE_PROVIDER__API_KEY`Authentication key for the providerAPI key stringNone

**Examples**

```
# Advanced provider configuration
export GOOSE_PROVIDER__TYPE="anthropic"
export GOOSE_PROVIDER__HOST="https://api.anthropic.com"
export GOOSE_PROVIDER__API_KEY="your-api-key-here"
```

### Lead/Worker Model Configuration[​](#leadworker-model-configuration "Direct link to Lead/Worker Model Configuration")

These variables configure a [lead/worker model pattern](https://block.github.io/goose/docs/tutorials/lead-worker) where a powerful lead model handles initial planning and complex reasoning, then switches to a faster/cheaper worker model for execution. The switch happens automatically based on your settings.

VariablePurposeValuesDefault`GOOSE_LEAD_MODEL`**Required to enable lead mode.** Name of the lead modelModel name (e.g., "gpt-4o", "claude-sonnet-4-20250514")None`GOOSE_LEAD_PROVIDER`Provider for the lead model[See available providers](https://block.github.io/goose/docs/getting-started/providers#available-providers)Falls back to `GOOSE_PROVIDER``GOOSE_LEAD_TURNS`Number of initial turns using the lead model before switching to the worker modelInteger3`GOOSE_LEAD_FAILURE_THRESHOLD`Consecutive failures before fallback to the lead modelInteger2`GOOSE_LEAD_FALLBACK_TURNS`Number of turns to use the lead model in fallback modeInteger2

A *turn* is one complete prompt-response interaction. Here's how it works with the default settings:

- Use the lead model for the first 3 turns
- Use the worker model starting on the 4th turn
- Fallback to the lead model if the worker model struggles for 2 consecutive turns
- Use the lead model for 2 turns and then switch back to the worker model

The lead model and worker model names are displayed at the start of the goose CLI session. If you don't export a `GOOSE_MODEL` for your session, the worker model defaults to the `GOOSE_MODEL` in your [configuration file](https://block.github.io/goose/docs/guides/config-files).

**Examples**

```
# Basic lead/worker setup
export GOOSE_LEAD_MODEL="o4"

# Advanced lead/worker configuration
export GOOSE_LEAD_MODEL="claude4-opus"
export GOOSE_LEAD_PROVIDER="anthropic"
export GOOSE_LEAD_TURNS=5
export GOOSE_LEAD_FAILURE_THRESHOLD=3
export GOOSE_LEAD_FALLBACK_TURNS=2
```

### Planning Mode Configuration[​](#planning-mode-configuration "Direct link to Planning Mode Configuration")

These variables control goose's [planning functionality](https://block.github.io/goose/docs/guides/creating-plans).

VariablePurposeValuesDefault`GOOSE_PLANNER_PROVIDER`Specifies which provider to use for planning mode[See available providers](https://block.github.io/goose/docs/getting-started/providers#available-providers)Falls back to GOOSE\_PROVIDER`GOOSE_PLANNER_MODEL`Specifies which model to use for planning modeModel name (e.g., "gpt-4", "claude-sonnet-4-20250514")Falls back to GOOSE\_MODEL

**Examples**

```
# Planning mode with different model
export GOOSE_PLANNER_PROVIDER="openai"
export GOOSE_PLANNER_MODEL="gpt-4"
```

### Provider Retries[​](#provider-retries "Direct link to Provider Retries")

Configurable retry parameters for LLM providers.

#### AWS Bedrock[​](#aws-bedrock "Direct link to AWS Bedrock")

VariablePurposeDefault`BEDROCK_MAX_RETRIES`The max number of retry attempts before giving up6`BEDROCK_INITIAL_RETRY_INTERVAL_MS`How long to wait (in milliseconds) before the first retry2000`BEDROCK_BACKOFF_MULTIPLIER`The factor by which the retry interval increases after each attempt2 (doubles every time)`BEDROCK_MAX_RETRY_INTERVAL_MS`The cap on the retry interval in milliseconds120000

**Examples**

```
export BEDROCK_MAX_RETRIES=10                    # 10 retry attempts
export BEDROCK_INITIAL_RETRY_INTERVAL_MS=1000    # start with 1 second before first retry
export BEDROCK_BACKOFF_MULTIPLIER=3              # each retry waits 3x longer than the previous
export BEDROCK_MAX_RETRY_INTERVAL_MS=300000      # cap the maximum retry delay at 5 min
```

#### Databricks[​](#databricks "Direct link to Databricks")

VariablePurposeDefault`DATABRICKS_MAX_RETRIES`The max number of retry attempts before giving up3`DATABRICKS_INITIAL_RETRY_INTERVAL_MS`How long to wait (in milliseconds) before the first retry1000`DATABRICKS_BACKOFF_MULTIPLIER`The factor by which the retry interval increases after each attempt2 (doubles every time)`DATABRICKS_MAX_RETRY_INTERVAL_MS`The cap on the retry interval in milliseconds30000

**Examples**

```
export DATABRICKS_MAX_RETRIES=5                      # 5 retry attempts
export DATABRICKS_INITIAL_RETRY_INTERVAL_MS=500      # start with 0.5 second before first retry
export DATABRICKS_BACKOFF_MULTIPLIER=2               # each retry waits 2x longer than the previous
export DATABRICKS_MAX_RETRY_INTERVAL_MS=60000        # cap the maximum retry delay at 1 min
```

## Session Management[​](#session-management "Direct link to Session Management")

These variables control how goose manages conversation sessions and context.

VariablePurposeValuesDefault`GOOSE_CONTEXT_STRATEGY`Controls how goose handles context limit exceeded situations"summarize", "truncate", "clear", "prompt""prompt" (interactive), "summarize" (headless)`GOOSE_MAX_TURNS`[Maximum number of turns](https://block.github.io/goose/docs/guides/sessions/smart-context-management#maximum-turns) allowed without user inputInteger (e.g., 10, 50, 100)1000`GOOSE_SUBAGENT_MAX_TURNS`Sets the maximum turns allowed for a [subagent](https://block.github.io/goose/docs/guides/subagents) to complete before timeoutInteger (e.g., 25)25`CONTEXT_FILE_NAMES`Specifies custom filenames for [hint/context files](https://block.github.io/goose/docs/guides/context-engineering/using-goosehints#custom-context-files)JSON array of strings (e.g., `["CLAUDE.md", ".goosehints"]`)`[".goosehints"]``GOOSE_CLI_THEME`[Theme](https://block.github.io/goose/docs/guides/goose-cli-commands#themes) for CLI response markdown"light", "dark", "ansi""dark"`GOOSE_RANDOM_THINKING_MESSAGES`Controls whether to show amusing random messages during processing"true", "false""true"`GOOSE_CLI_SHOW_COST`Toggles display of model cost estimates in CLI output"true", "1" (case insensitive) to enablefalse`GOOSE_AUTO_COMPACT_THRESHOLD`Set the percentage threshold at which goose [automatically summarizes your session](https://block.github.io/goose/docs/guides/sessions/smart-context-management#automatic-compaction).Float between 0.0 and 1.0 (disabled at 0.0)0.8

**Examples**

```
# Automatically summarize when context limit is reached
export GOOSE_CONTEXT_STRATEGY=summarize

# Always prompt user to choose (default for interactive mode)
export GOOSE_CONTEXT_STRATEGY=prompt

# Set a low limit for step-by-step control
export GOOSE_MAX_TURNS=5

# Set a moderate limit for controlled automation
export GOOSE_MAX_TURNS=25

# Set a reasonable limit for production
export GOOSE_MAX_TURNS=100

# Customize subagent turn limit
export GOOSE_SUBAGENT_MAX_TURNS=50

# Use multiple context files
export CONTEXT_FILE_NAMES='["CLAUDE.md", ".goosehints", ".cursorrules", "project_rules.txt"]'

# Set the ANSI theme for the session
export GOOSE_CLI_THEME=ansi

# Disable random thinking messages for less distraction
export GOOSE_RANDOM_THINKING_MESSAGES=false

# Enable model cost display in CLI
export GOOSE_CLI_SHOW_COST=true

# Automatically compact sessions when 60% of available tokens are used
export GOOSE_AUTO_COMPACT_THRESHOLD=0.6
```

### Model Context Limit Overrides[​](#model-context-limit-overrides "Direct link to Model Context Limit Overrides")

These variables allow you to override the default context window size (token limit) for your models. This is particularly useful when using [LiteLLM proxies](https://docs.litellm.ai/docs/providers/litellm_proxy) or custom models that don't match goose's predefined model patterns.

VariablePurposeValuesDefault`GOOSE_CONTEXT_LIMIT`Override context limit for the main modelInteger (number of tokens)Model-specific default or 128,000`GOOSE_LEAD_CONTEXT_LIMIT`Override context limit for the lead model in [lead/worker mode](https://block.github.io/goose/docs/tutorials/lead-worker)Integer (number of tokens)Falls back to `GOOSE_CONTEXT_LIMIT` or model default`GOOSE_WORKER_CONTEXT_LIMIT`Override context limit for the worker model in lead/worker modeInteger (number of tokens)Falls back to `GOOSE_CONTEXT_LIMIT` or model default`GOOSE_PLANNER_CONTEXT_LIMIT`Override context limit for the [planner model](https://block.github.io/goose/docs/guides/creating-plans)Integer (number of tokens)Falls back to `GOOSE_CONTEXT_LIMIT` or model default

**Examples**

```
# Set context limit for main model (useful for LiteLLM proxies)
export GOOSE_CONTEXT_LIMIT=200000

# Set different context limits for lead/worker models
export GOOSE_LEAD_CONTEXT_LIMIT=500000   # Large context for planning
export GOOSE_WORKER_CONTEXT_LIMIT=128000 # Smaller context for execution

# Set context limit for planner
export GOOSE_PLANNER_CONTEXT_LIMIT=1000000
```

For more details and examples, see [Model Context Limit Overrides](https://block.github.io/goose/docs/guides/sessions/smart-context-management#model-context-limit-overrides).

These variables control how goose handles [tool execution](https://block.github.io/goose/docs/guides/goose-permissions) and [tool management](https://block.github.io/goose/docs/guides/managing-tools/).

VariablePurposeValuesDefault`GOOSE_MODE`Controls how goose handles tool execution"auto", "approve", "chat", "smart\_approve""smart\_approve"`GOOSE_TOOLSHIM`Enables/disables tool call interpretation"1", "true" (case insensitive) to enablefalse`GOOSE_TOOLSHIM_OLLAMA_MODEL`Specifies the model for [tool call interpretation](https://block.github.io/goose/docs/experimental/ollama)Model name (e.g. llama3.2, qwen2.5)System default`GOOSE_CLI_MIN_PRIORITY`Controls verbosity of [tool output](https://block.github.io/goose/docs/guides/managing-tools/adjust-tool-output)Float between 0.0 and 1.00.0`GOOSE_CLI_TOOL_PARAMS_TRUNCATION_MAX_LENGTH`Maximum length for tool parameter values before truncation in CLI output (not in debug mode)Integer40`GOOSE_DEBUG`Enables debug mode to show full tool parameters without truncation"1", "true" (case insensitive) to enablefalse`GOOSE_SEARCH_PATHS`Additional directories to search for executables when running extensionsJSON array of paths (e.g., `["/usr/local/bin", "~/custom/bin"]`)System PATH only

**Examples**

```
# Enable tool interpretation
export GOOSE_TOOLSHIM=true
export GOOSE_TOOLSHIM_OLLAMA_MODEL=llama3.2
export GOOSE_MODE="auto"
export GOOSE_CLI_MIN_PRIORITY=0.2  # Show only medium and high importance output
export GOOSE_CLI_TOOL_PARAMS_MAX_LENGTH=100  # Show up to 100 characters for tool parameters in CLI output

# Add custom tool directories for extensions
export GOOSE_SEARCH_PATHS='["/usr/local/bin", "~/custom/tools", "/opt/homebrew/bin"]'
```

These paths are prepended to the system PATH when extensions execute commands, ensuring your custom tools are found without modifying your global PATH.

### Enhanced Code Editing[​](#enhanced-code-editing "Direct link to Enhanced Code Editing")

These variables configure [AI-powered code editing](https://block.github.io/goose/docs/guides/enhanced-code-editing) for the Developer extension's `str_replace` tool. All three variables must be set and non-empty for the feature to activate.

VariablePurposeValuesDefault`GOOSE_EDITOR_API_KEY`API key for the code editing modelAPI key stringNone`GOOSE_EDITOR_HOST`API endpoint for the code editing modelURL (e.g., "[https://api.openai.com/v1](https://api.openai.com/v1)")None`GOOSE_EDITOR_MODEL`Model to use for code editingModel name (e.g., "gpt-4o", "claude-sonnet-4")None

**Examples**

This feature works with any OpenAI-compatible API endpoint, for example:

```
# OpenAI configuration
export GOOSE_EDITOR_API_KEY="sk-..."
export GOOSE_EDITOR_HOST="https://api.openai.com/v1"
export GOOSE_EDITOR_MODEL="gpt-4o"

# Anthropic configuration (via OpenAI-compatible proxy)
export GOOSE_EDITOR_API_KEY="sk-ant-..."
export GOOSE_EDITOR_HOST="https://api.anthropic.com/v1"
export GOOSE_EDITOR_MODEL="claude-sonnet-4-20250514"

# Local model configuration
export GOOSE_EDITOR_API_KEY="your-key"
export GOOSE_EDITOR_HOST="http://localhost:8000/v1"
export GOOSE_EDITOR_MODEL="your-model"
```

## Security Configuration[​](#security-configuration "Direct link to Security Configuration")

These variables control security related features.

VariablePurposeValuesDefault`GOOSE_ALLOWLIST`Controls which extensions can be loadedURL for [allowed extensions](https://block.github.io/goose/docs/guides/allowlist) listUnset`GOOSE_DISABLE_KEYRING`Disables the system keyring for secret storageSet to any value (e.g., "1", "true", "yes") to disable. The actual value doesn't matter, only whether the variable is set.Unset (keyring enabled)

tip

When the keyring is disabled, secrets are stored here:

- macOS/Linux: `~/.config/goose/secrets.yaml`
- Windows: `%APPDATA%\Block\goose\config\secrets.yaml`

## Network Configuration[​](#network-configuration "Direct link to Network Configuration")

These variables configure network proxy settings for goose.

### HTTP Proxy[​](#http-proxy "Direct link to HTTP Proxy")

goose supports standard HTTP proxy environment variables for users behind corporate firewalls or proxy servers.

VariablePurposeValuesDefault`HTTP_PROXY`Proxy URL for HTTP connectionsURL (e.g., `http://proxy.company.com:8080`)None`HTTPS_PROXY`Proxy URL for HTTPS connections (takes precedence over `HTTP_PROXY` when both are set)URL (e.g., `http://proxy.company.com:8080`)None`NO_PROXY`Hosts to bypass the proxyComma-separated list (e.g., `localhost,127.0.0.1,.internal.com`)None

**Examples**

```
# Configure proxy for all connections
export HTTPS_PROXY="http://proxy.company.com:8080"
export NO_PROXY="localhost,127.0.0.1,.internal,.local,10.0.0.0/8"

# Or with authentication
export HTTPS_PROXY="http://username:password@proxy.company.com:8080"
export NO_PROXY="localhost,127.0.0.1,.internal"
```

## Observability[​](#observability "Direct link to Observability")

Beyond goose's built-in [logging system](https://block.github.io/goose/docs/guides/logs), you can export telemetry to external observability platforms for advanced monitoring, performance analysis, and production insights.

### OpenTelemetry Protocol (OTLP)[​](#opentelemetry-protocol-otlp "Direct link to OpenTelemetry Protocol (OTLP)")

Configure goose to export traces and metrics to any OTLP-compatible observability platform. OTLP is the standard protocol for sending telemetry collected by [OpenTelemetry](https://opentelemetry.io/docs/). When configured, goose exports telemetry asynchronously and flushes on exit.

VariablePurposeValuesDefault`OTEL_EXPORTER_OTLP_ENDPOINT`OTLP endpoint URLURL (e.g., `http://localhost:4318`)None`OTEL_EXPORTER_OTLP_TIMEOUT`Export timeout in millisecondsInteger (ms)`10000`

**When to use OTLP:**

- Diagnosing slow tool execution or LLM response times
- Understanding intermittent failures across multiple sessions
- Monitoring goose performance in production or CI/CD environments
- Tracking usage patterns, costs, and resource consumption over time
- Setting up alerts for performance degradation or high error rates

**Example:**

```
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"
export OTEL_EXPORTER_OTLP_TIMEOUT=10000
```

### Langfuse Integration[​](#langfuse-integration "Direct link to Langfuse Integration")

These variables configure the [Langfuse integration for observability](https://block.github.io/goose/docs/tutorials/langfuse).

VariablePurposeValuesDefault`LANGFUSE_PUBLIC_KEY`Public key for Langfuse integrationStringNone`LANGFUSE_SECRET_KEY`Secret key for Langfuse integrationStringNone`LANGFUSE_URL`Custom URL for Langfuse serviceURL StringDefault Langfuse URL`LANGFUSE_INIT_PROJECT_PUBLIC_KEY`Alternative public key for LangfuseStringNone`LANGFUSE_INIT_PROJECT_SECRET_KEY`Alternative secret key for LangfuseStringNone

## Recipe Configuration[​](#recipe-configuration "Direct link to Recipe Configuration")

These variables control recipe discovery and management.

VariablePurposeValuesDefault`GOOSE_RECIPE_PATH`Additional directories to search for recipesColon-separated paths on Unix, semicolon-separated on WindowsNone`GOOSE_RECIPE_GITHUB_REPO`GitHub repository to search for recipesFormat: "owner/repo" (e.g., "block/goose-recipes")None`GOOSE_RECIPE_RETRY_TIMEOUT_SECONDS`Global timeout for recipe success check commandsInteger (seconds)Recipe-specific default`GOOSE_RECIPE_ON_FAILURE_TIMEOUT_SECONDS`Global timeout for recipe on\_failure commandsInteger (seconds)Recipe-specific default

**Examples**

```
# Add custom recipe directories
export GOOSE_RECIPE_PATH="/path/to/my/recipes:/path/to/team/recipes"

# Configure GitHub recipe repository
export GOOSE_RECIPE_GITHUB_REPO="myorg/goose-recipes"

# Set global recipe timeouts
export GOOSE_RECIPE_RETRY_TIMEOUT_SECONDS=300
export GOOSE_RECIPE_ON_FAILURE_TIMEOUT_SECONDS=60
```

## Experimental Features[​](#experimental-features "Direct link to Experimental Features")

These variables enable experimental features that are in active development. These may change or be removed in future releases. Use with caution in production environments.

VariablePurposeValuesDefault`ALPHA_FEATURES`Enables experimental alpha features—check the feature docs to see if this flag is required"true", "1" (case insensitive) to enablefalse

**Examples**

```
# Enable alpha features
export ALPHA_FEATURES=true

# Or enable for a single session
ALPHA_FEATURES=true goose session
```

## Development & Testing[​](#development--testing "Direct link to Development & Testing")

These variables are primarily used for development, testing, and debugging goose itself.

VariablePurposeValuesDefault`GOOSE_PATH_ROOT`Override the root directory for all goose data, config, and state filesAbsolute path to directoryPlatform-specific defaults

**Default locations:**

- macOS: `~/Library/Application Support/Block/goose/`
- Linux: `~/.local/share/goose/`
- Windows: `%APPDATA%\Block\goose\`

When set, goose creates `config/`, `data/`, and `state/` subdirectories under the specified path. Useful for isolating test environments, running multiple configurations, or CI/CD pipelines.

**Examples**

```
# Temporary test environment
export GOOSE_PATH_ROOT="/tmp/goose-test"

# Isolated environment for a single command
GOOSE_PATH_ROOT="/tmp/goose-isolated" goose run --recipe my-recipe.yaml

# CI/CD usage
GOOSE_PATH_ROOT="$(mktemp -d)" goose run --recipe integration-test.yaml

# Use with developer tools
GOOSE_PATH_ROOT="/tmp/goose-test" ./scripts/goose-db-helper.sh status
```

## Variables Controlled by goose[​](#variables-controlled-by-goose "Direct link to Variables Controlled by goose")

These variables are automatically set by goose during command execution.

VariablePurposeValuesDefault`GOOSE_TERMINAL`Indicates that a command is being executed by goose, enables customizing shell behavior"1" when setUnset

### Customizing Shell Behavior[​](#customizing-shell-behavior "Direct link to Customizing Shell Behavior")

Sometimes you want goose to use different commands or have different shell behavior than your normal terminal usage. For example, you might want goose to use a different tool, prevent goose from running `git commit`, or block long-running development servers that could hang the AI agent. This is most useful when using goose CLI, where shell commands are executed directly in your terminal environment.

**How it works:**

1. When goose runs commands, `GOOSE_TERMINAL` is automatically set to "1"
2. Your shell configuration can detect this and change behavior while keeping your normal terminal usage unchanged

**Examples:**

```
# In ~/.zshenv (for zsh users) or ~/.bashrc (for bash users)

# Block git commit when run by goose
if [[ -n "$GOOSE_TERMINAL" ]]; then
  git() {
    if [[ "$1" == "commit" ]]; then
      echo "❌ BLOCKED: git commit is not allowed when run by goose"
      return 1
    fi
    command git "$@"
  }
fi
```

```
# Guide goose toward better tool choices
if [[ -n "$GOOSE_TERMINAL" ]]; then
  alias find="echo 'Use rg instead: rg --files | rg <pattern> for filenames, or rg <pattern> for content search'"
fi
```

## Enterprise Environments[​](#enterprise-environments "Direct link to Enterprise Environments")

When deploying goose in enterprise environments, administrators might need to control behavior and infrastructure, or enforce consistent settings across teams. The following environment variables are commonly used:

**Network and Infrastructure** - Control how goose connects to external services and internal infrastructure:

- [Network Configuration](#network-configuration) - Proxy configuration and network settings
- [Advanced Provider Configuration](#advanced-provider-configuration) - Point to internal LLM endpoints (e.g., Databricks, custom deployments)
- [Model Context Limit Overrides](#model-context-limit-overrides) - Configure context limits for LiteLLM proxies and custom models

**Security and Access Control** - Manage which extensions can run and how secrets are stored:

- [Security Configuration](#security-configuration) - Control extension loading (`GOOSE_ALLOWLIST`) and secrets management (`GOOSE_DISABLE_KEYRING`)

**Compliance and Monitoring** - Track usage and export telemetry for auditing:

- [Observability](#observability) - Export telemetry to monitoring platforms (OTLP, Langfuse)

## Notes[​](#notes "Direct link to Notes")

- Environment variables take precedence over configuration files.
- For security-sensitive variables (like API keys), consider using the system keyring instead of environment variables.
- Some variables may require restarting goose to take effect.
- When using the planning mode, if planner-specific variables are not set, goose will fall back to the main model configuration.