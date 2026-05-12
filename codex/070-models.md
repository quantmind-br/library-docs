---
number: 70
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/models.md
word_count: 323
---
# Codex Models

> **BLUF:** Codex supports frontier models for coding tasks. `gpt-5.5` (ChatGPT auth only) is best for complex work. `gpt-5.4` and `gpt-5.4-mini` offer strong coding with API access. `gpt-5.3-codex` powers cloud tasks. Configure via `config.toml` or `--model` flag.

## Recommended Models

| Model | Capability | Speed | CLI/SDK | App/IDE | Cloud | ChatGPT Credits | API |
|-------|-----------|-------|---------|---------|-------|-----------------|-----|
| **gpt-5.5** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | ❌ | ✅ | ❌ |
| **gpt-5.4** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **gpt-5.4-mini** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **gpt-5.3-codex** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **gpt-5.3-codex-spark** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ✅ | ❌ | ❌ (Pro only) | ❌ |

### Model Selection Guide

| Use Case | Recommended Model |
|----------|-------------------|
| Complex coding, computer use, research | `gpt-5.5` |
| General professional coding | `gpt-5.4` |
| Fast, lightweight tasks, subagents | `gpt-5.4-mini` |
| Cloud tasks, code review | `gpt-5.3-codex` |
| Real-time iteration (Pro users) | `gpt-5.3-codex-spark` |

> 💡 `gpt-5.5` is ChatGPT-auth only during rollout. If unavailable, use `gpt-5.4`.

## Alternative Models

| Model | Capability | Speed | CLI/SDK | App/IDE | Cloud | ChatGPT Credits | API |
|-------|-----------|-------|---------|---------|-------|-----------------|-----|
| **gpt-5.2** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | ❌ | ✅ | ✅ |

## Other Models

Any model supporting [Chat Completions](https://platform.openai.com/docs/api-reference/chat) or [Responses APIs](https://platform.openai.com/docs/api-reference/responses) works with Codex.

> ⚠️ Chat Completions API support is deprecated and will be removed in future releases.

## Configuration

### Default Model

```toml
# ~/.codex/config.toml
model = "gpt-5.5"
```

### Temporary Override

```bash
# CLI
codex -m gpt-5.5

# Active thread
/model gpt-5.4
```

### IDE Extension

Use model selector below input box.

### Cloud Tasks

Model selection is not currently configurable for Codex Cloud tasks.

## Related

- [[015-cli|Codex CLI]]
- [[067-config-reference|Configuration Reference]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/models.md)*
