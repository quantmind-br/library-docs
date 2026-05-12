---
description: Auto-generated documentation index
generated: 2026-05-03T12:24:08.983634+00:00
source: https://docs.getbifrost.ai/llms.txt
total_docs: 389
categories: 8
---

# Bifrost Documentation Index

> Organized for AI agent consumption. Files numbered following a logical learning sequence.

## Summary

| Property | Value |
|----------|-------|
| Source | https://docs.getbifrost.ai/llms.txt |
| Generated | 2026-05-03T12:24:08.983634+00:00 |
| Total Documents | 389 |
| Categories | Quick Start & Installation, Tutorials & Guides, Concepts & Fundamentals, Configuration, Features, API Reference, Changelog & Releases, Meta & Resources |

---

## Document Index

### 1. Quick Start & Installation (001–017)
*Installation, setup, and first steps*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 001 | `001-quickstart-gateway-setting-up.md` | Setting Up | This document provides a step-by-step guide for installing and configuring Bifrost, an HTTP API gateway for AI provider… | installation, docker, npx, api-gateway, configuration, openai-compatibility |
| 002 | `002-quickstart-gateway-setting-up-auth.md` | Setting up auth | This document provides instructions for enabling and managing basic authentication to secure the Bifrost dashboard and… | bifrost-security, authentication-setup, dashboard-access, api-security, basic-auth, security-configuration |
| 003 | `003-quickstart-gateway-cli-agents.md` | Tools, Editors & CLI Agents | This document provides instructions on integrating Bifrost with various AI agents and CLI tools by configuring base URL… | agent-integration, cli-tools, model-compatibility, api-proxy, mcp-tools, librechat |
| 004 | `004-quickstart-gateway-integrations.md` | Integrations | This document explains how Bifrost integrations act as protocol adapters to provide drop-in compatibility with existing… | ai-integrations, sdk-compatibility, drop-in-replacement, bifrost-api, protocol-adapters, sdk-integration |
| 005 | `005-quickstart-gateway-multimodal.md` | Multimodal Support | This document outlines how to implement multimodal features such as vision analysis, image generation, and audio proces… | multimodal-ai, vision-analysis, image-generation, speech-to-text, text-to-speech, audio-processing |
| 006 | `006-quickstart-gateway-provider-configuration.md` | Provider Configuration | This document explains how to set up and manage multiple AI model providers using the Web UI, API, or configuration fil… | provider-configuration, ai-models, load-balancing, api-keys, environment-variables, multi-provider |
| 007 | `007-quickstart-gateway-streaming.md` | Streaming Responses | This document explains how to implement real-time streaming for text completions, chat, and audio processing using Serv… | streaming-responses, server-sent-events, real-time-api, chat-completions, text-to-speech, speech-to-text |
| 008 | `008-quickstart-gateway-tool-calling.md` | Tool Calling | This document explains how to enable AI models to interact with external services through custom function calling schem… | tool-calling, function-calling, mcp-server, api-integration, model-context-protocol, ai-tools |
| 009 | `009-quickstart-go-sdk-setting-up.md` | Setting Up | This document provides a quick-start guide for integrating the Bifrost AI gateway into a Go application, covering insta… | go-sdk, bifrost-setup, quick-start, ai-gateway, openai-integration, multi-provider |
| 010 | `010-quickstart-go-sdk-context-keys.md` | Context Keys | This document explains how to use Go context keys in Bifrost to configure request behavior and access response metadata… | go-sdk, context-keys, request-configuration, response-metadata, bifrost, api-integration |
| 011 | `011-quickstart-go-sdk-logger.md` | Logging | This document explains how to configure and customize logging within the Bifrost integration, covering the default logg… | logging, bifrost, debugging, monitoring, golang, structured-logging |
| 012 | `012-quickstart-go-sdk-multimodal.md` | Multimodal Support | This document explains how to implement multimodal capabilities using the Bifrost SDK, including vision analysis, image… | multimodal, vision-analysis, image-generation, speech-to-text, text-to-speech, go-sdk |
| 013 | `013-quickstart-go-sdk-provider-configuration.md` | Provider Configuration | This document explains how to configure multiple AI providers, including managing API keys, weighted load balancing, cu… | ai-providers, load-balancing, api-keys, concurrency-control, network-configuration, error-handling |
| 014 | `014-quickstart-go-sdk-streaming.md` | Streaming Responses | This document explains how to implement real-time streaming for text, chat, speech synthesis, and transcription using t… | streaming-api, real-time-responses, go-sdk, text-to-speech, speech-to-text, chat-completions |
| 015 | `015-quickstart-go-sdk-tool-calling.md` | Tool Calling | This document explains how to enable AI models to interact with external functions and services by defining custom tool… | tool-calling, mcp, function-calling, go, chat-completion, ai-integration |
| 016 | `016-plugins-getting-started.md` | Getting Started | This document introduces Bifrost's plugin system, explaining how to extend gateway functionality by intercepting and mo… | bifrost-gateway, go-plugins, dynamic-loading, shared-objects, request-lifecycle, middleware |
| 017 | `017-benchmarking-getting-started.md` | Getting Started | This document provides performance benchmark results for Bifrost across different AWS EC2 instance types and offers gui… | performance-benchmarks, aws-ec2, instance-sizing, latency, scalability, load-testing |

### 2. Tutorials & Guides (018–069)
*Step-by-step tutorials and how-to guides*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 018 | `018-integrations-anthropic-sdk-overview.md` | Overview | This document explains how to use Bifrost as a drop-in replacement for the Anthropic API, enabling multi-provider suppo… | anthropic-api, api-proxy, multi-provider, sdk-integration, protocol-adaptation, load-balancing |
| 019 | `019-integrations-bedrock-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a Bedrock-compatible gateway using the Converse and Invoke APIs with… | aws-bedrock, bifrost-gateway, boto3-integration, api-protocol-adaptation, llm-governance, streaming-api |
| 020 | `020-integrations-genai-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a drop-in replacement for the Google GenAI API, enabling features li… | google-genai-api, api-compatibility, multi-provider, bifrost-integration, python-sdk, javascript-sdk |
| 021 | `021-integrations-openai-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a drop-in replacement for the OpenAI API, allowing users to leverage… | openai-compatibility, multi-provider, api-gateway, sdk-integration, bifrost, proxy-configuration |
| 022 | `022-deployment-guides-how-to-install-make.md` | Install make command | This document provides instructions for installing the make build tool across different operating systems including Win… | installation, make, build-tools, windows, macos, ubuntu |
| 023 | `023-integrations-anthropic-sdk-files-and-batch.md` | Files and Batch API | This document explains how to utilize the Anthropic SDK with Bifrost to perform cross-provider file management and asyn… | anthropic-sdk, batch-api, files-api, cross-provider-routing, asynchronous-processing, bifrost |
| 024 | `024-integrations-bedrock-sdk-files-and-batch.md` | Files and Batch API | This document explains how to use the AWS Bedrock SDK (boto3) with Bifrost to manage files and batch inference jobs acr… | aws-bedrock, boto3, batch-inference, file-management, cross-provider-routing, s3-api |
| 025 | `025-integrations-langchain-sdk.md` | Langchain SDK | This document provides instructions on integrating Bifrost as a drop-in proxy for Langchain applications to enable ente… | langchain, sdk-integration, proxy-setup, python, javascript, ai-governance |
| 026 | `026-integrations-litellm-sdk.md` | LiteLLM SDK | This document explains how to integrate the LiteLLM SDK with Bifrost to add enterprise features like governance and sem… | litellm-sdk, bifrost-proxy, multi-provider-ai, api-governance, semantic-caching, python-integration |
| 027 | `027-integrations-openai-sdk-files-and-batch.md` | Files and Batch API | This document explains how to use Bifrost to manage files and execute asynchronous batch jobs across multiple AI provid… | bifrost, openai-sdk, files-api, batch-api, cross-provider-routing, asynchronous-processing |
| 028 | `028-integrations-pydanticai-sdk.md` | Pydantic AI SDK | This document explains how to integrate the Pydantic AI SDK with Bifrost as a drop-in proxy to enable enterprise featur… | pydantic-ai, bifrost, python-sdk, llm-agents, proxy-configuration, ai-governance |
| 029 | `029-mcp-agent-mode.md` | Agent Mode (Auto-Execution) | This document explains how to enable and configure Agent Mode for autonomous tool execution, allowing AI agents to run… | agent-mode, autonomous-execution, tool-calling, mcp-gateway, automation, bifrost-sdk |
| 030 | `030-mcp-connecting-to-servers.md` | Connecting to MCP Servers | This document explains how to connect Bifrost to external MCP servers using STDIO, HTTP, and SSE protocols to discover… | mcp-server, connection-protocols, bifrost-gateway, stdio-connection, http-integration, sse-streaming |
| 031 | `031-mcp-filtering.md` | Tool Filtering | This document explains how to control MCP tool availability in Bifrost through three hierarchical levels: client config… | mcp, tool-filtering, access-control, bifrost-gateway, sdk-configuration, virtual-keys |
| 032 | `032-mcp-gateway-url.md` | MCP Gateway URL | This document explains how to expose Bifrost Gateway as an MCP server for external clients, covering JSON-RPC/SSE endpo… | mcp-server, bifrost-gateway, json-rpc, sse-stream, virtual-keys, tool-governance |
| 033 | `033-mcp-tool-execution.md` | Tool Execution | Explains how to manually execute Model Context Protocol (MCP) tools within the Bifrost platform to manage approval work… | mcp, tool-execution, workflow-control, bifrost, api-integration, go-sdk |
| 034 | `034-mcp-tool-hosting.md` | Tool Hosting | This document explains how to register and host custom tools directly within a Go application using the Bifrost SDK. It… | go-sdk, tool-hosting, mcp-server, custom-tools, function-calling, in-process-tools |
| 035 | `035-plugins-building-dynamic-binary.md` | Building Dynamically Linked Bifrost Binary | This document explains how to compile a dynamically linked Bifrost binary to enable support for custom Go-based plugins… | bifrost, dynamic-linking, go-plugins, compilation, cgo, docker-build |
| 036 | `036-plugins-writing-go-plugin.md` | Writing Go Plugins | This guide provides step-by-step instructions for developing native Go plugins for Bifrost using shared object files. I… | go-plugins, bifrost, shared-objects, middleware, plugin-development, go-modules |
| 037 | `037-plugins-writing-wasm-plugin.md` | Writing WASM Plugins | This document explains how to build cross-platform WebAssembly plugins for the Bifrost Enterprise platform using variou… | webassembly, wasm-plugins, bifrost-enterprise, plugin-development, assemblyscript, tinygo |
| 038 | `038-providers-supported-providers-anthropic.md` | Anthropic | This document outlines the technical mapping and structural transformations required to convert OpenAI-formatted reques… | anthropic-api, api-conversion, message-handling, parameter-mapping, tool-conversion, bifrost-gateway |
| 039 | `039-providers-supported-providers-azure.md` | Azure | This document provides a technical guide for using the Bifrost API to interface with Azure OpenAI Service, covering dep… | azure-openai, api-integration, deployment-mapping, authentication, multi-model, anthropic-on-azure |
| 040 | `040-providers-supported-providers-bedrock.md` | AWS Bedrock | This document explains how to convert API requests between OpenAI formats and AWS Bedrock's specific model requirements… | aws-bedrock, api-conversion, parameter-mapping, model-families, chat-completions, tool-restructuring |
| 041 | `041-providers-supported-providers-cohere.md` | Cohere | This document provides a technical guide for converting OpenAI-formatted API requests to Cohere's structure, detailing… | cohere, api-integration, parameter-mapping, chat-completions, tool-conversion, reasoning-capabilities |
| 042 | `042-providers-supported-providers-elevenlabs.md` | ElevenLabs | This document provides a technical guide for integrating ElevenLabs audio services, covering text-to-speech, speech-to-… | elevenlabs, text-to-speech, speech-to-text, voice-settings, api-integration, audio-processing |
| 043 | `043-providers-supported-providers-gemini.md` | Google Gemini | This document outlines the technical mapping and conversion processes required to translate OpenAI-style API requests a… | google-gemini, api-conversion, message-transformation, parameter-mapping, tool-calling, reasoning-support |
| 044 | `044-providers-supported-providers-groq.md` | Groq | This document details the integration of Groq's OpenAI-compatible API into Bifrost, covering endpoint support, paramete… | groq, openai-compatibility, chat-completions, api-integration, streaming-support, tool-calling |
| 045 | `045-providers-supported-providers-huggingface.md` | Hugging Face | This guide explains the technical implementation of the Hugging Face provider in Bifrost, detailing model aliasing, mul… | hugging-face, bifrost, inference-providers, model-aliasing, api-integration, request-handling |
| 046 | `046-providers-supported-providers-nebius.md` | Nebius | This document provides a technical guide for integrating with the Nebius API using OpenAI-compatible formats, detailing… | nebius, openai-compatible, api-integration, chat-completions, image-generation, embeddings |
| 047 | `047-providers-supported-providers-ollama.md` | Ollama | This guide explains how to integrate and configure Ollama for local model inference using its OpenAI-compatible API, co… | ollama, openai-compatibility, local-inference, chat-completions, embeddings, self-hosted |
| 048 | `048-providers-supported-providers-openrouter.md` | OpenRouter | This document outlines the integration and conversion logic for the OpenRouter API, detailing supported operations, rea… | openrouter, api-integration, chat-completions, reasoning-models, parameter-mapping, llm-routing |
| 049 | `049-providers-supported-providers-parasail.md` | Parasail | This document provides a technical guide on using the Parasail API, detailing its OpenAI-compatible chat completion cap… | parasail, openai-compatible, chat-completions, api-integration, streaming, tool-calling |
| 050 | `050-providers-supported-providers-perplexity.md` | Perplexity | This document provides a technical guide for integrating the Perplexity API using an OpenAI-compatible interface, focus… | perplexity-api, openai-compatibility, web-search, reasoning-effort, chat-completions, api-integration |
| 051 | `051-providers-supported-providers-sgl.md` | SGLang | This document provides a guide for using SGLang as an OpenAI-compatible inference engine, detailing supported endpoints… | sglang, openai-compatibility, inference-engine, api-reference, chat-completions, text-embeddings |
| 052 | `052-providers-supported-providers-vertex.md` | Vertex AI | This document explains the integration and conversion logic for Google Vertex AI, detailing how to configure multi-mode… | vertex-ai, google-cloud-platform, api-integration, gemini, anthropic-claude, oauth2 |
| 053 | `053-providers-supported-providers-xai.md` | xAI | This document provides an integration guide for the xAI API, detailing its OpenAI-compatible endpoints, supported Grok… | xai, grok, openai-compatible, chat-completions, vision-api, reasoning-models |
| 054 | `054-enterprise-advanced-governance.md` | Getting started | This document introduces the Bifrost Enterprise Governance module, detailing its advanced security, identity management… | enterprise-governance, identity-management, compliance-monitoring, audit-reporting, role-based-access-control, sso-integration |
| 055 | `055-enterprise-audit-logs.md` | Audit Logs | This document outlines the Bifrost audit logging system, detailing how to track security events, configure retention po… | audit-logs, compliance, security-monitoring, siem-integration, enterprise-governance, event-tracking |
| 056 | `056-enterprise-clustering.md` | Clustering | This document explains the architecture and configuration of Bifrost clustering for high-availability deployments, cove… | clustering, high-availability, service-discovery, gossip-protocol, kubernetes, peer-to-peer |
| 057 | `057-enterprise-datadog-connector.md` | Datadog | This document provides a guide for integrating and configuring the Datadog plugin to monitor LLM operations using APM t… | datadog, observability, apm-traces, llm-monitoring, metrics, configuration |
| 058 | `058-enterprise-invpc-deployments.md` | In-VPC Deployments | This document provides an overview and high-level instructions for deploying Bifrost within a Virtual Private Cloud (VP… | vpc-deployment, private-cloud, security-compliance, enterprise-infrastructure, high-availability, cloud-networking |
| 059 | `059-enterprise-mcp-with-fa.md` | MCP with Federated Auth | This document explains how to transform private enterprise APIs into LLM-ready Model Context Protocol tools using feder… | mcp, federated-authentication, api-integration, llm-tools, openapi, enterprise-security |
| 060 | `060-enterprise-rbac.md` | Role-Based Access Control | Explains how to implement and manage Role-Based Access Control (RBAC) in Bifrost to provide fine-grained access managem… | rbac, access-control, permissions, user-management, governance, enterprise-security |
| 061 | `061-enterprise-setting-up-entra.md` | Setting up Microsoft Entra | This document provides step-by-step instructions for configuring Microsoft Entra ID as an identity provider to enable S… | microsoft-entra-id, azure-ad, sso-authentication, identity-management, role-mapping, bifrost-enterprise |
| 062 | `062-enterprise-setting-up-okta.md` | Setting up Okta | Step-by-step instructions for configuring Okta as an identity provider for Bifrost Enterprise to enable SSO and automat… | okta, sso, authentication, identity-provider, oidc, user-provisioning |
| 063 | `063-deployment-guides-ecs.md` | ECS | This document provides instructions for deploying Bifrost to AWS ECS using Makefile automation or AWS CLI commands for… | aws-ecs, bifrost-deployment, fargate, ec2-launch-type, aws-secrets-manager, cloud-infrastructure |
| 064 | `064-deployment-guides-fly.md` | fly.io | This document provides step-by-step instructions for deploying Bifrost to Fly.io using either a cloned repository with… | bifrost, fly-io, deployment, docker, cloud-hosting, devops |
| 065 | `065-deployment-guides-helm.md` | Helm | This document provides instructions and configuration patterns for deploying Bifrost on Kubernetes using Helm charts, c… | helm, kubernetes, deployment, devops, high-availability, configuration |
| 066 | `066-deployment-guides-how-to-multinode.md` | Multinode Deployment | This document explains how to achieve high availability in Bifrost OSS deployments by using a shared configuration file… | high-availability, multinode-deployment, bifrost-oss, kubernetes, docker-compose, deployment-strategies |
| 067 | `067-deployment-guides-k8s.md` | Terraform + k8s | This document provides a comprehensive guide for deploying the Bifrost service on Kubernetes clusters using Terraform a… | terraform, kubernetes, bifrost, infrastructure-as-code, cloud-deployment, aws |
| 068 | `068-architecture-framework-vector-store.md` | Vector Store | This document explains the Bifrost Vector Store component, which provides a unified interface for storing embeddings an… | vector-store, semantic-search, embeddings, weaviate, go-sdk, vector-database |
| 069 | `069-benchmarking-run-your-own-benchmarks.md` | Run Your Own Benchmarks | This document provides instructions for using the official Bifrost benchmarking tool to measure performance across vari… | benchmarking, performance-testing, bifrost, load-testing, latency-metrics, stress-testing |

### 3. Concepts & Fundamentals (070–083)
*Core concepts and fundamental principles*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 070 | `070-mcp-overview.md` | Overview | This document provides an overview of the Model Context Protocol (MCP) integration in Bifrost, explaining how it enable… | model-context-protocol, mcp-server, tool-execution, ai-agents, security-design, bifrost-gateway |
| 071 | `071-integrations-what-is-an-integration.md` | What is an integration? | This document defines Bifrost integrations as protocol adapters that translate between a unified gateway API and variou… | integrations, protocol-adapters, api-gateway, llm-providers, migration-strategies, multi-provider-support |
| 072 | `072-mcp-code-mode.md` | Code Mode | This document explains Code Mode, a feature that optimizes LLM tool orchestration by using TypeScript to manage multipl… | mcp-server, code-mode, token-optimization, typescript-orchestration, performance-tuning, tool-management |
| 073 | `073-providers-provider-routing.md` | Provider Routing | This document explains how Bifrost manages request routing across multiple AI providers using governance rules, adaptiv… | provider-routing, model-catalog, load-balancing, ai-governance, request-routing, multi-provider |
| 074 | `074-enterprise-adaptive-load-balancing.md` | Adaptive Load Balancing | This document explains the technical implementation of adaptive load balancing, detailing how real-time metrics like er… | load-balancing, traffic-management, performance-optimization, health-monitoring, circuit-breaker, adaptive-routing |
| 075 | `075-enterprise-custom-plugins.md` | Custom Plugins | This document outlines Bifrost's custom plugin development services for extending the platform's LLM gateway with speci… | custom-plugins, llm-gateway, workflow-automation, ai-governance, extensibility, enterprise-integration |
| 076 | `076-architecture-core-concurrency.md` | Concurrency | This document explains Bifrost's advanced concurrency architecture, detailing its use of provider-isolated worker pools… | concurrency, worker-pools, goroutines, go-channels, backpressure, resource-management |
| 077 | `077-architecture-core-mcp.md` | Model Context Protocol (MCP) | This document provides a technical deep dive into Bifrost's Model Context Protocol (MCP) architecture, explaining how e… | mcp-architecture, tool-discovery, connection-protocols, runtime-registration, access-control, model-context-protocol |
| 078 | `078-architecture-core-plugins.md` | Plugins | This document provides a detailed overview of Bifrost's plugin architecture, covering its core design principles, lifec… | plugin-architecture, lifecycle-management, execution-pipeline, bifrost, software-extensibility, request-processing |
| 079 | `079-architecture-core-request-flow.md` | Request Flow | This document provides a technical deep dive into the Bifrost request processing pipeline, detailing the stages from tr… | bifrost-architecture, request-flow, load-balancing, middleware-plugins, mcp-integration, memory-pooling |
| 080 | `080-architecture-framework-log-store.md` | Log Store | This document explains the LogStore component of the Bifrost framework, which provides a persistent and queryable syste… | api-logging, data-persistence, observability, bifrost-framework, postgresql, sqlite |
| 081 | `081-architecture-framework-model-catalog.md` | Model Catalog | This document explains the Model Catalog, a centralized system in Bifrost for managing AI model information, automated… | model-catalog, pricing-sync, cost-calculation, multi-modal, model-management, bifrost |
| 082 | `082-architecture-framework-streaming.md` | Streaming | This document explains the Streaming package utility used to aggregate and process real-time AI stream chunks into stru… | streaming, ai-providers, data-aggregation, bifrost-framework, stream-processing, accumulator |
| 083 | `083-architecture-framework-what-is-framework.md` | What is framework? | This document introduces the Bifrost Framework, a shared SDK that provides standardized storage interfaces and utility… | sdk, bifrost-framework, plugin-development, data-storage, configuration-management, vector-store |

### 4. Configuration (084–088)
*Configuration, settings, and customization*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 084 | `084-providers-custom-providers.md` | Custom Providers | This document explains how to create and configure custom provider instances to restrict request types, customize namin… | custom-providers, provider-configuration, access-control, request-type-restriction, api-management, sdk-configuration |
| 085 | `085-providers-performance.md` | Performance Tuning | This document provides instructions and formulas for optimizing Bifrost performance through the configuration of concur… | performance-tuning, concurrency-control, buffer-management, memory-optimization, throughput, resource-allocation |
| 086 | `086-enterprise-guardrails.md` | Guardrails | This document explains how to configure and implement enterprise-grade content safety guardrails in Bifrost to validate… | guardrails, content-safety, llm-security, aws-bedrock, azure-content-safety, patronus-ai |
| 087 | `087-enterprise-log-exports.md` | Log Exports | This document explains how to configure and automate log exports from Bifrost to various storage destinations and data… | log-export, data-retention, cloud-storage, telemetry-data, enterprise-features, data-warehouse |
| 088 | `088-enterprise-vault-support.md` | Vault Support | This document explains how to integrate Bifrost with enterprise secret management systems like HashiCorp Vault and clou… | vault-integration, secret-management, api-key-security, hashicorp-vault, aws-secrets-manager, key-synchronization |

### 5. Features (089–103)
*Feature documentation*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 089 | `089-features-drop-in-replacement.md` | Drop-in Replacement | This document explains how to integrate the Bifrost Gateway as a drop-in replacement for popular AI SDKs by simply upda… | ai-gateway, sdk-integration, drop-in-replacement, load-balancing, failover-management, openai-compatible |
| 090 | `090-features-fallbacks.md` | Fallbacks | This document explains how Bifrost manages automatic failover between different AI providers and models to ensure appli… | automatic-failover, ai-provider-switching, error-handling, high-availability, redundancy, bifrost-gateway |
| 091 | `091-features-governance-budget-and-limits.md` | Budget and Limits | This document explains Bifrost's hierarchical budget management and rate-limiting system, detailing how costs and usage… | budget-management, cost-control, rate-limiting, virtual-keys, governance, usage-tracking |
| 092 | `092-features-governance-mcp-tools.md` | MCP Tool Filtering | This document explains how to restrict and manage access to Model Context Protocol (MCP) tools using Virtual Key config… | mcp-tools, virtual-keys, tool-filtering, access-control, governance, api-security |
| 093 | `093-features-governance-routing.md` | Routing | This document explains how to configure governance-based routing for AI models and providers using Virtual Keys to mana… | routing, virtual-keys, load-balancing, failover, ai-governance, model-management |
| 094 | `094-features-governance-virtual-keys.md` | Virtual Keys | This document explains how to use Virtual Keys as a governance entity to manage AI model access, authentication, budget… | virtual-keys, access-control, governance, rate-limiting, cost-management, api-authentication |
| 095 | `095-features-keys-management.md` | Load Balance | This document explains how to implement intelligent API key management using weighted load balancing, model-specific fi… | load-balancing, api-key-management, traffic-distribution, failover, model-filtering, bifrost |
| 096 | `096-features-litellm-compat.md` | LiteLLM Compatibility | This document explains the LiteLLM compatibility plugin, which provides automatic text-to-chat conversion and tool call… | litellm-compatibility, text-to-chat, tool-calls, api-transformation, model-interoperability, gateway-configuration |
| 097 | `097-features-observability-default.md` | Built-in Observability | This document explains Bifrost's built-in observability system, which provides real-time tracing and performance monito… | observability, request-tracing, monitoring, performance-metrics, logging, llm-ops |
| 098 | `098-features-observability-maxim.md` | Maxim AI | Explains how to integrate and configure the Maxim AI plugin with Bifrost for comprehensive LLM observability, tracing,… | maxim-ai, bifrost, llm-observability, tracing, go-sdk, configuration |
| 099 | `099-features-observability-otel.md` | OpenTelemetry (OTel) | This document explains how to integrate Bifrost with OpenTelemetry collectors to enable distributed tracing and observa… | opentelemetry, otel, distributed-tracing, observability, monitoring, tracing-plugin |
| 100 | `100-features-plugins-jsonparser.md` | JSON Parser | This document explains the Bifrost JSON Parser plugin, which automatically repairs partial JSON chunks in streaming res… | bifrost-plugin, json-parsing, streaming-responses, ai-integration, go-library, data-validation |
| 101 | `101-features-plugins-mocker.md` | Mocker | This document provides instructions for using the Mocker plugin to simulate AI provider responses, covering installatio… | ai-mocking, go, bifrost, testing, api-simulation, mocking-framework |
| 102 | `102-features-semantic-caching.md` | Semantic Caching | This document explains how to implement semantic caching using vector similarity search to reduce AI latency and API co… | semantic-caching, vector-search, ai-infrastructure, performance-optimization, weaviate, embeddings |
| 103 | `103-features-telemetry.md` | Telemetry | This document details the Prometheus-based telemetry system for Bifrost Gateway, covering HTTP transport metrics, AI pr… | prometheus, monitoring, telemetry, ai-gateway, metrics, observability |

### 6. API Reference (104–295)
*API and SDK reference*

#### API

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 104 | `104-api-reference-batch-list-batch-jobs.md` | List batch jobs | This document specifies the API endpoint for listing batch jobs from various AI providers through the Bifrost gateway. | batch-processing, ai-inference, api-reference, bifrost-gateway, multi-provider |
| 105 | `105-api-reference-files-list-files.md` | List files | This document defines the API endpoint for listing files from various AI providers through the Bifrost gateway, includi… | bifrost-api, file-management, api-endpoint, ai-gateway, openapi-spec |
| 106 | `106-api-reference-models-list-available-models.md` | List available models | This document provides the API specification for listing available AI models across multiple providers using the Bifros… | api-specification, model-listing, ai-gateway, multi-provider, bifrost-api, rest-api |
| 107 | `107-api-reference-governance-list-budgets.md` | List budgets | This document provides the API specification for listing budgets within the Bifrost governance system, including detail… | api-reference, governance, budgets, bifrost-api, resource-management |
| 108 | `108-api-reference-governance-list-customers.md` | List customers | This document specifies the GET /api/governance/customers endpoint, which retrieves a list of all customers along with… | api-reference, governance, customer-management, bifrost, json-api, endpoint-documentation |
| 109 | `109-api-reference-governance-list-rate-limits.md` | List rate limits | This document defines the API endpoint for retrieving a list of all configured rate limits and their current usage stat… | governance, rate-limiting, api-reference, usage-tracking, bifrost-api |
| 110 | `110-api-reference-governance-list-teams.md` | List teams | This document provides the technical specification for the Bifrost API endpoint used to retrieve a list of all teams, i… | bifrost-api, governance, team-management, api-endpoint, openapi-spec |
| 111 | `111-api-reference-governance-list-virtual-keys.md` | List virtual keys | This document specifies the API endpoint for retrieving a list of all virtual keys along with their configurations, pro… | governance, virtual-keys, api-endpoint, bifrost-api, access-management |
| 112 | `112-api-reference-mcp-list-mcp-clients.md` | List MCP clients | This document defines the API endpoint for retrieving a list of all configured Model Context Protocol (MCP) clients, in… | mcp, api-management, model-context-protocol, bifrost-api, client-configuration |
| 113 | `113-api-reference-plugins-list-all-plugins.md` | List all plugins | This document describes the API endpoint for retrieving a complete list of installed plugins, including their configura… | bifrost-api, plugin-management, rest-api, gateway-monitoring, plugin-configuration |
| 114 | `114-api-reference-providers-list-all-keys.md` | List all keys | Describes the API endpoint for listing all configured API keys and their associated configurations across different pro… | api-keys, provider-management, gateway-management, api-reference |
| 115 | `115-api-reference-providers-list-all-providers.md` | List all providers | This document defines the API endpoint for retrieving a list of all configured AI model providers, including their spec… | api-reference, provider-management, ai-gateway, configuration-api, model-providers |
| 116 | `116-api-reference-providers-list-models.md` | List models | This document defines the API endpoint for listing available AI models with support for filtering by provider, query st… | api-reference, model-management, bifrost-gateway, endpoint-specification, ai-models |
| 117 | `117-api-reference-anthropic-integration-list-batch-jobs-anthropic-format.md` | List batch jobs (Anthropic format) | This document specifies the API endpoint for retrieving a paginated list of batch processing jobs using the Anthropic-c… | anthropic-api, batch-processing, message-batches, api-reference, pagination |
| 118 | `118-api-reference-anthropic-integration-list-files-anthropic-format.md` | List files (Anthropic format) | This document provides the API specification for listing uploaded files using the Anthropic-compatible format within th… | anthropic-integration, file-management, list-files, bifrost-api, rest-api |
| 119 | `119-api-reference-anthropic-integration-list-models-anthropic-format.md` | List models (Anthropic format) | This document specifies the API endpoint for retrieving a list of available AI models using the Anthropic-compatible fo… | anthropic-integration, model-listing, api-specification, bifrost-gateway, ai-models |
| 120 | `120-api-reference-openai-integration-list-batch-jobs-openai-format.md` | List batch jobs (OpenAI format) | This document describes the API endpoint for listing batch processing jobs using the OpenAI-compatible format within th… | openai-integration, batch-processing, api-endpoint, bifrost-gateway, inference-api |
| 121 | `121-api-reference-openai-integration-list-files-openai-format.md` | List files (OpenAI format) | This document describes the API endpoint for listing uploaded files using the OpenAI-compatible interface provided by t… | openai-integration, file-management, api-reference, bifrost-gateway, file-listing |
| 122 | `122-api-reference-openai-integration-list-models-azure-openai.md` | List models (Azure OpenAI) | This document defines the API specification for listing models associated with a specific Azure OpenAI deployment throu… | azure-openai, bifrost-api, list-models, api-reference, model-deployment |
| 123 | `123-api-reference-openai-integration-list-models-openai-format.md` | List models (OpenAI format) | This document describes the API endpoint used to retrieve a list of available AI models in an OpenAI-compatible format… | openai-integration, model-listing, bifrost-api, api-reference, inference-gateway |
| 124 | `124-api-reference-bedrock-integration-list-batch-inference-jobs-bedrock-format.md` | List batch inference jobs (Bedrock format) | This document provides the API specification for listing batch inference jobs using the AWS Bedrock format through the… | bedrock, batch-inference, aws-bedrock, api-reference, model-invocation |
| 125 | `125-api-reference-genai-integration-list-files-gemini-format.md` | List files (Gemini format) | This document provides the API specification for listing uploaded files in the Google Gemini compatible format through… | gemini-api, file-management, google-genai, bifrost-gateway, api-integration |
| 126 | `126-api-reference-genai-integration-list-models-gemini-format.md` | List models (Gemini format) | This document defines the API endpoint for listing available AI models using the Google Gemini (GenAI) compatible forma… | gemini-api, model-listing, bifrost, genai-integration, api-reference |
| 127 | `127-api-reference-langchain-integration-list-models-langchain-gemini-format.md` | List models (LangChain - Gemini format) | This document defines the API endpoint for listing available AI models using the Google Gemini format via the LangChain… | google-gemini, langchain-integration, api-reference, model-listing, bifrost-gateway, ai-inference |
| 128 | `128-api-reference-langchain-integration-list-models-langchain-openai-format.md` | List models (LangChain - OpenAI format) | This document provides the API specification for listing available AI models using an OpenAI-compatible format designed… | langchain, openai-compatible, api-reference, model-listing, bifrost, ai-gateway |
| 129 | `129-api-reference-litellm-integration-list-models-litellm-gemini-format.md` | List models (LiteLLM - Gemini format) | This document defines the REST API endpoint for listing available AI models through the LiteLLM proxy using the Google… | litellm, gemini-api, model-listing, bifrost-api, rest-api, ai-gateway |
| 130 | `130-api-reference-litellm-integration-list-models-litellm-openai-format.md` | List models (LiteLLM - OpenAI format) | This document defines the API endpoint for retrieving a list of available AI models through the LiteLLM proxy using an… | litellm, openai-compatible, model-listing, api-gateway, bifrost-api |
| 131 | `131-api-reference-pydanticai-integration-list-models-pydanticai-gemini-format.md` | List models (PydanticAI - Gemini format) | This document specifies the API endpoint for listing available AI models through the PydanticAI framework using the Goo… | pydantic-ai, google-gemini, model-listing, bifrost-api, api-integration |
| 132 | `132-api-reference-pydanticai-integration-list-models-pydanticai-openai-format.md` | List models (PydanticAI - OpenAI format) | This document specifies the API endpoint for retrieving a list of available AI models using the PydanticAI framework in… | pydantic-ai, openai-compatible, model-listing, api-specification, bifrost-gateway |
| 133 | `133-api-reference-batch-get-batch-results.md` | Get batch results | This document provides the API specification for retrieving results from a completed batch processing job across variou… | batch-processing, api-endpoint, ai-inference, batch-results |
| 134 | `134-api-reference-configuration-get-configuration.md` | Get configuration | This document defines the GET /api/config endpoint used to retrieve the current Bifrost gateway configuration, includin… | bifrost, api-configuration, management-api, gateway-settings, ai-gateway |
| 135 | `135-api-reference-configuration-get-proxy-configuration.md` | Get proxy configuration | This document describes the API endpoint for retrieving the current global proxy configuration of the Bifrost gateway,… | api-reference, proxy-configuration, bifrost-gateway, network-settings, http-proxy, management-api |
| 136 | `136-api-reference-configuration-get-version.md` | Get version | This document specifies the API endpoint for retrieving the current version information of the Bifrost gateway service. | bifrost-api, version-endpoint, api-management, system-metadata, gateway-information |
| 137 | `137-api-reference-governance-get-customer.md` | Get customer | This document describes the API endpoint for retrieving detailed configuration and budget information for a specific cu… | governance, customer-management, api-reference, bifrost, budget-tracking |
| 138 | `138-api-reference-governance-get-team.md` | Get team | This document provides technical details for the Bifrost API endpoint used to retrieve detailed configuration and budge… | bifrost-api, governance, team-management, api-endpoint, rest-api |
| 139 | `139-api-reference-governance-get-virtual-key.md` | Get virtual key | This document provides the API specification for retrieving detailed configuration information for a specific virtual k… | api-reference, governance, virtual-keys, bifrost-api, access-management |
| 140 | `140-api-reference-logging-get-available-filter-data.md` | Get available filter data | This API endpoint retrieves unique metadata from logs, including available models and keys, to facilitate log filtering… | logging, api-reference, log-analytics, filter-data, bifrost-gateway, metadata |
| 141 | `141-api-reference-logging-get-dropped-requests-count.md` | Get dropped requests count | This document describes the API endpoint used to retrieve the total count of dropped requests from the Bifrost gateway… | bifrost-api, logging, monitoring, api-reference, dropped-requests, metrics |
| 142 | `142-api-reference-logging-get-log-statistics.md` | Get log statistics | This document specifies the API endpoint for retrieving aggregated log statistics, including request counts, token usag… | api-endpoint, log-statistics, analytics, monitoring, bifrost-api |
| 143 | `143-api-reference-logging-get-logs.md` | Get logs | This document describes the API endpoint for retrieving gateway logs with support for advanced filtering, search, and p… | logging-api, bifrost-gateway, log-management, rest-api, api-monitoring, search-parameters |
| 144 | `144-api-reference-plugins-get-a-specific-plugin.md` | Get a specific plugin | This document provides the API specification for retrieving the configuration details of a specific plugin within the B… | bifrost-api, plugin-management, openapi-spec, endpoint-reference, gateway-configuration |
| 145 | `145-api-reference-providers-get-a-specific-provider.md` | Get a specific provider | This document defines the API endpoint for retrieving configuration details, including API keys and model settings, for… | bifrost-api, provider-management, api-configuration, ai-gateway, rest-endpoint |
| 146 | `146-api-reference-anthropic-integration-get-batch-results-anthropic-format.md` | Get batch results (Anthropic format) | This document specifies the API endpoint for retrieving results from a completed batch job using the Anthropic-compatib… | anthropic-integration, batch-processing, api-reference, bifrost-gateway, inference-api, jsonl-results |
| 147 | `147-api-reference-anthropic-integration-get-file-content-anthropic-format.md` | Get file content (Anthropic format) | This document defines the API endpoint for retrieving file content or metadata using the Anthropic-compatible format, s… | anthropic-integration, file-management, api-endpoint, bifrost-gateway, binary-download |
| 148 | `148-api-reference-openai-integration-get-file-content-openai-format.md` | Get file content (OpenAI format) | This document describes the API endpoint for retrieving the binary content of an uploaded file using the OpenAI-compati… | openai-integration, file-management, api-reference, bifrost-gateway, rest-api |
| 149 | `149-api-reference-audio-create-speech.md` | Create speech | This document defines the API endpoint for converting text into speech using various AI models through a unified gatewa… | text-to-speech, audio-generation, speech-synthesis, bifrost-api, unified-inference |
| 150 | `150-api-reference-audio-create-transcription.md` | Create transcription | This document specifies the API endpoint for transcribing audio files into text using multiple AI providers through a u… | audio-transcription, speech-to-text, ai-inference, bifrost-api, rest-api |
| 151 | `151-api-reference-batch-create-a-batch-job.md` | Create a batch job | This document provides the technical specification for the Bifrost API endpoint used to create batch jobs for asynchron… | batch-processing, asynchronous-inference, api-reference, ai-models, bifrost-api, openapi-specification |
| 152 | `152-api-reference-chat-completions-create-a-chat-completion.md` | Create a chat completion | This document defines the API endpoint for generating chat completions across multiple AI providers through a unified g… | chat-completions, ai-inference, multi-provider, unified-api, openapi-specification, llm-gateway |
| 153 | `153-api-reference-embeddings-create-embeddings.md` | Create embeddings | This document specifies the API endpoint for generating embedding vectors from text or token inputs across multiple AI… | embeddings, api-reference, ai-inference, vector-generation, bifrost-gateway, nlp |
| 154 | `154-api-reference-responses-create-a-response.md` | Create a response | This document describes the Bifrost API endpoint for creating AI model responses using the OpenAI Responses format, sup… | ai-inference, openai-compatibility, streaming-sse, bifrost-api, multi-provider-gateway |
| 155 | `155-api-reference-text-completions-create-a-text-completion.md` | Create a text completion | This document provides the API specification for creating text completions via the Bifrost unified interface, supportin… | text-completions, ai-inference, api-reference, streaming-sse, unified-api, llm-gateway |
| 156 | `156-api-reference-governance-create-customer.md` | Create customer | This document specifies the API endpoint for creating a new customer within the Bifrost AI gateway, including options f… | bifrost-api, customer-management, governance, api-reference, budget-configuration |
| 157 | `157-api-reference-governance-create-team.md` | Create team | This document defines the API specification for creating a new team in the Bifrost gateway, including parameters for te… | bifrost-api, governance, team-management, api-endpoint, budget-configuration, ai-gateway |
| 158 | `158-api-reference-governance-create-virtual-key.md` | Create virtual key | This document provides the API specification for creating a virtual key, which includes configurations for provider wei… | virtual-keys, governance, api-management, rate-limiting, budget-management, ai-gateway |
| 159 | `159-api-reference-plugins-create-a-new-plugin.md` | Create a new plugin | This document defines the API endpoint and specification for creating a new plugin within the Bifrost AI gateway, inclu… | bifrost-api, plugin-management, openapi-spec, rest-api, ai-gateway |
| 160 | `160-api-reference-anthropic-integration-create-batch-job-anthropic-format.md` | Create batch job (Anthropic format) | This document provides the API specification for creating batch processing jobs using the Anthropic-compatible message… | anthropic-integration, batch-processing, api-gateway, ai-inference, message-batches |
| 161 | `161-api-reference-anthropic-integration-create-completion-anthropic-legacy-format.md` | Create completion (Anthropic legacy format) | This document defines the API endpoint for creating text completions using the legacy Anthropic format via the Bifrost… | anthropic-api, text-completion, api-gateway, legacy-format, streaming-sse, inference-api |
| 162 | `162-api-reference-anthropic-integration-create-message-anthropic-format.md` | Create message (Anthropic format) | This document defines the Bifrost API endpoint for creating messages using the Anthropic Messages API format, including… | anthropic-api, message-creation, ai-inference, streaming-sse, api-integration, bifrost-gateway |
| 163 | `163-api-reference-openai-integration-create-batch-job-openai-format.md` | Create batch job (OpenAI format) | This document specifies the API endpoint for creating batch processing jobs using the OpenAI-compatible format within t… | openai-integration, batch-processing, api-reference, bifrost, inference-gateway |
| 164 | `164-api-reference-openai-integration-create-chat-completion-azure-openai.md` | Create chat completion (Azure OpenAI) | This document provides the API specification for creating chat completions using Azure OpenAI deployments via the Bifro… | azure-openai, chat-completions, api-reference, bifrost-gateway, ai-inference, openai-integration |
| 165 | `165-api-reference-openai-integration-create-chat-completion-openai-format.md` | Create chat completion (OpenAI format) | This document provides the technical specification for the OpenAI-compatible chat completions endpoint, enabling unifie… | openai-compatibility, chat-completions, api-reference, streaming-sse, ai-inference |
| 166 | `166-api-reference-openai-integration-create-embeddings-azure-openai.md` | Create embeddings (Azure OpenAI) | This document provides the OpenAPI specification for the Azure OpenAI embedding endpoint within the Bifrost API gateway… | azure-openai, embeddings, api-reference, bifrost-api, text-processing |
| 167 | `167-api-reference-openai-integration-create-embeddings-openai-format.md` | Create embeddings (OpenAI format) | This document provides technical specifications for the OpenAI-compatible embeddings endpoint, detailing how to create… | openai-integration, embeddings, api-reference, vector-generation, text-processing |
| 168 | `168-api-reference-openai-integration-create-image-azure-openai.md` | Create image (Azure OpenAI) | This document specifies the API endpoint for generating images from text prompts using Azure OpenAI deployments through… | azure-openai, image-generation, api-reference, bifrost, dall-e |
| 169 | `169-api-reference-openai-integration-create-image.md` | Create image | This document provides the API specification for generating images from text prompts using an OpenAI-compatible endpoin… | openai-api, image-generation, text-to-image, ai-inference, api-reference, bifrost |
| 170 | `170-api-reference-openai-integration-create-response-azure-openai.md` | Create response (Azure OpenAI) | This document provides the OpenAPI specification for creating responses through Azure OpenAI deployments using the Bifr… | azure-openai, bifrost-api, api-reference, ai-inference, openai-integration |
| 171 | `171-api-reference-openai-integration-create-response-openai-responses-api.md` | Create response (OpenAI Responses API) | This document defines the API endpoint for creating responses using the OpenAI Responses API format, supporting both st… | openai-integration, responses-api, ai-inference, streaming-sse, bifrost-api, rest-api |
| 172 | `172-api-reference-openai-integration-create-speech-azure-openai-tts.md` | Create speech (Azure OpenAI TTS) | This document defines the OpenAPI specification for generating audio from text using the Azure OpenAI Text-to-Speech (T… | azure-openai, text-to-speech, api-specification, speech-synthesis, audio-generation |
| 173 | `173-api-reference-openai-integration-create-speech-openai-tts.md` | Create speech (OpenAI TTS) | This document defines the OpenAI-compatible text-to-speech endpoint for converting text into audio, supporting various… | openai-tts, text-to-speech, audio-generation, speech-synthesis, api-endpoint, streaming-audio |
| 174 | `174-api-reference-openai-integration-create-text-completion-azure-openai.md` | Create text completion (Azure OpenAI) | This document provides the API specification for generating text completions using Azure OpenAI deployments through the… | azure-openai, text-completions, openapi-spec, ai-inference, bifrost-gateway |
| 175 | `175-api-reference-openai-integration-create-text-completion-openai-format.md` | Create text completion (OpenAI format) | This document provides the specification for the OpenAI-compatible legacy text completions API endpoint used to generat… | openai-compatible, text-completion, api-reference, inference, bifrost-gateway |
| 176 | `176-api-reference-openai-integration-create-transcription-azure-openai.md` | Create transcription (Azure OpenAI) | This document defines the API endpoint for transcribing audio files using Azure OpenAI models through the Bifrost gatew… | azure-openai, transcription, audio-processing, speech-to-text, api-endpoint, bifrost |
| 177 | `177-api-reference-openai-integration-create-transcription-openai-whisper.md` | Create transcription (OpenAI Whisper) | This document provides technical specifications for the OpenAI Whisper transcription endpoint, which enables converting… | openai-whisper, audio-transcription, speech-to-text, api-endpoint, bifrost-gateway |
| 178 | `178-api-reference-bedrock-integration-create-batch-inference-job-bedrock-format.md` | Create batch inference job (Bedrock format) | This document defines the API specification for creating batch inference jobs using the AWS Bedrock format within the B… | aws-bedrock, batch-inference, api-endpoint, model-invocation, bifrost-api |
| 179 | `179-api-reference-langchain-integration-create-embeddings-langchain-cohere-format.md` | Create embeddings (LangChain - Cohere format) | This document specifies the API endpoint for generating text and multimodal embeddings using the LangChain framework in… | langchain, cohere, embeddings, api-reference, multimodal, text-processing |
| 180 | `180-api-reference-langchain-integration-create-embeddings-langchain-openai-format.md` | Create embeddings (LangChain - OpenAI format) | This document specifies the API endpoint for generating text embeddings using an OpenAI-compatible format optimized for… | langchain, openai-compatible, embeddings, api-specification, bifrost, ai-inference |
| 181 | `181-api-reference-langchain-integration-create-message-langchain-anthropic-format.md` | Create message (LangChain - Anthropic format) | This document defines the API specification for creating messages using the Anthropic-compatible format via LangChain w… | langchain, anthropic, chat-completions, api-gateway, ai-inference |
| 182 | `182-api-reference-langchain-integration-create-response-langchain-openai-responses-api.md` | Create response (LangChain - OpenAI Responses API) | This document specifies the API endpoint for creating AI model responses using the OpenAI format via LangChain, support… | langchain, openai-api, inference-gateway, rest-api, streaming-sse, bifrost-api |
| 183 | `183-api-reference-langchain-integration-create-speech-langchain-openai-tts.md` | Create speech (LangChain - OpenAI TTS) | This document specifies the LangChain-compatible API endpoint for converting text to audio using OpenAI's Text-to-Speec… | langchain, openai-tts, text-to-speech, speech-synthesis, api-endpoint |
| 184 | `184-api-reference-langchain-integration-create-transcription-langchain-openai-whisper.md` | Create transcription (LangChain - OpenAI Whisper) | This document specifies the API endpoint for transcribing audio into text using OpenAI Whisper via the LangChain framew… | langchain, openai-whisper, audio-transcription, speech-to-text, api-reference |
| 185 | `185-api-reference-litellm-integration-create-embeddings-litellm-cohere-format.md` | Create embeddings (LiteLLM - Cohere format) | This document specifies the API endpoint for generating text and multimodal embeddings using the Cohere-compatible form… | litellm, cohere, embeddings, api-proxy, multimodal-embeddings |
| 186 | `186-api-reference-litellm-integration-create-embeddings-litellm-openai-format.md` | Create embeddings (LiteLLM - OpenAI format) | Provides the API specification for generating text embeddings using an OpenAI-compatible format through the LiteLLM pro… | embeddings, litellm, openai-format, api-reference, bifrost |
| 187 | `187-api-reference-litellm-integration-create-message-litellm-anthropic-format.md` | Create message (LiteLLM - Anthropic format) | This document specifies the API endpoint for creating messages using the Anthropic-compatible format through the LiteLL… | litellm, anthropic-format, message-creation, api-integration, ai-inference, bifrost-api |
| 188 | `188-api-reference-litellm-integration-create-response-litellm-openai-responses-api.md` | Create response (LiteLLM - OpenAI Responses API) | This document defines the API endpoint for generating model responses using the LiteLLM proxy with OpenAI-compatible fo… | litellm, openai-responses, api-gateway, inference, streaming-sse |
| 189 | `189-api-reference-litellm-integration-create-speech-litellm-openai-tts.md` | Create speech (LiteLLM - OpenAI TTS) | This document provides the API specification for converting text into audio using OpenAI's Text-to-Speech models throug… | litellm, text-to-speech, openai-tts, api-reference, audio-generation |
| 190 | `190-api-reference-litellm-integration-create-transcription-litellm-openai-whisper.md` | Create transcription (LiteLLM - OpenAI Whisper) | This document provides the API specification for transcribing audio files into text using the OpenAI Whisper model thro… | audio-transcription, litellm, openai-whisper, speech-to-text, api-endpoint |
| 191 | `191-api-reference-pydanticai-integration-create-embeddings-pydanticai-cohere-format.md` | Create embeddings (PydanticAI - Cohere format) | This document defines the API specification for generating text and multimodal embeddings using a Cohere-compatible for… | pydantic-ai, cohere, embeddings, api-reference, multimodal, bifrost-gateway |
| 192 | `192-api-reference-pydanticai-integration-create-embeddings-pydanticai-openai-format.md` | Create embeddings (PydanticAI - OpenAI format) | This document specifies the API endpoint for creating text embeddings using the PydanticAI framework in an OpenAI-compa… | embeddings, pydanticai, openai-compatible, api-endpoint, text-processing |
| 193 | `193-api-reference-pydanticai-integration-create-message-pydanticai-anthropic-format.md` | Create message (PydanticAI - Anthropic format) | This document defines the API endpoint for creating messages using an Anthropic-compatible format through the PydanticA… | pydantic-ai, anthropic, api-gateway, message-creation, ai-inference, framework-integration |
| 194 | `194-api-reference-pydanticai-integration-create-response-pydanticai-openai-responses-api.md` | Create response (PydanticAI - OpenAI Responses API) | This document defines the API endpoint for generating AI model responses using the PydanticAI framework with compatibil… | pydantic-ai, openai-responses, ai-inference, api-gateway, sse-streaming, bifrost-api |
| 195 | `195-api-reference-pydanticai-integration-create-speech-pydanticai-openai-tts.md` | Create speech (PydanticAI - OpenAI TTS) | This document provides the OpenAPI specification for the PydanticAI-compatible endpoint used to generate audio from tex… | pydanticai, openai-tts, text-to-speech, api-specification, audio-generation, bifrost-api |
| 196 | `196-api-reference-pydanticai-integration-create-transcription-pydanticai-openai-whisper.md` | Create transcription (PydanticAI - OpenAI Whisper) | This document provides the OpenAPI specification for the PydanticAI-compatible endpoint used to transcribe audio files… | pydanticai, openai-whisper, audio-transcription, speech-to-text, api-specification, bifrost-gateway |
| 197 | `197-api-reference-configuration-update-configuration.md` | Update configuration | This document details the API endpoint for updating the Bifrost gateway configuration, supporting both hot-reloadable a… | bifrost, api-configuration, gateway-management, hot-reloading, inference-gateway, configuration-management |
| 198 | `198-api-reference-configuration-update-proxy-configuration.md` | Update proxy configuration | This document provides the API specification for updating the global proxy settings of the Bifrost gateway, including p… | bifrost-api, proxy-configuration, gateway-management, network-settings, http-proxy |
| 199 | `199-api-reference-governance-update-customer.md` | Update customer | This document provides the API specification for updating an existing customer's details, including their name and budg… | bifrost-api, customer-management, governance, api-endpoint, budget-configuration, http-put |
| 200 | `200-api-reference-governance-update-team.md` | Update team | This document provides the API specification for updating an existing team's information, including its name, customer… | bifrost-api, governance, team-management, budget-configuration, api-endpoint |
| 201 | `201-api-reference-governance-update-virtual-key.md` | Update virtual key | This document describes the API endpoint for updating the configuration of an existing virtual key, including its provi… | governance, virtual-keys, api-management, rate-limiting, budget-management, bifrost-api |
| 202 | `202-api-reference-plugins-update-a-plugin.md` | Update a plugin | This document defines the API endpoint for updating a plugin's configuration, which manages the plugin's enabled status… | plugins, api-endpoint, configuration-management, bifrost-api, gateway-management |
| 203 | `203-api-reference-providers-update-a-provider.md` | Update a provider | This document describes the API endpoint for updating a provider's configuration in the Bifrost gateway, requiring a fu… | bifrost-api, provider-management, api-reference, configuration-update, ai-gateway |
| 204 | `204-api-reference-files-delete-a-file.md` | Delete a file | This document defines the API endpoint for deleting a specific file from a supported AI provider via the Bifrost gatewa… | file-management, delete-file, api-endpoint, bifrost-api, ai-gateway |
| 205 | `205-api-reference-governance-delete-customer.md` | Delete customer | This document details the API endpoint for deleting a customer within the Bifrost governance framework using a specific… | bifrost-api, governance, customer-management, delete-operation, api-endpoint |
| 206 | `206-api-reference-governance-delete-team.md` | Delete team | This document provides the API specification for deleting a team from the Bifrost governance system using a specific te… | bifrost-api, governance, team-management, delete-team, rest-api |
| 207 | `207-api-reference-governance-delete-virtual-key.md` | Delete virtual key | This document specifies the API endpoint for deleting a virtual key within the Bifrost governance system using a unique… | bifrost-api, governance, virtual-keys, api-management, delete-endpoint, key-management |
| 208 | `208-api-reference-logging-delete-logs.md` | Delete logs | This document defines the API endpoint for deleting logs by their unique identifiers within the Bifrost gateway managem… | bifrost-api, log-management, api-endpoint, management-api, openapi-specification |
| 209 | `209-api-reference-plugins-delete-a-plugin.md` | Delete a plugin | This document specifies the API endpoint for removing a plugin from the Bifrost configuration and stopping its executio… | bifrost-api, plugin-management, gateway-configuration, api-endpoint |
| 210 | `210-api-reference-providers-delete-a-provider.md` | Delete a provider | This document specifies the API endpoint for removing an AI model provider from the Bifrost gateway configuration. | provider-management, api-gateway, configuration-api, delete-endpoint, bifrost-api |
| 211 | `211-api-reference-anthropic-integration-delete-file-anthropic-format.md` | Delete file (Anthropic format) | This document provides the OpenAPI specification and endpoint details for deleting an uploaded file through the Bifrost… | anthropic-integration, file-management, api-endpoint, bifrost-gateway, delete-file, openapi-spec |
| 212 | `212-api-reference-openai-integration-delete-file-openai-format.md` | Delete file (OpenAI format) | This document describes the API endpoint for deleting uploaded files using an OpenAI-compatible format within the Bifro… | openai-integration, file-management, api-reference, bifrost-gateway, file-deletion |
| 213 | `213-api-reference-genai-integration-delete-file-gemini-format.md` | Delete file (Gemini format) | This document specifies the API endpoint for deleting files in Google Gemini format through the Bifrost gateway. It det… | gemini-api, file-management, bifrost-gateway, genai-integration, api-endpoint |
| 214 | `214-api-reference-cohere-integration-chat-with-model-cohere-v2-format.md` | Chat with model (Cohere v2 format) | This document provides the API specification for sending chat completion requests using the Cohere v2 format through th… | cohere-api, chat-completion, ai-gateway, bifrost-api, api-integration, llm-inference |
| 215 | `215-api-reference-cohere-integration-create-embeddings-cohere-v2-format.md` | Create embeddings (Cohere v2 format) | This document provides the API specification for generating text and multimodal embeddings using the Cohere v2 compatib… | cohere-v2, embeddings, api-reference, bifrost-gateway, multimodal-ai |
| 216 | `216-api-reference-batch-retrieve-a-batch-job.md` | Retrieve a batch job | This document defines the API endpoint for retrieving the status and detailed information of a specific batch job using… | batch-processing, api-endpoint, job-retrieval, ai-gateway, bifrost |
| 217 | `217-api-reference-batch-cancel-a-batch-job.md` | Cancel a batch job | This document specifies the API endpoint and parameters required to cancel an ongoing batch job within the Bifrost gate… | bifrost-api, batch-processing, job-cancellation, ai-gateway, api-reference, batch-management |
| 218 | `218-api-reference-cache-clear-cache-by-cache-key.md` | Clear cache by cache key | This document defines the API endpoint for clearing a specific cache entry from the Bifrost gateway using its unique ca… | cache-management, api-endpoint, delete-method, bifrost-gateway, cache-key |
| 219 | `219-api-reference-cache-clear-cache-by-request-id.md` | Clear cache by request ID | This document provides the OpenAPI specification for an endpoint that allows users to delete cache entries associated w… | cache-management, api-endpoint, request-id, bifrost-gateway, data-cleanup |
| 220 | `220-api-reference-count-tokens-count-tokens.md` | Count tokens | This document provides the API specification for counting tokens in messages across various AI models using the Bifrost… | token-counting, api-specification, bifrost-api, ai-inference, token-usage, message-processing |
| 221 | `221-api-reference-files-download-file-content.md` | Download file content | This document describes the API endpoint used to retrieve and download the raw binary content of a file stored with a s… | api-endpoint, file-management, file-download, bifrost-api, ai-gateway |
| 222 | `222-api-reference-files-retrieve-file-metadata.md` | Retrieve file metadata | This document details the API endpoint for retrieving metadata and status information for a specific file across multip… | api-reference, file-management, metadata-retrieval, bifrost-api, unified-interface |
| 223 | `223-api-reference-files-upload-a-file.md` | Upload a file | This document describes the API endpoint for uploading files to the Bifrost gateway to be used in batch operations, fin… | file-upload, bifrost-api, api-endpoint, batch-operations, multipart-form-data, ai-infrastructure |
| 224 | `224-api-reference-health-health-check.md` | Health check | This document describes the Bifrost health check endpoint, which verifies the server's operational status and its conne… | health-check, api-monitoring, server-status, diagnostics, bifrost-gateway |
| 225 | `225-api-reference-image-generations-generate-image.md` | Generate image | This document specifies the API endpoint for generating images from text prompts using various AI providers via the Bif… | image-generation, text-to-image, bifrost-api, api-endpoint, multi-provider, ai-inference |
| 226 | `226-api-reference-configuration-force-pricing-sync.md` | Force pricing sync | This document describes the API endpoint used to manually trigger an immediate synchronization of pricing data and rese… | bifrost-api, pricing-sync, configuration-management, api-endpoint, gateway-administration |
| 227 | `227-api-reference-logging-recalculate-log-costs.md` | Recalculate log costs | This document defines an API endpoint for recomputing missing log costs in batches using current pricing data and vario… | logging, cost-management, batch-processing, api-reference, bifrost-api |
| 228 | `228-api-reference-mcp-add-mcp-client.md` | Add MCP client | This document defines the API endpoint for adding and configuring Model Context Protocol (MCP) clients within the Bifro… | mcp-client, model-context-protocol, api-endpoint, bifrost-gateway, configuration-management |
| 229 | `229-api-reference-mcp-edit-mcp-client.md` | Edit MCP client | This document provides the API specification for updating an existing Model Context Protocol (MCP) client configuration… | mcp, api-reference, model-context-protocol, client-configuration, bifrost-gateway, endpoint-update |
| 230 | `230-api-reference-mcp-execute-mcp-tool.md` | Execute MCP tool | This document defines the API endpoint for executing Model Context Protocol (MCP) tools and retrieving results using ch… | mcp, tool-execution, api-reference, model-context-protocol, bifrost-api |
| 231 | `231-api-reference-mcp-reconnect-mcp-client.md` | Reconnect MCP client | This document specifies the API endpoint for reconnecting a Model Context Protocol (MCP) client that has encountered an… | mcp-client, api-endpoint, reconnect, bifrost-api, model-context-protocol |
| 232 | `232-api-reference-mcp-remove-mcp-client.md` | Remove MCP client | This document provides the technical specification for the API endpoint used to remove a Model Context Protocol (MCP) c… | mcp, mcp-client, api-management, bifrost, delete-endpoint |
| 233 | `233-api-reference-providers-add-a-new-provider.md` | Add a new provider | This document describes the API endpoint for adding and configuring a new AI model provider within the Bifrost gateway… | api-management, provider-configuration, ai-gateway, endpoint-reference, infrastructure |
| 234 | `234-api-reference-session-check-if-authentication-is-enabled.md` | Check if authentication is enabled | This document describes an API endpoint used to verify if authentication is enabled for the Bifrost gateway and check t… | authentication, session-management, api-endpoint, token-validation, security, bifrost-gateway |
| 235 | `235-api-reference-session-login.md` | Login | This document defines the login endpoint for the Bifrost API, detailing how to authenticate users and obtain session to… | authentication, session-management, bifrost-api, login-endpoint, security |
| 236 | `236-api-reference-session-logout.md` | Logout | This document defines the API endpoint for logging out a user and invalidating their current session token within the B… | session-management, authentication, api-endpoint, user-logout, security, bifrost |
| 237 | `237-api-reference-anthropic-integration-retrieve-batch-job-anthropic-format.md` | Retrieve batch job (Anthropic format) | This document provides the API specification for retrieving the status and details of a batch processing job using the… | anthropic-integration, batch-processing, api-reference, inference-gateway, message-batches |
| 238 | `238-api-reference-anthropic-integration-cancel-batch-job-anthropic-format.md` | Cancel batch job (Anthropic format) | This document provides details for the API endpoint used to cancel an active batch processing job within the Anthropic-… | anthropic, batch-processing, api-endpoint, job-cancellation, message-batches |
| 239 | `239-api-reference-anthropic-integration-count-tokens-anthropic-format.md` | Count tokens (Anthropic format) | This document specifies the API endpoint for calculating the number of tokens in a message request using the Anthropic-… | anthropic, token-counting, api-integration, bifrost-gateway, llm-utilities |
| 240 | `240-api-reference-anthropic-integration-upload-file-anthropic-format.md` | Upload file (Anthropic format) | This document defines the API endpoint for uploading files using the Anthropic-compatible format through the Bifrost ga… | anthropic-integration, file-upload, api-endpoint, bifrost-gateway, multipart-form-data |
| 241 | `241-api-reference-openai-integration-retrieve-batch-job-openai-format.md` | Retrieve batch job (OpenAI format) | This document specifies the API endpoint for retrieving detailed information and status of a batch processing job using… | openai-integration, batch-processing, api-reference, bifrost-gateway, batch-retrieval |
| 242 | `242-api-reference-openai-integration-cancel-batch-job-openai-format.md` | Cancel batch job (OpenAI format) | This document describes the API endpoint for canceling an active batch processing job using the OpenAI-compatible inter… | openai-integration, batch-processing, api-endpoint, bifrost-gateway, job-management |
| 243 | `243-api-reference-openai-integration-count-input-tokens.md` | Count input tokens | This document describes an API endpoint for counting the number of tokens in an OpenAI-compatible Responses API request… | token-counting, openai-compatibility, bifrost-api, api-reference, input-tokens |
| 244 | `244-api-reference-openai-integration-retrieve-file-metadata-openai-format.md` | Retrieve file metadata (OpenAI format) | This document describes the API endpoint for retrieving metadata for an uploaded file using the OpenAI-compatible forma… | openai-integration, file-management, api-reference, metadata-retrieval, bifrost-api |
| 245 | `245-api-reference-openai-integration-upload-file-openai-format.md` | Upload file (OpenAI format) | This document specifies the API endpoint for uploading files in an OpenAI-compatible format to be used for batch proces… | openai-integration, file-upload, api-reference, batch-processing, bifrost-api, cloud-storage |
| 246 | `246-api-reference-bedrock-integration-retrieve-batch-inference-job-bedrock-format.md` | Retrieve batch inference job (Bedrock format) | This document specifies the API endpoint for retrieving the details and status of a batch inference job using the AWS B… | bedrock-integration, batch-inference, api-reference, aws-bedrock, job-management |
| 247 | `247-api-reference-bedrock-integration-cancel-batch-inference-job-bedrock-format.md` | Cancel batch inference job (Bedrock format) | This document specifies the API endpoint for cancelling an active batch inference job using the AWS Bedrock-compatible… | bedrock-integration, batch-inference, job-management, api-endpoint, bifrost-ai |
| 248 | `248-api-reference-bedrock-integration-converse-with-model-bedrock-format.md` | Converse with model (Bedrock format) | This document defines the API specification for interacting with AI models through the Bifrost gateway using the AWS Be… | bedrock-integration, aws-bedrock, converse-api, ai-inference, bifrost-api, api-endpoint |
| 249 | `249-api-reference-bedrock-integration-invoke-model-bedrock-format.md` | Invoke model (Bedrock format) | This document describes the Bifrost API endpoint for invoking AI models using the AWS Bedrock InvokeModel format, allow… | aws-bedrock, model-inference, api-reference, llm-gateway, rest-api |
| 250 | `250-api-reference-bedrock-integration-invoke-model-with-streaming-bedrock-format.md` | Invoke model with streaming (Bedrock format) | This document defines the API endpoint for invoking AI models with streaming responses using the AWS Bedrock InvokeMode… | bedrock-integration, streaming-api, ai-inference, openapi-spec, aws-bedrock, model-invocation |
| 251 | `251-api-reference-bedrock-integration-stream-converse-with-model-bedrock-format.md` | Stream converse with model (Bedrock format) | This document defines the API endpoint for streaming chat completions using the AWS Bedrock Converse format through the… | aws-bedrock, streaming-api, chat-completions, ai-inference, bifrost-gateway, api-integration |
| 252 | `252-api-reference-genai-integration-count-tokens-gemini-format.md` | Count tokens (Gemini format) | This document provides the OpenAPI specification for the Google Gemini-compatible token counting endpoint within the Bi… | gemini-api, token-counting, google-genai, bifrost-gateway, llm-utilities, api-specification |
| 253 | `253-api-reference-genai-integration-embed-content-gemini-format.md` | Embed content (Gemini format) | This document provides the OpenAPI specification for the Google Gemini-compatible embedding endpoint within the Bifrost… | gemini-api, embeddings, bifrost-gateway, google-genai, openapi-spec, vector-embeddings |
| 254 | `254-api-reference-genai-integration-retrieve-file-gemini-format.md` | Retrieve file (Gemini format) | This document describes the API endpoint for retrieving file metadata in the Google Gemini format through the Bifrost g… | gemini-api, file-management, metadata-retrieval, google-genai, api-integration |
| 255 | `255-api-reference-genai-integration-generate-content-gemini-format.md` | Generate content (Gemini format) | This document specifies the API endpoint for generating content through the Google Gemini-compatible interface within t… | gemini-api, google-genai, content-generation, api-integration, bifrost-gateway, inference-api |
| 256 | `256-api-reference-genai-integration-generate-image-gemini-format.md` | Generate image (Gemini format) | This document defines the API specification for generating images using Google's Gemini and Imagen models through the B… | gemini, imagen, image-generation, bifrost-api, google-genai, api-reference |
| 257 | `257-api-reference-genai-integration-stream-generate-content-gemini-format.md` | Stream generate content (Gemini format) | This document defines the OpenAPI specification for streaming content generation using the Google Gemini-compatible end… | gemini-api, streaming-content, ai-gateway, openapi-specification, google-genai, content-generation |
| 258 | `258-api-reference-genai-integration-upload-file-gemini-format.md` | Upload file (Gemini format) | This document describes the API endpoint for uploading files to Google Gemini via the Bifrost gateway using a multipart… | google-gemini, file-upload, multipart-upload, genai-integration, bifrost-api |
| 259 | `259-api-reference-cohere-integration-tokenize-text-cohere-format.md` | Tokenize text (Cohere format) | This document provides the API specification for tokenizing text using the Cohere-compatible endpoint within the Bifros… | cohere-integration, tokenization, api-reference, text-processing, bifrost-gateway |
| 260 | `260-api-reference-langchain-integration-chat-completions-langchain-openai-format.md` | Chat completions (LangChain - OpenAI format) | This document defines the API endpoint for generating chat completions via the LangChain framework using an OpenAI-comp… | langchain-integration, openai-compatibility, chat-completions, ai-inference, rest-api |
| 261 | `261-api-reference-langchain-integration-chat-with-model-langchain-cohere-format.md` | Chat with model (LangChain - Cohere format) | This document specifies the API endpoint for performing chat completions using the Cohere-compatible format via LangCha… | langchain, cohere, chat-completions, api-gateway, ai-inference |
| 262 | `262-api-reference-langchain-integration-converse-with-model-langchain-bedrock-format.md` | Converse with model (LangChain - Bedrock format) | This document provides the API specification for a LangChain-compatible endpoint that facilitates model interactions us… | langchain, aws-bedrock, converse-api, inference, api-integration |
| 263 | `263-api-reference-langchain-integration-count-input-tokens-langchain-openai-format.md` | Count input tokens (LangChain - OpenAI format) | This document defines an API endpoint for counting the number of input tokens in requests using the LangChain-OpenAI fo… | langchain-integration, openai-format, token-counting, input-tokens, api-specification, bifrost-gateway |
| 264 | `264-api-reference-langchain-integration-count-tokens-langchain-anthropic-format.md` | Count tokens (LangChain - Anthropic format) | This document provides the OpenAPI specification for an endpoint that counts tokens in messages using the Anthropic-com… | langchain, anthropic, token-counting, api-reference, bifrost |
| 265 | `265-api-reference-langchain-integration-generate-content-langchain-gemini-format.md` | Generate content (LangChain - Gemini format) | This document specifies the API endpoint for generating content using the Google Gemini format through the LangChain fr… | langchain-integration, google-gemini, api-specification, content-generation, ai-gateway, bifrost-api |
| 266 | `266-api-reference-langchain-integration-stream-converse-with-model-langchain-bedrock-format.md` | Stream converse with model (LangChain - Bedrock format) | This document defines an API endpoint for streaming conversational model responses using the AWS Bedrock Converse forma… | langchain, aws-bedrock, streaming-api, ai-inference, converse-stream |
| 267 | `267-api-reference-langchain-integration-stream-generate-content-langchain-gemini-format.md` | Stream generate content (LangChain - Gemini format) | This document defines the OpenAPI specification for streaming content generation using the Google Gemini-compatible for… | langchain, gemini, streaming, content-generation, api-reference, google-genai |
| 268 | `268-api-reference-langchain-integration-text-completions-langchain-openai-format.md` | Text completions (LangChain - OpenAI format) | This document specifies the legacy text completions API endpoint designed for LangChain integration using an OpenAI-com… | langchain, openai-compatible, text-completions, api-reference, legacy-api |
| 269 | `269-api-reference-langchain-integration-tokenize-text-langchain-cohere-format.md` | Tokenize text (LangChain - Cohere format) | This document provides the API specification for tokenizing text strings into token IDs and strings using Cohere-compat… | langchain, cohere, tokenization, api-reference, bifrost-gateway, text-processing |
| 270 | `270-api-reference-litellm-integration-chat-completions-litellm-openai-format.md` | Chat completions (LiteLLM - OpenAI format) | This document specifies the OpenAPI definition for the LiteLLM-compatible chat completion endpoint within the Bifrost A… | litellm, chat-completions, openai-format, api-gateway, inference-api |
| 271 | `271-api-reference-litellm-integration-chat-with-model-litellm-cohere-format.md` | Chat with model (LiteLLM - Cohere format) | This document specifies the API endpoint for performing chat completions using the Cohere-compatible format via the Lit… | litellm, cohere, chat-completion, api-gateway, ai-inference, multi-provider |
| 272 | `272-api-reference-litellm-integration-converse-with-model-litellm-bedrock-format.md` | Converse with model (LiteLLM - Bedrock format) | This document provides the API specification for interacting with AI models using the AWS Bedrock Converse format via t… | litellm, aws-bedrock, api-specification, ai-inference, converse-api, bifrost-gateway |
| 273 | `273-api-reference-litellm-integration-count-input-tokens-litellm-openai-format.md` | Count input tokens (LiteLLM - OpenAI format) | This document defines an API endpoint for calculating the number of input tokens in a LiteLLM-compatible OpenAI request… | litellm, openai-format, token-counting, api-specification, bifrost-api, inference-gateway |
| 274 | `274-api-reference-litellm-integration-generate-content-litellm-gemini-format.md` | Generate content (LiteLLM - Gemini format) | This document defines the API endpoint for generating AI content using the Google Gemini-compatible format through the… | litellm, google-gemini, content-generation, api-reference, ai-inference |
| 275 | `275-api-reference-litellm-integration-stream-converse-with-model-litellm-bedrock-format.md` | Stream converse with model (LiteLLM - Bedrock format) | This document provides the OpenAPI specification for streaming AI model conversations via the LiteLLM integration using… | litellm, aws-bedrock, streaming-api, converse-stream, ai-inference, openapi-spec |
| 276 | `276-api-reference-litellm-integration-stream-generate-content-litellm-gemini-format.md` | Stream generate content (LiteLLM - Gemini format) | This document provides the OpenAPI specification for streaming content generation using the Google Gemini-compatible fo… | litellm, google-gemini, streaming-api, openapi-spec, ai-inference, content-generation |
| 277 | `277-api-reference-litellm-integration-text-completions-litellm-openai-format.md` | Text completions (LiteLLM - OpenAI format) | This document defines the legacy OpenAI-compatible text completions endpoint provided via LiteLLM for multi-provider AI… | litellm, openai-format, text-completions, api-gateway, inference-api |
| 278 | `278-api-reference-litellm-integration-tokenize-text-litellm-cohere-format.md` | Tokenize text (LiteLLM - Cohere format) | This document specifies the API endpoint for tokenizing text using the Cohere-compatible format via the LiteLLM integra… | litellm, cohere, tokenization, api-reference, bifrost-api, text-processing |
| 279 | `279-api-reference-pydanticai-integration-chat-completions-pydanticai-openai-format.md` | Chat completions (PydanticAI - OpenAI format) | This document provides the OpenAPI specification for the PydanticAI-compatible chat completions endpoint, enabling Open… | pydanticai, chat-completions, openai-compatible, bifrost-api, inference, api-specification |
| 280 | `280-api-reference-pydanticai-integration-chat-with-model-pydanticai-cohere-format.md` | Chat with model (PydanticAI - Cohere format) | This document provides the API specification for performing chat completions using the Cohere-compatible format through… | pydanticai, cohere, chat-completions, ai-inference, api-gateway, bifrost |
| 281 | `281-api-reference-pydanticai-integration-converse-with-model-pydanticai-bedrock-format.md` | Converse with model (PydanticAI - Bedrock format) | This API endpoint enables model interaction by sending messages in an AWS Bedrock Converse-compatible format via the Py… | pydanticai, aws-bedrock, model-inference, converse-api, api-integration, bifrost-gateway |
| 282 | `282-api-reference-pydanticai-integration-count-input-tokens-pydanticai-openai-format.md` | Count input tokens (PydanticAI - OpenAI format) | This document defines the API endpoint for counting input tokens in a PydanticAI-compatible Responses request within th… | pydanticai, token-counting, openai-format, api-reference, bifrost-api |
| 283 | `283-api-reference-pydanticai-integration-generate-content-pydanticai-gemini-format.md` | Generate content (PydanticAI - Gemini format) | This document defines the OpenAPI specification for generating content using the Google Gemini-compatible format throug… | pydanticai, google-gemini, content-generation, openapi, ai-inference, bifrost |
| 284 | `284-api-reference-pydanticai-integration-stream-converse-with-model-pydanticai-bedrock-format.md` | Stream converse with model (PydanticAI - Bedrock format) | This document provides the OpenAPI specification for streaming model conversations using the AWS Bedrock Converse forma… | pydanticai, aws-bedrock, streaming-api, openapi-spec, conversational-ai |
| 285 | `285-api-reference-pydanticai-integration-stream-generate-content-pydanticai-gemini-format.md` | Stream generate content (PydanticAI - Gemini format) | This document provides the OpenAPI specification for the PydanticAI integration endpoint that enables streaming content… | openapi, pydanticai, gemini, streaming-api, ai-inference, content-generation |
| 286 | `286-api-reference-pydanticai-integration-text-completions-pydanticai-openai-format.md` | Text completions (PydanticAI - OpenAI format) | This document defines the PydanticAI-compatible endpoint for generating text completions using the legacy OpenAI-compat… | pydanticai, openai-compatible, text-completions, api-gateway, legacy-api |
| 287 | `287-api-reference-pydanticai-integration-tokenize-text-pydanticai-cohere-format.md` | Tokenize text (PydanticAI - Cohere format) | This document defines the OpenAPI specification for tokenizing text using the Cohere v1 API format through the Pydantic… | pydanticai, cohere, tokenization, api-reference, bifrost-gateway |

#### Providers

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 288 | `288-providers-supported-providers-overview.md` | Overview | This document provides an overview of Bifrost's unified OpenAI-compatible interface and a detailed support matrix for v… | ai-providers, openai-compatibility, api-gateway, feature-matrix, multi-model-support, integrations |
| 289 | `289-providers-reasoning.md` | Reasoning | Provides a cross-provider reference for implementing reasoning and thinking capabilities in AI models through a normali… | reasoning-capabilities, ai-providers, api-normalization, configuration, llm-parameters |
| 290 | `290-providers-supported-providers-cerebras.md` | Cerebras | This document outlines the integration of the Cerebras API into an OpenAI-compatible framework, detailing supported fea… | cerebras, openai-compatibility, chat-completions, streaming, tool-calling, api-integration |
| 291 | `291-providers-supported-providers-mistral.md` | Mistral | This document provides a technical guide for converting OpenAI-formatted requests to the Mistral API, detailing paramet… | mistral-ai, api-conversion, openai-compatibility, chat-completions, tool-calling, audio-transcription |
| 292 | `292-providers-supported-providers-openai.md` | OpenAI | This document outlines the integration of OpenAI's API with Bifrost, detailing supported operations, endpoints, and spe… | openai, bifrost, api-reference, chat-completions, api-integration, request-parameters |

#### Other

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 293 | `293-architecture-framework-config-store.md` | Config Store | This document explains the Bifrost ConfigStore, a persistent configuration management system that provides a unified AP… | bifrost, config-store, configuration-management, database-backend, postgresql, sqlite |
| 294 | `294-benchmarking-t3.medium.md` | t3.medium | This document provides performance benchmarks, resource utilization metrics, and configuration tuning recommendations f… | aws-t3-medium, performance-benchmarks, latency-analysis, resource-utilization, bifrost-optimization, ec2-performance |
| 295 | `295-benchmarking-t3.xl.md` | t3.xlarge | This document provides detailed performance benchmarks and resource utilization analysis for running Bifrost on AWS t3.… | aws-t3-xlarge, performance-benchmarks, bifrost-optimization, scalability-analysis, infrastructure-tuning, latency-metrics |

### 7. Changelog & Releases (296–382)
*Release notes, changelogs, and version history*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 296 | `296-changelogs-v1.4.1.md` | v1.4.1 | This document details the updates and bug fixes for Bifrost version 1.4.1, primarily addressing streaming support for B… | release-notes, changelog, bifrost, bedrock, structured-output, streaming |
| 297 | `297-changelogs-v1.4.0.md` | v1.4.0 | This document outlines the version 1.4.0 changelog for Bifrost, detailing new features, bug fixes, and dependency updat… | changelog, release-notes, bifrost, version-update, software-maintenance |
| 298 | `298-changelogs-v1.4.0-prerelease10.md` | v1.4.0-prerelease10 | This document provides the release notes for Bifrost version 1.4.0-prerelease10, detailing new features such as image g… | release-notes, bifrost, changelog, image-generation, llm-gateway, web-search |
| 299 | `299-changelogs-v1.4.0-prerelease9.md` | v1.4.0-prerelease9 | This document outlines the changes in Bifrost version 1.4.0-prerelease9, focusing on fixes for streaming response timeo… | release-notes, changelog, bifrost, bug-fix, streaming-responses, version-update |
| 300 | `300-changelogs-v1.4.0-prerelease8.md` | v1.4.0-prerelease8 | This document details the updates and bug fixes for Bifrost version 1.4.0-prerelease8, including model enhancements for… | release-notes, changelog, bifrost, vertex-ai, gemini, telemetry |
| 301 | `301-changelogs-v1.4.0-prerelease7.md` | v1.4.0-prerelease7 | This document outlines the changes in Bifrost v1.4.0-prerelease7, focusing on bug fixes for xAI provider integration, q… | release-notes, changelog, bifrost, xai-integration, bug-fixes, version-update |
| 302 | `302-changelogs-v1.4.0-prerelease6.md` | v1.4.0-prerelease6 | This document provides the release notes for Bifrost version 1.4.0-prerelease6, documenting various bug fixes, feature… | release-notes, changelog, bifrost, software-updates, version-history |
| 303 | `303-changelogs-v1.4.0-prerelease5.md` | v1.4.0-prerelease5 | This document provides the release notes for Bifrost version 1.4.0-prerelease5, detailing bug fixes for LLM integration… | release-notes, bifrost, changelog, bug-fixes, installation |
| 304 | `304-changelogs-v1.4.0-prerelease4.md` | v1.4.0-prerelease4 | This document provides the release notes and changelog for Bifrost version 1.4.0-prerelease4, detailing new features, b… | release-notes, changelog, bifrost, gemini-integration, anthropic-integration, bug-fixes |
| 305 | `305-changelogs-v1.4.0-prerelease3.md` | v1.4.0-prerelease3 | This document outlines the updates and bug fixes for the v1.4.0-prerelease3 release, covering provider-specific improve… | changelog, release-notes, bifrost, bug-fixes, azure-entra-id, anthropic |
| 306 | `306-changelogs-v1.4.0-prerelease2.md` | v1.4.0-prerelease2 | This document provides release notes for Bifrost version 1.4.0-prerelease2, detailing bug fixes for AI model integratio… | release-notes, bifrost, changelog, distributed-tracing, bug-fixes, version-update |
| 307 | `307-changelogs-v1.4.0-prerelease1.md` | v1.4.0-prerelease1 | Release notes for Bifrost v1.4.0-prerelease1 detailing new MCP gateway features, end-to-end tracing, and a significant… | release-notes, breaking-changes, bifrost, middleware, tracing, plugin-system |
| 308 | `308-changelogs-v1.3.63.md` | v1.3.63 | This document details the changelog for version 1.3.63 of Bifrost, covering bug fixes for authentication and provider m… | changelog, release-notes, bifrost, version-update, bug-fixes, deployment |
| 309 | `309-changelogs-v1.3.62.md` | v1.3.62 | This document provides the release notes for version 1.3.62, detailing the specific version update and its historical c… | release-notes, changelog, versioning, software-update, bifrost-ai |
| 310 | `310-changelogs-v1.3.61.md` | v1.3.61 | This document outlines the updates for Bifrost version 1.3.61, including bug fixes for Gemini chat converters and vario… | changelog, release-notes, bifrost, gemini-integration, version-update |
| 311 | `311-changelogs-v1.3.60.md` | v1.3.60 | This document outlines the version 1.3.60 release notes for the Bifrost platform, detailing updates to authentication,… | changelog, release-notes, bifrost, version-update, software-maintenance |
| 312 | `312-changelogs-v1.3.59.md` | v1.3.59 | This document outlines the changes, bug fixes, and new features introduced in Bifrost version 1.3.59, including improve… | release-notes, changelog, bifrost, gemini, anthropic, structured-outputs |
| 313 | `313-changelogs-v1.3.58.md` | v1.3.58 | Release notes for Bifrost v1.3.58, highlighting new Azure Entra ID support and fixes for Anthropic and Gemini provider… | changelog, release-notes, bifrost, azure-entra-id, anthropic, gemini |
| 314 | `314-changelogs-v1.3.57.md` | v1.3.57 | This document details the version 1.3.57 release notes for Bifrost, including bug fixes for configuration parsing and f… | changelog, release-notes, bifrost, version-update, bug-fixes, framework-upgrade |
| 315 | `315-changelogs-v1.3.56.md` | v1.3.56 | This document provides the changelog for Bifrost version 1.3.56, detailing bug fixes for configuration handling, new ha… | changelog, release-notes, bifrost, version-update, bug-fixes, configuration-management |
| 316 | `316-changelogs-v1.3.54.md` | v1.3.54 | This document outlines the changes in Bifrost version 1.3.54, highlighting new document support for AI providers and he… | release-notes, changelog, bifrost, ai-providers, header-filtering |
| 317 | `317-changelogs-v1.3.53.md` | v1.3.53 | This document outlines the changes and bug fixes introduced in Bifrost version 1.3.53, including improvements to Anthro… | changelog, release-notes, bifrost, bug-fixes, anthropic, bedrock |
| 318 | `318-changelogs-v1.3.52.md` | v1.3.52 | This document provides the release notes for version 1.3.52 of Bifrost, detailing bug fixes, new model features for Ant… | release-notes, changelog, bifrost, gemini, anthropic, software-update |
| 319 | `319-changelogs-v1.3.51.md` | v1.3.51 | This document outlines the changes, bug fixes, and new features introduced in version 1.3.51 of Bifrost, including Hugg… | release-notes, changelog, bifrost, huggingface, bug-fixes, proxy-support |
| 320 | `320-changelogs-v1.3.50.md` | v1.3.50 | This document provides the release notes for version 1.3.50, detailing new features, bug fixes, and improvements across… | release-notes, changelog, bifrost, api-updates, prompt-caching, model-support |
| 321 | `321-changelogs-v1.3.49.md` | v1.3.49 | This document outlines the changes in Bifrost version 1.3.49, detailing new features such as batch API support and prov… | changelog, release-notes, bifrost, batch-api, llm-providers, software-update |
| 322 | `322-changelogs-v1.3.48.md` | v1.3.48 | This document outlines the release notes and deployment instructions for Bifrost version 1.3.48, featuring security pat… | release-notes, bifrost, security-patch, docker, npx, changelog |
| 323 | `323-changelogs-v1.3.47.md` | v1.3.47 | This document outlines the version 1.3.47 release notes for Bifrost, detailing new features such as raw request logging… | changelog, bifrost, release-notes, chat-completions, api-updates, logging |
| 324 | `324-changelogs-v1.3.46.md` | v1.3.46 | This document provides the release notes and update instructions for Bifrost version 1.3.46, which includes critical se… | changelog, release-notes, security-patch, hotfix, bifrost, version-update |
| 325 | `325-changelogs-v1.3.45.md` | v1.3.45 | This document details the changelog for Bifrost version 1.3.45, providing information on new features, bug fixes, and c… | changelog, release-notes, bifrost, version-update, bug-fixes, deployment |
| 326 | `326-changelogs-v1.3.44.md` | v1.3.44 | This document provides the release notes and changelog for Bifrost version 1.3.44, detailing new features like RBAC sup… | changelog, release-notes, rbac, bifrost, docker, deployment |
| 327 | `327-changelogs-v1.3.43.md` | v1.3.43 | This document outlines the updates and new features introduced in version 1.3.43 of Bifrost, including global proxy sup… | release-notes, bifrost-updates, docker-deployment, proxy-support, datadog-integration, otel-plugin |
| 328 | `328-changelogs-v1.3.42.md` | v1.3.42 | This document provides the release notes for Bifrost version 1.3.42, detailing installation instructions via NPX and Do… | release-notes, changelog, bifrost, version-update, docker, npx |
| 329 | `329-changelogs-v1.3.41.md` | v1.3.41 | This document provides the release notes for version 1.3.41, detailing a critical fix for Docker segmentation faults an… | release-notes, bifrost, docker-fix, plugin-update, version-history, bug-fix |
| 330 | `330-changelogs-v1.3.40.md` | v1.3.40 | This document outlines the release notes and update instructions for Bifrost version 1.3.40, featuring critical securit… | release-notes, bifrost, security-update, docker, npx, v1-3-40 |
| 331 | `331-changelogs-v1.3.39.md` | v1.3.39 | This document provides the release notes for Bifrost version 1.3.39, detailing improvements to streaming usage aggregat… | changelog, release-notes, bifrost, streaming-fix, api-updates, version-history |
| 332 | `332-changelogs-v1.3.38.md` | v1.3.38 | This document provides the release notes for version 1.3.38, detailing new features like Anthropic model support in Azu… | release-notes, changelog, bifrost, anthropic, azure, google-gemini |
| 333 | `333-changelogs-v1.3.37.md` | v1.3.37 | This document details the release notes for version 1.3.37, covering new SDK support, breaking changes to plugin contex… | release-notes, changelog, bifrost, breaking-changes, sdk-support, version-update |
| 334 | `334-changelogs-v1.3.36.md` | v1.3.36 | This document provides the changelog and release notes for Bifrost version 1.3.36, detailing new features, bug fixes, a… | changelog, release-notes, bifrost, bug-fixes, version-update, opus-support |
| 335 | `335-changelogs-v1.3.35.md` | v1.3.35 | This document outlines the updates and bug fixes for Bifrost version 1.3.35, including new support for Qdrant Vector Se… | changelog, release-notes, qdrant, vector-search, bug-fixes, streaming |
| 336 | `336-changelogs-v1.3.34.md` | v1.3.34 | This document outlines the release notes and changelog for Bifrost version 1.3.34, detailing feature updates, bug fixes… | release-notes, changelog, bifrost, version-update, software-maintenance |
| 337 | `337-changelogs-v1.3.33.md` | v1.3.33 | This document outlines the updates and bug fixes in version 1.3.33 of Bifrost, including new log retention settings and… | release-notes, changelog, log-management, token-caching, bifrost |
| 338 | `338-changelogs-v1.3.32.md` | v1.3.32 | This document outlines the version 1.3.32 changelog for Bifrost, detailing new features for Anthropic and Gemini provid… | release-notes, changelog, bifrost, anthropic-integration, gemini-integration, version-update |
| 339 | `339-changelogs-v1.3.31.md` | v1.3.31 | This document outlines the release notes and update details for Bifrost version 1.3.31, including installation methods… | changelog, release-notes, bifrost, version-update, bug-fixes, docker |
| 340 | `340-changelogs-v1.3.30.md` | v1.3.30 | This document outlines the changes in version 1.3.30 of Bifrost, including database migrations for the provider column… | changelog, release-notes, bifrost, database-migration, version-update |
| 341 | `341-changelogs-v1.3.29.md` | v1.3.29 | This document provides the release notes and changelog for version 1.3.29 of the Bifrost platform, detailing bug fixes… | changelog, release-notes, bifrost, metrics, opentelemetry, bug-fixes |
| 342 | `342-changelogs-v1.3.28.md` | v1.3.28 | This document outlines the v1.3.28 release notes for Bifrost, detailing performance optimizations for log processing on… | changelog, release-notes, bifrost, performance-optimization, sqlite, log-management |
| 343 | `343-changelogs-v1.3.27.md` | v1.3.27 | This document provides the release notes for Bifrost version 1.3.27, detailing fixes for Bedrock memory and streaming r… | bifrost, changelog, release-notes, bedrock, bug-fixes, version-update |
| 344 | `344-changelogs-v1.3.26.md` | v1.3.26 | This document outlines the changes in version 1.3.26, featuring the addition of Elevenlabs provider support, security f… | release-notes, changelog, elevenlabs-integration, bifrost-update, version-v1-3-26, deployment |
| 345 | `345-changelogs-v1.3.25.md` | v1.3.25 | This document provides the release notes for Bifrost version 1.3.25, detailing updates to the core engine, framework, a… | changelog, release-notes, bifrost, vertex-ai, streaming-events, api-updates |
| 346 | `346-changelogs-v1.3.24.md` | v1.3.24 | This document provides the changelog for Bifrost version 1.3.24, detailing core and framework updates, logging improvem… | release-notes, changelog, bifrost, software-update, docker, npx |
| 347 | `347-changelogs-v1.3.23.md` | v1.3.23 | This document outlines the release notes and changelog for version 1.3.23 of the Bifrost platform, detailing new featur… | release-notes, changelog, bifrost, mcp-client, gemini-integration, software-update |
| 348 | `348-changelogs-v1.3.22.md` | v1.3.22 | This document provides the release notes for Bifrost version 1.3.22, detailing new features, breaking changes, and modu… | changelog, release-notes, bifrost, version-update, software-maintenance |
| 349 | `349-changelogs-v1.3.21.md` | v1.3.21 | This document details the changelog and deployment commands for Bifrost version 1.3.21, including bug fixes for session… | bifrost, changelog, version-update, http-proxy, bug-fix, docker |
| 350 | `350-changelogs-v1.3.20.md` | v1.3.20 | This document provides release notes and installation instructions for Bifrost version 1.3.20, including a bug fix for… | bifrost, release-notes, changelog, bug-fix, docker, npx |
| 351 | `351-changelogs-v1.3.19.md` | v1.3.19 | This document provides the release notes for Bifrost version v1.3.19, detailing new features in telemetry metrics, logg… | changelog, release-notes, bifrost, telemetry, logging, mcp-client |
| 352 | `352-changelogs-v1.3.18.md` | v1.3.18 | This document outlines the updates and bug fixes introduced in Bifrost version 1.3.18, including changes to the health… | bifrost, changelog, release-notes, v1-3-18, deployment, bug-fixes |
| 353 | `353-changelogs-v1.3.17.md` | v1.3.17 | This document provides the release notes and installation commands for Bifrost version 1.3.17, covering bug fixes for v… | changelog, release-notes, bifrost, version-update, docker, npx |
| 354 | `354-changelogs-v1.3.16.md` | v1.3.16 | This document details the updates in version 1.3.16 of Bifrost, highlighting new provider support for Perplexity and Mi… | changelog, bifrost, release-notes, perplexity, mistralai, anthropic |
| 355 | `355-changelogs-v1.3.15.md` | v1.3.15 | This document provides the release notes and changelog for version v1.3.15 of the Bifrost platform, detailing installat… | release-notes, changelog, bifrost, version-update, docker-installation, backend-framework |
| 356 | `356-changelogs-v1.3.14.md` | v1.3.14 | This document provides the release notes for Bifrost version 1.3.14, detailing new features such as dynamic plugins and… | release-notes, changelog, bifrost, software-update, authentication, dynamic-plugins |
| 357 | `357-changelogs-v1.3.13.md` | v1.3.13 | This document provides the release notes and changelog for Bifrost version 1.3.13, detailing new features like provider… | bifrost, release-notes, changelog, versioning, deployment, hot-reloading |
| 358 | `358-changelogs-v1.3.12.md` | v1.3.12 | This document provides the release notes for Bifrost version 1.3.12, detailing new features such as Azure native respon… | release-notes, changelog, bifrost-updates, azure-integration, async-processing, rate-limiting |
| 359 | `359-changelogs-v1.3.11.md` | v1.3.11 | This document details the release notes for Bifrost version 1.3.11, highlighting new features such as the models endpoi… | release-notes, bifrost, version-update, api-changes, deployment |
| 360 | `360-changelogs-v1.3.10.md` | v1.3.10 | This document provides the version 1.3.10 changelog for Bifrost, detailing new features, performance improvements, and… | release-notes, changelog, bifrost, otel, vertex-api, version-update |
| 361 | `361-changelogs-v1.3.9.md` | v1.3.9 | This document provides the release notes and installation instructions for Bifrost version 1.3.9, including a fix for A… | bifrost, changelog, release-notes, azure, deployment, docker |
| 362 | `362-changelogs-v1.3.8.md` | v1.3.8 | Detailed release notes for Bifrost version 1.3.8, highlighting bug fixes for OpenAI and Gemini providers and a breaking… | release-notes, bifrost, changelog, bug-fixes, breaking-changes, openai |
| 363 | `363-changelogs-v1.3.7.md` | v1.3.7 | This document provides the release notes and changelog for Bifrost version 1.3.7, detailing installation instructions a… | release-notes, changelog, version-update, bug-fixes, bifrost-deployment |
| 364 | `364-changelogs-v1.3.6.md` | v1.3.6 | This document details the changes and updates in Bifrost version 1.3.6, including bug fixes for tool message outputs an… | changelog, release-notes, bifrost, docker, version-update, bug-fixes |
| 365 | `365-changelogs-v1.3.5.md` | v1.3.5 | This document outlines the release notes and changelog for Bifrost version 1.3.5, detailing new features, bug fixes, an… | changelog, release-notes, bifrost, software-update, database-migration, mcp-client |
| 366 | `366-changelogs-v1.3.4.md` | v1.3.4 | This document provides the changelog for Bifrost version 1.3.4, detailing updates to the HTTP interface, core engine, a… | changelog, release-notes, bifrost, mcp-tools, dependency-update, key-management |
| 367 | `367-changelogs-v1.3.3.md` | v1.3.3 | This document details the changelog for version 1.3.3 of the Bifrost platform, highlighting bug fixes for JSON serializ… | changelog, release-notes, bifrost, version-update, bug-fix, json-serialization |
| 368 | `368-changelogs-v1.3.2.md` | v1.3.2 | This document outlines the changes in Bifrost version 1.3.2, including major refactoring of context keys, bug fixes for… | release-notes, changelog, bifrost, version-update, bug-fix, refactoring |
| 369 | `369-changelogs-v1.3.1.md` | v1.3.1 | Detailed release notes for Bifrost version 1.3.1, covering installation steps and specific updates across various core… | bifrost, changelog, release-notes, bug-fixes, dependency-upgrades, docker |
| 370 | `370-changelogs-v1.3.0.md` | v1.3.0 | This document outlines the version 1.3.0 release notes for Bifrost, detailing new features like OpenTelemetry support,… | changelog, release-notes, bifrost, opentelemetry, api-gateway, version-update |
| 371 | `371-changelogs-v1.3.0-prerelease7.md` | v1.3.0-prerelease7 | Detailed changelog for Bifrost v1.3.0-prerelease7, highlighting new streaming capabilities, telemetry fixes, and core d… | bifrost, release-notes, changelog, streaming, telemetry, bedrock |
| 372 | `372-changelogs-v1.3.0-prerelease6.md` | v1.3.0-prerelease6 | This document outlines the changes and new features in the v1.3.0-prerelease6 update for Bifrost, including Anthropic i… | release-notes, changelog, bifrost, anthropic-integration, latency-tracking, software-update |
| 373 | `373-changelogs-v1.3.0-prerelease5.md` | v1.3.0-prerelease5 | This document outlines the changes and updates included in the v1.3.0-prerelease5 release of Bifrost, specifically deta… | release-notes, changelog, bifrost, anthropic, logging, version-update |
| 374 | `374-changelogs-v1.3.0-prerelease4.md` | v1.3.0-prerelease4 | This document outlines the changes and installation steps for Bifrost version 1.3.0-prerelease4, featuring a new LiteLL… | bifrost, changelog, release-notes, groq, litellm, version-update |
| 375 | `375-changelogs-v1.3.0-prerelease3.md` | v1.3.0-prerelease3 | This document provides the changelog for Bifrost version 1.3.0-prerelease3, detailing bug fixes for string inputs and n… | bifrost, release-notes, changelog, openai-integration, bug-fixes |
| 376 | `376-changelogs-v1.3.0-prerelease2.md` | v1.3.0-prerelease2 | This document outlines the release notes and installation instructions for Bifrost version 1.3.0-prerelease2, highlight… | release-notes, bifrost, text-completion, streaming-support, error-handling, changelog |
| 377 | `377-changelogs-v1.3.0-prerelease1.md` | v1.3.0-prerelease1 | This document provides the changelog for Bifrost version 1.3.0-prerelease1, detailing new features, bug fixes, and brea… | changelog, release-notes, bifrost, observability, otlp, plugin-management |
| 378 | `378-changelogs-v1.2.24.md` | v1.2.24 | This document details the updates and bug fixes for Bifrost version 1.2.24, including component upgrades and UI improve… | release-notes, changelog, bifrost, version-update, bug-fixes, docker |
| 379 | `379-changelogs-v1.2.23.md` | v1.2.23 | This document details the release notes and changelog for version 1.2.23 of the Bifrost platform, including bug fixes a… | changelog, release-notes, bifrost, software-update, bug-fixes, version-1-2-23 |
| 380 | `380-changelogs-v1.2.22.md` | v1.2.22 | This document provides the release notes for Bifrost version 1.2.22, detailing bug fixes for streaming responses and UI… | release-notes, changelog, bifrost, bug-fixes, version-update, streaming-responses |
| 381 | `381-changelogs-v1.2.21.md` | v1.2.21 | This document outlines the changes in Bifrost version 1.2.21, including fixes for pricing computation with nested model… | bifrost, changelog, release-notes, bug-fix, pricing-module, framework-upgrade |
| 382 | `382-plugins-migration-guide.md` | Plugin Migration Guide | This document provides instructions and code examples for migrating Bifrost plugins from v1.3.x to v1.4.x, focusing on… | bifrost, plugin-migration, golang, http-transport, wasm-support, api-update |

### 8. Meta & Resources (383–389)
*Pricing, legal, community, and other resources*

| # | File | Title | Summary | Tags |
|---|---|---|---|---|
| 383 | `383-bifrost-discord.md` | Discord | This document provides a redirection notice indicating that the content has been moved to a new location on Discord. | redirection, http-302, document-moved, discord |
| 384 | `384-bifrost-enterprise.md` | Bifrost - AI Gateway | This document is empty and contains no text or instructions to analyze. | empty-document, no-content, placeholder |
| 385 | `385-contributing-adding-a-configstore.md` | Adding config store | This guide provides instructions for developers on how to extend the Bifrost config store by implementing new database… | bifrost, config-store, database-backend, gorm, golang, extensibility |
| 386 | `386-contributing-adding-a-logstore.md` | Adding a log store | This guide explains how to add a custom database backend for the Bifrost log store by implementing the LogStore interfa… | bifrost, log-store, database-backend, gorm, golang, extensibility |
| 387 | `387-contributing-adding-a-provider.md` | Adding a new provider | This guide provides a comprehensive walkthrough for adding new LLM providers to the Bifrost gateway, covering both Open… | bifrost, provider-integration, golang, api-gateway, llm-provider, open-source-contribution |
| 388 | `388-contributing-adding-a-vectorstore.md` | Adding a vector store | This guide provides instructions on how to contribute a new vector database backend to Bifrost by implementing the Vect… | bifrost, vector-store, database-integration, backend-development, vector-database, contribution-guide |
| 389 | `389-contributing-setting-up-repo.md` | Setting up the repository | This document provides a comprehensive guide for setting up the Bifrost repository for local development, covering prer… | development-setup, bifrost, go, makefile, local-environment, testing |

---

## Dropped (deduplication)

| Path | In favor of | Reason |
|------|-------------|--------|
| `389-bifrost-discord.md` | `001-bifrost-discord.md` | identico |
| `001-quickstart-gateway-setting-up.md` | `003-quickstart-gateway-setting-up.md` | identico |
| `295-bifrost-enterprise.md` | `002-bifrost-enterprise.md` | identico |
| `002-quickstart-gateway-setting-up-auth.md` | `004-quickstart-gateway-setting-up-auth.md` | identico |
| `003-quickstart-gateway-cli-agents.md` | `005-quickstart-gateway-cli-agents.md` | identico |
| `004-quickstart-gateway-integrations.md` | `006-quickstart-gateway-integrations.md` | identico |
| `005-quickstart-gateway-multimodal.md` | `007-quickstart-gateway-multimodal.md` | identico |
| `006-quickstart-gateway-provider-configuration.md` | `008-quickstart-gateway-provider-configuration.md` | identico |
| `007-quickstart-gateway-streaming.md` | `009-quickstart-gateway-streaming.md` | identico |
| `008-quickstart-gateway-tool-calling.md` | `010-quickstart-gateway-tool-calling.md` | identico |
| `009-quickstart-go-sdk-setting-up.md` | `011-quickstart-go-sdk-setting-up.md` | identico |
| `010-quickstart-go-sdk-context-keys.md` | `012-quickstart-go-sdk-context-keys.md` | identico |
| `011-quickstart-go-sdk-logger.md` | `013-quickstart-go-sdk-logger.md` | identico |
| `012-quickstart-go-sdk-multimodal.md` | `014-quickstart-go-sdk-multimodal.md` | identico |
| `013-quickstart-go-sdk-provider-configuration.md` | `015-quickstart-go-sdk-provider-configuration.md` | identico |
| `014-quickstart-go-sdk-streaming.md` | `016-quickstart-go-sdk-streaming.md` | identico |
| `015-quickstart-go-sdk-tool-calling.md` | `017-quickstart-go-sdk-tool-calling.md` | identico |
| `016-integrations-anthropic-sdk-overview.md` | `019-integrations-anthropic-sdk-overview.md` | identico |
| `017-integrations-bedrock-sdk-overview.md` | `020-integrations-bedrock-sdk-overview.md` | identico |
| `018-integrations-genai-sdk-overview.md` | `021-integrations-genai-sdk-overview.md` | identico |
| `052-integrations-what-is-an-integration.md` | `018-integrations-what-is-an-integration.md` | identico |
| `019-integrations-openai-sdk-overview.md` | `022-integrations-openai-sdk-overview.md` | identico |
| `020-mcp-overview.md` | `044-mcp-overview.md` | identico |
| `021-plugins-getting-started.md` | `052-plugins-getting-started.md` | identico |
| `022-providers-supported-providers-overview.md` | `057-providers-supported-providers-overview.md` | identico |
| `023-enterprise-advanced-governance.md` | `082-enterprise-advanced-governance.md` | identico |
| `154-integrations-anthropic-sdk-files-and-batch.md` | `023-integrations-anthropic-sdk-files-and-batch.md` | identico |
| `024-benchmarking-getting-started.md` | `111-benchmarking-getting-started.md` | identico |
| `155-integrations-bedrock-sdk-files-and-batch.md` | `024-integrations-bedrock-sdk-files-and-batch.md` | identico |
| `025-deployment-guides-how-to-install-make.md` | `098-deployment-guides-how-to-install-make.md` | identico |
| `156-integrations-langchain-sdk.md` | `025-integrations-langchain-sdk.md` | identico |
| `157-integrations-litellm-sdk.md` | `026-integrations-litellm-sdk.md` | identico |
| `026-plugins-migration-guide.md` | `054-plugins-migration-guide.md` | identico |
| `027-deployment-guides-ecs.md` | `095-deployment-guides-ecs.md` | identico |
| `158-integrations-openai-sdk-files-and-batch.md` | `027-integrations-openai-sdk-files-and-batch.md` | identico |
| `028-deployment-guides-fly.md` | `096-deployment-guides-fly.md` | identico |
| `159-integrations-pydanticai-sdk.md` | `028-integrations-pydanticai-sdk.md` | identico |
| `029-deployment-guides-helm.md` | `097-deployment-guides-helm.md` | identico |
| `053-features-drop-in-replacement.md` | `029-features-drop-in-replacement.md` | identico |
| `030-deployment-guides-how-to-multinode.md` | `099-deployment-guides-how-to-multinode.md` | identico |
| `054-features-fallbacks.md` | `030-features-fallbacks.md` | identico |
| `031-deployment-guides-k8s.md` | `100-deployment-guides-k8s.md` | identico |
| `055-features-governance-budget-and-limits.md` | `031-features-governance-budget-and-limits.md` | identico |
| `032-architecture-core-concurrency.md` | `101-architecture-core-concurrency.md` | identico |
| `056-features-governance-mcp-tools.md` | `032-features-governance-mcp-tools.md` | identico |
| `033-architecture-core-mcp.md` | `102-architecture-core-mcp.md` | identico |
| `057-features-governance-routing.md` | `033-features-governance-routing.md` | identico |
| `034-architecture-core-plugins.md` | `103-architecture-core-plugins.md` | identico |
| `058-features-governance-virtual-keys.md` | `034-features-governance-virtual-keys.md` | identico |
| `035-architecture-core-request-flow.md` | `104-architecture-core-request-flow.md` | identico |
| `059-features-keys-management.md` | `035-features-keys-management.md` | identico |
| `036-architecture-framework-config-store.md` | `105-architecture-framework-config-store.md` | identico |
| `060-features-litellm-compat.md` | `036-features-litellm-compat.md` | identico |
| `037-architecture-framework-log-store.md` | `106-architecture-framework-log-store.md` | identico |
| `061-features-observability-default.md` | `037-features-observability-default.md` | identico |
| `038-architecture-framework-model-catalog.md` | `107-architecture-framework-model-catalog.md` | identico |
| `062-features-observability-maxim.md` | `038-features-observability-maxim.md` | identico |
| `039-architecture-framework-streaming.md` | `108-architecture-framework-streaming.md` | identico |
| `063-features-observability-otel.md` | `039-features-observability-otel.md` | identico |
| `040-architecture-framework-vector-store.md` | `109-architecture-framework-vector-store.md` | identico |
| `064-features-plugins-jsonparser.md` | `040-features-plugins-jsonparser.md` | identico |
| `041-architecture-framework-what-is-framework.md` | `110-architecture-framework-what-is-framework.md` | identico |
| `065-features-plugins-mocker.md` | `041-features-plugins-mocker.md` | identico |
| `042-enterprise-setting-up-entra.md` | `092-enterprise-setting-up-entra.md` | identico |
| `066-features-semantic-caching.md` | `042-features-semantic-caching.md` | identico |
| `043-enterprise-setting-up-okta.md` | `093-enterprise-setting-up-okta.md` | identico |
| `067-features-telemetry.md` | `043-features-telemetry.md` | identico |
| `044-contributing-adding-a-configstore.md` | `115-contributing-adding-a-configstore.md` | identico |
| `045-contributing-setting-up-repo.md` | `119-contributing-setting-up-repo.md` | identico |
| `071-mcp-agent-mode.md` | `045-mcp-agent-mode.md` | identico |
| `046-api-reference-configuration-get-configuration.md` | `142-api-reference-configuration-get-configuration.md` | identico |
| `072-mcp-code-mode.md` | `046-mcp-code-mode.md` | identico |
| `047-api-reference-configuration-update-configuration.md` | `143-api-reference-configuration-update-configuration.md` | identico |
| `073-mcp-connecting-to-servers.md` | `047-mcp-connecting-to-servers.md` | identico |
| `048-api-reference-configuration-force-pricing-sync.md` | `144-api-reference-configuration-force-pricing-sync.md` | identico |
| `074-mcp-filtering.md` | `048-mcp-filtering.md` | identico |
| `049-api-reference-configuration-get-proxy-configuration.md` | `145-api-reference-configuration-get-proxy-configuration.md` | identico |
| `075-mcp-gateway-url.md` | `049-mcp-gateway-url.md` | identico |
| `050-api-reference-configuration-update-proxy-configuration.md` | `146-api-reference-configuration-update-proxy-configuration.md` | identico |
| `076-mcp-tool-execution.md` | `050-mcp-tool-execution.md` | identico |
| `051-api-reference-configuration-get-version.md` | `147-api-reference-configuration-get-version.md` | identico |
| `077-mcp-tool-hosting.md` | `051-mcp-tool-hosting.md` | identico |
| `078-plugins-building-dynamic-binary.md` | `053-plugins-building-dynamic-binary.md` | identico |
| `079-plugins-writing-go-plugin.md` | `055-plugins-writing-go-plugin.md` | identico |
| `080-plugins-writing-wasm-plugin.md` | `056-plugins-writing-wasm-plugin.md` | identico |
| `081-providers-custom-providers.md` | `058-providers-custom-providers.md` | identico |
| `082-providers-performance.md` | `059-providers-performance.md` | identico |
| `083-providers-provider-routing.md` | `060-providers-provider-routing.md` | identico |
| `084-providers-reasoning.md` | `061-providers-reasoning.md` | identico |
| `085-providers-supported-providers-anthropic.md` | `062-providers-supported-providers-anthropic.md` | identico |
| `086-providers-supported-providers-azure.md` | `063-providers-supported-providers-azure.md` | identico |
| `087-providers-supported-providers-bedrock.md` | `064-providers-supported-providers-bedrock.md` | identico |
| `088-providers-supported-providers-cerebras.md` | `065-providers-supported-providers-cerebras.md` | identico |
| `089-providers-supported-providers-cohere.md` | `066-providers-supported-providers-cohere.md` | identico |
| `090-providers-supported-providers-elevenlabs.md` | `067-providers-supported-providers-elevenlabs.md` | identico |
| `068-benchmarking-run-your-own-benchmarks.md` | `112-benchmarking-run-your-own-benchmarks.md` | identico |
| `091-providers-supported-providers-gemini.md` | `068-providers-supported-providers-gemini.md` | identico |
| `069-benchmarking-t3.medium.md` | `113-benchmarking-t3.medium.md` | identico |
| `092-providers-supported-providers-groq.md` | `069-providers-supported-providers-groq.md` | identico |
| `070-benchmarking-t3.xl.md` | `114-benchmarking-t3.xl.md` | identico |
| `093-providers-supported-providers-huggingface.md` | `070-providers-supported-providers-huggingface.md` | identico |
| `094-providers-supported-providers-mistral.md` | `071-providers-supported-providers-mistral.md` | identico |
| `095-providers-supported-providers-nebius.md` | `072-providers-supported-providers-nebius.md` | identico |
| `096-providers-supported-providers-ollama.md` | `073-providers-supported-providers-ollama.md` | identico |
| `097-providers-supported-providers-openai.md` | `074-providers-supported-providers-openai.md` | identico |
| `098-providers-supported-providers-openrouter.md` | `075-providers-supported-providers-openrouter.md` | identico |
| `099-providers-supported-providers-parasail.md` | `076-providers-supported-providers-parasail.md` | identico |
| `100-providers-supported-providers-perplexity.md` | `077-providers-supported-providers-perplexity.md` | identico |
| `101-providers-supported-providers-sgl.md` | `078-providers-supported-providers-sgl.md` | identico |
| `102-providers-supported-providers-vertex.md` | `079-providers-supported-providers-vertex.md` | identico |
| `103-providers-supported-providers-xai.md` | `080-providers-supported-providers-xai.md` | identico |
| `296-enterprise-adaptive-load-balancing.md` | `081-enterprise-adaptive-load-balancing.md` | identico |
| `297-enterprise-audit-logs.md` | `083-enterprise-audit-logs.md` | identico |
| `298-enterprise-clustering.md` | `084-enterprise-clustering.md` | identico |
| `104-enterprise-custom-plugins.md` | `085-enterprise-custom-plugins.md` | identico |
| `105-enterprise-datadog-connector.md` | `086-enterprise-datadog-connector.md` | identico |
| `151-enterprise-guardrails.md` | `087-enterprise-guardrails.md` | identico |
| `294-enterprise-invpc-deployments.md` | `088-enterprise-invpc-deployments.md` | identico |
| `299-enterprise-log-exports.md` | `089-enterprise-log-exports.md` | identico |
| `106-enterprise-mcp-with-fa.md` | `090-enterprise-mcp-with-fa.md` | identico |
| `152-enterprise-rbac.md` | `091-enterprise-rbac.md` | identico |
| `300-enterprise-vault-support.md` | `094-enterprise-vault-support.md` | identico |
| `107-contributing-adding-a-provider.md` | `117-contributing-adding-a-provider.md` | identico |
| `108-api-reference-models-list-available-models.md` | `139-api-reference-models-list-available-models.md` | identico |
| `109-api-reference-mcp-add-mcp-client.md` | `171-api-reference-mcp-add-mcp-client.md` | identico |
| `110-api-reference-mcp-edit-mcp-client.md` | `172-api-reference-mcp-edit-mcp-client.md` | identico |
| `111-api-reference-mcp-execute-mcp-tool.md` | `173-api-reference-mcp-execute-mcp-tool.md` | identico |
| `112-api-reference-mcp-list-mcp-clients.md` | `174-api-reference-mcp-list-mcp-clients.md` | identico |
| `113-api-reference-mcp-reconnect-mcp-client.md` | `175-api-reference-mcp-reconnect-mcp-client.md` | identico |
| `114-api-reference-mcp-remove-mcp-client.md` | `176-api-reference-mcp-remove-mcp-client.md` | identico |
| `115-api-reference-plugins-create-a-new-plugin.md` | `177-api-reference-plugins-create-a-new-plugin.md` | identico |
| `116-api-reference-plugins-update-a-plugin.md` | `178-api-reference-plugins-update-a-plugin.md` | identico |
| `387-contributing-adding-a-logstore.md` | `116-contributing-adding-a-logstore.md` | identico |
| `117-api-reference-plugins-delete-a-plugin.md` | `179-api-reference-plugins-delete-a-plugin.md` | identico |
| `118-api-reference-plugins-get-a-specific-plugin.md` | `180-api-reference-plugins-get-a-specific-plugin.md` | identico |
| `388-contributing-adding-a-vectorstore.md` | `118-contributing-adding-a-vectorstore.md` | identico |
| `119-api-reference-plugins-list-all-plugins.md` | `181-api-reference-plugins-list-all-plugins.md` | identico |
| `160-api-reference-audio-create-speech.md` | `120-api-reference-audio-create-speech.md` | identico |
| `120-api-reference-providers-update-a-provider.md` | `182-api-reference-providers-update-a-provider.md` | identico |
| `161-api-reference-audio-create-transcription.md` | `121-api-reference-audio-create-transcription.md` | identico |
| `121-api-reference-providers-delete-a-provider.md` | `183-api-reference-providers-delete-a-provider.md` | identico |
| `162-api-reference-batch-retrieve-a-batch-job.md` | `122-api-reference-batch-retrieve-a-batch-job.md` | identico |
| `122-api-reference-providers-get-a-specific-provider.md` | `184-api-reference-providers-get-a-specific-provider.md` | identico |
| `163-api-reference-batch-create-a-batch-job.md` | `123-api-reference-batch-create-a-batch-job.md` | identico |
| `123-api-reference-providers-add-a-new-provider.md` | `185-api-reference-providers-add-a-new-provider.md` | identico |
| `164-api-reference-batch-cancel-a-batch-job.md` | `124-api-reference-batch-cancel-a-batch-job.md` | identico |
| `124-api-reference-providers-list-all-keys.md` | `186-api-reference-providers-list-all-keys.md` | identico |
| `165-api-reference-batch-list-batch-jobs.md` | `125-api-reference-batch-list-batch-jobs.md` | identico |
| `125-api-reference-providers-list-all-providers.md` | `187-api-reference-providers-list-all-providers.md` | identico |
| `166-api-reference-batch-get-batch-results.md` | `126-api-reference-batch-get-batch-results.md` | identico |
| `126-api-reference-providers-list-models.md` | `188-api-reference-providers-list-models.md` | identico |
| `127-api-reference-anthropic-integration-list-models-anthropic-format.md` | `203-api-reference-anthropic-integration-list-models-anthropic-format.md` | identico |
| `167-api-reference-cache-clear-cache-by-cache-key.md` | `127-api-reference-cache-clear-cache-by-cache-key.md` | identico |
| `168-api-reference-cache-clear-cache-by-request-id.md` | `128-api-reference-cache-clear-cache-by-request-id.md` | identico |
| `128-api-reference-openai-integration-list-models-azure-openai.md` | `220-api-reference-openai-integration-list-models-azure-openai.md` | identico |
| `169-api-reference-chat-completions-create-a-chat-completion.md` | `129-api-reference-chat-completions-create-a-chat-completion.md` | identico |
| `129-api-reference-openai-integration-list-models-openai-format.md` | `221-api-reference-openai-integration-list-models-openai-format.md` | identico |
| `130-api-reference-bedrock-integration-converse-with-model-bedrock-format.md` | `235-api-reference-bedrock-integration-converse-with-model-bedrock-format.md` | identico |
| `170-api-reference-count-tokens-count-tokens.md` | `130-api-reference-count-tokens-count-tokens.md` | identico |
| `131-api-reference-bedrock-integration-invoke-model-bedrock-format.md` | `236-api-reference-bedrock-integration-invoke-model-bedrock-format.md` | identico |
| `171-api-reference-embeddings-create-embeddings.md` | `131-api-reference-embeddings-create-embeddings.md` | identico |
| `132-api-reference-bedrock-integration-invoke-model-with-streaming-bedrock-format.md` | `237-api-reference-bedrock-integration-invoke-model-with-streaming-bedrock-format.md` | identico |
| `172-api-reference-files-delete-a-file.md` | `132-api-reference-files-delete-a-file.md` | identico |
| `133-api-reference-bedrock-integration-stream-converse-with-model-bedrock-format.md` | `238-api-reference-bedrock-integration-stream-converse-with-model-bedrock-format.md` | identico |
| `173-api-reference-files-download-file-content.md` | `133-api-reference-files-download-file-content.md` | identico |
| `174-api-reference-files-retrieve-file-metadata.md` | `134-api-reference-files-retrieve-file-metadata.md` | identico |
| `134-api-reference-genai-integration-list-models-gemini-format.md` | `246-api-reference-genai-integration-list-models-gemini-format.md` | identico |
| `135-api-reference-cohere-integration-chat-with-model-cohere-v2-format.md` | `249-api-reference-cohere-integration-chat-with-model-cohere-v2-format.md` | identico |
| `175-api-reference-files-list-files.md` | `135-api-reference-files-list-files.md` | identico |
| `176-api-reference-files-upload-a-file.md` | `136-api-reference-files-upload-a-file.md` | identico |
| `136-api-reference-langchain-integration-chat-with-model-langchain-cohere-format.md` | `253-api-reference-langchain-integration-chat-with-model-langchain-cohere-format.md` | identico |
| `177-api-reference-health-health-check.md` | `137-api-reference-health-health-check.md` | identico |
| `137-api-reference-langchain-integration-converse-with-model-langchain-bedrock-format.md` | `254-api-reference-langchain-integration-converse-with-model-langchain-bedrock-format.md` | identico |
| `178-api-reference-image-generations-generate-image.md` | `138-api-reference-image-generations-generate-image.md` | identico |
| `138-api-reference-langchain-integration-list-models-langchain-gemini-format.md` | `261-api-reference-langchain-integration-list-models-langchain-gemini-format.md` | identico |
| `139-api-reference-langchain-integration-list-models-langchain-openai-format.md` | `262-api-reference-langchain-integration-list-models-langchain-openai-format.md` | identico |
| `140-api-reference-langchain-integration-stream-converse-with-model-langchain-bedrock-format.md` | `265-api-reference-langchain-integration-stream-converse-with-model-langchain-bedrock-format.md` | identico |
| `179-api-reference-responses-create-a-response.md` | `140-api-reference-responses-create-a-response.md` | identico |
| `141-api-reference-litellm-integration-chat-with-model-litellm-cohere-format.md` | `271-api-reference-litellm-integration-chat-with-model-litellm-cohere-format.md` | identico |
| `180-api-reference-text-completions-create-a-text-completion.md` | `141-api-reference-text-completions-create-a-text-completion.md` | identico |
| `142-api-reference-litellm-integration-converse-with-model-litellm-bedrock-format.md` | `272-api-reference-litellm-integration-converse-with-model-litellm-bedrock-format.md` | identico |
| `143-api-reference-litellm-integration-list-models-litellm-gemini-format.md` | `278-api-reference-litellm-integration-list-models-litellm-gemini-format.md` | identico |
| `144-api-reference-litellm-integration-list-models-litellm-openai-format.md` | `279-api-reference-litellm-integration-list-models-litellm-openai-format.md` | identico |
| `145-api-reference-litellm-integration-stream-converse-with-model-litellm-bedrock-format.md` | `282-api-reference-litellm-integration-stream-converse-with-model-litellm-bedrock-format.md` | identico |
| `146-api-reference-pydanticai-integration-chat-with-model-pydanticai-cohere-format.md` | `288-api-reference-pydanticai-integration-chat-with-model-pydanticai-cohere-format.md` | identico |
| `147-api-reference-pydanticai-integration-converse-with-model-pydanticai-bedrock-format.md` | `289-api-reference-pydanticai-integration-converse-with-model-pydanticai-bedrock-format.md` | identico |
| `181-api-reference-governance-list-budgets.md` | `148-api-reference-governance-list-budgets.md` | identico |
| `148-api-reference-pydanticai-integration-list-models-pydanticai-gemini-format.md` | `295-api-reference-pydanticai-integration-list-models-pydanticai-gemini-format.md` | identico |
| `182-api-reference-governance-get-customer.md` | `149-api-reference-governance-get-customer.md` | identico |
| `149-api-reference-pydanticai-integration-list-models-pydanticai-openai-format.md` | `296-api-reference-pydanticai-integration-list-models-pydanticai-openai-format.md` | identico |
| `183-api-reference-governance-create-customer.md` | `150-api-reference-governance-create-customer.md` | identico |
| `150-api-reference-pydanticai-integration-stream-converse-with-model-pydanticai-bedrock-format.md` | `299-api-reference-pydanticai-integration-stream-converse-with-model-pydanticai-bedrock-format.md` | identico |
| `184-api-reference-governance-update-customer.md` | `151-api-reference-governance-update-customer.md` | identico |
| `185-api-reference-governance-delete-customer.md` | `152-api-reference-governance-delete-customer.md` | identico |
| `186-api-reference-governance-list-customers.md` | `153-api-reference-governance-list-customers.md` | identico |
| `153-api-reference-session-login.md` | `190-api-reference-session-login.md` | identico |
| `187-api-reference-governance-list-rate-limits.md` | `154-api-reference-governance-list-rate-limits.md` | identico |
| `188-api-reference-governance-get-team.md` | `155-api-reference-governance-get-team.md` | identico |
| `189-api-reference-governance-create-team.md` | `156-api-reference-governance-create-team.md` | identico |
| `190-api-reference-governance-update-team.md` | `157-api-reference-governance-update-team.md` | identico |
| `191-api-reference-governance-delete-team.md` | `158-api-reference-governance-delete-team.md` | identico |
| `192-api-reference-governance-list-teams.md` | `159-api-reference-governance-list-teams.md` | identico |
| `193-api-reference-governance-get-virtual-key.md` | `160-api-reference-governance-get-virtual-key.md` | identico |
| `194-api-reference-governance-create-virtual-key.md` | `161-api-reference-governance-create-virtual-key.md` | identico |
| `195-api-reference-governance-update-virtual-key.md` | `162-api-reference-governance-update-virtual-key.md` | identico |
| `196-api-reference-governance-delete-virtual-key.md` | `163-api-reference-governance-delete-virtual-key.md` | identico |
| `197-api-reference-governance-list-virtual-keys.md` | `164-api-reference-governance-list-virtual-keys.md` | identico |
| `198-api-reference-logging-get-available-filter-data.md` | `165-api-reference-logging-get-available-filter-data.md` | identico |
| `199-api-reference-logging-get-dropped-requests-count.md` | `166-api-reference-logging-get-dropped-requests-count.md` | identico |
| `200-api-reference-logging-get-log-statistics.md` | `167-api-reference-logging-get-log-statistics.md` | identico |
| `201-api-reference-logging-get-logs.md` | `168-api-reference-logging-get-logs.md` | identico |
| `202-api-reference-logging-delete-logs.md` | `169-api-reference-logging-delete-logs.md` | identico |
| `203-api-reference-logging-recalculate-log-costs.md` | `170-api-reference-logging-recalculate-log-costs.md` | identico |
| `204-api-reference-session-check-if-authentication-is-enabled.md` | `189-api-reference-session-check-if-authentication-is-enabled.md` | identico |
| `205-api-reference-session-logout.md` | `191-api-reference-session-logout.md` | identico |
| `206-api-reference-anthropic-integration-retrieve-batch-job-anthropic-format.md` | `192-api-reference-anthropic-integration-retrieve-batch-job-anthropic-format.md` | identico |
| `207-api-reference-anthropic-integration-create-batch-job-anthropic-format.md` | `193-api-reference-anthropic-integration-create-batch-job-anthropic-format.md` | identico |
| `208-api-reference-anthropic-integration-cancel-batch-job-anthropic-format.md` | `194-api-reference-anthropic-integration-cancel-batch-job-anthropic-format.md` | identico |
| `209-api-reference-anthropic-integration-list-batch-jobs-anthropic-format.md` | `195-api-reference-anthropic-integration-list-batch-jobs-anthropic-format.md` | identico |
| `210-api-reference-anthropic-integration-get-batch-results-anthropic-format.md` | `196-api-reference-anthropic-integration-get-batch-results-anthropic-format.md` | identico |
| `211-api-reference-anthropic-integration-create-completion-anthropic-legacy-format.md` | `197-api-reference-anthropic-integration-create-completion-anthropic-legacy-format.md` | identico |
| `212-api-reference-anthropic-integration-count-tokens-anthropic-format.md` | `198-api-reference-anthropic-integration-count-tokens-anthropic-format.md` | identico |
| `213-api-reference-anthropic-integration-delete-file-anthropic-format.md` | `199-api-reference-anthropic-integration-delete-file-anthropic-format.md` | identico |
| `214-api-reference-anthropic-integration-get-file-content-anthropic-format.md` | `200-api-reference-anthropic-integration-get-file-content-anthropic-format.md` | identico |
| `215-api-reference-anthropic-integration-list-files-anthropic-format.md` | `201-api-reference-anthropic-integration-list-files-anthropic-format.md` | identico |
| `216-api-reference-anthropic-integration-create-message-anthropic-format.md` | `202-api-reference-anthropic-integration-create-message-anthropic-format.md` | identico |
| `217-api-reference-anthropic-integration-upload-file-anthropic-format.md` | `204-api-reference-anthropic-integration-upload-file-anthropic-format.md` | identico |
| `218-api-reference-openai-integration-retrieve-batch-job-openai-format.md` | `205-api-reference-openai-integration-retrieve-batch-job-openai-format.md` | identico |
| `219-api-reference-openai-integration-create-batch-job-openai-format.md` | `206-api-reference-openai-integration-create-batch-job-openai-format.md` | identico |
| `220-api-reference-openai-integration-cancel-batch-job-openai-format.md` | `207-api-reference-openai-integration-cancel-batch-job-openai-format.md` | identico |
| `221-api-reference-openai-integration-list-batch-jobs-openai-format.md` | `208-api-reference-openai-integration-list-batch-jobs-openai-format.md` | identico |
| `222-api-reference-openai-integration-create-chat-completion-azure-openai.md` | `209-api-reference-openai-integration-create-chat-completion-azure-openai.md` | identico |
| `223-api-reference-openai-integration-create-chat-completion-openai-format.md` | `210-api-reference-openai-integration-create-chat-completion-openai-format.md` | identico |
| `224-api-reference-openai-integration-count-input-tokens.md` | `211-api-reference-openai-integration-count-input-tokens.md` | identico |
| `225-api-reference-openai-integration-create-embeddings-azure-openai.md` | `212-api-reference-openai-integration-create-embeddings-azure-openai.md` | identico |
| `226-api-reference-openai-integration-create-embeddings-openai-format.md` | `213-api-reference-openai-integration-create-embeddings-openai-format.md` | identico |
| `227-api-reference-openai-integration-get-file-content-openai-format.md` | `214-api-reference-openai-integration-get-file-content-openai-format.md` | identico |
| `228-api-reference-openai-integration-retrieve-file-metadata-openai-format.md` | `215-api-reference-openai-integration-retrieve-file-metadata-openai-format.md` | identico |
| `229-api-reference-openai-integration-delete-file-openai-format.md` | `216-api-reference-openai-integration-delete-file-openai-format.md` | identico |
| `230-api-reference-openai-integration-list-files-openai-format.md` | `217-api-reference-openai-integration-list-files-openai-format.md` | identico |
| `231-api-reference-openai-integration-create-image-azure-openai.md` | `218-api-reference-openai-integration-create-image-azure-openai.md` | identico |
| `232-api-reference-openai-integration-create-image.md` | `219-api-reference-openai-integration-create-image.md` | identico |
| `233-api-reference-openai-integration-create-response-azure-openai.md` | `222-api-reference-openai-integration-create-response-azure-openai.md` | identico |
| `234-api-reference-openai-integration-create-response-openai-responses-api.md` | `223-api-reference-openai-integration-create-response-openai-responses-api.md` | identico |
| `235-api-reference-openai-integration-create-speech-azure-openai-tts.md` | `224-api-reference-openai-integration-create-speech-azure-openai-tts.md` | identico |
| `236-api-reference-openai-integration-create-speech-openai-tts.md` | `225-api-reference-openai-integration-create-speech-openai-tts.md` | identico |
| `237-api-reference-openai-integration-create-text-completion-azure-openai.md` | `226-api-reference-openai-integration-create-text-completion-azure-openai.md` | identico |
| `238-api-reference-openai-integration-create-text-completion-openai-format.md` | `227-api-reference-openai-integration-create-text-completion-openai-format.md` | identico |
| `239-api-reference-openai-integration-create-transcription-azure-openai.md` | `228-api-reference-openai-integration-create-transcription-azure-openai.md` | identico |
| `240-api-reference-openai-integration-create-transcription-openai-whisper.md` | `229-api-reference-openai-integration-create-transcription-openai-whisper.md` | identico |
| `241-api-reference-openai-integration-upload-file-openai-format.md` | `230-api-reference-openai-integration-upload-file-openai-format.md` | identico |
| `242-api-reference-bedrock-integration-retrieve-batch-inference-job-bedrock-format.md` | `231-api-reference-bedrock-integration-retrieve-batch-inference-job-bedrock-format.md` | identico |
| `243-api-reference-bedrock-integration-create-batch-inference-job-bedrock-format.md` | `232-api-reference-bedrock-integration-create-batch-inference-job-bedrock-format.md` | identico |
| `244-api-reference-bedrock-integration-cancel-batch-inference-job-bedrock-format.md` | `233-api-reference-bedrock-integration-cancel-batch-inference-job-bedrock-format.md` | identico |
| `245-api-reference-bedrock-integration-list-batch-inference-jobs-bedrock-format.md` | `234-api-reference-bedrock-integration-list-batch-inference-jobs-bedrock-format.md` | identico |
| `246-api-reference-genai-integration-count-tokens-gemini-format.md` | `239-api-reference-genai-integration-count-tokens-gemini-format.md` | identico |
| `247-api-reference-genai-integration-embed-content-gemini-format.md` | `240-api-reference-genai-integration-embed-content-gemini-format.md` | identico |
| `248-api-reference-genai-integration-retrieve-file-gemini-format.md` | `241-api-reference-genai-integration-retrieve-file-gemini-format.md` | identico |
| `249-api-reference-genai-integration-delete-file-gemini-format.md` | `242-api-reference-genai-integration-delete-file-gemini-format.md` | identico |
| `250-api-reference-genai-integration-list-files-gemini-format.md` | `243-api-reference-genai-integration-list-files-gemini-format.md` | identico |
| `251-api-reference-genai-integration-generate-content-gemini-format.md` | `244-api-reference-genai-integration-generate-content-gemini-format.md` | identico |
| `252-api-reference-genai-integration-generate-image-gemini-format.md` | `245-api-reference-genai-integration-generate-image-gemini-format.md` | identico |
| `253-api-reference-genai-integration-stream-generate-content-gemini-format.md` | `247-api-reference-genai-integration-stream-generate-content-gemini-format.md` | identico |
| `254-api-reference-genai-integration-upload-file-gemini-format.md` | `248-api-reference-genai-integration-upload-file-gemini-format.md` | identico |
| `255-api-reference-cohere-integration-create-embeddings-cohere-v2-format.md` | `250-api-reference-cohere-integration-create-embeddings-cohere-v2-format.md` | identico |
| `256-api-reference-cohere-integration-tokenize-text-cohere-format.md` | `251-api-reference-cohere-integration-tokenize-text-cohere-format.md` | identico |
| `257-api-reference-langchain-integration-chat-completions-langchain-openai-format.md` | `252-api-reference-langchain-integration-chat-completions-langchain-openai-format.md` | identico |
| `258-api-reference-langchain-integration-count-input-tokens-langchain-openai-format.md` | `255-api-reference-langchain-integration-count-input-tokens-langchain-openai-format.md` | identico |
| `259-api-reference-langchain-integration-count-tokens-langchain-anthropic-format.md` | `256-api-reference-langchain-integration-count-tokens-langchain-anthropic-format.md` | identico |
| `260-api-reference-langchain-integration-create-embeddings-langchain-cohere-format.md` | `257-api-reference-langchain-integration-create-embeddings-langchain-cohere-format.md` | identico |
| `261-api-reference-langchain-integration-create-embeddings-langchain-openai-format.md` | `258-api-reference-langchain-integration-create-embeddings-langchain-openai-format.md` | identico |
| `262-api-reference-langchain-integration-generate-content-langchain-gemini-format.md` | `259-api-reference-langchain-integration-generate-content-langchain-gemini-format.md` | identico |
| `263-api-reference-langchain-integration-create-message-langchain-anthropic-format.md` | `260-api-reference-langchain-integration-create-message-langchain-anthropic-format.md` | identico |
| `264-api-reference-langchain-integration-create-response-langchain-openai-responses-api.md` | `263-api-reference-langchain-integration-create-response-langchain-openai-responses-api.md` | identico |
| `265-api-reference-langchain-integration-create-speech-langchain-openai-tts.md` | `264-api-reference-langchain-integration-create-speech-langchain-openai-tts.md` | identico |
| `271-api-reference-litellm-integration-count-input-tokens-litellm-openai-format.md` | `273-api-reference-litellm-integration-count-input-tokens-litellm-openai-format.md` | identico |
| `272-api-reference-litellm-integration-create-embeddings-litellm-cohere-format.md` | `274-api-reference-litellm-integration-create-embeddings-litellm-cohere-format.md` | identico |
| `273-api-reference-litellm-integration-create-embeddings-litellm-openai-format.md` | `275-api-reference-litellm-integration-create-embeddings-litellm-openai-format.md` | identico |
| `274-api-reference-litellm-integration-generate-content-litellm-gemini-format.md` | `276-api-reference-litellm-integration-generate-content-litellm-gemini-format.md` | identico |
| `275-api-reference-litellm-integration-create-message-litellm-anthropic-format.md` | `277-api-reference-litellm-integration-create-message-litellm-anthropic-format.md` | identico |
| `276-api-reference-litellm-integration-create-response-litellm-openai-responses-api.md` | `280-api-reference-litellm-integration-create-response-litellm-openai-responses-api.md` | identico |
| `277-api-reference-litellm-integration-create-speech-litellm-openai-tts.md` | `281-api-reference-litellm-integration-create-speech-litellm-openai-tts.md` | identico |
| `278-api-reference-litellm-integration-stream-generate-content-litellm-gemini-format.md` | `283-api-reference-litellm-integration-stream-generate-content-litellm-gemini-format.md` | identico |
| `279-api-reference-litellm-integration-text-completions-litellm-openai-format.md` | `284-api-reference-litellm-integration-text-completions-litellm-openai-format.md` | identico |
| `280-api-reference-litellm-integration-tokenize-text-litellm-cohere-format.md` | `285-api-reference-litellm-integration-tokenize-text-litellm-cohere-format.md` | identico |
| `281-api-reference-litellm-integration-create-transcription-litellm-openai-whisper.md` | `286-api-reference-litellm-integration-create-transcription-litellm-openai-whisper.md` | identico |
| `282-api-reference-pydanticai-integration-chat-completions-pydanticai-openai-format.md` | `287-api-reference-pydanticai-integration-chat-completions-pydanticai-openai-format.md` | identico |
| `283-api-reference-pydanticai-integration-count-input-tokens-pydanticai-openai-format.md` | `290-api-reference-pydanticai-integration-count-input-tokens-pydanticai-openai-format.md` | identico |
| `284-api-reference-pydanticai-integration-create-embeddings-pydanticai-cohere-format.md` | `291-api-reference-pydanticai-integration-create-embeddings-pydanticai-cohere-format.md` | identico |
| `285-api-reference-pydanticai-integration-create-embeddings-pydanticai-openai-format.md` | `292-api-reference-pydanticai-integration-create-embeddings-pydanticai-openai-format.md` | identico |
| `286-api-reference-pydanticai-integration-generate-content-pydanticai-gemini-format.md` | `293-api-reference-pydanticai-integration-generate-content-pydanticai-gemini-format.md` | identico |
| `287-api-reference-pydanticai-integration-create-message-pydanticai-anthropic-format.md` | `294-api-reference-pydanticai-integration-create-message-pydanticai-anthropic-format.md` | identico |
| `288-api-reference-pydanticai-integration-create-response-pydanticai-openai-responses-api.md` | `297-api-reference-pydanticai-integration-create-response-pydanticai-openai-responses-api.md` | identico |
| `289-api-reference-pydanticai-integration-create-speech-pydanticai-openai-tts.md` | `298-api-reference-pydanticai-integration-create-speech-pydanticai-openai-tts.md` | identico |
| `290-api-reference-pydanticai-integration-stream-generate-content-pydanticai-gemini-format.md` | `300-api-reference-pydanticai-integration-stream-generate-content-pydanticai-gemini-format.md` | identico |
| `291-api-reference-pydanticai-integration-text-completions-pydanticai-openai-format.md` | `301-api-reference-pydanticai-integration-text-completions-pydanticai-openai-format.md` | identico |
| `292-api-reference-pydanticai-integration-tokenize-text-pydanticai-cohere-format.md` | `302-api-reference-pydanticai-integration-tokenize-text-pydanticai-cohere-format.md` | identico |
| `293-api-reference-pydanticai-integration-create-transcription-pydanticai-openai-whisper.md` | `303-api-reference-pydanticai-integration-create-transcription-pydanticai-openai-whisper.md` | identico |
| `301-changelogs-v1.4.1.md` | `304-changelogs-v1.4.1.md` | identico |
| `302-changelogs-v1.4.0.md` | `305-changelogs-v1.4.0.md` | identico |
| `303-changelogs-v1.4.0-prerelease10.md` | `306-changelogs-v1.4.0-prerelease10.md` | identico |
| `304-changelogs-v1.4.0-prerelease9.md` | `307-changelogs-v1.4.0-prerelease9.md` | identico |
| `305-changelogs-v1.4.0-prerelease8.md` | `308-changelogs-v1.4.0-prerelease8.md` | identico |
| `306-changelogs-v1.4.0-prerelease7.md` | `309-changelogs-v1.4.0-prerelease7.md` | identico |
| `307-changelogs-v1.4.0-prerelease6.md` | `310-changelogs-v1.4.0-prerelease6.md` | identico |
| `308-changelogs-v1.4.0-prerelease5.md` | `311-changelogs-v1.4.0-prerelease5.md` | identico |
| `309-changelogs-v1.4.0-prerelease4.md` | `312-changelogs-v1.4.0-prerelease4.md` | identico |
| `310-changelogs-v1.4.0-prerelease3.md` | `313-changelogs-v1.4.0-prerelease3.md` | identico |
| `311-changelogs-v1.4.0-prerelease2.md` | `314-changelogs-v1.4.0-prerelease2.md` | identico |
| `312-changelogs-v1.4.0-prerelease1.md` | `315-changelogs-v1.4.0-prerelease1.md` | identico |
| `313-changelogs-v1.3.63.md` | `316-changelogs-v1.3.63.md` | identico |
| `314-changelogs-v1.3.62.md` | `317-changelogs-v1.3.62.md` | identico |
| `315-changelogs-v1.3.61.md` | `318-changelogs-v1.3.61.md` | identico |
| `316-changelogs-v1.3.60.md` | `319-changelogs-v1.3.60.md` | identico |
| `317-changelogs-v1.3.59.md` | `320-changelogs-v1.3.59.md` | identico |
| `318-changelogs-v1.3.58.md` | `321-changelogs-v1.3.58.md` | identico |
| `319-changelogs-v1.3.57.md` | `322-changelogs-v1.3.57.md` | identico |
| `320-changelogs-v1.3.56.md` | `323-changelogs-v1.3.56.md` | identico |
| `321-changelogs-v1.3.54.md` | `324-changelogs-v1.3.54.md` | identico |
| `322-changelogs-v1.3.53.md` | `325-changelogs-v1.3.53.md` | identico |
| `323-changelogs-v1.3.52.md` | `326-changelogs-v1.3.52.md` | identico |
| `324-changelogs-v1.3.51.md` | `327-changelogs-v1.3.51.md` | identico |
| `325-changelogs-v1.3.50.md` | `328-changelogs-v1.3.50.md` | identico |
| `326-changelogs-v1.3.49.md` | `329-changelogs-v1.3.49.md` | identico |
| `327-changelogs-v1.3.48.md` | `330-changelogs-v1.3.48.md` | identico |
| `328-changelogs-v1.3.47.md` | `331-changelogs-v1.3.47.md` | identico |
| `329-changelogs-v1.3.46.md` | `332-changelogs-v1.3.46.md` | identico |
| `330-changelogs-v1.3.45.md` | `333-changelogs-v1.3.45.md` | identico |
| `331-changelogs-v1.3.44.md` | `334-changelogs-v1.3.44.md` | identico |
| `332-changelogs-v1.3.43.md` | `335-changelogs-v1.3.43.md` | identico |
| `333-changelogs-v1.3.42.md` | `336-changelogs-v1.3.42.md` | identico |
| `334-changelogs-v1.3.41.md` | `337-changelogs-v1.3.41.md` | identico |
| `335-changelogs-v1.3.40.md` | `338-changelogs-v1.3.40.md` | identico |
| `336-changelogs-v1.3.39.md` | `339-changelogs-v1.3.39.md` | identico |
| `337-changelogs-v1.3.38.md` | `340-changelogs-v1.3.38.md` | identico |
| `338-changelogs-v1.3.37.md` | `341-changelogs-v1.3.37.md` | identico |
| `339-changelogs-v1.3.36.md` | `342-changelogs-v1.3.36.md` | identico |
| `340-changelogs-v1.3.35.md` | `343-changelogs-v1.3.35.md` | identico |
| `341-changelogs-v1.3.34.md` | `344-changelogs-v1.3.34.md` | identico |
| `342-changelogs-v1.3.33.md` | `345-changelogs-v1.3.33.md` | identico |
| `343-changelogs-v1.3.32.md` | `346-changelogs-v1.3.32.md` | identico |
| `344-changelogs-v1.3.31.md` | `347-changelogs-v1.3.31.md` | identico |
| `345-changelogs-v1.3.30.md` | `348-changelogs-v1.3.30.md` | identico |
| `346-changelogs-v1.3.29.md` | `349-changelogs-v1.3.29.md` | identico |
| `347-changelogs-v1.3.28.md` | `350-changelogs-v1.3.28.md` | identico |
| `348-changelogs-v1.3.27.md` | `351-changelogs-v1.3.27.md` | identico |
| `349-changelogs-v1.3.26.md` | `352-changelogs-v1.3.26.md` | identico |
| `350-changelogs-v1.3.25.md` | `353-changelogs-v1.3.25.md` | identico |
| `351-changelogs-v1.3.24.md` | `354-changelogs-v1.3.24.md` | identico |
| `352-changelogs-v1.3.23.md` | `355-changelogs-v1.3.23.md` | identico |
| `353-changelogs-v1.3.22.md` | `356-changelogs-v1.3.22.md` | identico |
| `354-changelogs-v1.3.21.md` | `357-changelogs-v1.3.21.md` | identico |
| `355-changelogs-v1.3.20.md` | `358-changelogs-v1.3.20.md` | identico |
| `356-changelogs-v1.3.19.md` | `359-changelogs-v1.3.19.md` | identico |
| `357-changelogs-v1.3.18.md` | `360-changelogs-v1.3.18.md` | identico |
| `358-changelogs-v1.3.17.md` | `361-changelogs-v1.3.17.md` | identico |
| `359-changelogs-v1.3.16.md` | `362-changelogs-v1.3.16.md` | identico |
| `360-changelogs-v1.3.15.md` | `363-changelogs-v1.3.15.md` | identico |
| `361-changelogs-v1.3.14.md` | `364-changelogs-v1.3.14.md` | identico |
| `362-changelogs-v1.3.13.md` | `365-changelogs-v1.3.13.md` | identico |
| `363-changelogs-v1.3.12.md` | `366-changelogs-v1.3.12.md` | identico |
| `364-changelogs-v1.3.11.md` | `367-changelogs-v1.3.11.md` | identico |
| `365-changelogs-v1.3.10.md` | `368-changelogs-v1.3.10.md` | identico |
| `366-changelogs-v1.3.9.md` | `369-changelogs-v1.3.9.md` | identico |
| `367-changelogs-v1.3.8.md` | `370-changelogs-v1.3.8.md` | identico |
| `368-changelogs-v1.3.7.md` | `371-changelogs-v1.3.7.md` | identico |
| `369-changelogs-v1.3.6.md` | `372-changelogs-v1.3.6.md` | identico |
| `370-changelogs-v1.3.5.md` | `373-changelogs-v1.3.5.md` | identico |
| `371-changelogs-v1.3.4.md` | `374-changelogs-v1.3.4.md` | identico |
| `372-changelogs-v1.3.3.md` | `375-changelogs-v1.3.3.md` | identico |
| `373-changelogs-v1.3.2.md` | `376-changelogs-v1.3.2.md` | identico |
| `374-changelogs-v1.3.1.md` | `377-changelogs-v1.3.1.md` | identico |
| `375-changelogs-v1.3.0.md` | `378-changelogs-v1.3.0.md` | identico |
| `376-changelogs-v1.3.0-prerelease7.md` | `379-changelogs-v1.3.0-prerelease7.md` | identico |
| `377-changelogs-v1.3.0-prerelease6.md` | `380-changelogs-v1.3.0-prerelease6.md` | identico |
| `378-changelogs-v1.3.0-prerelease5.md` | `381-changelogs-v1.3.0-prerelease5.md` | identico |
| `379-changelogs-v1.3.0-prerelease4.md` | `382-changelogs-v1.3.0-prerelease4.md` | identico |
| `380-changelogs-v1.3.0-prerelease3.md` | `383-changelogs-v1.3.0-prerelease3.md` | identico |
| `381-changelogs-v1.3.0-prerelease2.md` | `384-changelogs-v1.3.0-prerelease2.md` | identico |
| `382-changelogs-v1.3.0-prerelease1.md` | `385-changelogs-v1.3.0-prerelease1.md` | identico |
| `383-changelogs-v1.2.24.md` | `386-changelogs-v1.2.24.md` | identico |
| `384-changelogs-v1.2.23.md` | `387-changelogs-v1.2.23.md` | identico |
| `385-changelogs-v1.2.22.md` | `388-changelogs-v1.2.22.md` | identico |

---

*Auto-generated. Files numbered sequentially following a content-driven learning progression.*
