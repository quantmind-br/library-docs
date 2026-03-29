---
title: ForgeCode
url: https://forgecode.dev/docs/environment-configuration/
source: sitemap
fetched_at: 2026-03-29T14:51:46.640211047-03:00
rendered_js: false
word_count: 467
summary: This document explains how to configure ForgeCode through environment variables and .env files, covering API keys, retry settings, HTTP configuration, tool behavior, and system-level options.
tags:
    - environment-variables
    - configuration
    - api-keys
    - http-settings
    - retry-configuration
    - tool-configuration
    - zsh-plugin
category: configuration
---

ForgeCode can be configured through environment variables to control its behavior, API connections, and model preferences. This page describes the available configuration options and how to use them.

You can configure ForgeCode using either:

1. **Environment Variables**: Set directly in your shell profile (`.bashrc`, `.zshrc`, etc.)
2. **`.env` File**: Create a file named `.env` in your home directory

The `.env` file method is recommended for most users as it keeps your configuration in one place and prevents exposing API keys in your shell history.

### API Keys[​](#api-keys "Direct link to API Keys")

ForgeCode supports multiple AI providers and checks for API keys in the following priority order:

Environment VariableProvider`FORGE_KEY`Antinomy's provider (OpenAI-compatible)`OPENROUTER_API_KEY`Open Router (aggregates multiple models)`OPENAI_API_KEY`Official OpenAI`ANTHROPIC_API_KEY`Official Anthropic

Example configuration in `.env` file:

### Custom Provider URLs[​](#custom-provider-urls "Direct link to Custom Provider URLs")

You can customize the API endpoint URLs for both OpenAI and Anthropic providers:

This is useful for:

- Self-hosted models with OpenAI or Anthropic-compatible APIs
- Enterprise deployments (OpenAI, Anthropic, or Azure)
- Proxy services or API gateways
- Regional API endpoints
- Custom upstream providers for Anthropic requests

ForgeCode supports several environment variables for advanced configuration and fine-tuning. These can be set in your `.env` file or system environment.

info

These variables are optional and have sensible defaults. Only set them if you need to customize ForgeCode's behavior for your specific use case.

### Retry Configuration[​](#retry-configuration "Direct link to Retry Configuration")

Control how ForgeCode handles retry logic for failed requests:

Environment VariableDefaultDescription`FORGE_RETRY_INITIAL_BACKOFF_MS``1000`Initial backoff time in milliseconds before retrying`FORGE_RETRY_BACKOFF_FACTOR``2`Multiplier for backoff time on each retry attempt`FORGE_RETRY_MAX_ATTEMPTS``3`Maximum number of retry attempts for failed requests`FORGE_SUPPRESS_RETRY_ERRORS``false`Suppress retry error messages in output`FORGE_RETRY_STATUS_CODES``429,500,502,503,504`Comma-separated HTTP status codes to retry

**Example:**

### HTTP Configuration[​](#http-configuration "Direct link to HTTP Configuration")

Fine-tune HTTP client behavior for API requests:

Environment VariableDefaultDescription`FORGE_HTTP_CONNECT_TIMEOUT``30`Connection timeout in seconds`FORGE_HTTP_READ_TIMEOUT``900`Read timeout in seconds (15 minutes)`FORGE_HTTP_POOL_IDLE_TIMEOUT``90`Pool idle timeout in seconds`FORGE_HTTP_POOL_MAX_IDLE_PER_HOST``5`Maximum idle connections per host`FORGE_HTTP_MAX_REDIRECTS``10`Maximum redirects to follow`FORGE_HTTP_USE_HICKORY``false`Use Hickory DNS resolver`FORGE_HTTP_TLS_BACKEND``default`TLS backend: `default` or `rustls``FORGE_HTTP_MIN_TLS_VERSION``1.2`Minimum TLS version: `1.0`, `1.1`, `1.2`, `1.3``FORGE_HTTP_MAX_TLS_VERSION``1.3`Maximum TLS version: `1.0`, `1.1`, `1.2`, `1.3``FORGE_HTTP_ADAPTIVE_WINDOW``true`Enable HTTP/2 adaptive window`FORGE_HTTP_KEEP_ALIVE_INTERVAL``60`Keep-alive interval in seconds (use `none` or `disabled` to disable)`FORGE_HTTP_KEEP_ALIVE_TIMEOUT``10`Keep-alive timeout in seconds`FORGE_HTTP_KEEP_ALIVE_WHILE_IDLE``true`Keep-alive while idle`FORGE_HTTP_ACCEPT_INVALID_CERTS``false`Accept invalid SSL/TLS certificates`FORGE_HTTP_ROOT_CERT_PATHS`-Comma-separated paths to root certificate files (PEM, CRT, CER format)

**Example:**

Security Warning

Setting `FORGE_HTTP_ACCEPT_INVALID_CERTS=true` disables SSL/TLS certificate verification, which can expose you to man-in-the-middle attacks. Only use this in development environments or when you fully trust the network and endpoints.

### Tool Configuration[​](#tool-configuration "Direct link to Tool Configuration")

Configure tool execution behavior:

Environment VariableDefaultDescription`FORGE_TOOL_TIMEOUT``300`Maximum execution time in seconds for a tool before termination`FORGE_DUMP_AUTO_OPEN``false`Automatically open dump files in browser

**Example:**

### ZSH Plugin Configuration[​](#zsh-plugin-configuration "Direct link to ZSH Plugin Configuration")

Configure the ZSH plugin behavior. The `FORGE_BIN` environment variable allows you to customize the command used by the ZSH plugin when transforming `#` prefixed commands.

Environment VariableDefaultDescription`FORGE_BIN``forge`Command to use for ForgeCode operations

**Example:**

### System Configuration[​](#system-configuration "Direct link to System Configuration")

System-level environment variables (usually set automatically):

Environment VariableDefaultDescription`FORGE_MAX_SEARCH_RESULT_BYTES``101024`Maximum bytes for search results (10 KB)`FORGE_HISTORY_FILE`System defaultCustom path for ForgeCode history file`SHELL`System defaultShell to use for command execution (Unix/Linux/macOS)`COMSPEC``cmd.exe`Command processor to use (Windows)

**Example:**

### Complete Configuration Example[​](#complete-configuration-example "Direct link to Complete Configuration Example")

Here's a comprehensive example of a `.env` file with all configuration options: