---
title: Billing | Enterprise | Warp
url: https://docs.warp.dev/enterprise/support-and-resources/billing
source: sitemap
fetched_at: 2026-04-29T15:06:08.744496736-03:00
rendered_js: false
word_count: 487
summary: This document outlines the credit-based billing model for enterprise teams, covering how credits are consumed, managed, and allocated across local and cloud agent usage.
tags:
    - enterprise-billing
    - credit-allocation
    - cloud-agents
    - byollm
    - spending-controls
    - usage-tracking
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Credits fuel Warp's billing model for enterprise teams, shared pool-wide with cloud and local usage drawing from the same source.

## Credits

Warp uses a credit-based billing model. Any interaction with Oz agents consumes credits based on task complexity, model used, and context processed.

### How credits work

- Each agent interaction consumes **at least one credit**; complex interactions may use multiple.
- Credit usage is influenced by LLM model, tool calls, task complexity, context amount, and prompt caching.
- Credit usage is **non-deterministic** — similar prompts may consume different credits.

For calculation details, see [[289-support-and-community-plans-and-billing-add-on-credits]].

### Credit allocation

Enterprise plans include a custom team-wide credit pool. Credits are primarily shared across the team rather than per seat. Individual credit grants (e.g., support refunds) may also occur.

> [!info]
> Credit allocations vary by contract. Contact your account manager for your team's specific allocation.

## Cloud agent billing

Oz cloud agents consume credits including a small hosting fee plus AI usage costs.

### How credits are consumed

Both local and cloud agent usage draw from the same team credit pool. No separate "cloud agent credits" or "local credits" exist — all agent usage consumes from your available pool.

For team API key runs (CI/CD, scheduled tasks), credits also draw from the team's shared pool since these runs aren't tied to any individual user.

See [[062-agent-platform-cloud-agents-team-access-billing-and-identity]] for details.

## BYOLLM billing

When using [Bring Your Own LLM (BYOLLM)](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm), Warp routes requests through your cloud infrastructure (AWS Bedrock, Google Vertex, or Azure Foundry). BYOLLM requests **consume credits at approximately 80% of standard rate**. Inference costs bill directly to your cloud account.

If a BYOLLM request fails and Warp falls back to a direct API model, that fallback consumes Warp credits at the standard rate.

## Managing billing

Your Warp account manager handles all billing for your Enterprise contract. Contact them or your dedicated Slack/Teams channel for:

- Invoices and payment changes
- Contract modifications
- Credit allocation adjustments

For urgent billing issues, email [billing@warp.dev](mailto:billing@warp.dev).

### Spending controls

Administrators configure monthly spending limits and receive alerts to prevent unexpected charges. Configure in the [Admin Panel](https://app.warp.dev/admin/) under **Billing**.

#### Monthly spending limits

Set caps across three categories:

| Category | Description |
|----------|-------------|
| Cloud spending limit | Cap monthly spend on Oz cloud agent usage |
| Local spending limit | Cap monthly spend on local agent usage in Warp app |
| Total spending limit | Cap combined monthly spend across both |

Spending is tracked across all payment types (Add-on Credits, pay-as-you-go) so limits apply consistently.

#### Monthly spend alerts

Warp sends alerts as team usage approaches configured spending limits, allowing cap adjustments, credit purchases, or team communication before blocking.

#### Credit pool depletion alerts

For enterprises with credit pools, administrators receive alerts as the team pool approaches full consumption, enabling top-ups before agent usage is interrupted.

## Related

- [[189-enterprise-team-management-admin-panel]] - Configure spending limits and billing settings
