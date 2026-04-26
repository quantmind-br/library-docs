---
title: Prompting | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/chat-completion/prompting
source: sitemap
fetched_at: 2026-04-26T04:12:22.809712348-03:00
rendered_js: false
word_count: 1100
summary: Best practices for designing effective prompts including role definition, structural formatting, few-shot prompting, and common pitfalls to avoid.
tags:
    - prompt-engineering
    - large-language-models
    - system-prompts
    - few-shot-prompting
    - structured-output
    - ai-best-practices
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Prompting

Master crafting effective prompts to generate high-quality responses from Mistral models.

## Main Concepts

### System vs User Prompts

| Level | Description |
|-------|-------------|
| `system` | Provided at conversation start — sets general context and instructions |
| `user` | Provided during conversation — specific context for current interaction |

**Role-Separated Example:**
```python
messages=[
    {"role": "system", "content": "You are a customer support agent for a bank."},
    {"role": "user", "content": "Can I use your card in the EU?"}
]
```

**Concatenated Example:**
```python
messages=[
    {"role": "user", "content": "You are a bank customer support agent. Can I use your card in the EU?"}
]
```

### Roleplaying

Define a clear role and task: *"You are a `<role>`, your task is to `<task>`."*

### Structure

Organize instructions hierarchically with clear sections. Write for someone with **no prior context**.

### Formatting

Use **Markdown** and/or **XML-style tags** — readable, parsable, and familiar from training.

### Example Prompt Structure

```markdown
# Task
You are a code reviewer.

# Input
The following Python function has a bug:

# Function
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Review
Identify the bug and suggest a fix.
```

## Few-shot Prompting

Provide task examples to improve model understanding and output format.

**Direct Example in Prompt:**
```python
messages=[
    {"role": "user", "content": "Translate to French: Hello"},
    {"role": "assistant", "content": "Bonjour"},
    {"role": "user", "content": "Translate to French: Good morning"},
    {"role": "assistant", "content": "Bonjour"}
]
```

## What to Avoid

| Avoid | Instead |
|-------|--------|
| "too long", "too short", "many", "few" | Objective measures with specific values |
| "things", "stuff", "interesting", "better" | Exact definitions of what you mean |
| Vague conditions like "if too long, split" | Specific rules like "if > 1000 chars, split" |

### Contradictions in System Prompts

If your system prompt gets long, watch for contradictions:

**Avoid:**
- "If related, update existing record"
- "If new, create new record"
- (Unclear if new-but-related data should update or create)

**Use a decision tree:**
- "If record with same ID exists: update"
- "If no record with same ID: create new"

### Token Efficiency

Models ingest faster than they generate. Only ask for necessary output:

**Bad:**
```python
# Generating full record for NO_OP
{"operation": "NO_OP", "content": "..."}  # Wasteful
```

**Good:**
```python
{"operation": "NO_OP"}  # Only what's needed
```

### Rating Scales

Use worded scales for better performance:

**Avoid:** "Rate 1-5"
**Use:** "Rate as: excellent / good / acceptable / poor / failing"

## Example Capabilities

- Classification
- Summarization
- Personalization
- Evaluation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/prompting/prompting_capabilities.ipynb)

### Classification Example

```python
messages=[
    {"role": "system", "content": "Classify the customer inquiry into one of: country_support, billing, technical, general."},
    {"role": "user", "content": "I am inquiring about the availability of your cards in the EU, as I am a resident of France."}
]
# Response: "country_support"
```

**Classification Strategies:**

| Strategy | Pros | Cons |
|----------|------|------|
| Direct label | Fast, cheap | May lack flexibility |
| JSON output | Reliable, flexible | More tokens |

#prompt-engineering #large-language-models #system-prompts #few-shot-prompting #structured-output #ai-best-practices
