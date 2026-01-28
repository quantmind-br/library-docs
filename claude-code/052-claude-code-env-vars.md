# Claude Code Environment Variables Reference

Based on the analysis of the documentation, here is a comprehensive list of all environment variables accepted by Claude Code, organized by category.

## 🔐 Authentication & Security

| Variable | Description |
| :--- | :--- |
| `ANTHROPIC_API_KEY` | API key sent in the `X-Api-Key` header (typically for SDK usage). |
| `ANTHROPIC_AUTH_TOKEN` | Custom value for the `Authorization` header (automatically prefixed with `Bearer `). |
| `CLAUDE_CODE_CLIENT_CERT` | Path to client certificate for mTLS authentication. |
| `CLAUDE_CODE_CLIENT_KEY` | Path to private key for mTLS client authentication. |
| `CLAUDE_CODE_CLIENT_KEY_PASSPHRASE` | Passphrase to decrypt the mTLS private key (if encrypted). |

## 🧠 Model Configuration

| Variable | Description |
| :--- | :--- |
| `ANTHROPIC_MODEL` | Sets the default model (overrides configuration settings). |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Sets the model used by the `opus` or `opusplan` alias. |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Sets the model used by the `sonnet` alias. |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Sets the model used by the `haiku` alias (formerly `ANTHROPIC_SMALL_FAST_MODEL`). |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Model used by custom subagents. |
| `DISABLE_PROMPT_CACHING` | Set to `1` to globally disable prompt caching. |
| `DISABLE_PROMPT_CACHING_HAIKU` | Disables prompt caching only for Haiku models. |
| `DISABLE_PROMPT_CACHING_SONNET` | Disables prompt caching only for Sonnet models. |
| `DISABLE_PROMPT_CACHING_OPUS` | Disables prompt caching only for Opus models. |

## ☁️ Cloud Providers

### Amazon Bedrock

| Variable | Description |
| :--- | :--- |
| `CLAUDE_CODE_USE_BEDROCK` | Set to `1` to enable Amazon Bedrock integration. |
| `AWS_REGION` | AWS Region (Required). |
| `AWS_PROFILE` | AWS profile name for SSO/CLI authentication. |
| `AWS_ACCESS_KEY_ID` | Explicit Access Key ID. |
| `AWS_SECRET_ACCESS_KEY` | Explicit Secret Access Key. |
| `AWS_SESSION_TOKEN` | Explicit Session Token. |
| `AWS_BEARER_TOKEN_BEDROCK` | Bedrock API Key (alternative to full credentials). |
| `ANTHROPIC_BEDROCK_BASE_URL` | Base URL for Bedrock-compatible LLM Gateway. |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Set to `1` if the gateway manages AWS authentication. |
| `ANTHROPIC_CUSTOM_HEADERS` | Custom headers (e.g., for Amazon Bedrock Guardrails). |

### Google Vertex AI

| Variable | Description |
| :--- | :--- |
| `CLAUDE_CODE_USE_VERTEX` | Set to `1` to enable Vertex AI integration. |
| `CLOUD_ML_REGION` | Vertex AI region (e.g., `us-east5` or `global`). |
| `ANTHROPIC_VERTEX_PROJECT_ID` | GCP Project ID. |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account credentials JSON file. |
| `VERTEX_REGION_<MODEL_NAME>` | Region override per model (e.g., `VERTEX_REGION_CLAUDE_3_5_SONNET`). |
| `ANTHROPIC_VERTEX_BASE_URL` | Base URL for Vertex-compatible LLM Gateway. |
| `CLAUDE_CODE_SKIP_VERTEX_AUTH` | Set to `1` if the gateway manages GCP authentication. |

### Microsoft Foundry (Azure)

| Variable | Description |
| :--- | :--- |
| `CLAUDE_CODE_USE_FOUNDRY` | Set to `1` to enable Microsoft Foundry integration. |
| `ANTHROPIC_FOUNDRY_API_KEY` | Azure resource API Key. |
| `ANTHROPIC_FOUNDRY_RESOURCE` | Azure AI resource name. |
| `ANTHROPIC_FOUNDRY_BASE_URL` | Full base URL of the Azure endpoint. |
| `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` | Set to `1` if the gateway manages Azure authentication. |

## 🌐 Network & Proxy

| Variable | Description |
| :--- | :--- |
| `HTTPS_PROXY` | HTTPS proxy URL (Recommended). |
| `HTTP_PROXY` | HTTP proxy URL. |
| `NO_PROXY` | List of domains to bypass the proxy. |
| `NODE_EXTRA_CA_CERTS` | Path to custom CA certificate (for corporate proxies). |

## 📊 Telemetry & Monitoring (OpenTelemetry)

| Variable | Description |
| :--- | :--- |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | Set to `1` to enable telemetry. |
| `OTEL_METRICS_EXPORTER` | Metrics exporter type (`otlp`, `console`, `prometheus`). |
| `OTEL_LOGS_EXPORTER` | Logs exporter type (`otlp`, `console`). |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint (e.g., `http://localhost:4317`). |
| `OTEL_EXPORTER_OTLP_HEADERS` | OTLP authentication headers (e.g., `Authorization=Bearer ...`). |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (`grpc`, `http/json`). |
| `OTEL_METRIC_EXPORT_INTERVAL` | Metrics export interval in ms. |
| `OTEL_LOG_USER_PROMPTS` | Set to `1` to log user prompt content (Caution: sensitive data). |
| `OTEL_RESOURCE_ATTRIBUTES` | Custom attributes to identify teams/departments. |

## ⚙️ System & LLM Gateway

| Variable | Description |
| :--- | :--- |
| `ANTHROPIC_BASE_URL` | Base URL for generic LLM Gateway (Anthropic/LiteLLM format). |
| `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` | TTL for API key helper script cache. |
| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` | Set to `1` to disable experimental beta headers. |
| `DISABLE_AUTOUPDATER` | Set to `1` to disable automatic updates. |
| `CLAUDE_PROJECT_DIR` | Available in hooks/scripts, contains the project root directory. |
| `CLAUDE_CODE_GIT_BASH_PATH` | (Windows only) Path to Git `bash.exe`. |

## 📝 Tokens & Performance

| Variable | Description |
| :--- | :--- |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Maximum output tokens limit (Recommended `4096` for Bedrock). |
| `MAX_THINKING_TOKENS` | Token limit for "extended thinking" (Recommended `1024` for Bedrock). |
