---
title: Chat Completions | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/chat-completion
source: sitemap
fetched_at: 2026-04-26T04:12:20.994571426-03:00
rendered_js: false
word_count: 875
summary: Chat Completion API overview explaining roles of system, user, assistant, and tool messages, with features like multi-turn conversations and request customization flags.
tags:
    - chat-completions
    - large-language-models
    - api-integration
    - prompt-engineering
    - message-roles
    - function-calling
    - multi-turn-conversations
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Chat Completions

Large language models (LLMs) generate text and engage in conversational interactions, following instructions and responding naturally to prompts.

![Chat Completions](https://docs.mistral.ai/img/chat_completions.png)![Chat Completions dark](https://docs.mistral.ai/img/chat_completions_dark.png)

## Use Cases

- Chatbots
- Classification
- Data extraction
- Text summarization
- Code generation
- Question answering

## API Input

The [Chat Completion API](https://docs.mistral.ai/api/#tag/chat) accepts a list of chat messages and generates a response as a new assistant message.

### Message Roles

| Role | Description |
|------|-------------|
| `system` | **Optional** — Sets behavior, context, and instructions for the AI assistant |
| `user` | Message from the human in the conversation |
| `assistant` | Message from the AI assistant (can include tool calls, citations) |
| `tool` | Only in **function calling** context — formats tool call output for the user |

### Message Content Types

Content can be a `string` or a `list` of chunks:

```python
# String response
{"content": "Hello, how can I help you?"}

# Chunked response (for citations, tool calls, etc.)
{"content": [
    {"type": "text", "text": "The answer is "},
    {"type": "tool_reference", "tool": "web_search", "title": "Source", "url": "..."}
]}
```

## System vs User Prompt

- Combine `system` and `user` into a single `user` message, or
- Use `system` for persistent instructions and `user` for conversation-specific input

> [!tip] Experiment with both to determine what works better for your use case.

## Multi-turn Conversations

Send multiple messages back and forth. Events like tool calls and handoffs can be interleaved between interactions.

For simplified multi-turn handling, consider using the [Agents and Conversations APIs](https://docs.mistral.ai/studio-api/agents/introduction).

## Request Customization

| Flag | Description |
|------|-------------|
| `prefix` | Prepend content to assistant's response |
| `safe_prompt` | Force moderation against sensitive content (see [Guardrailing](https://docs.mistral.ai/studio-api/safety-moderation)) |
| `stop` | Force model to stop after one or more chosen tokens/strings |

### Prefix Example

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    prefix="Answer in bullet points: "  # Model starts with this exact string
)
```

## Additional Features

- [Vision](https://docs.mistral.ai/studio-api/conversations/vision) — Image analysis
- [Function Calling](https://docs.mistral.ai/studio-api/agents/agent-tools/function-calling) — Tool integration
- [Predicted Outputs](https://docs.mistral.ai/studio-api/conversations/advanced/predicted-outputs) — Latency optimization
- [Structured Outputs](https://docs.mistral.ai/studio-api/conversations/structured-output) — Enforced JSON format

#chat-completions #large-language-models #api-integration #prompt-engineering #message-roles #function-calling #multi-turn-conversations
