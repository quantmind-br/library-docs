---
title: Custom Configuration
url: https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessor/custom-configuration
source: sitemap
fetched_at: 2026-04-07T21:32:19.994905972-03:00
rendered_js: false
word_count: 0
summary: This code snippet demonstrates how to define and build configuration schematics for an SDK, specifically adding fields for 'Special Instructions' and a 'Trigger Word'.
tags:
    - sdk-configuration
    - schema-definition
    - api-building
    - typescript
category: reference
---

```
import { createConfigSchematics } from "@lmstudio/sdk";
export const configSchematics = createConfigSchematics()
  .field(
    "specialInstructions",
    "string",
    {
      displayName: "Special Instructions",
      subtitle: "Special instructions to be injected when the trigger word is found.",
    },
    "Here is some default special instructions.",
  )
  .field(
    "triggerWord",
    "string",
    {
      displayName: "Trigger Word",
      subtitle: "The word that will trigger the special instructions.",
    },
    "@init",
  )
  .build();
```