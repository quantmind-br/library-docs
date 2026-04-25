---
title: Handling Aborts
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider/handling-aborts
source: sitemap
fetched_at: 2026-04-07T21:32:14.144671692-03:00
rendered_js: false
word_count: 36
summary: This code demonstrates how to define and register custom tools, specifically a 'fetch' tool, within an SDK controller.
tags:
    - sdk-implementation
    - tool-definition
    - async-function
    - api-integration
category: reference
---

```
import { tool, Tool, ToolsProviderController } from "@lmstudio/sdk";
import { z } from "zod";

export async function toolsProvider(ctl: ToolsProviderController) {
  const tools: Tool[] = [];

  const fetchTool = tool({
    name: `fetch`,
    description: "Fetch a URL using GET method.",
    parameters: { url: z.string() },
    implementation: async ({ url }, { signal }) => {
      const response = await fetch(url, {
        method: "GET",
        signal, // <-- Here, we pass the signal to fetch to allow cancellation
      });
      if (!response.ok) {
        return `Error: Failed to fetch ${url}: ${response.statusText}`;
      }
      const data = await response.text();
      return {
        status: response.status,
        headers: Object.fromEntries(response.headers.entries()),
        data: data.substring(0, 1000), // Limit to 1000 characters
      };
    },
  });
  tools.push(fetchTool);

  return tools;
}
```