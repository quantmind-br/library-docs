---
title: Introduction to Plugins
url: https://lmstudio.ai/docs/typescript/plugins
source: sitemap
fetched_at: 2026-04-07T21:32:00.110983042-03:00
rendered_js: false
word_count: 235
summary: This document guides developers on how to build and manage plugins for LM Studio, detailing the necessary setup, development workflow, and advanced features like tools providers and prompt preprocessors.
tags:
    - plugins
    - javascript
    - typescript
    - development-workflow
    - node-js
    - extension-building
category: tutorial
---

Plugins extend LM Studio's functionality by providing "hook functions" that execute at specific points during operation.

Plugins are currently written in JavaScript/TypeScript and run on Node.js v22.21.1. Python support is in development.

## Getting Started[](#getting-started "Link to 'Getting Started'")

LM Studio includes Node.js, so no separate installation is required.

### Create a new plugin[](#create-a-new-plugin)

To create a new plugin, navigate to LM Studio... \[TO BE CONTINUED]

### Run a plugin in development mode[](#run-a-plugin-in-development-mode)

Once you've created a plugin, run this command in the plugin directory to start development mode:


Your plugin will appear in LM Studio's plugin list. Development mode automatically rebuilds and reloads your plugin when you make code changes.

You only need `lms dev` during development. When the plugin is installed, LM Studio automatically runs them as needed. Learn more about distributing and installing plugins in the [Sharing Plugins](https://lmstudio.ai/docs/typescript/plugins/publish-plugins) section.

## Next Steps[](#next-steps "Link to 'Next Steps'")

- [Tools Providers](https://lmstudio.ai/docs/typescript/plugins/tools-provider)
  
  Give models extra capabilities by creating tools they can use during generation, like accessing external APIs or performing calculations.
- [Prompt Preprocessors](https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessor)
  
  Modify user input before it reaches the model - handle file uploads, inject context, or transform queries.
- [Generators](https://lmstudio.ai/docs/typescript/plugins/generator)
  
  Create custom text generation sources that replace the local model, perfect for online model adapters.
- [Custom Configurations](https://lmstudio.ai/docs/typescript/plugins/custom-configuration)
  
  Add configuration UIs so users can customize your plugin's behavior.
- [Third-Party Dependencies](https://lmstudio.ai/docs/typescript/plugins/dependencies)
  
  Use npm packages to leverage existing libraries in your plugins.
- [Sharing Plugins](https://lmstudio.ai/docs/typescript/plugins/publish-plugins)
  
  Package and share your plugins with the community.