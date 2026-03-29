---
title: SGLang Model Gateway — SGLang
url: https://docs.sglang.io/advanced_features/sgl_model_gateway.html
source: crawler
fetched_at: 2026-02-04T08:46:57.542214642-03:00
rendered_js: false
word_count: 2137
summary: The SGLang Model Gateway is a high-performance routing system for large-scale LLM deployments that centralizes worker management and traffic balancing across multiple protocols. It provides a unified control plane for heterogeneous model fleets with integrated features for reliability, privacy, and observability.
tags:
    - sglang
    - model-gateway
    - llm-routing
    - load-balancing
    - grpc
    - inference-serving
    - worker-management
category: guide
---

## SGLang Model Gateway[#](#sglang-model-gateway "Link to this heading")

SGLang Model Gateway is a high-performance model-routing gateway for large-scale LLM deployments. It centralizes worker lifecycle management, balances traffic across heterogeneous protocols (HTTP, gRPC, OpenAI-compatible), and provides enterprise-ready control over history storage, MCP tooling, and privacy-sensitive workflows. The gateway is deeply optimized for the SGLang serving runtime, but can route to any OpenAI-compatible backend.

* * *

## Table of Contents[#](#table-of-contents "Link to this heading")

01. [Overview](#overview)
02. [Architecture](#architecture)
    
    - [Control Plane](#control-plane)
    - [Data Plane](#data-plane)
    - [Storage and Privacy](#storage-and-privacy)
03. [Installation](#installation)
04. [Quick Start](#quick-start)
05. [Deployment Modes](#deployment-modes)
    
    - [Co-launch Router and Workers](#co-launch-router-and-workers)
    - [Separate Launch (HTTP)](#separate-launch-http)
    - [gRPC Launch](#grpc-launch)
    - [Prefill-Decode Disaggregation](#prefill-decode-disaggregation)
    - [OpenAI Backend Proxy](#openai-backend-proxy)
    - [Multi-Model Inference Gateway](#multi-model-inference-gateway)
06. [API Reference](#api-reference)
    
    - [Inference Endpoints](#inference-endpoints)
    - [Tokenization Endpoints](#tokenization-endpoints)
    - [Parser Endpoints](#parser-endpoints)
    - [Classification API](#classification-api)
    - [Conversation and Response APIs](#conversation-and-response-apis)
    - [Worker Management APIs](#worker-management-apis)
    - [Admin and Health Endpoints](#admin-and-health-endpoints)
07. [Load Balancing Policies](#load-balancing-policies)
08. [Reliability and Flow Control](#reliability-and-flow-control)
    
    - [Retries](#retries)
    - [Circuit Breaker](#circuit-breaker)
    - [Rate Limiting and Queuing](#rate-limiting-and-queuing)
    - [Health Checks](#health-checks)
09. [Reasoning Parser Integration](#reasoning-parser-integration)
10. [Tool Call Parsing](#tool-call-parsing)
11. [Tokenizer Management](#tokenizer-management)
12. [MCP Integration](#mcp-integration)
13. [Service Discovery (Kubernetes)](#service-discovery-kubernetes)
14. [History and Data Connectors](#history-and-data-connectors)
15. [WASM Middleware](#wasm-middleware)
16. [Language Bindings](#language-bindings)
17. [Security and Authentication](#security-and-authentication)
    
    - [TLS (HTTPS) for Gateway Server](#tls-https-for-gateway-server)
    - [mTLS for Worker Communication](#mtls-for-worker-communication)
18. [Observability](#observability)
    
    - [Prometheus Metrics](#prometheus-metrics)
    - [OpenTelemetry Tracing](#opentelemetry-tracing)
    - [Logging](#logging)
19. [Production Recommendations](#production-recommendations)
    
    - [Security Best Practices](#security-best-practices)
    - [High Availability](#high-availability)
    - [Performance](#performance)
    - [Kubernetes Deployment](#kubernetes-deployment)
    - [Monitoring with PromQL](#monitoring-with-promql)
20. [Configuration Reference](#configuration-reference)
21. [Troubleshooting](#troubleshooting)

* * *

## Overview[#](#overview "Link to this heading")

- **Unified control plane** for registering, monitoring, and orchestrating regular, prefill, and decode workers across heterogeneous model fleets.
- **Multi-protocol data plane** that routes traffic across HTTP, PD (prefill/decode), gRPC, and OpenAI-compatible backends with shared reliability primitives.
- **Industry-first gRPC pipeline** with native Rust tokenization, reasoning parsers, and tool-call execution for high-throughput, OpenAI-compatible serving; supports both single-stage and PD topologies.
- **Inference Gateway Mode (`--enable-igw`)** dynamically instantiates multiple router stacks (HTTP regular/PD, gRPC) and applies per-model policies for multi-tenant deployments.
- **Conversation & responses connectors** centralize chat history inside the router so the same context can be reused across models and MCP loops without leaking data to upstream vendors (memory, none, Oracle ATP, PostgreSQL).
- **Enterprise privacy**: agentic multi-turn `/v1/responses`, native MCP client (STDIO/HTTP/SSE/Streamable), and history storage all operate within the router boundary.
- **Reliability core**: retries with jitter, worker-scoped circuit breakers, token-bucket rate limiting with queuing, background health checks, and cache-aware load monitoring.
- **Comprehensive observability**: 40+ Prometheus metrics, OpenTelemetry distributed tracing, structured logging, and request ID propagation.

* * *

## Architecture[#](#architecture "Link to this heading")

### Control Plane[#](#control-plane "Link to this heading")

- **Worker Manager** discovers capabilities (`/get_server_info`, `/get_model_info`), tracks load, and registers/removes workers in the shared registry.
- **Job Queue** serializes add/remove requests and exposes status (`/workers/{worker_id}`) so clients can track onboarding progress.
- **Load Monitor** feeds cache-aware and power-of-two policies with live worker load statistics.
- **Health Checker** continuously probes workers and updates readiness, circuit breaker state, and router metrics.
- **Tokenizer Registry** manages dynamically registered tokenizers with async loading from HuggingFace or local paths.

### Data Plane[#](#data-plane "Link to this heading")

- **HTTP routers** (regular & PD) implement `/generate`, `/v1/chat/completions`, `/v1/completions`, `/v1/responses`, `/v1/embeddings`, `/v1/rerank`, `/v1/classify`, `/v1/tokenize`, `/v1/detokenize`, and associated admin endpoints.
- **gRPC router** streams tokenized requests directly to SRT gRPC workers, running fully in Rust—tokenizer, reasoning parser, and tool parser all reside in-process. Supports both single-stage and PD routing, including embeddings and classification.
- **OpenAI router** proxies OpenAI-compatible endpoints to external vendors (OpenAI, xAI, etc.) while keeping chat history and multi-turn orchestration local.

### Storage and Privacy[#](#storage-and-privacy "Link to this heading")

- Conversation and response history is stored at the router tier (memory, none, Oracle ATP, or PostgreSQL). The same history can power multiple models or MCP loops without sending data to upstream vendors.
- `/v1/responses` agentic flows, MCP sessions, and conversation APIs share the same storage layer, enabling compliance for regulated workloads.

* * *

## Installation[#](#installation "Link to this heading")

### Docker[#](#docker "Link to this heading")

Pre-built Docker images are available on Docker Hub with multi-architecture support (x86\_64 and ARM64):

```
dockerpulllmsysorg/sgl-model-gateway:latest
```

### Prerequisites[#](#prerequisites "Link to this heading")

- **Rust and Cargo**
  
  ```
  curl--proto'=https'--tlsv1.2-sSfhttps://sh.rustup.rs|sh
  source"$HOME/.cargo/env"
  rustc--version
  cargo--version
  ```
- **Python** with `pip` and virtualenv tooling available.

### Rust Binary[#](#rust-binary "Link to this heading")

```
cdsgl-model-gateway
cargobuild--release
```

### Python Package[#](#python-package "Link to this heading")

```
pipinstallmaturin

# Fast development mode
cdsgl-model-gateway/bindings/python
maturindevelop

# Production build
maturinbuild--release--outdist--featuresvendored-openssl
pipinstall--force-reinstalldist/*.whl
```

* * *

## Quick Start[#](#quick-start "Link to this heading")

### Regular HTTP Routing[#](#regular-http-routing "Link to this heading")

```
# Rust binary
./target/release/sgl-model-gateway\
--worker-urlshttp://worker1:8000http://worker2:8000\
--policycache_aware

# Python launcher
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000http://worker2:8000\
--policycache_aware
```

### gRPC Routing[#](#grpc-routing "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlsgrpc://127.0.0.1:20000\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--reasoning-parserdeepseek-r1\
--tool-call-parserjson\
--host0.0.0.0--port8080
```

* * *

## Deployment Modes[#](#deployment-modes "Link to this heading")

### Co-launch Router and Workers[#](#co-launch-router-and-workers "Link to this heading")

Launch the router and a fleet of SGLang workers in one process:

```
python-msglang_router.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--dp-size4\
--host0.0.0.0\
--port30000
```

Comprehensive example with router arguments (prefixed with `--router-`):

```
python-msglang_router.launch_server\
--host0.0.0.0\
--port8080\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--tp-size1\
--dp-size8\
--grpc-mode\
--log-leveldebug\
--router-prometheus-port10001\
--router-tool-call-parserllama\
--router-model-pathmeta-llama/Llama-3.1-8B-Instruct\
--router-policyround_robin\
--router-log-leveldebug
```

### Separate Launch (HTTP)[#](#separate-launch-http "Link to this heading")

Run workers independently and point the router at their HTTP endpoints:

```
# Worker nodes
python-msglang.launch_server--modelmeta-llama/Meta-Llama-3.1-8B-Instruct--port8000
python-msglang.launch_server--modelmeta-llama/Meta-Llama-3.1-8B-Instruct--port8001

# Router node
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000http://worker2:8001\
--policycache_aware\
--host0.0.0.0--port30000
```

### gRPC Launch[#](#grpc-launch "Link to this heading")

Use SRT gRPC workers to unlock the highest throughput and access native reasoning/tool pipelines:

```
# Workers expose gRPC endpoints
python-msglang.launch_server\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--grpc-mode\
--port20000

# Router
python-msglang_router.launch_router\
--worker-urlsgrpc://127.0.0.1:20000\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--reasoning-parserdeepseek-r1\
--tool-call-parserjson\
--host0.0.0.0--port8080
```

The gRPC router supports both regular HTTP-equivalent serving and PD (prefill/decode) serving. Provide `--tokenizer-path` or `--model-path` (HuggingFace ID or local directory) whenever connection mode resolves to gRPC.

### Prefill-Decode Disaggregation[#](#prefill-decode-disaggregation "Link to this heading")

Split prefill and decode workers for PD-aware caching and balancing:

```
python-msglang_router.launch_router\
--pd-disaggregation\
--prefillhttp://prefill1:300019001\
--decodehttp://decode1:30011\
--prefill-policycache_aware\
--decode-policypower_of_two
```

Prefill entries accept an optional bootstrap port. PD mode merges prefill metadata with decode outputs and streams results back to the client.

### OpenAI Backend Proxy[#](#openai-backend-proxy "Link to this heading")

Proxy OpenAI-compatible endpoints while keeping history and MCP sessions local:

```
python-msglang_router.launch_router\
--backendopenai\
--worker-urlshttps://api.openai.com\
--history-backendmemory
```

OpenAI backend mode expects exactly one `--worker-urls` entry per router instance.

### Multi-Model Inference Gateway[#](#multi-model-inference-gateway "Link to this heading")

Enable IGW mode to route multiple models through a single router:

```
./target/release/sgl-model-gateway\
--enable-igw\
--policycache_aware\
--max-concurrent-requests512

# Register workers dynamically
curl-XPOSThttp://localhost:30000/workers\
-H"Content-Type: application/json"\
-d'{
        "url": "http://worker-a:8000",
        "model_id": "mistral",
        "priority": 10,
        "labels": {"tier": "gold"}
      }'
```

* * *

## API Reference[#](#api-reference "Link to this heading")

### Inference Endpoints[#](#inference-endpoints "Link to this heading")

### Tokenization Endpoints[#](#tokenization-endpoints "Link to this heading")

The gateway provides HTTP endpoints for text tokenization with batch support, designed to mirror the SGLang Python tokenization API.

#### Tokenize Request[#](#tokenize-request "Link to this heading")

```
{
"model":"meta-llama/Llama-3.1-8B-Instruct",
"prompt":"Hello, world!"
}
```

#### Batch Tokenize Request[#](#batch-tokenize-request "Link to this heading")

```
{
"model":"meta-llama/Llama-3.1-8B-Instruct",
"prompt":["Hello","World","How are you?"]
}
```

#### Tokenize Response[#](#tokenize-response "Link to this heading")

```
{
"tokens":[15339,11,1917,0],
"count":4,
"char_count":13
}
```

#### Detokenize Request[#](#detokenize-request "Link to this heading")

```
{
"model":"meta-llama/Llama-3.1-8B-Instruct",
"tokens":[15339,11,1917,0],
"skip_special_tokens":true
}
```

#### Detokenize Response[#](#detokenize-response "Link to this heading")

```
{
"text":"Hello, world!"
}
```

#### Add Tokenizer (Async)[#](#add-tokenizer-async "Link to this heading")

```
curl-XPOSThttp://localhost:30000/v1/tokenizers\
-H"Content-Type: application/json"\
-d'{"name": "llama3", "source": "meta-llama/Llama-3.1-8B-Instruct"}'
```

Response:

```
{
"id":"550e8400-e29b-41d4-a716-446655440000",
"status":"pending",
"message":"Tokenizer registration queued"
}
```

Check status:

```
curlhttp://localhost:30000/v1/tokenizers/550e8400-e29b-41d4-a716-446655440000/status
```

### Parser Endpoints[#](#parser-endpoints "Link to this heading")

The gateway provides admin endpoints for parsing reasoning content and function calls from LLM outputs.

#### Separate Reasoning Request[#](#separate-reasoning-request "Link to this heading")

```
{
"text":"<think>Let me analyze this step by step...</think>The answer is 42.",
"parser":"deepseek-r1"
}
```

#### Response[#](#response "Link to this heading")

```
{
"normal_text":"The answer is 42.",
"reasoning_text":"Let me analyze this step by step..."
}
```

#### Function Call Parsing[#](#function-call-parsing "Link to this heading")

```
{
"text":"{\"name\": \"get_weather\", \"arguments\": {\"city\": \"NYC\"}}",
"parser":"json"
}
```

### Classification API[#](#classification-api "Link to this heading")

The `/v1/classify` endpoint provides text classification using sequence classification models (e.g., `Qwen2ForSequenceClassification`, `BertForSequenceClassification`).

#### Request[#](#request "Link to this heading")

```
curlhttp://localhost:30000/v1/classify\
-H"Content-Type: application/json"\
-d'{
    "model": "jason9693/Qwen2.5-1.5B-apeach",
    "input": "I love this product!"
  }'
```

#### Response[#](#id1 "Link to this heading")

```
{
"id":"classify-a1b2c3d4-5678-90ab-cdef-1234567890ab",
"object":"list",
"created":1767034308,
"model":"jason9693/Qwen2.5-1.5B-apeach",
"data":[
{
"index":0,
"label":"positive",
"probs":[0.12,0.88],
"num_classes":2
}
],
"usage":{
"prompt_tokens":6,
"completion_tokens":0,
"total_tokens":6
}
}
```

#### Response Fields[#](#response-fields "Link to this heading")

#### Notes[#](#notes "Link to this heading")

- Classification reuses the embedding backend—the scheduler returns logits which are converted to probabilities via softmax
- Labels come from the model’s HuggingFace config (`id2label` field); models without this mapping use generic labels (`LABEL_0`, `LABEL_1`, etc.)
- Both HTTP and gRPC routers support classification

### Conversation and Response APIs[#](#conversation-and-response-apis "Link to this heading")

### Worker Management APIs[#](#worker-management-apis "Link to this heading")

#### Add Worker[#](#add-worker "Link to this heading")

```
curl-XPOSThttp://localhost:30000/workers\
-H"Content-Type: application/json"\
-d'{"url":"grpc://0.0.0.0:31000","worker_type":"regular"}'
```

#### List Workers[#](#list-workers "Link to this heading")

```
curlhttp://localhost:30000/workers
```

Response:

```
{
"workers":[
{
"id":"2f3a0c3e-3a7b-4c3f-8c70-1b7d4c3a6e1f",
"url":"http://0.0.0.0:31378",
"model_id":"mistral",
"priority":50,
"cost":1.0,
"worker_type":"regular",
"is_healthy":true,
"load":0,
"connection_mode":"Http"
}
],
"total":1,
"stats":{
"prefill_count":0,
"decode_count":0,
"regular_count":1
}
}
```

### Admin and Health Endpoints[#](#admin-and-health-endpoints "Link to this heading")

* * *

## Load Balancing Policies[#](#load-balancing-policies "Link to this heading")

### Cache-Aware Policy Tuning[#](#cache-aware-policy-tuning "Link to this heading")

```
--cache-threshold0.5\
--balance-abs-threshold32\
--balance-rel-threshold1.5\
--eviction-interval-secs120\
--max-tree-size67108864
```

* * *

## Reliability and Flow Control[#](#reliability-and-flow-control "Link to this heading")

### Retries[#](#retries "Link to this heading")

Configure exponential backoff retries:

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000http://worker2:8001\
--retry-max-retries5\
--retry-initial-backoff-ms50\
--retry-max-backoff-ms30000\
--retry-backoff-multiplier1.5\
--retry-jitter-factor0.2
```

**Retryable Status Codes:** 408, 429, 500, 502, 503, 504

### Circuit Breaker[#](#circuit-breaker "Link to this heading")

Per-worker circuit breakers prevent cascading failures:

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000http://worker2:8001\
--cb-failure-threshold5\
--cb-success-threshold2\
--cb-timeout-duration-secs30\
--cb-window-duration-secs60
```

**Circuit Breaker States:**

- **Closed**: Normal operation, requests allowed
- **Open**: Failing, requests rejected immediately
- **Half-Open**: Testing recovery, limited requests allowed

### Rate Limiting and Queuing[#](#rate-limiting-and-queuing "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000http://worker2:8001\
--max-concurrent-requests256\
--rate-limit-tokens-per-second512\
--queue-size128\
--queue-timeout-secs30
```

Requests beyond the concurrency limit wait in a FIFO queue. Returns:

- `429 Too Many Requests` when queue is full
- `408 Request Timeout` when queue timeout expires

### Health Checks[#](#health-checks "Link to this heading")

```
--health-check-interval-secs30\
--health-check-timeout-secs10\
--health-success-threshold2\
--health-failure-threshold3\
--health-check-endpoint/health
```

* * *

## Reasoning Parser Integration[#](#reasoning-parser-integration "Link to this heading")

The gateway includes built-in reasoning parsers for models that use Chain-of-Thought (CoT) reasoning with explicit thinking blocks.

### Supported Parsers[#](#supported-parsers "Link to this heading")

### Usage[#](#usage "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlsgrpc://127.0.0.1:20000\
--model-pathdeepseek-ai/DeepSeek-R1\
--reasoning-parserdeepseek-r1
```

The gRPC router automatically:

1. Detects reasoning blocks in streaming output
2. Separates reasoning content from normal text
3. Applies incremental streaming parsing with buffer management
4. Handles partial token detection for correct streaming behavior

* * *

## Tool Call Parsing[#](#tool-call-parsing "Link to this heading")

The gateway supports parsing function/tool calls from LLM outputs in multiple formats.

### Supported Formats[#](#supported-formats "Link to this heading")

### Usage[#](#id2 "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlsgrpc://127.0.0.1:20000\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--tool-call-parserjson
```

* * *

## Tokenizer Management[#](#tokenizer-management "Link to this heading")

### Tokenizer Sources[#](#tokenizer-sources "Link to this heading")

The gateway supports multiple tokenizer backends:

- **HuggingFace**: Load from HuggingFace Hub by model ID
- **Local**: Load from local `tokenizer.json` or directory
- **Tiktoken**: Auto-detect OpenAI GPT models (gpt-4, davinci, etc.)

### Configuration[#](#configuration "Link to this heading")

```
# HuggingFace model
--model-pathmeta-llama/Llama-3.1-8B-Instruct

# Local tokenizer
--tokenizer-path/path/to/tokenizer.json

# With chat template override
--chat-template/path/to/template.jinja
```

### Tokenizer Caching[#](#tokenizer-caching "Link to this heading")

Two-level caching for optimal performance:

```
--enable-l0-cache\
--l0-max-entries10000\
--enable-l1-cache\
--l1-max-memory52428800# 50MB
```

* * *

## MCP Integration[#](#mcp-integration "Link to this heading")

The gateway provides native Model Context Protocol (MCP) client integration for tool execution.

### Supported Transports[#](#supported-transports "Link to this heading")

### Configuration[#](#id3 "Link to this heading")

```
python-msglang_router.launch_router\
--mcp-config-path/path/to/mcp-config.yaml\
--worker-urlshttp://worker1:8000
```

### MCP Configuration File[#](#mcp-configuration-file "Link to this heading")

```
servers:
-name:"filesystem"
command:"npx"
args:["-y","@modelcontextprotocol/server-filesystem","/tmp"]
protocol:"stdio"
required:false

-name:"github"
url:"https://api.github.com/mcp"
token:"ghp_xxxxx"
protocol:"sse"
required:false

-name:"custom-tools"
url:"https://tools.example.com/mcp"
protocol:"streamable"
required:true

pool:
max_connections:100
idle_timeout:300

proxy:
http:"http://proxy.internal:8080"
https:"https://proxy.internal:8443"
no_proxy:"localhost,127.0.0.1,*.internal"

inventory:
enable_refresh:true
tool_ttl:300
refresh_interval:300
```

* * *

## Service Discovery (Kubernetes)[#](#service-discovery-kubernetes "Link to this heading")

Enable automatic worker discovery via Kubernetes pod selectors:

```
python-msglang_router.launch_router\
--service-discovery\
--selectorapp=sglang-workerrole=inference\
--service-discovery-namespaceproduction\
--service-discovery-port8000
```

### PD Mode Discovery[#](#pd-mode-discovery "Link to this heading")

```
--pd-disaggregation\
--prefill-selectorapp=sglangcomponent=prefill\
--decode-selectorapp=sglangcomponent=decode\
--service-discovery
```

Prefill pods can expose bootstrap ports via the `sglang.ai/bootstrap-port` annotation. RBAC must allow `get`, `list`, and `watch` on pods.

* * *

## History and Data Connectors[#](#history-and-data-connectors "Link to this heading")

### Oracle Configuration[#](#oracle-configuration "Link to this heading")

```
# Connection descriptor
exportATP_DSN="(description=(address=(protocol=tcps)(port=1522)(host=adb.region.oraclecloud.com))(connect_data=(service_name=service_name)))"

# Or TNS alias (requires wallet)
exportATP_TNS_ALIAS="sglroutertestatp_high"
exportATP_WALLET_PATH="/path/to/wallet"

# Credentials
exportATP_USER="admin"
exportATP_PASSWORD="secret"
exportATP_POOL_MIN=4
exportATP_POOL_MAX=32

python-msglang_router.launch_router\
--backendopenai\
--worker-urlshttps://api.openai.com\
--history-backendoracle
```

### PostgreSQL Configuration[#](#postgresql-configuration "Link to this heading")

```
exportPOSTGRES_DB_URL="postgres://user:password@host:5432/dbname"

python-msglang_router.launch_router\
--backendopenai\
--worker-urlshttps://api.openai.com\
--history-backendpostgres
```

### Redis Configuration[#](#redis-configuration "Link to this heading")

```
exportREDIS_URL="redis://localhost:6379"
exportREDIS_POOL_MAX=16
exportREDIS_RETENTION_DAYS=30

python-msglang_router.launch_router\
--backendopenai\
--worker-urlshttps://api.openai.com\
--history-backendredis\
--redis-retention-days30
```

Use `--redis-retention-days -1` for persistent storage (default is 30 days).

* * *

## WASM Middleware[#](#wasm-middleware "Link to this heading")

The gateway supports WebAssembly (WASM) middleware modules for custom request/response processing. This enables organization-specific logic for authentication, rate limiting, billing, logging, and more—without modifying or recompiling the gateway.

### Overview[#](#id4 "Link to this heading")

WASM middleware runs in a sandboxed environment with memory isolation, no network/filesystem access, and configurable resource limits.

### Examples[#](#examples "Link to this heading")

Complete working examples are available in `examples/wasm/`:

The interface definition is located at `src/wasm/interface`.

### Building Modules[#](#building-modules "Link to this heading")

```
# Prerequisites
rustuptargetaddwasm32-wasip2
cargoinstallwasm-tools

# Build
cargobuild--targetwasm32-wasip2--release

# Convert to component format
wasm-toolscomponentnew\
target/wasm32-wasip2/release/my_middleware.wasm\
-omy_middleware.component.wasm
```

### Deploying Modules[#](#deploying-modules "Link to this heading")

```
# Enable WASM support
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000\
--enable-wasm

# Upload module
curl-XPOSThttp://localhost:30000/wasm\
-H"Content-Type: application/json"\
-d'{
    "modules": [{
      "name": "auth-middleware",
      "file_path": "/absolute/path/to/auth.component.wasm",
      "module_type": "Middleware",
      "attach_points": [{"Middleware": "OnRequest"}]
    }]
  }'

# List modules
curlhttp://localhost:30000/wasm

# Remove module
curl-XDELETEhttp://localhost:30000/wasm/{module_uuid}
```

### Runtime Configuration[#](#runtime-configuration "Link to this heading")

**Note:** Rate limiting state is per-worker thread and not shared across gateway replicas. For production, consider implementing rate limiting at a shared layer (e.g., Redis)

* * *

## Language Bindings[#](#language-bindings "Link to this heading")

SGLang Model Gateway provides official language bindings for Python and Go, enabling integration with different technology stacks and organizational requirements.

### Python Bindings[#](#python-bindings "Link to this heading")

The Python bindings provide a PyO3-based wrapper around the Rust gateway library. This is a straightforward binding that calls the gateway server startup from Python.

#### Installation[#](#id5 "Link to this heading")

```
# From PyPI
pipinstallsglang-router

# Development build
cdsgl-model-gateway/bindings/python
pipinstallmaturin&&maturindevelop--featuresvendored-openssl
```

#### Usage[#](#id6 "Link to this heading")

The Python bindings are used throughout this documentation. See the [Quick Start](#quick-start) and [Deployment Modes](#deployment-modes) sections for detailed examples.

Key components:

- `RouterArgs` dataclass with 50+ configuration options
- `Router.from_args()` for programmatic startup
- CLI commands: `smg launch`, `smg server`, `python -m sglang_router.launch_router`

### Go Bindings[#](#go-bindings "Link to this heading")

The Go bindings provide a high-performance gRPC client library for organizations with Go-based infrastructure. This is ideal for:

- Integration with internal Go services and tooling
- High-performance client applications
- Building custom OpenAI-compatible proxy servers

#### Architecture[#](#id7 "Link to this heading")

```
┌─────────────────────────────────────────┐
│         High-Level Go API               │
│   (client.go - OpenAI-style interface)  │
├─────────────────────────────────────────┤
│         gRPC Layer                      │
├─────────────────────────────────────────┤
│         Rust FFI Layer                  │
│   (Tokenization, Parsing, Conversion)   │
└─────────────────────────────────────────┘
```

**Key Features:**

- Native Rust tokenization via FFI (thread-safe, lock-free)
- Full streaming support with context cancellation
- Configurable channel buffer sizes for high concurrency
- Built-in tool call parsing and chat template application

#### Installation[#](#id8 "Link to this heading")

```
# Build the FFI library first
cdsgl-model-gateway/bindings/golang
makebuild&&makelib

# Then use in your Go project
gogetgithub.com/sgl-project/sgl-go-sdk
```

**Requirements:** Go 1.24+, Rust toolchain

#### Examples[#](#id9 "Link to this heading")

Complete working examples are available in `bindings/golang/examples/`:

```
# Run examples
cdsgl-model-gateway/bindings/golang/examples/simple&&./run.sh
cdsgl-model-gateway/bindings/golang/examples/streaming&&./run.sh
cdsgl-model-gateway/bindings/golang/examples/oai_server&&./run.sh
```

#### Testing[#](#testing "Link to this heading")

```
cdsgl-model-gateway/bindings/golang

# Unit tests
gotest-v./...

# Integration tests (requires running SGLang server)
exportSGL_GRPC_ENDPOINT=grpc://localhost:20000
exportSGL_TOKENIZER_PATH=/path/to/tokenizer
gotest-tags=integration-v./...
```

### Comparison[#](#comparison "Link to this heading")

**When to Use Python:** Launching and managing the gateway server, service discovery, PD disaggregation.

**When to Use Go:** Building custom client applications, integration with Go microservices, OpenAI-compatible proxy servers

* * *

## Security and Authentication[#](#security-and-authentication "Link to this heading")

### Router API Key[#](#router-api-key "Link to this heading")

```
python-msglang_router.launch_router\
--api-key"your-router-api-key"\
--worker-urlshttp://worker1:8000
```

Clients must supply `Authorization: Bearer <key>` for protected endpoints.

### Worker API Keys[#](#worker-api-keys "Link to this heading")

```
# Add worker with explicit key
curl-H"Authorization: Bearer router-key"\
-XPOSThttp://localhost:8080/workers\
-H"Content-Type: application/json"\
-d'{"url":"http://worker:8000","api_key":"worker-key"}'
```

### Security Configurations[#](#security-configurations "Link to this heading")

1. **No Authentication** (default): Use only in trusted environments
2. **Router-only Authentication**: Clients authenticate to router
3. **Worker-only Authentication**: Router open, workers require keys
4. **Full Authentication**: Both router and workers protected

### TLS (HTTPS) for Gateway Server[#](#tls-https-for-gateway-server "Link to this heading")

Enable TLS to serve the gateway over HTTPS:

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000\
--tls-cert-path/path/to/server.crt\
--tls-key-path/path/to/server.key
```

Both parameters must be provided together. The gateway uses rustls with the ring crypto provider for TLS termination. If TLS is not configured, the gateway falls back to plain HTTP.

### mTLS for Worker Communication[#](#mtls-for-worker-communication "Link to this heading")

Enable mutual TLS (mTLS) for secure communication with workers in HTTP mode:

```
python-msglang_router.launch_router\
--worker-urlshttps://worker1:8443https://worker2:8443\
--client-cert-path/path/to/client.crt\
--client-key-path/path/to/client.key\
--ca-cert-path/path/to/ca.crt
```

**Key Points:**

- Client certificate and key must be provided together
- Multiple CA certificates can be added with multiple `--ca-cert-path` flags
- Uses rustls backend when TLS is configured
- Single HTTP client is created for all workers (assumes single security domain)
- TCP keepalive (30 seconds) is enabled for long-lived connections

### Full TLS Configuration Example[#](#full-tls-configuration-example "Link to this heading")

Gateway HTTPS + Worker mTLS + API Key authentication:

```
python-msglang_router.launch_router\
--worker-urlshttps://worker1:8443https://worker2:8443\
--tls-cert-path/etc/certs/server.crt\
--tls-key-path/etc/certs/server.key\
--client-cert-path/etc/certs/client.crt\
--client-key-path/etc/certs/client.key\
--ca-cert-path/etc/certs/ca.crt\
--api-key"secure-api-key"\
--policycache_aware
```

* * *

## Observability[#](#observability "Link to this heading")

### Prometheus Metrics[#](#prometheus-metrics "Link to this heading")

Enable with `--prometheus-host`/`--prometheus-port` (defaults to `0.0.0.0:29000`).

#### Metric Categories (40+ metrics)[#](#metric-categories-40-metrics "Link to this heading")

#### Key Inference Metrics (gRPC mode)[#](#key-inference-metrics-grpc-mode "Link to this heading")

#### Duration Buckets[#](#duration-buckets "Link to this heading")

1ms, 5ms, 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 2.5s, 5s, 10s, 15s, 30s, 45s, 60s, 90s, 120s, 180s, 240s

### OpenTelemetry Tracing[#](#opentelemetry-tracing "Link to this heading")

Enable distributed tracing with OTLP export:

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000\
--enable-trace\
--otlp-traces-endpointlocalhost:4317
```

#### Features[#](#features "Link to this heading")

- OTLP/gRPC exporter (default port 4317)
- W3C Trace Context propagation for HTTP and gRPC
- Batch span processing (500ms delay, 64 span batch size)
- Custom filtering to reduce noise
- Trace context injection into upstream worker requests
- Service name: `sgl-router`

### Logging[#](#logging "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000\
--log-leveldebug\
--log-dir./router_logs
```

Structured tracing with optional file sink. Log levels: `debug`, `info`, `warn`, `error`.

### Request ID Propagation[#](#request-id-propagation "Link to this heading")

```
--request-id-headersx-request-idx-trace-idx-correlation-id
```

Responses include `x-request-id` header for correlation.

* * *

## Production Recommendations[#](#production-recommendations "Link to this heading")

This section provides guidance for deploying SGLang Model Gateway in production environments.

### Security Best Practices[#](#security-best-practices "Link to this heading")

**Always enable TLS in production:**

```
python-msglang_router.launch_router\
--worker-urlshttps://worker1:8443https://worker2:8443\
--tls-cert-path/etc/certs/server.crt\
--tls-key-path/etc/certs/server.key\
--client-cert-path/etc/certs/client.crt\
--client-key-path/etc/certs/client.key\
--ca-cert-path/etc/certs/ca.crt\
--api-key"${ROUTER_API_KEY}"
```

**Security Checklist:**

- Enable TLS for gateway HTTPS termination
- Enable mTLS for worker communication when workers are on untrusted networks
- Set `--api-key` to protect router endpoints
- Use Kubernetes Secrets or a secrets manager for credentials
- Rotate certificates and API keys periodically
- Restrict network access with firewalls or network policies

### High Availability[#](#high-availability "Link to this heading")

**Scaling Strategy:**

The gateway supports running multiple replicas behind a load balancer for high availability. However, there are important considerations:

**Recommendations:**

1. **Prefer horizontal scaling over vertical scaling**: Deploy multiple smaller gateway replicas rather than one large instance with excessive CPU and memory. This provides:
   
   - Better fault tolerance (single replica failure doesn’t take down the gateway)
   - More predictable resource usage
   - Easier capacity planning
2. **Use Kubernetes Service Discovery**: Let the gateway automatically discover and manage workers:
   
   ```
   python-msglang_router.launch_router\
   --service-discovery\
   --selectorapp=sglang-worker\
   --service-discovery-namespaceproduction
   ```
3. **Accept cache efficiency trade-off**: With multiple replicas, the cache-aware routing policy’s radix tree is not synchronized across replicas. This means:
   
   - Each replica builds its own cache tree
   - Requests from the same user may hit different replicas
   - Expected cache hit rate reduction: **10-20%**
   - This is often acceptable given the HA benefits
4. **Configure session affinity (optional)**: If cache efficiency is critical, configure your load balancer for session affinity based on a consistent hash of the request (e.g., user ID or API key).

**Example HA Architecture:**

```
                    ┌─────────────────┐
                    │  Load Balancer  │
                    │   (L4/L7)       │
                    └────────┬────────┘
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │  Gateway  │  │  Gateway  │  │  Gateway  │
        │ Replica 1 │  │ Replica 2 │  │ Replica 3 │
        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │  Worker   │  │  Worker   │  │  Worker   │
        │  Pod 1    │  │  Pod 2    │  │  Pod N    │
        └───────────┘  └───────────┘  └───────────┘
```

### Performance[#](#performance "Link to this heading")

**Use gRPC mode for high throughput:**

gRPC mode provides the highest performance for SGLang workers:

```
# Start workers in gRPC mode
python-msglang.launch_server\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--grpc-mode\
--port20000

# Configure gateway for gRPC
python-msglang_router.launch_router\
--worker-urlsgrpc://worker1:20000grpc://worker2:20000\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--policycache_aware
```

**Performance Benefits of gRPC:**

- Native Rust tokenization (no Python overhead)
- Streaming with lower latency
- Built-in reasoning parser execution
- Tool call parsing in the gateway
- Reduced serialization overhead

**Tuning Recommendations:**

### Kubernetes Deployment[#](#kubernetes-deployment "Link to this heading")

**Pod Labeling for Service Discovery:**

For the gateway to discover workers automatically, label your worker pods consistently:

```
# Worker Deployment (Regular Mode)
apiVersion:apps/v1
kind:Deployment
metadata:
name:sglang-worker
namespace:production
spec:
replicas:4
selector:
matchLabels:
app:sglang-worker
component:inference
template:
metadata:
labels:
app:sglang-worker
component:inference
model:llama-3-8b
spec:
containers:
-name:worker
image:lmsysorg/sglang:latest
ports:
-containerPort:8000
name:http
-containerPort:20000
name:grpc
```

**Gateway configuration for discovery:**

```
python-msglang_router.launch_router\
--service-discovery\
--selectorapp=sglang-workercomponent=inference\
--service-discovery-namespaceproduction\
--service-discovery-port8000
```

**PD (Prefill/Decode) Mode Labeling:**

```
# Prefill Worker
metadata:
labels:
app:sglang-worker
component:prefill
annotations:
sglang.ai/bootstrap-port:"9001"

# Decode Worker
metadata:
labels:
app:sglang-worker
component:decode
```

**Gateway configuration for PD discovery:**

```
python-msglang_router.launch_router\
--service-discovery\
--pd-disaggregation\
--prefill-selectorapp=sglang-workercomponent=prefill\
--decode-selectorapp=sglang-workercomponent=decode\
--service-discovery-namespaceproduction
```

**RBAC Requirements:**

The gateway needs permissions to watch pods:

```
apiVersion:rbac.authorization.k8s.io/v1
kind:Role
metadata:
name:sglang-gateway
namespace:production
rules:
-apiGroups:[""]
resources:["pods"]
verbs:["get","list","watch"]
---
apiVersion:rbac.authorization.k8s.io/v1
kind:RoleBinding
metadata:
name:sglang-gateway
namespace:production
subjects:
-kind:ServiceAccount
name:sglang-gateway
namespace:production
roleRef:
kind:Role
name:sglang-gateway
apiGroup:rbac.authorization.k8s.io
```

### Monitoring with PromQL[#](#monitoring-with-promql "Link to this heading")

Configure Prometheus to scrape the gateway metrics endpoint (default: `:29000/metrics`).

**Essential Dashboards:**

**1. Request Rate and Latency:**

```
# Request rate by endpoint
sum(rate(smg_http_requests_total[5m]))by(path,method)

# P50 latency
histogram_quantile(0.50,sum(rate(smg_http_request_duration_seconds_bucket[5m]))by(le))

# P99 latency
histogram_quantile(0.99,sum(rate(smg_http_request_duration_seconds_bucket[5m]))by(le))

# Error rate
sum(rate(smg_http_responses_total{status=~"5.."}[5m]))/sum(rate(smg_http_responses_total[5m]))
```

**2. Worker Health:**

```
# Healthy workers
sum(smg_worker_pool_size)

# Active connections per worker
smg_worker_connections_active

# Worker health check failures
sum(rate(smg_worker_health_checks_total{result="failure"}[5m]))by(worker_id)
```

**3. Circuit Breaker Status:**

```
# Circuit breaker states (0=closed, 1=open, 2=half-open)
smg_worker_cb_state

# Circuit breaker transitions
sum(rate(smg_worker_cb_transitions_total[5m]))by(worker_id,from_state,to_state)

# Workers with open circuits
count(smg_worker_cb_state==1)
```

**4. Inference Performance (gRPC mode):**

```
# Time to first token (P50)
histogram_quantile(0.50,sum(rate(smg_router_ttft_seconds_bucket[5m]))by(le,model))

# Time per output token (P99)
histogram_quantile(0.99,sum(rate(smg_router_tpot_seconds_bucket[5m]))by(le,model))

# Token throughput
sum(rate(smg_router_tokens_total[5m]))by(model,direction)

# Generation duration P95
histogram_quantile(0.95,sum(rate(smg_router_generation_duration_seconds_bucket[5m]))by(le))
```

**5. Rate Limiting and Queuing:**

```
# Rate limit rejections
sum(rate(smg_http_rate_limit_total{decision="rejected"}[5m]))

# Queue depth (if using concurrency limiting)
smg_worker_requests_active

# Retry attempts
sum(rate(smg_worker_retries_total[5m]))by(worker_id)

# Exhausted retries (failures after all retries)
sum(rate(smg_worker_retries_exhausted_total[5m]))
```

**6. MCP Tool Execution:**

```
# Tool call rate
sum(rate(smg_mcp_tool_calls_total[5m]))by(server,tool)

# Tool latency P95
histogram_quantile(0.95,sum(rate(smg_mcp_tool_duration_seconds_bucket[5m]))by(le,tool))

# Active MCP server connections
smg_mcp_servers_active
```

**Alerting Rules Example:**

```
groups:
-name:sglang-gateway
rules:
-alert:HighErrorRate
expr:|
sum(rate(smg_http_responses_total{status=~"5.."}[5m]))
/ sum(rate(smg_http_responses_total[5m])) > 0.05
for:5m
labels:
severity:critical
annotations:
summary:"HigherrorrateonSGLangGateway"

-alert:CircuitBreakerOpen
expr:count(smg_worker_cb_state == 1) > 0
for:2m
labels:
severity:warning
annotations:
summary:"Workercircuitbreakerisopen"

-alert:HighLatency
expr:|
histogram_quantile(0.99, sum(rate(smg_http_request_duration_seconds_bucket[5m])) by (le)) > 30
for:5m
labels:
severity:warning
annotations:
summary:"P99latencyexceeds30seconds"

-alert:NoHealthyWorkers
expr:sum(smg_worker_pool_size) == 0
for:1m
labels:
severity:critical
annotations:
summary:"Nohealthyworkersavailable"
```

* * *

## Configuration Reference[#](#configuration-reference "Link to this heading")

### Core Settings[#](#core-settings "Link to this heading")

### Prefill/Decode[#](#prefill-decode "Link to this heading")

### Kubernetes Discovery[#](#kubernetes-discovery "Link to this heading")

### TLS Configuration[#](#tls-configuration "Link to this heading")

* * *

## Troubleshooting[#](#troubleshooting "Link to this heading")

### Workers Never Ready[#](#workers-never-ready "Link to this heading")

Increase `--worker-startup-timeout-secs` or ensure health probes respond before router startup.

### Load Imbalance / Hot Workers[#](#load-imbalance-hot-workers "Link to this heading")

Inspect `smg_router_requests_total` by worker and tune cache-aware thresholds (`--balance-*`, `--cache-threshold`).

### Circuit Breaker Flapping[#](#circuit-breaker-flapping "Link to this heading")

Increase `--cb-failure-threshold` or extend the timeout/window durations. Consider temporarily disabling retries.

### Queue Overflow (429)[#](#queue-overflow-429 "Link to this heading")

Increase `--queue-size` or reduce client concurrency. Ensure `--max-concurrent-requests` matches downstream capacity.

### Memory Growth[#](#memory-growth "Link to this heading")

Reduce `--max-tree-size` or lower `--eviction-interval-secs` for more aggressive cache pruning.

### Debugging[#](#debugging "Link to this heading")

```
python-msglang_router.launch_router\
--worker-urlshttp://worker1:8000\
--log-leveldebug\
--log-dir./router_logs
```

### gRPC Connection Issues[#](#grpc-connection-issues "Link to this heading")

Ensure workers are started with `--grpc-mode` and verify `--model-path` or `--tokenizer-path` is provided to the router.

### Tokenizer Loading Failures[#](#tokenizer-loading-failures "Link to this heading")

Check HuggingFace Hub credentials (`HF_TOKEN` environment variable) for private models. Verify local paths are accessible.

* * *

SGLang Model Gateway continues to evolve alongside the SGLang runtime. Keep CLI flags, integrations, and documentation aligned when adopting new features or contributing improvements.