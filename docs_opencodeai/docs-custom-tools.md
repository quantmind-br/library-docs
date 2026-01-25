---
title: Custom Tools
url: https://opencode.ai/docs/custom-tools
source: sitemap
fetched_at: 2026-01-24T22:47:49.871622457-03:00
rendered_js: false
word_count: 302
---

Create tools the LLM can call in opencode.

Custom tools are functions you create that the LLM can call during conversations. They work alongside opencode’s [built-in tools](https://opencode.ai/docs/tools) like `read`, `write`, and `bash`.

* * *

Tools are defined as **TypeScript** or **JavaScript** files. However, the tool definition can invoke scripts written in **any language** — TypeScript or JavaScript is only used for the tool definition itself.

* * *

### [Location](#location)

They can be defined:

- Locally by placing them in the `.opencode/tools/` directory of your project.
- Or globally, by placing them in `~/.config/opencode/tools/`.

* * *

### [Structure](#structure)

The easiest way to create tools is using the `tool()` helper which provides type-safety and validation.

```

import { tool } from"@opencode-ai/plugin"
exportdefaulttool({
description: "Query the project database",
args: {
query: tool.schema.string().describe("SQL query to execute"),
},
asyncexecute(args) {
// Your database logic here
return`Executed query: ${args.query}`
},
})
```

The **filename** becomes the **tool name**. The above creates a `database` tool.

* * *

#### [Multiple tools per file](#multiple-tools-per-file)

You can also export multiple tools from a single file. Each export becomes **a separate tool** with the name **`<filename>_<exportname>`** :

```

import { tool } from"@opencode-ai/plugin"
exportconstadd=tool({
description: "Add two numbers",
args: {
a: tool.schema.number().describe("First number"),
b: tool.schema.number().describe("Second number"),
},
asyncexecute(args) {
return args.a + args.b
},
})
exportconstmultiply=tool({
description: "Multiply two numbers",
args: {
a: tool.schema.number().describe("First number"),
b: tool.schema.number().describe("Second number"),
},
asyncexecute(args) {
return args.a * args.b
},
})
```

This creates two tools: `math_add` and `math_multiply`.

* * *

### [Arguments](#arguments)

You can use `tool.schema`, which is just [Zod](https://zod.dev), to define argument types.

```

args: {
query: tool.schema.string().describe("SQL query to execute")
}
```

You can also import [Zod](https://zod.dev) directly and return a plain object:

```

import { z } from"zod"
exportdefault {
description: "Tool description",
args: {
param: z.string().describe("Parameter description"),
},
asyncexecute(args, context) {
// Tool implementation
return"result"
},
}
```

* * *

### [Context](#context)

Tools receive context about the current session:

```

import { tool } from"@opencode-ai/plugin"
exportdefaulttool({
description: "Get project information",
args: {},
asyncexecute(args, context) {
// Access context information
const { agent, sessionID, messageID } = context
return`Agent: ${agent}, Session: ${sessionID}, Message: ${messageID}`
},
})
```

* * *

## [Examples](#examples)

### [Write a tool in Python](#write-a-tool-in-python)

You can write your tools in any language you want. Here’s an example that adds two numbers using Python.

First, create the tool as a Python script:

```

import sys
a =int(sys.argv[1])
b =int(sys.argv[2])
print(a + b)
```

Then create the tool definition that invokes it:

```

import { tool } from"@opencode-ai/plugin"
exportdefaulttool({
description: "Add two numbers using Python",
args: {
a: tool.schema.number().describe("First number"),
b: tool.schema.number().describe("Second number"),
},
asyncexecute(args) {
constresult=await Bun.$`python3 .opencode/tools/add.py ${args.a} ${args.b}`.text()
return result.trim()
},
})
```

Here we are using the [`Bun.$`](https://bun.com/docs/runtime/shell) utility to run the Python script.