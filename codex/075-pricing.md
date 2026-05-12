---
number: 75
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/pricing.md
word_count: 273
---
# Pricing

> **BLUF:** Codex CLI and SDK are free during beta. ChatGPT (web/app) plans work with Codex for app/IDE. Pro and Pro+ users get full access. Enterprise and Edu tiers offer managed Codex plans. API usage billed separately via platform.openai.com.

## Codex Access by Plan

| Plan | Codex CLI | Codex App | Codex IDE | Notes |
|------|-----------|-----------|-----------|-------|
| **Free** | ✅ | ❌ | ❌ | Limited; see below |
| **Pro** | ✅ | ✅ | ✅ | Full access |
| **Pro+** | ✅ | ✅ | ✅ | Full access; priority |
| **Enterprise** | ✅ | ✅ | ✅ | Managed config available |
| **Edu** | ✅ | ✅ | ✅ | With institution license |

### Free Plan

- CLI access only
- Powered by `gpt-5.3-codex-spark` (OpenAI's code model)
- Cannot use Codex Cloud tasks (requires Pro+)
- Cannot use local OSS models (requires Pro)

## API Billing

Codex CLI and SDK call the OpenAI API directly. API usage is billed to your [platform.openai.com](https://platform.openai.com/api-keys) account.

| Component | Billing |
|-----------|--------|
| Model inference | Per-token (see [API pricing](https://openai.com/api/pricing/)) |
| Claude Max / Gemini Ultra | Respective provider billing |
| Data egress | Per provider |
| Custom providers | Per provider |

> 💡 Set usage limits on [platform.openai.com](https://platform.openai.com) to control spend.

## Enterprise & Managed

### Managed Configuration

Enterprise admins can push [managed configuration](https://developers.openai.com/codex/enterprise/managed-configuration) to deploy Codex with pre-configured policies.

### Custom Billing Arrangements

Contact your OpenAI account team for volume pricing, custom limits, or invoiced billing.

## Related

- [[016-cloud|Codex Cloud]]
- [[067-config-reference|Configuration Reference]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/pricing.md)*