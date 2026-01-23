---
title: Pricing & Plans - Zencoder Docs
url: https://docs.zencoder.ai/faq/plans
source: crawler
fetched_at: 2026-01-23T09:28:01.712524743-03:00
rendered_js: false
word_count: 2018
summary: This document outlines Zencoder's subscription plans, the Premium LLM Call pricing model, and daily usage limits. It explains how to monitor consumption and provides strategies for optimizing AI resource usage.
tags:
    - zencoder-pricing
    - subscription-plans
    - llm-calls
    - usage-limits
    - billing-model
    - account-management
category: guide
---

## Plans & Pricing Basics

Which plans are available and who are they for?

PlanPrice (per user/month)Premium LLM Call Limits per dayIdeal For**Free****$0****30**Exploring Zencoder, no commitment**Starter****$19****280**Light individual usage & side projects**Core****$49****750**Professional devs, small to mid teams**Advanced****$119****1900**AI-first orgs, power users, heavy automation**Max****$250****4200**Enterprises, high-performing teams, mission-critical development

The Free plan provides essential tools to get started. Starter includes a 7-day free trial. Core, Advanced, and Max plans include enterprise features like [Multi-Repo Indexing](https://docs.zencoder.ai/features/multi-repo), SSO and audit logs. The Max plan additionally includes priority support and SLA-backed reliability.

What are Premium LLM Calls, and why do we price this way?

A “Premium LLM Call” occurs each time the Agent interacts with the LLM (Large Language Model) while resolving your task. For example, if an Agent must use 5 different tools before giving you a final response, this process will consume a total of 6 Premium Calls: 5 for each tool interaction, plus 1 for the final response itself.This allows for fair pricing for complex tasks. Consider these two requests:

- “Change label heading to Zencoder”
- “Pull JIRA ticket DVL-0522, fix the bug, prepare PR, push to GitHub, and ping me on Slack when done”

In both cases, it’s one user message, but the latter would require more tool calls, and in general, assumes a more intelligent agent capable of following more complex instructions. The same logic applies to a simple edit vs a more complex one.**Why this pricing model?**

- **Transparency**: You can see exactly how many LLM calls each task requires
- **Control**: Optimize your agent instructions to be more efficient when needed
- **Quality**: Our success is directly tied to delivering the most effective AI assistance possible, not cutting corners

We will soon be offering a selection of Faster models (like Gemini Flash), which will consume a fraction of Premium LLM calls, and Advanced models (like Opus 4), which will consume multiple Premium LLM Calls, allowing you to further control the balance between quality and costs.**Why not price per token?** While token-based pricing would be simpler for us (pure pass-through), we chose LLM calls because they’re easier for you to understand and manage. You can visually track tool usage and develop an intuition for which tasks require more calls.

Core plan specifics—what are my limits?

- **1,100 Premium LLM Calls** per user per 24h (resets 24h after the first agentic request on a given period)
- **Seat-based**: each paid seat gets its own call bucket; buckets aren’t shared or pooled

What's the difference between Auto and Auto+ models?

- **Auto Model**: Robust and cost-effective option that uses 1x of your daily calls
- **Auto+ Model**: Our best-in-class agentic coding model that uses 2.5x calls but delivers superior performance for complex tasks

For more information on available models, see the [Models page](https://docs.zencoder.ai/features/models).

## Usage & Limits

How can I monitor my usage?

You can monitor your usage in two ways:**1) Real-time tracking after each message**After every agent usage, at the bottom of the message you can see how many premium LLM calls were consumed by the response, as well as how many are remaining for today and when the limit will be reset. The cost multiplier of the model used is also displayed.![Usage tracking shown after each agent message](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/post-message-usage.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=fc059a8df66c429123ee75364015b93b)**2) Daily limit dashboard**You can view your daily limit usage by going to your user account at [](https://auth.zencoder.ai)[https://auth.zencoder.ai](https://auth.zencoder.ai). Once logged in, navigate to the User Profile page where you’ll find a “Limits” tab. You can also access it directly as [View your usage dashboard](https://auth.zencoder.ai/profile?tab=usage).

The daily usage limits dashboard in the auth.zencoder.ai portal is only available to users on the new plans (those who upgraded on June 19, 2025, or later). Users on legacy plans will not be able to see these usage metrics.

![Limits tab in user profile showing daily usage](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/limits-tab-placeholder.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=f64e511b06ce5137ea198b019443c451)

Does Code Completion burn Premium LLM Calls?

No. Basic autocomplete is currently unlimited across all plans. Only agent-driven tasks (chat, refactor, multi-file edits, etc.) count toward the daily Premium LLM Call total.

What happens when I reach the daily rate limit on Premium LLM Calls?

If you reach your daily Premium Call limit, you’ll need to wait until the next day for your limits to reset or upgrade to a plan with higher limits. For users who frequently rely on AI, we recommend upgrading to a plan better suited to your daily usage needs, or consider using our “Bring Your Own Key” option to remove daily usage limits altogether.

Why does Zencoder have daily limits vs monthly limits like other vendors?

Daily limits ensure you have consistent AI assistance every day of the month, not just the first week. With monthly limits, developers often burn through their entire allocation early in the sprint cycle, leaving them without access during critical deadlines.Daily limits also prevent high overage bills and make budget forecasting more predictable for teams. Additionally, we’ve built a buffer into our plans to accommodate usage spikes within the daily structure.

If I have unused limits for the day, do they roll over?

No, unused Premium LLM calls do not roll over to the next day. Each day you get a fresh allocation of your plan’s daily limits. This design ensures:

- **Consistent daily access**: You’re guaranteed your full allocation every day
- **Predictable usage patterns**: Teams can plan their AI usage around daily cycles
- **Fair resource distribution**: Prevents users from hoarding calls and ensures everyone gets consistent access
- **Simplified billing**: No complex rollover calculations or expiration tracking

Your daily limits reset 24 hours after your first agentic request of the current period, giving you a clean slate to work with fresh resources each day.

How could I optimize my AI use?

Here are tips to help you use AI more efficiently and avoid hitting daily limits prematurely:

- **Choose the right model**: Use Auto for regular tasks, Auto+ for complex challenges
- **Use separate chats for different topics**: Agent might get confused by long chat history, causing quality issues and a need to use more tools to answer
- **Use Basic Chat Agent for simple queries**: For questions that don’t require a lot of code to be generated, and extensive codebase research (for example, quick questions about current file, or general software development knowledge questions) it’s better to use Basic Chat Agent which is faster and more cost-effective
- **Use custom agents for repetitive tasks**: Custom agents allow to specify custom prompts and tools to be reused, thus eliminating the need for agents to spend tool calls to investigate the details of what needs to be done
- **Monitor usage** in real-time to pace yourself throughout the day
- **Combine models strategically**: Start with Auto+ for complex setup, switch to Auto for iterations
- **Avoid “thank you” and other non-task-related messages**: While politeness is key in human interactions, it is not necessary, and even costly in interactions with agents. Please be aware that all messages are counted against the limits regardless of their content

## Account Management

What happens after my Zencoder trial ends?

Once the trial ends, your account will automatically switch to the Free plan with limited features. You can choose to upgrade at any time to retain access to advanced tools and workflows.

How do I upgrade my Zencoder subscription?

Upgrading is simple! Navigate to your account settings, select the plan you wish to upgrade to, and follow the on-screen instructions. Upgrading unlocks additional features and premium support.

How do upgrades, downgrades, or cancellations work?

You can upgrade, downgrade, or cancel your plan from the self-serve customer portal (customer portal under profile).

- **Upgrades** take effect instantly
- **Downgrades** take effect on your next renewal
- **Cancel** any time; you keep access until the end of the paid period

For more information about our policies regarding cancellations and refunds, please see our detailed [Refund Policy](https://docs.zencoder.ai/faq/refund-policy).

I upgraded my Zencoder plan but don't see the new limits. What should I do?

When you upgrade or change your Zencoder plan, the new features and permissions may not be immediately reflected in your IDE. Logging out and logging back in refreshes your authentication token and ensures your IDE recognizes your new plan’s entitlements. In some cases, you may also need to restart your IDE for all changes to take effect.**How to log out and log back in:**

**Visual Studio Code**

1. Open the Command Palette (On macOS: Press `Shift + Command + P`, On Windows/Linux: Press `Shift + Ctrl + P`)
2. Type `Zencoder: Sign out` and select it ![VS Code Sign Out and Authentication Process](https://mintcdn.com/forgoodaiinc/27PjYbRg8KyUQ0DD/images/vsc-signout-authenticate.png?fit=max&auto=format&n=27PjYbRg8KyUQ0DD&q=85&s=bf3bd8364aaf1ce39fbfd1cc549e6e3e)
3. After signing out, you’ll see large buttons to sign in - just follow the process

**JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)**

1. Open Settings (On macOS: Press `Command + ,`, On Windows/Linux: Press `Ctrl + Alt + S` or go to `File > Settings`)
2. Navigate to `Tools > Zencoder`
3. Click the `Authenticate` button under “Launch authentication process” ![JetBrains Authentication Settings](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/jb-settings-authenticate.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=bc6c4f46d642eb62dd0dfbf0f922cfa1)
4. Follow the prompts to sign out and sign back in

Can I buy multiple seats and assign them to myself for higher limits?

Yes! With dynamic seat allocation, you can purchase multiple seats and assign them to yourself to multiply your daily limits. Account admins can allocate unused seats to any user, effectively increasing their capacity:

- **×2 Allocation**: Doubles your daily usage limits by consuming 2 seats
- **×5 Allocation**: Increases your daily limits by 5x by consuming 5 seats

This is controlled through your Admin Panel, giving you flexibility to scale usage based on your development needs. For more details, see [Dynamic Seat Allocation](https://docs.zencoder.ai/get-started/subscription#dynamic-seat-allocation).

## Advanced Options

Can I use my API key for Anthropic/OpenAI ('Bring your own key')?

Yes, you can currently use your own API keys for OpenAI and Anthropic models. Gemini support is planned and coming soon. For most users, our pricing gives an easy and cost-effective way to plan and manage AI costs. Some users are comfortable spending $200+/usr/mo directly on API providers as they feel they are getting 10x ROI on their use; in that case, BYOK is a good option. In the future, we could replace it with per-token pricing through the platform, if there’s a demand for that.

How does BYOK pricing work?

You pay Zencoder the seat fee (Starter/Core/Advanced/Max). When you select the BYOK option and use your own OpenAI or Anthropic key, all LLM calls using that model will utilize your key. Gemini support is coming soon.

## Legacy Plans

I'm on the legacy Business plan at $19 / user. Can I switch to Starter, and what happens to my limits?

Yes. You can switch to the current Starter tier on the Billing page. The seat price stays at $19, but once you leave the legacy Business plan, you can’t switch back.

I'm on the legacy Enterprise plan at $39 / user. What changes if I move to Core or Advanced?

**Moving to Core ($49/user):** Your subscription cost increases by $10 per user per month. You retain all existing enterprise features including SSO and Audit Logs, while gaining enhanced visibility into LLM call consumption and usage analytics. Core plans and above also include [Multi-Repo Search](https://docs.zencoder.ai/features/multi-repo) capabilities for searching across multiple repositories.**Moving to Advanced ($119/user):** While the subscription cost increases, you gain access to 1,500 daily Premium LLM calls per user—substantially higher than both Core and legacy Enterprise plan limits. This tier is designed for power users and teams with high AI automation requirements.

Once you migrate from a legacy plan to any current plan tier, you cannot revert to the legacy pricing structure.

## General Support

What payment methods are accepted for Zencoder?

Zencoder supports payment via:

- All major credit cards
- Apple Pay
- Link
- Cash App and Klarna

For specific payment methods, wire transfers, or enterprise invoicing options, please [contact our support team](https://docs.zencoder.ai/get-started/community-support).

How does Zencoder ensure the security of my code?

Zencoder prioritizes security through:

- **Data encryption:**All data is encrypted in transit and at rest.
- **Access controls:**Implement multi-factor authentication and role-based permissions.
- **Audit logs:**Track activity for monitoring and compliance purposes.

Which IDEs and editors does Zencoder support?

Zencoder supports integrations with popular IDEs, including Visual Studio Code, JetBrains IDEs, and Android Studio.

Does Zencoder offer refunds?

We offer a comprehensive 7-day free trial that allows you to fully evaluate Zencoder before making any financial commitment. For detailed information about our refund policies, cancellations, and subscription management, please visit our [Refund Policy](https://docs.zencoder.ai/faq/refund-policy) page.