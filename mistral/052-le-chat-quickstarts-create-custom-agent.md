---
title: Create and share a custom agent | Mistral Docs
url: https://docs.mistral.ai/le-chat/quickstarts/create-custom-agent
source: sitemap
fetched_at: 2026-04-26T04:08:09.259872937-03:00
rendered_js: false
word_count: 439
summary: This document provides a step-by-step guide for creating, configuring, and sharing custom AI agents within the Le Chat platform.
tags:
    - ai-agents
    - mistral-le-chat
    - system-prompting
    - knowledge-base
    - tool-integration
    - team-collaboration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Create a custom agent in [Le Chat](https://chat.mistral.ai) with its own instructions, tools, and knowledge base.

**What you can do:**
- Write a system prompt to define the agent's behavior
- Attach documents as a knowledge source
- Enable tools like Web Search, Code Interpreter, and Canvas
- Share the agent with your team

**Time to complete:** ~10 minutes

**Prerequisites:**
- Le Chat account (Free, Pro, or Team plan)
- Optional: document to use as a knowledge source (PDF, TXT, DOCX)

## Steps

### 1. Create Agent

1. In the Le Chat sidebar, click **Agents**.
2. Click **Create agent**.
3. Give your agent a name: e.g., `Meeting Summarizer`.
4. Choose a model. **Mistral Medium** is a good default.

### 2. Write Instructions

Instructions shape how the agent behaves. Be specific about the task, format, and tone.

In the **Instructions** field, write a system prompt. Example:

> You are a meeting summarizer. When given meeting notes or a transcript, produce:
> 1. A one-paragraph executive summary
> 2. A bulleted list of action items with owners
> 3. A list of open questions
> Keep the tone professional and concise. Don't add information not present in the source material.

Set a **Temperature**: use `0.2` for consistent, deterministic output or `0.7` for more creative responses.

> [!tip]
> Good instructions define what the agent should do, the output format, and what it should avoid. Test with example conversations and refine.

### 3. Enable Tools

Tools extend what the agent can do beyond text generation.

Scroll to **Tools** and toggle on the capabilities you need:
- **Web browsing**: search the internet for current information
- **Code Interpreter**: run Python code for calculations, charts, and data analysis
- **Canvas**: create and edit documents, presentations, or code interactively

For a Meeting Summarizer, **Canvas** is useful so the agent can produce an editable summary document.

### 4. Add Knowledge (Optional)

Attach documents so the agent can reference them when answering questions.

1. Scroll to **Knowledge** and click **Add library**.
2. Upload a document: e.g., a company meeting template or style guide.
3. The agent retrieves relevant sections during conversations.

Useful when the agent needs domain-specific context like company policies, product docs, or internal guides.

### 5. Save and Test

1. Click **Save** to create the agent.
2. Start a conversation with your agent: paste some meeting notes and verify the output matches your instructions.

### 6. Share with Team

1. Click the **three-dot menu** on the agent.
2. Select **Share**.
3. Choose team members or copy the share link.

Team members can use the agent from their own Le Chat sidebar without seeing or modifying the instructions.

## Verification

Your agent is working correctly if:
- It follows the instruction format consistently across different inputs
- Enabled tools (web search, canvas) activate when relevant
- Knowledge base content is referenced when you ask related questions
- Shared team members can access and use the agent

#ai-agents #system-prompting #knowledge-base