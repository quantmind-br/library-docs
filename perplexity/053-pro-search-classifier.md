---
title: Pro Search Classifier
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/pro-search/classifier.md
source: llms
fetched_at: 2026-02-04T07:23:36.311820937-03:00
rendered_js: false
word_count: 511
summary: This document explains how the Pro Search Classifier automatically routes queries to either Pro Search or Fast Search modes based on complexity and research needs. It outlines the decision-making process and how this optimization balances performance with API cost efficiency.
tags:
    - search-optimization
    - query-classification
    - perplexity-api
    - cost-management
    - pro-search
    - fast-search
category: concept
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pro Search Classifier

> Optimize cost and performance with automatic query classification between Pro Search and Fast Search modes

## Overview

The Pro Search Classifier is an intelligent system that automatically determines whether a query requires the advanced multi-step tool usage of Pro Search or can be effectively answered with standard Fast Search. This optimization helps you balance performance needs with cost efficiency.

<Info>
  Instead of manually choosing between `"pro"` and `"fast"` search types, you can use `"auto"` to let the classifier make the optimal decision for each query.
</Info>

## How It Works

When you set `search_type: "auto"`, the classifier analyzes your query across multiple dimensions:

<Steps>
  <Step title="Query Complexity Analysis">
    The classifier evaluates:

    * Number of sub-questions or aspects
    * Requirement for comparative analysis
    * Need for multi-step reasoning
    * Complexity of information synthesis required

    ```json  theme={null}
    {
      "web_search_options": {
        "search_type": "auto"  // Let the classifier decide
      }
    }
    ```
  </Step>

  <Step title="Classification Decision">
    Based on the analysis, the classifier routes the query to either:

    * **Pro Search** for complex, multi-faceted queries requiring multi-step tool usage
    * **Fast Search** for straightforward information retrieval

    The decision is transparent in the response metadata.
  </Step>

  <Step title="Execution">
    The selected search mode processes your query:

    * **Pro Search**: Uses built-in tools (web\_search, fetch\_url\_content) automatically
    * **Fast Search**: Performs optimized single-pass search and synthesis

    You receive the same high-quality response format regardless of which mode is used.
  </Step>
</Steps>

## Classification Patterns

### Queries Classified as Pro Search

Complex queries that benefit from multi-step tool usage are automatically routed to Pro Search:

<AccordionGroup>
  <Accordion title="Multi-Part Questions">
    **Example Query:**
    "What are the differences between React, Vue, and Angular in terms of performance, learning curve, and ecosystem? Which one should I choose for a large enterprise application?"

    **Why Pro Search:**

    * Requires information about three different frameworks
    * Needs comparative analysis across multiple dimensions
    * Involves gathering expert opinions and recommendations
    * Benefits from synthesis of diverse sources

    **Tool Usage:**

    * Multiple web searches for each framework
    * URL fetching for benchmark data and official documentation
  </Accordion>

  <Accordion title="Research Synthesis">
    **Example Query:**
    "Summarize the latest peer-reviewed research on the effectiveness of intermittent fasting for weight loss and metabolic health. Include sample sizes and study limitations."

    **Why Pro Search:**

    * Requires finding multiple research papers
    * Needs access to full paper content, not just abstracts
    * Involves extracting specific data (sample sizes, limitations)
    * Requires synthesis across multiple studies

    **Tool Usage:**

    * Web search for recent peer-reviewed papers
    * `fetch_url_content` to read full papers
    * Information extraction and synthesis
  </Accordion>

  <Accordion title="Time-Sensitive Complex Analysis">
    **Example Query:**
    "Analyze the stock market impact of the Federal Reserve's most recent interest rate decision, including effects on different sectors and expert predictions for the next quarter."

    **Why Pro Search:**

    * Requires very recent information
    * Needs multi-source verification
    * Involves sector-by-sector analysis
    * Benefits from expert opinion gathering

    **Tool Usage:**

    * Multiple targeted web searches
    * URL fetching for financial analysis reports
    * Synthesis of diverse expert opinions
  </Accordion>
</AccordionGroup>

### Queries Classified as Fast Search

Straightforward queries that don't require multi-step reasoning are efficiently handled by Fast Search:

<AccordionGroup>
  <Accordion title="Simple Factual Questions">
    **Example Query:**
    "What is the capital of France?"

    **Why Fast Search:**

    * Single, well-established fact
    * No calculation or analysis needed
    * Information readily available in search snippets

    **Processing:**

    * Single web search
    * Direct answer from search results
    * No need for multi-step reasoning
  </Accordion>

  <Accordion title="Straightforward Information Retrieval">
    **Example Query:**
    "What are the main features of the iPhone 15 Pro?"

    **Why Fast Search:**

    * Single product inquiry
    * Information available in product descriptions
    * No comparative analysis required
    * No calculations needed

    **Processing:**

    * Search for product specifications
    * Extract and list features
    * Synthesize from search results
  </Accordion>

  <Accordion title="Single-Topic Queries">
    **Example Query:**
    "Explain what machine learning is."

    **Why Fast Search:**

    * Single concept definition
    * No multi-part analysis required
    * Standard information readily available

    **Processing:**

    * Search for machine learning explanations
    * Synthesize clear definition
    * Provide context from reliable sources
  </Accordion>

  <Accordion title="Basic Definitional Requests">
    **Example Query:**
    "What does API stand for and what is it used for?"

    **Why Fast Search:**

    * Simple definition request
    * No complex analysis needed
    * Information readily available

    **Processing:**

    * Quick search for API definition
    * Explain acronym and basic usage
    * Provide clear, concise answer
  </Accordion>
</AccordionGroup>

## Cost Implications

Understanding the cost difference helps you optimize your API usage:

<div className="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  <div className="bg-card p-6 rounded-lg border border-border">
    <h4 className="font-semibold text-foreground mb-3">Classified as Pro Search</h4>

    <ul className="space-y-2 text-sm text-muted-foreground">
      <li>Complex multi-part questions</li>
      <li>Requests requiring calculation or analysis</li>
      <li>Comparative research across sources</li>
      <li>Time-sensitive information needs</li>
    </ul>

    <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-950 rounded border border-blue-200 dark:border-blue-800">
      <span className="text-sm font-medium text-blue-700 dark:text-blue-300">Uses Pro Search billing rates</span>
    </div>
  </div>

  <div className="bg-card p-6 rounded-lg border border-border">
    <h4 className="font-semibold text-foreground mb-3">Classified as Fast Search</h4>

    <ul className="space-y-2 text-sm text-muted-foreground">
      <li>Simple factual questions</li>
      <li>Straightforward information retrieval</li>
      <li>Single-topic queries</li>
      <li>Basic definitional requests</li>
    </ul>

    <div className="mt-4 p-3 bg-green-50 dark:bg-green-950 rounded border border-green-200 dark:border-green-800">
      <span className="text-sm font-medium text-green-700 dark:text-green-300">Uses standard Sonar Pro billing rates</span>
    </div>
  </div>
</div>

### Pricing Comparison

**Pro Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: $14-$22 per 1,000 requests (based on context size)

**Fast Search Rates:**

* Input: \$3 per 1M tokens
* Output: \$15 per 1M tokens
* Request fees: $6-$14 per 1,000 requests (based on context size - same as standard Sonar Pro)

<Tip>
  The automatic classifier helps you save money by using Pro Search only when its advanced capabilities are truly needed, while still ensuring complex queries get full multi-step tool usage.
</Tip>

## Usage Examples

### Using Automatic Classification

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity(api_key="your-api-key")

  # Let the classifier decide
  response = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
          }
      ],
      stream=True,
      web_search_options={
          "search_type": "auto"  # Automatic classification
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript TypeScript SDK theme={null}
  import { Perplexity } from '@perplexity-ai/sdk';

  const client = new Perplexity({
    apiKey: 'your-api-key'
  });

  // Let the classifier decide
  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'auto'  // Automatic classification
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer your-api-key" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Compare the energy efficiency of Tesla Model 3, Chevrolet Bolt, and Nissan Leaf"
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "auto"
      }
    }' --no-buffer
  ```
</CodeGroup>

### Manual Override

You can still manually specify the search type when you know what you need:

<Tabs>
  <Tab title="Force Pro Search">
    Use when you know you need multi-step tool usage:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your complex query"}],
        stream=True,
        web_search_options={
            "search_type": "pro"  # Force Pro Search
        }
    )
    ```

    **Use cases for manual Pro:**

    * You know the query needs multi-step reasoning
    * Previous auto-classification was Fast but you need deeper analysis
    * Critical queries where you want maximum capability
  </Tab>

  <Tab title="Force Fast Search">
    Use when you want to optimize for speed and cost:

    ```python  theme={null}
    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Your simple query"}],
        stream=True,
        web_search_options={
            "search_type": "fast"  # Force Fast Search (or omit - fast is default)
        }
    )
    ```

    **Use cases for manual Fast:**

    * Simple queries where Pro Search would be overkill
    * Cost-sensitive applications
    * When response speed is critical
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Default to automatic classification">
    For most applications, use `search_type: "auto"` and let the classifier optimize:

    ```python  theme={null}
    web_search_options={"search_type": "auto"}
    ```

    This ensures the right tool for each query while optimizing costs.
  </Step>

  <Step title="Monitor classification patterns">
    Track which queries get classified as Pro vs Fast to understand your usage patterns:

    * Review queries that consistently use Pro Search
    * Identify opportunities to rephrase queries for Fast Search when appropriate
    * Understand which user questions require advanced capabilities

    This helps optimize your application's query design.
  </Step>

  <Step title="Use manual override strategically">
    Override the classifier only when:

    * You have specific performance requirements
    * Testing and comparing Pro vs Fast results
    * Building features with known complexity levels

    **Example:**

    ```python  theme={null}
    # Known complex analysis - force Pro
    if query_requires_calculations(user_query):
        search_type = "pro"
    else:
        search_type = "auto"
    ```
  </Step>

  <Step title="Design queries effectively">
    Structure queries to help the classifier make optimal decisions:

    **Less optimal:**
    "Tell me about electric cars"

    **Better:**
    "What is the average range of electric vehicles?" (Fast Search appropriate)

    **Or:**
    "Compare the total cost of ownership over 5 years for Tesla Model 3, Chevrolet Bolt, and Nissan Leaf, including depreciation, electricity costs, and maintenance" (Pro Search appropriate)

    Clear, specific queries enable better classification.
  </Step>
</Steps>

## Classification Transparency

You can verify the classification decision in the response metadata:

```json  theme={null}
{
  "id": "12345",
  "model": "sonar-pro",
  "search_metadata": {
    "search_type_used": "pro",  // or "fast"
    "classification_reason": "Multi-part comparative analysis with calculations"
  },
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

<Info>
  This transparency helps you understand why queries were classified a certain way and optimize future queries.
</Info>

## When to Use Each Mode

<CardGroup cols={3}>
  <Card title="Auto (Recommended)" icon="wand-magic-sparkles">
    **Best for:** Most applications

    Let the classifier optimize for you. Balances cost and capability automatically based on query complexity.
  </Card>

  <Card title="Manual Pro" icon="brain">
    **Best for:** Known complex tasks

    Use when you're certain multi-step tool usage is needed: calculations, multi-source synthesis, deep analysis.
  </Card>

  <Card title="Manual Fast" icon="bolt">
    **Best for:** Simple retrieval

    Use for straightforward facts, definitions, or when optimizing for speed and cost with simple queries.
  </Card>
</CardGroup>

## Common Questions

<AccordionGroup>
  <Accordion title="How accurate is the classifier?">
    The classifier is highly accurate, trained on thousands of query patterns. It errs on the side of using Pro Search when there's any ambiguity, ensuring you don't lose capability.

    However, if you notice consistent mis-classifications:

    * Rephrase queries to be more specific
    * Use manual override for those query types
    * Consider your use case's specific needs
  </Accordion>

  <Accordion title="Can I see which mode was used?">
    Yes, the response includes metadata showing:

    * Which search type was used
    * Why the classification was made (when using auto)
    * Cost breakdown by search type

    This helps you understand and optimize your usage patterns.
  </Accordion>

  <Accordion title="Does automatic classification add latency?">
    No. Classification happens in milliseconds before query processing begins and does not meaningfully impact response time. The classifier is optimized for real-time decision making.
  </Accordion>

  <Accordion title="What if I disagree with the classification?">
    You can always use manual override:

    ```python  theme={null}
    web_search_options={"search_type": "pro"}  # Force your preference
    ```

    If you consistently disagree with classifications, consider:

    * Making queries more specific
    * Using manual override for those query types
    * Reviewing whether your use case needs consistent Pro or Fast mode
  </Accordion>
</AccordionGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Quickstart" icon="rocket" href="/docs/grounded-llm/chat-completions/pro-search/quickstart">
    Get started with Pro Search basics
  </Card>

  <Card title="Built-in Tool Capabilities" icon="tools" href="/docs/grounded-llm/chat-completions/pro-search/tools">
    Learn about Pro Search's built-in tools and capabilities
  </Card>

  <Card title="Pricing Guide" icon="dollar-sign" href="/docs/getting-started/pricing">
    Understand pricing for Pro and Fast Search
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/chat-completions-post">
    Complete API documentation
  </Card>
</CardGroup>