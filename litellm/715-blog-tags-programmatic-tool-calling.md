---
title: One post tagged with "programmatic tool calling" | liteLLM
url: https://docs.litellm.ai/blog/tags/programmatic-tool-calling
source: sitemap
fetched_at: 2026-01-21T19:40:59.789928193-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to implement tool search and deferred tool loading using LiteLLM with Claude models to handle large toolsets efficiently.
tags:
    - litellm
    - anthropic-claude
    - tool-calling
    - deferred-loading
    - tool-search
    - python
category: tutorial
---

```
import litellm
import os

# Configure your API key
os.environ["ANTHROPIC_API_KEY"]="your-api-key"

# Define your tools with defer_loading
tools =[
# Tool search tool (regex variant)
{
"type":"tool_search_tool_regex_20251119",
"name":"tool_search_tool_regex"
},
# Deferred tools - loaded on-demand
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get the current weather in a given location. Returns temperature and conditions.",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA"
},
"unit":{
"type":"string",
"enum":["celsius","fahrenheit"],
"description":"Temperature unit"
}
},
"required":["location"]
}
},
"defer_loading":True# Load on-demand
},
{
"type":"function",
"function":{
"name":"search_files",
"description":"Search through files in the workspace using keywords",
"parameters":{
"type":"object",
"properties":{
"query":{"type":"string"},
"file_types":{
"type":"array",
"items":{"type":"string"}
}
},
"required":["query"]
}
},
"defer_loading":True
},
{
"type":"function",
"function":{
"name":"query_database",
"description":"Execute SQL queries against the database",
"parameters":{
"type":"object",
"properties":{
"sql":{"type":"string"}
},
"required":["sql"]
}
},
"defer_loading":True
}
]

# Make a request - Claude will search for and use relevant tools
response = litellm.completion(
    model="anthropic/claude-opus-4-5-20251101",
    messages=[{
"role":"user",
"content":"What's the weather like in San Francisco?"
}],
    tools=tools
)

print("Claude's response:", response.choices[0].message.content)
print("Tool calls:", response.choices[0].message.tool_calls)

# Check tool search usage
ifhasattr(response.usage,'server_tool_use'):
print(f"Tool searches performed: {response.usage.server_tool_use.tool_search_requests}")
```