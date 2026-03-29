---
title: ForgeCode
url: https://forgecode.dev/docs/context-compaction/
source: sitemap
fetched_at: 2026-03-29T14:51:40.013411643-03:00
rendered_js: false
word_count: 1005
summary: This document explains ForgeCode's automatic context compaction feature, which summarizes older conversation parts to extend AI interactions beyond token limits while preserving important information and maintaining reasoning chains.
tags:
    - context-compaction
    - ai-conversation
    - token-management
    - automatic-summation
    - configuration
    - performance-optimization
    - reasoning-preservation
category: guide
---

ForgeCode includes powerful automatic context management capabilities that optimize AI conversations while preserving important information.

## What is Context Compaction?[​](#what-is-context-compaction "Direct link to What is Context Compaction?")

As conversations with AI agents grow longer, they can exceed token limits and become inefficient. Context compaction automatically summarizes older parts of conversations when they reach configurable thresholds, allowing you to maintain longer, more productive interactions without hitting model context limits.

Key benefits include:

- **Extended Conversations**: Continue conversations beyond normal token limits
- **Optimized Performance**: Reduce token usage and improve response times
- **Preserved Context**: Keep critical information while summarizing less important details
- **Cost Efficiency**: Reduce token usage in API calls
- **Reasoning Preservation**: Maintains reasoning chains for extended thinking models

Context compaction uses an intelligent multi-step process:

1. **Trigger Detection**: Compaction activates when ANY of these conditions are met:
   
   - Token count exceeds `token_threshold`
   - Total message count exceeds `message_threshold`
   - User turn count exceeds `turn_threshold`
   - Last message is from user AND `on_turn_end` is enabled
2. **Message Selection**: The system identifies which messages to compact:
   
   - Preserves recent messages based on `retention_window` and `eviction_window`
   - Starts from the first assistant message in the sequence
   - Maintains tool call/result pairs atomically (never splits them)
   - Uses a conservative approach to prevent over-compaction
3. **Summarization**: Older messages are sent to the configured model for summarization:
   
   - Detects if a plan was being executed and uses appropriate format
   - Extracts file operations, action logs, and task status
   - Consolidates multiple older summaries chronologically
4. **Context Replacement**: The summary replaces compacted messages as a user message:
   
   - Includes any user feedback from the compacted sequence
   - Preserves the natural conversation flow
5. **Reasoning Preservation**: For extended thinking models:
   
   - Extracts the most recent reasoning from compacted messages
   - Injects it into the first remaining assistant message
   - Prevents breaking reasoning chains while avoiding accumulation

This process runs in parallel with your main request to minimize latency impact.

Add the following to your `forge.yaml` file under an agent configuration:

### Configuration Parameters[​](#configuration-parameters "Direct link to Configuration Parameters")

ParameterRequiredDescription`token_threshold`NoTrigger compaction when token count exceeds this value`message_threshold`NoTrigger compaction when total messages exceed this value`turn_threshold`NoTrigger compaction when user turns exceed this value`on_turn_end`NoTrigger compaction on user messages (default: false)`retention_window`NoNumber of recent messages to preserve unchanged`eviction_window`NoPercentage (0.0-1.0) of context that can be summarized`max_tokens`NoMaximum token count for the generated summary`model`NoAI model to use for generating the summary`prompt`NoCustom prompt template for summarization

Triggering Logic

Compaction triggers when **ANY** condition is met. You can use one or more thresholds based on your needs. The system uses a conservative strategy - if both `eviction_window` and `retention_window` apply, it will preserve more context (whichever is more conservative).

on\_turn\_end Usage

Setting `on_turn_end: true` will trigger compaction after every user message, which can be very aggressive and may remove important context. Use this option carefully and only in specific scenarios where you need frequent context reduction.

### Selecting Appropriate Thresholds[​](#selecting-appropriate-thresholds "Direct link to Selecting Appropriate Thresholds")

Set thresholds based on your model's context window and usage patterns:

**Token-based triggering (recommended for most cases):**

- For Claude 3.7 Sonnet (~200K token window): 150,000 to 180,000 tokens
- For Claude 3.5 haiku (~200K token window): 120,000 to 160,000 tokens
- Leave headroom for the model to work with full context

**Message/Turn-based triggering (useful for specific scenarios):**

- Use `message_threshold` for very long conversations regardless of token count
- Use `turn_threshold` when you want to limit based on user interactions
- Combine with token thresholds for multi-condition triggering

### Choosing Summarization Models[​](#choosing-summarization-models "Direct link to Choosing Summarization Models")

For the summarization model, balance speed and quality:

- **Fast models** (like Gemini Flash): Provide quicker summaries with lower cost
- **Powerful models** (like Claude Sonnet): Better context preservation but higher cost and latency
- Consider using a different model than your main agent for cost optimization

### Retention and Eviction Windows[​](#retention-and-eviction-windows "Direct link to Retention and Eviction Windows")

These settings work together to determine what gets compacted:

- **Retention Window** (fixed count): Preserves the last N messages unchanged
  
  - Typical value: 6-10 messages
  - Guarantees recent context is never compacted
- **Eviction Window** (percentage): Controls what portion can be summarized
  
  - Range: 0.0 (nothing) to 1.0 (everything eligible)
  - Typical value: 0.2 (20% of older context)
  - More conservative than retention window wins

**Example**: With `retention_window: 6` and `eviction_window: 0.2`, if you have 100 messages:

- Retention says: preserve last 6, can compact first 94
- Eviction says: can compact 20% of 100 = 20 messages
- Result: Compacts the first 20 messages (more conservative)

### Long Debugging Sessions[​](#long-debugging-sessions "Direct link to Long Debugging Sessions")

When debugging complex issues, conversations can become lengthy. Context compaction allows the agent to remember key debugging steps while summarizing earlier diagnostics.

### Multi-Stage Project Development[​](#multi-stage-project-development "Direct link to Multi-Stage Project Development")

For projects developed over multiple sessions, context compaction enables the agent to maintain awareness of project requirements and previous decisions while focusing on current tasks.

### Interactive Learning and Tutorials[​](#interactive-learning-and-tutorials "Direct link to Interactive Learning and Tutorials")

When using ForgeCode for learning or following tutorials, compaction helps maintain the thread of the lesson while summarizing earlier explanations.

Context compaction is designed to minimize performance impact:

- **Parallel Execution**: Compaction runs alongside your main request, not blocking responses
- **Summarization Latency**: More powerful models may take longer but provide better summaries
- **Cost Impact**: Each compaction requires an LLM call, adding to usage costs
- **Token Reduction**: Effective compaction can reduce overall token usage significantly

**Optimization tips:**

- Use faster models (like Gemini Flash) for summarization to reduce latency
- Set higher thresholds to compact less frequently
- Balance `retention_window` and `eviction_window` for your use case

### Issue: Context Seems Lost After Compaction[​](#issue-context-seems-lost-after-compaction "Direct link to Issue: Context Seems Lost After Compaction")

**Possible causes:**

- Summary model not preserving key details
- Eviction window too aggressive
- Retention window too small

**Solutions:**

- Increase `max_tokens` to allow for more detailed summaries
- Use a more capable summarization model
- Increase `retention_window` to preserve more recent messages
- Reduce `eviction_window` to compact less aggressively
- Customize the summarization `prompt` to emphasize important details

### Issue: Slow Responses After Threshold is Reached[​](#issue-slow-responses-after-threshold-is-reached "Direct link to Issue: Slow Responses After Threshold is Reached")

**Possible causes:**

- Slow summarization model
- Very large context to summarize

**Solutions:**

- Choose a faster summarization model (e.g., Gemini Flash)
- Reduce `token_threshold` to trigger earlier compaction with smaller context
- Increase `eviction_window` to compact more at once (fewer compactions)

<!--THE END-->

- [Agent Configuration](https://forgecode.dev/docs/agent-configuration/) - Learn about other agent configuration options
- [Operating Agents](https://forgecode.dev/docs/operating-agents/) - Understand how context works in different operation modes
- [Commands Reference](https://forgecode.dev/docs/commands/) - Use `/compact` to manually trigger compaction

* * *

By effectively using context compaction, you can maintain longer, more productive AI conversations while optimizing for performance and cost efficiency. The system intelligently balances context preservation with token optimization, ensuring your agents have the information they need without exceeding limits.