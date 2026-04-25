---
title: '`config.ts` File'
url: https://lmstudio.ai/docs/typescript/plugins/custom-configuration/config-ts
source: sitemap
fetched_at: 2026-04-07T21:29:07.511539745-03:00
rendered_js: false
word_count: 0
summary: This code demonstrates how to programmatically create and define custom configuration schematics using the createConfigSchematics function.
tags:
    - config-schematics
    - sdk-usage
    - field-definition
    - typescript
    - programming
category: reference
---

```
import { createConfigSchematics } from "@lmstudio/sdk";

export const configSchematics = createConfigSchematics()
  .field(
    "myCustomField", // The key of the field.
    "numeric", // Type of the field.
    // Options for the field. Different field types will have different options.
    {
      displayName: "My Custom Field",
      hint: "This is my custom field. Doesn't do anything special.",
      slider: { min: 0, max: 100, step: 1 }, // Add a slider to the field.
    },
    80, // Default Value
  )
  // You can add more fields by chaining the field method.
  // For example:
  //   .field("anotherField", ...)
  .build();

export const globalConfigSchematics = createConfigSchematics()
  .field(
    "myGlobalCustomField", // The key of the field.
    "string",
    {
      displayName: "My Global Custom Field",
      hint: "This is my global custom field. Doesn't do anything special.",
    },
    "default value", // Default Value
  )
  // You can add more fields by chaining the field method.
  // For example:
  //  .field("anotherGlobalField", ...)
  .build();
```