---
title: Configuration Files | goose
url: https://block.github.io/goose/docs/guides/config-files
source: github_pages
fetched_at: 2026-01-22T22:13:38.127123643-03:00
rendered_js: true
word_count: 539
summary: This document explains how to use YAML files to manage goose settings, including LLM providers, tool permissions, and extension configurations. It provides a complete reference for global settings, file locations, and configuration precedence across different operating systems.
tags:
    - goose-ai
    - yaml-configuration
    - llm-settings
    - extension-management
    - environment-variables
    - configuration-reference
category: configuration
---

goose uses YAML [configuration files](#configuration-files) to manage settings and extensions. The primary config file is located at:

- macOS/Linux: `~/.config/goose/config.yaml`
- Windows: `%APPDATA%\Block\goose\config\config.yaml`

The configuration files allow you to set default behaviors, configure language models, set tool permissions, and manage extensions. While many settings can also be set using [environment variables](https://block.github.io/goose/docs/guides/environment-variables), the config files provide a persistent way to maintain your preferences.

- **config.yaml** - Provider, model, extensions, and general settings
- **permission.yaml** - Tool permission levels configured via `goose configure`
- **secrets.yaml** - API keys and secrets (only when keyring is disabled)
- **permissions/tool\_permissions.json** - Runtime permission decisions (auto-managed)

## Global Settings[​](#global-settings "Direct link to Global Settings")

The following settings can be configured at the root level of your config.yaml file:

SettingPurposeValuesDefaultRequired`GOOSE_PROVIDER`Primary [LLM provider](https://block.github.io/goose/docs/getting-started/providers)"anthropic", "openai", etc.NoneYes`GOOSE_MODEL`Default model to useModel name (e.g., "claude-3.5-sonnet", "gpt-4")NoneYes`GOOSE_TEMPERATURE`Model response randomnessFloat between 0.0 and 1.0Model-specificNo`GOOSE_MAX_TOKENS`Maximum number of tokens for each model response (truncates longer responses)Positive integerModel-specificNo`GOOSE_MODE`[Tool execution behavior](https://block.github.io/goose/docs/guides/goose-permissions)"auto", "approve", "chat", "smart\_approve""auto"No`GOOSE_MAX_TURNS`[Maximum number of turns](https://block.github.io/goose/docs/guides/sessions/smart-context-management#maximum-turns) allowed without user inputInteger (e.g., 10, 50, 100)1000No`GOOSE_LEAD_PROVIDER`Provider for lead model in [lead/worker mode](https://block.github.io/goose/docs/guides/environment-variables#leadworker-model-configuration)Same as `GOOSE_PROVIDER` optionsFalls back to `GOOSE_PROVIDER`No`GOOSE_LEAD_MODEL`Lead model for lead/worker modeModel nameNoneNo`GOOSE_PLANNER_PROVIDER`Provider for [planning mode](https://block.github.io/goose/docs/guides/creating-plans)Same as `GOOSE_PROVIDER` optionsFalls back to `GOOSE_PROVIDER`No`GOOSE_PLANNER_MODEL`Model for planning modeModel nameFalls back to `GOOSE_MODEL`No`GOOSE_TOOLSHIM`Enable tool interpretationtrue/falsefalseNo`GOOSE_TOOLSHIM_OLLAMA_MODEL`Model for tool interpretationModel name (e.g., "llama3.2")System defaultNo`GOOSE_CLI_MIN_PRIORITY`Tool output verbosityFloat between 0.0 and 1.00.0No`GOOSE_CLI_THEME`[Theme](https://block.github.io/goose/docs/guides/goose-cli-commands#themes) for CLI response markdown"light", "dark", "ansi""dark"No`GOOSE_CLI_SHOW_COST`Show estimated cost for token use in the CLItrue/falsefalseNo`GOOSE_ALLOWLIST`URL for allowed extensionsValid URLNoneNo`GOOSE_RECIPE_GITHUB_REPO`GitHub repository for recipesFormat: "org/repo"NoneNo`GOOSE_AUTO_COMPACT_THRESHOLD`Set the percentage threshold at which goose [automatically summarizes your session](https://block.github.io/goose/docs/guides/sessions/smart-context-management#automatic-compaction).Float between 0.0 and 1.0 (disabled at 0.0)0.8No`OTEL_EXPORTER_OTLP_ENDPOINT`OTLP endpoint URL for [observability](https://block.github.io/goose/docs/guides/environment-variables#opentelemetry-protocol-otlp)URL (e.g., `http://localhost:4318`)NoneNo`OTEL_EXPORTER_OTLP_TIMEOUT`Export timeout in milliseconds for [observability](https://block.github.io/goose/docs/guides/environment-variables#opentelemetry-protocol-otlp)Integer (ms)10000No`SECURITY_PROMPT_ENABLED`Enable [prompt injection detection](https://block.github.io/goose/docs/guides/security/prompt-injection-detection) to identify potentially harmful commandstrue/falsefalseNo`SECURITY_PROMPT_THRESHOLD`Sensitivity threshold for [prompt injection detection](https://block.github.io/goose/docs/guides/security/prompt-injection-detection) (higher = stricter)Float between 0.01 and 1.00.7No

## Experimental Features[​](#experimental-features "Direct link to Experimental Features")

These settings enable experimental features that are in active development. These may change or be removed in future releases.

SettingPurposeValuesDefaultRequired`ALPHA_FEATURES`Enables access to experimental alpha features—check the feature docs to see if this flag is requiredtrue/falsefalseNo

Additional [environment variables](https://block.github.io/goose/docs/guides/environment-variables) may also be supported in config.yaml.

## Example Configuration[​](#example-configuration "Direct link to Example Configuration")

Here's a basic example of a config.yaml file:

```
# Model Configuration
GOOSE_PROVIDER:"anthropic"
GOOSE_MODEL:"claude-4.5-sonnet"
GOOSE_TEMPERATURE:0.7

# Planning Configuration
GOOSE_PLANNER_PROVIDER:"openai"
GOOSE_PLANNER_MODEL:"gpt-4"

# Tool Configuration
GOOSE_MODE:"smart_approve"
GOOSE_TOOLSHIM:true
GOOSE_CLI_MIN_PRIORITY:0.2

# Recipe Configuration
GOOSE_RECIPE_GITHUB_REPO:"block/goose-recipes"

# Search Path Configuration
GOOSE_SEARCH_PATHS:
-"/usr/local/bin"
-"~/custom/tools"
-"/opt/homebrew/bin"

# Observability (OpenTelemetry)
OTEL_EXPORTER_OTLP_ENDPOINT:"http://localhost:4318"
OTEL_EXPORTER_OTLP_TIMEOUT:20000

# Security Configuration
SECURITY_PROMPT_ENABLED:true

# Extensions Configuration
extensions:
developer:
bundled:true
enabled:true
name: developer
timeout:300
type: builtin

memory:
bundled:true
enabled:true
name: memory
timeout:300
type: builtin
```

## Extensions Configuration[​](#extensions-configuration "Direct link to Extensions Configuration")

Extensions are configured under the `extensions` key. Each extension can have the following settings:

```
extensions:
extension_name:
bundled: true/false       # Whether it's included with goose
display_name:"Name"# Human-readable name (optional)
enabled: true/false       # Whether the extension is active
name:"extension_name"# Internal name
timeout:300# Operation timeout in seconds
type: "builtin"/"stdio"   # Extension type

# Additional settings for stdio extensions:
cmd:"command"# Command to execute
args:["arg1","arg2"]# Command arguments
description:"text"# Extension description
env_keys:[]# Required environment variables
envs:{}# Environment values
```

## Search Path Configuration[​](#search-path-configuration "Direct link to Search Path Configuration")

Extensions may need to execute external commands or tools. By default, goose uses your system's PATH environment variable. You can add additional search directories in your config file:

```
GOOSE_SEARCH_PATHS:
-"/usr/local/bin"
-"~/custom/tools"
-"/opt/homebrew/bin"
```

These paths are prepended to the system PATH when running extension commands, ensuring your custom tools are found without modifying your global PATH.

## Recipe Command Configuration[​](#recipe-command-configuration "Direct link to Recipe Command Configuration")

You can optionally set up [custom slash commands](https://block.github.io/goose/docs/guides/context-engineering/slash-commands) to run recipes that you create. List the command (without the leading `/`) along with the path to the recipe:

```
slash_commands:
-command:"run-tests"
recipe_path:"/path/to/recipe.yaml"
-command:"daily-standup"
recipe_path:"/Users/me/.local/share/goose/recipes/standup.yaml"
```

## Configuration Priority[​](#configuration-priority "Direct link to Configuration Priority")

Settings are applied in the following order of precedence:

1. Environment variables (highest priority)
2. Config file settings
3. Default values (lowest priority)

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

- Avoid storing sensitive information (API keys, tokens) in the config file
- Use the system keyring for storing secrets
- If keyring is disabled, secrets are stored in a separate `secrets.yaml` file

## Updating Configuration[​](#updating-configuration "Direct link to Updating Configuration")

Changes to config files require restarting goose to take effect. You can verify your current configuration using:

This will show all active settings and their current values.

## See Also[​](#see-also "Direct link to See Also")

- [**Multi-Model Configuration**](https://block.github.io/goose/docs/guides/multi-model/) - For multiple model-selection strategies
- [**Environment Variables**](https://block.github.io/goose/docs/guides/environment-variables) - For environment variable configuration
- [**Using Extensions**](https://block.github.io/goose/docs/getting-started/using-extensions) - For more details on extension configuration