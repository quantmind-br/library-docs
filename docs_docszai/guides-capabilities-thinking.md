---
title: Deep Thinking
url: https://docs.z.ai/guides/capabilities/thinking.md
source: llms
fetched_at: 2026-01-24T11:23:04.339014626-03:00
rendered_js: false
word_count: 348
summary: This document explains how to implement and configure the Deep Thinking feature to enable advanced chain-of-thought reasoning and multi-step logic in GLM models.
tags:
    - deep-thinking
    - chain-of-thought
    - glm-models
    - api-integration
    - reasoning
    - python-sdk
    - llm-inference
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Thinking

<Tip>
  Deep Thinking is an advanced reasoning feature that enables Chain of Thought mechanisms, allowing the model to perform deep analysis and reasoning before answering questions. This approach significantly improves the model's accuracy and interpretability in complex tasks, particularly suitable for scenarios requiring multi-step reasoning, logical analysis, and problem-solving.
</Tip>

## Features

The Deep Thinking feature currently supports the latest models in the GLM-4.5 and GLM-4.6 series. By enabling deep thinking, the model can:

* **Multi-step Reasoning**: Break down complex problems into multiple steps for gradual analysis and resolution
* **Logical Analysis**: Provide clear reasoning processes and logical chains
* **Improved Accuracy**: Reduce errors and improve answer quality through deep thinking
* **Enhanced Interpretability**: Display the thinking process to help users understand the model's reasoning logic
* **Intelligent Judgment**: The model automatically determines whether deep thinking is needed to optimize response efficiency

### Core Parameters

* **`thinking.type`**: Controls the deep thinking mode
  * `enabled` (default): Enable dynamic thinking, model automatically determines if deep thinking is needed
  * `disabled`: Disable deep thinking, provide direct answers
* **`model`**: Models that support deep thinking, such as `glm-4.6`, `glm-4.5`, `glm-4.5v`, etc.

## Code Examples

<Tabs>
  <Tab title="cURL">
    **Basic Call (Enable Deep Thinking)**

    ```bash  theme={null}
    curl --location 'https://api.z.ai/api/paas/v4/chat/completions' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "glm-4.7",
        "messages": [
            {
                "role": "user",
                "content": "Explain in detail the basic principles of quantum computing and analyze its potential impact in the field of cryptography"
            }
        ],
        "thinking": {
            "type": "enabled"
        },
        "max_tokens": 4096,
        "temperature": 1.0
    }'
    ```

    **Streaming Call (Deep Thinking + Streaming Output)**

    ```bash  theme={null}
    curl --location 'https://api.z.ai/api/paas/v4/chat/completions' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "glm-4.7",
        "messages": [
            {
                "role": "user",
                "content": "Design a recommendation system architecture for an e-commerce website, considering user behavior, product features, and real-time requirements"
            }
        ],
        "thinking": {
            "type": "enabled"
        },
        "stream": true,
        "max_tokens": 4096,
        "temperature": 1.0
    }'
    ```

    **Disable Deep Thinking**

    ```bash  theme={null}
    curl --location 'https://api.z.ai/api/paas/v4/chat/completions' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "glm-4.7",
        "messages": [
            {
                "role": "user",
                "content": "How is the weather today?"
            }
        ],
        "thinking": {
            "type": "disabled"
        }
    }'
    ```
  </Tab>

  <Tab title="Python SDK">
    **Install SDK**

    ```bash  theme={null}
    # Install latest version
    pip install zai-sdk

    # Or specify version
    pip install zai-sdk==0.1.0
    ```

    **Verify Installation**

    ```python  theme={null}
    import zai
    print(zai.__version__)
    ```

    **Basic Call (Enable Deep Thinking)**

    ```python  theme={null}
    from zai import ZaiClient

    # Initialize client
    client = ZaiClient(api_key='your_api_key')

    # Create deep thinking request
    response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {"role": "user", "content": "Explain in detail the basic principles of quantum computing and analyze its potential impact in the field of cryptography"}
        ],
        thinking={
            "type": "enabled"  # Enable deep thinking mode
        },
        max_tokens=4096,
        temperature=1.0
    )

    print("Model response:")
    print(response.choices[0].message.content)
    print("\n---")
    print(response.choices[0].message.reasoning_content)
    ```

    **Streaming Call (Deep Thinking + Streaming Output)**

    ```python  theme={null}
    from zai import ZaiClient

    # Initialize client
    client = ZaiClient(api_key='your_api_key')

    # Create streaming deep thinking request
    response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {"role": "user", "content": "Design a recommendation system architecture for an e-commerce website, considering user behavior, product features, and real-time requirements"}
        ],
        thinking={
            "type": "enabled"  # Enable deep thinking mode
        },
        stream=True,  # Enable streaming output
        max_tokens=4096,
        temperature=1.0
    )

    # Process streaming response
    reasoning_content = ""
    thinking_phase = True

    for chunk in response:
        if not chunk.choices:
            continue
        
        delta = chunk.choices[0].delta
        
        # Process thinking process (if any)
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content:
            reasoning_content += delta.reasoning_content
            if thinking_phase:
                print("🧠 Thinking...", end="", flush=True)
                thinking_phase = False
            print(delta.reasoning_content, end="", flush=True)
        
        # Process answer content
        if hasattr(delta, 'content') and delta.content:
            if thinking_phase:
                print("\n\n💡 Answer:")
                thinking_phase = False
            print(delta.content, end="", flush=True)

    ```

    **Disable Deep Thinking**

    ```python  theme={null}
    from zai import ZaiClient

    # Initialize client
    client = ZaiClient(api_key='your_api_key')

    # Disable deep thinking for quick response
    response = client.chat.completions.create(
        model="glm-4.7",
        messages=[
            {"role": "user", "content": "How is the weather today?"}
        ],
        thinking={
            "type": "disabled"  # Disable deep thinking mode
        }
    )

    print(response.choices[0].message.content)
    ```
  </Tab>
</Tabs>

### Response Example

Response format with deep thinking enabled:

```json  theme={null}
{
  "created": 1677652288,
  "model": "glm-4.7",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Artificial intelligence has tremendous application prospects in medical diagnosis...",
        "reasoning_content": "Let me analyze this question from multiple angles. First, I need to consider the technical advantages of AI in medical diagnosis..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "completion_tokens": 239,
    "prompt_tokens": 8,
    "prompt_tokens_details": {
      "cached_tokens": 0
    },
    "total_tokens": 247
  }
}
```

## Best Practices

**Recommended scenarios to enable:**

* Complex problem analysis and solving
* Multi-step reasoning tasks
* Technical solution design
* Strategy planning and decision
* Academic research and analysis
* Creative writing and content creation

**Can be disabled scenarios:**

* Simple fact query
* Basic translation tasks
* Simple classification judgment
* Quick question and answer requirements

## Application scenarios

<CardGroup cols={2}>
  <Card title="Academic Research" icon="book">
    * Research method design
    * Data analysis and explanation
    * Theory deduction and proof
  </Card>

  <Card title="Technology Consulting" icon="code">
    * System architecture design
    * Technological scheme evaluation
    * Problem diagnosis and solution
  </Card>

  <Card title="Business Analysis" icon="chart-line">
    * Market trends analysis
    * Business model design
    * Investment decision support
  </Card>

  <Card title="Education Training" icon="users">
    * Complex concept explanation
    * Learning path planning
    * Knowledge system building
  </Card>
</CardGroup>

## Notes

1. **Response time**：Enable deep thinking will increase response time, particularly for complex tasks
2. **Token consumption**：Thinking process will consume extra tokens, please manage your tokens
3. **Model support**：Ensure you're using models that support deep thinking
4. **Task matching**：Choose whether to enable deep thinking according to the task complexity
5. **Streaming output**：Combine streaming output to see the thinking process, improving user experience