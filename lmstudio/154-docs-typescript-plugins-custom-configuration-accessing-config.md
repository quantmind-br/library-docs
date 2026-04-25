---
title: Accessing Configuration
url: https://lmstudio.ai/docs/typescript/plugins/custom-configuration/accessing-config
source: sitemap
fetched_at: 2026-04-07T21:29:05.699726219-03:00
rendered_js: false
word_count: 58
summary: This code demonstrates how to access both plugin-specific and global configurations using the PreprocessorController within a TypeScript environment.
tags:
    - configuration
    - typescript
    - plugin-config
    - global-settings
    - sdk-usage
category: reference
---

You can access the configuration using the method `ctl.getPluginConfig(configSchematics)` and `ctl.getGlobalConfig(globalConfigSchematics)` respectively.

src/promptPreprocessor.ts

```
import { type PreprocessorController, type ChatMessage } from "@lmstudio/sdk";
import { configSchematics } from "./config";

export async function preprocess(ctl: PreprocessorController, userMessage: ChatMessage) {
  const pluginConfig = ctl.getPluginConfig(configSchematics);
  const myCustomField = pluginConfig.get("myCustomField");

  const globalPluginConfig = ctl.getGlobalPluginConfig(configSchematics);
  const globalMyCustomField = globalPluginConfig.get("myCustomField");

  return (
    `${userMessage.getText()},` +
    `myCustomField: ${myCustomField}, ` +
    `globalMyCustomField: ${globalMyCustomField}`
  );
}
```