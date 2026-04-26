---
title: Agents | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/agents
source: sitemap
fetched_at: 2026-04-26T04:07:49.198559539-03:00
rendered_js: false
word_count: 991
summary: This document provides a comprehensive overview of how to create, configure, share, and manage customized AI Agents within the platform to automate repetitive tasks and ensure consistent outputs.
tags:
    - ai-agents
    - prompt-engineering
    - workflow-automation
    - knowledge-base
    - collaboration
    - user-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Agents

An Agent is a specialized assistant you configure once and reuse across conversations. Give it instructions, tools, and knowledge sources, and it handles the rest.

Use Agents when you need the same instructions, tone, or knowledge applied consistently.

## Use Cases

- **Brand voice editor**: paste any draft and get it rewritten in your company's tone with the same formatting rules.
- **Legal clause checker**: upload a contract and flag non-standard clauses based on your internal policy [Library](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries).
- **Meeting prep assistant**: share a prospect's website or briefing doc and get structured talking points, key figures, and open questions.
- **Technical FAQ**: attach your product documentation as a [Library](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries) and share the Agent with your team.
- **Translation with context**: translate content while respecting your glossary and brand terminology.

## Creating an Agent

1. Click `Agents` in the left sidebar.
2. Click `Create Agent` to start from scratch, or pick a **pre-built template**.
3. Configure the Agent (see below).
4. Test it in the **preview panel** on the right side of the screen.

Agents save automatically. There's no save button.

Templates cover common patterns like summarizers, translators, and code assistants.

## Configuration

Every Agent starts with four fields:

- **Name**: clear, descriptive name your team can find at a glance (e.g., `Customer Support Triage`).
- **Description** (optional): short explanation of what the Agent does, visible in the Agent picker.
- **Avatar** (optional): choose from presets or generate a custom one.
- **Instructions**: detailed guidance for the Agent's behavior. Type `/` in the field to reference tools and knowledge sources inline.

## Using an Agent

1. Click `+` then select `Agents` or type `/` in the message box.
2. Search for or select an Agent. Its name appears at the top of the chat box.
3. Send your message.

### Switching Agents

Click the dropdown arrow next to the Agent name and select a different Agent. Only **one Agent can be active at a time** within a conversation.

### Returning to the Default Model

Click the cross icon next to the Agent name to remove it. The conversation continues with the default Le Chat model.

## Writing Good Instructions

- **Define the role clearly.** Start with who the Agent is and what it does.
- **Specify the output format.** Tell the Agent whether you expect bullet points, JSON, prose, a table, or something else.
- **Set explicit boundaries.** State what the Agent should not do.
- **Reference tools inline.** Type `/` in the instructions field to mention specific tools or knowledge sources.
- **Iterate in small steps.** Change one thing, test in the preview panel, repeat.

For prompt writing techniques, see our [prompt engineering guide](https://docs.mistral.ai/models/best-practices/prompt-engineering).

## Sharing

By default, a new Agent is **private** (only you can see and use it).

### Sharing with Specific People

1. Open the Agent's card on the `Agents` page.
2. Click the sharing status label (`Private`, `Organization`, or `x people`).
3. Search for users or groups and assign a permission level:
   - **Collaborator**: can use, edit, and delete the Agent.
   - **Viewer**: can use the Agent but can't edit or delete it.

### Sharing with Your Entire Organization

Toggle `Entire organization` and choose whether everyone gets Collaborator or Viewer access.

> [!note]
> We don't send notifications when you share an Agent. Let your teammates know so they can start using it.

## Duplicating an Agent

Open the three-dots menu (`⠇`) on the Agent card and select `Duplicate my Agent`. This creates a new, independent copy you own.

Duplicating is also the workaround for transferring an Agent to a colleague.

## Deleting an Agent

1. Open the three-dots menu (`⠇`) on the Agent card.
2. Select `Delete` and confirm.

> [!warning]
> Deleting an Agent is permanent. If the Agent was shared, it becomes unavailable to everyone.

## Availability

Agents are available on all plans. If you change or cancel your subscription, your Agents and their sharing settings are preserved. Some tools or knowledge sources may become unavailable on lower-tier plans.

Agents created in Le Chat are designed for the chat interface and can't be used programmatically. For API access, create Agents through [Studio Agents](https://console.mistral.ai/build/agents) or the [REST API](https://docs.mistral.ai/api/#tag/beta.agents).

Studio Agents can be deployed to Le Chat and appear in a dedicated section of your Agent list.

## Related

- [[146-le-chat-knowledge-integrations-custom-instructions|Custom instructions]]: set persistent behavior rules that apply to all conversations.
- [[147-le-chat-knowledge-integrations-libraries|Libraries]]: build knowledge bases from uploaded documents.
- [[143-le-chat-knowledge-integrations-connectors|Connectors]]: connect external data sources like Google Drive, GitHub, or Notion.
- [[149-le-chat-knowledge-integrations-projects|Projects]]: organize conversations into scoped work areas.

#ai-agents #prompt-engineering #workflow-automation
