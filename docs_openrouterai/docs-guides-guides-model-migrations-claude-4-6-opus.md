---
title: Claude 4.6 Opus Migration Guide
url: https://openrouter.ai/docs/guides/guides/model-migrations/claude-4-6-opus.mdx
source: llms
fetched_at: 2026-02-13T15:15:31.201248-03:00
rendered_js: false
word_count: 411
summary: This guide explains the migration process to Claude 4.6 Opus, focusing on the introduction of adaptive thinking and new response effort configurations. It outlines how these changes affect API parameters for reasoning and verbosity compared to previous model versions.
tags:
    - claude-4-6-opus
    - model-migration
    - adaptive-thinking
    - openrouter
    - api-configuration
    - ai-models
category: guide
---

***

title: Claude 4.6 Opus Migration Guide
subtitle: Migrate to Claude 4.6 Opus with adaptive thinking and max effort level
headline: Claude 4.6 Opus Migration Guide | OpenRouter
canonical-url: '[https://openrouter.ai/docs/guides/guides/model-migrations/opus-4-6](https://openrouter.ai/docs/guides/guides/model-migrations/opus-4-6)'
'og:site\_name': OpenRouter Documentation
'og:title': Claude 4.6 Opus Migration Guide
'og:description': Learn about adaptive thinking and the new max effort level in Claude 4.6 Opus.
'og:image':
type: url
value: >-
[https://openrouter.ai/dynamic-og?title=Claude%204.6%20Opus%20Migration%20Guide\&description=Adaptive%20thinking%20and%20max%20effort%20level](https://openrouter.ai/dynamic-og?title=Claude%204.6%20Opus%20Migration%20Guide\&description=Adaptive%20thinking%20and%20max%20effort%20level)
'og:image:width': 1200
'og:image:height': 630
'twitter:card': summary\_large\_image
'twitter:site': '@OpenRouterAI'
noindex: false
nofollow: false
---------------

## What's New

See Anthropic's [What's new in Claude 4.6](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6) for a full overview of new features.

Claude 4.6 Opus introduces two major changes to reasoning:

1. **Adaptive Thinking** — Claude decides how much to think based on task complexity, replacing budget-based extended thinking
2. **Max Effort Level** — A new `'max'` effort level above `'high'` (Opus 4.6 only)

## Adaptive Thinking

For Claude 4.6 Opus, OpenRouter now uses adaptive thinking (`thinking.type: 'adaptive'`) by default instead of budget-based thinking (`thinking.type: 'enabled'` with `budget_tokens`).

### How it works

* When you enable reasoning without specifying `reasoning.max_tokens`, Claude 4.6 Opus uses adaptive thinking
* Claude automatically determines the appropriate amount of reasoning based on task complexity
* You don't need to estimate or tune token budgets

### When budget-based thinking is still used

* If you explicitly set `reasoning.max_tokens`, budget-based thinking is used
* If you pass the raw Anthropic `thinking` parameter directly

```json
// Adaptive thinking (recommended for 4.6)
{
  "model": "anthropic/claude-4.6-opus",
  "reasoning": { "enabled": true }
}
```

```json
// Budget-based thinking (still supported)
{
  "model": "anthropic/claude-4.6-opus",
  "reasoning": { "enabled": true, "max_tokens": 10000 }
}
```

## Max Effort Level

A new `'max'` effort level is available for Claude 4.6 Opus via the `verbosity` parameter. See Anthropic's [effort documentation](https://platform.claude.com/docs/en/build-with-claude/effort) for details on how effort controls response thoroughness and token usage.

```json
{
  "model": "anthropic/claude-4.6-opus",
  "verbosity": "max"
}
```

<Note>
  `'max'` is only supported on Claude 4.6 Opus. For other models, it automatically falls back to `'high'`.
</Note>

## Verbosity vs Reasoning Effort

These are separate parameters:

| Parameter          | Controls                                 | 4.6 Behavior                             |
| ------------------ | ---------------------------------------- | ---------------------------------------- |
| `verbosity`        | Response detail (`output_config.effort`) | Works normally, supports `'max'`         |
| `reasoning.effort` | Thinking token budget                    | Ignored (adaptive thinking used instead) |

```json
// verbosity works - controls response detail
{ "model": "anthropic/claude-4.6-opus", "verbosity": "max" }
```

```json
// reasoning.effort ignored - still uses adaptive
{ "model": "anthropic/claude-4.6-opus", "reasoning": { "enabled": true, "effort": "low" } }
```

## Breaking Changes

None. Existing requests continue to work:

* Budget-based thinking still works when `reasoning.max_tokens` is set
* `reasoning.effort` values (low, medium, high) are still supported for older models, but will be ignored for Opus 4.6. Use `reasoning.max_tokens` to control Anthropic's `thinking.budget_tokens`, and `verbosity` to control Anthropic's `output_config.effort`.
* Older models (4.5 Opus, 3.7 Sonnet, etc.) behave exactly as before

| Feature                | Opus 4.5             | Opus 4.6     |
| ---------------------- | -------------------- | ------------ |
| Default Thinking Mode  | Budget-based         | Adaptive     |
| `reasoning.max_tokens` | Budget-based         | Budget-based |
| `verbosity: 'max'`     | Falls back to `high` | Supported    |