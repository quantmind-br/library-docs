# Pydantic AI Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://ai.pydantic.dev/sitemap.xml |
| **Generated** | 2026-01-22T22:26:31.945986339-03:00 |
| **Organized** | 2026-01-23T01:28:48.165606+00:00 |
| **Total Documents** | 151 |
| **Strategy** | sitemap |

---

## Document Index

### 1. Introduction & Overview (001-001)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Pydantic AI | Pydantic AI is a Python framework for building production-grade Generative AI agents and workflows u... | pydantic-ai, agent-framework, python |

### 2. Installation (002-002)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 002 | `002-install.md` | Installation | This document provides comprehensive instructions for installing the Pydantic AI library, detailing ... | installation, pydantic-ai, python-package |

### 3. Core Concepts (003-005)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-agents.md` | Agents | This document introduces the Agent class as the primary interface for Pydantic AI, detailing its cor... | pydantic-ai, agent-interface, llm-integration |
| 004 | `004-dependencies.md` | Dependencies | This document explains how to use Pydantic AI's dependency injection system to pass type-safe data a... | dependency-injection, pydantic-ai, type-safety |
| 005 | `005-message-history.md` | Messages and chat history | This document explains how to access and retrieve message history from Pydantic AI agent runs using ... | pydantic-ai, message-history, agent-run |

### 4. Tools (006-012)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-tools.md` | Function Tools | This document explains how to use function tools in Pydantic AI to enable models to perform actions ... | pydantic-ai, function-tools, tool-registration |
| 007 | `007-toolsets.md` | Toolsets | This document explains how to use toolsets in Pydantic AI to organize, reuse, and dynamically manage... | pydantic-ai, toolsets, agent-configuration |
| 008 | `008-builtin-tools.md` | Built-in Tools | This document explains how to use native built-in tools provided by LLM providers within Pydantic AI... | pydantic-ai, built-in-tools, agent-capabilities |
| 009 | `009-common-tools.md` | Common Tools | This document explains how to install and integrate native web search tools, such as DuckDuckGo and ... | pydantic-ai, web-search, duckduckgo |
| 010 | `010-deferred-tools.md` | Deferred Tools | This document explains how to implement deferred tools in Pydantic AI for scenarios requiring human ... | pydantic-ai, deferred-tools, human-in-the-loop |
| 011 | `011-tools-advanced.md` | Advanced Tool Features | This document explains advanced tool functionalities in Pydantic AI, focusing on multi-modal return ... | pydantic-ai, tool-calling, multi-modal |
| 012 | `012-third-party-tools.md` | Third-Party Tools | This document explains how to integrate third-party tool ecosystems like LangChain and ACI.dev into ... | pydantic-ai, langchain-integration, aci-dev |

### 5. Input & Output (013-018)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 013 | `013-input.md` | Image, Audio, Video & Document Input | This document explains how to provide multimodal inputs such as images, audio, video, and documents ... | pydantic-ai, multimodal-input, binary-content |
| 014 | `014-output.md` | Output | This document explains how to define and handle agent outputs, including structured data validation ... | pydantic-ai, structured-output, agent-run-result |
| 015 | `015-thinking.md` | Thinking | This document explains how to enable and configure reasoning or 'thinking' capabilities for various ... | pydantic-ai, llm-reasoning, model-configuration |
| 016 | `016-direct.md` | Direct Model Requests | The direct module provides low-level, imperative functions for making synchronous and asynchronous r... | pydantic-ai, llm-api, direct-module |
| 017 | `017-embeddings.md` | Embeddings | This document explains how to use the Pydantic AI embedding interface to generate vector representat... | pydantic-ai, embeddings, vector-embeddings |
| 018 | `018-retries.md` | HTTP Request Retries | This document explains how to implement and configure retry functionality in Pydantic AI using custo... | pydantic-ai, tenacity, retry-logic |

### 6. Models Overview (019-019)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 019 | `019-models-overview.md` | Overview | This document outlines the supported LLM providers for Pydantic AI and explains core concepts such a... | model-providers, pydantic-ai, llm-integration |

### 7. Model Providers (020-031)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 020 | `020-models-openai.md` | OpenAI | This document provides instructions for installing and configuring OpenAI and Azure OpenAI models wi... | pydantic-ai, openai, azure-openai |
| 021 | `021-models-anthropic.md` | Anthropic | Provides comprehensive instructions for integrating Anthropic Claude models with Pydantic AI, includ... | anthropic, claude, pydantic-ai |
| 022 | `022-models-google.md` | Google | This document provides instructions for installing, configuring, and using the GoogleModel in Pydant... | google-genai, gemini, vertex-ai |
| 023 | `023-models-bedrock.md` | Bedrock | This document explains how to integrate and configure AWS Bedrock models within the Pydantic AI fram... | aws-bedrock, pydantic-ai, llm-integration |
| 024 | `024-models-mistral.md` | Mistral | This document explains how to install and configure Mistral models for use with Pydantic AI, coverin... | pydantic-ai, mistral-ai, python-setup |
| 025 | `025-models-groq.md` | Groq | This document provides instructions for installing, configuring, and using Groq models within the Py... | groq, pydantic-ai, python |
| 026 | `026-models-cohere.md` | Cohere | This document explains how to install and configure Cohere models for use with PydanticAI, covering ... | cohere, pydantic-ai, installation |
| 027 | `027-models-huggingface.md` | Hugging Face | This document explains how to integrate Hugging Face models with PydanticAI, covering installation, ... | pydantic-ai, hugging-face, llm-integration |
| 028 | `028-models-openrouter.md` | OpenRouter | This document provides instructions for installing and configuring OpenRouter models within the Pyda... | pydantic-ai, openrouter, model-configuration |
| 029 | `029-models-cerebras.md` | Cerebras | This document explains how to install and configure Cerebras models within the PydanticAI framework,... | pydantic-ai, cerebras, model-configuration |
| 030 | `030-models-xai.md` | xAI | This document provides instructions for installing and configuring xAI models within the Pydantic AI... | pydantic-ai, xai-model, python-sdk |
| 031 | `031-models-outlines.md` | Outlines | This document explains how to install, initialize, and run Outlines models within the Pydantic AI fr... | pydantic-ai, outlines, structured-output |

### 8. MCP (Model Context Protocol) (032-035)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-mcp-overview.md` | Overview | This document explains how Pydantic AI integrates with the Model Context Protocol (MCP), outlining d... | model-context-protocol, mcp, pydantic-ai |
| 033 | `033-mcp-client.md` | Client | This document explains how to integrate Pydantic AI agents with MCP (Model Context Protocol) servers... | pydantic-ai, mcp-client, model-context-protocol |
| 034 | `034-mcp-server.md` | Server | This document explains how to integrate Pydantic AI agents into Model Context Protocol (MCP) servers... | pydantic-ai, mcp-server, mcp-client |
| 035 | `035-mcp-fastmcp-client.md` | FastMCP Client | This document explains how to integrate FastMCP with Pydantic AI using the FastMCPToolset, covering ... | fastmcp, pydantic-ai, toolsets |

### 9. Pydantic Graph (036-036)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-graph.md` | Overview | This document introduces pydantic-graph, a type-safe library for building asynchronous graphs and fi... | pydantic-graph, state-machine, python |

### 10. Graph Beta API (037-041)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 037 | `037-graph-beta.md` | Getting Started | This document introduces the beta graph API in pydantic-graph, explaining how to use the builder pat... | pydantic-graph, graph-api, parallel-execution |
| 038 | `038-graph-beta-steps.md` | Steps | This document explains how to define and use steps as the fundamental units of work in a graph, cove... | pydantic-graph, python, asynchronous |
| 039 | `039-graph-beta-decisions.md` | Decisions | This document explains how to implement conditional branching in graphs using decision nodes, coveri... | pydantic-graph, decision-nodes, conditional-branching |
| 040 | `040-graph-beta-parallel.md` | Parallel Execution | This document explains how to implement parallel execution in the Pydantic Graph beta API using broa... | pydantic-graph, parallel-execution, broadcasting |
| 041 | `041-graph-beta-joins.md` | Joins & Reducers | This document explains how join nodes in Pydantic Graph synchronize and aggregate results from paral... | pydantic-graph, parallel-execution, join-nodes |

### 11. Pydantic Evals (042-056)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 042 | `042-evals.md` | Pydantic Evals | Pydantic Evals is a code-first framework for systematically evaluating AI systems through datasets, ... | pydantic-evals, llm-evaluation, ai-testing |
| 043 | `043-evals-quick-start.md` | Quick Start | Pydantic Evals is a framework for systematically testing and evaluating AI systems using structured ... | pydantic-evals, ai-evaluation, llm-testing |
| 044 | `044-evals-core-concepts.md` | Core Concepts | This document explains the core components and architectural workflow of Pydantic Evals, including h... | pydantic-evals, llm-evaluation, testing-framework |
| 045 | `045-evals-evaluators-overview.md` | Overview | This document explains the core components of Pydantic Evals known as evaluators, which are used to ... | pydantic-evals, llm-evaluation, llm-as-a-judge |
| 046 | `046-evals-evaluators-built-in.md` | Built-in Evaluators | This document details the built-in evaluators provided by Pydantic Evals for verifying model outputs... | pydantic-evals, evaluators, llm-judge |
| 047 | `047-evals-evaluators-custom.md` | Custom Evaluators | This guide explains how to implement custom evaluators in the pydantic-evals framework by subclassin... | pydantic-evals, custom-evaluators, llm-evaluation |
| 048 | `048-evals-evaluators-llm-judge.md` | LLM Judge | This document provides a detailed overview of the LLMJudge evaluator in pydantic-evals, explaining h... | pydantic-evals, llm-judge, ai-evaluation |
| 049 | `049-evals-evaluators-span-based.md` | Span-Based | This document explains how to evaluate AI system behavior by analyzing internal execution paths usin... | span-based-evaluation, pydantic-evals, logfire |
| 050 | `050-evals-examples-simple-validation.md` | Simple Validation | This document provides a practical example of using the pydantic-evals library to perform determinis... | pydantic-evals, validation, unit-testing |
| 051 | `051-evals-how-to-concurrency.md` | Concurrency & Performance | This document explains how to control parallel execution of evaluation cases using the max_concurren... | pydantic-evals, concurrency-control, rate-limiting |
| 052 | `052-evals-how-to-dataset-management.md` | Dataset Management | This document explains how to manage evaluation datasets using pydantic-evals, covering manual creat... | pydantic-evals, dataset-management, evaluations |
| 053 | `053-evals-how-to-dataset-serialization.md` | Dataset Serialization | This document explains how to serialize and deserialize datasets using YAML and JSON formats, includ... | pydantic-evals, serialization, yaml |
| 054 | `054-evals-how-to-logfire-integration.md` | Logfire Integration | This guide explains how to integrate Pydantic Evals with Pydantic Logfire to visualize, analyze, and... | pydantic-evals, pydantic-logfire, opentelemetry |
| 055 | `055-evals-how-to-metrics-attributes.md` | Metrics & Attributes | Explains how to record and use custom numeric metrics and qualitative attributes during task executi... | pydantic-evals, metrics, attributes |
| 056 | `056-evals-how-to-retry-strategies.md` | Retry Strategies | This document explains how to implement automatic retry logic for tasks and evaluators using the Ten... | pydantic-evals, tenacity, error-handling |

### 12. Durable Execution (057-060)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 057 | `057-durable-execution-overview.md` | Overview | This document explains how Pydantic AI supports durable execution to create fault-tolerant, long-run... | durable-execution, pydantic-ai, fault-tolerance |
| 058 | `058-durable-execution-temporal.md` | Temporal | This document explains how to integrate Pydantic AI agents with Temporal to achieve durable executio... | temporal, durable-execution, pydantic-ai |
| 059 | `059-durable-execution-dbos.md` | DBOS | This guide explains how to integrate Pydantic AI agents with DBOS to provide durable execution and s... | dbos, pydantic-ai, durable-execution |
| 060 | `060-durable-execution-prefect.md` | Prefect | This document explains how to integrate Prefect with Pydantic AI to enable durable execution, provid... | prefect, durable-execution, workflow-orchestration |

### 13. UI Integration (061-063)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 061 | `061-ui-overview.md` | Overview | This document explains how to stream real-time agent events to frontends using UI event stream proto... | pydantic-ai, ui-event-streams, streaming-responses |
| 062 | `062-ui-ag-ui.md` | AG-UI | This document explains how to implement the Agent-User Interaction (AG-UI) Protocol within Pydantic ... | pydantic-ai, ag-ui-protocol, fastapi |
| 063 | `063-ui-vercel-ai.md` | Vercel AI | This document explains how to use Pydantic AI's VercelAIAdapter to integrate with the Vercel AI Data... | pydantic-ai, vercel-ai-sdk, data-stream-protocol |

### 14. Guides & Features (064-070)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 064 | `064-gateway.md` | Pydantic AI Gateway | This document introduces the Pydantic AI Gateway, a unified interface for managing multiple LLM prov... | pydantic-ai, ai-gateway, llm-infrastructure |
| 065 | `065-a2a.md` | Agent2Agent (A2A) | This document introduces the Agent2Agent (A2A) Protocol and the FastA2A library, explaining how to i... | a2a-protocol, fasta2a, pydantic-ai |
| 066 | `066-multi-agent-applications.md` | Multi-Agent Patterns | Explains how to coordinate multiple agents in Pydantic AI applications, with a detailed focus on age... | multi-agent, agent-delegation, pydantic-ai |
| 067 | `067-logfire.md` | Debugging & Monitoring with Pydantic Logfire | This document explains how to integrate and use Pydantic Logfire with Pydantic AI to provide observa... | pydantic-ai, logfire, observability |
| 068 | `068-testing.md` | Testing | This document explains strategies and tools for unit testing Pydantic AI applications, focusing on t... | unit-testing, pydantic-ai, pytest |
| 069 | `069-cli.md` | Clai | This document explains how to install and use the Pydantic AI CLI (clai) to interact with AI agents ... | pydantic-ai, cli, ai-agents |
| 070 | `070-web.md` | Web Chat UI | This document explains how to set up and configure the Pydantic AI built-in web chat interface to in... | pydantic-ai, web-ui, agent-to-web |

### 15. Examples (071-084)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 071 | `071-examples-setup.md` | Setup | This document provides instructions for installing dependencies, configuring environment variables, ... | pydantic-ai, example-usage, environment-setup |
| 072 | `072-examples-weather-agent.md` | Weather agent | This document provides a practical implementation guide for creating AI agents capable of sequential... | pydantic-ai, tool-calling, agent-dependencies |
| 073 | `073-examples-bank-support.md` | Bank support | A comprehensive example demonstrating how to build a bank support agent using Pydantic AI, covering ... | pydantic-ai, python, structured-output |
| 074 | `074-examples-pydantic-model.md` | Pydantic Model | This document demonstrates how to use Pydantic AI to extract structured data from text input and map... | pydantic-ai, structured-output, pydantic-model |
| 075 | `075-examples-chat-app.md` | Chat App with FastAPI | This document demonstrates how to build a real-time chat application using FastAPI and Pydantic AI, ... | fastapi, pydantic-ai, streaming |
| 076 | `076-examples-rag.md` | RAG | This document provides a comprehensive example of implementing Retrieval-Augmented Generation (RAG) ... | pydantic-ai, rag, pgvector |
| 077 | `077-examples-sql-gen.md` | SQL Generation | This document demonstrates how to build a Pydantic AI agent that generates and validates PostgreSQL ... | pydantic-ai, sql-generation, postgresql |
| 078 | `078-examples-data-analyst.md` | Data Analyst | This document demonstrates how to use agent dependencies in Pydantic AI to share state and tool outp... | pydantic-ai, agent-dependencies, data-analysis |
| 079 | `079-examples-flight-booking.md` | Flight booking | This document demonstrates a multi-agent orchestration flow where specialized agents delegate tasks ... | pydantic-ai, multi-agent, agent-delegation |
| 080 | `080-examples-question-graph.md` | Question Graph | This document demonstrates how to build an interactive AI-driven question and evaluation system usin... | pydantic-graph, pydantic-ai, agent-orchestration |
| 081 | `081-examples-stream-markdown.md` | Stream markdown | This document demonstrates how to stream markdown text responses from a Pydantic AI agent and render... | pydantic-ai, streaming, markdown |
| 082 | `082-examples-stream-whales.md` | Stream whales | This document demonstrates how to implement and validate streaming structured outputs from an LLM us... | pydantic-ai, streaming-output, structured-data |
| 083 | `083-examples-ag-ui.md` | Agent User Interaction (AG-UI) | This document provides a setup guide and code examples for integrating Pydantic AI agents with the A... | pydantic-ai, ag-ui, ai-agents |
| 084 | `084-examples-slack-lead-qualifier.md` | Slack Lead Qualifier with Modal | This document provides a step-by-step tutorial on building and deploying an AI-powered Slack lead qu... | pydantic-ai, modal-deployment, slack-integration |

### 16. API Reference: Core (085-107)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 085 | `085-api-agent.md` | pydantic_ai.agent | This reference defines the Agent dataclass, which serves as the primary interface for configuring an... | pydantic-ai, llm-agent, python-api |
| 086 | `086-api-run.md` | pydantic_ai.run | The AgentRun class provides a stateful and async-iterable interface for managing and inspecting the ... | pydantic-ai, agent-run, async-iterator |
| 087 | `087-api-result.md` | pydantic_ai.result | Defines the StreamedRunResult class for handling and iterating over streamed responses from AI agent... | pydantic-ai, streaming-api, async-python |
| 088 | `088-api-tools.md` | pydantic_ai.tools | This document defines the Tool class in Pydantic AI, which encapsulates Python functions for use by ... | pydantic-ai, tool-definition, function-calling |
| 089 | `089-api-toolsets.md` | pydantic_ai.toolsets | This document defines the FunctionToolset class, which allows Python functions to be registered and ... | pydantic-ai, function-tools, agent-framework |
| 090 | `090-api-output.md` | pydantic_ai.output | Defines classes and type variables for controlling and customizing the structured output format of a... | pydantic-ai, structured-outputs, llm-agents |
| 091 | `091-api-messages.md` | pydantic_ai.messages | This document defines the ModelResponse data structure used to represent and manage LLM outputs, inc... | llm-responses, pydantic-ai, api-reference |
| 092 | `092-api-settings.md` | pydantic_ai.settings | This document defines the ModelSettings TypedDict, which provides common configuration parameters su... | pydantic-ai, llm-configuration, model-settings |
| 093 | `093-api-usage.md` | pydantic_ai.usage | Defines the UsageLimits class for managing and enforcing constraints on API requests, token consumpt... | pydantic-ai, usage-limits, token-counting |
| 094 | `094-api-exceptions.md` | pydantic_ai.exceptions | This document defines the custom exception classes used in the Pydantic AI framework to manage tool ... | pydantic-ai, error-handling, exceptions |
| 095 | `095-api-retries.md` | pydantic_ai.retries | This document defines utilities for implementing retry logic in HTTP requests using the tenacity lib... | pydantic-ai, tenacity, retry-logic |
| 096 | `096-api-direct.md` | pydantic_ai.direct | This document defines the methods for making direct, imperative requests to language models with min... | pydantic-ai, llm-requests, api-reference |
| 097 | `097-api-embeddings.md` | pydantic_ai.embeddings | This document defines the abstract base class for embedding models, providing the standard interface... | embedding-model, abstract-base-class, pydantic-ai |
| 098 | `098-api-mcp.md` | pydantic_ai.mcp | This document defines the base class for integrating agents with Model Context Protocol (MCP) server... | mcp, model-context-protocol, agent-integration |
| 099 | `099-api-providers.md` | pydantic_ai.providers | This document defines the BedrockProvider class for interacting with AWS Bedrock, covering client in... | aws-bedrock, python, api-client |
| 100 | `100-api-profiles.md` | pydantic_ai.profiles | This document defines the OpenAIModelProfile dataclass used to configure settings and compatibility ... | pydantic-ai, openai-model-profile, llm-configuration |
| 101 | `101-api-format-prompt.md` | pydantic_ai.format_prompt | Documentation for the format_as_xml function which serializes Python objects, including Pydantic mod... | python, xml-serialization, pydantic |
| 102 | `102-api-builtin-tools.md` | pydantic_ai.builtin_tools | This document defines the base classes and specific implementations for built-in tools in PydanticAI... | pydantic-ai, builtin-tools, web-search |
| 103 | `103-api-common-tools.md` | pydantic_ai.common_tools | This document provides an API reference for the DuckDuckGo and Exa search tools integrated into Pyda... | pydantic-ai, duckduckgo-search, exa-search |
| 104 | `104-api-ext.md` | pydantic_ai.ext | Provides an API reference for functions and classes that integrate external tools from LangChain and... | pydantic-ai, langchain, aci-dev |
| 105 | `105-api-durable-exec.md` | pydantic_ai.durable_exec | The TemporalAgent class wraps a standard agent to enable durable execution within Temporal workflows... | temporal, durable-execution, pydantic-ai |
| 106 | `106-api-fasta2a.md` | fasta2a | Defines the core FastA2A application class and the Broker abstract base class for building AI agent-... | fasta2a, python, starlette |
| 107 | `107-api-ag-ui.md` | pydantic_ai.ag_ui | This document defines the AGUIApp class, an ASGI application based on Starlette that serves Pydantic... | pydantic-ai, asgi-application, starlette |

### 17. API Reference: Models (108-126)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 108 | `108-api-models-base.md` | pydantic_ai.models | This document defines a Python type alias containing a comprehensive list of supported large languag... | llm-models, python-typing, model-registry |
| 109 | `109-api-models-openai.md` | pydantic_ai.models.openai | This document defines a Python class for interacting with the OpenAI Responses API, providing suppor... | openai-api, python-sdk, llm-integration |
| 110 | `110-api-models-anthropic.md` | pydantic_ai.models.anthropic | This document defines the AnthropicModel class, which provides an interface to the Anthropic API for... | anthropic-api, claude-models, python-client |
| 111 | `111-api-models-google.md` | pydantic_ai.models.google | This document defines the GoogleModel class, which provides a Python interface for interacting with ... | google-gemini, vertex-ai, python-sdk |
| 112 | `112-api-models-bedrock.md` | pydantic_ai.models.bedrock | Implementation of the BedrockConverseModel class which provides a structured interface for interacti... | aws-bedrock, bedrock-converse-api, python-sdk |
| 113 | `113-api-models-mistral.md` | pydantic_ai.models.mistral | This document defines the MistralModel class, which provides an interface for interacting with Mistr... | mistral-ai, python-sdk, llm-integration |
| 114 | `114-api-models-groq.md` | pydantic_ai.models.groq | This document defines the GroqModel class, which provides an interface for interacting with the Groq... | groq, python-sdk, llm-integration |
| 115 | `115-api-models-cohere.md` | pydantic_ai.models.cohere | Implementation of the CohereModel class for integrating the Cohere API into a model framework, handl... | cohere-api, python-sdk, model-integration |
| 116 | `116-api-models-huggingface.md` | pydantic_ai.models.huggingface | This document defines the HuggingFaceModel class, which provides an interface for interacting with H... | hugging-face, inference-api, async-programming |
| 117 | `117-api-models-openrouter.md` | pydantic_ai.models.openrouter | This document defines the Python type hints and configuration schemas used for interacting with Open... | openrouter, pydantic-ai, api-reference |
| 118 | `118-api-models-cerebras.md` | pydantic_ai.models.cerebras | This document defines the technical reference for Cerebras model integration, detailing the model cl... | pydantic-ai, cerebras, llm-integration |
| 119 | `119-api-models-xai.md` | pydantic_ai.models.xai | This document defines the XaiModel class, which implements the integration between Pydantic AI and t... | xai, pydantic-ai, python |
| 120 | `120-api-models-outlines.md` | pydantic_ai.models.outlines | This document defines the OutlinesModel class, which integrates the Outlines library to provide stru... | outlines-library, hugging-face, llama-cpp |
| 121 | `121-api-models-fallback.md` | pydantic_ai.models.fallback | The FallbackModel class implements a failover mechanism that attempts to use alternative models sequ... | fallback-models, error-handling, llm-integration |
| 122 | `122-api-models-function.md` | pydantic_ai.models.function | The FunctionModel class implements a model provider controlled by local Python functions, supporting... | python, function-model, asynchronous-programming |
| 123 | `123-api-models-test.md` | pydantic_ai.models.test | This document defines the TestModel class, a mock model implementation used for testing AI agents by... | python, testing, mock-model |
| 124 | `124-api-models-wrapper.md` | pydantic_ai.models.wrapper | This document defines the WrapperModel base class, which provides a structural foundation for wrappi... | python, model-wrapper, delegation-pattern |
| 125 | `125-api-models-instrumented.md` | pydantic_ai.models.instrumented | This document defines the InstrumentationSettings class, which provides configuration options for mo... | pydantic-ai, opentelemetry, instrumentation |
| 126 | `126-api-models-mcp-sampling.md` | pydantic_ai.models.mcp_sampling | This document defines the MCPSamplingModel and MCPSamplingModelSettings classes, which enable MCP se... | mcp-sampling, model-context-protocol, pydantic-ai |

### 18. API Reference: Graph (127-138)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 127 | `127-api-pydantic-graph-graph.md` | pydantic_graph | This document defines the Graph class in the pydantic-graph library, which manages a collection of n... | pydantic-graph, python, workflow-orchestration |
| 128 | `128-api-pydantic-graph-nodes.md` | pydantic_graph.nodes | This document defines the core API components for pydantic-graph, specifically the BaseNode abstract... | pydantic-graph, python, graph-execution |
| 129 | `129-api-pydantic-graph-mermaid.md` | pydantic_graph.mermaid | This document provides technical documentation for generating Mermaid state diagrams and images from... | pydantic-graph, mermaid-js, state-diagram |
| 130 | `130-api-pydantic-graph-persistence.md` | pydantic_graph.persistence | This document defines the FileStatePersistence class for storing and managing graph run states and n... | pydantic-graph, state-persistence, file-storage |
| 131 | `131-api-pydantic-graph-exceptions.md` | pydantic_graph.exceptions | This document defines the custom exception classes for the pydantic-graph library, covering errors r... | pydantic-graph, python, exceptions |
| 132 | `132-api-pydantic-graph-beta.md` | pydantic_graph.beta | This document defines the GraphBuilder class, providing a fluent interface for constructing executab... | graph-builder, workflow-engine, python-api |
| 133 | `133-api-pydantic-graph-beta-graph.md` | pydantic_graph.beta.graph | This document defines the core Graph class used to represent and execute structured workflows with t... | graph-execution, workflow-engine, python-api |
| 134 | `134-api-pydantic-graph-beta-graph-builder.md` | pydantic_graph.beta.graph_builder | The document defines the GraphBuilder class, a fluent interface for constructing executable graph-ba... | graph-builder, workflow-orchestration, python-api |
| 135 | `135-api-pydantic-graph-beta-step.md` | pydantic_graph.beta.step | This document defines the core abstractions and protocols for step-based graph execution in pydantic... | pydantic-graph, graph-execution, step-functions |
| 136 | `136-api-pydantic-graph-beta-node.md` | pydantic_graph.beta.node | This document defines the fundamental node types for constructing and executing graphs, including en... | pydantic-graph, node-types, graph-execution |
| 137 | `137-api-pydantic-graph-beta-decision.md` | pydantic_graph.beta.decision | The DecisionBranchBuilder class provides a fluent API for defining decision branches in a graph, all... | pydantic-graph, graph-builder, fluent-api |
| 138 | `138-api-pydantic-graph-beta-join.md` | pydantic_graph.beta.join | This document defines the Join class, which is used to synchronize and aggregate parallel execution ... | pydantic-graph, parallel-execution, reducer-functions |

### 19. API Reference: Evals (139-143)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 139 | `139-api-pydantic-evals-dataset.md` | pydantic_evals.dataset | This document defines the Dataset class, which facilitates organizing collections of test cases and ... | pydantic-evals, test-automation, dataset-management |
| 140 | `140-api-pydantic-evals-evaluators.md` | pydantic_evals.evaluators | Defines the abstract base Evaluator class for implementing custom task performance assessments with ... | pydantic-evals, evaluator-base-class, asynchronous-execution |
| 141 | `141-api-pydantic-evals-generation.md` | pydantic_evals.generation | This module provides utilities and an asynchronous function to generate structured evaluation datase... | pydantic-evals, dataset-generation, synthetic-data |
| 142 | `142-api-pydantic-evals-reporting.md` | pydantic_evals.reporting | Defines the EvaluationReport class for aggregating, summarizing, and rendering results from model ev... | python, model-evaluation, reporting |
| 143 | `143-api-pydantic-evals-otel.md` | pydantic_evals.otel | Defines the SpanNode class for representing and querying hierarchical trace spans in a tree structur... | distributed-tracing, python-api, span-tree |

### 20. API Reference: UI (144-146)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 144 | `144-api-ui-base.md` | pydantic_ai.ui | This document defines the `UIAdapter` abstract base class, which facilitates the integration of Pyda... | pydantic-ai, ui-adapter, event-streaming |
| 145 | `145-api-ui-ag-ui.md` | pydantic_ai.ui.ag_ui | This document defines the AGUIApp class, an ASGI application based on Starlette for serving Pydantic... | pydantic-ai, asgi, starlette |
| 146 | `146-api-ui-vercel-ai.md` | pydantic_ai.ui.vercel_ai | This document defines the VercelAIAdapter class, which facilitates integration between the Vercel AI... | vercel-ai, pydantic-ai, ui-adapter |

### 21. Reference & Meta (147-151)

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 147 | `147-changelog.md` | Upgrade Guide | This document outlines the breaking changes and migration requirements for Pydantic AI across variou... | pydantic-ai, breaking-changes, migration-guide |
| 148 | `148-version-policy.md` | Version policy | This document outlines the versioning policy for Pydantic AI, detailing rules for breaking changes, ... | version-policy, backward-compatibility, breaking-changes |
| 149 | `149-contributing.md` | Contributing | This document provides instructions and guidelines for contributing to the Pydantic AI project, incl... | contributing-guide, pydantic-ai, developer-setup |
| 150 | `150-help.md` | Getting Help | This document outlines the available support channels and community resources for users seeking help... | community-support, help-resources, slack-channel |
| 151 | `151-troubleshooting.md` | Troubleshooting | Provides solutions for common errors in Pydantic AI, covering issues with Jupyter event loops, API k... | pydantic-ai, troubleshooting, error-handling |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-005 |
| **Tools & Toolsets** | 006-012 |
| **Input/Output Handling** | 013-018 |
| **LLM Providers** | 019-031 |
| **MCP Integration** | 032-035 |
| **Graph Workflows** | 036-041 |
| **Evaluation Framework** | 042-056 |
| **Durable Execution** | 057-060 |
| **UI Integration** | 061-063 |
| **Examples & Tutorials** | 071-084 |
| **API Reference** | 085-146 |
| **Meta & Support** | 147-151 |

### By Concept

| Concept | Files |
|---------|-------|
| **Agents** | 001, 003, 085 |
| **Structured Output** | 014, 093 |
| **Streaming** | 081, 082 |
| **Dependencies** | 004 |
| **Testing** | 069 |
| **Observability** | 067, 055 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for introduction and installation
- Complete files **003-005** for core agent concepts

### Level 2: Core Features
- Learn tools from files **006-012**
- Understand input/output handling in files **013-018**

### Level 3: Model Integration
- Review model overview in file **019**
- Configure providers in files **020-031**

### Level 4: Practical Application
- Set up examples with file **071**
- Follow tutorials in files **072-084**

### Level 5: Advanced Topics
- Master MCP integration in files **032-035**
- Learn graph workflows in files **036-041**
- Implement evaluation in files **042-056**
- Configure durable execution in files **057-060**

### Level 6: API Deep Dive
- Core API reference in files **085-107**
- Model APIs in files **108-126**
- Graph APIs in files **127-138**
- Evals APIs in files **139-143**
- UI APIs in files **144-146**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*