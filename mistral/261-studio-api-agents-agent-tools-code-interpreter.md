---
title: Code Interpreter | Mistral Docs
url: https://docs.mistral.ai/studio-api/agents/agent-tools/code_interpreter
source: sitemap
fetched_at: 2026-04-26T04:11:51.478216705-03:00
rendered_js: false
word_count: 328
summary: Integrate the Code Interpreter tool within AI agents for secure, on-demand code execution for data analysis and mathematical tasks.
tags:
    - code-interpreter
    - ai-agents
    - python-execution
    - data-analysis
    - tool-integration
    - agentic-workflow
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Code Interpreter

Safely executes code in an isolated container. This built-in tool allows Agents to run code on demand for graphs, data analysis, mathematical operations, code validation, and more.

![Code Interpreter architecture](https://docs.mistral.ai/img/code_interpreter_connector.png)![Code Interpreter architecture dark](https://docs.mistral.ai/img/code_interpreter_connector_dark.png)

## Usage

Create an agent with the code interpreter tool, then start a conversation. The agent runs code on demand, leveraging outputs to answer questions.

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Create agent with code interpreter
agent = client.agents.create(
    model="mistral-large-latest",
    tools=[{"type": "code_interpreter"}]
)

# Start conversation
chat_response = client.agents.chat(
    agent_id=agent.id,
    inputs="Generate the first 20 Fibonacci numbers"
)
```

## Response Structure

The response contains `message.output` and `tool.execution` entries:

### `message.output`

Initial assistant response indicating task understanding.

### `tool.execution`

Code interpreter execution metadata:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Tool name: `code_interpreter` |
| `object` | string | Object type: `entry` |
| `type` | string | Entry type: `tool.execution` |
| `created_at` | datetime | Execution start timestamp |
| `completed_at` | datetime | Execution completion timestamp |
| `id` | string | Unique execution identifier |
| `info.code` | string | Actual code executed |
| `info.code_output` | string | Output from executed code |

### Final `message.output`

Assistant's final response using the code execution results.

#code-interpreter #ai-agents #python-execution #data-analysis #tool-integration #agentic-workflow
