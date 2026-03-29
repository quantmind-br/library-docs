---
title: Configuration file
url: https://docs.docker.com/ai/cagent/reference/config/
source: llms
fetched_at: 2026-01-24T14:13:40.230666408-03:00
rendered_js: false
word_count: 811
summary: This document provides a technical specification for the YAML configuration file used by cagent agents, detailing parameters for models, toolsets, RAG sources, and agent delegation strategies.
tags:
    - cagent
    - yaml-configuration
    - ai-agents
    - rag-configuration
    - toolsets
    - model-parameters
category: configuration
---

## Configuration file reference

This reference documents the YAML configuration file format for cagent agents. It covers file structure, agent parameters, model configuration, toolset setup, and RAG sources.

For detailed documentation of each toolset's capabilities and specific options, see the [Toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/).

A configuration file has four top-level sections:

PropertyTypeDescriptionRequired`model`stringModel reference or nameYes`description`stringBrief description of agent's purposeNo`instruction`stringDetailed behavior instructionsYes`sub_agents`arrayAgent names for task delegationNo`handoffs`arrayAgent names for conversation handoffNo`toolsets`arrayAvailable toolsNo`welcome_message`stringMessage displayed on startNo`add_date`booleanInclude current date in contextNo`add_environment_info`booleanInclude working directory, OS, Git infoNo`add_prompt_files`arrayPrompt file paths to includeNo`max_iterations`integerMaximum tool call loops (unlimited if not set)No`num_history_items`integerConversation history limitNo`code_mode_tools`booleanEnable Code Mode for toolsNo`commands`objectNamed prompts accessible via `/command_name`No`structured_output`objectJSON schema for structured responsesNo`rag`arrayRAG source namesNo

### [Task delegation versus conversation handoff](#task-delegation-versus-conversation-handoff)

Agents support two different delegation mechanisms. Choose based on whether you need task results or conversation control.

#### [Sub\_agents: Hierarchical task delegation](#sub_agents-hierarchical-task-delegation)

Use `sub_agents` for hierarchical task delegation. The parent agent assigns a specific task to a child agent using the `transfer_task` tool. The child executes in its own context and returns results. The parent maintains control and can delegate to multiple agents in sequence.

This works well for structured workflows where you need to combine results from specialists, or when tasks have clear boundaries. Each delegated task runs independently and reports back to the parent.

**Example:**

Root calls: `transfer_task(agent="researcher", task="Find pricing data")`. The researcher completes the task and returns results to root.

#### [Handoffs: Conversation transfer](#handoffs-conversation-transfer)

Use `handoffs` to transfer conversation control to a different agent. When an agent uses the `handoff` tool, the new agent takes over completely. The original agent steps back until someone hands back to it.

This works well when different agents should own different parts of an ongoing conversation, or when specialists need to collaborate as peers without a coordinator managing every step.

**Example:**

When the user asks about query performance, generalist executes: `handoff(agent="database_expert")`. The database expert now owns the conversation and can continue working with the user directly, or hand off to security\_expert if the discussion shifts to SQL injection concerns.

### [Commands](#commands)

Named prompts users invoke with `/command_name`. Supports JavaScript template literals with `${env.VARIABLE}` for environment variables:

Run with: `cagent run config.yaml /greet`

### [Structured output](#structured-output)

Constrain responses to a JSON schema (OpenAI and Gemini only):

PropertyTypeDescriptionRequired`provider`string`openai`, `anthropic`, `google`, `dmr`Yes`model`stringModel nameYes`temperature`floatRandomness (0.0-2.0)No`max_tokens`integerMaximum response lengthNo`top_p`floatNucleus sampling (0.0-1.0)No`frequency_penalty`floatRepetition penalty (-2.0 to 2.0, OpenAI only)No`presence_penalty`floatTopic penalty (-2.0 to 2.0, OpenAI only)No`base_url`stringCustom API endpointNo`parallel_tool_calls`booleanEnable parallel tool execution (default: true)No`token_key`stringAuthentication token keyNo`track_usage`booleanTrack token usageNo`thinking_budget`mixedReasoning effort (provider-specific)No`provider_opts`objectProvider-specific optionsNo

### [Alloy models](#alloy-models)

Use multiple models in rotation by separating names with commas:

### [Thinking budget](#thinking-budget)

Controls reasoning depth. Configuration varies by provider:

- **OpenAI**: String values - `minimal`, `low`, `medium`, `high`
- **Anthropic**: Integer token budget (1024-32768, must be less than `max_tokens`)
  
  - Set `provider_opts.interleaved_thinking: true` for tool use during reasoning
- **Gemini**: Integer token budget (0 to disable, -1 for dynamic, max 24576)
  
  - Gemini 2.5 Pro: 128-32768, cannot disable (minimum 128)

### [Docker Model Runner (DMR)](#docker-model-runner-dmr)

Run local models. If `base_url` is omitted, cagent auto-discovers via Docker Model plugin.

Pass llama.cpp options via `provider_opts.runtime_flags` (array, string, or multiline):

Model config fields auto-map to runtime flags:

- `temperature` → `--temp`
- `top_p` → `--top-p`
- `max_tokens` → `--context-size`

Explicit `runtime_flags` override auto-mapped flags.

Speculative decoding for faster inference:

Configure tools in the `toolsets` array. Three types: built-in, MCP (local/remote), and Docker Gateway.

> documentation of each toolset's capabilities, available tools, and specific configuration options, see the [Toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/).

All toolsets support common properties like `tools` (whitelist), `defer` (deferred loading), `toon` (output compression), `env` (environment variables), and `instruction` (usage guidance). See the [Toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/) for details on these properties and what each toolset does.

### [Built-in tools](#built-in-tools)

### [MCP tools](#mcp-tools)

Local process:

Remote server:

### [Docker MCP Gateway](#docker-mcp-gateway)

Containerized tools from [Docker MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/):

Retrieval-augmented generation for document knowledge bases. Define sources at the top level, reference in agents.

### [Retrieval strategies](#retrieval-strategies)

All strategies support chunking configuration. Chunk size and overlap are measured in characters (Unicode code points), not tokens.

#### [Chunked-embeddings](#chunked-embeddings)

Direct semantic search using vector embeddings. Best for understanding intent, synonyms, and paraphrasing.

FieldTypeDefault`embedding_model`string-`database`string-`vector_dimensions`integer-`similarity_metric`stringcosine`threshold`float0.5`limit`integer5`chunking.size`integer1000`chunking.overlap`integer75`chunking.respect_word_boundaries`booleantrue`chunking.code_aware`booleanfalse

#### [Semantic-embeddings](#semantic-embeddings)

LLM-enhanced semantic search. Uses a language model to generate rich semantic summaries of each chunk before embedding, capturing deeper meaning.

FieldTypeDefault`embedding_model`string-`chat_model`string-`database`string-`vector_dimensions`integer-`similarity_metric`stringcosine`threshold`float0.5`limit`integer5`ast_context`booleanfalse`semantic_prompt`string-`chunking.size`integer1000`chunking.overlap`integer75`chunking.respect_word_boundaries`booleantrue`chunking.code_aware`booleanfalse

#### [BM25](#bm25)

Keyword-based search using BM25 algorithm. Best for exact terms, technical jargon, and code identifiers.

FieldTypeDefault`database`string-`k1`float1.5`b`float0.75`threshold`float0.0`limit`integer5`chunking.size`integer1000`chunking.overlap`integer75`chunking.respect_word_boundaries`booleantrue`chunking.code_aware`booleanfalse

### [Hybrid retrieval](#hybrid-retrieval)

Combine multiple strategies with fusion:

Fusion strategies:

- `rrf`: Reciprocal Rank Fusion (recommended, rank-based, no normalization needed)
- `weighted`: Weighted combination (`fusion.weights: {chunked-embeddings: 0.7, bm25: 0.3}`)
- `max`: Maximum score across strategies

### [Reranking](#reranking)

Re-score results with a specialized model for improved relevance:

DMR native reranking:

### [Code-aware chunking](#code-aware-chunking)

For source code, use AST-based chunking. With semantic-embeddings, you can include AST metadata in the LLM prompts:

### [RAG properties](#rag-properties)

Top-level RAG source:

FieldTypeDescription`docs`\[]stringDocument paths (suppports glob patterns, respects `.gitignore`)`tool`objectCustomize RAG tool name/description/instruction`strategies`\[]objectRetrieval strategies (see above for strategy-specific fields)`results`objectPost-processing (fusion, reranking, limits)

Results:

FieldTypeDefault`limit`integer15`deduplicate`booleantrue`include_score`booleanfalse`fusion.strategy`string-`fusion.k`integer60`fusion.weights`object-`reranking.model`string-`reranking.top_k`integer0`reranking.threshold`float0.5`reranking.criteria`string""`return_full_content`booleanfalse

Documentation and sharing information:

PropertyTypeDescription`author`stringAuthor name`license`stringLicense (e.g., MIT, Apache-2.0)`readme`stringUsage documentation

Complete configuration demonstrating key features:

- Read the [Toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/) for detailed toolset documentation
- Review the [CLI reference](https://docs.docker.com/ai/cagent/reference/cli/) for command-line options
- Browse [example configurations](https://github.com/docker/cagent/tree/main/examples)
- Learn about [sharing agents](https://docs.docker.com/ai/cagent/sharing-agents/)