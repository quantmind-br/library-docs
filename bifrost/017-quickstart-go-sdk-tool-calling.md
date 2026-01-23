---
title: Tool Calling
url: https://docs.getbifrost.ai/quickstart/go-sdk/tool-calling.md
source: llms
fetched_at: 2026-01-21T19:45:04.03278844-03:00
rendered_js: false
word_count: 183
summary: This document explains how to enable AI models to interact with external functions and services by defining custom tool schemas or connecting to Model Context Protocol (MCP) servers.
tags:
    - tool-calling
    - mcp
    - function-calling
    - go
    - chat-completion
    - ai-integration
category: guide
---

# Tool Calling

> Enable AI models to use external functions and services by defining tool schemas or connecting to Model Context Protocol (MCP) servers. This allows AI to interact with databases, APIs, file systems, and more.

## Function Calling with Custom Tools

Enable AI models to use external functions by defining tool schemas. Models can then call these functions automatically based on user requests.

```go  theme={null}
// Define a tool for the calculator
calculatorTool := schemas.ChatTool{
	Type: schemas.ChatToolTypeFunction,
	Function: &schemas.ChatToolFunction{
		Name:        "calculator",
		Description: schemas.Ptr("A calculator tool"),
		Parameters: &schemas.ToolFunctionParameters{
			Type: "object",
			Properties: map[string]interface{}{
				"operation": map[string]interface{}{
					"type":        "string",
					"description": "The operation to perform",
					"enum":        []string{"add", "subtract", "multiply", "divide"},
				},
				"a": map[string]interface{}{
					"type":        "number",
					"description": "The first number",
				},
				"b": map[string]interface{}{
					"type":        "number",
					"description": "The second number",
				},
			},
			Required: []string{"operation", "a", "b"},
		},
	},
}

response, err := client.ChatCompletionRequest(context.Background(), &schemas.BifrostChatRequest{
	Provider: schemas.OpenAI,
	Model:    "gpt-4o-mini",
	Input: []schemas.ChatMessage{
		{
			Role: schemas.ChatMessageRoleUser,
			Content: &schemas.ChatMessageContent{
				ContentStr: schemas.Ptr("What is 2+2? Use the calculator tool."),
			},
		},
	},
	Params: &schemas.ChatParameters{
		Tools: []schemas.ChatTool{calculatorTool},
	},
})

if err != nil {
	panic(err)
}

if response.Choices[0].Message.ChatAssistantMessage != nil && response.Choices[0].Message.ChatAssistantMessage.ToolCalls != nil {
	for _, toolCall := range response.Choices[0].Message.ChatAssistantMessage.ToolCalls {
		fmt.Printf("Tool call in response - %s: %s\n", *toolCall.ID, *toolCall.Function.Name)
		fmt.Printf("Tool call arguments - %s\n", toolCall.Function.Arguments)
	}
}
```

## Connecting to MCP Servers

Connect to Model Context Protocol (MCP) servers to give AI models access to external tools and services without manually defining each function.

```go  theme={null}
client, initErr := bifrost.Init(context.Background(), schemas.BifrostConfig{
	Account: &MyAccount{},
	MCPConfig: &schemas.MCPConfig{
		ClientConfigs: []schemas.MCPClientConfig{
			// Sample youtube-mcp server
			{
				Name:             "youtube-mcp",
				ConnectionType:   schemas.MCPConnectionTypeHTTP,
				ConnectionString: schemas.Ptr("http://your-youtube-mcp-url"),
				ToolsToExecute: []string{"*"}, // Allow all tools from this client
			},
		},
	},
})
if initErr != nil {
	panic(initErr)
}
defer client.Shutdown()

response, err := client.ChatCompletionRequest(context.Background(), &schemas.BifrostChatRequest{
	Provider: schemas.OpenAI,
	Model:    "gpt-4o-mini",
	Input: []schemas.ChatMessage{
		{
			Role: schemas.ChatMessageRoleUser,
			Content: &schemas.ChatMessageContent{
				ContentStr: schemas.Ptr("What do you see when you search for 'bifrost' on youtube?"),
			},
		},
	},
})

if err != nil {
	panic(err)
}

if response.Choices[0].Message.ChatAssistantMessage != nil && response.Choices[0].Message.ChatAssistantMessage.ToolCalls != nil {
	for _, toolCall := range response.Choices[0].Message.ChatAssistantMessage.ToolCalls {
		fmt.Printf("Tool call in response - %s: %s\n", *toolCall.ID, *toolCall.Function.Name)
		fmt.Printf("Tool call arguments - %s\n", toolCall.Function.Arguments)
	}
}
```

Read more about MCP connections and in-house tool registration via local MCP server in the [MCP Features](../../mcp/overview) section.

## Advanced Tool Examples

### Weather API Tool

```go  theme={null}
weatherTool := schemas.ChatTool{
	Type: schemas.ChatToolTypeFunction,
	Function: &schemas.ChatToolFunction{
		Name:        "get_weather",
		Description: schemas.Ptr("Get the current weather for a location"),
		Parameters: &schemas.ToolFunctionParameters{
			Type: "object",
			Properties: map[string]interface{}{
				"location": map[string]interface{}{
					"type":        "string",
					"description": "The city and state, e.g. San Francisco, CA",
				},
				"unit": map[string]interface{}{
					"type":        "string",
					"description": "Temperature unit",
					"enum":        []string{"celsius", "fahrenheit"},
				},
			},
			Required: []string{"location"},
		},
	},
}
```

### Database Query Tool

```go  theme={null}
databaseTool := schemas.ChatTool{
	Type: schemas.ChatToolTypeFunction,
	Function: &schemas.ChatToolFunction{
		Name:        "query_database",
		Description: schemas.Ptr("Execute a SQL query on the customer database"),
		Parameters: &schemas.ToolFunctionParameters{
			Type: "object",
			Properties: map[string]interface{}{
				"query": map[string]interface{}{
					"type":        "string",
					"description": "The SQL query to execute",
				},
				"table": map[string]interface{}{
					"type":        "string",
					"description": "The table to query",
					"enum":        []string{"customers", "orders", "products"},
				},
			},
			Required: []string{"query", "table"},
		},
	},
}
```

### File System Tool

```go  theme={null}
fileSystemTool := schemas.ChatTool{
	Type: schemas.ChatToolTypeFunction,
	Function: &schemas.ChatToolFunction{
		Name:        "read_file",
		Description: schemas.Ptr("Read the contents of a file"),
		Parameters: &schemas.ToolFunctionParameters{
			Type: "object",
			Properties: map[string]interface{}{
				"path": map[string]interface{}{
					"type":        "string",
					"description": "The file path to read",
				},
				"encoding": map[string]interface{}{
					"type":        "string",
					"description": "File encoding",
					"enum":        []string{"utf-8", "ascii", "base64"},
					"default":     "utf-8",
				},
			},
			Required: []string{"path"},
		},
	},
}
```

## Multiple Tool Support

Use multiple tools in a single request:

```go  theme={null}
response, err := client.ChatCompletionRequest(context.Background(), &schemas.BifrostChatRequest{
	Provider: schemas.OpenAI,
	Model:    "gpt-4o-mini",
	Input: []schemas.ChatMessage{
		{
			Role: schemas.ChatMessageRoleUser,
			Content: &schemas.ChatMessageContent{
				ContentStr: schemas.Ptr("What's the weather in New York and calculate 15% tip for a $50 bill?"),
			},
		},
	},
	Params: &schemas.ChatParameters{
		Tools: []schemas.ChatTool{weatherTool, calculatorTool},
		ToolChoice: &schemas.ChatToolChoice{
			ChatToolChoiceStr: schemas.Ptr("auto"), // Let AI decide which tools to use
		},
	},
})
```

## Tool Choice Options

Control how the AI uses tools:

```go  theme={null}
// Force use of a specific tool
Params: &schemas.ChatParameters{
	Tools: []schemas.ChatTool{calculatorTool},
	ToolChoice: &schemas.ChatToolChoice{
		ChatToolChoiceStruct: &schemas.ChatToolChoiceStruct{
			Type: schemas.ChatToolChoiceTypeFunction,
			Function: &schemas.ChatToolChoiceFunction{
				Name: "calculator",
			},
		},
	},
}

// Let AI decide automatically
Params: &schemas.ChatParameters{
	Tools: []schemas.ChatTool{calculatorTool, weatherTool},
	ToolChoice: &schemas.ChatToolChoice{
		ChatToolChoiceStr: schemas.Ptr("auto"),
	},
}

// Disable tool usage
Params: &schemas.ChatParameters{
	Tools: []schemas.ChatTool{calculatorTool},
	ToolChoice: &schemas.ChatToolChoice{
		ChatToolChoiceStr: schemas.Ptr("none"),
	},
}
```

## Next Steps

* **[Multimodal AI](./multimodal)** - Process images, audio, and multimedia content
* **[Streaming Responses](./streaming)** - Real-time response generation
* **[Provider Configuration](./provider-configuration)** - Multiple providers for redundancy
* **[MCP Features](../../mcp/overview)** - Advanced MCP server management


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt