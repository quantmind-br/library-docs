---
title: Coding agent suite tests
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/test/suite/README.md
source: git
fetched_at: 2026-05-03T09:32:16.403367714-03:00
rendered_js: false
word_count: 94
summary: Harness-based test suite for AgentSession and AgentSessionRuntime using faux provider.
tags:
    - testing-guidelines
    - test-harness
    - agent-development
    - quality-assurance
    - regression-testing
    - ci-testing
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Coding agent suite tests

Use `test/suite/` for harness-based tests around `AgentSession` and `AgentSessionRuntime`.

## Rules

- Use `test/suite/harness.ts`
- Use the faux provider from `packages/ai/src/providers/faux.ts`
- **Do not use**: real provider APIs, real API keys, network calls, or paid tokens
- Keep tests CI-safe and deterministic
- Do not extend legacy `test/test-harness.ts` unless a missing capability forces it

## Organization

| Location | Purpose |
|----------|---------|
| `test/suite/` | Broad lifecycle and characterization tests |
| `test/suite/regressions/` | Issue-specific regression tests |

## Regression Test Naming

Format: `<issue-number>-<short-slug>.test.ts`

Example: `test/suite/regressions/2023-queued-slash-command-followup.test.ts`

#testing-guidelines #test-harness #regression-testing
