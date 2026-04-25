---
title: Custom Configuration
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider/custom-configuration
source: sitemap
fetched_at: 2026-04-07T21:32:10.350630621-03:00
rendered_js: false
word_count: 69
summary: This code provides a function to define and return an array of available tools for a controller, specifically demonstrating how to implement a file creation tool using local file system operations.
tags:
    - tool-implementation
    - file-system-operations
    - sdk-integration
    - async-functions
category: reference
---

```
import { tool, Tool, ToolsProviderController } from "@lmstudio/sdk";
import { existsSync } from "fs";
import { mkdir, writeFile } from "fs/promises";
import { join } from "path";
import { z } from "zod";
import { configSchematics } from "./config";

export async function toolsProvider(ctl: ToolsProviderController) {
  const tools: Tool[] = [];

  const createFileTool = tool({
    name: `create_file`,
    description: "Create a file with the given name and content.",
    parameters: { file_name: z.string(), content: z.string() },
    implementation: async ({ file_name, content }) => {
      // Read the config field
      const folderName = ctl.getPluginConfig(configSchematics).get("folderName");
      const folderPath = join(ctl.getWorkingDirectory(), folderName);

      // Ensure the folder exists
      await mkdir(folderPath, { recursive: true });

      // Create the file
      const filePath = join(folderPath, file_name);
      if (existsSync(filePath)) {
        return "Error: File already exists.";
      }
      await writeFile(filePath, content, "utf-8");
      return "File created.";
    },
  });
  tools.push(createFileTool); // First tool

  return tools; // Return the tools array
}
```