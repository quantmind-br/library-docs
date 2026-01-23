---
description: Auto-generated Bifrost documentation index
generated: 2026-01-22T16:14:27.791Z
source: https://docs.getbifrost.ai/llms.txt
total_docs: 389
categories: 24
---

# Bifrost Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from quickstart to advanced topics.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.getbifrost.ai/llms.txt |
| **Generated** | 2026-01-22 |
| **Total Documents** | 389 |
| **Strategy** | llms |
| **Categories** | 24 |

---

## Document Index

### 1. Meta & Resources (001-002)
*Project links and resources*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-bifrost-discord.md` | Discord | This document provides a redirection notice indicating that the content has been moved to a new loca... | redirection, http-302, document-moved, discord |
| 002 | `002-bifrost-enterprise.md` | Bifrost - AI Gateway | This document is empty and contains no text or instructions to analyze. | empty-document, no-content, placeholder |

### 2. Gateway Quickstart (003-010)
*Getting started with Bifrost Gateway*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-quickstart-gateway-setting-up.md` | Setting Up | This document provides a step-by-step guide for installing and configuring Bifrost, an HTTP API gate... | installation, docker, npx, api-gateway |
| 004 | `004-quickstart-gateway-setting-up-auth.md` | Setting up auth | This document provides instructions for enabling and managing basic authentication to secure the Bif... | bifrost-security, authentication-setup, dashboard-access, api-security |
| 005 | `005-quickstart-gateway-cli-agents.md` | Tools, Editors & CLI Agents | This document provides instructions on integrating Bifrost with various AI agents and CLI tools by c... | agent-integration, cli-tools, model-compatibility, api-proxy |
| 006 | `006-quickstart-gateway-integrations.md` | Integrations | This document explains how Bifrost integrations act as protocol adapters to provide drop-in compatib... | ai-integrations, sdk-compatibility, drop-in-replacement, bifrost-api |
| 007 | `007-quickstart-gateway-multimodal.md` | Multimodal Support | This document outlines how to implement multimodal features such as vision analysis, image generatio... | multimodal-ai, vision-analysis, image-generation, speech-to-text |
| 008 | `008-quickstart-gateway-provider-configuration.md` | Provider Configuration | This document explains how to set up and manage multiple AI model providers using the Web UI, API, o... | provider-configuration, ai-models, load-balancing, api-keys |
| 009 | `009-quickstart-gateway-streaming.md` | Streaming Responses | This document explains how to implement real-time streaming for text completions, chat, and audio pr... | streaming-responses, server-sent-events, real-time-api, chat-completions |
| 010 | `010-quickstart-gateway-tool-calling.md` | Tool Calling | This document explains how to enable AI models to interact with external services through custom fun... | tool-calling, function-calling, mcp-server, api-integration |

### 3. Go SDK Quickstart (011-017)
*Getting started with Bifrost Go SDK*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 011 | `011-quickstart-go-sdk-setting-up.md` | Setting Up | This document provides a quick-start guide for integrating the Bifrost AI gateway into a Go applicat... | go-sdk, bifrost-setup, quick-start, ai-gateway |
| 012 | `012-quickstart-go-sdk-context-keys.md` | Context Keys | This document explains how to use Go context keys in Bifrost to configure request behavior and acces... | go-sdk, context-keys, request-configuration, response-metadata |
| 013 | `013-quickstart-go-sdk-logger.md` | Logging | This document explains how to configure and customize logging within the Bifrost integration, coveri... | logging, bifrost, debugging, monitoring |
| 014 | `014-quickstart-go-sdk-multimodal.md` | Multimodal Support | This document explains how to implement multimodal capabilities using the Bifrost SDK, including vis... | multimodal, vision-analysis, image-generation, speech-to-text |
| 015 | `015-quickstart-go-sdk-provider-configuration.md` | Provider Configuration | This document explains how to configure multiple AI providers, including managing API keys, weighted... | ai-providers, load-balancing, api-keys, concurrency-control |
| 016 | `016-quickstart-go-sdk-streaming.md` | Streaming Responses | This document explains how to implement real-time streaming for text, chat, speech synthesis, and tr... | streaming-api, real-time-responses, go-sdk, text-to-speech |
| 017 | `017-quickstart-go-sdk-tool-calling.md` | Tool Calling | This document explains how to enable AI models to interact with external functions and services by d... | tool-calling, mcp, function-calling, go |

### 4. SDK Integrations (018-028)
*Integration with popular AI frameworks and SDKs*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 018 | `018-integrations-what-is-an-integration.md` | What is an integration? | This document defines Bifrost integrations as protocol adapters that translate between a unified gat... | integrations, protocol-adapters, api-gateway, llm-providers |
| 019 | `019-integrations-anthropic-sdk-overview.md` | Overview | This document explains how to use Bifrost as a drop-in replacement for the Anthropic API, enabling m... | anthropic-api, api-proxy, multi-provider, sdk-integration |
| 020 | `020-integrations-bedrock-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a Bedrock-compatible gateway using the Converse a... | aws-bedrock, bifrost-gateway, boto3-integration, api-protocol-adaptation |
| 021 | `021-integrations-genai-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a drop-in replacement for the Google GenAI API, e... | google-genai-api, api-compatibility, multi-provider, bifrost-integration |
| 022 | `022-integrations-openai-sdk-overview.md` | Overview | This document explains how to integrate Bifrost as a drop-in replacement for the OpenAI API, allowin... | openai-compatibility, multi-provider, api-gateway, sdk-integration |
| 023 | `023-integrations-anthropic-sdk-files-and-batch.md` | Files and Batch API | This document explains how to utilize the Anthropic SDK with Bifrost to perform cross-provider file ... | anthropic-sdk, batch-api, files-api, cross-provider-routing |
| 024 | `024-integrations-bedrock-sdk-files-and-batch.md` | Files and Batch API | This document explains how to use the AWS Bedrock SDK (boto3) with Bifrost to manage files and batch... | aws-bedrock, boto3, batch-inference, file-management |
| 025 | `025-integrations-langchain-sdk.md` | Langchain SDK | This document provides instructions on integrating Bifrost as a drop-in proxy for Langchain applicat... | langchain, sdk-integration, proxy-setup, python |
| 026 | `026-integrations-litellm-sdk.md` | LiteLLM SDK | This document explains how to integrate the LiteLLM SDK with Bifrost to add enterprise features like... | litellm-sdk, bifrost-proxy, multi-provider-ai, api-governance |
| 027 | `027-integrations-openai-sdk-files-and-batch.md` | Files and Batch API | This document explains how to use Bifrost to manage files and execute asynchronous batch jobs across... | bifrost, openai-sdk, files-api, batch-api |
| 028 | `028-integrations-pydanticai-sdk.md` | Pydantic AI SDK | This document explains how to integrate the Pydantic AI SDK with Bifrost as a drop-in proxy to enabl... | pydantic-ai, bifrost, python-sdk, llm-agents |

### 5. Features (029-043)
*Core features and capabilities*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 029 | `029-features-drop-in-replacement.md` | Drop-in Replacement | This document explains how to integrate the Bifrost Gateway as a drop-in replacement for popular AI ... | ai-gateway, sdk-integration, drop-in-replacement, load-balancing |
| 030 | `030-features-fallbacks.md` | Fallbacks | This document explains how Bifrost manages automatic failover between different AI providers and mod... | automatic-failover, ai-provider-switching, error-handling, high-availability |
| 031 | `031-features-governance-budget-and-limits.md` | Budget and Limits | This document explains Bifrost's hierarchical budget management and rate-limiting system, detailing ... | budget-management, cost-control, rate-limiting, virtual-keys |
| 032 | `032-features-governance-mcp-tools.md` | MCP Tool Filtering | This document explains how to restrict and manage access to Model Context Protocol (MCP) tools using... | mcp-tools, virtual-keys, tool-filtering, access-control |
| 033 | `033-features-governance-routing.md` | Routing | This document explains how to configure governance-based routing for AI models and providers using V... | routing, virtual-keys, load-balancing, failover |
| 034 | `034-features-governance-virtual-keys.md` | Virtual Keys | This document explains how to use Virtual Keys as a governance entity to manage AI model access, aut... | virtual-keys, access-control, governance, rate-limiting |
| 035 | `035-features-keys-management.md` | Load Balance | This document explains how to implement intelligent API key management using weighted load balancing... | load-balancing, api-key-management, traffic-distribution, failover |
| 036 | `036-features-litellm-compat.md` | LiteLLM Compatibility | This document explains the LiteLLM compatibility plugin, which provides automatic text-to-chat conve... | litellm-compatibility, text-to-chat, tool-calls, api-transformation |
| 037 | `037-features-observability-default.md` | Built-in Observability | This document explains Bifrost's built-in observability system, which provides real-time tracing and... | observability, request-tracing, monitoring, performance-metrics |
| 038 | `038-features-observability-maxim.md` | Maxim AI | Explains how to integrate and configure the Maxim AI plugin with Bifrost for comprehensive LLM obser... | maxim-ai, bifrost, llm-observability, tracing |
| 039 | `039-features-observability-otel.md` | OpenTelemetry (OTel) | This document explains how to integrate Bifrost with OpenTelemetry collectors to enable distributed ... | opentelemetry, otel, distributed-tracing, observability |
| 040 | `040-features-plugins-jsonparser.md` | JSON Parser | This document explains the Bifrost JSON Parser plugin, which automatically repairs partial JSON chun... | bifrost-plugin, json-parsing, streaming-responses, ai-integration |
| 041 | `041-features-plugins-mocker.md` | Mocker | This document provides instructions for using the Mocker plugin to simulate AI provider responses, c... | ai-mocking, go, bifrost, testing |
| 042 | `042-features-semantic-caching.md` | Semantic Caching | This document explains how to implement semantic caching using vector similarity search to reduce AI... | semantic-caching, vector-search, ai-infrastructure, performance-optimization |
| 043 | `043-features-telemetry.md` | Telemetry | This document details the Prometheus-based telemetry system for Bifrost Gateway, covering HTTP trans... | prometheus, monitoring, telemetry, ai-gateway |

### 6. Model Context Protocol (044-051)
*MCP integration for agentic tools*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 044 | `044-mcp-overview.md` | Overview | This document provides an overview of the Model Context Protocol (MCP) integration in Bifrost, expla... | model-context-protocol, mcp-server, tool-execution, ai-agents |
| 045 | `045-mcp-agent-mode.md` | Agent Mode (Auto-Execution) | This document explains how to enable and configure Agent Mode for autonomous tool execution, allowin... | agent-mode, autonomous-execution, tool-calling, mcp-gateway |
| 046 | `046-mcp-code-mode.md` | Code Mode | This document explains Code Mode, a feature that optimizes LLM tool orchestration by using TypeScrip... | mcp-server, code-mode, token-optimization, typescript-orchestration |
| 047 | `047-mcp-connecting-to-servers.md` | Connecting to MCP Servers | This document explains how to connect Bifrost to external MCP servers using STDIO, HTTP, and SSE pro... | mcp-server, connection-protocols, bifrost-gateway, stdio-connection |
| 048 | `048-mcp-filtering.md` | Tool Filtering | This document explains how to control MCP tool availability in Bifrost through three hierarchical le... | mcp, tool-filtering, access-control, bifrost-gateway |
| 049 | `049-mcp-gateway-url.md` | MCP Gateway URL | This document explains how to expose Bifrost Gateway as an MCP server for external clients, covering... | mcp-server, bifrost-gateway, json-rpc, sse-stream |
| 050 | `050-mcp-tool-execution.md` | Tool Execution | Explains how to manually execute Model Context Protocol (MCP) tools within the Bifrost platform to m... | mcp, tool-execution, workflow-control, bifrost |
| 051 | `051-mcp-tool-hosting.md` | Tool Hosting | This document explains how to register and host custom tools directly within a Go application using ... | go-sdk, tool-hosting, mcp-server, custom-tools |

### 7. Plugins (052-056)
*Plugin development and management*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 052 | `052-plugins-getting-started.md` | Getting Started | This document introduces Bifrost's plugin system, explaining how to extend gateway functionality by ... | bifrost-gateway, go-plugins, dynamic-loading, shared-objects |
| 053 | `053-plugins-building-dynamic-binary.md` | Building Dynamically Linked Bifrost Binary | This document explains how to compile a dynamically linked Bifrost binary to enable support for cust... | bifrost, dynamic-linking, go-plugins, compilation |
| 054 | `054-plugins-migration-guide.md` | Plugin Migration Guide | This document provides instructions and code examples for migrating Bifrost plugins from v1.3.x to v... | bifrost, plugin-migration, golang, http-transport |
| 055 | `055-plugins-writing-go-plugin.md` | Writing Go Plugins | This guide provides step-by-step instructions for developing native Go plugins for Bifrost using sha... | go-plugins, bifrost, shared-objects, middleware |
| 056 | `056-plugins-writing-wasm-plugin.md` | Writing WASM Plugins | This document explains how to build cross-platform WebAssembly plugins for the Bifrost Enterprise pl... | webassembly, wasm-plugins, bifrost-enterprise, plugin-development |

### 8. Providers (057-080)
*AI provider configurations and routing*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 057 | `057-providers-supported-providers-overview.md` | Overview | This document provides an overview of Bifrost's unified OpenAI-compatible interface and a detailed s... | ai-providers, openai-compatibility, api-gateway, feature-matrix |
| 058 | `058-providers-custom-providers.md` | Custom Providers | This document explains how to create and configure custom provider instances to restrict request typ... | custom-providers, provider-configuration, access-control, request-type-restriction |
| 059 | `059-providers-performance.md` | Performance Tuning | This document provides instructions and formulas for optimizing Bifrost performance through the conf... | performance-tuning, concurrency-control, buffer-management, memory-optimization |
| 060 | `060-providers-provider-routing.md` | Provider Routing | This document explains how Bifrost manages request routing across multiple AI providers using govern... | provider-routing, model-catalog, load-balancing, ai-governance |
| 061 | `061-providers-reasoning.md` | Reasoning | Provides a cross-provider reference for implementing reasoning and thinking capabilities in AI model... | reasoning-capabilities, ai-providers, api-normalization, configuration |
| 062 | `062-providers-supported-providers-anthropic.md` | Anthropic | This document outlines the technical mapping and structural transformations required to convert Open... | anthropic-api, api-conversion, message-handling, parameter-mapping |
| 063 | `063-providers-supported-providers-azure.md` | Azure | This document provides a technical guide for using the Bifrost API to interface with Azure OpenAI Se... | azure-openai, api-integration, deployment-mapping, authentication |
| 064 | `064-providers-supported-providers-bedrock.md` | AWS Bedrock | This document explains how to convert API requests between OpenAI formats and AWS Bedrock's specific... | aws-bedrock, api-conversion, parameter-mapping, model-families |
| 065 | `065-providers-supported-providers-cerebras.md` | Cerebras | This document outlines the integration of the Cerebras API into an OpenAI-compatible framework, deta... | cerebras, openai-compatibility, chat-completions, streaming |
| 066 | `066-providers-supported-providers-cohere.md` | Cohere | This document provides a technical guide for converting OpenAI-formatted API requests to Cohere's st... | cohere, api-integration, parameter-mapping, chat-completions |
| 067 | `067-providers-supported-providers-elevenlabs.md` | ElevenLabs | This document provides a technical guide for integrating ElevenLabs audio services, covering text-to... | elevenlabs, text-to-speech, speech-to-text, voice-settings |
| 068 | `068-providers-supported-providers-gemini.md` | Google Gemini | This document outlines the technical mapping and conversion processes required to translate OpenAI-s... | google-gemini, api-conversion, message-transformation, parameter-mapping |
| 069 | `069-providers-supported-providers-groq.md` | Groq | This document details the integration of Groq's OpenAI-compatible API into Bifrost, covering endpoin... | groq, openai-compatibility, chat-completions, api-integration |
| 070 | `070-providers-supported-providers-huggingface.md` | Hugging Face | This guide explains the technical implementation of the Hugging Face provider in Bifrost, detailing ... | hugging-face, bifrost, inference-providers, model-aliasing |
| 071 | `071-providers-supported-providers-mistral.md` | Mistral | This document provides a technical guide for converting OpenAI-formatted requests to the Mistral API... | mistral-ai, api-conversion, openai-compatibility, chat-completions |
| 072 | `072-providers-supported-providers-nebius.md` | Nebius | This document provides a technical guide for integrating with the Nebius API using OpenAI-compatible... | nebius, openai-compatible, api-integration, chat-completions |
| 073 | `073-providers-supported-providers-ollama.md` | Ollama | This guide explains how to integrate and configure Ollama for local model inference using its OpenAI... | ollama, openai-compatibility, local-inference, chat-completions |
| 074 | `074-providers-supported-providers-openai.md` | OpenAI | This document outlines the integration of OpenAI's API with Bifrost, detailing supported operations,... | openai, bifrost, api-reference, chat-completions |
| 075 | `075-providers-supported-providers-openrouter.md` | OpenRouter | This document outlines the integration and conversion logic for the OpenRouter API, detailing suppor... | openrouter, api-integration, chat-completions, reasoning-models |
| 076 | `076-providers-supported-providers-parasail.md` | Parasail | This document provides a technical guide on using the Parasail API, detailing its OpenAI-compatible ... | parasail, openai-compatible, chat-completions, api-integration |
| 077 | `077-providers-supported-providers-perplexity.md` | Perplexity | This document provides a technical guide for integrating the Perplexity API using an OpenAI-compatib... | perplexity-api, openai-compatibility, web-search, reasoning-effort |
| 078 | `078-providers-supported-providers-sgl.md` | SGLang | This document provides a guide for using SGLang as an OpenAI-compatible inference engine, detailing ... | sglang, openai-compatibility, inference-engine, api-reference |
| 079 | `079-providers-supported-providers-vertex.md` | Vertex AI | This document explains the integration and conversion logic for Google Vertex AI, detailing how to c... | vertex-ai, google-cloud-platform, api-integration, gemini |
| 080 | `080-providers-supported-providers-xai.md` | xAI | This document provides an integration guide for the xAI API, detailing its OpenAI-compatible endpoin... | xai, grok, openai-compatible, chat-completions |

### 9. Enterprise (081-094)
*Enterprise features and security*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 081 | `081-enterprise-adaptive-load-balancing.md` | Adaptive Load Balancing | This document explains the technical implementation of adaptive load balancing, detailing how real-t... | load-balancing, traffic-management, performance-optimization, health-monitoring |
| 082 | `082-enterprise-advanced-governance.md` | Getting started | This document introduces the Bifrost Enterprise Governance module, detailing its advanced security, ... | enterprise-governance, identity-management, compliance-monitoring, audit-reporting |
| 083 | `083-enterprise-audit-logs.md` | Audit Logs | This document outlines the Bifrost audit logging system, detailing how to track security events, con... | audit-logs, compliance, security-monitoring, siem-integration |
| 084 | `084-enterprise-clustering.md` | Clustering | This document explains the architecture and configuration of Bifrost clustering for high-availabilit... | clustering, high-availability, service-discovery, gossip-protocol |
| 085 | `085-enterprise-custom-plugins.md` | Custom Plugins | This document outlines Bifrost's custom plugin development services for extending the platform's LLM... | custom-plugins, llm-gateway, workflow-automation, ai-governance |
| 086 | `086-enterprise-datadog-connector.md` | Datadog | This document provides a guide for integrating and configuring the Datadog plugin to monitor LLM ope... | datadog, observability, apm-traces, llm-monitoring |
| 087 | `087-enterprise-guardrails.md` | Guardrails | This document explains how to configure and implement enterprise-grade content safety guardrails in ... | guardrails, content-safety, llm-security, aws-bedrock |
| 088 | `088-enterprise-invpc-deployments.md` | In-VPC Deployments | This document provides an overview and high-level instructions for deploying Bifrost within a Virtua... | vpc-deployment, private-cloud, security-compliance, enterprise-infrastructure |
| 089 | `089-enterprise-log-exports.md` | Log Exports | This document explains how to configure and automate log exports from Bifrost to various storage des... | log-export, data-retention, cloud-storage, telemetry-data |
| 090 | `090-enterprise-mcp-with-fa.md` | MCP with Federated Auth | This document explains how to transform private enterprise APIs into LLM-ready Model Context Protoco... | mcp, federated-authentication, api-integration, llm-tools |
| 091 | `091-enterprise-rbac.md` | Role-Based Access Control | Explains how to implement and manage Role-Based Access Control (RBAC) in Bifrost to provide fine-gra... | rbac, access-control, permissions, user-management |
| 092 | `092-enterprise-setting-up-entra.md` | Setting up Microsoft Entra | This document provides step-by-step instructions for configuring Microsoft Entra ID as an identity p... | microsoft-entra-id, azure-ad, sso-authentication, identity-management |
| 093 | `093-enterprise-setting-up-okta.md` | Setting up Okta | Step-by-step instructions for configuring Okta as an identity provider for Bifrost Enterprise to ena... | okta, sso, authentication, identity-provider |
| 094 | `094-enterprise-vault-support.md` | Vault Support | This document explains how to integrate Bifrost with enterprise secret management systems like Hashi... | vault-integration, secret-management, api-key-security, hashicorp-vault |

### 10. Deployment Guides (095-100)
*Installation and deployment options*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 095 | `095-deployment-guides-ecs.md` | ECS | This document provides instructions for deploying Bifrost to AWS ECS using Makefile automation or AW... | aws-ecs, bifrost-deployment, fargate, ec2-launch-type |
| 096 | `096-deployment-guides-fly.md` | fly.io | This document provides step-by-step instructions for deploying Bifrost to Fly.io using either a clon... | bifrost, fly-io, deployment, docker |
| 097 | `097-deployment-guides-helm.md` | Helm | This document provides instructions and configuration patterns for deploying Bifrost on Kubernetes u... | helm, kubernetes, deployment, devops |
| 098 | `098-deployment-guides-how-to-install-make.md` | Install make command | This document provides instructions for installing the make build tool across different operating sy... | installation, make, build-tools, windows |
| 099 | `099-deployment-guides-how-to-multinode.md` | Multinode Deployment | This document explains how to achieve high availability in Bifrost OSS deployments by using a shared... | high-availability, multinode-deployment, bifrost-oss, kubernetes |
| 100 | `100-deployment-guides-k8s.md` | Terraform + k8s | This document provides a comprehensive guide for deploying the Bifrost service on Kubernetes cluster... | terraform, kubernetes, bifrost, infrastructure-as-code |

### 11. Architecture (101-110)
*System architecture and internals*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 101 | `101-architecture-core-concurrency.md` | Concurrency | This document explains Bifrost's advanced concurrency architecture, detailing its use of provider-is... | concurrency, worker-pools, goroutines, go-channels |
| 102 | `102-architecture-core-mcp.md` | Model Context Protocol (MCP) | This document provides a technical deep dive into Bifrost's Model Context Protocol (MCP) architectur... | mcp-architecture, tool-discovery, connection-protocols, runtime-registration |
| 103 | `103-architecture-core-plugins.md` | Plugins | This document provides a detailed overview of Bifrost's plugin architecture, covering its core desig... | plugin-architecture, lifecycle-management, execution-pipeline, bifrost |
| 104 | `104-architecture-core-request-flow.md` | Request Flow | This document provides a technical deep dive into the Bifrost request processing pipeline, detailing... | bifrost-architecture, request-flow, load-balancing, middleware-plugins |
| 105 | `105-architecture-framework-config-store.md` | Config Store | This document explains the Bifrost ConfigStore, a persistent configuration management system that pr... | bifrost, config-store, configuration-management, database-backend |
| 106 | `106-architecture-framework-log-store.md` | Log Store | This document explains the LogStore component of the Bifrost framework, which provides a persistent ... | api-logging, data-persistence, observability, bifrost-framework |
| 107 | `107-architecture-framework-model-catalog.md` | Model Catalog | This document explains the Model Catalog, a centralized system in Bifrost for managing AI model info... | model-catalog, pricing-sync, cost-calculation, multi-modal |
| 108 | `108-architecture-framework-streaming.md` | Streaming | This document explains the Streaming package utility used to aggregate and process real-time AI stre... | streaming, ai-providers, data-aggregation, bifrost-framework |
| 109 | `109-architecture-framework-vector-store.md` | Vector Store | This document explains the Bifrost Vector Store component, which provides a unified interface for st... | vector-store, semantic-search, embeddings, weaviate |
| 110 | `110-architecture-framework-what-is-framework.md` | What is framework? | This document introduces the Bifrost Framework, a shared SDK that provides standardized storage inte... | sdk, bifrost-framework, plugin-development, data-storage |

### 12. Benchmarking (111-114)
*Performance benchmarks and testing*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 111 | `111-benchmarking-getting-started.md` | Getting Started | This document provides performance benchmark results for Bifrost across different AWS EC2 instance t... | performance-benchmarks, aws-ec2, instance-sizing, latency |
| 112 | `112-benchmarking-run-your-own-benchmarks.md` | Run Your Own Benchmarks | This document provides instructions for using the official Bifrost benchmarking tool to measure perf... | benchmarking, performance-testing, bifrost, load-testing |
| 113 | `113-benchmarking-t3.medium.md` | t3.medium | This document provides performance benchmarks, resource utilization metrics, and configuration tunin... | aws-t3-medium, performance-benchmarks, latency-analysis, resource-utilization |
| 114 | `114-benchmarking-t3.xl.md` | t3.xlarge | This document provides detailed performance benchmarks and resource utilization analysis for running... | aws-t3-xlarge, performance-benchmarks, bifrost-optimization, scalability-analysis |

### 13. Contributing (115-119)
*Developer contribution guides*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 115 | `115-contributing-adding-a-configstore.md` | Adding config store | This guide provides instructions for developers on how to extend the Bifrost config store by impleme... | bifrost, config-store, database-backend, gorm |
| 116 | `116-contributing-adding-a-logstore.md` | Adding a log store | This guide explains how to add a custom database backend for the Bifrost log store by implementing t... | bifrost, log-store, database-backend, gorm |
| 117 | `117-contributing-adding-a-provider.md` | Adding a new provider | This guide provides a comprehensive walkthrough for adding new LLM providers to the Bifrost gateway,... | bifrost, provider-integration, golang, api-gateway |
| 118 | `118-contributing-adding-a-vectorstore.md` | Adding a vector store | This guide provides instructions on how to contribute a new vector database backend to Bifrost by im... | bifrost, vector-store, database-integration, backend-development |
| 119 | `119-contributing-setting-up-repo.md` | Setting up the repository | This document provides a comprehensive guide for setting up the Bifrost repository for local develop... | development-setup, bifrost, go, makefile |

### 14. API Reference - Core (120-141)
*Core API endpoints (chat, completions, embeddings, files)*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 120 | `120-api-reference-audio-create-speech.md` | Create speech | This document defines the API endpoint for converting text into speech using various AI models throu... | text-to-speech, audio-generation, speech-synthesis, bifrost-api |
| 121 | `121-api-reference-audio-create-transcription.md` | Create transcription | This document specifies the API endpoint for transcribing audio files into text using multiple AI pr... | audio-transcription, speech-to-text, ai-inference, bifrost-api |
| 122 | `122-api-reference-batch-retrieve-a-batch-job.md` | Retrieve a batch job | This document defines the API endpoint for retrieving the status and detailed information of a speci... | batch-processing, api-endpoint, job-retrieval, ai-gateway |
| 123 | `123-api-reference-batch-create-a-batch-job.md` | Create a batch job | This document provides the technical specification for the Bifrost API endpoint used to create batch... | batch-processing, asynchronous-inference, api-reference, ai-models |
| 124 | `124-api-reference-batch-cancel-a-batch-job.md` | Cancel a batch job | This document specifies the API endpoint and parameters required to cancel an ongoing batch job with... | bifrost-api, batch-processing, job-cancellation, ai-gateway |
| 125 | `125-api-reference-batch-list-batch-jobs.md` | List batch jobs | This document specifies the API endpoint for listing batch jobs from various AI providers through th... | batch-processing, ai-inference, api-reference, bifrost-gateway |
| 126 | `126-api-reference-batch-get-batch-results.md` | Get batch results | This document provides the API specification for retrieving results from a completed batch processin... | batch-processing, api-endpoint, ai-inference, batch-results |
| 127 | `127-api-reference-cache-clear-cache-by-cache-key.md` | Clear cache by cache key | This document defines the API endpoint for clearing a specific cache entry from the Bifrost gateway ... | cache-management, api-endpoint, delete-method, bifrost-gateway |
| 128 | `128-api-reference-cache-clear-cache-by-request-id.md` | Clear cache by request ID | This document provides the OpenAPI specification for an endpoint that allows users to delete cache e... | cache-management, api-endpoint, request-id, bifrost-gateway |
| 129 | `129-api-reference-chat-completions-create-a-chat-completion.md` | Create a chat completion | This document defines the API endpoint for generating chat completions across multiple AI providers ... | chat-completions, ai-inference, multi-provider, unified-api |
| 130 | `130-api-reference-count-tokens-count-tokens.md` | Count tokens | This document provides the API specification for counting tokens in messages across various AI model... | token-counting, api-specification, bifrost-api, ai-inference |
| 131 | `131-api-reference-embeddings-create-embeddings.md` | Create embeddings | This document specifies the API endpoint for generating embedding vectors from text or token inputs ... | embeddings, api-reference, ai-inference, vector-generation |
| 132 | `132-api-reference-files-delete-a-file.md` | Delete a file | This document defines the API endpoint for deleting a specific file from a supported AI provider via... | file-management, delete-file, api-endpoint, bifrost-api |
| 133 | `133-api-reference-files-download-file-content.md` | Download file content | This document describes the API endpoint used to retrieve and download the raw binary content of a f... | api-endpoint, file-management, file-download, bifrost-api |
| 134 | `134-api-reference-files-retrieve-file-metadata.md` | Retrieve file metadata | This document details the API endpoint for retrieving metadata and status information for a specific... | api-reference, file-management, metadata-retrieval, bifrost-api |
| 135 | `135-api-reference-files-list-files.md` | List files | This document defines the API endpoint for listing files from various AI providers through the Bifro... | bifrost-api, file-management, api-endpoint, ai-gateway |
| 136 | `136-api-reference-files-upload-a-file.md` | Upload a file | This document describes the API endpoint for uploading files to the Bifrost gateway to be used in ba... | file-upload, bifrost-api, api-endpoint, batch-operations |
| 137 | `137-api-reference-health-health-check.md` | Health check | This document describes the Bifrost health check endpoint, which verifies the server's operational s... | health-check, api-monitoring, server-status, diagnostics |
| 138 | `138-api-reference-image-generations-generate-image.md` | Generate image | This document specifies the API endpoint for generating images from text prompts using various AI pr... | image-generation, text-to-image, bifrost-api, api-endpoint |
| 139 | `139-api-reference-models-list-available-models.md` | List available models | This document provides the API specification for listing available AI models across multiple provide... | api-specification, model-listing, ai-gateway, multi-provider |
| 140 | `140-api-reference-responses-create-a-response.md` | Create a response | This document describes the Bifrost API endpoint for creating AI model responses using the OpenAI Re... | ai-inference, openai-compatibility, streaming-sse, bifrost-api |
| 141 | `141-api-reference-text-completions-create-a-text-completion.md` | Create a text completion | This document provides the API specification for creating text completions via the Bifrost unified i... | text-completions, ai-inference, api-reference, streaming-sse |

### 15. API Reference - Configuration (142-191)
*Configuration and management APIs*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 142 | `142-api-reference-configuration-get-configuration.md` | Get configuration | This document defines the GET /api/config endpoint used to retrieve the current Bifrost gateway conf... | bifrost, api-configuration, management-api, gateway-settings |
| 143 | `143-api-reference-configuration-update-configuration.md` | Update configuration | This document details the API endpoint for updating the Bifrost gateway configuration, supporting bo... | bifrost, api-configuration, gateway-management, hot-reloading |
| 144 | `144-api-reference-configuration-force-pricing-sync.md` | Force pricing sync | This document describes the API endpoint used to manually trigger an immediate synchronization of pr... | bifrost-api, pricing-sync, configuration-management, api-endpoint |
| 145 | `145-api-reference-configuration-get-proxy-configuration.md` | Get proxy configuration | This document describes the API endpoint for retrieving the current global proxy configuration of th... | api-reference, proxy-configuration, bifrost-gateway, network-settings |
| 146 | `146-api-reference-configuration-update-proxy-configuration.md` | Update proxy configuration | This document provides the API specification for updating the global proxy settings of the Bifrost g... | bifrost-api, proxy-configuration, gateway-management, network-settings |
| 147 | `147-api-reference-configuration-get-version.md` | Get version | This document specifies the API endpoint for retrieving the current version information of the Bifro... | bifrost-api, version-endpoint, api-management, system-metadata |
| 148 | `148-api-reference-governance-list-budgets.md` | List budgets | This document provides the API specification for listing budgets within the Bifrost governance syste... | api-reference, governance, budgets, bifrost-api |
| 149 | `149-api-reference-governance-get-customer.md` | Get customer | This document describes the API endpoint for retrieving detailed configuration and budget informatio... | governance, customer-management, api-reference, bifrost |
| 150 | `150-api-reference-governance-create-customer.md` | Create customer | This document specifies the API endpoint for creating a new customer within the Bifrost AI gateway, ... | bifrost-api, customer-management, governance, api-reference |
| 151 | `151-api-reference-governance-update-customer.md` | Update customer | This document provides the API specification for updating an existing customer's details, including ... | bifrost-api, customer-management, governance, api-endpoint |
| 152 | `152-api-reference-governance-delete-customer.md` | Delete customer | This document details the API endpoint for deleting a customer within the Bifrost governance framewo... | bifrost-api, governance, customer-management, delete-operation |
| 153 | `153-api-reference-governance-list-customers.md` | List customers | This document specifies the GET /api/governance/customers endpoint, which retrieves a list of all cu... | api-reference, governance, customer-management, bifrost |
| 154 | `154-api-reference-governance-list-rate-limits.md` | List rate limits | This document defines the API endpoint for retrieving a list of all configured rate limits and their... | governance, rate-limiting, api-reference, usage-tracking |
| 155 | `155-api-reference-governance-get-team.md` | Get team | This document provides technical details for the Bifrost API endpoint used to retrieve detailed conf... | bifrost-api, governance, team-management, api-endpoint |
| 156 | `156-api-reference-governance-create-team.md` | Create team | This document defines the API specification for creating a new team in the Bifrost gateway, includin... | bifrost-api, governance, team-management, api-endpoint |
| 157 | `157-api-reference-governance-update-team.md` | Update team | This document provides the API specification for updating an existing team's information, including ... | bifrost-api, governance, team-management, budget-configuration |
| 158 | `158-api-reference-governance-delete-team.md` | Delete team | This document provides the API specification for deleting a team from the Bifrost governance system ... | bifrost-api, governance, team-management, delete-team |
| 159 | `159-api-reference-governance-list-teams.md` | List teams | This document provides the technical specification for the Bifrost API endpoint used to retrieve a l... | bifrost-api, governance, team-management, api-endpoint |
| 160 | `160-api-reference-governance-get-virtual-key.md` | Get virtual key | This document provides the API specification for retrieving detailed configuration information for a... | api-reference, governance, virtual-keys, bifrost-api |
| 161 | `161-api-reference-governance-create-virtual-key.md` | Create virtual key | This document provides the API specification for creating a virtual key, which includes configuratio... | virtual-keys, governance, api-management, rate-limiting |
| 162 | `162-api-reference-governance-update-virtual-key.md` | Update virtual key | This document describes the API endpoint for updating the configuration of an existing virtual key, ... | governance, virtual-keys, api-management, rate-limiting |
| 163 | `163-api-reference-governance-delete-virtual-key.md` | Delete virtual key | This document specifies the API endpoint for deleting a virtual key within the Bifrost governance sy... | bifrost-api, governance, virtual-keys, api-management |
| 164 | `164-api-reference-governance-list-virtual-keys.md` | List virtual keys | This document specifies the API endpoint for retrieving a list of all virtual keys along with their ... | governance, virtual-keys, api-endpoint, bifrost-api |
| 165 | `165-api-reference-logging-get-available-filter-data.md` | Get available filter data | This API endpoint retrieves unique metadata from logs, including available models and keys, to facil... | logging, api-reference, log-analytics, filter-data |
| 166 | `166-api-reference-logging-get-dropped-requests-count.md` | Get dropped requests count | This document describes the API endpoint used to retrieve the total count of dropped requests from t... | bifrost-api, logging, monitoring, api-reference |
| 167 | `167-api-reference-logging-get-log-statistics.md` | Get log statistics | This document specifies the API endpoint for retrieving aggregated log statistics, including request... | api-endpoint, log-statistics, analytics, monitoring |
| 168 | `168-api-reference-logging-get-logs.md` | Get logs | This document describes the API endpoint for retrieving gateway logs with support for advanced filte... | logging-api, bifrost-gateway, log-management, rest-api |
| 169 | `169-api-reference-logging-delete-logs.md` | Delete logs | This document defines the API endpoint for deleting logs by their unique identifiers within the Bifr... | bifrost-api, log-management, api-endpoint, management-api |
| 170 | `170-api-reference-logging-recalculate-log-costs.md` | Recalculate log costs | This document defines an API endpoint for recomputing missing log costs in batches using current pri... | logging, cost-management, batch-processing, api-reference |
| 171 | `171-api-reference-mcp-add-mcp-client.md` | Add MCP client | This document defines the API endpoint for adding and configuring Model Context Protocol (MCP) clien... | mcp-client, model-context-protocol, api-endpoint, bifrost-gateway |
| 172 | `172-api-reference-mcp-edit-mcp-client.md` | Edit MCP client | This document provides the API specification for updating an existing Model Context Protocol (MCP) c... | mcp, api-reference, model-context-protocol, client-configuration |
| 173 | `173-api-reference-mcp-execute-mcp-tool.md` | Execute MCP tool | This document defines the API endpoint for executing Model Context Protocol (MCP) tools and retrievi... | mcp, tool-execution, api-reference, model-context-protocol |
| 174 | `174-api-reference-mcp-list-mcp-clients.md` | List MCP clients | This document defines the API endpoint for retrieving a list of all configured Model Context Protoco... | mcp, api-management, model-context-protocol, bifrost-api |
| 175 | `175-api-reference-mcp-reconnect-mcp-client.md` | Reconnect MCP client | This document specifies the API endpoint for reconnecting a Model Context Protocol (MCP) client that... | mcp-client, api-endpoint, reconnect, bifrost-api |
| 176 | `176-api-reference-mcp-remove-mcp-client.md` | Remove MCP client | This document provides the technical specification for the API endpoint used to remove a Model Conte... | mcp, mcp-client, api-management, bifrost |
| 177 | `177-api-reference-plugins-create-a-new-plugin.md` | Create a new plugin | This document defines the API endpoint and specification for creating a new plugin within the Bifros... | bifrost-api, plugin-management, openapi-spec, rest-api |
| 178 | `178-api-reference-plugins-update-a-plugin.md` | Update a plugin | This document defines the API endpoint for updating a plugin's configuration, which manages the plug... | plugins, api-endpoint, configuration-management, bifrost-api |
| 179 | `179-api-reference-plugins-delete-a-plugin.md` | Delete a plugin | This document specifies the API endpoint for removing a plugin from the Bifrost configuration and st... | bifrost-api, plugin-management, gateway-configuration, api-endpoint |
| 180 | `180-api-reference-plugins-get-a-specific-plugin.md` | Get a specific plugin | This document provides the API specification for retrieving the configuration details of a specific ... | bifrost-api, plugin-management, openapi-spec, endpoint-reference |
| 181 | `181-api-reference-plugins-list-all-plugins.md` | List all plugins | This document describes the API endpoint for retrieving a complete list of installed plugins, includ... | bifrost-api, plugin-management, rest-api, gateway-monitoring |
| 182 | `182-api-reference-providers-update-a-provider.md` | Update a provider | This document describes the API endpoint for updating a provider's configuration in the Bifrost gate... | bifrost-api, provider-management, api-reference, configuration-update |
| 183 | `183-api-reference-providers-delete-a-provider.md` | Delete a provider | This document specifies the API endpoint for removing an AI model provider from the Bifrost gateway ... | provider-management, api-gateway, configuration-api, delete-endpoint |
| 184 | `184-api-reference-providers-get-a-specific-provider.md` | Get a specific provider | This document defines the API endpoint for retrieving configuration details, including API keys and ... | bifrost-api, provider-management, api-configuration, ai-gateway |
| 185 | `185-api-reference-providers-add-a-new-provider.md` | Add a new provider | This document describes the API endpoint for adding and configuring a new AI model provider within t... | api-management, provider-configuration, ai-gateway, endpoint-reference |
| 186 | `186-api-reference-providers-list-all-keys.md` | List all keys | Describes the API endpoint for listing all configured API keys and their associated configurations a... | api-keys, provider-management, gateway-management, api-reference |
| 187 | `187-api-reference-providers-list-all-providers.md` | List all providers | This document defines the API endpoint for retrieving a list of all configured AI model providers, i... | api-reference, provider-management, ai-gateway, configuration-api |
| 188 | `188-api-reference-providers-list-models.md` | List models | This document defines the API endpoint for listing available AI models with support for filtering by... | api-reference, model-management, bifrost-gateway, endpoint-specification |
| 189 | `189-api-reference-session-check-if-authentication-is-enabled.md` | Check if authentication is enabled | This document describes an API endpoint used to verify if authentication is enabled for the Bifrost ... | authentication, session-management, api-endpoint, token-validation |
| 190 | `190-api-reference-session-login.md` | Login | This document defines the login endpoint for the Bifrost API, detailing how to authenticate users an... | authentication, session-management, bifrost-api, login-endpoint |
| 191 | `191-api-reference-session-logout.md` | Logout | This document defines the API endpoint for logging out a user and invalidating their current session... | session-management, authentication, api-endpoint, user-logout |

### 16. API Reference - Anthropic (192-204)
*Anthropic-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 192 | `192-api-reference-anthropic-integration-retrieve-batch-job-anthropic-format.md` | Retrieve batch job (Anthropic format) | This document provides the API specification for retrieving the status and details of a batch proces... | anthropic-integration, batch-processing, api-reference, inference-gateway |
| 193 | `193-api-reference-anthropic-integration-create-batch-job-anthropic-format.md` | Create batch job (Anthropic format) | This document provides the API specification for creating batch processing jobs using the Anthropic-... | anthropic-integration, batch-processing, api-gateway, ai-inference |
| 194 | `194-api-reference-anthropic-integration-cancel-batch-job-anthropic-format.md` | Cancel batch job (Anthropic format) | This document provides details for the API endpoint used to cancel an active batch processing job wi... | anthropic, batch-processing, api-endpoint, job-cancellation |
| 195 | `195-api-reference-anthropic-integration-list-batch-jobs-anthropic-format.md` | List batch jobs (Anthropic format) | This document specifies the API endpoint for retrieving a paginated list of batch processing jobs us... | anthropic-api, batch-processing, message-batches, api-reference |
| 196 | `196-api-reference-anthropic-integration-get-batch-results-anthropic-format.md` | Get batch results (Anthropic format) | This document specifies the API endpoint for retrieving results from a completed batch job using the... | anthropic-integration, batch-processing, api-reference, bifrost-gateway |
| 197 | `197-api-reference-anthropic-integration-create-completion-anthropic-legacy-format.md` | Create completion (Anthropic legacy format) | This document defines the API endpoint for creating text completions using the legacy Anthropic form... | anthropic-api, text-completion, api-gateway, legacy-format |
| 198 | `198-api-reference-anthropic-integration-count-tokens-anthropic-format.md` | Count tokens (Anthropic format) | This document specifies the API endpoint for calculating the number of tokens in a message request u... | anthropic, token-counting, api-integration, bifrost-gateway |
| 199 | `199-api-reference-anthropic-integration-delete-file-anthropic-format.md` | Delete file (Anthropic format) | This document provides the OpenAPI specification and endpoint details for deleting an uploaded file ... | anthropic-integration, file-management, api-endpoint, bifrost-gateway |
| 200 | `200-api-reference-anthropic-integration-get-file-content-anthropic-format.md` | Get file content (Anthropic format) | This document defines the API endpoint for retrieving file content or metadata using the Anthropic-c... | anthropic-integration, file-management, api-endpoint, bifrost-gateway |
| 201 | `201-api-reference-anthropic-integration-list-files-anthropic-format.md` | List files (Anthropic format) | This document provides the API specification for listing uploaded files using the Anthropic-compatib... | anthropic-integration, file-management, list-files, bifrost-api |
| 202 | `202-api-reference-anthropic-integration-create-message-anthropic-format.md` | Create message (Anthropic format) | This document defines the Bifrost API endpoint for creating messages using the Anthropic Messages AP... | anthropic-api, message-creation, ai-inference, streaming-sse |
| 203 | `203-api-reference-anthropic-integration-list-models-anthropic-format.md` | List models (Anthropic format) | This document specifies the API endpoint for retrieving a list of available AI models using the Anth... | anthropic-integration, model-listing, api-specification, bifrost-gateway |
| 204 | `204-api-reference-anthropic-integration-upload-file-anthropic-format.md` | Upload file (Anthropic format) | This document defines the API endpoint for uploading files using the Anthropic-compatible format thr... | anthropic-integration, file-upload, api-endpoint, bifrost-gateway |

### 17. API Reference - OpenAI (205-230)
*OpenAI-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 205 | `205-api-reference-openai-integration-retrieve-batch-job-openai-format.md` | Retrieve batch job (OpenAI format) | This document specifies the API endpoint for retrieving detailed information and status of a batch p... | openai-integration, batch-processing, api-reference, bifrost-gateway |
| 206 | `206-api-reference-openai-integration-create-batch-job-openai-format.md` | Create batch job (OpenAI format) | This document specifies the API endpoint for creating batch processing jobs using the OpenAI-compati... | openai-integration, batch-processing, api-reference, bifrost |
| 207 | `207-api-reference-openai-integration-cancel-batch-job-openai-format.md` | Cancel batch job (OpenAI format) | This document describes the API endpoint for canceling an active batch processing job using the Open... | openai-integration, batch-processing, api-endpoint, bifrost-gateway |
| 208 | `208-api-reference-openai-integration-list-batch-jobs-openai-format.md` | List batch jobs (OpenAI format) | This document describes the API endpoint for listing batch processing jobs using the OpenAI-compatib... | openai-integration, batch-processing, api-endpoint, bifrost-gateway |
| 209 | `209-api-reference-openai-integration-create-chat-completion-azure-openai.md` | Create chat completion (Azure OpenAI) | This document provides the API specification for creating chat completions using Azure OpenAI deploy... | azure-openai, chat-completions, api-reference, bifrost-gateway |
| 210 | `210-api-reference-openai-integration-create-chat-completion-openai-format.md` | Create chat completion (OpenAI format) | This document provides the technical specification for the OpenAI-compatible chat completions endpoi... | openai-compatibility, chat-completions, api-reference, streaming-sse |
| 211 | `211-api-reference-openai-integration-count-input-tokens.md` | Count input tokens | This document describes an API endpoint for counting the number of tokens in an OpenAI-compatible Re... | token-counting, openai-compatibility, bifrost-api, api-reference |
| 212 | `212-api-reference-openai-integration-create-embeddings-azure-openai.md` | Create embeddings (Azure OpenAI) | This document provides the OpenAPI specification for the Azure OpenAI embedding endpoint within the ... | azure-openai, embeddings, api-reference, bifrost-api |
| 213 | `213-api-reference-openai-integration-create-embeddings-openai-format.md` | Create embeddings (OpenAI format) | This document provides technical specifications for the OpenAI-compatible embeddings endpoint, detai... | openai-integration, embeddings, api-reference, vector-generation |
| 214 | `214-api-reference-openai-integration-get-file-content-openai-format.md` | Get file content (OpenAI format) | This document describes the API endpoint for retrieving the binary content of an uploaded file using... | openai-integration, file-management, api-reference, bifrost-gateway |
| 215 | `215-api-reference-openai-integration-retrieve-file-metadata-openai-format.md` | Retrieve file metadata (OpenAI format) | This document describes the API endpoint for retrieving metadata for an uploaded file using the Open... | openai-integration, file-management, api-reference, metadata-retrieval |
| 216 | `216-api-reference-openai-integration-delete-file-openai-format.md` | Delete file (OpenAI format) | This document describes the API endpoint for deleting uploaded files using an OpenAI-compatible form... | openai-integration, file-management, api-reference, bifrost-gateway |
| 217 | `217-api-reference-openai-integration-list-files-openai-format.md` | List files (OpenAI format) | This document describes the API endpoint for listing uploaded files using the OpenAI-compatible inte... | openai-integration, file-management, api-reference, bifrost-gateway |
| 218 | `218-api-reference-openai-integration-create-image-azure-openai.md` | Create image (Azure OpenAI) | This document specifies the API endpoint for generating images from text prompts using Azure OpenAI ... | azure-openai, image-generation, api-reference, bifrost |
| 219 | `219-api-reference-openai-integration-create-image.md` | Create image | This document provides the API specification for generating images from text prompts using an OpenAI... | openai-api, image-generation, text-to-image, ai-inference |
| 220 | `220-api-reference-openai-integration-list-models-azure-openai.md` | List models (Azure OpenAI) | This document defines the API specification for listing models associated with a specific Azure Open... | azure-openai, bifrost-api, list-models, api-reference |
| 221 | `221-api-reference-openai-integration-list-models-openai-format.md` | List models (OpenAI format) | This document describes the API endpoint used to retrieve a list of available AI models in an OpenAI... | openai-integration, model-listing, bifrost-api, api-reference |
| 222 | `222-api-reference-openai-integration-create-response-azure-openai.md` | Create response (Azure OpenAI) | This document provides the OpenAPI specification for creating responses through Azure OpenAI deploym... | azure-openai, bifrost-api, api-reference, ai-inference |
| 223 | `223-api-reference-openai-integration-create-response-openai-responses-api.md` | Create response (OpenAI Responses API) | This document defines the API endpoint for creating responses using the OpenAI Responses API format,... | openai-integration, responses-api, ai-inference, streaming-sse |
| 224 | `224-api-reference-openai-integration-create-speech-azure-openai-tts.md` | Create speech (Azure OpenAI TTS) | This document defines the OpenAPI specification for generating audio from text using the Azure OpenA... | azure-openai, text-to-speech, api-specification, speech-synthesis |
| 225 | `225-api-reference-openai-integration-create-speech-openai-tts.md` | Create speech (OpenAI TTS) | This document defines the OpenAI-compatible text-to-speech endpoint for converting text into audio, ... | openai-tts, text-to-speech, audio-generation, speech-synthesis |
| 226 | `226-api-reference-openai-integration-create-text-completion-azure-openai.md` | Create text completion (Azure OpenAI) | This document provides the API specification for generating text completions using Azure OpenAI depl... | azure-openai, text-completions, openapi-spec, ai-inference |
| 227 | `227-api-reference-openai-integration-create-text-completion-openai-format.md` | Create text completion (OpenAI format) | This document provides the specification for the OpenAI-compatible legacy text completions API endpo... | openai-compatible, text-completion, api-reference, inference |
| 228 | `228-api-reference-openai-integration-create-transcription-azure-openai.md` | Create transcription (Azure OpenAI) | This document defines the API endpoint for transcribing audio files using Azure OpenAI models throug... | azure-openai, transcription, audio-processing, speech-to-text |
| 229 | `229-api-reference-openai-integration-create-transcription-openai-whisper.md` | Create transcription (OpenAI Whisper) | This document provides technical specifications for the OpenAI Whisper transcription endpoint, which... | openai-whisper, audio-transcription, speech-to-text, api-endpoint |
| 230 | `230-api-reference-openai-integration-upload-file-openai-format.md` | Upload file (OpenAI format) | This document specifies the API endpoint for uploading files in an OpenAI-compatible format to be us... | openai-integration, file-upload, api-reference, batch-processing |

### 18. API Reference - Bedrock (231-238)
*AWS Bedrock-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 231 | `231-api-reference-bedrock-integration-retrieve-batch-inference-job-bedrock-format.md` | Retrieve batch inference job (Bedrock format) | This document specifies the API endpoint for retrieving the details and status of a batch inference ... | bedrock-integration, batch-inference, api-reference, aws-bedrock |
| 232 | `232-api-reference-bedrock-integration-create-batch-inference-job-bedrock-format.md` | Create batch inference job (Bedrock format) | This document defines the API specification for creating batch inference jobs using the AWS Bedrock ... | aws-bedrock, batch-inference, api-endpoint, model-invocation |
| 233 | `233-api-reference-bedrock-integration-cancel-batch-inference-job-bedrock-format.md` | Cancel batch inference job (Bedrock format) | This document specifies the API endpoint for cancelling an active batch inference job using the AWS ... | bedrock-integration, batch-inference, job-management, api-endpoint |
| 234 | `234-api-reference-bedrock-integration-list-batch-inference-jobs-bedrock-format.md` | List batch inference jobs (Bedrock format) | This document provides the API specification for listing batch inference jobs using the AWS Bedrock ... | bedrock, batch-inference, aws-bedrock, api-reference |
| 235 | `235-api-reference-bedrock-integration-converse-with-model-bedrock-format.md` | Converse with model (Bedrock format) | This document defines the API specification for interacting with AI models through the Bifrost gatew... | bedrock-integration, aws-bedrock, converse-api, ai-inference |
| 236 | `236-api-reference-bedrock-integration-invoke-model-bedrock-format.md` | Invoke model (Bedrock format) | This document describes the Bifrost API endpoint for invoking AI models using the AWS Bedrock Invoke... | aws-bedrock, model-inference, api-reference, llm-gateway |
| 237 | `237-api-reference-bedrock-integration-invoke-model-with-streaming-bedrock-format.md` | Invoke model with streaming (Bedrock format) | This document defines the API endpoint for invoking AI models with streaming responses using the AWS... | bedrock-integration, streaming-api, ai-inference, openapi-spec |
| 238 | `238-api-reference-bedrock-integration-stream-converse-with-model-bedrock-format.md` | Stream converse with model (Bedrock format) | This document defines the API endpoint for streaming chat completions using the AWS Bedrock Converse... | aws-bedrock, streaming-api, chat-completions, ai-inference |

### 19. API Reference - Gemini (239-248)
*Google Gemini-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 239 | `239-api-reference-genai-integration-count-tokens-gemini-format.md` | Count tokens (Gemini format) | This document provides the OpenAPI specification for the Google Gemini-compatible token counting end... | gemini-api, token-counting, google-genai, bifrost-gateway |
| 240 | `240-api-reference-genai-integration-embed-content-gemini-format.md` | Embed content (Gemini format) | This document provides the OpenAPI specification for the Google Gemini-compatible embedding endpoint... | gemini-api, embeddings, bifrost-gateway, google-genai |
| 241 | `241-api-reference-genai-integration-retrieve-file-gemini-format.md` | Retrieve file (Gemini format) | This document describes the API endpoint for retrieving file metadata in the Google Gemini format th... | gemini-api, file-management, metadata-retrieval, google-genai |
| 242 | `242-api-reference-genai-integration-delete-file-gemini-format.md` | Delete file (Gemini format) | This document specifies the API endpoint for deleting files in Google Gemini format through the Bifr... | gemini-api, file-management, bifrost-gateway, genai-integration |
| 243 | `243-api-reference-genai-integration-list-files-gemini-format.md` | List files (Gemini format) | This document provides the API specification for listing uploaded files in the Google Gemini compati... | gemini-api, file-management, google-genai, bifrost-gateway |
| 244 | `244-api-reference-genai-integration-generate-content-gemini-format.md` | Generate content (Gemini format) | This document specifies the API endpoint for generating content through the Google Gemini-compatible... | gemini-api, google-genai, content-generation, api-integration |
| 245 | `245-api-reference-genai-integration-generate-image-gemini-format.md` | Generate image (Gemini format) | This document defines the API specification for generating images using Google's Gemini and Imagen m... | gemini, imagen, image-generation, bifrost-api |
| 246 | `246-api-reference-genai-integration-list-models-gemini-format.md` | List models (Gemini format) | This document defines the API endpoint for listing available AI models using the Google Gemini (GenA... | gemini-api, model-listing, bifrost, genai-integration |
| 247 | `247-api-reference-genai-integration-stream-generate-content-gemini-format.md` | Stream generate content (Gemini format) | This document defines the OpenAPI specification for streaming content generation using the Google Ge... | gemini-api, streaming-content, ai-gateway, openapi-specification |
| 248 | `248-api-reference-genai-integration-upload-file-gemini-format.md` | Upload file (Gemini format) | This document describes the API endpoint for uploading files to Google Gemini via the Bifrost gatewa... | google-gemini, file-upload, multipart-upload, genai-integration |

### 20. API Reference - Cohere (249-251)
*Cohere-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 249 | `249-api-reference-cohere-integration-chat-with-model-cohere-v2-format.md` | Chat with model (Cohere v2 format) | This document provides the API specification for sending chat completion requests using the Cohere v... | cohere-api, chat-completion, ai-gateway, bifrost-api |
| 250 | `250-api-reference-cohere-integration-create-embeddings-cohere-v2-format.md` | Create embeddings (Cohere v2 format) | This document provides the API specification for generating text and multimodal embeddings using the... | cohere-v2, embeddings, api-reference, bifrost-gateway |
| 251 | `251-api-reference-cohere-integration-tokenize-text-cohere-format.md` | Tokenize text (Cohere format) | This document provides the API specification for tokenizing text using the Cohere-compatible endpoin... | cohere-integration, tokenization, api-reference, text-processing |

### 21. API Reference - LangChain (252-269)
*LangChain-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 252 | `252-api-reference-langchain-integration-chat-completions-langchain-openai-format.md` | Chat completions (LangChain - OpenAI format) | This document defines the API endpoint for generating chat completions via the LangChain framework u... | langchain-integration, openai-compatibility, chat-completions, ai-inference |
| 253 | `253-api-reference-langchain-integration-chat-with-model-langchain-cohere-format.md` | Chat with model (LangChain - Cohere format) | This document specifies the API endpoint for performing chat completions using the Cohere-compatible... | langchain, cohere, chat-completions, api-gateway |
| 254 | `254-api-reference-langchain-integration-converse-with-model-langchain-bedrock-format.md` | Converse with model (LangChain - Bedrock format) | This document provides the API specification for a LangChain-compatible endpoint that facilitates mo... | langchain, aws-bedrock, converse-api, inference |
| 255 | `255-api-reference-langchain-integration-count-input-tokens-langchain-openai-format.md` | Count input tokens (LangChain - OpenAI format) | This document defines an API endpoint for counting the number of input tokens in requests using the ... | langchain-integration, openai-format, token-counting, input-tokens |
| 256 | `256-api-reference-langchain-integration-count-tokens-langchain-anthropic-format.md` | Count tokens (LangChain - Anthropic format) | This document provides the OpenAPI specification for an endpoint that counts tokens in messages usin... | langchain, anthropic, token-counting, api-reference |
| 257 | `257-api-reference-langchain-integration-create-embeddings-langchain-cohere-format.md` | Create embeddings (LangChain - Cohere format) | This document specifies the API endpoint for generating text and multimodal embeddings using the Lan... | langchain, cohere, embeddings, api-reference |
| 258 | `258-api-reference-langchain-integration-create-embeddings-langchain-openai-format.md` | Create embeddings (LangChain - OpenAI format) | This document specifies the API endpoint for generating text embeddings using an OpenAI-compatible f... | langchain, openai-compatible, embeddings, api-specification |
| 259 | `259-api-reference-langchain-integration-generate-content-langchain-gemini-format.md` | Generate content (LangChain - Gemini format) | This document specifies the API endpoint for generating content using the Google Gemini format throu... | langchain-integration, google-gemini, api-specification, content-generation |
| 260 | `260-api-reference-langchain-integration-create-message-langchain-anthropic-format.md` | Create message (LangChain - Anthropic format) | This document defines the API specification for creating messages using the Anthropic-compatible for... | langchain, anthropic, chat-completions, api-gateway |
| 261 | `261-api-reference-langchain-integration-list-models-langchain-gemini-format.md` | List models (LangChain - Gemini format) | This document defines the API endpoint for listing available AI models using the Google Gemini forma... | google-gemini, langchain-integration, api-reference, model-listing |
| 262 | `262-api-reference-langchain-integration-list-models-langchain-openai-format.md` | List models (LangChain - OpenAI format) | This document provides the API specification for listing available AI models using an OpenAI-compati... | langchain, openai-compatible, api-reference, model-listing |
| 263 | `263-api-reference-langchain-integration-create-response-langchain-openai-responses-api.md` | Create response (LangChain - OpenAI Responses API) | This document specifies the API endpoint for creating AI model responses using the OpenAI format via... | langchain, openai-api, inference-gateway, rest-api |
| 264 | `264-api-reference-langchain-integration-create-speech-langchain-openai-tts.md` | Create speech (LangChain - OpenAI TTS) | This document specifies the LangChain-compatible API endpoint for converting text to audio using Ope... | langchain, openai-tts, text-to-speech, speech-synthesis |
| 265 | `265-api-reference-langchain-integration-stream-converse-with-model-langchain-bedrock-format.md` | Stream converse with model (LangChain - Bedrock format) | This document defines an API endpoint for streaming conversational model responses using the AWS Bed... | langchain, aws-bedrock, streaming-api, ai-inference |
| 266 | `266-api-reference-langchain-integration-stream-generate-content-langchain-gemini-format.md` | Stream generate content (LangChain - Gemini format) | This document defines the OpenAPI specification for streaming content generation using the Google Ge... | langchain, gemini, streaming, content-generation |
| 267 | `267-api-reference-langchain-integration-text-completions-langchain-openai-format.md` | Text completions (LangChain - OpenAI format) | This document specifies the legacy text completions API endpoint designed for LangChain integration ... | langchain, openai-compatible, text-completions, api-reference |
| 268 | `268-api-reference-langchain-integration-tokenize-text-langchain-cohere-format.md` | Tokenize text (LangChain - Cohere format) | This document provides the API specification for tokenizing text strings into token IDs and strings ... | langchain, cohere, tokenization, api-reference |
| 269 | `269-api-reference-langchain-integration-create-transcription-langchain-openai-whisper.md` | Create transcription (LangChain - OpenAI Whisper) | This document specifies the API endpoint for transcribing audio into text using OpenAI Whisper via t... | langchain, openai-whisper, audio-transcription, speech-to-text |

### 22. API Reference - LiteLLM (270-286)
*LiteLLM-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 270 | `270-api-reference-litellm-integration-chat-completions-litellm-openai-format.md` | Chat completions (LiteLLM - OpenAI format) | This document specifies the OpenAPI definition for the LiteLLM-compatible chat completion endpoint w... | litellm, chat-completions, openai-format, api-gateway |
| 271 | `271-api-reference-litellm-integration-chat-with-model-litellm-cohere-format.md` | Chat with model (LiteLLM - Cohere format) | This document specifies the API endpoint for performing chat completions using the Cohere-compatible... | litellm, cohere, chat-completion, api-gateway |
| 272 | `272-api-reference-litellm-integration-converse-with-model-litellm-bedrock-format.md` | Converse with model (LiteLLM - Bedrock format) | This document provides the API specification for interacting with AI models using the AWS Bedrock Co... | litellm, aws-bedrock, api-specification, ai-inference |
| 273 | `273-api-reference-litellm-integration-count-input-tokens-litellm-openai-format.md` | Count input tokens (LiteLLM - OpenAI format) | This document defines an API endpoint for calculating the number of input tokens in a LiteLLM-compat... | litellm, openai-format, token-counting, api-specification |
| 274 | `274-api-reference-litellm-integration-create-embeddings-litellm-cohere-format.md` | Create embeddings (LiteLLM - Cohere format) | This document specifies the API endpoint for generating text and multimodal embeddings using the Coh... | litellm, cohere, embeddings, api-proxy |
| 275 | `275-api-reference-litellm-integration-create-embeddings-litellm-openai-format.md` | Create embeddings (LiteLLM - OpenAI format) | Provides the API specification for generating text embeddings using an OpenAI-compatible format thro... | embeddings, litellm, openai-format, api-reference |
| 276 | `276-api-reference-litellm-integration-generate-content-litellm-gemini-format.md` | Generate content (LiteLLM - Gemini format) | This document defines the API endpoint for generating AI content using the Google Gemini-compatible ... | litellm, google-gemini, content-generation, api-reference |
| 277 | `277-api-reference-litellm-integration-create-message-litellm-anthropic-format.md` | Create message (LiteLLM - Anthropic format) | This document specifies the API endpoint for creating messages using the Anthropic-compatible format... | litellm, anthropic-format, message-creation, api-integration |
| 278 | `278-api-reference-litellm-integration-list-models-litellm-gemini-format.md` | List models (LiteLLM - Gemini format) | This document defines the REST API endpoint for listing available AI models through the LiteLLM prox... | litellm, gemini-api, model-listing, bifrost-api |
| 279 | `279-api-reference-litellm-integration-list-models-litellm-openai-format.md` | List models (LiteLLM - OpenAI format) | This document defines the API endpoint for retrieving a list of available AI models through the Lite... | litellm, openai-compatible, model-listing, api-gateway |
| 280 | `280-api-reference-litellm-integration-create-response-litellm-openai-responses-api.md` | Create response (LiteLLM - OpenAI Responses API) | This document defines the API endpoint for generating model responses using the LiteLLM proxy with O... | litellm, openai-responses, api-gateway, inference |
| 281 | `281-api-reference-litellm-integration-create-speech-litellm-openai-tts.md` | Create speech (LiteLLM - OpenAI TTS) | This document provides the API specification for converting text into audio using OpenAI's Text-to-S... | litellm, text-to-speech, openai-tts, api-reference |
| 282 | `282-api-reference-litellm-integration-stream-converse-with-model-litellm-bedrock-format.md` | Stream converse with model (LiteLLM - Bedrock format) | This document provides the OpenAPI specification for streaming AI model conversations via the LiteLL... | litellm, aws-bedrock, streaming-api, converse-stream |
| 283 | `283-api-reference-litellm-integration-stream-generate-content-litellm-gemini-format.md` | Stream generate content (LiteLLM - Gemini format) | This document provides the OpenAPI specification for streaming content generation using the Google G... | litellm, google-gemini, streaming-api, openapi-spec |
| 284 | `284-api-reference-litellm-integration-text-completions-litellm-openai-format.md` | Text completions (LiteLLM - OpenAI format) | This document defines the legacy OpenAI-compatible text completions endpoint provided via LiteLLM fo... | litellm, openai-format, text-completions, api-gateway |
| 285 | `285-api-reference-litellm-integration-tokenize-text-litellm-cohere-format.md` | Tokenize text (LiteLLM - Cohere format) | This document specifies the API endpoint for tokenizing text using the Cohere-compatible format via ... | litellm, cohere, tokenization, api-reference |
| 286 | `286-api-reference-litellm-integration-create-transcription-litellm-openai-whisper.md` | Create transcription (LiteLLM - OpenAI Whisper) | This document provides the API specification for transcribing audio files into text using the OpenAI... | audio-transcription, litellm, openai-whisper, speech-to-text |

### 23. API Reference - PydanticAI (287-303)
*PydanticAI-compatible API endpoints*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 287 | `287-api-reference-pydanticai-integration-chat-completions-pydanticai-openai-format.md` | Chat completions (PydanticAI - OpenAI format) | This document provides the OpenAPI specification for the PydanticAI-compatible chat completions endp... | pydanticai, chat-completions, openai-compatible, bifrost-api |
| 288 | `288-api-reference-pydanticai-integration-chat-with-model-pydanticai-cohere-format.md` | Chat with model (PydanticAI - Cohere format) | This document provides the API specification for performing chat completions using the Cohere-compat... | pydanticai, cohere, chat-completions, ai-inference |
| 289 | `289-api-reference-pydanticai-integration-converse-with-model-pydanticai-bedrock-format.md` | Converse with model (PydanticAI - Bedrock format) | This API endpoint enables model interaction by sending messages in an AWS Bedrock Converse-compatibl... | pydanticai, aws-bedrock, model-inference, converse-api |
| 290 | `290-api-reference-pydanticai-integration-count-input-tokens-pydanticai-openai-format.md` | Count input tokens (PydanticAI - OpenAI format) | This document defines the API endpoint for counting input tokens in a PydanticAI-compatible Response... | pydanticai, token-counting, openai-format, api-reference |
| 291 | `291-api-reference-pydanticai-integration-create-embeddings-pydanticai-cohere-format.md` | Create embeddings (PydanticAI - Cohere format) | This document defines the API specification for generating text and multimodal embeddings using a Co... | pydantic-ai, cohere, embeddings, api-reference |
| 292 | `292-api-reference-pydanticai-integration-create-embeddings-pydanticai-openai-format.md` | Create embeddings (PydanticAI - OpenAI format) | This document specifies the API endpoint for creating text embeddings using the PydanticAI framework... | embeddings, pydanticai, openai-compatible, api-endpoint |
| 293 | `293-api-reference-pydanticai-integration-generate-content-pydanticai-gemini-format.md` | Generate content (PydanticAI - Gemini format) | This document defines the OpenAPI specification for generating content using the Google Gemini-compa... | pydanticai, google-gemini, content-generation, openapi |
| 294 | `294-api-reference-pydanticai-integration-create-message-pydanticai-anthropic-format.md` | Create message (PydanticAI - Anthropic format) | This document defines the API endpoint for creating messages using an Anthropic-compatible format th... | pydantic-ai, anthropic, api-gateway, message-creation |
| 295 | `295-api-reference-pydanticai-integration-list-models-pydanticai-gemini-format.md` | List models (PydanticAI - Gemini format) | This document specifies the API endpoint for listing available AI models through the PydanticAI fram... | pydantic-ai, google-gemini, model-listing, bifrost-api |
| 296 | `296-api-reference-pydanticai-integration-list-models-pydanticai-openai-format.md` | List models (PydanticAI - OpenAI format) | This document specifies the API endpoint for retrieving a list of available AI models using the Pyda... | pydantic-ai, openai-compatible, model-listing, api-specification |
| 297 | `297-api-reference-pydanticai-integration-create-response-pydanticai-openai-responses-api.md` | Create response (PydanticAI - OpenAI Responses API) | This document defines the API endpoint for generating AI model responses using the PydanticAI framew... | pydantic-ai, openai-responses, ai-inference, api-gateway |
| 298 | `298-api-reference-pydanticai-integration-create-speech-pydanticai-openai-tts.md` | Create speech (PydanticAI - OpenAI TTS) | This document provides the OpenAPI specification for the PydanticAI-compatible endpoint used to gene... | pydanticai, openai-tts, text-to-speech, api-specification |
| 299 | `299-api-reference-pydanticai-integration-stream-converse-with-model-pydanticai-bedrock-format.md` | Stream converse with model (PydanticAI - Bedrock format) | This document provides the OpenAPI specification for streaming model conversations using the AWS Bed... | pydanticai, aws-bedrock, streaming-api, openapi-spec |
| 300 | `300-api-reference-pydanticai-integration-stream-generate-content-pydanticai-gemini-format.md` | Stream generate content (PydanticAI - Gemini format) | This document provides the OpenAPI specification for the PydanticAI integration endpoint that enable... | openapi, pydanticai, gemini, streaming-api |
| 301 | `301-api-reference-pydanticai-integration-text-completions-pydanticai-openai-format.md` | Text completions (PydanticAI - OpenAI format) | This document defines the PydanticAI-compatible endpoint for generating text completions using the l... | pydanticai, openai-compatible, text-completions, api-gateway |
| 302 | `302-api-reference-pydanticai-integration-tokenize-text-pydanticai-cohere-format.md` | Tokenize text (PydanticAI - Cohere format) | This document defines the OpenAPI specification for tokenizing text using the Cohere v1 API format t... | pydanticai, cohere, tokenization, api-reference |
| 303 | `303-api-reference-pydanticai-integration-create-transcription-pydanticai-openai-whisper.md` | Create transcription (PydanticAI - OpenAI Whisper) | This document provides the OpenAPI specification for the PydanticAI-compatible endpoint used to tran... | pydanticai, openai-whisper, audio-transcription, speech-to-text |

### 24. Changelogs (304-389)
*Version history and release notes*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 304 | `304-changelogs-v1.4.1.md` | v1.4.1 | This document details the updates and bug fixes for Bifrost version 1.4.1, primarily addressing stre... | release-notes, changelog, bifrost, bedrock |
| 305 | `305-changelogs-v1.4.0.md` | v1.4.0 | This document outlines the version 1.4.0 changelog for Bifrost, detailing new features, bug fixes, a... | changelog, release-notes, bifrost, version-update |
| 306 | `306-changelogs-v1.4.0-prerelease10.md` | v1.4.0-prerelease10 | This document provides the release notes for Bifrost version 1.4.0-prerelease10, detailing new featu... | release-notes, bifrost, changelog, image-generation |
| 307 | `307-changelogs-v1.4.0-prerelease9.md` | v1.4.0-prerelease9 | This document outlines the changes in Bifrost version 1.4.0-prerelease9, focusing on fixes for strea... | release-notes, changelog, bifrost, bug-fix |
| 308 | `308-changelogs-v1.4.0-prerelease8.md` | v1.4.0-prerelease8 | This document details the updates and bug fixes for Bifrost version 1.4.0-prerelease8, including mod... | release-notes, changelog, bifrost, vertex-ai |
| 309 | `309-changelogs-v1.4.0-prerelease7.md` | v1.4.0-prerelease7 | This document outlines the changes in Bifrost v1.4.0-prerelease7, focusing on bug fixes for xAI prov... | release-notes, changelog, bifrost, xai-integration |
| 310 | `310-changelogs-v1.4.0-prerelease6.md` | v1.4.0-prerelease6 | This document provides the release notes for Bifrost version 1.4.0-prerelease6, documenting various ... | release-notes, changelog, bifrost, software-updates |
| 311 | `311-changelogs-v1.4.0-prerelease5.md` | v1.4.0-prerelease5 | This document provides the release notes for Bifrost version 1.4.0-prerelease5, detailing bug fixes ... | release-notes, bifrost, changelog, bug-fixes |
| 312 | `312-changelogs-v1.4.0-prerelease4.md` | v1.4.0-prerelease4 | This document provides the release notes and changelog for Bifrost version 1.4.0-prerelease4, detail... | release-notes, changelog, bifrost, gemini-integration |
| 313 | `313-changelogs-v1.4.0-prerelease3.md` | v1.4.0-prerelease3 | This document outlines the updates and bug fixes for the v1.4.0-prerelease3 release, covering provid... | changelog, release-notes, bifrost, bug-fixes |
| 314 | `314-changelogs-v1.4.0-prerelease2.md` | v1.4.0-prerelease2 | This document provides release notes for Bifrost version 1.4.0-prerelease2, detailing bug fixes for ... | release-notes, bifrost, changelog, distributed-tracing |
| 315 | `315-changelogs-v1.4.0-prerelease1.md` | v1.4.0-prerelease1 | Release notes for Bifrost v1.4.0-prerelease1 detailing new MCP gateway features, end-to-end tracing,... | release-notes, breaking-changes, bifrost, middleware |
| 316 | `316-changelogs-v1.3.63.md` | v1.3.63 | This document details the changelog for version 1.3.63 of Bifrost, covering bug fixes for authentica... | changelog, release-notes, bifrost, version-update |
| 317 | `317-changelogs-v1.3.62.md` | v1.3.62 | This document provides the release notes for version 1.3.62, detailing the specific version update a... | release-notes, changelog, versioning, software-update |
| 318 | `318-changelogs-v1.3.61.md` | v1.3.61 | This document outlines the updates for Bifrost version 1.3.61, including bug fixes for Gemini chat c... | changelog, release-notes, bifrost, gemini-integration |
| 319 | `319-changelogs-v1.3.60.md` | v1.3.60 | This document outlines the version 1.3.60 release notes for the Bifrost platform, detailing updates ... | changelog, release-notes, bifrost, version-update |
| 320 | `320-changelogs-v1.3.59.md` | v1.3.59 | This document outlines the changes, bug fixes, and new features introduced in Bifrost version 1.3.59... | release-notes, changelog, bifrost, gemini |
| 321 | `321-changelogs-v1.3.58.md` | v1.3.58 | Release notes for Bifrost v1.3.58, highlighting new Azure Entra ID support and fixes for Anthropic a... | changelog, release-notes, bifrost, azure-entra-id |
| 322 | `322-changelogs-v1.3.57.md` | v1.3.57 | This document details the version 1.3.57 release notes for Bifrost, including bug fixes for configur... | changelog, release-notes, bifrost, version-update |
| 323 | `323-changelogs-v1.3.56.md` | v1.3.56 | This document provides the changelog for Bifrost version 1.3.56, detailing bug fixes for configurati... | changelog, release-notes, bifrost, version-update |
| 324 | `324-changelogs-v1.3.54.md` | v1.3.54 | This document outlines the changes in Bifrost version 1.3.54, highlighting new document support for ... | release-notes, changelog, bifrost, ai-providers |
| 325 | `325-changelogs-v1.3.53.md` | v1.3.53 | This document outlines the changes and bug fixes introduced in Bifrost version 1.3.53, including imp... | changelog, release-notes, bifrost, bug-fixes |
| 326 | `326-changelogs-v1.3.52.md` | v1.3.52 | This document provides the release notes for version 1.3.52 of Bifrost, detailing bug fixes, new mod... | release-notes, changelog, bifrost, gemini |
| 327 | `327-changelogs-v1.3.51.md` | v1.3.51 | This document outlines the changes, bug fixes, and new features introduced in version 1.3.51 of Bifr... | release-notes, changelog, bifrost, huggingface |
| 328 | `328-changelogs-v1.3.50.md` | v1.3.50 | This document provides the release notes for version 1.3.50, detailing new features, bug fixes, and ... | release-notes, changelog, bifrost, api-updates |
| 329 | `329-changelogs-v1.3.49.md` | v1.3.49 | This document outlines the changes in Bifrost version 1.3.49, detailing new features such as batch A... | changelog, release-notes, bifrost, batch-api |
| 330 | `330-changelogs-v1.3.48.md` | v1.3.48 | This document outlines the release notes and deployment instructions for Bifrost version 1.3.48, fea... | release-notes, bifrost, security-patch, docker |
| 331 | `331-changelogs-v1.3.47.md` | v1.3.47 | This document outlines the version 1.3.47 release notes for Bifrost, detailing new features such as ... | changelog, bifrost, release-notes, chat-completions |
| 332 | `332-changelogs-v1.3.46.md` | v1.3.46 | This document provides the release notes and update instructions for Bifrost version 1.3.46, which i... | changelog, release-notes, security-patch, hotfix |
| 333 | `333-changelogs-v1.3.45.md` | v1.3.45 | This document details the changelog for Bifrost version 1.3.45, providing information on new feature... | changelog, release-notes, bifrost, version-update |
| 334 | `334-changelogs-v1.3.44.md` | v1.3.44 | This document provides the release notes and changelog for Bifrost version 1.3.44, detailing new fea... | changelog, release-notes, rbac, bifrost |
| 335 | `335-changelogs-v1.3.43.md` | v1.3.43 | This document outlines the updates and new features introduced in version 1.3.43 of Bifrost, includi... | release-notes, bifrost-updates, docker-deployment, proxy-support |
| 336 | `336-changelogs-v1.3.42.md` | v1.3.42 | This document provides the release notes for Bifrost version 1.3.42, detailing installation instruct... | release-notes, changelog, bifrost, version-update |
| 337 | `337-changelogs-v1.3.41.md` | v1.3.41 | This document provides the release notes for version 1.3.41, detailing a critical fix for Docker seg... | release-notes, bifrost, docker-fix, plugin-update |
| 338 | `338-changelogs-v1.3.40.md` | v1.3.40 | This document outlines the release notes and update instructions for Bifrost version 1.3.40, featuri... | release-notes, bifrost, security-update, docker |
| 339 | `339-changelogs-v1.3.39.md` | v1.3.39 | This document provides the release notes for Bifrost version 1.3.39, detailing improvements to strea... | changelog, release-notes, bifrost, streaming-fix |
| 340 | `340-changelogs-v1.3.38.md` | v1.3.38 | This document provides the release notes for version 1.3.38, detailing new features like Anthropic m... | release-notes, changelog, bifrost, anthropic |
| 341 | `341-changelogs-v1.3.37.md` | v1.3.37 | This document details the release notes for version 1.3.37, covering new SDK support, breaking chang... | release-notes, changelog, bifrost, breaking-changes |
| 342 | `342-changelogs-v1.3.36.md` | v1.3.36 | This document provides the changelog and release notes for Bifrost version 1.3.36, detailing new fea... | changelog, release-notes, bifrost, bug-fixes |
| 343 | `343-changelogs-v1.3.35.md` | v1.3.35 | This document outlines the updates and bug fixes for Bifrost version 1.3.35, including new support f... | changelog, release-notes, qdrant, vector-search |
| 344 | `344-changelogs-v1.3.34.md` | v1.3.34 | This document outlines the release notes and changelog for Bifrost version 1.3.34, detailing feature... | release-notes, changelog, bifrost, version-update |
| 345 | `345-changelogs-v1.3.33.md` | v1.3.33 | This document outlines the updates and bug fixes in version 1.3.33 of Bifrost, including new log ret... | release-notes, changelog, log-management, token-caching |
| 346 | `346-changelogs-v1.3.32.md` | v1.3.32 | This document outlines the version 1.3.32 changelog for Bifrost, detailing new features for Anthropi... | release-notes, changelog, bifrost, anthropic-integration |
| 347 | `347-changelogs-v1.3.31.md` | v1.3.31 | This document outlines the release notes and update details for Bifrost version 1.3.31, including in... | changelog, release-notes, bifrost, version-update |
| 348 | `348-changelogs-v1.3.30.md` | v1.3.30 | This document outlines the changes in version 1.3.30 of Bifrost, including database migrations for t... | changelog, release-notes, bifrost, database-migration |
| 349 | `349-changelogs-v1.3.29.md` | v1.3.29 | This document provides the release notes and changelog for version 1.3.29 of the Bifrost platform, d... | changelog, release-notes, bifrost, metrics |
| 350 | `350-changelogs-v1.3.28.md` | v1.3.28 | This document outlines the v1.3.28 release notes for Bifrost, detailing performance optimizations fo... | changelog, release-notes, bifrost, performance-optimization |
| 351 | `351-changelogs-v1.3.27.md` | v1.3.27 | This document provides the release notes for Bifrost version 1.3.27, detailing fixes for Bedrock mem... | bifrost, changelog, release-notes, bedrock |
| 352 | `352-changelogs-v1.3.26.md` | v1.3.26 | This document outlines the changes in version 1.3.26, featuring the addition of Elevenlabs provider ... | release-notes, changelog, elevenlabs-integration, bifrost-update |
| 353 | `353-changelogs-v1.3.25.md` | v1.3.25 | This document provides the release notes for Bifrost version 1.3.25, detailing updates to the core e... | changelog, release-notes, bifrost, vertex-ai |
| 354 | `354-changelogs-v1.3.24.md` | v1.3.24 | This document provides the changelog for Bifrost version 1.3.24, detailing core and framework update... | release-notes, changelog, bifrost, software-update |
| 355 | `355-changelogs-v1.3.23.md` | v1.3.23 | This document outlines the release notes and changelog for version 1.3.23 of the Bifrost platform, d... | release-notes, changelog, bifrost, mcp-client |
| 356 | `356-changelogs-v1.3.22.md` | v1.3.22 | This document provides the release notes for Bifrost version 1.3.22, detailing new features, breakin... | changelog, release-notes, bifrost, version-update |
| 357 | `357-changelogs-v1.3.21.md` | v1.3.21 | This document details the changelog and deployment commands for Bifrost version 1.3.21, including bu... | bifrost, changelog, version-update, http-proxy |
| 358 | `358-changelogs-v1.3.20.md` | v1.3.20 | This document provides release notes and installation instructions for Bifrost version 1.3.20, inclu... | bifrost, release-notes, changelog, bug-fix |
| 359 | `359-changelogs-v1.3.19.md` | v1.3.19 | This document provides the release notes for Bifrost version v1.3.19, detailing new features in tele... | changelog, release-notes, bifrost, telemetry |
| 360 | `360-changelogs-v1.3.18.md` | v1.3.18 | This document outlines the updates and bug fixes introduced in Bifrost version 1.3.18, including cha... | bifrost, changelog, release-notes, v1-3-18 |
| 361 | `361-changelogs-v1.3.17.md` | v1.3.17 | This document provides the release notes and installation commands for Bifrost version 1.3.17, cover... | changelog, release-notes, bifrost, version-update |
| 362 | `362-changelogs-v1.3.16.md` | v1.3.16 | This document details the updates in version 1.3.16 of Bifrost, highlighting new provider support fo... | changelog, bifrost, release-notes, perplexity |
| 363 | `363-changelogs-v1.3.15.md` | v1.3.15 | This document provides the release notes and changelog for version v1.3.15 of the Bifrost platform, ... | release-notes, changelog, bifrost, version-update |
| 364 | `364-changelogs-v1.3.14.md` | v1.3.14 | This document provides the release notes for Bifrost version 1.3.14, detailing new features such as ... | release-notes, changelog, bifrost, software-update |
| 365 | `365-changelogs-v1.3.13.md` | v1.3.13 | This document provides the release notes and changelog for Bifrost version 1.3.13, detailing new fea... | bifrost, release-notes, changelog, versioning |
| 366 | `366-changelogs-v1.3.12.md` | v1.3.12 | This document provides the release notes for Bifrost version 1.3.12, detailing new features such as ... | release-notes, changelog, bifrost-updates, azure-integration |
| 367 | `367-changelogs-v1.3.11.md` | v1.3.11 | This document details the release notes for Bifrost version 1.3.11, highlighting new features such a... | release-notes, bifrost, version-update, api-changes |
| 368 | `368-changelogs-v1.3.10.md` | v1.3.10 | This document provides the version 1.3.10 changelog for Bifrost, detailing new features, performance... | release-notes, changelog, bifrost, otel |
| 369 | `369-changelogs-v1.3.9.md` | v1.3.9 | This document provides the release notes and installation instructions for Bifrost version 1.3.9, in... | bifrost, changelog, release-notes, azure |
| 370 | `370-changelogs-v1.3.8.md` | v1.3.8 | Detailed release notes for Bifrost version 1.3.8, highlighting bug fixes for OpenAI and Gemini provi... | release-notes, bifrost, changelog, bug-fixes |
| 371 | `371-changelogs-v1.3.7.md` | v1.3.7 | This document provides the release notes and changelog for Bifrost version 1.3.7, detailing installa... | release-notes, changelog, version-update, bug-fixes |
| 372 | `372-changelogs-v1.3.6.md` | v1.3.6 | This document details the changes and updates in Bifrost version 1.3.6, including bug fixes for tool... | changelog, release-notes, bifrost, docker |
| 373 | `373-changelogs-v1.3.5.md` | v1.3.5 | This document outlines the release notes and changelog for Bifrost version 1.3.5, detailing new feat... | changelog, release-notes, bifrost, software-update |
| 374 | `374-changelogs-v1.3.4.md` | v1.3.4 | This document provides the changelog for Bifrost version 1.3.4, detailing updates to the HTTP interf... | changelog, release-notes, bifrost, mcp-tools |
| 375 | `375-changelogs-v1.3.3.md` | v1.3.3 | This document details the changelog for version 1.3.3 of the Bifrost platform, highlighting bug fixe... | changelog, release-notes, bifrost, version-update |
| 376 | `376-changelogs-v1.3.2.md` | v1.3.2 | This document outlines the changes in Bifrost version 1.3.2, including major refactoring of context ... | release-notes, changelog, bifrost, version-update |
| 377 | `377-changelogs-v1.3.1.md` | v1.3.1 | Detailed release notes for Bifrost version 1.3.1, covering installation steps and specific updates a... | bifrost, changelog, release-notes, bug-fixes |
| 378 | `378-changelogs-v1.3.0.md` | v1.3.0 | This document outlines the version 1.3.0 release notes for Bifrost, detailing new features like Open... | changelog, release-notes, bifrost, opentelemetry |
| 379 | `379-changelogs-v1.3.0-prerelease7.md` | v1.3.0-prerelease7 | Detailed changelog for Bifrost v1.3.0-prerelease7, highlighting new streaming capabilities, telemetr... | bifrost, release-notes, changelog, streaming |
| 380 | `380-changelogs-v1.3.0-prerelease6.md` | v1.3.0-prerelease6 | This document outlines the changes and new features in the v1.3.0-prerelease6 update for Bifrost, in... | release-notes, changelog, bifrost, anthropic-integration |
| 381 | `381-changelogs-v1.3.0-prerelease5.md` | v1.3.0-prerelease5 | This document outlines the changes and updates included in the v1.3.0-prerelease5 release of Bifrost... | release-notes, changelog, bifrost, anthropic |
| 382 | `382-changelogs-v1.3.0-prerelease4.md` | v1.3.0-prerelease4 | This document outlines the changes and installation steps for Bifrost version 1.3.0-prerelease4, fea... | bifrost, changelog, release-notes, groq |
| 383 | `383-changelogs-v1.3.0-prerelease3.md` | v1.3.0-prerelease3 | This document provides the changelog for Bifrost version 1.3.0-prerelease3, detailing bug fixes for ... | bifrost, release-notes, changelog, openai-integration |
| 384 | `384-changelogs-v1.3.0-prerelease2.md` | v1.3.0-prerelease2 | This document outlines the release notes and installation instructions for Bifrost version 1.3.0-pre... | release-notes, bifrost, text-completion, streaming-support |
| 385 | `385-changelogs-v1.3.0-prerelease1.md` | v1.3.0-prerelease1 | This document provides the changelog for Bifrost version 1.3.0-prerelease1, detailing new features, ... | changelog, release-notes, bifrost, observability |
| 386 | `386-changelogs-v1.2.24.md` | v1.2.24 | This document details the updates and bug fixes for Bifrost version 1.2.24, including component upgr... | release-notes, changelog, bifrost, version-update |
| 387 | `387-changelogs-v1.2.23.md` | v1.2.23 | This document details the release notes and changelog for version 1.2.23 of the Bifrost platform, in... | changelog, release-notes, bifrost, software-update |
| 388 | `388-changelogs-v1.2.22.md` | v1.2.22 | This document provides the release notes for Bifrost version 1.2.22, detailing bug fixes for streami... | release-notes, changelog, bifrost, bug-fixes |
| 389 | `389-changelogs-v1.2.21.md` | v1.2.21 | This document outlines the changes in Bifrost version 1.2.21, including fixes for pricing computatio... | bifrost, changelog, release-notes, bug-fix |

---

## Quick Reference

### By Topic

| Topic | File Range | Count |
|-------|------------|-------|
| **Meta & Resources** | 001-002 | 2 |
| **Gateway Quickstart** | 003-010 | 8 |
| **Go SDK Quickstart** | 011-017 | 7 |
| **SDK Integrations** | 018-028 | 11 |
| **Features** | 029-043 | 15 |
| **Model Context Protocol** | 044-051 | 8 |
| **Plugins** | 052-056 | 5 |
| **Providers** | 057-080 | 24 |
| **Enterprise** | 081-094 | 14 |
| **Deployment Guides** | 095-100 | 6 |
| **Architecture** | 101-110 | 10 |
| **Benchmarking** | 111-114 | 4 |
| **Contributing** | 115-119 | 5 |
| **API Reference - Core** | 120-141 | 22 |
| **API Reference - Configuration** | 142-191 | 50 |
| **API Reference - Anthropic** | 192-204 | 13 |
| **API Reference - OpenAI** | 205-230 | 26 |
| **API Reference - Bedrock** | 231-238 | 8 |
| **API Reference - Gemini** | 239-248 | 10 |
| **API Reference - Cohere** | 249-251 | 3 |
| **API Reference - LangChain** | 252-269 | 18 |
| **API Reference - LiteLLM** | 270-286 | 17 |
| **API Reference - PydanticAI** | 287-303 | 17 |
| **Changelogs** | 304-389 | 86 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for project links and meta information
- Complete files **003-019** for Gateway and SDK quickstart guides

### Level 2: Core Understanding
- Learn SDK integrations from files **020-029**
- Explore core features in files **030-049**

### Level 3: Advanced Features
- Understand MCP integration in files **050-057**
- Master plugins in files **058-062**
- Configure providers in files **063-087**

### Level 4: Enterprise & Deployment
- Explore enterprise features in files **088-102**
- Learn deployment options in files **103-108**
- Understand architecture in files **109-119**

### Level 5: Performance & Development
- Run benchmarks with files **120-123**
- Contribute to development with files **124-128**

### Level 6: API Reference
- Core APIs in files **129-154**
- Configuration APIs in files **155-186**
- Provider-specific APIs in files **187-332**

### Level 7: Version History
- Review changelogs in files **333-389** (newest to oldest)

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the documentation structure.*
