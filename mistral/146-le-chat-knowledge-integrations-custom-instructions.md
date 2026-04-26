---
title: Custom instructions | Mistral Docs
url: https://docs.mistral.ai/le-chat/knowledge-integrations/custom-instructions
source: sitemap
fetched_at: 2026-04-26T04:07:56.972946263-03:00
rendered_js: false
word_count: 539
summary: This document explains how to configure and utilize custom instructions to establish persistent preferences and formatting styles for interactions within Le Chat.
tags:
    - custom-instructions
    - user-preferences
    - le-chat
    - context-management
    - ai-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Custom Instructions

Custom instructions define **persistent preferences** that shape how Le Chat responds across every conversation. Think of them as a brief profile: your role, domain, preferred output style. Set it once and Le Chat applies it automatically.

For teams, custom instructions help standardize how your organization interacts with Le Chat.

## Setting Up Custom Instructions

1. In the left-menu bar, click `Intelligence` then `Instructions`.
2. The Custom instructions pop-up opens.
3. Choose a **Tone** and enter your instructions.
4. Save your changes.

Your instructions take effect in all new conversations from that point on. Existing conversations aren't affected.

Custom instructions are included in the [context](https://docs.mistral.ai/le-chat/conversation/chat) Le Chat uses to generate every response.

## Priority with Other Features

| Feature | Priority |
|---------|----------|
| **Agents** | When you activate an Agent, its instructions take precedence over your custom instructions. |
| **Memories** | Both apply together. If they conflict, custom instructions take priority. |
| **Tools** | Custom instructions shape how Le Chat communicates but don't change how tools execute. |

## Examples of Good Custom Instructions

**Role and domain expertise:**
- *"I'm a compliance officer at a European bank. Reference EU regulations (MiFID II, GDPR) when relevant."*
- *"I'm a software engineer working with Python and TypeScript. Tailor code examples accordingly."*

**Output formatting:**
- *"Structure all technical responses with Problem, Analysis, Solution, and Next Steps sections."*
- *"Always format financial figures with two decimal places and include the currency symbol."*

**Language and tone:**
- *"Always respond in French unless I ask otherwise."*
- *"Respond in British English. Use formal tone for client-facing content, casual for internal notes."*

**Constraints:**
- *"Don't include disclaimers or caveats unless I'm asking about medical, legal, or financial advice."*
- *"When generating code, always include error handling and type annotations."*

## Best Practices

- **Don't use them as a project brief.** They're meant for persistent preferences, not task descriptions.
- **Don't contradict your prompts.** If your custom instruction says "always respond in French" but you ask questions in English, you'll get inconsistent results.
- **Keep them concise.** A few well-written sentences work better than multiple paragraphs.

## Related

- [[142-le-chat-knowledge-integrations-agents|Agents]]: create specialized configurations with their own instructions, tools, and Connectors.
- [[148-le-chat-knowledge-integrations-memories|Memories]]: let Le Chat learn and recall context from your conversations automatically.
- [[149-le-chat-knowledge-integrations-projects|Projects]]: organize conversations within scoped work areas.

#custom-instructions #user-preferences #le-chat #context-management
