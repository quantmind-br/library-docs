---
title: Best practices
url: https://docs.docker.com/ai/cagent/best-practices/
source: llms
fetched_at: 2026-01-24T14:13:24.455529108-03:00
rendered_js: false
word_count: 593
summary: This document outlines best practices and architectural patterns for building and optimizing cagent agents, covering context management, multi-agent coordination, and RAG efficiency.
tags:
    - cagent-patterns
    - agent-orchestration
    - rag-optimization
    - multi-agent-systems
    - context-management
    - docker-ai
category: guide
---

Patterns you learn from building and running cagent agents. These aren't features or configuration options - they're approaches that work well in practice.

Shell commands that produce large output can overflow your agent's context window. Validation tools, test suites, and build logs often generate thousands of lines. If you capture this output directly, it consumes all available context and the agent fails.

The solution: redirect output to a file, then read the file. The Read tool automatically truncates large files to 2000 lines, and your agent can navigate through it if needed.

**Don't do this:**

The validation output goes directly into context. If it's large, the agent fails with a context overflow error.

**Do this:**

The output goes to a file, not context. The agent reads what it needs using the filesystem toolset.

A single agent handling multiple responsibilities makes instructions complex and behavior unpredictable. Breaking work across specialized agents produces better results.

The coordinator pattern works well: a root agent understands the overall task and delegates to specialists. Each specialist focuses on one thing.

**Example: Documentation writing team**

Each agent has clear responsibilities. The writer doesn't worry about line wrapping. The editor doesn't generate content. The reviewer just runs tools.

This example uses `sub_agents` where root delegates discrete tasks and gets results back. The root agent maintains control and coordinates all work. For different coordination patterns where agents should transfer control to each other, see the `handoffs` mechanism in the [configuration reference](https://docs.docker.com/ai/cagent/reference/config/#task-delegation-versus-conversation-handoff).

**When to use teams:**

- Multiple distinct steps in your workflow
- Different skills required (writing ↔ editing ↔ testing)
- One step might need to retry based on later feedback

**When to use a single agent:**

- Simple, focused tasks
- All work happens in one step
- Adding coordination overhead doesn't help

RAG indexing takes time when you have many files. A configuration that indexes your entire codebase might take minutes to start. Optimize for what your agent actually needs.

**Narrow the scope:**

Don't index everything. Index what's relevant for the agent's work.

If your agent only works with API code, don't index tests, vendor directories, or generated files.

**Increase batching and concurrency:**

Process more chunks per API call and make parallel requests.

This reduces both API calls and indexing time.

**Consider BM25 for fast local search:**

If you need exact term matching (function names, error messages, identifiers), BM25 is fast and runs locally without API calls.

Combine with embeddings using hybrid retrieval when you need both semantic understanding and exact matching.

When building agents that update documentation, a common problem: the agent transforms minimal guides into tutorials. It adds prerequisites, troubleshooting, best practices, examples, and detailed explanations to everything.

These additions might individually be good, but they change the document's character. A focused 90-line how-to becomes a 200-line reference.

**Build this into instructions:**

Tell your agents explicitly to preserve the existing document's scope. Without this guidance, they default to being comprehensive.

Choose models based on the agent's role and complexity.

**Use larger models (Sonnet, GPT-5) for:**

- Complex reasoning and planning
- Writing and editing content
- Coordinating multiple agents
- Tasks requiring judgment and creativity

**Use smaller models (Haiku, GPT-5 Mini) for:**

- Running validation tools
- Simple structured tasks
- Reading logs and reporting errors
- High-volume, low-complexity work

Example from the documentation writing team:

The reviewer uses Haiku because it runs commands and checks for errors. No complex reasoning needed, and Haiku is faster and cheaper.

- Review [configuration reference](https://docs.docker.com/ai/cagent/reference/config/) for all available options
- Check [toolsets reference](https://docs.docker.com/ai/cagent/reference/toolsets/) to understand what tools agents can use
- See [example configurations](https://github.com/docker/cagent/tree/main/examples) for complete working agents
- Read the [RAG guide](https://docs.docker.com/ai/cagent/rag/) for detailed retrieval optimization