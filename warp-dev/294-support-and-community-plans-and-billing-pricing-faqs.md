---
title: Pricing FAQs | Support & Community | Warp
url: https://docs.warp.dev/support-and-community/plans-and-billing/pricing-faqs
source: sitemap
fetched_at: 2026-04-29T15:05:51.382987765-03:00
rendered_js: false
word_count: 2129
summary: Guide to Warp pricing plans, billing cycles, team management, credits, and upgrades.
tags:
    - billing
    - subscription-plans
    - team-management
    - warp-account
    - credits
    - pricing
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## How can I upgrade and subscribe to a Warp plan?

Paid plans include higher monthly credit limits than Free. When upgrading from Free to paid, credit usage resets. Switching between paid plans carries over accumulated AI usage.

**To upgrade:** Go to **Settings** > **Billing and usage** > click Upgrade. After payment, you'll receive an invoice and email confirmation.

## How can I get the most out of my Warp plan?

> [!warning]
> Warp's legacy plans (Pro, Turbo, Lightspeed) are being replaced. After **Oct 30, 2025**, legacy plans roll over to the new Build plan starting **Dec 1, 2025**.

| Plan | Description |
|------|-------------|
| **Build** | Usage-based with included credits, Bring Your Own API Key (BYOK), and Add-on Credits with volume discounts |
| **Business** | Build features plus team-wide Zero Data Retention, SAML SSO, up to 50 seats |

Legacy plans (until Dec 1, 2025):

| Plan | Description |
|------|-------------|
| **Pro** | Higher credit limits, codebase support, premium models with optional overages |
| **Turbo** | Higher limits, larger codebase indexing, optional pay-as-you-go overages |
| **Lightspeed** | Highest limits, expanded indexing, top-tier models, pay-as-you-go overages |

For current pricing, visit [warp.dev/pricing](https://www.warp.dev/pricing).

## How can I subscribe to a Warp Enterprise plan?

| Option | Description |
|--------|-------------|
| **Business Plan** | Up to 50 seats, team-wide Zero Data Retention, admin-controlled SAML SSO |
| **Enterprise Plan** | Custom pricing/limits/terms, larger orgs, advanced security/compliance/support |

## What counts as a team member and how does billing work?

A *team member* is any seat with access to shared Warp Drive, Notebooks, Workflows, and team resources. All plans allow unlimited user invites, but upgrading unlocks higher limits and advanced features.

> [!warning]
> All team members share the same subscription plan. Different plans require separate teams.

**Billing is prorated:**
- **Monthly plans**: New members billed immediately for remaining days in the month
- **Annual plans**: New members billed immediately for remaining days in the year

**Example:** Member joins halfway through a monthly billing cycle ($50/month) → charged $25. If a member leaves mid-cycle, a prorated credit is applied to the next invoice.

## What is the value of joining or creating a team?

Team members access shared [[144-knowledge-and-collaboration-warp-drive.md|Warp Drive]] objects and collaboration features including Session Sharing and Warp Drive storage. Upgrading to a paid plan unlocks team-wide tools for collaboration and knowledge sharing.

## My co-workers use Warp but we're not on a team yet. How does billing work?

Individual users continue independently without billing. When ready to collaborate, an Admin can [create a Team](https://docs.warp.dev/knowledge-and-collaboration/teams) and invite members. When Warp Drive limits are exceeded, upgrade to a plan.

## How does usage work if logged into the same account on multiple devices?

Metered features like credits are tracked at the **account level**, not device level. Settings and preferences sync across devices via [Settings Sync](https://docs.warp.dev/terminal/more-features/settings-sync).

## What happens when I downgrade during a billing cycle?

The subscription downgrades at the **end of the billing cycle**. Accumulated AI usage carries over. Downgrade via **Settings** > **Billing and usage** > **Manage billing**.

## What happens when I cancel during a billing cycle?

The subscription remains active until the **end of the billing cycle**. You can continue using paid features until the cycle end date. Additional team members are invoiced at the end of the billing cycle.

## What happens if I upgrade from monthly to annual billing?

Billing is prorated — you only pay for the unused portion of the year at the discounted annual rate. Upgrade via **Settings** > **Billing and usage** > **Manage billing**.

## What happens to unused credits?

Unused credits **do not rollover** to the next cycle and cannot be transferred. View reset timing in **Settings** > **Billing and usage**.

## What happens if my payment fails?

You'll receive an email from Stripe and your Team Settings will show a past-due alert. Paid features and ability to invite members are locked while past-due. Pay the invoice via **Settings** > **Billing and usage** > **Manage billing** to re-enable features.

## What counts as a credit?

Each prompt submitted to the Agent initiates an AI interaction. See [[291-support-and-community-plans-and-billing-credits.md|Credits]] for details.

## What counts as an AI token?

Tokens are text chunks (words, code parts, characters) that LLMs process. Warp abstracts token usage — you monitor **credit usage** against plan limits.

> [!info]
> Warp abstracts token usage. Monitor your **credit usage** against plan limits. If you reach credit limits on a paid plan, premium models are temporarily disabled until quota resets.

If you reach monthly limits, purchase [Add-on Credits](https://docs.warp.dev/support-and-community/plans-and-billing/add-on-credits) or enable [BYOK](https://docs.warp.dev/support-and-community/plans-and-billing/bring-your-own-api-key). Legacy plan users continue using [Overages (Legacy)](https://docs.warp.dev/support-and-community/plans-and-billing/overages-legacy) until first renewal after Dec 1, 2025.

## How often do my credits reset?

Credits refill every **30 days** from signup date. Upgrade to a [paid plan](https://www.warp.dev/pricing) for immediate additional credits. Follow refill period in **Settings** > **Billing and usage** or purchase [Add-on Credits](https://docs.warp.dev/support-and-community/plans-and-billing/add-on-credits).

> [!info]
> Unused credits do not rollover to the next cycle and cannot be transferred to other accounts.

## Can I use a Free plan if I'm a developer at a large company?

Yes. Developers at any company size can use Warp's Free plan. Upgrade only if you need advanced collaboration features or higher limits.

## Are there any Warp discounts for students, non-profits, or open-source teams?

No current discounts for students or non-profits. Free plan includes all core terminal features.

For open source teams:
- [GitHub Open Source Program](https://github.com/warpdotdev/gitbook/blob/main/docs/README.md#community) — free Warp for qualifying open source projects
- [Open Source Initiative](https://www.warp.dev/open-source) — contact Warp for team discounts

## Where is Warp Drive data for my team stored?

Warp Drive data is stored on **Google Cloud Platform servers in the United States**, encrypted in transit and at rest. See [Security Overview](https://www.warp.dev/legal/security) or contact [security@warp.dev](mailto:security@warp.dev).

## What happened to the Lite model?

The Lite model was delivering inconsistent results for complex prompts. Warp recommends the new **Auto (cost-efficiency) model**, which automatically selects the optimal model based on task complexity.

To continue AI usage: add [Add-on Credits](https://docs.warp.dev/support-and-community/plans-and-billing/add-on-credits) or [use your own API key](https://docs.warp.dev/support-and-community/plans-and-billing/bring-your-own-api-key).

## What payment options are available?

Warp uses **Stripe** and accepts:
- Credit card, debit card
- Link
- Apple Pay (Safari on Apple device)
- Google Pay (Chrome with Google Wallet and "Save and fill payment methods" enabled)

> [!info]
> ACH, checks, PayPal, cryptocurrency, and alternative payment methods are not supported.

## How do I cancel my subscription?

Cancel via **Settings** > **Billing and usage** > **Manage billing**. The subscription remains active until the end of the billing cycle.

## How do I get a refund?

| Plan Type | Refund Policy |
|-----------|---------------|
| Monthly | Full refund if canceled within **24 hours** of charge and no credits used |
| Annual | Full refund within **15 days** if no credits used, or prorated refund for remaining months |

See [Refund Policy](https://docs.warp.dev/support-and-community/plans-and-billing/plans-pricing-refunds#warps-refund-policies) for full details.

## Why doesn't my promo code work or why was it disabled?

Promo codes are for trying Warp, not unlimited free AI. Restrictions:
- One promo code per account
- Some codes valid for specific plans only
- Codes expire after a certain time
- Promotions don't transfer to upgraded plans

> [!warning]
> Warp reserves the right to disable promotion codes and cancel associated subscriptions if abused.

## How can I subscribe to Warp as tax exempt?

1. Create account, login, go to [upgrade page](https://app.warp.dev/upgrade), select a plan — **don't checkout yet**
2. Email [billing@warp.dev](mailto:billing@warp.dev) with tax exempt proof and Warp account email
3. Warp verifies status and sets account to tax exempt
4. Subscribe to your plan — no taxes applied

## Why can't I subscribe to Warp?

Stripe and credit card networks restrict certain businesses. See [Stripe Restricted Businesses](https://stripe.com/legal/restricted-businesses).

## I have a question and need help. How can I reach a human at Warp?

Email [billing@warp.dev](mailto:billing@warp.dev) for plan or subscription questions.

---

## Warp's pricing change FAQs (Oct 30, 2025)

For details, see [Warp's plan changes blog post](https://www.warp.dev/blog/warp-new-pricing-flexibility-byok).

### How do I change from my current plan to the new Build or Business plan?

Switch anytime via **Settings** > **Billing and usage** > **Manage billing** > **Update subscription** or [app.warp.dev/upgrade](https://app.warp.dev/upgrade).

If you take no action, legacy plans auto-transition on first renewal after **December 1, 2025**.

### What happens when I change from my legacy plan to the new plans?

- **Prorated Stripe credit** for unused portion of current billing cycle
- Credit balance applies toward monthly Build fees or Add-on Credits
- **Credit balance resets to 0/1,500** when switching to Build or Business

> [!info]
> Use all credits on your legacy plan before switching. This way you can make best use of them before they reset.

> [!warning]
> Add-on credit auto reload is enabled by default for some legacy plan users transitioning to Build.

### What should I keep in mind about this change?

- **BYOK and Add-on credits**: Only available on new Build and Business plans
- **Pricing differences**: Monthly cost may increase or decrease based on usage
- **Renewal timing**: Stay on current plan until renewal after December 1
- **Transparency**: View credit balance, monthly spend, and Add-on settings in **Settings** > **Billing and usage**

### For existing paid users: when will the new pricing take effect?

| User Type | Effective Date |
|-----------|----------------|
| New customers | Immediately (Oct 30, 2025) |
| Monthly subscribers | First renewal after Dec 1, 2025 |
| Annual subscribers | Next renewal after Dec 1, 2025 |

### What happens to my current plan (Pro, Turbo, Lightspeed, Business)?

Legacy plans retain current plan and credits until first renewal after Dec 1, 2025, then transition to Build or Business.

**Auto-reload defaults by plan:**

| Plan | Transitions To | Auto-reload Enabled | Default Monthly Limit |
|------|----------------|---------------------|----------------------|
| Pro | Build | No | — |
| Turbo | Build | Yes | $30/month (monthly) / $22 (yearly) |
| Lightspeed | Build | Yes | $205/month (monthly) / $182 (yearly) |
| Business | Business | Yes | $10/month |

For Turbo subscribers with team bulk discounts: check email for specific default limits.

**Auto-reload denomination defaults:**
- Total spend limit ≥ $80 → $20 / 1,000 credits
- Total spend limit < $80 → $10 / 400 credits

### Can I continue to use Warp as my primary terminal?

Yes, terminal features are **free to use**. See [[293-support-and-community-plans-and-billing-plans-pricing-refunds.md|Plans and Pricing]].

### How are Add-on credits different from overages?

| Feature | Add-on Credits | Legacy Overages |
|---------|----------------|----------------|
| Cost | Up to ~40% cheaper | Higher rates |
| Rollover | Month-to-month, valid 12 months | No rollover |
| Protection | SOC 2 / Zero Data Retention | Not included |

### Do credits rollover?

- **Legacy plans (Pro, Turbo, Lightspeed)**: Plan credits do not rollover
- **Build plan**: Credits do not rollover, but Add-on credits rollover and stay valid 12 months

### Can I purchase Add-on Credits on legacy plans?

No. Add-on Credits are only available on Build, Business, and Enterprise plans. Legacy plan users can use [Overages (Legacy)](https://docs.warp.dev/support-and-community/plans-and-billing/overages-legacy) until first renewal after Dec 1, 2025.

### Can I bring my own key on legacy plans?

No. BYOK for OpenAI, Anthropic, and Gemini is only available on the **Build plan**.

### How does the monthly spend limit on Add-on Credits work?

You set a monthly spend limit for AI usage. If a purchase would exceed your limit, it won't go through.

**Auto reload defaults:**
- New users: $200 spend limit
- Existing paid users: Matches existing Overages spend limit (or $200 if not configured)

### I'm an individual developer and need more than 1,500 credits per month. What's the right plan for me?

**Build plan** is designed for you. It includes 1,500 monthly credits plus:
- Add-on Credits with rollover and 12-month validity
- Up to ~40% savings for larger denominations
- Auto reload to automatically top up when balance runs low
- BYOK for OpenAI, Anthropic, or Google models

For team shared credit management, SSO, or enforced Zero Data Retention, choose **Business plan**.

### Should I subscribe to the Build plan or the Business plan?

| Plan | Best For |
|------|----------|
| **Build** | Individual developers or small teams needing AI credits, BYOK, and Add-on Credits |
| **Business** | Teams up to 50 members needing SSO, enforced ZDR, shared Add-on Credits, and centralized billing |

### How do credits work for multi-seat teams?

| Credit Type | Description |
|-------------|-------------|
| **Included monthly credits** | Each seat receives 1,500 credits/month, tied to user, resets every 30 days |
| **Add-on Credits** | Shared team balance when individual credits are used up, managed by team admins |

This shared model gives teams flexibility to handle variable AI usage with volume-based discounts.
