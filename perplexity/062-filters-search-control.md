---
title: Web Search Control
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/search-control.md
source: llms
fetched_at: 2026-02-04T07:23:21.901913132-03:00
rendered_js: false
word_count: 418
summary: This document explains how to manage web search functionality for Sonar models using the search classifier for automated decision-making or by disabling search entirely. It provides implementation details via the Chat Completions API along with best practices for performance optimization.
tags:
    - perplexity-api
    - sonar-models
    - web-search
    - search-classifier
    - api-configuration
    - search-control
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Search Control

> Control when Sonar models search the web using the search classifier or by disabling search altogether.

## Overview

Grounded LLMs provide powerful web search capabilities, but there are times when you want to control when and how searches are performed. Perplexity offers two main approaches for search control:

* **Search Classifier** - Let AI intelligently decide when to search based on the query context
* **Disable Search** - Turn off web search completely for specific requests

<Info>
  Search control features (`enable_search_classifier` and `disable_search`) are currently only available in the Chat Completions API.
</Info>

<Warning>
  Pricing remains the same regardless of whether search is triggered or not. Search control features are designed for performance optimization and user experience, not cost reduction.
</Warning>

## Search Classifier

The search classifier is a trained model that automatically determines whether a web search is necessary based on the context and content of your query. This helps optimize performance and costs by only searching when beneficial.

### How It Works

The classifier analyzes your query and decides whether:

* **Search is needed** - For questions requiring current information, facts, or research
* **Search is unnecessary** - For creative tasks, math problems, or general knowledge that doesn't require real-time data

### When to Use Search Classifier

Use the search classifier when you want to:

* **Improve response speed** - Skip search for queries that don't benefit from it
* **Automatic intelligence** - Let AI decide the best approach for each query
* **Optimal user experience** - Ensure search is only used when it adds value

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import requests

    # API configuration
    API_URL = "https://api.perplexity.ai/chat/completions"
    API_KEY = "your-api-key-here"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }

    # Query that benefits from search classifier
    user_query = "What are the latest developments in quantum computing?"

    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": user_query}],
        "stream": False,
        "enable_search_classifier": True
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    print(response.json())
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    interface ChatCompletionRequest {
      model: string;
      messages: Array<{role: string; content: string}>;
      stream?: boolean;
      enable_search_classifier?: boolean;
    }

    const API_URL = "https://api.perplexity.ai/chat/completions";
    const API_KEY = "your-api-key-here";

    const headers = {
      "accept": "application/json",
      "authorization": `Bearer ${API_KEY}`,
      "content-type": "application/json"
    };

    // Query that benefits from search classifier
    const userQuery = "What are the latest developments in quantum computing?";

    const payload: ChatCompletionRequest = {
      model: "sonar-pro",
      messages: [{role: "user", content: userQuery}],
      stream: false,
      enable_search_classifier: true
    };

    fetch(API_URL, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log(data));
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.perplexity.ai/chat/completions" \
      -H "accept: application/json" \
      -H "authorization: Bearer $SONAR_API_KEY" \
      -H "content-type: application/json" \
      -d '{
        "model": "sonar",
        "messages": [
          {
            "role": "user", 
            "content": "What is 2+2?"
          }
        ],
        "stream": false,
        "enable_search_classifier": true
      }' | jq
    ```
  </Tab>
</Tabs>

### Search Classifier Examples

<AccordionGroup>
  <Accordion title="Queries that typically trigger search">
    * "What happened in the stock market today?"
    * "Latest news about renewable energy"
    * "Current weather in San Francisco"
    * "Recent research on machine learning"
  </Accordion>

  <Accordion title="Queries that typically skip search">
    * "What is 2 + 2?"
    * "Write a creative story about a dragon"
    * "Explain the concept of recursion"
    * "Generate a business name for a bakery"
  </Accordion>
</AccordionGroup>

## Disabling Search Completely

For certain use cases, you may want to disable web search entirely. This is useful when:

* **Offline-like responses** - Get responses based only on training data
* **Creative tasks** - Focus on generation without external influence
* **Deterministic responses** - Ensure consistent outputs based only on training data

### Implementation

To disable search completely, set the `disable_search` parameter to `true`:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import requests

    # API configuration
    API_URL = "https://api.perplexity.ai/chat/completions"
    API_KEY = "your-api-key-here"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }

    # Query that doesn't need web search
    user_query = "What is 2 + 2?"

    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": user_query}],
        "stream": False,
        "disable_search": True
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    print(response.json())
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    interface ChatCompletionRequest {
      model: string;
      messages: Array<{role: string; content: string}>;
      stream?: boolean;
      disable_search?: boolean;
    }

    const API_URL = "https://api.perplexity.ai/chat/completions";
    const API_KEY = "your-api-key-here";

    const headers = {
      "accept": "application/json",
      "authorization": `Bearer ${API_KEY}`,
      "content-type": "application/json"
    };

    // Query that doesn't need web search
    const userQuery = "What is 2 + 2?";

    const payload: ChatCompletionRequest = {
      model: "sonar-pro",
      messages: [{role: "user", content: userQuery}],
      stream: false,
      disable_search: true
    };

    fetch(API_URL, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log(data));
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={null}
    curl -X POST "https://api.perplexity.ai/chat/completions" \
      -H "accept: application/json" \
      -H "authorization: Bearer your-api-key-here" \
      -H "content-type: application/json" \
      -d '{
        "model": "sonar-pro",
        "messages": [
          {
            "role": "user", 
            "content": "What is 2 + 2?"
          }
        ],
        "stream": false,
        "disable_search": true
      }'
    ```
  </Tab>
</Tabs>

<Warning>
  When search is disabled, responses will be based solely on the model's training data and may not include the most current information.
</Warning>

## Comparison and Best Practices

### When to Use Each Approach

<CardGroup cols={2}>
  <Card title="Search Classifier" icon="brain">
    **Best for:**

    * Mixed workloads with varying query types
    * Performance optimization without manual intervention
    * General-purpose applications
    * Unknown query patterns
  </Card>

  <Card title="Disabled Search" icon="ban">
    **Best for:**

    * Creative content generation
    * Mathematical computations
    * Sensitive data processing
    * Offline-like experiences
  </Card>
</CardGroup>

### Performance Considerations

<Tabs>
  <Tab title="Response Time">
    **Search Classifier:** Variable response time depending on whether search is triggered

    **Disabled Search:** Consistently faster responses since no search operations occur
  </Tab>

  <Tab title="Information Accuracy">
    **Search Classifier:** Provides current information when search is triggered

    **Disabled Search:** Limited to training data cutoff date
  </Tab>
</Tabs>

## Complete Examples

### Search Classifier in Action

<Steps>
  <Step title="Set up the request with search classifier">
    ```python  theme={null}
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": "Explain machine learning"}],
        "enable_search_classifier": True
    }
    ```

    <Info>
      The classifier will likely skip search for this general concept explanation.
    </Info>
  </Step>

  <Step title="Try with a current events query">
    ```python  theme={null}
    payload = {
        "model": "sonar-pro", 
        "messages": [{"role": "user", "content": "Latest AI news this week"}],
        "enable_search_classifier": True
    }
    ```

    <Check>
      The classifier will trigger search for this time-sensitive query.
    </Check>
  </Step>
</Steps>

### Creative Task with Disabled Search

Here's an example of using disabled search for creative content generation:

```python  theme={null}
import requests

payload = {
    "model": "sonar-pro",
    "messages": [
        {
            "role": "user",
            "content": "Write a short science fiction story about time travel"
        }
    ],
    "disable_search": True
}

response = requests.post(
    "https://api.perplexity.ai/chat/completions",
    headers={
        "authorization": "Bearer your-api-key-here",
        "content-type": "application/json"
    },
    json=payload
)
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Search classifier not working as expected">
    **Common causes:**

    * API key doesn't have access to classifier features
    * Using an unsupported model
    * Incorrect parameter syntax

    **Solutions:**

    * Verify your API key permissions
    * Ensure you're using a Sonar model
    * Check parameter spelling: `enable_search_classifier`
  </Accordion>

  <Accordion title="Responses seem outdated with disabled search">
    This is expected behavior when search is disabled. The model can only use information from its training data.

    **Solutions:**

    * Re-enable search for queries requiring current information
    * Use search classifier for automatic optimization
    * Clearly document when search is disabled for your users
  </Accordion>
</AccordionGroup>

<Tip>
  Start with the search classifier for most applications, then selectively disable search for specific use cases where you want guaranteed offline-like behavior.
</Tip>