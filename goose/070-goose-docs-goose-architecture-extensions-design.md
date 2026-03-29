---
title: Extensions Design | goose
url: https://block.github.io/goose/docs/goose-architecture/extensions-design
source: github_pages
fetched_at: 2026-01-22T22:13:28.48690887-03:00
rendered_js: true
word_count: 306
summary: This document outlines the design and implementation of the goose Extensions framework, which enables AI agents to interact with external tools through a standardized Rust-based interface.
tags:
    - goose-ai
    - extensions-framework
    - ai-agents
    - tool-calling
    - rust-development
    - software-architecture
category: guide
---

This document describes the design and implementation of the [Extensions framework](https://block.github.io/goose/docs/getting-started/using-extensions) in goose, which enables AI agents to interact with different extensions through a unified tool-based interface.

## Core Concepts[​](#core-concepts "Direct link to Core Concepts")

### Extension[​](#extension "Direct link to Extension")

An Extension represents any component that can be operated by an AI agent. Extensions expose their capabilities through Tools and maintain their own state. The core interface is defined by the `Extension` trait:

```
#[async_trait]
pubtraitExtension:Send+Sync{
fnname(&self)->&str;
fndescription(&self)->&str;
fninstructions(&self)->&str;
fntools(&self)->&[Tool];
asyncfnstatus(&self)->AnyhowResult<HashMap<String,Value>>;
asyncfncall_tool(&self, tool_name:&str, parameters:HashMap<String,Value>)->ToolResult<Value>;
}
```

### Tools[​](#tools "Direct link to Tools")

Tools are the primary way Extensions expose functionality to agents. Each tool has:

- A name
- A description
- A set of parameters
- An implementation that executes the tool's functionality

A tool must take a Value and return an `AgentResult<Value>` (it must also be async). This is what makes it compatible with the tool calling framework from the agent.

```
asyncfnecho(&self, params:Value)->AgentResult<Value>
```

## Architecture[​](#architecture "Direct link to Architecture")

### Component Overview[​](#component-overview "Direct link to Component Overview")

1. **Extension Trait**: The core interface that all extensions must implement
2. **Error Handling**: Specialized error types for tool execution
3. **Proc Macros**: Simplify tool definition and registration \[*not yet implemented*]

### Error Handling[​](#error-handling "Direct link to Error Handling")

The system uses two main error types:

- `ErrorData`: Specific errors related to tool execution
- `anyhow::Error`: General purpose errors for extension status and other operations

This split allows precise error handling for tool execution while maintaining flexibility for general extension operations.

## Best Practices[​](#best-practices "Direct link to Best Practices")

### Tool Design[​](#tool-design "Direct link to Tool Design")

1. **Clear Names**: Use clear, action-oriented names for tools (e.g., "create\_user" not "user")
2. **Descriptive Parameters**: Each parameter should have a clear description
3. **Error Handling**: Return specific errors when possible, the errors become "prompts"
4. **State Management**: Be explicit about state modifications

### Extension Implementation[​](#extension-implementation "Direct link to Extension Implementation")

1. **State Encapsulation**: Keep extension state private and controlled
2. **Error Propagation**: Use `?` operator with `ErrorData` for tool execution
3. **Status Clarity**: Provide clear, structured status information
4. **Documentation**: Document all tools and their effects

### Example Implementation[​](#example-implementation "Direct link to Example Implementation")

Here's a complete example of a simple extension:

```
usegoose_macros::tool;

structFileSystem{
    registry:ToolRegistry,
    root_path:PathBuf,
}

implFileSystem{
#[tool(
        name = "read_file",
        description = "Read contents of a file"
    )]
asyncfnread_file(&self, path:String)->ToolResult<Value>{
let full_path =self.root_path.join(path);
let content =tokio::fs::read_to_string(full_path)
.await
.map_err(|e|ErrorData{
                code:ErrorCode::INTERNAL_ERROR,
                message:Cow::from(e.to_string(),
                data:None,
}))?;

Ok(json!({"content": content }))
}
}

#[async_trait]
implExtensionforFileSystem{
// ... implement trait methods ...
}
```

## Testing[​](#testing "Direct link to Testing")

Extensions should be tested at multiple levels:

1. Unit tests for individual tools
2. Integration tests for extension behavior
3. Property tests for tool invariants

Example test:

```
#[tokio::test]
asyncfntest_echo_tool(){
let extension =TestExtension::new();
let result = extension.call_tool(
"echo",
hashmap!{"message"=>json!("hello")}
).await;

assert_eq!(result.unwrap(),json!({"response":"hello"}));
}
```