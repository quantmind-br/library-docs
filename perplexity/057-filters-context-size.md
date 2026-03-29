---
title: Search Context Size
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/context-size.md
source: llms
fetched_at: 2026-02-04T07:23:17.76412823-03:00
rendered_js: false
word_count: 399
summary: This document explains how to use the search_context_size parameter in the Chat Completions API to control the volume of web search results for balancing response cost and depth.
tags:
    - search-context-size
    - web-search-options
    - api-configuration
    - cost-optimization
    - grounded-llms
    - chat-completions
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Context Size

<Note>
  The `search_context_size` parameter allows you to control how much search context is retrieved from the web during query resolution, letting you balance cost and comprehensiveness.
</Note>

<Info>
  The `search_context_size` feature is currently only available in the Chat Completions API.
</Info>

<Warning>
  * Default `search_context_size` is `low`
  * Selecting `"high"` increases search costs due to more extensive web retrieval. Use `"low"` when cost efficiency is critical.
</Warning>

## Overview

The `search_context_size` field—passed via the `web_search_options` object—determines how much search context is retrieved by Grounded LLMs. This setting can help you optimize for either:

* Cost savings with minimal search input (`low`)
* Comprehensive answers by maximizing retrieved information (`high`)
* A balance of both (`medium`)

This flexibility allows teams to tune their API usage to their budget and use case.

To enable this feature, include the web\_search\_options.search\_context\_size parameter in your request payload:

```bash  theme={null}
"web_search_options": {
  "search_context_size": "low"
}
```

## Best Practices

**Choosing the Right Context Size**

* `low`: The default and best suited for general use cases. Best for short factual queries or when operating under strict token cost constraints.
* `medium`: Balanced cost/quality tradeoff for more comprehensive answers.
* `high`: Use for deep research, exploratory questions, or when citations and evidence coverage are critical.

**Cost Optimization**

* Selecting `low` or `medium` can significantly reduce overall token usage, especially at scale.
* Consider defaulting to `low` for high-volume endpoints and selectively upgrading to `high` for complex user prompts.

Combining with Other Filters

* You can use `search_context_size` alongside other features like `search_domain_filter` to further control the scope of search.
* Combining `medium` with a focused domain filter often gives a good tradeoff between quality and cost.

Performance Considerations

* Larger context sizes may slightly increase response latency due to more extensive search and reranking.
* If you’re batching queries or supporting real-time interfaces, test with different settings to balance user experience and runtime.

## Examples

**1. Minimal Search Context ("low")**

This option limits the search context retrieved for the model, reducing cost per request while still producing useful responses for simpler questions.

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [
        {
          "role": "system",
          "content": "Be precise and concise."
        },
        {
          "role": "user",
          "content": "How many stars are there in our galaxy?"
        }
      ],
      "web_search_options": {
        "search_context_size": "low"
      }
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[
          {"role": "system", "content": "Be precise and concise."},
          {"role": "user", "content": "How many stars are there in our galaxy?"}
      ],
      web_search_options={
          "search_context_size": "low"
      }
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [
      {"role": "system", "content": "Be precise and concise."},
      {"role": "user", "content": "How many stars are there in our galaxy?"}
    ],
    web_search_options: {
      "search_context_size": "low"
    }
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

**Pro-tip**: Use `low` when cost optimization is more important than answer completeness.

**2. Comprehensive Search Context ("high")**

This option maximizes the amount of search context used to answer the question, resulting in more thorough and nuanced responses.

## Request

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [
        {
          "role": "system",
          "content": "Be precise and concise."
        },
        {
          "role": "user",
          "content": "Explain the economic causes of the 2008 financial crisis."
        }
      ],
      "web_search_options": {
        "search_context_size": "high"
      }
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[
          {"role": "system", "content": "Be precise and concise."},
          {"role": "user", "content": "Explain the economic causes of the 2008 financial crisis."}
      ],
      web_search_options={
          "search_context_size": "high"
      }
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [
      {"role": "system", "content": "Be precise and concise."},
      {"role": "user", "content": "Explain the economic causes of the 2008 financial crisis."}
    ],
    web_search_options: {
      "search_context_size": "high"
    }
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

**Pro-tip**: Use `high` for research-heavy or nuanced queries where coverage matters more than cost.

⸻