---
title: Agent FAQs | Agents | Warp
url: https://docs.warp.dev/agent-platform/getting-started/faqs
source: sitemap
fetched_at: 2026-04-29T15:03:43.749433766-03:00
rendered_js: false
word_count: 454
summary: This document provides an overview of Warp's AI Agent features, including data privacy, billing policies, model selection, and troubleshooting common error messages.
tags:
    - warp-terminal
    - ai-agents
    - data-privacy
    - billing-credits
    - api-configuration
    - troubleshooting
    - llm-models
category: reference
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
## General

### What data is sent and/or stored when using Agents in Warp?

Warp sends data to model providers (Anthropic, OpenAI, Google) for inference. Only embeddings are stored on Warp's servers during codebase indexing—your source code is not persisted. See the [[299-support-and-community-privacy-security-and-licensing-privacy|Privacy Page]] for full details.

### What happened to the old Warp AI chat panel?

Agent Mode has replaced the previous AI chat panel. Agent Mode runs commands, gathers context automatically, and is more powerful in all use cases. To start a similar chat, click the AI button in the menu bar.

### Is my data used for model training?

Warp reserves the right to use data to train models and improve Warp. Zero Data Retention applies with all model providers. Telemetry details are on the [[297-support-and-community-privacy-security-and-licensing-privacy|Privacy Page]].

### What model are you using for Agent Mode?

Warp supports curated LLMs from OpenAI, Anthropic, and Gemini. See [[039-agent-platform-warp-agents-capabilities-overview-model-choice|Model Choice]] for the full list and switching instructions.

### Can I use my own LLM API key?

Yes. Bring Your Own Key (BYOK) is available on paid plans (Build tier and above). Connect Anthropic, OpenAI, or Google API keys. Enterprise teams can also enable managed BYOLLM configurations. See [[290-support-and-community-plans-and-billing-bring-your-own-api-key|Bring Your Own API Key]].

## Billing

Every Warp plan includes credits per user per month. Credit limits apply to Agent Mode, Generate (Legacy), and AI autofill in Workflows.

| Question | Answer |
|---|---|
| What counts as a credit? | Usage during AI-assisted sessions |
| How often do credits refresh? | Start of each billing cycle |
| More details? | See [[291-support-and-community-plans-and-billing-credits|Credits]] and [[293-support-and-community-plans-and-billing-plans-pricing-refunds|Plans & Pricing]] |

## Common AI error messages

### "Message token limit exceeded" error

Your input (plus attached context) exceeds the model's context window. Fix it by:

- Starting a new conversation
- Reducing the number of blocks or lines attached to your query

### "Monthly request limit exceeded" or "Monthly credit limit exceeded" errors

Once you exceed your monthly credit limit, premium models are disabled until quota resets. Paid plans with Add-on Credits continue with usage-based billing.

### "Request failed with error: QuotaLimit"

All models are disabled after exceeding AI token limits. Credits and tokens are calculated separately—even with set credit amounts, tokens have separate limits.

### "Request failed with error: ErrorStatus (403, "Your account has been blocked from using AI features")"

Your account was blocked due to a violation of [Terms of Service](https://www.warp.dev/terms-of-service) or suspected abuse (e.g., bypassing credit/token limits).

> [!tip]
> To appeal: email [appeals@warp.dev](mailto:appeals@warp.dev). Any error not mentioning this address should be reported as feedback or a bug. See [[sending-us-feedback|Feedback]].

## Gathering AI debugging ID

When troubleshooting, you may need the AI debugging ID for the specific conversation. See [[sending-us-feedback#gathering-ai-debugging-id|Gathering AI Debugging ID]].