---
title: Rate Limiting | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/rate_limiting
source: sitemap
fetched_at: 2026-04-26T04:14:31.458668369-03:00
rendered_js: false
word_count: 211
summary: This document explains how to implement and manage rate limiting for workflows, including how to configure shared limits across multiple activities using specific keys.
tags:
    - rate-limiting
    - workflow-management
    - task-queues
    - resource-control
    - distributed-systems
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Rate limiting is a crucial aspect of workflow management that helps control resource consumption and prevent any single workflow or activity from monopolizing shared resources.

Rate limits are always shared across all workers and workflows in the same task workspace (or `TEMPORAL_TASK_QUEUE` if configured). The `key` parameter controls how activities share these limits.

## Without Key

When **no key is provided**, the rate limit applies to the activity itself and is shared across all workers and workflows that use it.

**Use this when:** You want to protect a shared resource (like an API client) that should have a global rate limit regardless of which workflow is using it.

## With Key

When **a key is provided**, multiple different activities that use the same key share a single rate limit pool across all workers and workflows.

**Use this when:** You need to coordinate rate limits across multiple different activities (e.g., limiting total API calls across read, write, and delete operations using the same external service).

**Example behavior**: All workflows calling `generate_chat_response` share the same 100 executions/sec limit. If Workflow A makes 60 calls and Workflow B makes 50 calls in the same second, they compete for the same pool.

## Shared Limit Across Activities

**With a key**: Add `key="mistral_api"` to share this limit across multiple activities (e.g., `generate_chat_response`, `generate_embeddings`, `moderate_content`).