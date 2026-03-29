---
title: ForgeCode
url: https://forgecode.dev/docs/agent-configuration/
source: sitemap
fetched_at: 2026-03-29T14:51:22.187237301-03:00
rendered_js: false
word_count: 426
summary: This document provides comprehensive guidance on configuring AI agents in ForgeCode, covering parameters like temperature, context compaction, and visibility settings with troubleshooting advice and best practices.
tags:
    - agent-configuration
    - temperature-settings
    - context-compaction
    - system-prompts
    - custom-rules
    - ai-agents
    - forge-yaml
category: guide
---

ForgeCode provides extensive configuration options for AI agents, allowing you to tailor their behavior to your specific needs. This guide covers all available agent configuration options with examples and best practices.

In your `forge.yaml` file, agents are defined under the `agents` section:

### Basic Configuration Parameters[​](#basic-configuration-parameters "Direct link to Basic Configuration Parameters")

ParameterRequiredDescription`id`YesUnique identifier for the agent`model`YesAI model to use (e.g., anthropic/claude-3.5-sonnet)`system_prompt`YesSystem prompt or template reference`max_walker_depth`NoMaximum directory/file depth for exploration`custom_rules`NoCustom instructions or rules (see [Custom Rules](https://forgecode.dev/docs/custom-rules/))

Fine-tune the creativity and determinism of agent responses with the `temperature` setting:

The temperature parameter accepts values between 0.0 and 2.0:

TemperatureDescriptionBest For0.0 - 0.3Most deterministic, highly consistentCode generation, factual responses0.4 - 0.7Balanced creativity and consistencyGeneral purpose assistance0.8 - 1.2Increased creativity and variationCreative writing, brainstorming1.3 - 2.0Highest creativity, most variedUnconventional ideas, maximum exploration

### When to Adjust Temperature[​](#when-to-adjust-temperature "Direct link to When to Adjust Temperature")

- **Lower Temperature (0.0 - 0.3)** when you need:
  
  - Precise, reproducible code
  - Factual, consistent responses
  - Technical documentation
  - Structured data outputs
- **Medium Temperature (0.4 - 0.7)** when you need:
  
  - Balanced responses for everyday tasks
  - Natural-sounding text with reasonable variation
  - Problem-solving with some creativity
- **Higher Temperature (0.8 - 2.0)** when you need:
  
  - Creative writing assistance
  - Diverse brainstorming ideas
  - Out-of-the-box thinking
  - Varied solution approaches

## Context Compaction[​](#context-compaction "Direct link to Context Compaction")

Control how conversation history is managed with context compaction:

For detailed information about context compaction settings, see the [Context Compaction](https://forgecode.dev/docs/context-compaction/) documentation.

Control whether an agent's outputs are visible in the console with the `hide_content` setting:

When `hide_content` is set to `true`:

- The agent's responses won't appear in the console output
- The agent will still function normally in the background
- Other agents can still access its outputs
- This is useful for "helper" agents that support other primary agents

<!--THE END-->

1. **Match Temperature to Task**: Use lower temperatures for precise tasks and higher for creative ones
2. **Enable Context Compaction**: For long-running sessions or complex projects
3. **Use Base Models Appropriately**: More capable models for complex reasoning, faster models for simpler tasks
4. **Optimize System Prompts**: Use Handlebars templates for dynamic system prompts
5. **Leverage Hidden Agents**: Use background agents for auxiliary tasks without cluttering output

### Issue: Agent Responses Too Random[​](#issue-agent-responses-too-random "Direct link to Issue: Agent Responses Too Random")

- Lower the temperature setting
- Provide more specific instructions in the system prompt
- Add more detailed custom\_rules

### Issue: Agent Responses Too Repetitive[​](#issue-agent-responses-too-repetitive "Direct link to Issue: Agent Responses Too Repetitive")

- Increase the temperature slightly
- Review and update system prompt to allow more flexibility
- Check if your instructions are too restrictive

### Issue: Agent Not Seeing Full Context[​](#issue-agent-not-seeing-full-context "Direct link to Issue: Agent Not Seeing Full Context")

- Configure context compaction with higher token limits
- Increase retention\_window to keep more recent messages
- Use a model with larger context window

<!--THE END-->

- [ForgeCode Configuration](https://forgecode.dev/docs/forge-configuration/) - Global configuration settings
- [Context Compaction](https://forgecode.dev/docs/context-compaction/) - Detailed guide on context management
- [Tools Reference](https://forgecode.dev/docs/tools-reference/) - Available tools for agents to use