---
title: Multiple Tools
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider/multiple-tools
source: sitemap
fetched_at: 2026-04-07T21:32:08.86437345-03:00
rendered_js: false
word_count: 72
summary: This code snippet demonstrates how to define and register custom, asynchronous tooling functions within a provided controller for an AI system.
tags:
    - tool-definition
    - sdk-usage
    - file-system-interaction
    - async-operations
category: api
---

```
import { tool, Tool, ToolsProviderController } from "@lmstudio/sdk";
import { z } from "zod";
import { existsSync } from "fs";
import { readFile, writeFile } from "fs/promises";
import { join } from "path";

export async function toolsProvider(ctl: ToolsProviderController) {
  const tools: Tool[] = [];

  const createFileTool = tool({
    name: `create_file`,
    description: "Create a file with the given name and content.",
    parameters: { file_name: z.string(), content: z.string() },
    implementation: async ({ file_name, content }) => {
      const filePath = join(ctl.getWorkingDirectory(), file_name);
      if (existsSync(filePath)) {
        return "Error: File already exists.";
      }
      await writeFile(filePath, content, "utf-8");
      return "File created.";
    },
  });
  tools.push(createFileTool); // First tool

  const readFileTool = tool({
    name: `read_file`,
    description: "Read the content of a file with the given name.",
    parameters: { file_name: z.string() },
    implementation: async ({ file_name }) => {
      const filePath = join(ctl.getWorkingDirectory(), file_name);
      if (!existsSync(filePath)) {
        return "Error: File does not exist.";
      }
      const content = await readFile(filePath, "utf-8");
      return content;
    },
  });
  tools.push(readFileTool); // Second tool

  return tools; // Return the tools array
}
```