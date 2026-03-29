---
title: Function Calling
url: https://docs.perplexity.ai/docs/grounded-llm/responses/tools/function-calling.md
source: llms
fetched_at: 2026-02-04T07:24:26.140333368-03:00
rendered_js: false
word_count: 800
summary: This document explains how to define and implement custom functions that allow AI models to interact with external databases and APIs via the Agentic Research API. It covers the multi-turn interaction cycle, function schema definitions, and strict validation mode for reliable integration.
tags:
    - function-calling
    - agentic-api
    - json-schema
    - api-integration
    - tool-use
    - perplexity-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Function Calling

> Define custom functions that models can call to interact with external systems, databases, and APIs through the Agentic Research API.

## Overview

Function calling allows you to define custom functions that models can invoke during a conversation. Unlike the built-in tools (`web_search` and `fetch_url`), custom functions let you connect the model to your own systems—databases, APIs, business logic, or any external service.

<CardGroup cols={2}>
  <Card title="Custom Integrations" icon="plug">
    Connect models to your databases, APIs, and internal systems.
  </Card>

  <Card title="Multi-Turn Pattern" icon="arrows-rotate">
    Model requests a function call, you execute it, then return results.
  </Card>
</CardGroup>

<Info>
  **Built-in vs Custom Tools:** Use `web_search` and `fetch_url` for web information retrieval. Use function calling when you need the model to interact with your own systems or perform custom operations.
</Info>

## How It Works

Function calling follows a multi-turn conversation pattern:

<Steps>
  <Step title="Define Functions">
    Specify the functions available to the model, including their names, descriptions, and parameter schemas.
  </Step>

  <Step title="Send Initial Request">
    Send your prompt along with the function definitions. The model decides if and when to call a function.
  </Step>

  <Step title="Receive Function Call">
    If the model needs to call a function, it returns a `function_call` item in the response output with the function name and arguments.
  </Step>

  <Step title="Execute the Function">
    Your code executes the actual function logic using the provided arguments.
  </Step>

  <Step title="Return Results">
    Send the function output back to the model as a `function_call_output` item.
  </Step>

  <Step title="Get Final Response">
    The model uses the function results to generate its final response.
  </Step>
</Steps>

## Defining Functions

Define functions using the `tools` parameter with `type: "function"`. Each function needs a name, description, and a JSON Schema for its parameters.

```python  theme={null}
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name, e.g., 'San Francisco'"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit"
                }
            },
            "required": ["location"]
        }
    }
]
```

### Function Schema Properties

| Property      | Type    | Required | Description                                                    |
| ------------- | ------- | -------- | -------------------------------------------------------------- |
| `type`        | string  | Yes      | Must be `"function"`                                           |
| `name`        | string  | Yes      | Function name the model will use to call it                    |
| `description` | string  | Yes      | Clear description of what the function does and when to use it |
| `parameters`  | object  | Yes      | JSON Schema defining the function's parameters                 |
| `strict`      | boolean | No       | Enable strict schema validation                                |

<Tip>
  Write clear, specific descriptions. The model uses these to decide when to call each function. Include details about what the function returns and any constraints.
</Tip>

### Strict Mode

Setting `strict: true` ensures function calls reliably adhere to your schema. When enabled, the model will always include all required parameters with the correct types.

```python  theme={null}
{
    "type": "function",
    "name": "get_weather",
    "description": "Get weather for a location",
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City name"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
            }
        },
        "required": ["location", "unit"],
        "additionalProperties": False
    }
}
```

When using strict mode:

* Set `additionalProperties: false` on your parameter object
* Mark all fields in `properties` as `required`
* Use `"type": ["string", "null"]` for optional fields that can be null

<Info>
  Strict mode is recommended for production applications where consistent function call structure is important.
</Info>

## Basic Example

Here's a complete example showing the full function calling flow:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import json

  client = Perplexity()

  # 1. Define your function tools
  tools = [
      {
          "type": "function",
          "name": "get_horoscope",
          "description": "Get today's horoscope for an astrological sign.",
          "parameters": {
              "type": "object",
              "properties": {
                  "sign": {
                      "type": "string",
                      "description": "An astrological sign like Taurus or Aquarius"
                  }
              },
              "required": ["sign"]
          }
      }
  ]

  # Your actual function implementation
  def get_horoscope(sign: str) -> str:
      # In a real app, this might call an external API
      return f"{sign}: Today brings new opportunities for growth."

  # 2. Send initial request with tools
  response = client.responses.create(
      model="openai/gpt-5.2",
      tools=tools,
      input="What is my horoscope? I am an Aquarius."
  )

  # 3. Process the response and handle function calls
  next_input = [item.model_dump() for item in response.output]

  for item in response.output:
      if item.type == "function_call":
          # 4. Execute the function
          args = json.loads(item.arguments)
          result = get_horoscope(args["sign"])

          # 5. Add the function result to the input
          next_input.append({
              "type": "function_call_output",
              "call_id": item.call_id,
              "output": json.dumps({"horoscope": result})
          })

  # 6. Send the function results back to get the final response
  final_response = client.responses.create(
      model="openai/gpt-5.2",
      input=next_input
  )

  print(final_response.output_text)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // 1. Define your function tools
  const tools = [
      {
          type: "function" as const,
          name: "get_horoscope",
          description: "Get today's horoscope for an astrological sign.",
          parameters: {
              type: "object",
              properties: {
                  sign: {
                      type: "string",
                      description: "An astrological sign like Taurus or Aquarius"
                  }
              },
              required: ["sign"]
          }
      }
  ];

  // Your actual function implementation
  function getHoroscope(sign: string): string {
      return `${sign}: Today brings new opportunities for growth.`;
  }

  // 2. Send initial request with tools
  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      tools: tools,
      input: "What is my horoscope? I am an Aquarius."
  });

  // 3. Process the response and handle function calls
  const nextInput: any[] = response.output.map(item => ({ ...item }));

  for (const item of response.output) {
      if (item.type === "function_call") {
          // 4. Execute the function
          const args = JSON.parse(item.arguments);
          const result = getHoroscope(args.sign);

          // 5. Add the function result to the input
          nextInput.push({
              type: "function_call_output",
              call_id: item.call_id,
              output: JSON.stringify({ horoscope: result })
          });
      }
  }

  // 6. Send the function results back to get the final response
  const finalResponse = await client.responses.create({
      model: "openai/gpt-5.2",
      input: nextInput
  });

  console.log(finalResponse.output_text);
  ```

  ```bash cURL theme={null}
  # Step 1: Initial request with function tools
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": "What is my horoscope? I am an Aquarius.",
      "tools": [
        {
          "type": "function",
          "name": "get_horoscope",
          "description": "Get today'\''s horoscope for an astrological sign.",
          "parameters": {
            "type": "object",
            "properties": {
              "sign": {
                "type": "string",
                "description": "An astrological sign like Taurus or Aquarius"
              }
            },
            "required": ["sign"]
          }
        }
      ]
    }'

  # Step 2: After receiving a function_call, send the result back
  # (Replace call_id with the actual value from the response)
  curl https://api.perplexity.ai/v1/responses \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.2",
      "input": [
        {
          "type": "function_call",
          "call_id": "call_abc123",
          "name": "get_horoscope",
          "arguments": "{\"sign\": \"Aquarius\"}"
        },
        {
          "type": "function_call_output",
          "call_id": "call_abc123",
          "output": "{\"horoscope\": \"Aquarius: Today brings new opportunities for growth.\"}"
        }
      ]
    }'
  ```
</CodeGroup>

## Handling Function Calls

When the model decides to call a function, the response contains a `function_call` item in the `output` array:

```json  theme={null}
{
  "output": [
    {
      "type": "function_call",
      "call_id": "call_abc123",
      "name": "get_horoscope",
      "arguments": "{\"sign\": \"Aquarius\"}"
    }
  ]
}
```

### Function Call Properties

| Property    | Description                                                     |
| ----------- | --------------------------------------------------------------- |
| `type`      | Always `"function_call"`                                        |
| `call_id`   | Unique identifier for this call—use this when returning results |
| `name`      | The function name the model is calling                          |
| `arguments` | JSON string containing the function arguments                   |

<Warning>
  The `arguments` field is a JSON string, not a parsed object. Always use `json.loads()` (Python) or `JSON.parse()` (JavaScript) to parse it.
</Warning>

## Returning Function Results

After executing the function, return the results using `function_call_output`:

```python  theme={null}
{
    "type": "function_call_output",
    "call_id": "call_abc123",  # Must match the original call_id
    "output": "{\"horoscope\": \"Aquarius: Today brings new opportunities.\"}"
}
```

### Function Output Properties

| Property  | Description                                          |
| --------- | ---------------------------------------------------- |
| `type`    | Must be `"function_call_output"`                     |
| `call_id` | The `call_id` from the corresponding `function_call` |
| `output`  | JSON string containing the function's return value   |

<Tip>
  Structure your output as JSON for consistency. The model will parse and use this data to formulate its response.
</Tip>

## Multiple Functions

You can define multiple functions for the model to choose from:

<CodeGroup>
  ```python Python theme={null}
  tools = [
      {
          "type": "function",
          "name": "get_weather",
          "description": "Get current weather for a location.",
          "parameters": {
              "type": "object",
              "properties": {
                  "location": {"type": "string", "description": "City name"}
              },
              "required": ["location"]
          }
      },
      {
          "type": "function",
          "name": "get_stock_price",
          "description": "Get current stock price for a ticker symbol.",
          "parameters": {
              "type": "object",
              "properties": {
                  "ticker": {"type": "string", "description": "Stock ticker symbol"}
              },
              "required": ["ticker"]
          }
      }
  ]

  response = client.responses.create(
      model="openai/gpt-5.2",
      tools=tools,
      input="What's the weather in NYC and the current price of AAPL?"
  )

  # Handle each function call in the response
  for item in response.output:
      if item.type == "function_call":
          if item.name == "get_weather":
              # Execute weather function
              pass
          elif item.name == "get_stock_price":
              # Execute stock price function
              pass
  ```

  ```typescript TypeScript theme={null}
  const tools = [
      {
          type: "function" as const,
          name: "get_weather",
          description: "Get current weather for a location.",
          parameters: {
              type: "object",
              properties: {
                  location: { type: "string", description: "City name" }
              },
              required: ["location"]
          }
      },
      {
          type: "function" as const,
          name: "get_stock_price",
          description: "Get current stock price for a ticker symbol.",
          parameters: {
              type: "object",
              properties: {
                  ticker: { type: "string", description: "Stock ticker symbol" }
              },
              required: ["ticker"]
          }
      }
  ];

  const response = await client.responses.create({
      model: "openai/gpt-5.2",
      tools: tools,
      input: "What's the weather in NYC and the current price of AAPL?"
  });

  // Handle each function call in the response
  for (const item of response.output) {
      if (item.type === "function_call") {
          if (item.name === "get_weather") {
              // Execute weather function
          } else if (item.name === "get_stock_price") {
              // Execute stock price function
          }
      }
  }
  ```
</CodeGroup>

## Combining with Built-in Tools

You can use custom functions alongside built-in tools like `web_search`:

```python  theme={null}
tools = [
    {"type": "web_search"},
    {
        "type": "function",
        "name": "save_to_database",
        "description": "Save information to the user's database.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "Data to save"}
            },
            "required": ["data"]
        }
    }
]

response = client.responses.create(
    model="openai/gpt-5.2",
    tools=tools,
    input="Search for the latest AI news and save a summary to my database.",
    instructions="Use web_search to find information, then save_to_database to store it."
)
```

## Best Practices

### Write Clear Descriptions

The model relies on function descriptions to decide when to call them. Be specific:

```python  theme={null}
# Good - clear and specific
{
    "name": "get_user_orders",
    "description": "Retrieve a user's order history from the database. Returns the last 10 orders including order ID, date, items, and total amount. Use this when the user asks about their past purchases or order status."
}

# Less effective - vague
{
    "name": "get_orders",
    "description": "Gets orders."
}
```

### Define Precise Parameter Schemas

Use JSON Schema features to constrain parameters:

```python  theme={null}
"parameters": {
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "enum": ["pending", "shipped", "delivered"],
            "description": "Filter orders by status"
        },
        "limit": {
            "type": "integer",
            "minimum": 1,
            "maximum": 100,
            "default": 10,
            "description": "Number of orders to return"
        }
    },
    "required": ["status"]
}
```

### Handle Errors Gracefully

Return error information in a structured way:

```python  theme={null}
try:
    result = execute_function(args)
    output = json.dumps({"success": True, "data": result})
except Exception as e:
    output = json.dumps({"success": False, "error": str(e)})

next_input.append({
    "type": "function_call_output",
    "call_id": item.call_id,
    "output": output
})
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Web Search" icon="magnifying-glass" href="/docs/grounded-llm/responses/tools/web-search">
    Use web\_search for real-time web information.
  </Card>

  <Card title="Fetch URL" icon="globe" href="/docs/grounded-llm/responses/tools/fetch-url">
    Extract content from specific URLs.
  </Card>

  <Card title="Structured Outputs" icon="code" href="/docs/grounded-llm/output-control/structured-outputs">
    Control response format with JSON schemas.
  </Card>

  <Card title="API Reference" icon="book" href="/api-reference/responses-post">
    View complete endpoint documentation.
  </Card>
</CardGroup>