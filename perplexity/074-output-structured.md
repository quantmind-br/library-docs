---
title: Structured Outputs Guide
url: https://docs.perplexity.ai/docs/grounded-llm/output-control/structured-outputs.md
source: llms
fetched_at: 2026-02-04T07:24:06.86255275-03:00
rendered_js: false
word_count: 563
summary: This document explains how to use the structured outputs feature to enforce specific JSON Schema formats in model responses for consistent, machine-readable data integration.
tags:
    - structured-outputs
    - json-schema
    - perplexity-api
    - api-configuration
    - machine-readable-data
    - response-format
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Structured Outputs Guide

## Overview

Structured outputs enable you to enforce specific response formats from Perplexity's models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.

We currently support **JSON Schema** structured outputs. To enable structured outputs, add a `response_format` field to your request with the following structure:

```json  theme={null}
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "your_schema_name",
      "schema": { /* your JSON schema object */ }
    }
  }
}
```

The `name` field is required and must be 1-64 alphanumeric characters. The schema should be a valid JSON schema object. LLM responses will match the specified format unless the output exceeds `max_tokens`.

<Tip>
  **Improve Schema Compliance**: Give the LLM some hints about the output format in your prompts to improve adherence to the structured format.

  For example, include phrases like "Please return the data as a JSON object with the following structure..." or "Extract the information and format it as specified in the schema."
</Tip>

<Info>
  The first request with a new JSON Schema expects to incur delay on the first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may result in timeout errors. Once the schema has been prepared, the subsequent requests will not see such delay.
</Info>

## Examples

### 1. Financial Analysis

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from typing import List, Optional
      from pydantic import BaseModel

      class FinancialMetrics(BaseModel):
          company: str
          quarter: str
          revenue: float
          net_income: float
          eps: float
          revenue_growth_yoy: Optional[float] = None
          key_highlights: Optional[List[str]] = None

      client = Perplexity()

      response = client.responses.create(
          preset="pro-search",
          input="Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.",
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "name": "financial_metrics",
                  "schema": FinancialMetrics.model_json_schema()
              }
          }
      )


      metrics = FinancialMetrics.model_validate_json(response.output_text)
      print(f"Revenue: ${metrics.revenue}B")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface FinancialMetrics {
        company: string;
        quarter: string;
        revenue: number;
        net_income: number;
        eps: number;
        revenue_growth_yoy?: number;
        key_highlights?: string[];
      }

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: 'pro-search',
        input: 'Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.',
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'financial_metrics',
            schema: {
              type: 'object',
              properties: {
                company: { type: 'string' },
                quarter: { type: 'string' },
                revenue: { type: 'number' },
                net_income: { type: 'number' },
                eps: { type: 'number' },
                revenue_growth_yoy: { type: 'number' },
                key_highlights: {
                  type: 'array',
                  items: { type: 'string' }
                }
              },
              required: ['company', 'quarter', 'revenue', 'net_income', 'eps']
            }
          }
        }
      });

      const metrics: FinancialMetrics = JSON.parse(response.output_text);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "pro-search",
          "input": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.",
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "name": "financial_metrics",
              "schema": {
                "type": "object",
                "properties": {
                  "company": {"type": "string"},
                  "quarter": {"type": "string"},
                  "revenue": {"type": "number"},
                  "net_income": {"type": "number"},
                  "eps": {"type": "number"},
                  "revenue_growth_yoy": {"type": "number"},
                  "key_highlights": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                },
                "required": ["company", "quarter", "revenue", "net_income", "eps"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from typing import List, Optional
      from pydantic import BaseModel

      class FinancialMetrics(BaseModel):
          company: str
          quarter: str
          revenue: float
          net_income: float
          eps: float
          revenue_growth_yoy: Optional[float] = None
          key_highlights: Optional[List[str]] = None

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar-pro",
          messages=[
              {
                  "role": "user",
                  "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."
              }
          ],
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "schema": FinancialMetrics.model_json_schema()
              }
          }
      )

      metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
      print(f"Revenue: ${metrics.revenue}B")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface FinancialMetrics {
        company: string;
        quarter: string;
        revenue: number;
        net_income: number;
        eps: number;
        revenue_growth_yoy?: number;
        key_highlights?: string[];
      }

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: 'sonar-pro',
        messages: [
          {
            role: 'user',
            content: 'Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics.'
          }
        ],
        response_format: {
          type: 'json_schema',
          json_schema: {
            schema: {
              type: 'object',
              properties: {
                company: { type: 'string' },
                quarter: { type: 'string' },
                revenue: { type: 'number' },
                net_income: { type: 'number' },
                eps: { type: 'number' },
                revenue_growth_yoy: { type: 'number' },
                key_highlights: {
                  type: 'array',
                  items: { type: 'string' }
                }
              },
              required: ['company', 'quarter', 'revenue', 'net_income', 'eps']
            }
          }
        }
      });

      const metrics: FinancialMetrics = JSON.parse(completion.choices[0].message.content);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar-pro",
          "messages": [
            {
              "role": "user", 
              "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."
            }
          ],
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "schema": {
                "type": "object",
                "properties": {
                  "company": {"type": "string"},
                  "quarter": {"type": "string"},
                  "revenue": {"type": "number"},
                  "net_income": {"type": "number"},
                  "eps": {"type": "number"},
                  "revenue_growth_yoy": {"type": "number"},
                  "key_highlights": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                },
                "required": ["company", "quarter", "revenue", "net_income", "eps"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### 2. Extract Contact Information

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from pydantic import BaseModel

      class ContactInfo(BaseModel):
          email: str

      client = Perplexity()

      response = client.responses.create(
          preset="fast-search",
          input="Find the direct email address for the investor relations contact at Tesla Inc.",
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "name": "contact_info",
                  "schema": ContactInfo.model_json_schema()
              }
          }
      )


      contact = ContactInfo.model_validate_json(response.output_text)
      print(f"Investor Relations Email: {contact.email}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface ContactInfo {
        email: string;
      }

      const client = new Perplexity();

      const response = await client.responses.create({
        preset: 'fast-search',
        input: 'Find the direct email address for the investor relations contact at Tesla Inc.',
        response_format: {
          type: 'json_schema',
          json_schema: {
            name: 'contact_info',
            schema: {
              type: 'object',
              properties: {
                email: { type: 'string' }
              },
              required: ['email']
            }
          }
        }
      });

      const contact: ContactInfo = JSON.parse(response.output_text);
      console.log(`Investor Relations Email: ${contact.email}`);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "fast-search",
          "input": "Find the direct email address for the investor relations contact at Tesla Inc.",
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "name": "contact_info",
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string"}
                },
                "required": ["email"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python theme={null}
      from perplexity import Perplexity
      from pydantic import BaseModel

      class ContactInfo(BaseModel):
          email: str

      client = Perplexity()

      completion = client.chat.completions.create(
          model="sonar",
          messages=[
              {
                  "role": "user",
                  "content": "Find the direct email address for the investor relations contact at Tesla Inc."
              }
          ],
          response_format={
              "type": "json_schema",
              "json_schema": {
                  "schema": ContactInfo.model_json_schema()
              }
          }
      )

      contact = ContactInfo.model_validate_json(completion.choices[0].message.content)
      print(f"Investor Relations Email: {contact.email}")
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      interface ContactInfo {
        email: string;
      }

      const client = new Perplexity();

      const completion = await client.chat.completions.create({
        model: 'sonar',
        messages: [
          {
            role: 'user',
            content: 'Find the direct email address for the investor relations contact at Tesla Inc.'
          }
        ],
        response_format: {
          type: 'json_schema',
          json_schema: {
            schema: {
              type: 'object',
              properties: {
                email: { type: 'string' }
              },
              required: ['email']
            }
          }
        }
      });

      const contact: ContactInfo = JSON.parse(completion.choices[0].message.content);
      console.log(`Investor Relations Email: ${contact.email}`);
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar",
          "messages": [
            {
              "role": "user",
              "content": "Find the direct email address for the investor relations contact at Tesla Inc."
            }
          ],
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "schema": {
                "type": "object",
                "properties": {
                  "email": {"type": "string"}
                },
                "required": ["email"]
              }
            }
          }
        }' | jq
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Best Practices

### Generating responses in a JSON Format

For Python users, we recommend using the Pydantic library to [generate JSON schema](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema).

### Unsupported JSON Schemas

Recursive JSON schema is not supported. As a result of that, unconstrained objects are not supported either. Here are a few examples of unsupported schemas:

```
# UNSUPPORTED!

from typing import Any

class UnconstrainedDict(BaseModel):
   unconstrained: dict[str, Any]

class RecursiveJson(BaseModel):
   value: str
   child: list["RecursiveJson"]
```

<Warning>
  **Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably and can result in hallucinations or broken links. Models may generate invalid URLs when forced to include links directly in structured outputs.

  To ensure all links are valid, use the links returned in the `citations` or `search_results` fields from the API response. Never count on the model to return valid links directly as part of the JSON response content.
</Warning>

## Perplexity's JSON Schema Implementation

Perplexity's structured outputs implementation has several key differences compared to other providers:

### Simplified Schema Definition

* **Optional naming**: Unlike other providers that require explicit schema names, Perplexity automatically handles schema naming with sensible defaults
* **Flexible strictness**: Schema validation is handled automatically without requiring manual strictness configuration
* **Streamlined syntax**: You only need to provide the core schema object without additional wrapper fields

**Other Providers:**

```json  theme={null}
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "financial_data",
      "strict": true,
      "schema": { /* your schema */ }
    }
  }
}
```

**Perplexity:**

```json  theme={null}
{
  "response_format": {
    "type": "json_schema", 
    "json_schema": {
      "schema": { /* your schema */ }
    }
  }
}
```

### Enhanced Error Handling

* **Clear error messages**: When schemas fail validation, you'll receive specific, actionable error messages
* **Recursion protection**: Built-in safeguards prevent infinite recursion in complex nested schemas
* **Constraint validation**: Automatic detection and clear messaging for unsupported features like unconstrained objects

### Schema Compatibility

While Perplexity supports standard JSON Schema syntax, some advanced features may not be available:

* Recursive schemas are not supported for performance and reliability reasons
* Unconstrained objects (like `dict[str, Any]`) are automatically detected and rejected
* Complex reference patterns may require simplification

This approach prioritizes reliability and performance while maintaining compatibility with most common JSON Schema use cases.

## Structured Outputs for Reasoning Models

When using structured outputs with reasoning models like `sonar-reasoning-pro`, the response will include a `<think>` section containing reasoning tokens, immediately followed by the structured output. The `response_format` parameter does not remove these reasoning tokens from the output, so the final response will need to be parsed manually.

**Sample Response:**

```
<think>
I need to provide information about France in a structured JSON format with specific fields: country, capital, population, official_language.

For France:
- Country: France
- Capital: Paris
- Population: About 67 million (as of 2023)
- Official Language: French

Let me format this information as required.
</think>
{"country":"France","capital":"Paris","population":67750000,"official_language":"French"}
```

For a reusable implementation to extract JSON from reasoning model outputs, see our [example utility on GitHub](https://github.com/perplexityai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).