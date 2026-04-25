---
title: Single Tool
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider/single-tool
source: sitemap
fetched_at: 2026-04-07T21:32:06.853906588-03:00
rendered_js: false
word_count: 166
summary: This document explains the necessary steps for setting up a tools provider within a plugin, detailing how to define a specific tool like 'create_file' and then register that provider in the plugin's main entry file.
tags:
    - tools-provider
    - plugin-development
    - tool-definition
    - typescript
    - llm-integration
category: tutorial
---

To setup a tools provider, first create the a file `toolsProvider.ts` in your plugin's `src` directory:

The above tools provider defines a single tool called `create_file` that allows the model to create a file with a specified name and content inside the working directory. You can learn more about defining tools in [Tool Definition](https://lmstudio.ai/docs/typescript/plugins/agent/tools).

Then register the tools provider in your plugin's `index.ts`:

Now, you can try to ask the LLM to create a file, and it should be able to do so using the tool you just created.

## Tips[](#tips "Link to 'Tips'")

- **Use Descriptive Names and Descriptions**: When defining tools, use descriptive names and detailed descriptions. This helps the model understand when and how to use each tool effectively.
- **Return Errors as Strings**: Sometimes, the model may make a mistake when calling a tool. In such cases, you can return an error message as a string. In most cases, the model will try to correct itself and call the tool again with the correct parameters.