---
title: Bring Your Own API Key | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/plans-and-billing/bring-your-own-api-key
source: sitemap
fetched_at: 2026-04-29T15:05:48.456700011-03:00
rendered_js: false
word_count: 591
summary: This document explains how to configure and use the Bring Your Own Key (BYOK) feature in Warp, allowing users to route agent requests through their own API providers.
tags:
    - byok
    - api-keys
    - billing
    - model-selection
    - data-privacy
    - configuration
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
BYOK lets you connect your own Anthropic, OpenAI, or Google API keys for full control over model selection, billing, and data routing — Warp never consumes your credits for BYOK requests.

> [!info]
> BYOK is available on paid plans (Build and above). Learn more at [warp.dev/pricing](https://www.warp.dev/pricing).

## How BYOK works

When you add your own model API keys in Warp, those keys are stored **locally on your device** and are **never synced to the cloud**.

Warp uses these API keys to directly route your agent requests to your configured model provider.

> [!warning]
> BYOK does not apply to [Oz Cloud Agents](https://docs.warp.dev/agent-platform/cloud-agents/overview). Because API keys are stored locally, they are not available to cloud-hosted agent runs. Cloud agent runs always consume [Warp credits](https://docs.warp.dev/support-and-community/plans-and-billing/credits).

When a model is selected using your own key:
- Warp **does not consume** any of your credits
- Costs billed directly through your model provider account
- Warp does not retain or store your API key on any servers

## Enabling BYOK

1. Open **Settings** and search for `API keys` to jump to the BYOK configuration.
2. Add your API key(s) for Anthropic, OpenAI, or Google.
3. Once added, you'll see a **key icon** next to supported models in the model picker.

When you explicitly select a model with a key icon, Warp routes requests through your own API key instead of consuming Warp's credits.

## BYOK usage and billing behavior

### Auto Model

Warp's **Auto** models dynamically route requests across different models based on context and performance. Because this routing depends on Warp's infrastructure, **Auto always consumes Warp's credits**, even with configured API keys.

To use your own key, select a specific provider model directly from the model picker with a key icon.

### Credit usage

When selecting a model with the key icon:
- No Warp credits are consumed
- Cost billed directly through your provider account
- Core Agent Mode always **prioritizes BYOK usage** over available credits

The credit transparency footer shows "0 credits used" and the `Billing & Usage` page reflects no deductions.

**Other AI features in Warp** are not affected by BYOK and function normally as part of Warp's paid plans.

### Failover and fallback behavior

| Scenario | Behavior |
|----------|----------|
| Invalid key | Warp notifies you and halts the request |
| Usage/rate limits | Warp will not retry using credits |
| API error or quota limit | Optional Warp credit fallback can be enabled |

**Warp credit fallback** (optional): If enabled, failed BYOK requests automatically route to Warp-provided models. Warp always prioritizes your API keys first.

Update or replace keys anytime via **Settings** searching for `API keys`.

## Zero Data Retention (ZDR) and BYOK

Warp is **SOC 2 compliant** with **Zero Data Retention (ZDR)** policies with contracted LLM providers. However, when using your own API key:

- Data retention depends on your provider's account settings
- Warp cannot enforce ZDR for requests sent through your API keys
- If your provider account doesn't have ZDR enabled, requests may be retained per their terms

Warp itself never stores your LLM API keys.

## BYOK on Enterprise and Business plans

Currently, BYOK is configured at the **user level**, not team/admin level:

- Each team member manages their own API keys locally
- Team admins cannot enforce or share API keys across members
- No organization-level Admin Panel for BYOK yet

For enterprise key management needs, contact [warp.dev/contact-sales](https://warp.dev/contact-sales).

## Related

- [[039-agent-platform-warp-agents-capabilities-overview-model-choice]] - Supported models for BYOK
- [[289-support-and-community-plans-and-billing-add-on-credits]] - Add-on credits system
- [[232-enterprise-enterprise-features-bring-your-own-llm]] - Enterprise BYOLLM option
